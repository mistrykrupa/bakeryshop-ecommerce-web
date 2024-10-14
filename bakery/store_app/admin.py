from django.contrib import admin
from django.utils.html import format_html
from django.http import HttpResponse
from django.urls import path  # Add this import statement
from django.urls import reverse

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from datetime import datetime

# Register your models here.
from .models import *




def generate_item_report(items, title):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{title}.pdf"'

    # Create PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()
    style_heading = ParagraphStyle(
        name='Heading1',
        fontSize=16,
        leading=30,
        textColor=colors.darkblue,
    )
    elements = []

    # Add title to PDF
    elements.append(Paragraph(title, style_heading))
    elements.append(Paragraph("", styles['BodyText']))

    # Create table for item data
    data = [['Name', 'Price', 'Created Date', 'Status']]
    for item in items:
        data.append([item.name, str(item.price), str(item.created_date), item.status])

    # Customize table style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.darkblue),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])

    # Create table and apply style
    table = Table(data)
    table.setStyle(table_style)
    elements.append(table)

    # Build PDF document
    doc.build(elements)
    return response





def generate_pending_orders_report(orderitems, title):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{title}.pdf"'

    # Create PDF document
    doc = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()
    style_heading = ParagraphStyle(
        name='Heading1',
        fontSize=16,
        leading=30,
        textColor=colors.darkblue,
    )
    elements = []

    # Add title to PDF
    elements.append(Paragraph(title, style_heading))
    elements.append(Paragraph("", styles['BodyText']))

    # Create table for order item data
    data = [['Item Name', 'User', 'Quantity', 'Price', 'Process']]
    for order_item in orderitems:
        data.append([
            order_item.item,
            order_item.user.username,
            order_item.quantity,
            order_item.price,
            order_item.process,
        ])

    # Customize table style
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.darkblue),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])

    # Create table and apply style
    table = Table(data)
    table.setStyle(table_style)
    elements.append(table)

    # Build PDF document
    doc.build(elements)
    return response







class OrderItemTubleinline(admin.TabularInline):
    model=OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines=[OrderItemTubleinline]    
    list_display = ['first_name','phone','email','payment_id','paid','date']
    search_fields = ['first_name','email','payment_id']

@admin.register(OrderItem)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = ['item','user','quantity','price','process']



    actions = ['download_pending_orders_report','download_in_process_orders_report']

    def download_pending_orders_report(self, request, queryset):
        # Filter order items based on 'PENDING' process status
        pending_order_items = queryset.filter(process='PENDING')
        title = 'Pending Orders Report'

        # Generate and return PDF response
        return generate_pending_orders_report(pending_order_items, title)

    download_pending_orders_report.short_description = 'Download Pending Orders Report'

    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False




    def download_in_process_orders_report(self, request, queryset):
        # Filter order items based on 'PENDING' process status
        pending_order_items = queryset.filter(process='IN PROCESS')
        title = 'In Process Orders Report'

        # Generate and return PDF response
        return generate_pending_orders_report(pending_order_items, title)

    download_pending_orders_report.short_description = 'Download In process Orders Report'


@admin.register(Item)
class ItemModelAdmin(admin.ModelAdmin):
    list_display = ['name','price','created_date','status']

    actions = ['download_datewise_items', 'download_price_wise_report','download_month_wise_report']
    

    
    def download_datewise_items(self, request, queryset):
        # Get date-wise items
        all_items = Item.objects.all()
        # datewise_items = [item for item in all_items if item.created_date.date() == datetime.now().date()]
        title = ' Items Report'

        # Generate and return PDF response
        return generate_item_report(all_items, title)

    download_datewise_items.short_description = 'Download Items'

    def download_month_wise_report(self, request, queryset):
        # Get items for the current month
        current_month = datetime.now().month
        month_items = Item.objects.filter(created_date__month=current_month)
        title = f'Month-wise Items Report ({datetime.now().strftime("%B %Y")})'

        # Generate and return PDF response
        return generate_item_report(month_items, title)

    download_month_wise_report.short_description = 'Download Month-wise Report'



    def download_price_wise_report(self, request, queryset):
        # Get all items and order them by price
        all_items = Item.objects.all().order_by('price')
        title = 'Price-wise Items Report'  # Set the report title

        # Generate and return PDF response
        return generate_item_report(all_items, title)

    download_price_wise_report.short_description = 'Download Price-wise Report'

   

    






@admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user','phone','address','city','state','pin']

@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['user','item','review','rating','created_at']    



#admin.site.register(cust)
# admin.site.register(Profile)
admin.site.register(UserProfile)
# admin.site.register(Review)
# admin.site.register(Wishlist)
admin.site.register(Flavour)
admin.site.register(Categories)
admin.site.register(Filter_Price)
# admin.site.register(Item)
admin.site.register(Coupon)
admin.site.register(Contact_us)



admin.site.register(Order,OrderAdmin)
#admin.site.register(OrderItem)