from django.db import models

# bug type choices as an iterable
BUG_TYPE = (
    ("error", "error"),
    ("new feature", "new feature")
)

# bug status choices
STATUS = (
    ("to do", "to do"),
    ("in progress", "in progress"),
    ("done", "done")
)

# Create your models here.
class Bug(models.Model):
    description = models.TextField(max_length=200)
    bug_type = models.CharField(max_length=20, choices=BUG_TYPE, default="error")
    report_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS, default="to do")

