# Generated by Django 3.0.3 on 2020-02-19 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('storyboard', '0005_auto_20200219_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('blurb', models.CharField(max_length=150)),
                ('selected', models.BooleanField(default=False)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('addition', models.TextField()),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storyboard.Plot')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.CharField(max_length=2000)),
                ('plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storyboard.Plot')),
            ],
        ),
    ]
