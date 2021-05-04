from github import Github
import pandas as pd
import numpy as np

# First create a Github instance:

# using an access token
g = Github("")

# Then play with your Github objects:
ss_org=g.get_organization("")
df = pd.DataFrame()

c=0
for r in ss_org.get_repos():
    print(r)
    df = df.append(pd.DataFrame(np.array([[r.name, r.last_modified, r.private, r.fork, r.archived, r.description]]),
                           columns=['name', 'last_mod', 'private', 'fork', 'archived', 'description']))
    c += 1

print(df)
df.to_csv("repo-list.csv")