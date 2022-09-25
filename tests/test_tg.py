from telegram.objects import *

def test_chat():
    chat = Chat()
    assert chat is None
    chat = Chat(None)
    assert chat is None
    chat = Chat(**{'id': 1})
    assert chat is not None
    assert chat.id == 1

def test_message():
    msg = Message()
    assert msg is None
    msg = Message(None)
    assert msg is None
    msg = Message(
        message_id=1,
        chat={'id': 1},
        text='test'
    )
    assert msg is not None
    assert msg.chat is not None

def test_update():
    upd = Update(
        update_id=1,
        message={
            'message_id': 1,
            'chat': {'id': 1},
        },
        edited_message={
            'message_id': 2,
            'chat': {'id': 1},
        },
    )