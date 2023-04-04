from django.db import models
from django.urls import reverse


# Create your models here.
class Men(models.Model):
        title=models.CharField(max_length=255, verbose_name='Заголовок')
        slug=models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
        content=models.TextField(blank=True, verbose_name='Текст статьи')
        photo=models.ImageField(upload_to='photos/%Y/%m/$d/', verbose_name='Фото')
        time_create=models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
        time_update=models.DateTimeField(auto_now=True, verbose_name='Вреья обновления')
        is_published=models.BooleanField(verbose_name='Публикация', default=True)
        cat=models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория',null=True)


        def __str__(self):
                return self.title

        def get_absolute_url(self):
                return reverse('post', kwargs={'post_slug': self.slug})

        class Meta:
                verbose_name='Известный мужчина'
                verbose_name_plural = 'Известные мужчины'
                ordering=['time_create', 'title']


class Category(models.Model):
        name=models.CharField(max_length=100, db_index=True, verbose_name='Название категории')
        slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

        def get_absolute_url(self):
                return reverse('category', kwargs={'cat_slug': self.slug})


        def __str__(self):
                return self.name

        class Meta:
                verbose_name='Категория'
                verbose_name_plural='Категории'