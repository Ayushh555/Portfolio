from django.core.management.base import BaseCommand
from core.models import Project, Skill


class Command(BaseCommand):
    help = "Seed initial projects and skills"

    def handle(self, *args, **options):
        Project.objects.all().delete()
        Skill.objects.all().delete()

        Project.objects.create(
            name="Spotify Clone",
            description="A Spotify-inspired music app with a Django REST Framework backend — Artist, Album, and Song models — paired with a custom HTML/CSS frontend.",
            github_link="https://github.com/Ayushh555",
            tags="Django, DRF, REST API, HTML/CSS",
            order=1,
            featured=True,
        )
        Project.objects.create(
            name="Job Portal",
            description="An online job portal application built with Django, supporting listings and applications end-to-end.",
            github_link="https://github.com/Ayushh555",
            tags="Django, Python, SQLite",
            order=2,
        )
        Project.objects.create(
            name="E-Commerce Web App",
            description="A full e-commerce application covering product listings, cart, and order flow, built on Django.",
            github_link="https://github.com/Ayushh555",
            tags="Django, Python, Full-Stack",
            order=3,
        )
        Project.objects.create(
            name="Student Management System",
            description="A desktop-based student management system with add, update, delete, and search functionality, built with an interactive Tkinter GUI following OOP principles.",
            github_link="https://github.com/Ayushh555",
            tags="Python, Tkinter, SQLite, OOP",
            order=4,
        )

        skills = [
            ("Python", "PROFICIENT", 85, 1),
            ("Django", "PROFICIENT", 85, 2),
            ("DRF", "PROFICIENT", 80, 3),
            ("JavaScript", "LEARNING", 60, 4),
            ("HTML/CSS", "COMFORTABLE", 75, 5),
            ("Git/GitHub", "COMFORTABLE", 70, 6),
        ]
        for name, level, percent, order in skills:
            Skill.objects.create(name=name, level=level, percent=percent, order=order)

        self.stdout.write(self.style.SUCCESS("Seeded projects and skills."))
