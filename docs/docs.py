import os
from mkdocs import config 
from mkdocs.commands import build,gh_deploy

CWD = os.getcwd()
from mkdocs.commands import gh_deploy


def delete_branch(branch):
    try:
        out = git.cmd.Git(CWD).execute('git branch -D {}'.format(branch))
    except:
        pass


def handle_mkdocs_ghdeploy():
    delete_branch('gh-pages')
    cfg = config.load_config(
        config_file=os.path.join(CWD, "docs/mkdocs.yml"),
        repo_url='git@github.com:sumeetpatil/TravisTest.git'
    )
    build.build(cfg)
    print('Deploying {} Github Pages to {}#gh-pages')
    gh_deploy.gh_deploy(cfg, force=True)


handle_mkdocs_ghdeploy()

