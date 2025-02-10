from github import Github
access_token="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"
g = Github(access_token)
user = g.get_user()
print(user.login)
