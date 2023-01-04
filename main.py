import discord
from discord.ext import commands
import os
from replit import db
import random
from keep_alive import keep_alive
import asyncio
import praw

my_secret = os.environ['TOKEN']
reddit_client = os.environ['REDDIT_CLIENT']
reddit_secret = os.environ['REDDIT_SECRET']
client = commands.Bot(command_prefix = '$')
client.remove_command('help')

# set up quote databases
if 'irl' not in db.keys(): 
  db['irl'] = [
  "Jonathan: It’s not every day you get to beat up your hot boss. \n5/30/20",
  "Vivian: GOBLIN THESE NUTS \n5/30/20",
  "Eric: D&D is a game where Jonathan can play out any fantasy, such as wearing badass armor and not being down bad. \n8/14/20",
  "Eric: The hulk's only donkey companion is America's ass. \n12/3/21",
  "Eric:  Why do what I do, when my deviance leads to the smiles of others. \nVivian: Eric sounds like a quote from the world’s noblest clown. \n12/15/21",
  "Don: When I get home, I’m gonna hit it. \nEric: Hit what? \nJason: Children? \n12/15/21",
  "Don: If I was a flavor, I’d be a damn good one. \n12/16/21",
  "Eric: Big Juice can be a rapper name \n12/15/21 9:33pm",
  "Eric: you don’t DESERVE Bart! \n12/15/21 10:37pm",
  "Jon: You like drinking hand sanitizer? \nEric: It's called detox baby look it up. \n12/18/21 1:00pm",
  "Don: I ignored the warnings of my predecessors and it led to my downfall. \n12/19/21 8:45pm",
  "Jon: Eric you played him like a pickle. \n12/25/21 11:40pm",
  "CJ: Yeah you have an excuse to not make it to sessions– I’m ready (proceeds to order thru drive-thru) Can I get a… \n1/6/22 8:02pm",
  "Don: You can be enemies-to-lovers, but you can’t be brothers-to-lovers. \n1/6/22 8:11pm",
  "Jason: I broke the wrong block in Minecraft and the game crashed \n1/6/22 8:13pm",
  "Vivian: I’d roast that snake. \n1/6/22",
  "Eggric: Eggs fly everywhere. \n1/6/22",
  "Eggric: Don, you get a lot of nightmares, don’t you? \n1/7/22 5:40pm",
  "Eggric: Valentine's Day?!, It's January… oh. \n1/9/22 7:57pm",
  "CJ: I just guzzled some balls. \n1/9/22 9:11pm",
  "CJ: I sucked so hard that the balls went up and I guzzled them down the back of my throat. \n1/9/22 9:12pm",
  "Eggric: If you put a bunch of toilet paper rolls back to back, it’ll look like a sushi roll. \n1/9/22 9:17pm",
  "Eggric: So you have a tail? \n1/9/22 10:XXpm",
  "CJ: It’s like a beyblade. \n1/9/22 10:XXpm",
  "Eggric: I can’t believe women just walk around with tails. \n1/9/22 10:XXpm",
  "Eggric: So what if you used hot glue? \n1/9/22 10:XXpm",
  "Jason: Why wouldn’t you hate children? Children deserve it. \n1/10/22 10:39pm",
  "Eggric: She’s my punching bag. \n1/10/22 10:42pm",
  "Don: We’re talking about Vivian’s whore-ish-ness. \n1/11/22 2:09pm",
  "Eggric: This is a 3am talk at 9pm. \n1/11/22 9:10pm",
  "Eggric: I love Jonathan’s skin. \n1/12/22 12:32am",
  "Jason: Arvind I’ll touch you later tonight but not now. \n1/12/22 12:48am",
  "CJ: MMM The mussy, you know? \n1/13/22 8:16pm",
  "Don: It’s one thing if the dragon decides to fuck you, but another thing if you decide to fuck the dragon. \n1/15/22 8:01pm",
  "Vivian: It’s too much work being mortal enemies so we’re friends. \n1/16/22 11:30pm",
  "Jason: You know what’s a very telling character trait of mine? I stop playing Sims every time children appear. \n1/16/22 11:56pm",
  "Eric: I don’t watch the Simpsons for nothing. \n1/17/22 1:02am",
  "Jason: Sorry Eric I couldn’t hear you over CJ talking about Smegma. \n1/19/22 6:59pm",
  "Vivian: Eric, it’s kind of cute of you to be a loan shark or whatever~ \n1/19/22 8:25pm",
  "Eric: CJ It’s kinda sexy of you to lose over and over. \n1/19/22 8:29pm",
  "CJ: It was a moment of weakness \nVivian: You tried to rob three people in a row! \nCJ: It was a moment of w e a k n e s s \n1/19/22 8:41pm",
  "CJ: Untouched, practically factory smell new. \n1/19/22 8:43pm",
  "Jason: Do you believe in the heart of the cards? \nCJ: Yes. \n1/19/22",
  "Prad: This is what capitalism looks like.. The rich get richer and the poor get poorer. \n1/19/22 9:22pm",
  "Eric: And you get diarrhea all night? \n1/22/22 5:23pm",
  "Jason: Eric stream the FUCKING vine. \n1/23/22 1:18pm",
  "CJ: HA A dragon is just a wanna be snake. \n1/24/22 5:40pm",
  "Prad: I can’t do homework if no else has done it yet. \n1/24/22  5:44pm",
  "CJ: I REFUSE TO BE QUOTED. \n1/24/22 5:46pm ",
  "CJ: If you can hate on my poop brown, I CAN HATE ON YOUR PISS YELLOW. \n1/24/22 5:47pm",
  "CJ: I CANT LAST ONE MINUTE. \nVivian: THAT’S WHAT SHE SAID. \n1/24/22 5:47pm",
  "Vivian: NNNNNNNNNNNN. \n1/24/22 5:52pm",
  "Jason: Don’t make me go there and remove your mic. \nCJ: Oh no, not my removable mic. \n1/24/22 5:56pm",
  "Eric: I have a bunch of homebrew drugs I can share with CJ. \n1/24/22 7:58pm",
  "Jason: I’m gonna stab myself with a knife! \nEric: Wait! I was gonna stab you with a knife! \n1/24/22 8:53",
  "Eric: I want my kisses with the homies to be intimate okay. \n1/24/22 10:26pm",
  "Eric: I start the day 100% done but the day is only 30% done with me. \n1/25/22 10:52pm",
  "Jason: The only person I’m willing to kill for someone is me. \nEric: Well I’m glad you have standards. \n1/25/22 11:52pm",
  "Vivian: Extreme water boarding? \nPrad: I think that’s called drowning? \n1/27/22 4:46pm",
  "CJ: Cause you can’t decide. Women moment. \n1/27/22 6:59pm",
  "CJ: I can’t wait to get a girlfriend so I can be misogynistic. \n1/27/22 7:00pm",
  "Eric: That’s a good suck. I saw it. \n1/27/22 7:40pm",
  "Eric: I guess I’m racist. \n1/29/22 11:43pm",
  "Vivian: You know what, I AM racist. \n2/3/22 11:59pm",
  "Eric: Witnessing Vietnamese on Vietnamese violence again. \n2/4/22 12:14am",
  "CJ: We love youuu *mwah* \nEric: Ok. \n2/4/22 12:15am",
  "Jason: Oh my god Vivian, we’re gonna become Dice Pirates. \n2/6/22 6:36pm ",
  "Vivian: I’m still feeling CJ out right now. \n2/6/22 6:43pm",
  "Jason: I’m willing to kill myself for everyone. \n2/6/22 7:10pm",
  "Eric: I was too slow... Don died. \n2/6/22 8:50pm",
  "Eric: CJ… Are you ready for our nightly piss discussion… piscussion if you will. \n2/6/22 10:51pm",
  "CJ: Are you piss and poop cuz I got piss and poop on the brain. \n2/10/22 10:00pm",
  "Vivian: I would have a small cup of fish sauce… and I’d take sips. \n2/13/22 8:17pm",
  "Eggric: Well you see, honey is sweet, but frosting is thicccc. \n2/13.22 8:20pm",
  "Eggric: Are you putting frosting in your ear?? \n2/13/22 8:46pm",
  "Don: If you poor for a millenia then you deserve it. \n2/13/22 9:29pm",
  "Eggric: I gotta watch where I put my tentacles. \n2/19/22",
  "Vivian: I gotta be real with you. I don't know where San Diego is. \n2/26/22",
  "Don: Vivian so stupid? More believable than you think. \n2/26/22 11:57pm",
  "Vivian: Its just like beef… but less cow. \n3/5/22 12:46",
  "Don: Are you guys canadian or something? \nJason: AIYAAAAAA \nDon: Thats not very canadian. \n3/7/22 1:15 am",
  "Prad: How inefficient is snorting  \n3/7/22 1:46 am",
  "CJ: HOW DO I PUT THIS IN JASON  \n3/12/22 7:46pm",
  "Jason: CJ is thrusting hard in the other room. \n3/12/22 7:49pm",
  "Jason: Arvind is showing CJ how much better he is at thrusting. \n3/12/22 7:55pm",
  "CJ: I’m too busy blowing this burrito… sexually. \n3/12/22 7:56pm",
  "Don: It can’t throw me into depression if I’m already in depression ;)  \n3/12/22 8:07pm",
  "Vivian: I love voyeurism.  \n3/12/22 8:16pm",
  "Vivian: Oh my god, CJ's naked.  \n3/17/22 12:57am",
  "CJ: (in reference to being the middle child) This is why I hate women. \n3/17/22 2:59pm",
  "CJ: What the fuck are you doing to my floor? \n3/17/22 3:13pm",
  "CJ: Jesus is God's smurf. \n3/19/22 9:44pm",
  "Eggric: Our lives would be so much better off right now if eggs didn’t exist. \nJason: Yeah? Eggric??? \n3/19/22 9:54pm",
  "CJ: Yeah I read it in a documentary. \n3/19/22 10:05pm",
  "CJ’s uncle: Boys have a penis and girls have a vagina, if you didn’t know. \nEggric (incredulously): So who has the pee? \n3/19/22 10:28pm",
  "Eric: It’s every man for himself and you are a WOMAN  \n3/20/22 7:15pm",
  "Eric: An empath? More like an emFAT. \n3/20/22 8:03pm",
  "CJ: Jonathan was gonna sacrifice his girlfriend! \nJonathan: …anything for the win. \n3/20/22 10:22pm",
  "Eric: Men love balls. \n3/22/22 6:49pm",
  "CJ: bitches ain’t shit… and that can be quoted. \n4/6/22",
  "CJ: CM…. for Cum Master. 4/13/22 \n7:45pm",
  "CJ: I just got absolutely shit on by the Chinese. \n4/15/22 3:35pm",
  "Eric: I love clowns. \n5/15/22 12:22am",
  "Vivian, sitting in a sushi restaurant: wait I thought potato croquettes are a Japanese thing. \n5/16/22 7:20pm",
  "CJ: Did you see the DM I sent you about your feet? \n5/25/22 11:08pm",
  "Eggric: 12% is basically non-alcoholic. \n6/27/22 3:52pm",
  "Vivian: (in reference to the devil’s lettuce) The god's leaves \n6/27/22 5:57pm",
  "Eric: Vivian, you better be quiet or I'm gonna SELL you. \n6/27/22 6:50pm",
  "Krystal: Are you just yeeting women? Why do they have to be aerodynamic? \n6/30/22",
  "Jonathan: I will collect all of the women. \nJason: Jonathan do you need to drink more respect women juice?",
  "Eric: I'm uninstalling minecraft. I just accidentally killed me dog.",
  "Eric: I have daddy issues but I'm the daddy.",
  "CJ: Would you prefer Father Bean over Bean Daddy?",
  "Prad: These are slutty beans.",
  "Eric: Please don't slut shame the beans.",
  "Eric: I take off my eyepatch to reveal...a perfectly normal eye.",
  "CJ: The pyramid is lubed and ready to go.",
  "CJ: (incoherent yelling because Mah Arba isn't running out of the way) It's not my fault if Mah Arba dies. \nEveryone else: Don't worry, no one will blame you.",
  "Jason: You can't boke my butt, I don't give you consent. \nCJ: They're not asking for your permission :)",
  "Everyone: This is why Jonathan doesn't have any rights",
  "Eric: Yeah and Jon rolled the smallest one.",
  "Don: I don't want to write smut...I've never written smut before.",
  "Eric: (in reference to Kerkylos' other use) Hey, this wasn't in the module.",
  "Eric: I just wanna kiss my homies is that too much to ask?",
  "Everyone: Hey we're *all* premed.",
  "Vivian: (looking right at the chairs in the shower) There's nothing in the shower???",
  "Jason: (incredulously) You think I'm a wizard?",
  "CJ: I'm just a hopeless romantic until you know, it comes to me. \nEric: Yeah because then it's just hopeless.",
  "Don: ...this is a club. \nEric: No this is a *tavern* where are the clubs?",
  "Don: What is a rave? \nEric: It's like when people rub their bodies against each other. \nDon: Like wrestling? \nEric: Yeah but with music and lights.",
  "Vivian: Wym I just peed my pants.",
  "Eric: I care about their SPOONS and their MAGIC, but no one cares when I want to slam dunk someone's head into the floor:(",
  "Vivian: Two unstoppable himbos and not a brain cell between them.",
  "Eric: I'm used to being on the bottom, but this time I'll mount.",
  "CJ: I have personal experience with a friend dating a family member.", 
  "Eric: Even Jesus can't make a girlfriend for you.",
  "Prad: Of course I remember my girlfriend...do you remember yours?",
  "Vivian: Money is a social construct anyways.",
  "Jason: Cannibalism is the answer to world hunger, overpopulation and global warming.",
  "Vivian: BRO I'm NOT going to ask a question. How stupid do you think I am?",
  "CJ: Not anything can be a quote",
  "Prad: We love trees...we love trees and grass. \nAlso Prad: Why did no one ever try to attack a tree? That's on you.",
  "CJ: Jonathan you're lucky Don's not letting me kill your character.",
  "Jon: I'm so tired...I beat a woman today.",
  "Jon: (with joy) Killing myself!!!",
  "Jason: This is a Jason to Jonathan question: WHY",
  "CJ: I did not play DND to go to school.",
  "Don: The Storm's Wake quietly, and finally, came to an end."
]
if 'worm' not in db.keys():
  db['worm'] = [
  "Ostin: I agree with the ballsack with ears. \n1/22/22 09:10pm, Session 1",
  "Thallan: Why/How are you pointing at like three people at the same time. \n1/22/22 9:25pm Session 1",
  "Thallan: I will not dropkick a dog but I will dropkick a child. \n1/22/22 10:39pm",
  "Rhomi: Is it not normal to kill people? \nRone: Honestly, at their age, I’m surprised they haven’t. \n1/22/22 10:47pm Session 1",
  "Rone: (in reference to attempted murder) You tried your best, and that’s all that matters. \n1/22/22 10:53pm Session 1",
  "Rone: I’m not sure if purposeful sleep-deprivation is a war crime or not, but I’m going to sleep. \n1/22/22 11:05pm Session 1",
  "Rhomi: Well it’s good torture. \n1/23/22 12:13am Session 1",
  "Jason: Well Thallan’s a fucking librarian. \n1/23/22 12:17am",
  "Vivian: How dare you Eric you whore… Eric’s whorishness is popping out right now. \n1/23/22 12:25am",
  "Don: A shower of balls. *slowly nods to himself* \n1/23/22 12:55am",
  "Vivian: This is so disappointing I can’t believe you’re more colorblind than the colorblind guy. \n1/23/22 1:06am",
  "Ostin: THey got BAbies. \n2/12/22 9:29pm",
  "Ostin: I take half your damage. \nEveryone else: THEY’RE MARRIED. THEY’RE MARRIED. \n2/12/22 9:33pm",
  "Dewdrop: Cleric powered resuscitation. \n2/12/22 10:04pm",
  "Ostin: Got you old man. \nThallan: Thank you, young man. \n2/12/22 10:32pm",
  "Thallan/Jason: Who let him live for a 100 years? \n10:47pm",
  "CJ: A weary traveler collapses… 'ah I am tired and weary from my travels.' \nRhomi: Ah of course you weary traveler. \n2/12/22 11:14pm",
  "Ostin: Ostin giveth and Ostin taketh away. \n2/26/22 8:40pm",
  "Rhomi: Alright Dewdrop, hit me! \n2/26/22 9:28pm",
  "Don: I KNOW WHAT I WANNA SAY BUT I DON’T WANNA SAY IT. \n2/26/22 9:35pm",
  "Orc Guard: What are you doing here? \nRhomi: ..Adventure? \nRone: Adventure. \nThallan: …….adventure? \nOstin: Kick ass, you want in? \n2/26/22 9:45pm",
  "Eric: They have the impossible salad here. \n2/26/22 10:10pm",
  "Thallan: I can’t believe Ostin is pounding guys in front of Rone. \n2/26/22 10:18pm",
  "Ostin: I am the superior pounder in this party. \n2/26/22 10:18pm",
  "Chief Pounder: We orcs don’t die cuz we’re fucking lit bro. \n2/26/22 10:33pm",
  "Rone: He’s quite the pounder. \n2/26/22 10:52pm",
  "Rone: All women do is manipulate. \nThallan: And now you’re with a man. \n2/26/22 10:59pm",
  "Ostin: I don’t really do rocks guys. \nThallan: Is it because it's not green? \n2/26/22 11:09pm",
  "Ostin: I do it all the time. \nRhomi: and Rone is okay with that? \n3/25/22 09:23pm",
  "Dewdrop: It’s only murder if it hurts their feelings. \n3/25/22 10:18pm",
  "Rone: Did you bring the pot? \nDewdrop: Uh… I was supposed to bring a pot? \nRone: How else do you fly so high? \n4/24/22 8:54pm",
  "Morgan: You want her to deepthroat us? \n6/27/22 8:57pm",
  "Nomira: It’s not human trafficking if it’s with consent. \n6/27/22 9:41pm"
]
if 'seekers' not in db.keys():
  db['seekers'] = [
  "Ophellya: We’re getting paid. \nV’dun: Say no more fam.\nSession 1: 5/30/21",
  "Ejis: I propose to the sword.",
  "Ophellya: Can we roll for tentacle size? 1/28/2022",
  "Ophellya: They're very straight. Session 31: 4/1/2022",
  "Ophellya: We visited Monmurg! \nBeth: What did you see? \nOphellya: ...jail?",
  "V'dun: Bet bitch!",
  "Ejis: Aren't you glad you guys got a drug dealer?",
  "Ophellya: Did you just suffocate that bird? \nSession 32: 4/16/2022",
  "V'dun: Children can easily be bought out. \nSession 34: 5/13/2022",
  "Ingeqk: Athlete's foot coming in clutch. \nSession 35: 6/3/2022",
  "Ophellya: Non-consensual touching. Dont touch people without their consent. Bitch stop touching me. \nSession 35: 6/3/2022",
  "Eric: Non-consensual touching but at a distance. \nSession 35: 6/3/2022",
  "Ophellya: NO MEANS NO. \nSession 35: 6/3/2022",
  "Jimson: I love watching construction.",
  "Ophellya: Biting without consent. \nSession 36 6/23/2022",
  "Ophellya: Another bitch in my head. \nSession 36 6/23/2022",
  "Jimson: Give me my milk! \nSession 36 6/23/2022",
  "Travis: Eric just likes a sausage party"
]
if 'test' not in db.keys():
  db['test'] = [
  "Alice: Hi Bob! \nBob: Hi Alice!"
]

# set database values(list of quotes) to variables
quotes = db['irl']
quotes_worm = db['worm'] 
quotes_seekers = db['seekers']
quotes_test = db['test']
quotes_list = list(quotes) + list(quotes_worm) + list(quotes_seekers)

# Reddit client
reddit = praw.Reddit(
  client_id = reddit_client,
  client_secret = reddit_secret,
  user_agent = "QUOTE_BOT:%s:1.0" % reddit_client
)

# Update function
def update(type, timestamp, text):
  quote_list = []
  quote_list = db[type]
  new_text = text.replace(";", " \n") + " \n" + timestamp
  quote_list.append(new_text)
  db[type] = quote_list

# Dictionary of channel member names and DND character names
name_dict = {
  'jon' : ['Jon', 'Jonathan'],
  'jonathan' : ['Jon', 'Jonathan'],
  'eric' : ['Eric'],
  'jason' : ['Jason'],
  'cj' : ['CJ', 'Ingeqk'],
  'vivian' : ['Vivian'],
  'don' : ['Don'],
  'prad': ['Prad'],
  'pradyumna': ['Prad'],
  'krystal' : ['Krystal', 'Ophellya'],
  'anthony' : ['Anthony', 'Ejis'],
  'travis' : ['Travis', "V'dun"],
  'victor' : ['Victor', 'Jimson']
}
name_triggers = name_dict.keys()

# Function to output quotes on name triggers
def fetch_quote(name):
  name_outputs = name_dict[name]
  choice_name = random.choice(name_outputs)
  quote_list_by_name = [quote for quote in quotes_list if quote.startswith(choice_name)]
  return random.choice(quote_list_by_name)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  await client.process_commands(message)
  msg = message.content # simplify message content as msg variable
  
  # Check that bot doesn't respond to itself
  if message.author == client.user:
    return

  # Quote commands
  if msg.startswith('$quote'):
    if msg.startswith('$quote '):
      value = msg.split('$quote ', 1)[1]
      if value == "worm":
        await message.channel.send(random.choice(quotes_worm))
      elif value == "seekers":
        await message.channel.send(random.choice(quotes_seekers))
      elif value == "test":
        await message.channel.send(random.choice(quotes_test))
      elif value == "irl":
        await message.channel.send(random.choice(quotes))
      else:
        await message.channel.send("Remember to specify which type of quote you want to see (irl, worm, seekers)")
    else:
      await message.channel.send(random.choice(quotes_list))

  # Generates quote when messages contain names
  word_by_word = msg.lower().split()
  for word in word_by_word:
    if word in name_triggers:
      await message.channel.send(fetch_quote(word))
      return
    
  # naive approach
  '''
  if 'jon' in msg.lower():
    # quotes_jon = [quote for quote in quotes_list if re.findall('jon', quote, flags=re.I) or re.findall('jonathan', quote, flags=re.I)]
    quotes_jon = [quote for quote in quotes_list if 'Jon' in quote or 'Dewdrop' in quote]
    await message.channel.send(random.choice(quotes_jon))

  if 'eric' in msg.lower():
    quotes_eric = [quote for quote in quotes_list if 'Eric' in quote or 'Eggric' in quote or 'Ostin' in quote]
    await message.channel.send(random.choice(quotes_eric))

  if 'jason' in msg.lower():
    quotes_jason = [quote for quote in quotes_list if 'Jason' in quote or 'Thallan' in quote]
    await message.channel.send(random.choice(quotes_jason))

  if 'cj' in msg.lower():
    quotes_cj = [quote for quote in quotes_list if 'CJ' in quote]
    await message.channel.send(random.choice(quotes_cj))

  if 'don' in msg.lower():
    quotes_don = [quote for quote in quotes_list if 'Don ' in quote or 'Rhomi' in quote]
    await message.channel.send(random.choice(quotes_don))

  if ' vivian ' in msg.lower():
    quotes_vivian = [quote for quote in quotes_list if 'Vivian' in quote or 'Nomira' in quote]
    await message.channel.send(random.choice(quotes_vivian))

  if ' prad ' in msg.lower():
    quotes_prad = [quote for quote in quotes_list if 'Prad' in quote or 'Rone' in quote]
    await message.channel.send(random.choice(quotes_prad))

  if ' krystal ' in msg.lower():
    quotes_krystal = [quote for quote in quotes_list if 'Krystal' in quote or 'Ophellya' in quote]
    await message.channel.send(random.choice(quotes_krystal))

  if ' travis ' in msg.lower():
    quotes_travis = [quote for quote in quotes_list if 'Travis' in quote or "V'dun" in quote]
    await message.channel.send(random.choice(quotes_travis))

  if ' anthony ' in msg.lower():
    quotes_anthony = [quote for quote in quotes_list if 'Anthony' in quote or 'Ejis' in quote]
    await message.channel.send(random.choice(quotes_anthony))

  if ' victor ' in msg.lower():
    quotes_victor = [quote for quote in quotes_list if 'Victor' in quote or 'Jimson' in quote]
    await message.channel.send(random.choice(quotes_victor))
  '''
  
  # List the last 10 inputted quotes of a given quote type
  if msg.startswith('$list'):
    quote_list = []
    channel = message.channel
    author = message.author
    await message.channel.send('Which quote list would you like to see (irl, worm, seekers)?')
    def check(m):
      return m.author == author and m.channel == channel and (m.content in db.keys())
    try:
      response = await client.wait_for('message', check=check, timeout=30.0)
      quote_list = db[str(response.content)]
      last_10 = quote_list[-10:]
      output_string = ""
      for quote in last_10:
        output_string += quote.replace("\n", "")
        output_string += " \n"
      await message.channel.send(output_string)
    except asyncio.TimeoutError:
      await message.channel.send("Time's up!")
      return
     
  # Add quote command  
  if msg.startswith('$addquote'):
    author = message.author
    channel = message.channel
    # User chooses what type of quote this is
    await message.channel.send('What type of quote do you wish to add (irl, worm, seekers)?')
    def check1(m):
      return m.author == author and m.channel == channel and m.content in db.keys()
    try:
      response = await client.wait_for('message', check=check1, timeout=30.0)
      quote_type = response.content
    except asyncio.TimeoutError:
      await message.channel.send("Fine then, don't choose. See if I care.")
      return
    # User inputs timestamp
    await message.channel.send('What is the timestamp of this quote? (e.g. 3/14/15 9:26pm Session 53)')
    def check2(m):
      return m.author == author and m.channel == channel
    try:
      response = await client.wait_for('message', check=check2, timeout=60.0)
      quote_timestamp = response.content
    except asyncio.TimeoutError:
      await message.channel.send("Time's up!")
      return
    # User inputs quote
    await message.channel.send("Type the quote. For more than one line, separate them by a ';' with no space between. \n(e.g. A: There's only one thing worse than a rapist, boom.;B: A child.;A: No.)")
    try:
      response = await client.wait_for('message', check=check2, timeout=180.0)
      quote_text = response.content
    except asyncio.TimeoutError:
      await message.channel.send("Time's up!")
      return

    # Update quote list
    update(quote_type, quote_timestamp, quote_text)
    await message.channel.send("Successfully added quote!")

  # Delete last added quote command by quote type
  if msg.startswith('$del'):
    value = msg.split('$del ', 1)[1]
    if value == "worm":
      quotes_worm.pop()
      db['worm'] = quotes_worm        
      await message.channel.send('Quote deleted!')
    elif value == "seekers":
      quotes_seekers.pop()
      db['seekers'] = quotes_seekers
      await message.channel.send('Quote deleted!')
    elif value == "test":
      quotes_test.pop()
      db['test'] = quotes_test
      await message.channel.send('Quote deleted!')
    elif value == "irl":
      quotes.pop()
      db['irl'] = quotes
      await message.channel.send('Quote deleted!')
    else:
      await message.channel.send("Remember to specify which type of quote you want to delete ('irl', 'worm', or 'seekers')")

# help command (need to expand)
@client.command()
async def help(ctx):
  embed=discord.Embed(title="Quote Bot Commands", url="https://i.pinimg.com/736x/ba/92/7f/ba927ff34cd961ce2c184d47e8ead9f6.jpg", description="Use the prefix '$' for all commands", color=discord.Color.gold())
  embed.add_field(name=":speaking_head: Random Quote Generation", value="`quote` (all quotes) \n`quote irl` (for non-campaign specific quotes) \n`quote worm` (for Worms 'R' Us quotes) \n`quote seekers` (for Seekers quotes)", inline=False)
  embed.add_field(name=":wrench: Utility", value="`addquote` (to manually add a quote) \n`del + [quote type]` (deletes last added quote) \n`list` (lists last 10 added quotes)", inline=False)
  embed.add_field(name=":frog Frog", value="")
  await ctx.send(embed=embed)

# sends discord random frog image
@client.command()
async def frog(ctx):
  frog_submissions = reddit.subreddit('frogs').hot()
  post_to_pick = random.randint(1,50)
  for i in range(0, post_to_pick):
    submission = next(x for x in frog_submissions if (not x.stickied and not x.is_self))
  await ctx.send(submission.url)

  
keep_alive() # uptime robot to keep bot running every 5 seconds
client.run(my_secret) # run the bot