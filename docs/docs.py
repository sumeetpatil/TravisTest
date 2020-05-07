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


def handle_mkdocs_ghdeploy(kind, remote):
    delete_branch('gh-pages')
    cfg = config.load_config(
        config_file=os.path.join(CWD, "/docs/mkdocs.yml"),
        remote_name=remote
    )
    build.build(cfg)
    print('Deploying {} Github Pages to {}#gh-pages'.format(kind, remote))
    gh_deploy.gh_deploy(cfg, force=True)


handle_mkdocs_ghdeploy('public', 'origin')

