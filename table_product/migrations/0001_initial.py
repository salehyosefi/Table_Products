# Generated by Django 4.0.2 on 2022-07-31 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='نام محصول')),
                ('price', models.IntegerField(verbose_name='قیمت محصول')),
                ('number', models.IntegerField(verbose_name='تعداد')),
                ('description', models.CharField(max_length=250, verbose_name='توضیحات')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'پست',
                'verbose_name_plural': 'پست ها',
            },
        ),
    ]