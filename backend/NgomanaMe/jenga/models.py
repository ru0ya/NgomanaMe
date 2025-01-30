from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


DIFFICULTY_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        )


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
                'jenga:tutorial_list_by_category',
                args=[self.slug]
                )


class Tutorial(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(unique=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
            Category,
            on_delete=models.CASCADE,
            related_name='tutorials'
            )
    introduction = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    difficulty_level = models.CharField(
            max_length=20,
            choices=DIFFICULTY_CHOICES
            )
    estimated_time = models.PositiveIntegerField(
        help_text="Estimated time in minutes"
        )

    class Meta:
        ordering = ['-created_at']
        indexes = [
                models.Index(fields=['-created_at']),
                models.Index(fields=['slug']),
                ]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('jenga:tutorial_detail', args=[self.slug])


class Step(models.Model):
    tutorial = models.ForeignKey(
            Tutorial,
            related_name='steps',
            on_delete=models.CASCADE
            )
    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    class Meta:
        ordering = ['step_number']
        unique_together = ['tutorial', 'step_number']

    def __str__(self):
        return f"{self.tutorial.title} - Step {self.step_number}"


class Material(models.Model):
    tutorial = models.ForeignKey(
            Tutorial,
            related_name='materials',
            on_delete=models.CASCADE
            )
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    optional = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['-optional', 'name']

    def __str__(self):
        return f"{self.name} ({self.quantity})"


class Comment(models.Model):
    tutorial = models.ForeignKey(
            Tutorial,
            related_name='comments',
            on_delete=models.CASCADE
            )
    author = models.ForeignKey(
            User,
            related_name='comments',
            on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
                models.Index(fields=['-created_at']),
                ]
