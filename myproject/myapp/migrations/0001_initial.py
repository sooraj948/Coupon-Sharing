# Generated by Django 4.0.1 on 2022-01-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon_List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=200)),
                ('expiry', models.DateField()),
                ('used', models.BooleanField()),
            ],
            options={
                'db_table': 'coupon_list',
            },
        ),
    ]
