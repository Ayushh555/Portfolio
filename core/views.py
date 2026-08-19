from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.throttling import AnonRateThrottle
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill, ContactMessage, SiteInfo
from .serializers import ProjectSerializer, SkillSerializer, ContactMessageSerializer


def home(request):
    """Serves the portfolio frontend (core/templates/index.html)."""
    return render(request, "index.html", {"site_info": SiteInfo.get()})


class ContactRateThrottle(AnonRateThrottle):
    scope = "contact"
    rate = "5/hour"


class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    """GET /api/projects/  and  GET /api/projects/<id>/"""
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """GET /api/skills/"""
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]


class ContactMessageViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """POST /api/contact/  — anyone can submit (rate-limited), nobody can read via API"""
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]
    throttle_classes = [ContactRateThrottle]

    def perform_create(self, serializer):
        message = serializer.save()
        # Notify the owner by email whenever someone submits the contact form.
        # Fails silently so a broken email config never breaks the form for the visitor.
        send_mail(
            subject=f"New portfolio message from {message.name}",
            message=f"From: {message.name} <{message.email}>\n\n{message.message}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_NOTIFY_EMAIL],
            fail_silently=True,
        )
