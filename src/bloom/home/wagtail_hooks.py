# home/wagtail_hooks.py

from wagtail import hooks
from django.core.management import call_command

@hooks.register("after_publish_page")
def build_tailwind_after_publish(request, page):
    """
    Run Tailwind build command only when a page from 'home' app is published.
    """
    # Check if the published page belongs to 'home' app
    if page._meta.app_label == "home":
        print(f"⚡ Building Tailwind after publishing: {page.title}")
        try:
            call_command("build_tailwind_from_content")
            print("✅ Tailwind build completed successfully.")
        except Exception as e:
            print(f"❌ Tailwind build failed: {e}")
