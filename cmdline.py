import os
import readline
import sys
import tempfile
from code import InteractiveConsole

from api import chat

readline.set_auto_history(True)
_exit_messages = ['exit', 'quit', 'bye']
_commands = ['dump', 'read']

TMP_RENDER_FILE = tempfile.NamedTemporaryFile()


class Conversation:
    def __init__(self):
        self._messages: list[dict[str, str]] = [{
            "role": "system", "content": "You are a helpful assistant."
        }]

    def _append(self, role: str, content: str):
        self._messages.append({
            "role": role, "content": content
        })

    def append_user(self, content: str):
        self._append('user', content)

    def append_assistant(self, content: str):
        self._append('assistant', content)

    @property
    def messages(self):
        return self._messages


def pretty_print(content: str):
    if os.system('glow -v >/dev/null') != 0:
        _pretty_print_tty(content)
    else:
        _pretty_print_render(content)


def _pretty_print_render(content: str):
    with open(TMP_RENDER_FILE.name, 'w') as f:
        f.write(content)
    os.system(f'glow {TMP_RENDER_FILE.name}')


def _pretty_print_tty(content: str):
    size = os.get_terminal_size()
    counter = 0
    max_col = int(size.columns * 0.6)
    for i in range(0, len(content)):
        if counter > max_col:
            counter = 0
            print('\n')
        print(content[i], end='')
        counter = counter + 1
    print()


def _exit():
    print('Bye')
    sys.exit(0)


def dispatch(command: str, conversation: Conversation):
    print('Not implemented yet')


def single_request(content: str):
    conversation = Conversation()
    conversation.append_user(content)
    pretty_print(chat(conversation.messages))


def input_loop():
    console = InteractiveConsole()
    conversation = Conversation()
    while True:
        try:
            line = console.raw_input('>>> ')
            if line in _exit_messages:
                _exit()
            elif line in _commands:
                dispatch(line, conversation)
            else:
                conversation.append_user(line)
                response = chat(conversation.messages)
                pretty_print(response)
                conversation.append_assistant(response)
        except KeyboardInterrupt:
            _exit()
        except EOFError:
            _exit()
