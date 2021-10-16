# Generated by Django 3.2.8 on 2021-10-08 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_one', models.CharField(max_length=30)),
                ('option_two', models.CharField(max_length=30)),
                ('option_three', models.CharField(max_length=30)),
                ('count_one', models.IntegerField(default=0)),
                ('count_two', models.IntegerField(default=0)),
                ('count_three', models.IntegerField(default=0)),
            ],
        ),
    ]