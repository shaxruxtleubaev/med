# Generated by Django 4.1 on 2023-06-03 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_alter_specializations_options_doctors_friday_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicesCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'services category',
                'verbose_name_plural': 'services categories',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('short_description', models.TextField(verbose_name='Short Description')),
                ('icon', models.ImageField(upload_to='services-icons', verbose_name='Icon')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.servicescategories')),
                ('doctors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.doctors')),
            ],
            options={
                'verbose_name': 'service',
                'verbose_name_plural': 'services',
            },
        ),
    ]