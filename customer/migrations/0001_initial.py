# Generated by Django 3.2 on 2021-05-01 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='1.jpg', upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.category')),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=70)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_shipped', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(blank=True, to='customer.MenuItem')),
            ],
        ),
    ]