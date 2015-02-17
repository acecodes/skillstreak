from django import template

register = template.Library()


@register.filter
def gen_multiply(value):
    return '<span style="background:red; width:20px; height:5px;">&nbsp;&nbsp;</span> ' * value
