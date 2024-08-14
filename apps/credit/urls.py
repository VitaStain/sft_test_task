from django.urls import include, path

from apps.credit.views.credit import CreditListView

urlpatterns = [
    path(
        "v1/",
        include(
            [
                path("credits/", CreditListView.as_view()),
            ]
        ),
    ),
]
