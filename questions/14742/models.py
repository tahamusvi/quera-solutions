from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)


class BlogPost(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='posts')
    date_created = models.DateTimeField(auto_now=True)


    def copy(self):
        new_post = BlogPost(title = self.title,
        body= self.body,
        author= self.author)

        new_post.save()

        comments = self.comments.all()

        for cm in comments:
            new_cm = Comment(blog_post = new_post,
            text=cm.text)
            new_cm.save()

        return new_post.id
        




class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='comments')
    text = models.CharField(max_length=500)

