from aiogram import Dispatcher
from dotenv import load_dotenv

# from abstract_tool_user.lib import MyPlugin
from abstract_tool_user.handler import MyHandler
from abstract_tool_user.app import MyApp

from bot_lib import (
    BotConfig,
    setup_dispatcher,
)
from bot_lib.demo import create_bot, run_bot
from calmapp.plugins import GptPlugin

# plugins = [MyPlugin, GptPlugin]
plugins = []
from abstract_tool_user.app import ConversationMode

app = MyApp(conversation_mode=ConversationMode.WITH_HISTORY, plugins=plugins)
bot_config = BotConfig(app=app)

# set up dispatcher
dp = Dispatcher()

my_handler = MyHandler()
handlers = [my_handler]
setup_dispatcher(dp, bot_config, extra_handlers=handlers)

load_dotenv()
bot = create_bot()

if __name__ == "__main__":
    run_bot(dp, bot)
