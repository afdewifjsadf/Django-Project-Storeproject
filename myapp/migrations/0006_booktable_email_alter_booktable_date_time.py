# Generated by Django 4.0 on 2021-12-10 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_booktable_first_name_remove_booktable_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booktable',
            name='email',
            field=models.EmailField(default=8, max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booktable',
            name='date_time',
            field=models.DateTimeField(verbose_name='my date'),
        ),
    ]
