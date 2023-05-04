# encoding:utf-8

import time

import openai
import openai.error
import requests

from bot.bot import Bot
from bot.chatgpt.chat_gpt_session import ChatGPTSession
from bot.openai.open_ai_image import OpenAIImage
from bot.session_manager import SessionManager
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from common.log import logger
from common.token_bucket import TokenBucket
from config import conf, load_config


# OpenAI对话模型API (可用)
class GPTertioBot(Bot):
    def __init__(self):
        super().__init__()
        

    def reply(self, query, context=None):
        return None


    def reply_text(self, session: ChatGPTSession, api_key=None, retry_count=0) -> dict:
        return None



