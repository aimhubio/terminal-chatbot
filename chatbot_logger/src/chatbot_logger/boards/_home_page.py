from asp import Metric
from chatbot_logger import Experiment, SessionProd, SessionDev, Release


def getReleasesCount():
    releases = Release.filter('')
    return len(releases)

def getProdSessionsCount():
    sessions = SessionProd.filter('')
    return len(sessions)

def getDevSessionsCount():
    sessions = SessionDev.filter('')
    return len(sessions)


def getExperimentsCount():
    exps = Experiment.filter('')
    return len(exps)

ui.header('ChatBot Logger HomePage')

overview_row, navigation_row, metrics_row = ui.rows(3)

table = overview_row.table({
    "Releases": [getReleasesCount()],
    "Production Sessions": [getProdSessionsCount()],
    "Dev Sessions": [getDevSessionsCount()],
    "LangChain Experiments": [getExperimentsCount()]
})

col_system, col_prod, col_user, col_releases = \
    navigation_row.columns(4)


with col_system:
    col_system.subheader('System Lineage')
    col_system.board_link('_system_lineage.py', 'Full System Lineage')
with col_prod:
    col_prod.subheader('Production Sessions')
    col_prod.board_link('production.py', 'Production Overview')
with col_user:
    col_user.subheader('User Analytics')
    col_user.board_link('analytics.py', 'User Page')
with col_releases:
    col_releases.subheader("Releases")
    col_releases.board_link('dev/release.py', 'Releases')


metrics_row.header('Token Usage per User Session')

all_metrics = Metric.filter('')
line_chart = metrics_row.line_chart(all_metrics, x='steps', y='values')
line_chart.group('column', ['name'])
line_chart.group('row', ['container.hash'])


