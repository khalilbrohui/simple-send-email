from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import SendEmailView

urlpatterns = [
    path("send-email/", SendEmailView.as_view(), name="send-email"),
    # path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # path(
    #     "swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"
    # ),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
