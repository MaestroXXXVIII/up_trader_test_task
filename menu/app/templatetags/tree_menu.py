import re

from django import template
from django.http import HttpRequest
from django.conf import settings

from app.models import MenuItem
from django.urls import reverse, NoReverseMatch

register = template.Library()


@register.inclusion_tag('app/tags/tree_menu.html', takes_context=True)
def draw_menu(context, slug: str = '', parent: int = 0):

    if parent != 0 and 'menu' in context:
        menu = context['menu']
    else:
        menu = []
        is_url = re.compile(r'^http[s]?://')

        if 'request' in context and isinstance(context['request'],
                                               HttpRequest):
            current_path = context['request'].path
        else:
            current_path = ''

        menu_items = MenuItem.objects.select_related() \
            .filter(category__slug=slug) \
            .order_by('pk')

        for item in menu_items:
            path = item.url
            target = '_self'

            if is_url.match(path):
                url = path
                target = '_blank'
            else:
                try:
                    url = reverse(path)
                except NoReverseMatch:
                    url = path

            if f'/app/{url}/' == current_path:
                active = True
            else:
                active = False

            if item.parent:
                for app in settings.MAIN_APPS:
                    url = (f"{context['request'].scheme}://"
                           f"{context['request'].get_host()}/{app}/{url}/")

            menu.append({
                'id': item.pk,
                'url': url,
                'target': target,
                'title': item.title,
                'parent': item.parent_id or 0,
                'active': active,
            })

    current_menu = (item for item in menu if 'parent' in item and item['parent'] == parent)

    return {
        'menu': menu,
        'current_menu': current_menu,
    }
