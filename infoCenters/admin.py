from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "知涯运维管理系统"

@admin.register(DMIMG)
class DMImgAdmin(admin.ModelAdmin):
    list_display = ['img_name','img_url','img_auth','img_type','hot']
    list_filter = ['img_name','img_url','img_auth','img_type','hot']
    search_fields = ['img_name','img_url','img_auth','img_type','hot']
    list_editable = ['img_type','hot']

@admin.register(Passage)
class PassageAdmin(admin.ModelAdmin):
    list_display = ['title', 'Type', 'content', 'passage_time', 'passage_img', 'source','views','hot']
    list_filter = ['title', 'Type', 'content', 'passage_time', 'passage_img', 'source','views','hot']
    search_fields = ['title', 'Type', 'content', 'passage_time', 'passage_img', 'source','views','hot']
    list_editable = ['Type','hot']

@admin.register(ViewTimes)
class ViewTimeAdmin(admin.ModelAdmin):
    list_display = ['times']

@admin.register(DmView)
class DmViewAdmin(admin.ModelAdmin):
    list_display = ['views']

@admin.register(Vedio)
class VedioAdmin(admin.ModelAdmin):
    list_display = ['vedio_name','vedio_url','vedio_time','vedio_img','vedio_source','vedio_views','hot']
    list_filter = ['vedio_name','vedio_url','vedio_time','vedio_img','vedio_source','vedio_views','hot']
    search_fields = ['vedio_name','vedio_url','vedio_time','vedio_img','vedio_source','vedio_views','hot']
    list_editable = ['hot']

@admin.register(Magazine)
class MagezineAdmin(admin.ModelAdmin):
    list_display = ['issue', 'title', 'magazine', 'cover']
    list_filter = ['issue', 'title', 'magazine', 'cover']
    list_fields = ['issue', 'title', 'magazine', 'cover']

@admin.register(TotalTitleModel)
class TotalTitleModelAdmin(admin.ModelAdmin):
    list_display = ['Total_title', 'tm']
    list_filter = ['Total_title', 'tm']
    list_fields = ['Total_title', 'tm']
    search_fields = ['Total_title', 'tm']

@admin.register(BarModel)
class BarModelAdmin(admin.ModelAdmin):
    list_display = ['bar_title','bar_time','data_type','bar_legend','bar_dataset','bar_axis','x_type','y_type']
    list_filter = ['bar_title','bar_time','data_type','bar_legend','bar_dataset','bar_axis','x_type','y_type']
    search_fields = ['bat_title','bar_time','data_type','bar_legend','bar_dataset','bar_axis','x_type','y_type']
    list_editable = ['bar_time']

@admin.register(LineModel)
class LineModelAdmin(admin.ModelAdmin):
    list_display = ['line_title', 'line_time', 'line_smth', 'data_type', 'line_legend', 'line_dataset', 'line_axis', 'x_type', 'y_type']
    list_filter = ['line_title','line_time', 'line_smth', 'data_type', 'line_legend', 'line_dataset', 'line_axis', 'x_type', 'y_type']
    search_fields = [ 'line_title', 'line_time', 'line_smth', 'data_type', 'line_legend', 'line_dataset', 'line_axis', 'x_type', 'y_type']
    list_editable = ['line_time','line_smth']

@admin.register(PieModel)
class PieModelAdmin(admin.ModelAdmin):
    list_display = ['pie_title', 'pie_time',  'data_type', 'pie_legend', 'pie_dataset', 'pie_radius', 'pie_tooltip', 'pie_colors']
    list_filter = ['pie_title', 'pie_time',  'data_type', 'pie_legend', 'pie_dataset', 'pie_radius', 'pie_tooltip', 'pie_colors']
    search_fields = ['pie_title', 'pie_time',  'data_type', 'pie_legend', 'pie_dataset', 'pie_radius', 'pie_tooltip', 'pie_colors']
    list_editable = ['pie_time']

@admin.register(MixModel)
class MixModelAdmin(admin.ModelAdmin):
    list_display = ['mix_time','code']
    list_filter = ['mix_time', 'code']
    list_fields = ['mix_time','code']

'''
@admin.register(NormalUser)
class NormalUserAdmin(admin.ModelAdmin):
    list_display = ['username','headImg']
    list_fields = ['username','headImg']
    list_filter = ['username','headImg']
'''

