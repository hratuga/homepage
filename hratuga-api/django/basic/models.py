from queue import PriorityQueue
from django.db import models

from django_quill.fields import QuillField

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class Group(TimeStampMixin):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    name = models.CharField(max_length=60)
    tech_name = models.CharField(max_length=60)
    description = models.CharField(max_length=200, blank=True)
    age_group = models.IntegerField(null=True, blank=True)
    is_searching = models.BooleanField(default=True)
    weekday = models.CharField(max_length=10)
    time_start = models.CharField(max_length=10)
    time_end = models.CharField(max_length=10)
    text = QuillField(max_length=1000, blank=True)
    group_leader = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class Event(TimeStampMixin):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    title = models.CharField(max_length=60)
    organizer = models.CharField(max_length=30)
    responsible_person = models.CharField(max_length=30)
    description = QuillField(max_length=1000, blank=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    deadline_date = models.DateTimeField(blank=True, null=True)
    start_place = models.CharField(max_length=30)
    end_place = models.CharField(max_length=30)
    costs = models.FloatField(blank=True, null=True)
    groups = models.ManyToManyField(Group, blank=True)
    is_public = models.BooleanField(default=1)
    in_heim = models.BooleanField(default=1)

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.__str__()


class Faq(TimeStampMixin):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    question = QuillField(max_length=1000, blank=True)
    answer = QuillField(max_length=1000, blank=True)
    sorting = models.IntegerField(
        blank=False, auto_created=True, unique=True, null=True)

    def __str__(self):
        return str(self.sorting)

    def __repr__(self):
        return self.__str__()


class PackingListTag(TimeStampMixin):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class PackingList(TimeStampMixin):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)
    packing_list_tags = models.ManyToManyField(PackingListTag, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class PackingListItem(TimeStampMixin):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)
    packing_list_tags = models.ManyToManyField(PackingListTag, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()


class NewsBox(TimeStampMixin):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    name = models.CharField(max_length=60)
    content = QuillField(max_length=1000, blank=True)
    valid_from = models.DateTimeField()
    valid_till = models.DateTimeField()
    priority = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
