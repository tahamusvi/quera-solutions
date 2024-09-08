from rest_framework import serializers
from .models import Post,Comment

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField()
    class Meta:
        model=Post
        fields = [
            'title',
            'body',
            'created',
            'owner'

        ]

    def get_owner(self,obj):
            return obj.owner.username

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.SerializerMethodField()
    comment_set = serializers.HyperlinkedRelatedField(
         many=True,
         read_only=True,
         view_name = 'comment_detail'
    )
    class Meta:
        model=Post
        fields =[
            'title',
            'body',
            'created',
            'updated',
            'owner',
            'comment_set'
        ]

    def get_owner(self,obj):
         return obj.owner.username    

    def get_comment_set(self,obj):
        return obj.comment.all()   




class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
         view_name='post_detail',
         read_only=True
    )
    owner = serializers.CharField(source='owner.username',read_only=True)
    class Meta:
         model=Comment
         fields = ['post','owner','body','created','updated']