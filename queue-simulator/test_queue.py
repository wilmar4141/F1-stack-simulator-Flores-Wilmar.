from app import app

app.config['TESTING'] = True

def run():
    c = app.test_client()
    def act(action, value='', peek=False):
        return c.post('/queue', data={'action': action, 'value': value}, follow_redirects=True).get_data(as_text=True)
    def state():
        with c.session_transaction() as s:
            return s.get('items', []), s.get('removed', [])

    for v in ('100', '200', '300'): act('enqueue', v)
    assert state()[0] == ['100', '200', '300']
    html = act('peek'); assert state()[0][0] == '100' and 'highlight' in html and 'Front: 100' in html
    act('dequeue'); assert state() == (['200', '300'], ['100'])
    act('enqueue', '400'); assert state()[0] == ['200', '300', '400']
    act('dequeue'); assert state()[0] == ['300', '400'] and state()[1][0] == '200'
    act('clear'); assert state() == ([], [])
    assert 'empty' in act('dequeue'); assert 'empty' in act('peek')
    assert '1 to 24' in act('enqueue', '   ')

    c = app.test_client()
    for v in ('100', '100', '200'): act('enqueue', v)
    act('dequeue'); assert state()[0] == ['100', '200']
    act('dequeue'); assert state()[0] == ['200']
    act('dequeue'); assert state()[0] == []
    assert c.get('/').status_code == 200 and c.get('/contact').status_code == 200
    print('All tests passed')

run()
