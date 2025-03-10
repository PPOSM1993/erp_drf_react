# Generated by Django 5.1.6 on 2025-03-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_group_grouppermission_usergroups'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GroupPermission',
            new_name='GroupsPermissions',
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=85),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
