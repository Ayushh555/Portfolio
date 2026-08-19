from rest_framework import serializers
from .models import Project, Skill, ContactMessage


class ProjectSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ["id", "name", "description", "github_link", "live_link", "tags", "featured"]

    def get_tags(self, obj):
        return obj.tag_list()


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name", "level", "percent"]


class ContactMessageSerializer(serializers.ModelSerializer):
    # honeypot field — real users never fill this, bots often do.
    # write_only + not saved to the model; used only to silently reject spam.
    website = serializers.CharField(required=False, allow_blank=True, write_only=True)

    class Meta:
        model = ContactMessage
        fields = ["id", "name", "email", "message", "created_at", "website"]
        read_only_fields = ["id", "created_at"]

    def validate(self, attrs):
        if attrs.pop("website", ""):
            raise serializers.ValidationError("Spam detected.")
        return attrs

    def validate_message(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError("Message is too short.")
        return value
