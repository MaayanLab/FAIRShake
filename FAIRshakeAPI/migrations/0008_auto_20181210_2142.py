# Generated by Django 2.0.7 on 2018-12-10 21:42

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('FAIRshakeAPI', '0007_auto_20180924_1435'),
    ]

    operations = [
        migrations.RenameField(
            'answer',
            'answer',
            'answer_tmp',
        ),
        migrations.AddField(
            model_name='answer',
            name='answer',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
