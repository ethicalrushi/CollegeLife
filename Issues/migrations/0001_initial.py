# Generated by Django 2.0.1 on 2018-03-17 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Loginapp', '0004_remove_userprofileinfo_portfolio_site'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob_stat', models.TextField()),
                ('created', models.DateField()),
                ('rating_likes', models.PositiveIntegerField(blank=True, default=0, editable=False)),
                ('rating_dislikes', models.PositiveIntegerField(blank=True, default=0, editable=False)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Loginapp.College')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
