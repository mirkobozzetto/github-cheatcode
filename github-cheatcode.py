#!/usr/bin/env python3
import os
import random
from datetime import datetime, timedelta
import subprocess
import sys

def create_commit(date):
    env = os.environ.copy()
    date_str = date.strftime('%Y-%m-%d %H:%M:%S')
    env['GIT_AUTHOR_DATE'] = date_str
    env['GIT_COMMITTER_DATE'] = date_str

    with open('counter.txt', 'r') as f:
        counter = int(f.read().strip())
    counter += 1
    with open('counter.txt', 'w') as f:
        f.write(str(counter))

    subprocess.run(['git', 'add', 'counter.txt'], check=True)
    subprocess.run(['git', 'commit', '-m', 'Update'], env=env, check=True)

if not os.path.exists('.git'):
    subprocess.run(['git', 'init'], check=True)

if not os.path.exists('counter.txt'):
    with open('counter.txt', 'w') as f:
        f.write('0')
    subprocess.run(['git', 'add', 'counter.txt'], check=True)
    subprocess.run(['git', 'commit', '-m', 'Init'], check=True)

days = int(sys.argv[1]) if len(sys.argv) > 1 else 1095
start_date = datetime.now() - timedelta(days=days)

for day in range(days):
    current_date = start_date + timedelta(days=day)
    if random.random() < 0.7:  # 70% chance of commit
        num_commits = random.randint(1, 3)
        for _ in range(num_commits):
            hour = random.randint(9, 20)
            minute = random.randint(0, 59)
            commit_date = current_date.replace(hour=hour, minute=minute)
            create_commit(commit_date)

print("Done. Push with: git push -u origin main --force")
