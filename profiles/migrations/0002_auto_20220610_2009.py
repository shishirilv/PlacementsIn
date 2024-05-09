# Generated by Django 3.0 on 2022-06-10 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='branch',
            field=models.CharField(default='Some branch', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='name',
            field=models.CharField(default='Some name', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='org',
            field=models.CharField(default='some company', max_length=120),
        ),
        migrations.AddField(
            model_name='profiles',
            name='package_LPA',
            field=models.DecimalField(decimal_places=1, default=5, max_digits=1000),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='LinkedIn',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='internships',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='special_courses',
            field=models.TextField(blank=True, null=True),
        ),
    ]
