from django.contrib import admin

import sportstore.models as sm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'num_products')

    def num_products(self, obj):
        return sm.Product.objects.filter(category=obj).count()

admin.site.register(sm.Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')

admin.site.register(sm.Product, ProductAdmin)


class OrderItemInline(admin.TabularInline):
    model = sm.OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'street', 'country', 'total')
    inlines = [OrderItemInline]

admin.site.register(sm.Order, OrderAdmin)
