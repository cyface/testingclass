from django.db.models import Model, CharField, ForeignKey, DO_NOTHING


class List(Model):
    name = CharField(max_length=5)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/list/{self.id}/"


class Item(Model):
    title = CharField(max_length=5)
    list = ForeignKey(to=List, on_delete=DO_NOTHING)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/item/{self.id}/"
