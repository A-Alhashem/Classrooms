# Generated by Django 2.0.6 on 2018-12-16 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0008_auto_20181211_2104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['name', 'exam_grade']},
        ),
    ]