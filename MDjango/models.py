# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Root(models.Model):
    name = models.CharField(primary_key=True, max_length=45)
    passwd = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'root'
        unique_together = (('name', 'passwd'),)


class Student(models.Model):
    no = models.IntegerField(db_column='No', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    chinese = models.IntegerField(db_column='Chinese', blank=True, null=True)  # Field name made lowercase.
    math = models.IntegerField(db_column='Math', blank=True, null=True)  # Field name made lowercase.
    english = models.IntegerField(db_column='English', blank=True, null=True)  # Field name made lowercase.
    sport = models.IntegerField(db_column='Sport', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'student'
        unique_together = (('no', 'name'),)