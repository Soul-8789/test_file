# Generated by Django 4.1.4 on 2023-01-08 21:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_postcomment_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFollow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follows_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dest_follow', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='src_follow', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
