from django.db import models

class RetailData(models.Model):
    Market = models.CharField(max_length=100)
    Channel = models.CharField(max_length=100)
    Region = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    SubCategory = models.CharField(max_length=100)
    Brand = models.CharField(max_length=100)
    Variant = models.CharField(max_length=100)
    PackType = models.CharField(max_length=100)
    PPG = models.CharField(max_length=100)
    PackSize = models.CharField(max_length=50)
    Year = models.IntegerField()
    Month = models.IntegerField()
    Week = models.IntegerField()
    Date = models.DateField()
    BrCatId = models.CharField(max_length=100)

    SalesValue = models.FloatField()
    Volume = models.FloatField()
    VolumeUnits = models.CharField(max_length=50)

    # Display (D1–D6), Availability (AV1–AV6), and Execution (EV1–EV6)
    D1 = models.FloatField(null=True, blank=True)
    D2 = models.FloatField(null=True, blank=True)
    D3 = models.FloatField(null=True, blank=True)
    D4 = models.FloatField(null=True, blank=True)
    D5 = models.FloatField(null=True, blank=True)
    D6 = models.FloatField(null=True, blank=True)

    AV1 = models.FloatField(null=True, blank=True)
    AV2 = models.FloatField(null=True, blank=True)
    AV3 = models.FloatField(null=True, blank=True)
    AV4 = models.FloatField(null=True, blank=True)
    AV5 = models.FloatField(null=True, blank=True)
    AV6 = models.FloatField(null=True, blank=True)

    EV1 = models.FloatField(null=True, blank=True)
    EV2 = models.FloatField(null=True, blank=True)
    EV3 = models.FloatField(null=True, blank=True)
    EV4 = models.FloatField(null=True, blank=True)
    EV5 = models.FloatField(null=True, blank=True)
    EV6 = models.FloatField(null=True, blank=True)

    PrepDate = models.DateField()

    def __str__(self):
        return f"{self.Brand} - {self.Year}-{self.Month}"
