from django.db import models


class SiteInfo(models.Model):
    """Singleton-style model — one row holds the editable home-page info widgets."""
    location = models.CharField(max_length=120, default="Bhakra, Himachal Pradesh, India")
    currently_learning = models.CharField(
        max_length=150,
        default="JavaScript — closures, async/await, DOM APIs",
        help_text="Shown in the 'Currently learning' widget on the home page.",
    )

    class Meta:
        verbose_name = "Site Info"
        verbose_name_plural = "Site Info"

    def __str__(self):
        return "Site Info"

    def save(self, *args, **kwargs):
        self.pk = 1  # force single row
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Project(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    tags = models.CharField(max_length=200, help_text="Comma-separated, e.g. Django, DRF, REST API")
    featured = models.BooleanField(default=False, help_text="Show a 'featured' badge on this project")
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.name

    def tag_list(self):
        return [t.strip() for t in self.tags.split(",") if t.strip()]


class Skill(models.Model):
    LEVEL_CHOICES = [
        ("PROFICIENT", "Proficient"),
        ("COMFORTABLE", "Comfortable"),
        ("LEARNING", "Learning"),
    ]
    name = models.CharField(max_length=60)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default="COMFORTABLE")
    percent = models.PositiveIntegerField(default=50, help_text="0-100, used for the progress bar")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.created_at:%Y-%m-%d %H:%M}"
