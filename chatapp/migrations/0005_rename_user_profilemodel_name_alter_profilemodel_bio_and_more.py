# Generated by Django 4.1.7 on 2023-04-14 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0004_alter_profilemodel_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilemodel',
            old_name='user',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='bio',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
