from django.db import models
from django.contrib.auth.models import User


class PartnerType(models.Model):
    """Тип партнера (ЗАО, ООО, ПАО, ОАО)"""
    name = models.CharField(max_length=10, unique=True, verbose_name='Тип партнера')

    class Meta:
        verbose_name = 'Тип партнера'
        verbose_name_plural = 'Типы партнеров'

    def __str__(self):
        return self.name


class Partner(models.Model):
    """Партнеры компании"""
    partner_type = models.ForeignKey(PartnerType, on_delete=models.PROTECT, verbose_name='Тип партнера')
    name = models.CharField(max_length=255, verbose_name='Наименование партнера')
    director = models.CharField(max_length=255, verbose_name='Директор')
    email = models.EmailField(verbose_name='Электронная почта')
    phone = models.CharField(max_length=50, verbose_name='Телефон')
    address = models.TextField(verbose_name='Юридический адрес')
    inn = models.CharField(max_length=12, unique=True, verbose_name='ИНН')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_total_sales(self):
        """Общий объем продаж партнера"""
        total = PartnerProduct.objects.filter(partner=self).aggregate(
            total=models.Sum('quantity')
        )['total']
        return total or 0


class ProductType(models.Model):
    """Тип продукции с коэффициентом"""
    name = models.CharField(max_length=100, unique=True, verbose_name='Тип продукции')
    coefficient = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Коэффициент типа продукции')

    class Meta:
        verbose_name = 'Тип продукции'
        verbose_name_plural = 'Типы продукции'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Продукция компании"""
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT, verbose_name='Тип продукции')
    name = models.CharField(max_length=255, verbose_name='Наименование продукции')
    article = models.CharField(max_length=50, unique=True, verbose_name='Артикул')
    min_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Минимальная стоимость для партнера')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Изображение')

    # Дополнительные поля из ТЗ
    length = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Длина упаковки')
    width = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Ширина упаковки')
    height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Высота упаковки')
    weight_without_pack = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True, verbose_name='Вес без упаковки')
    weight_with_pack = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True, verbose_name='Вес с упаковкой')
    production_time = models.IntegerField(blank=True, null=True, verbose_name='Время изготовления (мин)')
    cost_price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name='Себестоимость')

    class Meta:
        verbose_name = 'Продукция'
        verbose_name_plural = 'Продукция'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.article})"


class MaterialType(models.Model):
    """Тип материала с процентом брака"""
    name = models.CharField(max_length=100, verbose_name='Тип материала')
    defect_percentage = models.DecimalField(max_digits=5, decimal_places=4, verbose_name='Процент брака материала')

    class Meta:
        verbose_name = 'Тип материала'
        verbose_name_plural = 'Типы материалов'

    def __str__(self):
        return self.name


class PartnerProduct(models.Model):
    """История реализации продукции партнерам"""
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name='Партнер')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукция')
    quantity = models.IntegerField(verbose_name='Количество продукции')
    sale_date = models.DateField(verbose_name='Дата продажи')

    class Meta:
        verbose_name = 'Продажа партнеру'
        verbose_name_plural = 'История продаж партнерам'
        ordering = ['-sale_date']

    def __str__(self):
        return f"{self.partner.name} - {self.product.name} ({self.quantity} шт.)"


class ProductPriceHistory(models.Model):
    """История изменений цен на продукцию"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукция')
    old_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Старая цена')
    new_price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Новая цена')
    changed_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Изменено пользователем')

    class Meta:
        verbose_name = 'История изменения цены'
        verbose_name_plural = 'История изменения цен'
        ordering = ['-changed_at']

    def __str__(self):
        return f"{self.product.name}: {self.old_price} -> {self.new_price}"
