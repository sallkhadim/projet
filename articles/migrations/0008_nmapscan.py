# Generated by Django 2.1.1 on 2018-10-04 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='NmapScan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.CharField(max_length=2048)),
            ],
        ),
    ]
