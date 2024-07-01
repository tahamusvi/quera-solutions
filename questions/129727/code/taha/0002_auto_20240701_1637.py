from django.db import migrations
from django.utils import timezone
import django
from django.db import migrations, models
from django.db import transaction
from django.conf import settings
from django.db.models import F


@transaction.atomic
def set_category_title(apps, schema_editor):
    Article = apps.get_model('blog', 'Article')
    Category = apps.get_model('blog', 'Category')

    # برای هر مقاله موجود
    for article in Article.objects.all():
        # اگر فیلد category خالی نباشد
        if article.category:
            # ایجاد یا بروزرسانی شئ Category با تایتل برابر مقدار قبلی فیلد category
            category, created = Category.objects.get_or_create(title=article.category)
            # تغییر فیلد category مقاله به شئ Category جدید ایجاد شده
            article.category = category.id
            article.save()

@transaction.atomic
def set_author(apps, schema_editor):
    Article = apps.get_model('blog', 'Article')
    User = apps.get_model(settings.AUTH_USER_MODEL)

    for article in Article.objects.all():
        if article.author:

            author = User.objects.get(username=article.author)
            article.author = author.id
            article.save()

@transaction.atomic
def set_published(apps, schema_editor):
    Article = apps.get_model('blog', 'Article')

    Article.objects.update(published=F('created'), updated=F('created'))



class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.RunPython(set_category_title),
        migrations.RunPython(set_author),
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.DateTimeField(default=timezone.now),
        ),
        migrations.AddField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.RunPython(set_published),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('p', 'publish'), ('d', 'draft')], default='d', max_length=1),
        ),
        
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category'),
        ),
        
    ]
