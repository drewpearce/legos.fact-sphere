from Legobot.Lego import Lego
import os
import pytest
import sys
import threading


path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'legos'))
sys.path.append(path)
from fact_sphere import FactSphere  # noqa: E402

LOCK = threading.Lock()
BASEPLATE = Lego.start(None, LOCK)
LEGO = FactSphere(BASEPLATE, LOCK)
MSG = {
    'text': '!fact you later',
    'metadata': {
        'source': 'urn:uuid:11a222b3-4d55-6666-efg7-h8i9j0a1111b',
        'dest': None,
        'opts': None,
        'text': '!fact you later',
        'source_user': 'HX99U7P36',
        'user_id': 'HX99U7P36',
        'display_name': 'test_user',
        'source_channel': 'YZ366W8K2',
        'is_private_message': True,
        'source_connector': 'slack'
    },
    'should_log': False
}


def test_get_name():
    assert LEGO.get_name() == 'fact_sphere'


def test_get_help():
    assert LEGO.get_help() == '!fact to return a random Fact Sphere fact.'


def test_set_opts(caplog):
    opts = LEGO.set_opts(MSG)
    assert isinstance(opts, dict)
    assert opts.get('target') == MSG['metadata']['source_channel']

    LEGO.set_opts({})
    assert 'Could not identify message source in message' in caplog.text


def test_listening_for(caplog):
    message_no_match = {
        'text': 'no match'
    }
    assert LEGO.listening_for(message_no_match) is None

    message_match = MSG
    assert LEGO.listening_for(message_match) is True

    message_exception = {
        'text': True
    }
    LEGO.listening_for(message_exception)
    assert 'FactSphere lego failed to check the message' in caplog.text


def test_load_fact_data():
    facts = LEGO._load_fact_data()
    assert facts
    assert isinstance(facts, dict)
    assert facts.get('facts')
    assert isinstance(facts['facts'], list)
    assert len(facts['facts']) > 0
    for fact in facts['facts']:
        assert fact.get('fact')
        assert fact.get('audio')


def test_get_random_fact():
    fact = LEGO._get_random_fact()
    assert fact
    assert isinstance(fact, dict)
    assert fact.get('fact')
    assert fact.get('audio')


def test_format_response():
    fact = LEGO._get_random_fact()
    response = LEGO._format_response(fact)
    assert response
    assert isinstance(response, str)
    assert response == '> {}\n-The Fact Sphere\n({})'.format(fact['fact'],
                                                             fact['audio'])


BASEPLATE.stop()
