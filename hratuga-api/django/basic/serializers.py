# serializers.py
from rest_framework import serializers
from .models import *


class GroupSerializer(serializers.ModelSerializer):
    text_html = serializers.SerializerMethodField()
    class Meta:
        model = Group
        fields = ('id', 'name', 'tech_name', 'description', 'age_group', 'is_searching', 'weekday', 'time_start', 'time_end', 'text_html', 'group_leader', 'picture_url', 'year_of_borth')

    def get_text_html(self, obj):
        return obj.text.html

class EventSerializer(serializers.ModelSerializer):
    description_html = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = ('id', 'title', 'organizer', 'responsible_person', 'description_html', 'start_date',
                  'end_date', 'deadline_date', 'start_place', 'end_place', 'costs', 'groups', 'is_public', 'in_heim')

    def get_description_html(self, obj):
        return obj.description.html


class FaqSerializer(serializers.ModelSerializer):
    question_html = serializers.SerializerMethodField()
    answer_html = serializers.SerializerMethodField()

    class Meta:
        model = Faq
        fields = ('id', 'sorting', 'question_html', 'answer_html')

    def get_question_html(self, obj):
        return obj.question.html

    def get_answer_html(self, obj):
        return obj.question.html


class PackingListTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingListTag
        fields = '__all__'


class PackingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingList
        fields = '__all__'


class PackingListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackingListItem
        fields = '__all__'


class NewsBoxSerializer(serializers.ModelSerializer):
    content_html = serializers.SerializerMethodField()
    class Meta:
        model = NewsBox
        fields = ('id', 'name', 'content_html', 'valid_from', 'valid_till', 'priority')

    def get_content_html(self, obj):
            return obj.content.html
