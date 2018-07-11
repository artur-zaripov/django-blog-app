from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Article


class UserSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True, queryset=Article.objects.all())

    class Meta:
        model = User
        fields = ['username', 'articles']


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(required=True)
    text = serializers.CharField(required=True, max_length=2000)
    pub_date = serializers.DateTimeField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', instance.user)
        instance.text = validated_data.get('text', instance.text)
        instance.pub_date = validated_data.get('pub_date', instance.pub_date)

        instance.save()
        return instance
