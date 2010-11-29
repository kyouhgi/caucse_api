from django.conf.urls.defaults import patterns

urlpatterns = patterns('api1_app.views',
    (r'^articles/list', 'articles_list'),
    (r'^articles/show', 'articles_show'),
    (r'^comments/update', 'comments_update'),
    (r'^users/show', 'users_show'),
    (r'^users/lookup', 'users_lookup'),
    (r'^boards/lookup', 'boards_lookup'),
)
