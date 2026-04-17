from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from .models import Partner, PartnerType, Product, ProductType, PartnerProduct


def partner_list(request):
    """Список всех партнеров с расчетом скидки"""
    partners = Partner.objects.all().select_related('partner_type')

    # Расчет скидки для каждого партнера
    partner_data = []
    for partner in partners:
        total_sales = partner.get_total_sales()

        # Определение скидки по объему продаж
        if total_sales < 10000:
            discount = 0
        elif total_sales < 50000:
            discount = 5
        elif total_sales < 300000:
            discount = 10
        else:
            discount = 15

        partner_data.append({
            'partner': partner,
            'total_sales': total_sales,
            'discount': discount
        })

    return render(request, 'main/partner_list.html', {'partner_data': partner_data})


def partner_detail(request, pk):
    """Детальная информация о партнере с историей продаж"""
    partner = get_object_or_404(Partner, pk=pk)
    sales = PartnerProduct.objects.filter(partner=partner).select_related('product').order_by('-sale_date')
    total_sales = partner.get_total_sales()

    # Расчет скидки
    if total_sales < 10000:
        discount = 0
    elif total_sales < 50000:
        discount = 5
    elif total_sales < 300000:
        discount = 10
    else:
        discount = 15

    return render(request, 'main/partner_detail.html', {
        'partner': partner,
        'sales': sales,
        'total_sales': total_sales,
        'discount': discount
    })


@login_required
def partner_add(request):
    """Добавление нового партнера"""
    if request.method == 'POST':
        # Обработка формы добавления
        partner_type_id = request.POST.get('partner_type')
        name = request.POST.get('name')
        director = request.POST.get('director')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        inn = request.POST.get('inn')
        rating = request.POST.get('rating', 0)

        partner = Partner.objects.create(
            partner_type_id=partner_type_id,
            name=name,
            director=director,
            email=email,
            phone=phone,
            address=address,
            inn=inn,
            rating=rating
        )
        return redirect('partner_detail', pk=partner.pk)

    partner_types = PartnerType.objects.all()
    return render(request, 'main/partner_form.html', {'partner_types': partner_types, 'action': 'add'})


@login_required
def partner_edit(request, pk):
    """Редактирование партнера"""
    partner = get_object_or_404(Partner, pk=pk)

    if request.method == 'POST':
        partner.partner_type_id = request.POST.get('partner_type')
        partner.name = request.POST.get('name')
        partner.director = request.POST.get('director')
        partner.email = request.POST.get('email')
        partner.phone = request.POST.get('phone')
        partner.address = request.POST.get('address')
        partner.inn = request.POST.get('inn')
        partner.rating = request.POST.get('rating', 0)
        partner.save()
        return redirect('partner_detail', pk=partner.pk)

    partner_types = PartnerType.objects.all()
    return render(request, 'main/partner_form.html', {
        'partner': partner,
        'partner_types': partner_types,
        'action': 'edit'
    })


def product_list(request):
    """Список продукции"""
    products = Product.objects.all().select_related('product_type')
    return render(request, 'main/product_list.html', {'products': products})


def product_detail(request, pk):
    """Детальная информация о продукции"""
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'main/product_detail.html', {'product': product})


def sales_history(request):
    """История продаж всех партнеров"""
    sales = PartnerProduct.objects.all().select_related('partner', 'product').order_by('-sale_date')
    return render(request, 'main/sales_history.html', {'sales': sales})
