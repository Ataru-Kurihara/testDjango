import os
import pathlib

from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.views import APIView

from ..models import Choice, Question
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import glob
import json


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be published in the future).
        """
        # files = glob.glob("/minecraft/computer/0/test", recursive=True)
        # files_json = json.dumps(files, ensure_ascii=False, indent=2)
        # print(files)
        # # return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
        # return HttpResponse(files_json)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# http://localhost:8881/my_cp_txt/0/


class project(APIView):

    def get(self, request, *args, **kargs):
        files = glob.glob("/minecraft/computer/*[!lastid.txt]", recursive=True)
        files_json = json.dumps(files, ensure_ascii=False, indent=2)
        print(files)
        return HttpResponse(files_json)


class project_id(APIView):

    def get(self, request, *args, **kargs):
        project_id = kargs['id']

        return HttpResponse(project_id)


def cp_txt(request):
    files = glob.glob("/server5/world/computer/*[!lastid.txt]", recursive=True)
    file_json = json.dumps(files, ensure_ascii=False, indent=2)
    return HttpResponse(file_json)
