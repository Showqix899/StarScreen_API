from django.db import models

# Create your models here.

#from python
import uuid


#Movie Data Table

class Movie(models.Model):


    #movie Genre
    genre_type=[("ACTION","Action"),("FANTASY","Fantasy"),("SCIENCE FICTION","Science Fiction"),
    ("ROMANCE","Romance"),("DOCUMENTRY","Documentry"),("DRAMA","Drama"),("ANIME","ANIME"),("ANIMATION","Animation"),
    ("MYSTERY","Mystery"),("HORROR","Horror"),("THRILLER","Thriller"),("WESTERN","Westerm"),("WAR","War")
    ,("SPORTS","Sports"),("Biography","Biography")]

    # according  Motion Picture Association film age rating system
    types_of_movies=[("G","General Audiences"),("PG","Parental Guidance Suggested"),("PG-13","Parents Strongly Cautioned"),
    ("R","Restricted"),("NC-17","Adults Only")]

    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    title=models.CharField(max_length=220,null=True,blank=True)
    description=models.TextField()
    run_time=models.TimeField()
    production_home=models.CharField(max_length=220,null=True,blank=True)
    release_date=models.DateTimeField()
    imdb_rating=models.DecimalField(max_digits=4,decimal_places=2)
    rotten_tomato=models.CharField(max_length=20,blank=True,null=True)
    Director=models.CharField(max_length=220,null=True,blank=True)
    genre=models.CharField(max_length=30,choices=genre_type)
    expiration=models.DateTimeField()
    
    actor=models.CharField(max_length=100,null=True,blank=True)
    actress=models.CharField(max_length=100,null=True,blank=True)
    movie_type=models.CharField(max_length=30,choices=types_of_movies)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)


    def __str__(self):
        return self.title


    

