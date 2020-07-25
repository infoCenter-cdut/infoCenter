from django.db import models
from django.contrib import admin
# Create your models here.
class ViewTimes(models.Model):
    times = models.IntegerField(default = 0,null = True)

#美工dm单
class DMIMG(models.Model):
    IMG_TYPE = (
        ('LOGO','LOGO'),
        ('工作类','工作类'),
        ('办公类','办公类'),
        ('宣传类','宣传类'),
        ('展示类','展示类'),
        ('形象类','形象类')
    )
    img_url = models.ImageField(verbose_name="美工DM单",upload_to="dmImg")
    img_name = models.CharField(max_length=20, verbose_name="DM单名字", null=True, blank=True)
    img_auth = models.CharField(max_length=100,verbose_name="作者姓名",default="美工部小组", null=True)
    img_type = models.CharField(max_length=50,null=True, verbose_name="图片种类", choices=IMG_TYPE)
    hot = models.BooleanField(default=False, verbose_name="是否置顶该图片", null=False)
    class Meta:
        verbose_name = "创意空间表"
        verbose_name_plural = '创意空间表'

#新闻模型
class Passage(models.Model):
    PASSAGE_TYPE = (
        ("宣传类新闻","宣传类新闻"),
        ("双选会新闻","双选会新闻"),
        ("面试技巧","面试技巧"),
        ("美丽校园","美丽校园"),
        ("企业专访","企业专访"),
        ("其他","其他"),
    )
    title = models.CharField(max_length=1000, verbose_name="文章标题")#文章标题
    Type = models.CharField(max_length=40, choices=PASSAGE_TYPE,verbose_name="文章类型")#文章类别
    content = models.FileField(verbose_name="文章正文",upload_to="newspassage")#文章内容
    passage_time = models.DateTimeField(max_length=100,verbose_name="发布时间")#文章公布时间
    passage_img = models.ImageField(max_length=100,verbose_name="文章配图",upload_to="newspassageImg")#文章配图
    source = models.CharField(max_length=100,default='就业信息中心',verbose_name="文章来源")#文章来源
    views = models.IntegerField(default=0, null=True,verbose_name="浏览次数")
    hot = models.BooleanField(default=False, verbose_name="是否置顶该文章", null=False)

    class Meta:
        verbose_name = "微关注表"
        verbose_name_plural = '微关注表'

class DmView(models.Model):
    views = models.IntegerField(default=0,null=True)

#视频
class Vedio(models.Model):
    vedio_url = models.CharField(max_length=1000,null=True, verbose_name="视频链接")
    vedio_name = models.CharField(max_length=50, null=True, verbose_name="视频名字")
    vedio_img = models.ImageField(null=True, verbose_name="视频配图", upload_to='vedioImg')
    vedio_time = models.DateTimeField(null=True, verbose_name="发布时间")
    vedio_source = models.CharField(max_length=100, default='就业信息中心', verbose_name="视频来源")
    vedio_views = models.IntegerField(default=0,null =True, verbose_name="浏览次数")
    hot = models.BooleanField(default=False, verbose_name="是否置顶该视频", null=False)
    class Meta:
        verbose_name = "视频表"
        verbose_name_plural = '视频表'

#就协杂志
class Magazine(models.Model):
    title = models.CharField(max_length=50, verbose_name="杂志主题(一般不写)", null=True)
    cover = models.ImageField(verbose_name="封面图片", null=True, upload_to="magezineImage")
    issue = models.IntegerField(default=0, null=False, verbose_name="杂志期数")
    magazine = models.FileField(verbose_name="杂志文件(pdf)", null=False, upload_to="magazine")
    class Meta:
        verbose_name = "就协杂志表"
        verbose_name_plural = '就协杂志表'

class InterView(models.Model):
    PSG_TYPE = (
        ('面试技巧','面试技巧')
    )
    inter_title = models.CharField(max_length=50, null=True, verbose_name="文章名字")
    inter_type = models.CharField(max_length=20, null=True,  verbose_name="文章类型")
    inter_content = models.FileField(verbose_name="文章内容", upload_to='interviewTrick')
    inter_source = models.CharField(max_length=20, null=True, verbose_name="文章来源")
    inter_time = models.DateTimeField(verbose_name="发布时间")
    class Meta:
        verbose_name = "面试技巧表"
        verbose_name_plural = '面试技巧表'

class TotalTitleModel(models.Model):
    Total_title = models.CharField(max_length=100, null=True, verbose_name="数据总标题")
    tm = models.CharField(max_length=30, null=True, verbose_name='时间',help_text="以YMD形式输入，例如20180510，表示2018年5月10号")
    class Meta:
        verbose_name = "大数据标题表"
        verbose_name_plural = '大数据标题表'

#柱状图
class BarModel(models.Model):
    axis_type = (
        ('value','value'),#数轴为连续型数据
        ('category', 'category'),#数轴为离散型数据
        ('time', 'time'),
        ('log', 'log'),
    )
    bar_time = models.CharField(max_length=30, null=True, verbose_name='时间',help_text="以YMD形式输入，例如20180510，表示2018年5月10号")
    bar_title = models.CharField(max_length=50, null=True, verbose_name="柱状图标题")
    data_type = models.CharField(default="bar", verbose_name="图类型(勿更改)", null=False, max_length=10)
    bar_legend = models.CharField(max_length=1000, verbose_name="图例")
    '''
        dataset中的数据以空格分隔，不写中括号比如一组数据[12,4,5]在录入的时候写
        12 4 5
    '''
    bar_dataset = models.TextField(verbose_name="数据",max_length=10000)
    bar_axis = models.TextField(verbose_name="x,y轴名字", max_length=10000)
    x_type = models.CharField(max_length=10, null=False, default="category", choices=axis_type, verbose_name="x轴类型")
    y_type = models.CharField(max_length=10, null=False, default="category", choices=axis_type, verbose_name="y轴类型")
    class Meta:
        verbose_name = "柱状图表"
        verbose_name_plural = '柱状图表'

#折线图
class LineModel(models.Model):
    axis_type = (
        ('value','value'),#数轴为连续型数据
        ('category', 'category'),#数轴为离散型数据
        ('time', 'time'),
        ('log', 'log'),
    )
    line_time = models.CharField(max_length=30, null=True, verbose_name='时间',help_text="以YMD形式输入，例如20180510，表示2018年5月10号")
    line_title = models.CharField(max_length=50, null=True, verbose_name="折线图标题")
    data_type = models.CharField(default="line", verbose_name="图类型(勿更改)", null=False, max_length=10)
    line_legend = models.CharField(max_length=1000, verbose_name="图例")
    '''
        dataset中的数据以空格分隔，不写中括号比如一组数据[12,4,5]在录入的时候写
        12 4 5
    '''
    line_dataset = models.TextField(verbose_name="数据", max_length=10000)
    line_axis = models.TextField(verbose_name="x,y轴名字", max_length=10000)
    line_smth = models.BooleanField(verbose_name="是否用光滑曲线", default=False)
    x_type = models.CharField(max_length=10, null=False, default="category", choices=axis_type, verbose_name="x轴类型")
    y_type = models.CharField(max_length=10, null=False, default="category", choices=axis_type, verbose_name="y轴类型")
    class Meta:
        verbose_name = "折线图表"
        verbose_name_plural = '折线图表'

#饼状图
class PieModel(models.Model):
    pie_time = models.CharField(max_length=30, null=True, verbose_name='时间',help_text="以YMD形式输入，例如20180510，表示2018年5月10号")
    pie_title = models.CharField(max_length=50, null=False, verbose_name="饼状图标题")
    data_type = models.CharField(default="pie", verbose_name="图类型(勿更改)", null=False, max_length=10)
    pie_legend = models.CharField(max_length=1000, verbose_name="图例", null=False)
    pie_tooltip = models.CharField(max_length=1000, verbose_name="显示设置(勿更改)", null=False, default="trigger: 'item',formatter: '{a} <br/>{b}: {c} ({d}%)'")
    pie_radius = models.CharField(max_length=30, verbose_name="饼状图半径", default="70%", null=False)
    '''
        dataset中的数据以dict的形式进行编写，比如，雨天有20天，晴天有10天
        {20,雨天} {10,晴天}
    '''
    pie_dataset = models.TextField(verbose_name="数据", max_length=10000, default="{data,value} {data,value}")
    pie_colors = models.CharField(verbose_name="颜色", max_length=500, null=True, default="一般不填写")
    class Meta:
        verbose_name = "饼状图表"
        verbose_name_plural = '饼状图表'

class MixModel(models.Model):
    code = models.TextField(verbose_name="代码", help_text="请按照echartJS的文档进行编写")
    mix_time = models.CharField(max_length=30, null=True, verbose_name='时间',help_text="以YMD形式输入，例如20180510，表示2018年5月10号")
    class Meta:
        verbose_name = "混合展示数据表"
        verbose_name_plural = '混合展示数据表'

'''
有文件上传需求的时候开启
class NormalUser(models.Model):
    username=models.CharField('用户名',max_length=30)
    #用户名
    headImg=models.FileField('文件',upload_to='upload')#文件名
    def __str__(self):
        return self.username

    class Meta:
        ordering=['username']#排序风格username
'''


