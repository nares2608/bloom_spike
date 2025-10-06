from wagtail import hooks
from django.core.management import call_command
from wagtail.blocks import StreamValue

@hooks.register("after_publish_page")
def build_tailwind_after_publish(request, page):
    def has_rawhtml_block(stream_value):
        if not isinstance(stream_value, StreamValue):
            return False

        for block in stream_value:
            if block.block_type.lower() in ["rawhtml", "raw_html", "html"]:  # adjust as per your block name
                return True
            if isinstance(block.value, StreamValue):
                if has_rawhtml_block(block.value):
                    return True
        return False

    
    for field in page._meta.get_fields():
        if hasattr(page, field.name):
            value = getattr(page, field.name)
            if isinstance(value, StreamValue) and has_rawhtml_block(value):
                print(f"RawHTML block found in page '{page.title}' — running Tailwind build...")
                try:
                    call_command("build_tailwind_from_content")
                    print("Tailwind build completed successfully.")
                except Exception as e:
                    print(f"Tailwind build failed: {e}")
                break  
