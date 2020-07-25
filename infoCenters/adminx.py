import xadmin
from infoCenters.models import *
from xadmin import views
# Register your models here.

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSettings():
    site_title = "知涯后台"
    site_footer = "在线网站"
    menu_style = "accordion"

class DMImgAdmin():
    list_display = ['img_name','img_url','img_auth','img_type']
    list_filter = ['img_name','img_url','img_auth','img_type']
    search_fields = ['img_name','img_url','img_auth','img_type']


class PassageAdmin():
    list_display = ['title', 'Type', 'content', 'passage_time', 'passage_img', 'source','views']
    list_filter = ['title', 'Type', 'content', 'passage_time', 'passage_img', 'source','views']
    search_fields = ['title', 'Type', 'content', 'passage_time', 'passage_img', 'source','views']
    list_editable = ['Type']

class ViewTimeAdmin():
    list_display = ['times']

class DmViewAdmin():
    list_display = ['views']

class VedioAdmin():
    list_display = ['vedio_name','vedio_url','vedio_time','vedio_img','vedio_source','vedio_views']
    list_filter = ['vedio_name','vedio_url','vedio_time','vedio_img','vedio_source','vedio_views']
    search_fields = ['vedio_name','vedio_url','vedio_time','vedio_img','vedio_source','vedio_views']

class MagezineAdmin():
    list_display = ['issue', 'title', 'magazine', 'cover']
    list_filter = ['issue', 'title', 'magazine', 'cover']
    list_fields = ['issue', 'title', 'magazine', 'cover']

class TotalTitleModelAdmin():
    list_display = ['Total_title', 'tm']
    list_filter = ['Total_title', 'tm']
    list_fields = ['Total_title', 'tm']
    search_fields = ['Total_title', 'tm']
    list_editable = ['tm']

class BarModelAdmin():
    list_display = ['bar_title','bar_time','data_type','bar_legend','bar_dataset','bar_axis','x_type','y_type']
    list_filter = ['bar_title','bar_time','data_type','bar_legend','bar_dataset','bar_axis','x_type','y_type']
    search_fields = ['bat_title','bar_time','data_type','bar_legend','bar_dataset','bar_axis','x_type','y_type']
    list_editable = ['bar_time']

class LineModelAdmin():
    list_display = ['line_title', 'line_time', 'line_smth', 'data_type', 'line_legend', 'line_dataset', 'line_axis', 'x_type', 'y_type']
    list_filter = ['line_title','line_time', 'line_smth', 'data_type', 'line_legend', 'line_dataset', 'line_axis', 'x_type', 'y_type']
    search_fields = [ 'line_title', 'line_time', 'line_smth', 'data_type', 'line_legend', 'line_dataset', 'line_axis', 'x_type', 'y_type']
    list_editable = ['line_time','line_smth']

class PieModelAdmin():
    list_display = ['pie_title', 'pie_time',  'data_type', 'pie_legend', 'pie_dataset', 'pie_radius', 'pie_tooltip', 'pie_colors']
    list_filter = ['pie_title', 'pie_time',  'data_type', 'pie_legend', 'pie_dataset', 'pie_radius', 'pie_tooltip', 'pie_colors']
    search_fields = ['pie_title', 'pie_time',  'data_type', 'pie_legend', 'pie_dataset', 'pie_radius', 'pie_tooltip', 'pie_colors']
    list_editable = ['pie_time']

class MixModelAdmin():
    list_display = ['mix_time','code']
    list_filter = ['mix_time', 'code']
    list_fields = ['mix_time','code']

# class NormalUserAdmin():
#     list_display = ['username','headImg']
#     list_fields = ['username','headImg']
#     list_filter = ['username','headImg']

xadmin.site.register(DMIMG, DMImgAdmin)
xadmin.site.register(Passage,PassageAdmin)
xadmin.site.register(ViewTimes, ViewTimeAdmin)
xadmin.site.register(DmView, DmViewAdmin)
xadmin.site.register(Vedio, VedioAdmin)
xadmin.site.register(Magazine, MagezineAdmin)
xadmin.site.register(TotalTitleModel, TotalTitleModelAdmin)
xadmin.site.register(BarModel, BarModelAdmin)
xadmin.site.register(LineModel, LineModelAdmin)
xadmin.site.register(PieModel, PieModelAdmin)
xadmin.site.register(MixModel, MixModelAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView,BaseSetting)