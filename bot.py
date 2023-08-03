"""Main telegram bot file. Answers inline queries about RTD's docs search."""

import telebot
from telebot import types, formatting
from config import DEFAULT_URL, DEFAULT_TEXT
from dotenv import load_dotenv
load_dotenv()
from os import getenv
import search_api as rtd

bot = telebot.TeleBot(getenv("TOKEN"), parse_mode="MarkdownV2")

@bot.inline_handler(lambda query: len(query.query) < 3)
def default_inline_query(query):
    """Answers empty/too short inline queries with a default article."""
    default_result = types.InlineQueryResultArticle(
        "1",
        DEFAULT_TEXT,
        types.InputTextMessageContent(
            formatting.mlink(DEFAULT_TEXT, DEFAULT_URL),
            parse_mode="MarkdownV2"
        )
    )
    bot.answer_inline_query(query.id, [default_result])


@bot.inline_handler(lambda query: len(query.query) >= 3)
def search_inline_query(query):
    """Answers inline queries with search results."""
    response = rtd.parse_query(rtd.query(query.query))
    results = [
        types.InlineQueryResultArticle(
            r['title'],
            r['title'],
            types.InputTextMessageContent(
                f"{DEFAULT_TEXT}: {formatting.mlink(r['title'], r['url'])}",
                parse_mode="MarkdownV2"
            )
        ) for r in response
    ]
    bot.answer_inline_query(query.id, results)

bot.infinity_polling()