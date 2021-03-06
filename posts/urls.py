from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^all/$', 'posts.views.posts'),
	url(r'^post/(?P<post_id>\d+)/$', 'posts.views.post'),
	url(r'^myposts/$', 'posts.views.myposts'),
	url(r'^create/$', 'posts.views.create'),
	url(r'^like/(?P<post_id>\d+)/$', 'posts.views.like_post'),
	url(r'^delete/(?P<post_id>\d+)/$', 'posts.views.delete_post'),
	url(r'^comment/(?P<post_id>\d+)/$', 'posts.views.create_comment'),
	url(r'^delcomment/(?P<comment_id>\d+)/$', 'posts.views.delete_comment'),
	url(r'^show/(?P<user_id>\d+)/$', 'posts.views.show_user'),
	url(r'^clike/(?P<comment_id>\d+)/$', 'posts.views.like_comment'),
	url(r'^follow/(?P<user_id>\d+)/$', 'posts.views.follow_user'),
)
