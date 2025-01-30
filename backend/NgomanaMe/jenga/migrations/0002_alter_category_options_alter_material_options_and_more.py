# Generated by Django 5.0.6 on 2025-01-30 11:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jenga', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='material',
            options={'ordering': ['-optional', 'name']},
        ),
        migrations.AlterModelOptions(
            name='tutorial',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutorials', to='jenga.category'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='estimated_time',
            field=models.PositiveIntegerField(help_text='Estimated time in minutes'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterUniqueTogether(
            name='step',
            unique_together={('tutorial', 'step_number')},
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['-created_at'], name='jenga_comme_created_81e015_idx'),
        ),
        migrations.AddIndex(
            model_name='tutorial',
            index=models.Index(fields=['-created_at'], name='jenga_tutor_created_ad1bb4_idx'),
        ),
        migrations.AddIndex(
            model_name='tutorial',
            index=models.Index(fields=['slug'], name='jenga_tutor_slug_b9e02a_idx'),
        ),
    ]
