from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from .models import RetailData

@api_view(['GET'])
def filter_options(request):
    brands = RetailData.objects.values_list('Brand', flat=True).distinct()
    pack_types = RetailData.objects.values_list('PackType', flat=True).distinct()
    ppgs = RetailData.objects.values_list('PPG', flat=True).distinct()
    channels = RetailData.objects.values_list('Channel', flat=True).distinct()
    years = RetailData.objects.values_list('Year', flat=True).distinct().order_by('Year')

    return Response({
        'brands': sorted(brands),
        'pack_types': sorted(pack_types),
        'ppgs': sorted(ppgs),
        'channels': sorted(channels),
        'years': sorted(years),
    })


@api_view(['GET'])
def dashboard_data(request):
    qs = RetailData.objects.all()

    # Apply filters
    brand = request.GET.get('brand')
    pack_type = request.GET.get('packType')
    ppg = request.GET.get('ppg')
    channel = request.GET.get('channel')
    year = request.GET.get('year')

    if brand and brand != 'All':
        qs = qs.filter(Brand=brand)
    if pack_type and pack_type != 'All':
        qs = qs.filter(PackType=pack_type)
    if ppg and ppg != 'All':
        qs = qs.filter(PPG=ppg)
    if channel and channel != 'All':
        qs = qs.filter(Channel=channel)
    if year and year != 'All':
        qs = qs.filter(Year=year)

    # Sales Value by Year (for horizontal bar)
    sales_value = (
        qs.values('Year')
        .annotate(value=Sum('SalesValue'))
        .order_by('Year')
    )

    # Volume Contribution by Brand
    volume_contribution = (
        qs.values('Brand')
        .annotate(volume=Sum('Volume'))
        .order_by('-volume')
    )

    # Year-wise Value (vertical bar)
    yearly_value = (
        qs.values('Year')
        .annotate(value=Sum('SalesValue'))
        .order_by('Year')
    )

    # Monthly Trend in Value
    monthly_trend = (
        qs.values('Month')
        .annotate(value=Sum('SalesValue'))
        .order_by('Month')
    )

    # Market Share (Pie Chart): Share by Brand
    brand_totals = (
        qs.values('Brand')
        .annotate(total=Sum('SalesValue'))
        .order_by('-total')
    )
    total_sales = sum(item['total'] for item in brand_totals) or 1
    market_share = [
        {'brand': item['Brand'], 'share': round((item['total'] / total_sales) * 100, 2)}
        for item in brand_totals
    ]

    return Response({
        'salesValue': sales_value,
        'volumeContribution': volume_contribution,
        'yearlyValue': yearly_value,
        'monthlyTrend': monthly_trend,
        'marketShare': market_share
    })
