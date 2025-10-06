from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import RichTextField
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.blocks import RawHTMLBlock

class RawHTMLBlock(RawHTMLBlock):
    def __init__(self, *args, **kwargs):
        kwargs["required"] = False  # allow empty HTML
        super().__init__(*args, **kwargs)

    class Meta:
        icon = "code"
        label = "Raw HTML"
        help_text = "Raw HTML content (can be empty) with Tailwind CSS classes"