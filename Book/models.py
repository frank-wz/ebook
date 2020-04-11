from django.db import models

# Create your models here.

__all__ = ["Book", "Author", "AccessCode", 'Tag']

FIRST_CATEGORY_LIST = ((1, '文学'), (2, '人文社科'), (3, '经济管理'), (4, '科技科普'), (5, '计算机于互联网'),(6, '成功励志'),
                       (7, '生活'), (8, '少儿'), (9, '艺术设计'), (10, '漫画绘本'), (11, '教育考试'), (12, '杂志'),(13, '小说'))

TAG_LIST = ((1, '投资'), (2, '短篇'), (3, '文化'), (4, '政治'), (5, '大家小书'), (6, '心理学'), (7, '旅行'),
            (8, '恋爱'), (9, '书单'), (10, '三毛'), (11, '学习'), (12, '中篇'), (13, '经典'), (14, '长篇'), (15, '诗词'),
            (16, '创业'), (17, '阅读'), (18, '文艺'), (19, '散文'), (20, '哲学'), (21, '下载'), (22, '外国文学'),
            (23, '人物'), (24, '日本'), (25, '心灵'), (26, '励志'), (27, '生活'), (28, '合集'), (29, '中国'), (30, '必读'),
            (31, '随笔'), (32, '社会'), (33, '英国'), (34, '经济'), (35, '思享'), (36, '青春'), (37, '爱情'), (38, '成长'),
            (39, '文学'), (40, '小说'), (41, '美国'), (42, '历史'), (43, '情感'), (44, '人生'),(45, '古典'))


class Book(models.Model):
    """图书表"""
    title = models.CharField(max_length=128, verbose_name="图书的名称")
    # course_img = models.ImageField(upload_to="course/%Y-%m", verbose_name='图书的图片')
    book_img = models.CharField(max_length=255, verbose_name='图书的图片', help_text="图片网址链接")
    authors = models.ManyToManyField(verbose_name='作者', to='Author')

    brief = models.CharField(verbose_name="图书简介", max_length=1024)
    pub_date = models.DateField(verbose_name="上架日期", auto_now_add=True)
    isbn = models.CharField('ISBN', max_length=32)
    issn = models.CharField('ISSN', max_length=32, blank=True, null=True)
    bpan_link = models.CharField('网盘链接', max_length=255)
    bpan_code = models.CharField('提取码', max_length=8)
    foreign_book_name = models.CharField(verbose_name='外文书名', max_length=64, blank=True, null=True)
    LANGUAGE_CHOICES = ((0, '中文'), (1, '英语'))
    language = models.SmallIntegerField(verbose_name="语言", choices=LANGUAGE_CHOICES, default=0)
    order = models.IntegerField("图书顺序", help_text="从上一个图书数字往后排")

    first_category = models.SmallIntegerField(verbose_name="一级分类", choices=FIRST_CATEGORY_LIST)

    # book_tag = models.SmallIntegerField('标签', choices=TAG_LIST, default=0)
    tags = models.ManyToManyField(to='Tag', blank=True, null=True)
    # 相关图书
    related_books = models.ManyToManyField(to="Book", blank=True, null=True)
    # is_free = models.BooleanField(default=True)

    editer = models.CharField(verbose_name='编者', max_length=64, blank=True, null=True)
    proofreader = models.CharField(verbose_name='译者', max_length=64, blank=True, null=True)
    remarker = models.CharField(verbose_name='校对', max_length=64, blank=True, null=True)
    transfer = models.CharField(verbose_name='译者', max_length=64, blank=True, null=True)
    drawer = models.CharField(verbose_name='绘者', max_length=64, blank=True, null=True)
    publishers = models.CharField(verbose_name='出版社', max_length=64, blank=True, null=True)
    publish_no = models.CharField(verbose_name='出版社号', max_length=64, blank=True, null=True)
    series = models.CharField(verbose_name='丛书名', max_length=64, blank=True, null=True)
    brand = models.CharField(verbose_name='品牌', max_length=64, blank=True, null=True)
    format = models.CharField(verbose_name='格式', max_length=64, blank=True, null=True)
    packages = models.CharField(verbose_name='包装', max_length=64, blank=True, null=True)
    pages = models.CharField(verbose_name='页数', max_length=64, blank=True, null=True)
    batch_no = models.CharField(verbose_name='版次', max_length=64, blank=True, null=True)
    publish_time = models.CharField(verbose_name='出版时间', max_length=64, blank=True, null=True)
    print_no = models.SmallIntegerField(verbose_name='印次', blank=True, null=True)
    print_time = models.CharField(verbose_name='印刷时间', max_length=64, blank=True, null=True)
    size_and_height = models.CharField(verbose_name='尺寸及重量', max_length=64, blank=True, null=True)
    china_catalog = models.CharField(verbose_name='中国法分类号', max_length=64, blank=True, null=True)
    sheet = models.CharField(verbose_name='印张', max_length=64, blank=True, null=True)
    papers = models.CharField(verbose_name='用纸', max_length=64, blank=True, null=True)
    attachment = models.CharField(verbose_name='附件', max_length=64, blank=True, null=True)
    attachment_num = models.SmallIntegerField(verbose_name='附件数量', blank=True, null=True)
    pack_num = models.SmallIntegerField(verbose_name='套装数量', blank=True, null=True)
    letters = models.SmallIntegerField(verbose_name='字数', blank=True, null=True)
    bar_code = models.CharField(verbose_name='条形码', max_length=64, blank=True, null=True)
    keywords = models.CharField(verbose_name='主题词', max_length=64, blank=True, null=True)
    pick_state = models.CharField(verbose_name='捡货标记', max_length=64, blank=True, null=True)
    compile = models.CharField(verbose_name='编纂', max_length=64, blank=True, null=True)
    photography = models.CharField(verbose_name='摄影', max_length=64, blank=True, null=True)
    dictation = models.CharField(verbose_name='口述', max_length=64, blank=True, null=True)
    read = models.CharField(verbose_name='朗读', max_length=64, blank=True, null=True)
    finishing = models.CharField(verbose_name='整理', max_length=64, blank=True, null=True)
    write = models.CharField(verbose_name='书写', max_length=64, blank=True, null=True)

    jdPrice = models.SmallIntegerField(verbose_name='原价', blank=True, null=True)
    martPrice = models.SmallIntegerField(verbose_name='当前价', blank=True, null=True)
    skuId = models.CharField(verbose_name='商品编号', max_length=64, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "图书表"
        # db_table = verbose_name
        verbose_name_plural = verbose_name
        # ordering = ['-pub_date']


class Author(models.Model):
    """作者表"""
    name = models.CharField(max_length=32, verbose_name="作者名字")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "作者表"
        # db_table = verbose_name
        verbose_name_plural = verbose_name

class AccessCode(models.Model):
    """验证码"""
    access_code = models.CharField(max_length=32,unique=True)

    def __str__(self):
        return self.access_code

    class Meta:
        verbose_name = "验证码"
        # db_table = verbose_name
        verbose_name_plural = verbose_name


class Tag(models.Model):
    '''标签'''
    name = models.CharField(max_length=12)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        # db_table = verbose_name
        verbose_name_plural = verbose_name