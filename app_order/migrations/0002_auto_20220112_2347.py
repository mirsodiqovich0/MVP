# Generated by Django 3.2.9 on 2022-01-12 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={},
        ),
        migrations.RemoveField(
            model_name='order',
            name='accepted',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cancelled',
        ),
        migrations.RemoveField(
            model_name='order',
            name='created',
        ),
        migrations.RemoveField(
            model_name='order',
            name='finished',
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app_order.client'),
        ),
        migrations.AlterField(
            model_name='order',
            name='driver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='app_order.driver'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status_of_order',
            field=models.CharField(choices=[('Created', 'Created'), ('Cancelled', 'Cancelled'), ('Accepted', 'Accepted'), ('Finished', 'Finished')], max_length=20),
        ),
    ]
