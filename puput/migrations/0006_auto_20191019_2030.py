# Generated by Django 2.2.4 on 2019-10-20 00:30

from django.db import migrations
import wagtailmarkdown.fields


class Migration(migrations.Migration):

    dependencies = [
        ('puput', '0005_blogpage_main_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrypage',
            name='body',
            field=wagtailmarkdown.fields.MarkdownField(blank=True),
        ),
    ]
