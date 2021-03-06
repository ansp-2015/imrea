from django.utils.text import capfirst
from django.apps import apps
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import ModelAdmin
# from django.contrib.admin.validation import  validate
from django.contrib.admin.validation import BaseValidator

# get_models returns all the models, but there are
# some which we would like to ignore
# It can be the <app_label> or the <app_label>.<model_name>

IGNORE_MODELS = (
    "sites",
    "sessions.session",
    "admin.logentry",
    "contenttypes.contenttype",
    "reversion.revision",
    "reversion.version",
    "report_builder.displayfield",
    "report_builder.filterfield",
    "reversion.revision",
    "reversion.version",
    "explorer.querylog",
    "evaluation.eegfile",
    "evaluation.baseevaluation",
    "evaluation.bostonaphasiavisualconfrontation",
    "evaluation.bostonaphasiaanimalnaming",
    "evaluation.bostonaphasiaoralsentencereading",
    "evaluation.bostonaphasiasymbolworddisc",
    "evaluation.bostonaphasiawordrecognition",
    "evaluation.bostonaphasiaoralspelling",
    "evaluation.bostonaphasiawordpicturematching",
    "evaluation.bostonaphasiareadingsentences",
    "evaluation.bostonaphasiamechanicswriting",
    "evaluation.bostonaphasiarecallwrittensymbols",
    "evaluation.bostonaphasiadictatedwords",
    "evaluation.bostonaphasiacopypangramphrase",
    "evaluation.bostonaphasiaspellingdictation",
    "evaluation.bostonaphasiawrittenpicturenaming",
    "evaluation.bostonaphasianarrativewriting",
    "evaluation.bostonaphasiasenteceswrittendictation",
)

def app_list(request):
    '''
    Get all models and add them to the context apps variable.
    '''
    user = request.user
    app_dict = {}
    admin_class = ModelAdmin
    for model in apps.get_models():
        # BaseValidator().validate(admin_class, model)
        model_admin = admin_class(model, None)
        app_label = model._meta.app_label
        full_label = "%s.%s" % (app_label, model._meta.model_name)
        if app_label in IGNORE_MODELS or full_label in IGNORE_MODELS:
            continue
        has_module_perms = user.has_module_perms(app_label)
        if has_module_perms:
            perms = model_admin.get_model_perms(request)
            # Check whether user has any perm for this module.
            # If so, add the module to the model_list.
            if True in perms.values():
                model_dict = {
                    'name': capfirst(model._meta.verbose_name_plural),
                    'admin_url': mark_safe('%s/%s/' % (app_label, model.__name__.lower())),
                }
                if app_label in app_dict:
                    app_dict[app_label]['models'].append(model_dict)
                else:
                    app_dict[app_label] = {
                        'name': app_label.title(),
                        'app_url': app_label + '/',
                        'has_module_perms': has_module_perms,
                        'models': [model_dict],
                    }

    # manually adding Explorer SQL report
    app_dict['explorer'] = {
        'name': _('Report Explorer'),
        'app_url': '/explorer',
        'models': [{
            'name': _('Reports'),
            'admin_url': mark_safe('../%s/' % ('explorer')),
        }],
    }

    app_list = app_dict.values()
    app_list.sort(key=lambda x: x['name'])
    for app in app_list:
        app['models'].sort(key=lambda x: x['name'])
    return {'apps': app_list}