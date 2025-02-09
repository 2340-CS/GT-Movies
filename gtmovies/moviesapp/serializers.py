class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_name', 'description', 'duration', 'price', 'rating_type', 'rating', 'genre']