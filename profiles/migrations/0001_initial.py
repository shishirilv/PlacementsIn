# Generated by Django 3.0 on 2022-06-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobtitle', models.CharField(max_length=120)),
                ('cgpa', models.DecimalField(decimal_places=2, max_digits=1000)),
                ('major', models.CharField(max_length=120)),
                ('mini', models.CharField(max_length=120)),
                ('minor', models.CharField(max_length=120)),
                ('internships', models.TextField(blank=True, null=True, default=None)),
                ('special_courses', models.TextField(blank=True, null=True, default=None)),
                ('email', models.EmailField(max_length=250)),
                ('LinkedIn', models.URLField()),
            ],
        ),
    ]
