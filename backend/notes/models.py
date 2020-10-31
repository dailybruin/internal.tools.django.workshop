from django.db import models

# Note:
# title
# body

# Note table
# title (string)  |   body (string)

class Note(models.Model):
	title = models.CharField(max_length=30)
	body = models.CharField(max_length=400)

