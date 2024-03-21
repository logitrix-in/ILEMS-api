# Generated by Django 4.1.13 on 2024-03-21 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0005_alter_fir_ioassigned_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chargesheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('UnitName', models.CharField(blank=True, max_length=100, null=True)),
                ('FIRNo', models.CharField(blank=True, max_length=100, null=True)),
                ('RI', models.CharField(blank=True, max_length=100, null=True)),
                ('Year', models.IntegerField(blank=True, null=True)),
                ('Month', models.IntegerField(blank=True, null=True)),
                ('FIR_Date', models.DateField(blank=True, null=True)),
                ('Report_Date', models.DateField(blank=True, null=True)),
                ('Final_Report_Date', models.DateField(blank=True, null=True)),
                ('Report_Type', models.CharField(max_length=100)),
                ('FIR_ID', models.TextField(blank=True, null=True)),
                ('Unit_ID', models.TextField(blank=True, null=True)),
                ('Crime_No', models.TextField(blank=True, null=True)),
                ('FR_ID', models.TextField(blank=True, null=True)),
            ],
        ),
    ]