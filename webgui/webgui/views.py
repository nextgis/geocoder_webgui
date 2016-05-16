# encoding: utf-8

from pyramid.view import view_config
from sqlalchemy import create_engine

from address_utils.postgres.models import Name, AddressParser
from address_utils.postgres.models import Base
from address_utils.postgres import DBSession


# FIXME: move connection string to config file
connection_string = 'postgresql://geocoder:@localhost:5432/geocoder'
engine = create_engine(connection_string)

Base.metadata.bind = engine
DBSession.configure(bind=engine)

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'webgui'}

@view_config(route_name='address_parser', renderer='templates/address_parser.pt')
def address_parser(request):
    params = dict((k.upper(), v) for k, v in request.params.iteritems())

    input_address = unicode(params.get('ADDRESS'))
    count = params.get('COUNT')
    try:
        count = int(count)
    except (ValueError, TypeError) as e:
        count = 5

    # import ipdb; ipdb.set_trace()
    session = DBSession()
    parser = AddressParser()
    addresses = parser.parse_address(session, input_address, count)
    addresses = [{'addr': a[0], 'count': a[1]} for a in addresses]

    return {'input_address': input_address, 'address': addresses}
