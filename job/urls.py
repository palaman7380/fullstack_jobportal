from django.urls import path
from .views import (
    JobListView,
    JobDetailView,
    JobCreateView,
    JobUpdateView,
    JobDeleteView,
    MyJobListView,
    ApplyJobView,
    MyApplicationListView,
    MyJobApplicationListView,
)

urlpatterns = [
    path("", JobListView.as_view(), name="job_list"),
    path("<int:pk>/", JobDetailView.as_view(), name="job_detail"),
    path("create/", JobCreateView.as_view(), name="job_create"),

    path("update/<int:pk>/", JobUpdateView.as_view(), name="job_update"),
    path("delete/<int:pk>/", JobDeleteView.as_view(), name="job_delete"),

    path("my-jobs/", MyJobListView.as_view(), name="my_jobs"),
    path("apply/<int:pk>/", ApplyJobView.as_view(), name="apply_job"),

    path(
        "my-applications/",
        MyApplicationListView.as_view(),
        name="my_applications",
    ),

    path(
        "applications/<int:pk>/",
        MyJobApplicationListView.as_view(),
        name="job_applications",
    ),
]