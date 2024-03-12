# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import FIR


@admin.register(FIR)
class FIRAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fir_no',
        'district',
        'unit_name',
        'year',
        'month',
        'registered_on',
        'fir_type',
        'fir_stage',
        'complaint_mode',
        'crime_group_name',
        'crime_head_name',
        'latitude',
        'longitude',
        'ActSection',
        'IOName',
        'KGID',
        'IOAssigned_Date',
        'Internal_IO',
        'Place_of_Offence',
        'distance_from_ps',
        'Beat_Name',
        'Village_Area_Name',
        'Male',
        'Female',
        'Boy',
        'Girl',
        'Age',
        'VICTIM_COUNT',
        'ACCUSED_COUNT',
        'Arrested_Male',
        'Arrested_Female',
        'Arrested_Count_No',
        'Accused_ChargeSheeted_Count',
        'Conviction_Count',
        'fir_id',
        'unit_id',
        'crime_no',
    )
    list_filter = ('registered_on', 'IOAssigned_Date')
