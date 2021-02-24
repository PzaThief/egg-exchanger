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
        db_table = "cryptocurrency_from_bithumb"
        app_label = "dataforapi"


class FinancialProductsFromKrx(models.Model):
    product = models.CharField(max_length=50, blank=True, null=True)
    ticker = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50, blank=True, null=True)
    count_unit = models.CharField(max_length=50, blank=True, null=True)
    time_fromapi = models.DateTimeField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "financial_products_from_krx"
        app_label = "dataforapi"


class Miscellaneous(models.Model):
    unit_name = models.CharField(primary_key=True, max_length=50)
    count_unit = models.CharField(max_length=50, blank=True, null=True)
    price_unit = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    update_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "miscellaneous"
        app_label = "dataforapi"


class MoneyExchangeFromKoreaexim(models.Model):
    cur_unit = models.CharField(db_column="CUR_UNIT", primary_key=True, max_length=50)  # Field name made lowercase.
    cur_nm = models.CharField(db_column="CUR_NM", max_length=50, blank=True, null=True)  # Field name made lowercase.
    ttb = models.FloatField(db_column="TTB", blank=True, null=True)  # Field name made lowercase.
    tts = models.FloatField(db_column="TTS", blank=True, null=True)  # Field name made lowercase.
    deal_bas_r = models.FloatField(db_column="DEAL_BAS_R", blank=True, null=True)  # Field name made lowercase.
    bkpr = models.FloatField(db_column="BKPR", blank=True, null=True)  # Field name made lowercase.
    yy_efee_r = models.FloatField(db_column="YY_EFEE_R", blank=True, null=True)  # Field name made lowercase.
    ten_dd_efee_r = models.FloatField(db_column="TEN_DD_EFEE_R", blank=True, null=True)  # Field name made lowercase.
    kftc_deal_bas_r = models.FloatField(
        db_column="KFTC_DEAL_BAS_R", blank=True, null=True
    )  # Field name made lowercase.
    kftc_bkpr = models.FloatField(db_column="KFTC_BKPR", blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateTimeField()
    time_fromapi = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "money_exchange_from_koreaexim"
        app_label = "dataforapi"


class NormalizationUnit(models.Model):
    unit_category = models.CharField(max_length=50, blank=True, null=True)
    unit_name = models.CharField(primary_key=True, max_length=50)
    count_unit = models.CharField(max_length=50, blank=True, null=True)
    price_unit = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    fromurl = models.CharField(max_length=50, blank=True, null=True)
    update_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "normalization_unit"
        app_label = "dataforapi"
