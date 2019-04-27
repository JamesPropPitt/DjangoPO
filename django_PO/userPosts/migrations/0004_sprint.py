# Generated by Django 2.1.7 on 2019-04-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userPosts', '0003_auto_20190404_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sprint_Number', models.CharField(choices=[('SprintNo0', 'No Sprint Selected'), ('SprintNo1', 'Sprint 1'), ('SprintNo2', 'Sprint 2'), ('SprintNo3', 'Sprint 3'), ('SprintNo4', 'Sprint 4'), ('SprintNo5', 'Sprint 5')], default='SprintNo0', max_length=9)),
            ],
        ),
    ]
