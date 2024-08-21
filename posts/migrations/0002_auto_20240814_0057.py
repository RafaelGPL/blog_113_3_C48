# Generated by Django 5.0 on 2024-08-14 00:57

from django.db import migrations

def populate_status(apps, schemaeditor):
    entries = {
        "published": "A post available for all to view",
        "draft": "A post only visible to the author",
        "archived": "An older post, visible to logged in users"
    }
    Status = apps.get_model("posts", "Status")
    for key, value in entries.items():
        status_obj = Status(name=key, description=value)
        status_obj.save()

class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(populate_status)           # note: reference, not call!
    ]
