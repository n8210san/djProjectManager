from django.db import models
from django.urls import reverse


class MyModelName(models.Model):
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    class Meta:
        ordering = ['-my_field_name']
    def get_absolute_url(self):
         return reverse('model-detail-view', args=[str(self.id)])
    def __str__(self):
        return self.field_name


# ***** ***** ***** 詳細說明如下 ***** ***** *****

class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields 字段
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    # ...
    """ 字段 就是欄位名稱. 
    可以被指定一個參數（verbose_name）, 或是默認 大寫字段的變量名的第一個字母，並用空格替換下劃線
    （例如 my_field_name 的默認標籤為 My field name ）

    常用字段參數：  完整的字段選項 https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-options

help_text :提供HTML表單文本標籤(eg i在管理站點中),如上所述。
verbose_name :字段標籤中的可讀性名稱，如果沒有被指定，Django將從字段名稱推斷默認的詳細名稱。
default :該字段的默認值。這可以是值或可呼叫物件(callable object)，在這種情況下，每次創建新紀錄時都將呼叫該物件。
null：如為 True，即允許 Django 於資料庫該欄位寫入 NULL（但欄位型態如為 CharField 則會寫入空字串）。預設值是 False。
blank :如果True，表單中的字段被允許為空白。默認是False，這意味著Django的表單驗證將強制你輸入一個值。這通常搭配 NULL=True 使用，因為如果要允許空值，你還希望數據庫能夠適當地表示它們。
choices :這是給此字段的一組選項。如果提供這一項，預設對應的表單部件是「該組選項的列表」，而不是原先的標准文本字段。
primary_key :如果是True，將當前字段設置為模型的主鍵（主鍵是被指定用來唯一辨識所有不同表記錄的特殊數據庫欄位(column)）。如果沒有指定字段作為主鍵，則Django將自動為此添加一個字段。

    常用字段類型：  完整列表 https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types

CharField 是用來定義短到中等長度的字段字符串。你必須指定max_length要存儲的數據。
TextField 用於大型任意長度的字符串。你可以max_length為該字段指定一個字段，但僅當該字段以表單顯示時才會使用（不會在數據庫級別強制執行）。
IntegerField 是一個用於存儲整數（整數）值的字段，用於在表單中驗證輸入的值為整數。
DateField 和DateTimeField 用於存儲／表示日期和日期／時間信息（分別是Python.datetime.date 和 datetime.datetime 對象）。這些字段可以另外表明（互斥）參數 auto_now=Ture （在每次保存模型時將該字段設置為當前日期），auto_now_add（僅設置模型首次創建時的日期）和 default（設置默認日期，可以被用戶覆蓋）。
EmailField 用於存儲和驗證電子郵件地址。
FileField 和ImageField 分別用於上傳文件和圖像（ImageField 只需添加上傳的文件是圖像的附加驗證）。這些參數用於定義上傳文件的存儲方式和位置。
AutoField 是一種 IntegerField 自動遞增的特殊類型。如果你沒有明確指定一個主鍵，則此類型的主鍵將自動添加到模型中。
ForeignKey 用於指定與另一個數據庫模型的一對多關係（例如，汽車有一個製造商，但製造商可以製作許多汽車）。關係的“一”側是包含密鑰的模型。
ManyToManyField 用於指定多對多關係（例如，一本書可以有幾種類型，每種類型可以包含幾本書）。在我們的圖書館應用程序中，我們將非常類似地使用它們 ForeignKeys，但是可以用更複雜的方式來描述組之間的關係。這些具有參數 on_delete 來定義關聯記錄被刪除時會發生什麼（例如，值 models.SET_NULL 將簡單地設置為值 NULL ）。
還有許多其他類型的字段，包括不同類型數字的字段（大整數，小整數，浮點數），布林值，URLs，唯一 ids 和其他 “時間相關” 的信息（持續時間，時間等）。你可以查閱完整列表 .
    """

    # Metadata 元數據
    class Meta:
        ordering = ['-my_field_name']
        verbose_name = 'BetterName'

    """ 通過宣告 class Meta 來宣告 元數據
    最有用的功能之一是控制在查詢模型類型時返回之記錄的默認排序
    """

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.).
        為每個物件返回一個人類可讀的字符串
        """
        return self.field_name


""" 創建和修改記錄
要創建一個記錄，你可以定義一個模型實例，然後呼叫 save()。
"""
# Create a new record using the model's constructor.
record = MyModelName(my_field_name="Instance #1")

# Save the object into the database.
record.save()
# 如果沒有任何的欄位被宣告為主鍵，這筆新的紀錄會被自動的賦予一個主鍵並將主鍵欄命名為 id
# 透過「點(dot)的語法」取得或變更這筆新資料的欄位
print(record.id)  # should return 1 for the first record.
print(record.my_field_name)  # should print 'Instance #1'

record.my_field_name = "New Instance Name"
record.save()
# 呼叫 save() 將變更過的資料存進資料庫。

""" 搜尋紀錄
"""


class Book(models.Model):
    title = models.CharField(max_length=20, help_text='book name')
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.field_name



# QuerySet 是一個可迭代的物件，使用 objects.all() 取得
all_books = Book.objects.all()

# filter()
wild_books = Book.objects.filter(title__contains='wild')
number_wild_books = Book.objects.filter(title__contains='wild').count()
""" 使用這個格式：比對字段__比對方法 (請注意上方範例中的 title 與 contains 中間隔了兩個底線唷)
# 還有很多比對方式可以使用： icontains (不區分大小寫), iexact (大小寫區分且完全符合), exact (不區分大小寫但完全符合) 還有 in, gt (大於), startswith ... 
 https://docs.djangoproject.com/en/2.0/ref/models/querysets/#field-lookups

 有時候你會須要透過某個一對多的字段來篩選(例如一個 外鍵)。 這樣的狀況下，你可以使用兩個底線來指定相關模型的字段。例如透過某個特定的genre名稱篩選書籍，如下所示：
"""
# 會比對到: Fiction, Science fiction, non-fiction etc.
books_containing_genre = Book.objects.filter(genre__name__icontains='fiction')
"""你可隨心地使用雙底線 (__) 來探索更多層的關係 (ForeignKey/ManyToManyField).
例如, 一本 Book 有許多不同的 types, 其進一步定義有參數 name 關聯的"cover"：type__cover__name__exact='hard'.
還有很多是你可以用索引(queries)來做的，包含從相關的模型做向後查詢(backwards searches)、連鎖過濾器(chaining filters)、回傳「值的小集合」等。更多資訊可以到 Making queries (Django Docs) 查詢。
"""


# ***** ***** ***** 資料庫遷移 @ terminal ***** ***** *****
"""
運行資料庫遷移
# makemigrations 創建（但不實施）項目中安裝的所有應用程序的遷移（你可以指定應用程序名稱，也可以為單個項目運行遷移）
python3 manage.py makemigrations
# migrate 命令，真正對你的資料庫實施遷移
python3 manage.py migrate
重要: 每次模型改變，都需要運行以上命令，來影響需要存放的數據結構（包括添加和刪除整個模型和單個字段）
"""
