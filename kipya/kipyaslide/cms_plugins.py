from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

@plugin_pool.register_plugin
class KipyaSlide(CMSPluginBase):
    model = CMSPlugin
    render_template = "kipya_slide.html"
    cache = False
    allow_children = True
    name=("Kipya Slide")

    def render(self, context, instance, placeholder):
        context = super(KipyaSlide, self).render(context, instance, placeholder)
        context.update({
            'objects_list': instance.child_plugin_instances,
        })
        return context