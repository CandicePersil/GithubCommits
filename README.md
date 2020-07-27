# GithubCommits django project

*-> See STEPS.md for more details*

## Try the app

* Modify personal access token to have access Github api in views.py:

Actual personal access token are an example:
```
g = Github("bc0ae3e44e6ff8568af787037da23bea65d757e8")
```
Go to https://github.com/settings/tokens and generate access token with read access.


* Use next command in main qwarrysiteproject directory:
```
python manage.py runserver
```

Then use following url in your browser:
<http://localhost:8000/githubcommits/>

