from django.db import models
from masterdata.models import Master
class attendance( models.Model ):
    mastid = models.ForeignKey( Master, on_delete=models.CASCADE )
    indate = models.DateField()
    outdate = models.DateField()
    indate_intime = models.DateTimeField( auto_now_add=False, blank=True )
    outdate_outtime = models.DateTimeField( auto_now_add=False, blank=True )
    shift = models.CharField( max_length=2 )
    divid = models.CharField( max_length=3 )
    secid = models.CharField( max_length=4 )
    wtype = models.CharField( max_length=4 )