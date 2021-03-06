# Generated by Django 2.0.7 on 2018-10-14 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.FloatField()),
                ('addr', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Pill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='../media')),
                ('qrcode', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('pill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appDatas.Pill')),
            ],
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='pills',
            field=models.ManyToManyField(related_name='pharmacies', to='appDatas.Pill'),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='products',
            field=models.ManyToManyField(to='appDatas.Product'),
        ),
    ]
