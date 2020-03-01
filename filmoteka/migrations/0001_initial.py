# Generated by Django 3.0.3 on 2020-03-01 16:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('plot', models.TextField(blank=True, null=True, verbose_name='Plot')),
                ('release_date', models.DateField(default=django.utils.timezone.now, help_text='Please use the following format: <em>YYYY-MM-DD</em>.', verbose_name='Release date')),
                ('runtime', models.IntegerField(blank=True, verbose_name='Runtime')),
                ('rate', models.FloatField(default=5.0, verbose_name='Rate')),
                ('poster', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Poster')),
            ],
            options={
                'ordering': ['-release_date', 'title'],
            },
        ),
    ]