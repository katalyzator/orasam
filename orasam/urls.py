from django.conf.urls import url, patterns, include
from django.conf.urls.static import static
from django.contrib import admin
from solid_i18n.urls import solid_i18n_patterns

from orasam import settings

urlpatterns = solid_i18n_patterns('',
                                  url(r'^jet/', include('jet.urls', 'jet')),
                                  url(r'^$', 'main.views.index_view', name='index'),
                                  url(r'^admin/', admin.site.urls),
                                  url(r'^about/', 'main.views.about_view', name='about'),
                                  url(r'^activities/', 'main.views.acitivity_view', name='activity'),
                                  url(r'^new/(?P<id>\d+)/$', 'main.views.single_news', name='single_news'),
                                  url(r'^event/(?P<id>\d+)/$', 'main.views.single_event', name='single_event'),
                                  url(r'^publication/(?P<id>\d+)/$', 'main.views.single_publication',
                                      name='single_publication'),
                                  url(r'^news', 'main.views.all_news_view', name='news'),
                                  url(r'^books/', 'main.views.book_view', name='book'),
                                  url(r'^contacts/', 'main.views.contacts_view', name='contacts'),
                                  url(r'^countries/', 'main.views.country_view', name='country'),
                                  url(r'^groups/', 'main.views.group_view', name='group'),
                                  url(r'^members/', 'main.views.member_view', name='members'),
                                  url(r'^partners/', 'main.views.partners_view', name='partners'),
                                  url(r'^projects/', 'main.views.projects_view', name='projects'),
                                  url(r'^raporlar/', 'main.views.raporlar_view', name='raporlar'),
                                  url(r'^degerlendirme/', 'main.views.degerlendirme_view', name='degerlendirme'),
                                  url(r'^bultenler/', 'main.views.bulten_view', name='bulten'),
                                  url(r'^mcountries/', 'main.views.makale_country_view', name='mcountry'),
                                  url(r'^mnews/', 'main.views.makale_konu_view', name='konular'),

                                  )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
