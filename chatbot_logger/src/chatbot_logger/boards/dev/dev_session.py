import json

from chatbot_logger import SessionDev, MessagesSequence
from asp import Metric, SystemMetric

# FIXIT:
# There is LOTS of repeat non-ui code in these files.
# To be moved to "server functions" once its available (to be shipped as part of stable)

# FIXIT:
# There is lots of repeat UI code that should be moved into template.
# This is exactly the same page as the prod_session.
# In real world these would be different pages built on the same base.
# We need to enable __init__.py in the UI folders so devs can precisely define what files get rendered and what become reusable templates.


##################
# Utils
##################

def get_session(session_hash):
    sessions = SessionDev.filter(f'c.hash == "{session_hash}"')
    if sessions and len(sessions):
        return sessions[0]
    return None

def get_sessions(query = '', param = None):
    sessions = SessionDev.filter(query)
    sessions = sorted(sessions, key=lambda sess: sess['params'].get('started') or 0, reverse=True)
    if param is not None:
        return [session.get(param) for session in sessions]
    return sessions

##################

def overview(session_hash):
    if not session_hash:
        ui.text('Select a session')
        return

    session = get_session(session_hash)
    if session is None:
        ui.text('Session not found')
        return

    ui.header(f'Dev Session "{session_hash}"')
    ui.subheader('Overview')

    ui.table({
        'Params': [
            'Model',
            'Used tools',
        ],
        'Values': [
            session['params'].get('model'),
            json.dumps(session['params'].get('used_tools')),
        ],
    })

def history(session_hash):
    if not session_hash:
        return

    ui.subheader('History')

    qa_sequences = MessagesSequence.filter(f's.name == "messages" and c.hash == "{session_hash}"')
    
    if qa_sequences and len(qa_sequences):
        history_table = ui.table({
            'question': [r['question'] for r in qa_sequences],
            'answer': [r['answer'] for r in qa_sequences],
            'index': [step for (step, _) in enumerate(qa_sequences)],
        })

        if history_table.focused_row:
            ui.subheader('Agent actions')
            step = history_table.focused_row['index']
            ui.json(qa_sequences[step])
    
    else:
        ui.text('No message history')
        

def session_cost(session_hash):
    if not session_hash:
        return

    ui.subheader('Tokens usage')

    # Calculate cost
    metrics = Metric.filter(f'c.hash == "{session_hash}"')

    input_tokens = 0
    output_tokens = 0
    for metric in metrics:
        if metric['name'] == 'token-usage-input':
            input_tokens = sum(metric['values'])
        if metric['name'] == 'token-usage-output':
            output_tokens = sum(metric['values'])

    input_price = input_tokens * 0.002 / 1000
    output_price = output_tokens * 0.002 / 1000
    total_price = input_price + output_price

    ui.text(f'Total price: ${total_price}, input tokens: ${input_price}, output tokens: ${output_price}')
    ui.text(f'Total count: {input_tokens+output_tokens}, input count: {input_tokens}, output count: {output_tokens}')

    line_chart = ui.line_chart(metrics, x='steps', y='values')
    line_chart.group('column', ['name'])


def system_metrics(session_hash):
    ui.header('System Metrics')
    system_metrics = SystemMetric.filter(f'c.hash == "{session_hash}"')
    line_chart = ui.line_chart(system_metrics, x='steps', y='values')
    line_chart.group('column', ['name'])

def user_info(session_hash):
    if not session_hash:
        return

    session = get_session(session_hash)
    if session is None:
        return

    ui.subheader('User')

    username = session['params'].get('username')
    if not username:
        ui.text('No associated user')
        return

    ui.text(f'User: {username}')
    ui.board_link('analytics.py', 'User page', state={
        'username': username,
    })

##################
# Page
##################

try:
    session_hash = state['sessions.py']['session_hash']
except:
    session_hash = ''

sessions = get_sessions('', 'hash')
if sessions:
    default_session = sessions.index(session_hash) if session_hash != '' else 0
    session_hash = ui.select(options=sessions, index=default_session)

if session_hash:
    overview(session_hash)
    history(session_hash)
    session_cost(session_hash)
    system_metrics(session_hash)
    user_info(session_hash)
else:
    ui.header('No dev sessions')
