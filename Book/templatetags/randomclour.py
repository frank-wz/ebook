from django import template
from random import choice
register = template.Library()

@register.filter(name='classcolour')
def classcolour(value):
    return "{}{}".format(value,choice
        (["label label-success",
          "label label-warning",
          "label label-danger",
          "label label-primary",
          "label label-info",
          ])
                         )
