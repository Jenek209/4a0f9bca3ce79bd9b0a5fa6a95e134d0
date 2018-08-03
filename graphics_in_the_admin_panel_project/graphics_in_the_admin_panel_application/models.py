from django.db import models
from django.dispatch import receiver
from .tasks import draw_chart_by_id
from django.utils.safestring import mark_safe

class Function(models.Model):
    function = models.CharField(max_length=200)
    graph = models.ImageField(null=True)
    t = models.IntegerField()
    dt = models.IntegerField()
    date = models.DateTimeField(auto_now=True, null=True)

    def image_tag(self):
        if self.graph:
            html = '<img src="{}" style="width: 400px; height:auto" />'.format(self.graph.url)
            return mark_safe(html)
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


@receiver(models.signals.post_save, sender=Function)
def save_signal_catcher(sender, **kwargs):
    models.signals.post_save.disconnect(save_signal_catcher, sender=Function)
    draw_chart_by_id(kwargs['instance'].id)
    models.signals.post_save.connect(save_signal_catcher, sender=Function)    

