from .__init__ import *

MSG = """
<b>Heyπ, I'm a @Internfreakbot Created By [Zaid](https://t.me/lulu786)</b>

<b>β Channel : [InternFreak Posts](https://t.me/internfreakposts)</b>
<b>β Language : [Python](https://www.python.org/)</b>
<b>β Library : [Pyrogram](https://docs.pyrogram.org/)</b>
<b>β Server : [Heroku](https://heroku.com/)</b>
<b>β Database : [Deta](https://deta.sh/)</b>
<b>β Credit : Everyone in this Journey</b>
"""


@bot.on_message(filters.command(['about', 'about@internfreakbot']))
async def about(app, message):
    await app.send_message(message.chat.id, MSG, disable_web_page_preview=True)
