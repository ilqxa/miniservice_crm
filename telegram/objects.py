from typing import Optional

class Update:
    def __init__(
        self,
        update_id:int,
        message:Optional[dict] = None,
        edited_message:Optional[dict] = None,
    ) -> None:
        self.update_id = update_id
        self.message:Optional[Message] = Message(**message)
        self.edited_message:Optional[Message] = Message(**edited_message)

class Message:
    def __new__(cls, *args, **kwargs):
        if any([a is not None for a in args]) or kwargs: return super().__new__(cls)

    def __init__(
        self,
        message_id:int,
        chat:dict,
        text:Optional[str] = None,
    ) -> None:
        self.message_id = message_id
        self.chat:Optional[Chat] = Chat(**chat)
        self.text:Optional[str] = text

class Chat:
    def __new__(cls, *args, **kwargs):
        if any([a is not None for a in args]) or kwargs: return super().__new__(cls)

    def __init__(
        self,
        id:int,
    ) -> None:
        self.id:int = id