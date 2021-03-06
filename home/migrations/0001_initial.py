# Generated by Django 3.0.8 on 2020-08-08 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=200, verbose_name='Название статьи ')),
                ('article_text', models.TextField(verbose_name='текст')),
                ('pub_date', models.DateTimeField(verbose_name='дата')),
                ('img_post', models.ImageField(upload_to='templates/img', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
