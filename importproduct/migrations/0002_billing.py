# Generated by Django 3.2.15 on 2022-10-15 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('importproduct', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_id', models.TextField(max_length=200, null=True)),
                ('createdAt', models.DateTimeField()),
                ('currentPeriodEnd', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='importproduct.authappshopuser')),
            ],
        ),
    ]
