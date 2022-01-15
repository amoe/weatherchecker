from pyramid.view import view_config
import pyramid.response
import weatherchecker.engine
import io

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
    f = io.StringIO()
    
    def buffer_print(*args, **kwargs):
        print(*args, **kwargs, file=f)
    
    weatherchecker.engine.get_weather(buffer_print)
    return pyramid.response.Response(f.getvalue(), content_type='text/plain')
