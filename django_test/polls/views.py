# coding=utf-8
# Create your views here.
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template import RequestContext

from polls.models import Poll, Choice
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_protect


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html',
                              {'latest_poll_list': latest_poll_list})


@csrf_protect
def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p},
                              context_instance=RequestContext(request))


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Poll 投票フォームを再表示します。
        return render_to_response('polls/detail.html', {
            'poll': p,
            'error_message': "選択肢を選んでいません。",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # ユーザが Back ボタンを押して同じフォームを提出するのを防ぐ
        # ため、POST データを処理できた場合には、必ず
        # HttpResponseRedirect を返すようにします。
        return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))


def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': p})