from pyramid.view import view_config
import pyramid.response

# Not using templates at the moment
#
# @view_config(
#     route_name='home',
#     renderer='weatherchecker:templates/home.j2'
# )
# def my_view(request):
#     return {'project': 'myproject4'}

@view_config(route_name='home')
def my_view(request):
    return pyramid.response.Response("Foo bar baz", content_type='text/plain')
