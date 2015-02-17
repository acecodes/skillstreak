from django import template
import datetime

register = template.Library()


@register.filter
def gen_multiply(value):
    """Generate streak boxes - hack until JS implemented"""
    return '<span class="streak_box">&nbsp;&nbsp;&nbsp;</span> ' * value


@register.filter
def date_delta(value):
    """Get time between now and start of streak"""
    return datetime.date.today() - datetime.timedelta(days=value)
