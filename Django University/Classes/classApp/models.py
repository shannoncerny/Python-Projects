from django.db import models

# Create your models here.
class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default='', blank=True, null=False)
    course_number = models.IntegerField(default='', blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default='', blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

    # CREATES MODEL MANAGER
    object = models.Manager()

    # Displays object output values in string form
    def __str__(self):
        # returns input value of title and instructor name field as a tuple
        # to display in the browser instead of default titles
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)

    # Removes added 's' that Django adds to model name in browser display
    class Meta:
        verbose_name_plural = 'University Classes'
