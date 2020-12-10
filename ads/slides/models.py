from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField
from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

class KipyaCard(CMSPlugin):
	card_image = models.ImageField(upload_to="uploads/general_images/",verbose_name=_('Card Image'),blank=False)
	card_content = HTMLField(verbose_name=_('Card Content'),blank=True,default='',help_text=_('Content may also be added using child plugins.'))


class Slide(CMSPlugin):
	# slide_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	is_active = models.BooleanField(default=False)
	content_image = models.ImageField(upload_to="uploads/slide_images/",verbose_name=_('Slide image'),blank=False)
	carousel_content = HTMLField(verbose_name=_('Content'),blank=True,default='',help_text=_('Content may also be added using child plugins.'))

class CustomContent(CMSPlugin):
	"""docstring for CustomContent"""
	
	custome_content_html=models.TextField()
		