from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

LISTENS = (
    ('Y', 'Yes'),
    ('N', 'No')
)

class Playlist(models.Model):
  name = models.CharField(max_length=50)
  vibe = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('playlists_detail', kwargs={'pk': self.id})

class Banger(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    hypeness = models.IntegerField()
    playlists = models.ManyToManyField(Playlist)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'banger_id': self.id})

    def listened_for_today(self):
        return self.listening_set.filter(date=date.today()).count() >= len(LISTENS)


class Listening(models.Model):
    date = models.DateField('listening date')
    listen = models.CharField(
        max_length=1,
            choices=LISTENS,
            default=LISTENS[0][0]
    )
    
    banger = models.ForeignKey(Banger, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_listen_display()} on {self.date}"

    class Meta:
        ordering = ['-date']




    


