# Generated by Django 4.0.3 on 2022-03-02 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=11024)),
                ('subject_groups', models.CharField(max_length=10241)),
                ('research_interests', models.CharField(max_length=11024)),
                ('email', models.CharField(max_length=256)),
                ('pic', models.CharField(max_length=256)),
            ],
        ),
    ]
