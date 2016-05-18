from django.core.urlresolvers import reverse

def url_to_edit_object(model_name, object):
    url = None
    if object:
        url = reverse('admin:evaluation_%s_change' % model_name, args=[object.id])
    return url

def url_new_object(model_name):
    url = reverse('admin:evaluation_%s_add' % model_name)
    return url