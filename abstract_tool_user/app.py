from calmapp import App

from enum import Enum

from abstract_tool_user.utils import query_prompt


class ConversationMode(Enum):
    SIMPLE = 1  # dumb and simple - send the user message as is
    CONTEXTUAL = 2  # send user message with chat history
    SWITCH = 3  # control chat history - switch conversations
    DROP = 4  # drop / shorten messages if history is too long
    LARGE_CONTEXT = 5  # use a model with larger context window


class MyApp(App):
    def __init__(
        self, conversation_mode: ConversationMode = ConversationMode.SIMPLE, **kwargs
    ):
        """Initialize the gpt agent and the toolkit"""
        super().__init__(**kwargs)
        self.conversation_mode = conversation_mode

    def invoke(self, input_str: str) -> str:
        """Invoke the gpt agent with the input string and return the response."""

        # version 0: dumb and simple - send the user message as is
        if self.conversation_mode == ConversationMode.SIMPLE:

            return query_prompt(input_str)

        # version 1: send user message with chat history

        # version 2: control chat history - switch conversations

        # version 3: drop / shorten messages if history is too long
        # or use a model with larger context window

        # version 4:

        # version 5:
