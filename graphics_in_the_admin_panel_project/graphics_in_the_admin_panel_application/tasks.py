from django.utils import timezone
from celery import shared_task
from . import parser
import datetime
from django.core.files.images import ImageFile
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
from matplotlib import pyplot
import io

@shared_task
def draw_chart_by_id(function_id):
    from .models import Function

    chart_info = Function.objects.get(id=function_id)
    t = chart_info.t*24*60*60
    dt = chart_info.dt*60*60
    date2 = chart_info.date
    date2_in_seconds = date2.timestamp()
    date1_in_seconds = date2_in_seconds - t
    date1 = datetime.date.fromtimestamp(date1_in_seconds)
    
    series = [[parser.eval_expr(chart_info.function.replace('t', str(date1_in_seconds+i*dt))), date1_in_seconds+i*dt] for i in range(t//dt+1)]

    pyplot.plot([x[1] for x in series], [x[0] for x in series])
    figure = io.BytesIO()
    pyplot.savefig(figure, format='png')
    content_file = ImageFile(figure)

    chart_info.graph.save('{}.png'.format(chart_info.function), content_file)
    chart_info.date = timezone.now()

    chart_info.save()
