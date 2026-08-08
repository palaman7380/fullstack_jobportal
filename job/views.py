from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import JobForm
from .models import Application, Job


class JobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = "job_list.html"
    context_object_name = "all_jobs"


class JobDetailView(DetailView):
    model = Job
    template_name = "job_detail.html"
    context_object_name = "job_details"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["has_applied"] = (
            self.request.user.is_authenticated
            and Application.objects.filter(
                job=self.object,
                applicant=self.request.user,
            ).exists()
        )
        return context


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job
    form_class = JobForm
    template_name = "job_form.html"

    def form_valid(self, form):
        form.instance.posted_by = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("job_detail", kwargs={"pk": self.object.pk})


class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = JobForm
    template_name = "job_update.html"

    def get_queryset(self):
        return Job.objects.filter(posted_by=self.request.user)

    def get_success_url(self):
        return reverse_lazy("job_detail", kwargs={"pk": self.object.pk})


class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = Job
    template_name = "job_delete.html"
    success_url = reverse_lazy("job_list")

    def get_queryset(self):
        return Job.objects.filter(posted_by=self.request.user)


class MyJobListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = "my_job_list.html"

    def get_queryset(self):
        return Job.objects.filter(posted_by=self.request.user)


class ApplyJobView(LoginRequiredMixin, CreateView):
    model = Application
    fields = []
    template_name = "apply_job.html"

    def get_success_url(self):
        return reverse_lazy("job_detail", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        job = get_object_or_404(Job, pk=self.kwargs["pk"])
        if Application.objects.filter(job=job, applicant=self.request.user).exists():
            return redirect("job_detail", pk=job.pk)

        form.instance.job = job
        form.instance.applicant = self.request.user
        try:
            return super().form_valid(form)
        except IntegrityError:
            return redirect("job_detail", pk=job.pk)


class MyApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = "my_application_list.html"


class MyJobApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = "my_job_application_list.html"

    def get_queryset(self):
        job = get_object_or_404(Job, pk=self.kwargs["pk"])
        if job.posted_by_id != self.request.user.id:
            raise PermissionDenied
        return Application.objects.filter(job=job)