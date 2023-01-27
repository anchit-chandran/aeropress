from django.db import models

# Create your models here.
class Recipe(models.Model):
    datetime_added = models.DateTimeField(auto_now_add=True)
    coffee_g = models.IntegerField()
    water_brew_ml = models.IntegerField()
    brew_time_s = models.IntegerField()
    milk_ml = models.IntegerField()
    extra_water_ml = models.IntegerField(default=0)
    nausea = models.BooleanField()
    rating = models.IntegerField(
        choices=((1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)),
        default=6
        )

    def __str__(self):
        return str(self.datetime_added)
    
    def get_dict_fields(self):
        return {
            'datetime_added' : self.datetime_added,
            'coffee_g' : self.coffee_g,
            'water_brew_ml' : self.water_brew_ml,
            'brew_time_s' : self.brew_time_s,
            'milk_ml' : self.milk_ml,
            'extra_water_ml' : self.extra_water_ml,
            'nausea' : self.nausea,
            'rating' : self.rating,
        }
