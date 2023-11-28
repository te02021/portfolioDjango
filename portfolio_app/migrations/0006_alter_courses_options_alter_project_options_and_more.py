# Generated by Django 4.2.4 on 2023-11-28 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0005_works'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterModelOptions(
            name='savecontactmessage',
            options={'verbose_name': 'Save Contact Message', 'verbose_name_plural': 'Save Contact Messages'},
        ),
        migrations.AlterModelOptions(
            name='studies',
            options={'verbose_name': 'Studie', 'verbose_name_plural': 'Studies'},
        ),
        migrations.AlterModelOptions(
            name='works',
            options={'verbose_name': 'Work', 'verbose_name_plural': 'Works'},
        ),
        migrations.AlterField(
            model_name='works',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]