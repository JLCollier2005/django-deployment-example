"""
This is used to create custom template filters. See documentation for more info
"""
from django import template


register = template.Library()

# This is the decorators way of registering, see below for the other way
@register.filter(name="cutt")
#create your custom filter
def cutt(value,arg):
    """
    This cuts out all values of 'arg' from the string!
    """
    return value.replace(arg,"")

#register your filter. the first cut is what you will use to call your filter
#and the second cut is the name of the defined function above
#This is the "standard" way, but you can also use decorators (as shown above)
# register.filter("cut",cut)
