# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CryptocurrencyFromBithumb(models.Model):
    payment_currency = models.CharField(max_length=50, blank=True, null=True)
    order_currency = models.CharField(max_length=50, blank=True, null=True)
    bids_asks = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    time_fromapi = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cryptocurrency_from_bithumb'


class FinancialProductsFromKrx(models.Model):
    product = models.CharField(max_length=50, blank=True, null=True)
    ticker = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    count_unit = models.CharField(max_length=50, blank=True, null=True)
    time_fromapi = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'financial_products_from_krx'


class Miscellaneous(models.Model):
    unit_name = models.CharField(max_length=50, blank=True, null=True)
    count_unit = models.CharField(max_length=50, blank=True, null=True)
    price = models.CharField(max_length=50, blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'miscellaneous'


class MoneyExchangeFromKoreaexim(models.Model):
    result = models.IntegerField(db_column='RESULT', blank=True, null=True)  # Field name made lowercase.
    cur_unit = models.CharField(db_column='CUR_UNIT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cur_nm = models.CharField(db_column='CUR_NM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ttb = models.CharField(db_column='TTB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tts = models.CharField(db_column='TTS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    deal_bas_r = models.CharField(db_column='DEAL_BAS_R', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bkpr = models.CharField(db_column='BKPR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yy_efee_r = models.CharField(db_column='YY_EFEE_R', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ten_dd_efee_r = models.CharField(db_column='TEN_DD_EFEE_R', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kftc_deal_bas_r = models.CharField(db_column='KFTC_DEAL_BAS_R', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kftc_bkpr = models.CharField(db_column='KFTC_BKPR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField()
    time_fromapi = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'money_exchange_from_koreaexim'


class NormalizationUnit(models.Model):
    unit_name = models.CharField(max_length=50, blank=True, null=True)
    count_unit = models.CharField(max_length=50, blank=True, null=True)
    price_unit = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fromurl = models.CharField(max_length=50, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'normalization_unit'
