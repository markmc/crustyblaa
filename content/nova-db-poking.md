Title: Nova DB Poking
Date: 2012-07-31 13:37
Author: markmc
Category: openstack
Slug: nova-db-poking
Status: published

So, you want to play with some sqlalchemy queries against the Nova DB in
an interactive python console?

    $> sudo nova-manage shell python
    ...
    >>> from nova.db.sqlalchemy import api
    >>> from nova.db.sqlalchemy import models
    >>> from nova import context
    >>> ctxt = context.get_admin_context()
    >>> vars(api.model_query(ctxt, models.Service).all()[0])
    {'binary': u'nova-compute', ..., 'topic': u'compute', 'host': u'f16', 'disabled': False, 'deleted_at': None, 'id': 1L}
