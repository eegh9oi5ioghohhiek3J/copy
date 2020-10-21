#!/usr/bin/env python3
import os
import random
import subprocess

env = os.environ

subprocess.Popen([
    'docker', 'login',
    '--username', env.get('DOCKER_USERNAME'),
    '--password', env.get('DOCKER_PASSWORD'),
], stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()

prefix = 'data'
image = random.choice(['alpine', 'ubuntu', 'debian', 'redis', 'node'])

subprocess.Popen([
    'docker', 'pull', image,
], stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()

chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345678')

for num in [random.randint(1, 3100) for x in range(15)]:
    print(num)
    tag_prefix_name = random.choice(['dummy', 'workplace', 'strike'])
    image_variable = ''.join(random.choices(chars, k=30))
    dest = "%s/%s-%d:%s-%s" % (
        env.get('DOCKER_USERNAME'), prefix,
        num, tag_prefix_name,
        image_variable
    )
    subprocess.Popen([
        'docker', 'tag', image, dest,
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
    subprocess.Popen([
        'docker', 'push', dest,
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
    subprocess.Popen([
        'docker', 'rmi', dest,
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()