from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import RichTextField
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.blocks import RawHTMLBlock

class RawHTMLBlock(RawHTMLBlock):
    class Meta:
        icon = "code"
        label = "Raw HTML"
        help_text = "Raw HTML content with Tailwind CSS classes"