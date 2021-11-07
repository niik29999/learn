from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
    name='PythonSampleBot',
    avatar='http://viber.com/avatar.jpg',
    auth_token='4cf12e150627d11e-175dcb0fc7df8426-f7ae4c2d5a64fb3c'
)
viber = Api(bot_configuration)

viber.set_webhook('http://127.0.0.1:443/')





