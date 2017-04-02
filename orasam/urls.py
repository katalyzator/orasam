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
                       url(r'^news/', 'main.views.all_news_view', name='news'),
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
                       )

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
