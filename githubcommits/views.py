from django.shortcuts import get_object_or_404, render
import github
from github import Github, UnknownObjectException


def index(request):
    return render(request, 'githubcommits/index.html')


def github_caller(repository_name):
    g = Github("bc0ae3e44e6ff8568af787037da23bea65d757e8")

    list_commits = None
    try:
        rep_inst = g.get_repo(repository_name)
        list_commits = []
        for com in rep_inst.get_commits()[:10]:
            list_commits.append({"sha": com.commit.sha, "message": com.commit.message,
                                 "date": com.commit.committer.date.strftime("%d/%m/%Y %H:%M:%S")})
    except UnknownObjectException as uoe:
        print('Exception raised: ', uoe)

    return list_commits


def process(request):
    if request.method == 'POST':
        query_dict = request.POST
        repository_name = query_dict['process_repo_name']
        if repository_name:
            commit_list = github_caller(repository_name)
            context = {
                'repo_name': repository_name,
                'commit_list': commit_list,
            }

    return render(request, 'githubcommits/index.html', context)