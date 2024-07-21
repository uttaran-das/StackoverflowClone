from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm, RegistrationForm


def index(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'questions/index.html', {'questions': questions})


def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = Answer.objects.filter(question=question).order_by('-created_at')
    return render(request, 'questions/question_detail.html', {'question': question, 'answers': answers})


@login_required
def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = QuestionForm()
    return render(request, 'questions/ask_question.html', {'form': form})


@login_required
def answer_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'questions/answer_question.html', {'form': form, 'question': question})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'registration/profile.html')


@login_required
def logout_view(request):
    logout(request)
    return render(request, 'registration/logged_out.html')
