from django.db import models


class Article_Publish_Blog(models.Manager):
    def published(self):
        return self.filter(is_published=True)

