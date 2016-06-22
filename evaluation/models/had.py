# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _, pgettext_lazy
from . import BaseEvaluation

class HAD(BaseEvaluation):
    """
    HOSPITAL ANXIETY AND DEPRESSION - had
    """

    # Cuidados pessoais
    HAD_TENSION = (
        (3, _('Most of the time')),
        (2, _('A lot of time')),
        (1, _('From time to time, occasionally')),
        (0, pgettext_lazy('tension', 'Not at all'))
    )
    tension = models.IntegerField(_('I feel tense or "wound up"'), choices=HAD_TENSION)

    HAD_ENJOY = (
        (3, pgettext_lazy('enjoy', 'Hardly at all')),
        (2, _('Only a little')),
        (1, _('Not quite so much')),
        (0, _('Definitely as much'))
    )
    enjoy = models.IntegerField(_('I still enjoy the things I used to enjoy'), choices=HAD_ENJOY)

    HAD_FRIGHTENED = (
        (3, _('Very definitely and quite badly')),
        (2, _('Yes, but not too badly')),
        (1, _('A little, but it doesn\'t worry me')),
        (0, pgettext_lazy('frightened', 'Not at all'))
    )
    frightened = models.IntegerField(_('I get a sort of frightened feeling as if something awful is about to happen'),
                                     choices=HAD_FRIGHTENED)

    HAD_LAUGH = (
        (3, pgettext_lazy('laugh', 'Not at all')),
        (2, _('Definitely not so much now')),
        (1, _('Not quite so much now')),
        (0, _('As much as I always could')),
    )
    laugh = models.IntegerField(_('I can laugh and see the funny side of things'), choices=HAD_LAUGH)

    HAD_WORRY = (
        (3, _('A great deal of the time')),
        (2, _('A lot of the time')),
        (1, _('From time to time, but not too often')),
        (0, _('Only occasionally')),
    )
    worry = models.IntegerField(_('Worrying thoughts go through my mind'), choices=HAD_WORRY)

    HAD_CHEERFUL = (
        (3, pgettext_lazy('cheerful', 'Not at all')),
        (2, _('Not often')),
        (1, _('Sometimes')),
        (0, _('Most of the time')),
    )
    cheerful = models.IntegerField(_('I feel cheerful'), choices=HAD_CHEERFUL)

    HAD_EASE = (
        (3, pgettext_lazy('ease', 'Not at all')),
        (2, _('Not often')),
        (1, _('Usually')),
        (0, _('Definitely')),
    )
    ease = models.IntegerField(_('I can sit at ease and feel relaxed'), choices=HAD_EASE)

    HAD_SLOWED = (
        (3, _('Nearly all the time')),
        (2, _('Very often')),
        (1, _('Sometimes')),
        (0, pgettext_lazy('slowed', 'Not at all')),
    )
    slowed = models.IntegerField(_('I feel as if I am slowed down'), choices=HAD_SLOWED)

    HAD_BUTTERFLIES = (
        (3, _('Very Often')),
        (2, _('Quite Often')),
        (1, _('Occasionally')),
        (0, pgettext_lazy('butterflies', 'Not at all')),
    )
    butterflies = models.IntegerField(_('I get a sort of frightened feeling like \'butterflies\' in the stomach'), choices=HAD_BUTTERFLIES)

    HAD_APPEARANCE = (
        (3, _('Definitely')),
        (2, _('I don\'t take as much care as I should')),
        (1, _('I may not take quite as much care')),
        (0, _('I take just as much care as ever')),
    )
    appearance = models.IntegerField(_('I have lost interest in my appearance'), choices=HAD_APPEARANCE)

    HAD_RESTLESS = (
        (3, _('Very much indeed')),
        (2, _('Quite a lot')),
        (1, _('Not very much')),
        (0, pgettext_lazy('restless', 'Not at all')),
    )
    restless = models.IntegerField(_('I feel restless as I have to be on the move'), choices=HAD_RESTLESS)

    HAD_FORWARD = (
        (3, _('Hardly at all')),
        (2, _('Definitely less than I used to')),
        (1, _('Rather less than I used to')),
        (0, _('As much as I ever did')),
    )
    forward = models.IntegerField(_('I look forward with enjoyment to things'), choices=HAD_FORWARD)

    HAD_PANIC = (
        (3, _('Very often indeed')),
        (2, _('Quite often')),
        (1, _('Not very often')),
        (0, pgettext_lazy('panic', 'Not at all')),
    )
    panic = models.IntegerField(_('I get sudden feelings of panic'), choices=HAD_PANIC)

    HAD_BOOK = (
        (3, _('Very seldom')),
        (2, _('Not often')),
        (1, _('Sometimes')),
        (0, _('Often')),
    )
    book = models.IntegerField(_('I can enjoy a good book or radio or TV program'), choices=HAD_BOOK)

    class Meta:
        verbose_name = _('HAD')
        verbose_name_plural = _('HADs')