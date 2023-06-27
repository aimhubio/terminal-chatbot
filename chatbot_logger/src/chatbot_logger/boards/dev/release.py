from datetime import datetime
from chatbot_logger import Release, Experiment

from chatbot_logger import get_release_by_version, get_last_experiment


##################
# Utils
##################

def get_releases(query = '', param = None):
    sessions = Release.filter(query)
    sessions = sorted(sessions, key=lambda sess: (sess['params'].get('version') or '0.0.0').split('.'), reverse=True)
    if param is not None:
        return [session.get(param) or session['params'].get(param) for session in sessions]
    return sessions


##################

def render_experiment(release_version):
    if not release_version:
        return

    exp = get_last_experiment(version=release_version)
    if not exp:
        ui.text('No experiment')
        return

    ui.subheader('Experiment')

    overview, memory, llm, tools, agent = ui.tabs(['Overview', 'Memory', 'LLM', 'Tools', 'Agent'])

    overview.json({
        'release': exp['params'].get('release'),
        'version': exp['params'].get('version'),
        'started': datetime.fromtimestamp(exp['params'].get('started')).strftime("%Y-%m-%d %H:%M:%S") if exp['params'].get('started') else '-',
    })

    memory.json(exp['params'].get('memory'))
    llm.json(exp['params'].get('llm'))
    tools.json(exp['params'].get('tools'))
    agent.json(exp['params'].get('agent'))

def render_release(release_version):
    release = get_release_by_version(version=release_version)
    if not release:
        ui.text('Pick a release')
        return

    ui.subheader('Release')
    ui.json(release)

##################
# Page
##################

# state is a dictionary that's available for each board.
# Think of it as reactJS props that can be passed down to a component.
try:
    release_version = state['dev/release.py']['version']
except:
    release_version = ''

releases = get_releases('', 'version')
default_release = releases.index(release_version) if release_version != '' else 0
release_version = ui.select(options=releases, index=default_release)

render_release(release_version)
render_experiment(release_version)
