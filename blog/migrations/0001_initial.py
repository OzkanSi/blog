# Generated by Django 4.2.4 on 2023-08-24 01:43

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
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('publish_date', models.DateTimeField(auto_now_add=True, verbose_name='Publish Date')),
                ('image', models.ImageField(blank=True, null=True, upload_to='post')),
                ('slug', models.SlugField(editable=False, max_length=130, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish_date', 'id'],
            },
        ),
    ]
