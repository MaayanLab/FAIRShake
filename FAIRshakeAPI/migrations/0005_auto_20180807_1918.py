# Generated by Django 2.0.7 on 2018-08-07 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('FAIRshakeAPI', '0004_auto_20180807_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='assessment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='FAIRshakeAPI.Assessment'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='metric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='FAIRshakeAPI.Metric'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='assessor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='requestor',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='rubric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='FAIRshakeAPI.Rubric'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assessments', to='FAIRshakeAPI.DigitalObject'),
        ),
    ]
