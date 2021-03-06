# Generated by Django 3.2 on 2022-02-12 23:28

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='picture_url',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='group',
            name='year_of_borth',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=django_quill.fields.QuillField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=django_quill.fields.QuillField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=django_quill.fields.QuillField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='group',
            name='text',
            field=django_quill.fields.QuillField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='newsbox',
            name='content',
            field=django_quill.fields.QuillField(blank=True, max_length=10000),
        ),
    ]
