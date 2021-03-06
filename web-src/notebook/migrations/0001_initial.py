# Generated by Django 2.1.5 on 2019-01-25 22:00

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteBook',
            fields=[
                ('id', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=150)),
                ('description', ckeditor.fields.RichTextField(null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('updated_at', models.DateTimeField(null=True)),
                ('private', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Notebook',
                'verbose_name_plural': 'Notebooks',
                'db_table': 'notebooks',
            },
        ),
    ]
