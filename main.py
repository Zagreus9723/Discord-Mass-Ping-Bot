import discum
import json
import time
token = input('ur token: ')
guildz = input('input guild id: ')
chanid = input('input channel id: ')
pingz = []
memberz = []
bot = discum.Client(token=token, log=False)
@bot.gateway.command
def memberTest(resp):
    if resp.event.ready_supplemental:
        bot.gateway.fetchMembers(guildz, chanid)
    if bot.gateway.finishedMemberFetching(guildz):
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()

bot.gateway.run()
print("Starting add members.")
for memberID in bot.gateway.session.guild(guildz).members:
  memberz.append(memberID)
print("Starting to DM.")
msg = ""
for x in memberz:
    try:
      if len(msg) + 22 > 2000:
        pingz.append(msg)
        msg = ""
        msg = msg + f"<@{x}> "
      else:
        msg = msg + f"<@{x}> "
    except Exception as E:
      print(E)
while True:
  for pin in pingz:
    bot.sendMessage(f"{chanid}", f"{pin}")
