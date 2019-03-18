from django.db import models

# Create your models here.
class Location(models.Model):
    image_location = models.CharField(max_length =30)
    def save_location(self):
        self.save()

    def __str__(self):
        return self.image_location

class Category(models.Model):
    image_category = models.CharField(max_length=50)
    def save_category(self):
        self.save()
    def __str__(self):
        return self.image_category

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length=30)
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ManyToManyField(Category)
    # phone_number = models.CharField(max_length = 10,blank =True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    # def display_image(self):
    #     self.save()

    def update_image(self):
        self.update()

    # @classmethod
    # def all_images(cls):
    #     return Image.objects.all()
        


    @classmethod
    def get_image_by_id(cls, id):
        images = Image.objects.get(id=id)
        return images

    @classmethod
    def search_image(cls,search_category):
        images_category = Image.objects.filter(category__image_category__icontains=search_category)
        return images_category

    @classmethod
    def search_img(cls,search_location):
        images_location = Image.objects.filter(location__image_location__icontains=search_location)
        return images_location

   