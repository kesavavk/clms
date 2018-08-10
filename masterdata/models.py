from django.db import models
import datetime      
class contractor( models.Model ):
    cid = models.CharField( max_length=3, unique=True )
    cname = models.CharField( max_length=100 )
    firmname = models.CharField( max_length=200 )
    vendor_code = models.CharField( max_length= 20 )
    mobile = models.CharField( max_length= 12, null=True )
    strenth = models.IntegerField( null=True )
    licence_id = models.CharField( max_length=30, null=True )
    lic_from = models.DateField( null=True )
    lic_to = models.DateField( null=True )
    lic_strenth = models.IntegerField( null=True )
    pfno = models.CharField( max_length=20, null=True )
    esino = models.CharField( max_length=20, null=True )
    address = models.TextField( max_length=1000, null=True )
    doj = models.DateTimeField(default=datetime.date.today())
    service_type = models.CharField( max_length=10 )
    region = models.CharField( max_length=2 )
    supbasic = models.FloatField( null=True )
    supgross = models.FloatField( null=True )
    commision = models.FloatField( null=True )
    pstrenth = models.IntegerField( null=True )
    pfstatus = models.IntegerField(default=1, null=True)
    cant_status = models.IntegerField(default=1, null=True)
    status = models.IntegerField(default=1, null=True)

    def __str__(self):
        return self.cid

class Master( models.Model ):
    contid = models.ForeignKey( contractor, on_delete=models.CASCADE )
    uid = models.CharField( null=False, max_length=6, primary_key=True )
    def __str__(self):
        return self.uid

class PersonalData( models.Model ):
    mastid = models.ForeignKey( Master, on_delete=models.CASCADE )
    raw_id_fields = ('mastid')
    first_name = models.CharField( max_length=100 )
    last_name = models.CharField( max_length=100 )
    father_name = models.CharField( max_length=100 )
    mother_name = models.CharField( max_length=100 )
    spouse = models.CharField( max_length=100 )
    no_of_children = models.IntegerField()
    dob = models.DateField()
    blood_group = models.CharField( max_length=4 )
    qualification = models.CharField( max_length=50 )
    marital_status = models.CharField( max_length=10 )
    mobile = models.IntegerField()

class orgdata( models.Model ):
    mastid = models.ForeignKey( Master, on_delete=models.CASCADE )
    uid = models.CharField( max_length=6, unique=True )
    doj = models.DateField()
    prevexp = models.FloatField()
    wage = models.IntegerField()
    position = models.CharField( max_length=100 )
    division = models.CharField( max_length=3 )
    section = models.CharField( max_length=4 )
    dept = models.CharField( max_length=4 )
    pfno = models.IntegerField()
    esino = models.IntegerField()
    status = models.IntegerField()
    cant_status = models.IntegerField()
    cant_id = models.CharField( max_length=10 )
    lwd = models.DateField()
    lid = models.DateField()

class address( models.Model ):
    mastid = models.ForeignKey( Master, on_delete=models.CASCADE )
    per_state = models.CharField( max_length=100 )
    per_district = models.CharField( max_length=100 )
    per_city = models.CharField( max_length=100 )
    per_village = models.CharField( max_length=100 )
    per_street = models.CharField( max_length=100 )
    per_hno = models.CharField( max_length=100 )
    state = models.CharField( max_length=100 )
    district = models.CharField( max_length=100 )
    city = models.CharField( max_length=100 )
    village = models.CharField( max_length=100 )
    street = models.CharField( max_length=100 )
    hno = models.CharField( max_length=100 )

class bankdata( models.Model ):
    mastid = models.ForeignKey( Master, on_delete=models.CASCADE )
    acno = models.IntegerField()
    name = models.CharField( max_length=100 )
    branch = models.CharField( max_length=100 )
    ifsc = models.CharField( max_length=11 )

class pfdata( models.Model ):
    mastid = models.ForeignKey( Master, on_delete=models.CASCADE )
    pfno = models.IntegerField()
    uanid = models.CharField( max_length=20 )
    rdate = models.DateField()

class division( models.Model ):
    dname = models.CharField( max_length=200 )
    did = models.CharField( max_length=3 )

class section( models.Model ):
    sname = models.CharField( max_length=200 )
    sid = models.CharField( max_length=4 )
