from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('avatar.views',
    url('^add/$', 'add', name='avatar_add'),
    url('^change/$', 'change', name='avatar_change'),
    url('^delete/$', 'delete', name='avatar_delete'),
    url('^render_primary/(?P<user>[\+\w]+)/(?P<size>[\d]+)/$', 'render_primary', name='avatar_render_primary'),    
    url(r'^add_for_user/(?P<for_user>[\w@\.\+\-_]+)/$',
        add_avatar_for_user, name='avatar_add_for_user'),
    url(r'^change_for_user/(?P<for_user>[\w@\.\+\-_]+)/$',
        change_avatar_for_user, name='avatar_change_for_user'),
    url(r'^delete_for_user/(?P<for_user>[\w@\.\+\-_]+)/$',
        delete_avatar_for_user, name='avatar_delete_for_user'),
)
