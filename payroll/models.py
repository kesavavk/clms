from django.db import models
from masterdata.models import Master

class Payroll( models.Model ):
    mastid = models.ForeignKey( Master, on_delete=models.CASCADE )
    divid = models.CharField( max_length=3 )
    secid = models.CharField( max_length=4 )
    wdays = models.FloatField()
    otdays = models.FloatField()
    iomdays = models.FloatField()
    iomotdays = models.FloatField()
    totdays = models.FloatField()
    drate = models.FloatField()
    basic = models.FloatField()
    other = models.FloatField()
    other1 = models.FloatField()
    otamt = models.FloatField()
    wdamt = models.FloatField()
    wdotamt = models.FloatField()
    iomamt = models.FloatField()
    iomotamt = models.FloatField()
    grosse = models.FloatField()
    pfamt = models.FloatField()
    esiamt = models.FloatField()
    ded = models.FloatField()
    othded = models.FloatField()
    netamt = models.FloatField()
    wbasic = models.FloatField()
    iombasic = models.FloatField()
    wpfamt = models.FloatField()
    wesiamt = models.FloatField()
    iompfamt = models.FloatField()
    iomesiamt = models.FloatField()
    wdotheramt = models.FloatField()
    iomotheramt = models.FloatField()
    supcharge = models.FloatField()
    strenth = models.IntegerField()
    pdate = models.DateField()

class incentive( models.Model):
    mastid = models.ForeignKey( Master, on_delete=models.CASCADE )
    wdays = models.FloatField()
    mdate = models.DateField()
    cid = models.CharField( max_length=6 )
    uid = models.CharField( max_length=6 )
    divid = models.CharField( max_length=3 )
    secid = models.CharField( max_length=4 )
    incamt = models.FloatField()
    rpd = models.IntegerField()
    epx = models.FloatField()

class bonus( models.Model ):
    mastid = models.ForeignKey( Master, on_delete=models.CASCADE )
    rndp = models.FloatField()
    drate = models.FloatField()
    basic = models.FloatField()
    date = models.DateField()