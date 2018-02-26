from django import template


register = template.Library()


@register.filter
def addcss(field, args):
    data = {}
    for item in args.split(','):
        attr, value = item.split('=')
        data[attr] = value
    return field.as_widget(attrs=data)


