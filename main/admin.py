from django.contrib import admin
from .models import PartnerType, Partner, ProductType, Product, MaterialType, PartnerProduct, ProductPriceHistory


@admin.register(PartnerType)
class PartnerTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'partner_type', 'director', 'phone', 'email', 'inn', 'rating']
    list_filter = ['partner_type', 'rating']
    search_fields = ['name', 'director', 'inn', 'email']
    ordering = ['name']


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'coefficient']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'article', 'product_type', 'min_price']
    list_filter = ['product_type']
    search_fields = ['name', 'article']
    ordering = ['name']


@admin.register(MaterialType)
class MaterialTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'defect_percentage']
    search_fields = ['name']


@admin.register(PartnerProduct)
class PartnerProductAdmin(admin.ModelAdmin):
    list_display = ['partner', 'product', 'quantity', 'sale_date']
    list_filter = ['sale_date', 'partner']
    search_fields = ['partner__name', 'product__name']
    date_hierarchy = 'sale_date'


@admin.register(ProductPriceHistory)
class ProductPriceHistoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'old_price', 'new_price', 'changed_at', 'changed_by']
    list_filter = ['changed_at']
    date_hierarchy = 'changed_at'
