from pyramid.view import view_config
import pyramid.response

@view_config(
    route_name='home',
    renderer='weatherchecker:templates/home.j2'
)
def my_view(request):
    return {'project': 'myproject4'}
