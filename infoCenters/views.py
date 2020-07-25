from django.shortcuts import render, redirect
from infoCenters.models import *
from django.db.models import Q
from .OpenFile2List import *
import time
from django.views.decorators.cache import cache_page

@cache_page(60 * 15) #缓存15分钟
def index(request):
    '''
    :param request: 
    :return: return_context为字典类型，其中
             res_banner:首页轮播的数据
             res_psg: 首页微关注的数据
             res_ved: 首页视频的数据
             res_dm: 首页图片展示的数据 
    '''
    # 2019/10/18 19:35   修改首页轮播图片为3个
    if Passage.objects.filter(hot=True).count() is 0:#如果置顶的数据为0，则获取一般的数据，下面逻辑相同
        IMG = Passage.objects.order_by('-passage_time')[:3].values()
    else:
        IMG = Passage.objects.filter(hot=True).order_by('-passage_time')[:3].values()#首页轮播图
    # 2019/10/18 19:35   修改首页DM图片为2个
    if DMIMG.objects.filter(hot=True).count() is 0:
        DM = DMIMG.objects.order_by('-id').values()[:2]  # 首页图片展示
    else:
        DM = DMIMG.objects.filter(hot=True).order_by('-id')[:2].values()#首页图片展示


    PSG = Passage.objects.all()[3:9].values()#首页微关注
    #2019/10/18 19:35   修改首页视频图片为3个
    VEDIO = Vedio.objects.all()[:3].values()#首页视频
    res_banner = OpenPassage2List(IMG)
    res_psg = OpenPassage2List(PSG)
    res_ved = OpenVedio2List(VEDIO)
    res_dm = OpenDMIMGandIndexImg2List(DM)
    return_context = {
        'bannerImg': res_banner,
        'Passage': res_psg,
        'Vedio':res_ved,
        'DmImg':res_dm
    }
    return render(request, 'career/index.html', return_context)

def indexChange(request):
    return redirect('/')

@cache_page(60 * 15) #缓存15分钟
def allNews(request, page):

    '''
        page:页数

    '''
    pernum = 4  # 每页新闻数量
    MAG = Magazine.objects.order_by('-id')[:3].values()
    if page is None or page is '0':
        PSG = Passage.objects.order_by('-passage_time')[:pernum].values()
        res_psg = OpenPassage2List(PSG)
        res_pre = None
        res_next = [{'id':'1'}]
        res_magazine = OpenMagazine2List(MAG)
    else:
        PSG = Passage.objects.order_by('-passage_time')[int(page)*pernum:int(page)*pernum+pernum].values()
        res_psg = OpenPassage2List(PSG)
        if res_psg[-1]['id'] is Passage.objects.order_by('passage_time')[0].id:
            res_pre = [{'id':str(int(page) - 1)}]
            res_next = None
        elif res_psg[0]['id'] is Passage.objects.order_by('-passage_time')[0].id:
            res_next = [{'id':str(int(page) + 1)}]
            res_pre = None
        else:
            res_next = [{'id':str(int(page) + 1)}]
            res_pre = [{'id':str(int(page) - 1)}]
        res_magazine = OpenMagazine2List(MAG)

    return_context = {
        'Passage': res_psg,
        'Magazine': res_magazine,
        'next':res_next,
        'pre':res_pre,
    }
    return render(request, 'career/allNews.html', return_context)

@cache_page(60 * 15) #缓存15分钟
def news(request, i):
    PSG = Passage.objects.filter(id=i).values()
    # 当前这篇文章的时间
    now_time = Passage.objects.filter(id=i).values('passage_time')
    # 通过对比时间来获取上下文
    # 修改日期：2019/03/20 13点31分 更新文章中翻页逻辑的问题
    # 当前文章的上一篇应该是小于它时间的文章中最接近它的一篇
    # 当前文章的下一篇应该是大于它时间的文章中最接近它的一篇
    nextpsg = Passage.objects.order_by('-passage_time').filter(passage_time__lt=now_time)[:1].values()
    prepsg = Passage.objects.order_by('passage_time').filter(passage_time__gt=now_time)[:1].values()
    
    # 以下是增加一次访问次数的逻辑
    temp = PSG.values()[0]['views'] + 1  # 访问次数+1
    PSG.update(views=temp)  # 更新访问次数

    res_psg = OpenPassage2List(PSG)
    res_next = OpenPassage2List(nextpsg)
    res_pre = OpenPassage2List(prepsg)
    return_context = {
        'Passage': res_psg,
        'next': res_next,
        'pre': res_pre,
    }
    return render(request, 'career/news.html', return_context)

@cache_page(60 * 15) #缓存15分钟
def vediolist(request, page):
    pernum = 5#每页视频数
    '''
        page:页数

    '''
    MAG = Magazine.objects.order_by('-id')[:3].values()
    if page is None or page is '0':
        vedio = Vedio.objects.order_by('-id')[:pernum].values()
        
        res_ved = OpenVedio2List(vedio)
        res_pre = None
        if res_ved[-1]['id'] is Vedio.objects.first().id:
            res_next = None
        else:
            try:
                res_next = [{'id': str(int(page) + 1)}]
            except TypeError as e:
            #page = 0
            	res_next = [{'id':'1'}]
        res_magazine = OpenMagazine2List(MAG)
    else:
        vedio = Vedio.objects.order_by('-vedio_time')[int(page) * pernum:int(page) * pernum + pernum].values()
        res_ved = OpenVedio2List(vedio, 2)
        if res_ved[-1]['id'] is Vedio.objects.order_by('vedio_time')[0].id:
            res_pre = [{'id':str(int(page)- 1)}]
            res_next = None
        elif res_ved[0]['id'] is Vedio.objects.order_by('-vedio_time')[0].id:
            res_next = [{'id':str(int(page)+ 1)}]
            res_pre = None
        else:
            res_next = [{'id':str(int(page) +1)}]
            res_pre = [{'id':str(int(page) -1)}]
        res_magazine = OpenMagazine2List(MAG)
    return_context = {
        'Vedio': res_ved,
        'Magazine': res_magazine,
        'next': res_next,
        'pre': res_pre,
        }

    return render(request, 'career/vediolist.html', return_context)


@cache_page(60 * 15) #缓存15分钟
def imgDisplay(request, page):

    pernum = 13#每页的图片数量
    '''
        page:页数
        以下是res_next的构造逻辑，res_pre同理
        1.数据结构：res_next:[{'id':num1}], res_pre:[{'id':num2}]
        2.num1=page+1, num2=page-1, 前提是前后页都存在，不存在则直接不设置即可
    '''
    res_type = [{
        'name': 'LOGO'
        },
        {
            'name': '办公室美化'
        },
        {
            'name': '宣传类'
        },
        {
            'name': '展示类'
        }]
    if page is None:
        res_pre = None
        if DMIMG.objects.all().count() <= pernum:
            res_next = None
        else:
            res_next = [{'id':'1'}]
        IMG = DMIMG.objects.all()[:pernum].values()
        res_img = OpenDMIMGandIndexImg2List(IMG)
    else:
        IMG = DMIMG.objects.all()[int(page)*pernum: int(page)*pernum + pernum].values()#获取 页数*pernum->页数*pernum+pernum的图片，即实现翻页功能
        res_img = OpenDMIMGandIndexImg2List(IMG)
        
        if res_img[-1]['id'] is DMIMG.objects.last().id and len(res_img) > 1:
            res_pre = [{'id': str(int(page) - 1)}]
            res_next = None

        elif res_img[0]['id'] is Passage.objects.first().id or len(res_img) == 1:
            res_next = [{'id': str(int(page) + 1)}]
            res_pre = None
        else:
            res_next = [{'id': str(int(page) + 1)}]
            res_pre = [{'id': str(int(page) - 1)}]
    return_context = {
        'Img':res_img,
        'next':res_next,
        'pre':res_pre,
        'type':res_type
    }
    return render(request, 'career/ImgDisplay.html', return_context)

# @cache_page(60 * 15) #缓存15分钟
def vedio(request, page):
    '''
        page：即数据库中视频的id
    '''
    PSG = Passage.objects.all()[:3].values()
    VEDIO = Vedio.objects.filter(id=page).values()
    prevedio = Vedio.objects.filter(id__gt=page)[:1].values()
    nextvedio = Vedio.objects.order_by('-id').filter(id__lt=page)[:1].values()

    #增加一次访问量的逻辑
    temp = VEDIO.values()[0]['vedio_views'] + 1
    VEDIO.update(vedio_views = temp)

    res_vedio = OpenVedio2List(VEDIO)
    res_psg = OpenPassage2List(PSG)
    res_next = OpenVedio2List(nextvedio)
    res_pre = OpenVedio2List(prevedio)
    return_context = {
        'Vedio': res_vedio,
        'PSG': res_psg,
        'next': res_next,
        'pre': res_pre,
    }
    return render(request, 'career/vedio.html', return_context)

# @cache_page(60 * 15) #缓存15分钟
def dataDisplay(request,tm):
    try:
        timeList = BarModel.objects.values('bar_time')#获取可选的时间列表
        NEWS = Passage.objects.all()[:4].values()
        MAGA = Magazine.objects.all()[:3].values()
        if tm is None:
            #获取最新的数据的时间，通过柱状图的时间来获取其他图形在同一天的数据
            tm = BarModel.objects.order_by('-id')[0].bar_time

            barData = BarModel.objects.filter(bar_time=tm)[:1].values()
            lineData = LineModel.objects.filter(line_time=tm)[:1].values()
            pieData = PieModel.objects.filter(pie_time=tm)[:1].values()
            mix = MixModel.objects.filter(mix_time=tm)[:1].values()
            Datatitle = TotalTitleModel.objects.filter(tm=tm)[:1].values()
            res_news = OpenPassage2List(NEWS)
            res_mag = OpenMagazine2List(MAGA)
        else:
            tm = str(tm)
            timeArr = time.strptime(tm, '%Y%m%d')  # 获得年月日
            year, month, day = str(timeArr[0]), str(timeArr[1]), str(timeArr[2])
            tm = year+'年'+month+'月'+day+'日'#构造查询的时间字符串

            barData = BarModel.objects.filter(bar_time=tm)[:1].values()
            lineData = LineModel.objects.filter(line_time=tm)[:1].values()
            pieData = PieModel.objects.filter(pie_time=tm)[:1].values()
            mix = MixModel.objects.filter(mix_time=tm)[:1].values()
            Datatitle = TotalTitleModel.objects.filter(tm=tm)[:1].values()

            res_news = OpenPassage2List(NEWS)
            res_mag = OpenMagazine2List(MAGA)

        res_title = []
        for i in Datatitle:
            res_title.append(i)
        res_bar = OpenData2List(barData)
        res_line = OpenData2List(lineData)
        res_pie = OpenData2List(pieData)
        res_list = OpenData2List(timeList)
        res_mix = OpenData2List(mix)

        return_context = {
            'bar':res_bar,
            'line':res_line,
            'pie':res_pie,
            'mix':res_mix,
            'timeList':res_list,
            'news':res_news,
            'maga':res_mag,
            'dataTitile':res_title
        }
        return render(request, 'career/Data.html', return_context)
    except IndexError:
        res_bar = res_line = res_list =res_mag = res_mix =res_news =res_pie = res_title = []
        return_context = {
            'bar': res_bar,
            'line': res_line,
            'pie': res_pie,
            'mix': res_mix,
            'timeList': res_list,
            'news': res_news,
            'maga': res_mag,
            'dataTitile': res_title
        }
        return render(request, 'career/Data.html', return_context)
# @cache_page(60 * 15) #缓存15分钟
def contactus(request):
    return render(request, 'career/contactus.html')

def page_not_found(request):
    return render(request, '404.html')

def Success(request):
    return render(request, 'career/success.html')
