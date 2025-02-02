# Generated by Django 3.0.3 on 2020-02-19 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storyboard', '0003_auto_20200219_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot',
            name='plot',
            field=models.TextField(default='test the plot value'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plot',
            name='pov',
            field=models.CharField(choices=[('First', 'First'), ('Second', 'Second'), ('Third', 'Third'), ('N/A', 'N/A')], default='N/A', max_length=6),
        ),
        migrations.AlterField(
            model_name='plot',
            name='setting',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='plot',
            name='theme',
            field=models.CharField(max_length=100),
        ),
    ]
