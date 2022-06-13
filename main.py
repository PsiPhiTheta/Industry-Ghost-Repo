# Author: Thomas Hollis
# Date: 06/01/2020
# Purpose: Generate a blank git repo that contains empty commits matching those undertaken while working in industry

# 0. Import libraries
import os
import git
import pandas as pd


def commit(date, message):
    mock_repo = git.Repo("/Users/tom/PycharmProjects/Industry-Ghost-Repo")
    os.environ['GIT_AUTHOR_DATE'] = date
    os.environ['GIT_COMMITTER_DATE'] = date
    try:
        mock_repo.git.commit('-m', message, '--allow-empty')
    except git.exc.GitError as e:
        print('Error in commit: ' + str(e))


dates_df = pd.read_csv("all-commits-bbg.csv")
i = 0
for valsys_commit_date in dates_df["Time"]:
    commit(valsys_commit_date, message="Commit number: {}".format(i))
    i += 1
