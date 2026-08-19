from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import ProjectViewSet, SkillViewSet, ContactMessageViewSet, home

router = DefaultRouter()
router.register("projects", ProjectViewSet, basename="project")
router.register("skills", SkillViewSet, basename="skill")
router.register("contact", ContactMessageViewSet, basename="contact")

urlpatterns = router.urls
