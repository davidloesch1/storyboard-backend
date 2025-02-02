# Generated by Django 3.0.3 on 2020-02-22 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storyboard', '0007_auto_20200220_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='plot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='storyboard.Plot'),
        ),
        migrations.AlterField(
            model_name='plot',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
