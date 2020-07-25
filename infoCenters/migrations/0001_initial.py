# Generated by Django 2.1.1 on 2019-10-10 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar_time', models.CharField(help_text='以YMD形式输入，例如20180510，表示2018年5月10号', max_length=30, null=True, verbose_name='时间')),
                ('bar_title', models.CharField(max_length=50, null=True, verbose_name='柱状图标题')),
                ('data_type', models.CharField(default='bar', max_length=10, verbose_name='图类型(勿更改)')),
                ('bar_legend', models.CharField(max_length=1000, verbose_name='图例')),
                ('bar_dataset', models.TextField(max_length=10000, verbose_name='数据')),
                ('bar_axis', models.TextField(max_length=10000, verbose_name='x,y轴名字')),
                ('x_type', models.CharField(choices=[('value', 'value'), ('category', 'category'), ('time', 'time'), ('log', 'log')], default='category', max_length=10, verbose_name='x轴类型')),
                ('y_type', models.CharField(choices=[('value', 'value'), ('category', 'category'), ('time', 'time'), ('log', 'log')], default='category', max_length=10, verbose_name='y轴类型')),
            ],
            options={
                'verbose_name': '柱状图表',
                'verbose_name_plural': '柱状图表',
            },
        ),
        migrations.CreateModel(
            name='DMIMG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.ImageField(upload_to='dmImg', verbose_name='美工DM单')),
                ('img_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='DM单名字')),
                ('img_auth', models.CharField(default='美工部小组', max_length=100, null=True, verbose_name='作者姓名')),
                ('img_type', models.CharField(choices=[('LOGO', 'LOGO'), ('工作类', '工作类'), ('办公类', '办公类'), ('宣传类', '宣传类'), ('展示类', '展示类'), ('形象类', '形象类')], max_length=50, null=True, verbose_name='图片种类')),
                ('hot', models.BooleanField(default=False, verbose_name='是否置顶该图片')),
            ],
            options={
                'verbose_name': '创意空间表',
                'verbose_name_plural': '创意空间表',
            },
        ),
        migrations.CreateModel(
            name='DmView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InterView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inter_title', models.CharField(max_length=50, null=True, verbose_name='文章名字')),
                ('inter_type', models.CharField(max_length=20, null=True, verbose_name='文章类型')),
                ('inter_content', models.FileField(upload_to='interviewTrick', verbose_name='文章内容')),
                ('inter_source', models.CharField(max_length=20, null=True, verbose_name='文章来源')),
                ('inter_time', models.DateTimeField(verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '面试技巧表',
                'verbose_name_plural': '面试技巧表',
            },
        ),
        migrations.CreateModel(
            name='LineModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_time', models.CharField(help_text='以YMD形式输入，例如20180510，表示2018年5月10号', max_length=30, null=True, verbose_name='时间')),
                ('line_title', models.CharField(max_length=50, null=True, verbose_name='折线图标题')),
                ('data_type', models.CharField(default='line', max_length=10, verbose_name='图类型(勿更改)')),
                ('line_legend', models.CharField(max_length=1000, verbose_name='图例')),
                ('line_dataset', models.TextField(max_length=10000, verbose_name='数据')),
                ('line_axis', models.TextField(max_length=10000, verbose_name='x,y轴名字')),
                ('line_smth', models.BooleanField(default=False, verbose_name='是否用光滑曲线')),
                ('x_type', models.CharField(choices=[('value', 'value'), ('category', 'category'), ('time', 'time'), ('log', 'log')], default='category', max_length=10, verbose_name='x轴类型')),
                ('y_type', models.CharField(choices=[('value', 'value'), ('category', 'category'), ('time', 'time'), ('log', 'log')], default='category', max_length=10, verbose_name='y轴类型')),
            ],
            options={
                'verbose_name': '折线图表',
                'verbose_name_plural': '折线图表',
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True, verbose_name='杂志主题(一般不写)')),
                ('cover', models.ImageField(null=True, upload_to='magezineImage', verbose_name='封面图片')),
                ('issue', models.IntegerField(default=0, verbose_name='杂志期数')),
                ('magazine', models.FileField(upload_to='magazine', verbose_name='杂志文件(pdf)')),
            ],
            options={
                'verbose_name': '就协杂志表',
                'verbose_name_plural': '就协杂志表',
            },
        ),
        migrations.CreateModel(
            name='MixModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(help_text='请按照echartJS的文档进行编写', verbose_name='代码')),
                ('mix_time', models.CharField(help_text='以YMD形式输入，例如20180510，表示2018年5月10号', max_length=30, null=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '混合展示数据表',
                'verbose_name_plural': '混合展示数据表',
            },
        ),
        migrations.CreateModel(
            name='Passage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000, verbose_name='文章标题')),
                ('Type', models.CharField(choices=[('宣传类新闻', '宣传类新闻'), ('双选会新闻', '双选会新闻'), ('面试技巧', '面试技巧'), ('美丽校园', '美丽校园'), ('企业专访', '企业专访'), ('其他', '其他')], max_length=40, verbose_name='文章类型')),
                ('content', models.FileField(upload_to='newspassage', verbose_name='文章正文')),
                ('passage_time', models.DateTimeField(max_length=100, verbose_name='发布时间')),
                ('passage_img', models.ImageField(upload_to='newspassageImg', verbose_name='文章配图')),
                ('source', models.CharField(default='就业信息中心', max_length=100, verbose_name='文章来源')),
                ('views', models.IntegerField(default=0, null=True, verbose_name='浏览次数')),
                ('hot', models.BooleanField(default=False, verbose_name='是否置顶该文章')),
            ],
            options={
                'verbose_name': '微关注表',
                'verbose_name_plural': '微关注表',
            },
        ),
        migrations.CreateModel(
            name='PieModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pie_time', models.CharField(help_text='以YMD形式输入，例如20180510，表示2018年5月10号', max_length=30, null=True, verbose_name='时间')),
                ('pie_title', models.CharField(max_length=50, verbose_name='饼状图标题')),
                ('data_type', models.CharField(default='pie', max_length=10, verbose_name='图类型(勿更改)')),
                ('pie_legend', models.CharField(max_length=1000, verbose_name='图例')),
                ('pie_tooltip', models.CharField(default="trigger: 'item',formatter: '{a} <br/>{b}: {c} ({d}%)'", max_length=1000, verbose_name='显示设置(勿更改)')),
                ('pie_radius', models.CharField(default='70%', max_length=30, verbose_name='饼状图半径')),
                ('pie_dataset', models.TextField(default='{data,value} {data,value}', max_length=10000, verbose_name='数据')),
                ('pie_colors', models.CharField(default='一般不填写', max_length=500, null=True, verbose_name='颜色')),
            ],
            options={
                'verbose_name': '饼状图表',
                'verbose_name_plural': '饼状图表',
            },
        ),
        migrations.CreateModel(
            name='TotalTitleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total_title', models.CharField(max_length=100, null=True, verbose_name='数据总标题')),
                ('tm', models.CharField(help_text='以YMD形式输入，例如20180510，表示2018年5月10号', max_length=30, null=True, verbose_name='时间')),
            ],
            options={
                'verbose_name': '大数据标题表',
                'verbose_name_plural': '大数据标题表',
            },
        ),
        migrations.CreateModel(
            name='Vedio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vedio_url', models.CharField(max_length=1000, null=True, verbose_name='视频链接')),
                ('vedio_name', models.CharField(max_length=50, null=True, verbose_name='视频名字')),
                ('vedio_img', models.ImageField(null=True, upload_to='vedioImg', verbose_name='视频配图')),
                ('vedio_time', models.DateTimeField(null=True, verbose_name='发布时间')),
                ('vedio_source', models.CharField(default='就业信息中心', max_length=100, verbose_name='视频来源')),
                ('vedio_views', models.IntegerField(default=0, null=True, verbose_name='浏览次数')),
                ('hot', models.BooleanField(default=False, verbose_name='是否置顶该视频')),
            ],
            options={
                'verbose_name': '视频表',
                'verbose_name_plural': '视频表',
            },
        ),
        migrations.CreateModel(
            name='ViewTimes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times', models.IntegerField(default=0, null=True)),
            ],
        ),
    ]
