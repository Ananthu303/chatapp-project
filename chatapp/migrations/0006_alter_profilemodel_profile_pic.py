# Generated by Django 4.1.7 on 2023-04-14 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0005_rename_user_profilemodel_name_alter_profilemodel_bio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='profile_pic',
            field=models.ImageField(default='gofg_7CJTSER.jpg', null=True, upload_to=''),
        ),
    ]
