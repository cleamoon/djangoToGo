# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from termios import VERASE
from django.db import models


class Project(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=50, verbose_name="NAME")
    desc = models.CharField(max_length=1000, verbose_name="DESCRIPTION")
    is_good = models.IntegerField(verbose_name="IS_GOOD")

    class Meta:
        managed = False
        db_table = 'tb_projects'


class Manager(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=20, verbose_name="NAME")
    gender = models.IntegerField(default=True, verbose_name='GENDER')
    birthday = models.DateField(verbose_name="BIRTHDAY")
    desc = models.CharField(max_length=1000, verbose_name="DESCRIPTION")
    photo = models.CharField(max_length=255, verbose_name="PHOTO")
    gcount = models.IntegerField(default=0, db_column='gcount', verbose_name='GOOD_COUNT')
    bcount = models.IntegerField(default=0, db_column='bcount', verbose_name='BAD_COUNT')
    proj = models.ForeignKey(Project, models.DO_NOTHING, db_column='proj_id')

    class Meta:
        managed = False
        db_table = 'tb_managers'

