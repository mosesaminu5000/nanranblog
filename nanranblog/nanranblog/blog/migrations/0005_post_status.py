# Generated by Django 4.1.2 on 2022-11-04 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_category_options_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('draft', 'Draft')], default='active', max_length=10),
        ),
    ]
