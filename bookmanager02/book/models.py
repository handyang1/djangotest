from django.db import models


# Create your models here.
class BookInfo(models.Model):
    name = models.CharField(max_length=10, unique=True, verbose_name='mingzi')
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'
        verbose_name = 'shujiguanli'

    def __str__(self):
        return self.name  # 返回书名作为显示内容


class PeopleInfo(models.Model):
    GENDER_CHOICE = (
        (1, 'MALE'),
        (2, 'FEMALE')
    )
    name = models.CharField(max_length=10, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)

    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    class Meta:
        db_table='peopleinfo'
