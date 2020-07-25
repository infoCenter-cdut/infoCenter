#以下是将文件转换为数据的方法
media = 'media/'
PASSAGE_TYPE = (
        "宣传类新闻",
        "双选会新闻",
        "面试技巧",
        "美丽校园",
        "企业专访",
        "其他",
    )

def OpenDMIMGandIndexImg2List(IMG):
    res_img = []
    for i in IMG:
        res_img.append(i)
    return res_img

def OpenPassage2List(Passage):
    res_psg = []
    for i in Passage:
        res_psg.append(i)
    for j in range(len(res_psg)):
        try:
            content = open(media+res_psg[j]['content'],encoding="utf-8").read()#读取文件数据
        except UnicodeDecodeError:
            content = open(media+res_psg[j]['content'],encoding="gbk").read()
        res_psg[j]['content'] = content  #替换文件名为文件内容
    return res_psg

def OpenMagazine2List(data):
    res_magazine = []
    for i in data:
        res_magazine.append(i)
    return res_magazine

def OpenVedio2List(VEDIO, urldepth=0):
    res_vedio = []
    for i in VEDIO:
        res_vedio.append(i)
    return res_vedio

def OpenData2List(data):
    res_data = []
    for i in data:
        res_data.append(i)
    return res_data