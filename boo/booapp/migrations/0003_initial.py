# Generated by Django 4.2 on 2023-06-24 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booapp', '0002_delete_abi'),
    ]

    operations = [
        migrations.CreateModel(
            name='don',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
            ],
            options={
                'db_table': 'don',
            },
        ),
    ]
