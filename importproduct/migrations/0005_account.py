# Generated by Django 3.2.15 on 2022-10-24 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importproduct', '0004_alter_billing_charge_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=40, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('initialized', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
