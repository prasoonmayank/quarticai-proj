# Generated by Django 2.1.2 on 2018-11-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_signal', models.CharField(max_length=10)),
                ('rule_vartype', models.CharField(max_length=8)),
                ('rule_condition', models.CharField(max_length=200)),
            ],
        ),
    ]
