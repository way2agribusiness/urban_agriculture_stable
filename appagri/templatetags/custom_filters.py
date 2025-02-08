from django import template

register = template.Library()

@register.filter
def get_star_icons(rating):
    num_stars = int(rating)
    return range(num_stars)

@register.filter
def first_letter(name):
    return name[0]

@register.filter  # Add this decorator to register the filter
def discount_percentage(mrp, sales_price):
    try:
        if mrp > 0:
            return round(((mrp - sales_price) / mrp) * 100, 2)
        return 0
    except Exception as e:
        return 0