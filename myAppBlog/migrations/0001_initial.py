# Generated by Django 5.0.2 on 2024-02-22 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('idPost', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('contenido', models.TextField()),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'db_table': 'Posts',
            },
        ),
    ]
