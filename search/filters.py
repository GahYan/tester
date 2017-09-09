from django import forms
from .models import Video

import django_filters


class VideoFilter(django_filters.FilterSet):
    GENDER_CHOICES = (
    (0, 'Straight'),
    (1, 'Lesbian'),
    (2, 'Gay'),
    (3, 'Threesome (FMF)'),
    (4, 'Threesome (MMF)'),)

    MOOD_CHOICES= (
    (0, 'Soft'),
    (1, 'Intense'),
    (2, 'Rough'),)
    TOPIC_CHOICES=(
    (0, 'Normal Romantic Stuff'),
    (1, 'BDSM'),
    (2, 'Toys and Machines'),
    (3, 'Blowjob'),
    (4, 'Anal'),
    (5, 'Female Masturbation'),
    (6, 'Other'),)
    RACE_CHOICES=(
    (0, 'Interacial'),
    (1, 'White'),
    (2, 'Black'),
    (3, 'Asian'),
    (4, 'Latino'),
    (5, 'Other'),
    )
    title = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple,choices=GENDER_CHOICES)
    mood = django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple,choices=MOOD_CHOICES)
    topic = django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple,choices=TOPIC_CHOICES)
    race = django_filters.MultipleChoiceFilter( widget=forms.CheckboxSelectMultiple,choices=RACE_CHOICES)
    class Meta:
        model = Video
        fields = ['title', 'gender','mood', 'topic']
