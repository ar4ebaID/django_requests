import os
from django.db import models
from simple_history.models import HistoricalRecords


class Request(models.Model):
    Customers_full_name = models.CharField(max_length=50, verbose_name='Customer', blank=False)
    Lecture_hall = models.CharField(max_length=10, verbose_name='Office', blank=False)
    Description = models.TextField(max_length=150, blank=True, verbose_name='Description')
    Work = models.ForeignKey('Type_of_work_list', on_delete=models.DO_NOTHING, verbose_name='Type of work', blank=False)
    Performer = models.ForeignKey('Full_name_of_the_performer_list', on_delete=models.DO_NOTHING,
                                  verbose_name='Executor', blank=False)
    Comment = models.TextField(max_length=150, blank=True, verbose_name='Comment from the performer')
    Files = models.FileField(upload_to='./static' + '/files' + '/%Y/%m/%d/', verbose_name='File upload', blank=True)
    Request_date = models.DateTimeField(auto_now_add=True, verbose_name='Request date')
    Condition = models.ForeignKey('Condition_list', on_delete=models.DO_NOTHING, verbose_name='Condition', blank=False)
    History = HistoricalRecords()

    def __str__(self):
        return f"{self.Customers_full_name}"

    def get_absolute_url(self):
        return '/'

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Requests'
        verbose_name_plural = 'Requests'


class Type_of_work_list(models.Model):
    Type_of_work = models.CharField(max_length=50, db_index=True, unique=True, verbose_name='Type of work')
    History = HistoricalRecords()

    def __str__(self):
        return f"{self.Type_of_work}"

    class Meta:
        verbose_name = 'Types of work'
        verbose_name_plural = 'Types of work'
        ordering = ['Type_of_work']


class Condition_list(models.Model):
    Condition = models.CharField(max_length=15, db_index=True, verbose_name='Condition')
    History = HistoricalRecords()

    def __str__(self):
        return self.Condition

    class Meta:
        verbose_name = 'Conditions'
        verbose_name_plural = 'Conditions'
        ordering = ['Condition']


class Full_name_of_the_performer_list(models.Model):
    Full_name_of_the_performer = models.CharField(max_length=50, db_index=True, unique=True, verbose_name='Full name performer')
    History = HistoricalRecords()

    def __str__(self):
        return f"{self.Full_name_of_the_performer}"

    class Meta:
        verbose_name = 'Performers'
        verbose_name_plural = 'Performers'
        ordering = ['Full_name_of_the_performer']