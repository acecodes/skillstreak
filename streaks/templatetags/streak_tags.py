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


@register.filter
def add_to_streak(obj):
    return obj.add()


@register.filter
def subtract_from_streak(obj):
    return obj.subtract()


@register.filter
def reset_current_streak(obj):
    return obj.reset_current()
