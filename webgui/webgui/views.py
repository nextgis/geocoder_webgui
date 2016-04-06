from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'webgui'}

@view_config(route_name='address_parser', renderer='templates/address_parser.pt')
def my_view(request):
    params = dict((k.upper(), v) for k, v in request.params.iteritems())
    input_address = params.get('ADDRESS')
    x = 'Address: ' + input_address
    return {'input_address': input_address, 'address': x}
