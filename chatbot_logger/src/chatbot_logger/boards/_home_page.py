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

col1, col2, col3 = navigation_row.columns(3)

with col1:
    col1.subheader('Production Sessions')
    col1.board_link('production.py', 'Overview')
with col2:
    col2.subheader('User Analytics')
    col2.board_link('analytics.py', 'User Page')
with col3:
    col3.subheader("Releases")
    col3.board_link('dev/release.py', 'Releases')


metrics_row.header('Token Usage per User Session')

all_metrics = Metric.filter('')
line_chart = metrics_row.line_chart(all_metrics, x='steps', y='values')
line_chart.group('column', ['name'])
line_chart.group('row', ['container.hash'])


