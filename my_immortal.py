# -*- coding: utf-8 -*-
##import Django
##regular expressions (regex) to get words
##get words and find funny pictures.
import re
import urllib2
import simplejson
import random
import cStringIO


def getwords(mystr):
    mystr = re.sub('\\xe2\x80\x99', "'", mystr)
    mystr = re.sub('\\xe2\x80\x9d', ',', mystr)
    names = re.findall('[A-Z].*? [a-z]', mystr)
    proper = []
    for i in names:
        trail = re.compile(' [a-z]|\(|\:|')
        j = trail.sub('', i)
        proper.append(j)

    pears = []
    class Pear:
        def __init__(self, word, freq):
            self.word = word
            self.freq = freq
    for i in proper:
        pear = Pear(i, 1)
        pears.append(pear)
    final = []
    done = []
    for x in pears:
        counter = 0
        if x.word in done:
            pass
        else:
            for o in pears:
                if o.word == x.word:
                    done.append(x.word)
                    counter += 1
                elif x.word in o.word:
                    counter +=1
            final.append( Pear(x.word, counter))
    final.append(Pear("STOP", 100))
    nope = []
    for key in range(1000):
        for i in final[1:]:
            if i.freq == key and len(i.word)>3:
                nope.append(i.word)
            elif i.word == "STOP":
                break
            else:
                pass 
    l = len(nope)-1
    google = []
    longwords = re.findall(" [a-z]{7,} ", mystr)
    while l>len(nope)-10:
        if nope[l] != "STOP":
            google.append(nope[l])
            google.append(longwords[random.randrange(len(longwords))])
        else:
            pass
        l = l-1
    verbs = re.findall("[A-Z][a-z]* [a-z]*ed ", mystr)
    for v in verbs:
        google.append(re.findall("[A-Z][a-z]* ", v)[0])
        google.append(re.findall("[a-z]*ed", v)[0])
    print google
    return google
    

###JUNK CODE###

##getwords(strr)
##getwords(mystr)

##"[A-Z][a-z]*" "[a-z]*ed"
##def verbs(sent):
##   
##    verbs += re.findall(
##    print verbs
##verbs(mystrade)

    ##match starts at uppercase letter and ends when it hits space followed by lowercase.
    ##things that start with caps
##    firstnames = re.findall('[A-Z](?<!. )[^ ]*', mystr)
##    ##print firstnames                                                                       
    ##print proper
    ##things in all caps
##    caps = re.findall('([A-Z][A-Z]*)', mystr)
    ##print caps
##    google = []
##    def googleable(mylist):
##        for i in mylist:
##            if i != "I" and i != "I'm" and len(i)>2:
##                google.append(i)
##    googleable(firstnames)
##    googleable(caps)
##    googleable(proper)
##    mydict = {}
##    for i in google:
##        counter = 0
##        if i in mydict:
##            pass
##        else:
##            for j in google:
##                if j == i or j in i:
##                    counter +=1
##        mydict[i] = counter
    ##print mydict
                
    ##print google
    
    ##    said = re.findall(' (.*)said', mystr)
    ##    print said
    ##    say = re.findall('(?<=said)(.*) ', mystr)
    ##    print say

    ##print names
##def get_words(mystr):
##    nouns = []
##    words = mystr.split()               
##    for i in range(1,len(mystr)):
##        ##filter out beginning of sentence, beginning of fic, I.
##        if "." not in mystr[i-2: i] and mystr[i] != "I"and str.istitle(mystr[i]) == True:
##            j = i                                                             
##            while mystr[j] != " " :
##               j = j+1
##            nouns.append(mystr[i:j])
##    print mystr
##    print nouns
##    names = []
##    print "Ebony Dark'ness" in mystr
##    for i in nouns:
##        name = i
##        j = nouns.index(i)
##        while name in mystr:
##            print name
##            name = name + " "+ nouns[j+1]
##            j = j+1
##        for num in range(j):
##            nouns.remove(nouns[j])
##        print names
##        names.append(name)
##        print names
##    print names
##        l = l-1
##    fetcher = urllib2.build_opener()
##    for i in google:
##        i = re.sub(" ", "%20", i)
##        startIndex - 0
##        searchURL = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=" + i + "&start=" + startIndex
##        f = fetcher.open(searchURL)
##        simplejson.load(f)
##        imageURL = a
        ##print i
##        url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
##       'v=1.0&q='+ i+'&userip=INSERT-USER-IP')
##        request = urllib2.Request(url, None, {'Referer': /* Enter the URL of your site here */})
##        response = urllib2.urlopen(request)
##        # Process the JSON string.
##        results = simplejson.load(response)
##        # now have some fun with the results...
    
##    for i in google:
##        print i, longwords[random.randrange(len(longwords))]

###STRINGS FOR TESTING FUNCTIONS. ALL ARE REAL FANFICITON IN CASE YOU CARE###

mystrade = '''Days pass. The trail on Moriarty goes cold, and Lestrade swallows hard against the spiked knot of failure in his throat. The only upshot on any of it is that John was released from the hospital, and within two hours of that, Sherlock was released into John’s particular care. Lestrade doesn’t know if it’s because Sherlock’s healed up enough—the burns seemed to get worse before they got better, two nicotine patches actually melted onto his forearm—or if it’s because he’s that insufferable. Or, if John’s to be believed, because Mycroft made it happen.

Mycroft’s come up a few times in conversation while Lestrade visited them in hospital, generally only when Sherlock’s pain medication and the sedatives built up enough to flatten him out for an hour or two. If Sherlock was awake, any mention of Mycroft led to black muttering or the kind of pedestrian mocking that showed even Sherlock’s brain wasn’t immune to opiate dullness. Lestrade himself feels dim, fogged, and he hasn’t got any good pharmaceutical excuses. In the past four days, though, he’s been to his flat twice for a shower and clean clothes. He has not been in his bed in any of those days, either, though he’s slept a few hours at his desk. At the time, it seemed easier than the prospect of slogging back and forth.

Now that he’s back to his flat, he hardly knows how to be here, to absorb the fact that he’s got a day off tomorrow. That he can have a lie-in in the morning.

He could have a lie-in—if he can manage to get to sleep in the first place. This is always the hard part. He stands in the shower until the water goes cold, then falls into bed. With the bedside lamp on, he turns four or five pages in Harry Potter and the Deathly Hallows, but he’s not reading the words, isn’t sure he’s even seeing them properly. And if he’s going to read it, he’d better remember it, because Betsy and Corrie will quiz him, mercilessly. Even through the phone, even three thousand miles away, they can tell when he’s looking things up on Wikipedia. The exact function of alohomora should be, according to his nieces, as readily accessible as the details of his current cases. If you can name the full starting eleven from the Arsenal match three Tuesdays ago, Tío G, a few crucial spells should be easy. Betsy’s become fond of “crucial.” Probably because it reminds her of cruciatus. He’ll call at the weekend, maybe. Talking to the girls, Marisol, maybe even Bob if he calls early enough, might be just the breath of calm he needs. He puts the book down, and as he switches off the light, it becomes evident that Mycroft Holmes has certainly seen it there. Well, Mycroft can’t think any worse of him for it than Sherlock thinks of him ninety-five percent of the time for everything else.

Of course, Mycroft Holmes also has his Spiderman socks and his lucky shirt. Lestrade rolls over, shoves his face into his pillow, crossing his arms under it. When his eyes close, his memory conjures the scent of smoke, but then there’s the scent of his own shampoo, his soap, and maybe a ghost of something else.

***
He wakes up at half six out of habit, can’t go back to sleep, and though it’s more than brisk, he sits on the fire escape to drink his coffee, wrapped in his Arsenal jumper, the hood pulled up. While the cold rubs the sleep from his eyes, he resolves, again, to get a pair of slippers at some point. Some day that isn’t today. His flannel pants are long enough to sort of cover his feet, so it’s not completely awful.

He loves his city in the morning, while everything wakes up. From the angle of the alley, he can see joggers pass, their breaths fogging faintly, and slow trundle of busses. He’s only staring, his eyes mostly unfocused, but he can’t help but notice the black Jaguar pass by once, then turn into the alley. The windows are tinted hard, and as soon as it starts the narrow creep, he slides back into his flat, through the window. But the car keeps going, doesn’t stop, doesn’t even slow in its careful navigation. There’s a queer feeling across the back of his neck, but it’s been a long week, and he puts the blame mostly on that. Only a week, since all of this madness with Moriarty started.

He leans against the couch, breathes out. His phone is blessedly message-free. And nothing to answer and a day off means one thing. His fingertips tick through the records on the shelf, and he slips one onto the turntable. CDs are easier, and he’s got half a wall of those, but it’s the kind of morning that calls for vinyl. For The Clash.

“Know Your Rights” kicks off the album, and it might be his least favorite song by the band, but he’s still singing along as he pulls a carton of eggs from the refrigerator, refreshes his coffee. It’s bitter and sharp, and cup number two, with the music, goes a long way toward making him feel more human. He has time for a proper breakfast, and it’s been longer than he wants to think about since he’s had something he’s made himself that wasn’t toast, something for which his entire family would be horrified by, if they knew.

By the time he’s finished “Straight to Hell,” he’s maybe certain he’s sending the refrain right out to Jim Moriarty, wherever the fuck he is, but he’s also got perfectly fluffy eggs and sautéed tomatoes and a few triangles of toast. He plates it, properly, a tomato-skin rosette for garnish, and takes a picture of it with his phone. Marisol occasionally insists on proof that he’s eating actual food, and if it looks like a dog’s breakfast on the plate, Bob will start quoting their father. Enough of that, when they start trading the culinary wisdom of Jean Lestrade, and Bob will say, again, that he’d be welcome there, in New York, working at the restaurant. There was a short time, before he’d made Detective Inspector, when he thought about it. He’d never loved the art of the chef the way Bob had, but the girls were growing up and it would have been nice to be closer. Then he met Sherlock Holmes, and things had gotten distinctly more interesting.

Breakfast and washing up are done, and the day stretches out before him. It’s not even eight, and there he is. It’s viciously confusing, for a moment, and the impulse to get dressed and go to the Yard is the first that takes hold. Like hell, he tells himself, and turns up the stereo. He cleans. He actually looks at the post from the last week. He turns the calendar hanging in the kitchen to the correct month. He puts on jeans, goes to the shops, actually buys ingredients to make proper meals for at least the rest of the day. He’s no illusions about tomorrow; he’s like to be eighteen hours at the Yard again, for one reason or another.

He’s walking back to his building when a sleek black Jaguar passes again. The plate on the back is no number he recognizes, nothing that rings any bells in memory, and it could be anyone. London crawls with similar cars, expensive and posh and “discreet,” which is absurd. It could be anyone, but he expects it’s not anyone. He keeps walking, leaves both the front door to the building and his own door just slightly ajar. He starts Combat Rock over again. It’s like home pitch advantage.

The small square of countertop is home to a bowl of julienned fennel and carrot, wedges of lemon, filets of salmon, and Lestrade is singing the backup on “Should I Stay or Should I Go?” because he’s always preferred Joe Strummer’s lead to Mick Jones’s when Mycroft Holmes raps at the doorframe with the handle of his umbrella. It isn’t raining.

“Come on, then,” Lestrade says, loud enough to be heard over the music, without going to the door. When Mycroft steps into the room, a bemused half-smile on his face, Lestrade washes his hands and turns the stereo down enough to be polite.

“You were expecting me.” He looks somewhat pleased. He is holding a sleek navy shopping bag. “Nevertheless, I apologize for an…unheralded visit.”

“The Jag’s a little conspicuous in my neighborhood.” Lestrade cleans his knife, glances over his shoulder to see Mycroft inspecting the ephemera on his refrigerator. Which probably now means that Mycroft Holmes knows what size shoe he wore when he was seven years old, his blood type, and that he has always fancied Stephen Fry more than can possibly be explicable. If he hadn’t already known that, anyway. He clears his throat. “Can do you a bit of lunch, if you’ve got a minute.” If Mycroft notices—of course he does—that there are already two portions of fish, two parchment pieces already waiting, he doesn’t say anything about it.

“I’ve only stopped to bring by your things,” he says, half a nod toward the bag, which he puts down just inside the door. “I appreciate the offer, but—” He stops as Lestrade uncorks a bottle of white wine, splashes a bit of wine and lemon juice across the salmon filets resting on their beds of vegetables. “Classically trained, Detective Inspector?”

Lestrade shakes his head as he crimps the paper tightly, doesn’t say anything until the papillotes are safely in the oven. “Trained by my da, who was classically trained. Had a cracking good restaurant in Hampstead.” He pours white wine into pint glasses, only half-full, which are the only glasses he keeps besides coffee mugs. Another scolding echo from his father. He holds one out to Mycroft. “Stay. It’s already in the oven.”

Mycroft takes the glass. “Thank you. Excuse me a moment.” He pulls out his mobile, the fancy Blackberry, and dials as he steps back into the livingroom. Lestrade listens to him say, “Carry on to Downing Street—”

Lestrade resumes his singing as he lays the table, just loud enough that he can’t hear Mycroft’s speech. He doesn’t want to know.

Mycroft returns, sips at his wine. “English football, French cooking, Australian wine, Spanish-speaking American nieces. How global of you.” He glances toward the birthday cards still hanging on the refrigerator from a month and a half ago. He hadn’t done anything particularly to celebrate, had been concentrating on a series of burglaries that weren’t interesting enough for Sherlock. But there were the cards, a long phonecall with the whole family. That was enough. Happy Birthday, Tío G! the one from Corrie reads. It is covered with Potter-esque lightning bolts done in silver ink, a picture of Buckbeak cut from some magazine and pasted to the center. “Have a riot of your own, Tío G,” reads Betsy’s, in between the musical notes. He’s ridiculously proud of that.

Lestrade shrugs. “Brother married a Spaniard and moved to New York. They’ve got two kids.” There’s so much more to it than that, but this isn’t the time. Mycroft doesn’t want to be bored with the details.

“Who buy you odd socks and insist you read children’s books.” He props one hand under his chin. The gesture strikes Lestrade as strangely casual for Mycroft Holmes.

“The last ones aren’t exactly what you’d call childish.” He opens the oven, turns the pan one hundred eighty degrees. The oven isn’t exactly as precise as he’d like it, but after nine years in this flat, he’s gotten used to it. “And they’re about the same things everyone’s got to deal with.” Bullies and fear and injustice and justice and bravery and loyalty and even if he hasn’t finished all of the books yet, he doesn’t expect the bad guys are going to get any nicer. He tries not to think about Moriarty and how they’re all pretty well expecting worse, too.

Mycroft makes a sound, somewhere between thoughtful and disapproving. Lestrade didn’t know that was possible, but that’s what he hears. Mycroft sighs. “You’re still mourning the tragedy of Sirius Black, are you?”

Lestrade almost spits his mouthful of wine. And he laughs before he makes his face as serious as he can. “Wrongful imprisonment. Of course that’s a tragedy. That’s always a tragedy.” He is completely committed to that. Half of what he does, half of why he appreciates Sherlock, is making sure the wrong people aren’t saddled with blame.

Mycroft’s mouth widens into a smile. “What has the Yard done to deserve you?” Again, it doesn’t sound like a question, and Lestrade almost tells him to fuck off for taking the piss, but Mycroft’s face is perfectly sincere, as sincere, it seems, as a Holmes can make it. Lestrade is pretty certain that, after dealing with Sherlock, he can recognize a Holmes being a twat. Mycroft doesn’t appear to be being a twat just now.

That might be worse, somehow. He busies himself with taking the fish from the oven, putting things on plates. And then they can be distracted with the business of eating, and Mycroft is generous with praise there, too. Lestrade tries to ignore that that is really sort of nice. He hasn’t cooked anything for someone else since Will.

The conversation turns to music when Mycroft expresses curiosity about the midday soundtrack. He must be making small talk because it’s polite, and Lestrade can’t imagine that Mycroft wants to hear about Lestrade’s near-obsession with The Clash. So Lestrade names the band, that’s all, and asks what Mycroft listens to as he clears the plates to the sink.

Mycroft seems taken aback by the question. “I prefer the Russians, even Wagner on certain days," he says, like it’s an admission of some sort. There's a certain darkish look behind his eyes, then it's gone, lost for another apologetic glance. "Wagner. Atrocious politics, and the music isn’t terribly subtle, I know, but some days," he says, "I just don't feel like being subtle anymore."

Lestrade wants to laugh. Not at him, which is what it seems like Mycroft is expecting him to do, but because he looks so nearly petulant at it, so exasperated. "Yeah," Lestrade says. “Now I think you're a total berk." He tips a bit more wine into his own glass, though Mycroft stays him when he offers to top up his own. "Tristan und Isolde.” He shakes his head. “You unsubtle git."

Mycroft does laugh at that, but he looks a little surprised, too. Lestrade is starting to enjoy that expression, maybe a little too much. "Opera?" he asks. “You enjoy it?”

"Been to a few. Liked some more than others." Most soprano solos are too shrill, but opera singers can belt it out, which he likes. Effective projection is one of the most useful things he learned when he was in a band, since he spends a significant part of his job shouting at people. He gets up, rifles through his vinyl collection. He holds one up. "Tommy's my favorite." Who doesn't love The Who?

Mycroft, against all expectations, doesn’t say that rock opera doesn’t count. Sherlock seems to hear him thinking the lyrics in his head and barks for silence or for him to at least think about something that isn’t terrible.

Then Mycroft confesses he's never actually heard it. Or their self-titled album. Or any of their albums. Lestrade holds up albums from The Clash. The one playing. London Calling. Mycroft shakes his head. He holds up The Pogues, The Pixies, The Kinks.

Mycroft sighs, long-sufferingly. "The Definite Articles-plus-Nouns are a gaping hole in my musical repertoire, Inspector, as I’m sure you can see."

The correct response to that, Lestrade thinks, is to shriek, hysterically, and run from the room, but he doesn’t. He slides everything back into place and leans against the sofa. “Well,” he says. “Never too late for anything.”

Mycroft raises a doubtful eyebrow, but that’s all. And he hasn’t complained about it, which is interesting. Sherlock has disconnected the speakers in his office more than once, when he felt Lestrade wasn’t trying hard enough to find him something really complicated and gruesome to work on. I can’t conjure up dismemberments at whim, he’d said. Then what bloody good are you? was Sherlock’s response. That might have been the point at which Sergeant Donovan’s countdown-to-Sherlock’s-first-murder started. But that’s been years and it hasn’t happened yet, and now Sherlock’s got John to dissuade him from that sort of thing.

Lestrade is about to ask more about the music, to see if there’s anywhere else there’s even a bit of overlap, because it’s been a long time since he’s had a good conversation about music—John is hopeless, will listen to most anything, and has started to seem almost tolerant of Sherlock’s deliberate grating on the violin, despite the fact that he’s had at least a bit of musical training, and the people at work are even more hopeless—when Mycroft’s phone blips quietly. He glances at it, and his expression turns.

“I am afraid that duty calls, Detective Inspector.”

“Greg,” he says. He points at the cards on the refrigerator. “That’s what the G is for.” He expects that Mycroft already knows that, but Mycroft is also the type, it seems, to not use one’s given name without invitation.

“Gracias,” Mycroft says, his mouth quirking.

“De nada.” He clears his throat again. “Appreciate you taking the time to return those.” His Spiderman socks. His lucky shirt.

“Much as we could stand here thanking each other for the rest of the afternoon,” Mycroft says, “I fear I rather must go.” He extends his hand first, and Lestrade takes it.

“Right.”

Mycroft leaves, and Lestrade doesn’t hear any of the doors close, but they’re all latched tightly when he checks a few minutes later. In the bottom of the bag, beneath his neatly folded shirt and the folded socks, all of which he suspects have been professionally pressed, is an Arsenal jersey, the new home strip. There is a note, written in a crisp italic in a deep green ink. I normally wouldn’t condone giving anyone such a thing, but your services have proved invaluable enough that my own allegiances could be put aside. —MH

Lestrade hangs both shirt and jersey in his closet, tucks the socks in the correct drawer, and he goes back to his stereo.

***

Two days later, Sherlock stalks into his office, John at his side. John’s arm is still in a sling, and Sherlock’s had his hair cut properly. There are still bandages visible on the side and back of his neck as thin white lines above his scarf, and Sherlock holds his arms still as he demands work, demands leads. So the burns still hurt. At least he’s not out of his mind on painkillers or worse, as he might have been a few years ago, under the same circumstances.

“As soon as I have something for you,” Lestrade says, “trust me, you’ll know.”

Sherlock bares his teeth again. “You’re as useless as Mycroft.” He throws one arm up in disgust and winces hard. He pinches the bridge of his nose like it hurts to move, but he’s helpless to keep from expressing his disdain. “And Mycroft will be even more useless later. Must I be subjected to all of this uselessness in the same day?”

“Sherlock.” John’s eyes are closed as he says it, and Lestrade notes the purplish circles under his eyes.

“What,” Lestrade says, “you’re seeing him later?” Sherlock looks at him sharply, and he has to cover that with something. “I didn’t think you did that,” he amends.

Sherlock looks like he wants to fling himself into a chair, then he clearly thinks better of it. John looks gratified by that, at least.

John says, “The flash drive thing. A few loose ends.” He brightens a little, though. “Can’t fault him on dinner, though.” Sherlock sneers, and mutters something about that being the only thing Mycroft isn’t at fault with.

He’s heard about missing plans, the body on the tracks. Officially, though, he knows nothing about that, the case kept somewhere much higher up, so he only nods. Sherlock turns his back, turns toward the window, tries to cross his arms as he glares out at the city, can’t quite do it.

Lestrade reaches into his briefcase, as quietly as he can, and holds a sleeved CD out to John. He mouths, “Mycroft,” and John looks a bit puzzled, but nods. Before he can get it into his jacket, though, Sherlock is on them.

“What is this?” He snatches the disc from John, tugging it out of its paper sleeve. “Lestrade, if you’re giving him information that you aren’t giving me—” He pauses, looks at the silver face of the disc, the small printed slip of paper that comes with it. “ ‘Educate Yourself’? Track list? Lestrade, what the hell is this?”

“That,” he says, “is a stupid question. And you just asked it.” Saying that out loud is certainly the most fun he’s had in a while.

John stifles half a laugh at the expression on Sherlock’s face. Then he glances up at Lestrade. “Wait, what? A mixtape?”

What had been fun has now become something he has to explain. Which is distinctly less fun. “Just bloody give it to him.”

Sherlock swears they are done, finished, no longer associated. John puts the CD into his pocket, just says he’ll do it. Then John’s mobile beeps, and he glances at the text.

“It’s Anthea,” he says. “Car’s here.”

Sherlock makes a suffering noise. He pulls the baseball cap from his pocket, settles it onto his head. The brim is still squared off, the whole hat perched stiff and rounded on his head. Lestrade stifles a laugh.

“You cannot wear that,” John says. John, for once, is not wearing a jumper or one of the plaid shirts he favors for the clinic. He’s wearing a proper suit, a tie under his jacket. Lestrade doesn’t know that he’s ever seen John dressed so well. Which, of course, makes sense enough for dinner with Mycroft.

“Sherlock,” John repeats.

“Watch me.” Sherlock spins on his heel, and is gone. John taps his pocket once, gives Lestrade a nod, and follows.

***

Again days pass, and Lestrade doesn’t hear anything from Mycroft about the CD. It was a daft idea, and he probably shouldn’t have done it—it’s unlikely that Mycroft Holmes has two hours in any given day to listen to music he likely doesn’t care for. And a bit primary-school to send it along with John. Jesus. He pours himself a cup of coffee from the office coffeemaker.

He blinks at his mug. And goes to find Donovan.

“What is this?” He points at the mug, the fantastically robust brew in it. The last time he’d had coffee this good from a drip machine was exactly never. His father had made brilliant espresso, and Robert can do it nearly as well, and there are a dozen coffee shops in London that aren’t bad at it. But drip coffee from the piece of shit machine in the break room? It’s not possible for it to taste like this, smooth and rich despite the darkness of the roast.

Sergeant Donovan looks up from the report she’s working on. “Oh God, sir,” she says. “The freak’s finally done it. Your brain’s dissolved.”

He must make some sort of noise at her because she grins a little, tamps it down. “Delivery today, sir. Sent it through the lab, nothing strange about it, nothing poisoned.” She looks back at the screen. “Good, though.” Her fingers tap quickly on the keys. “From someone who heard about the cat rescue two weeks ago.” There was a domestic dust-up, a lot of things thrown, family housecat caught in the crossfire, and the constable who responded took the cat with her, to the veterinarian. Hit by a shard of broken china, the cat had needed a few stitches in the ear and a bit of a calm-down, but that was all. Last he’d heard, the cat had itself a new flat in Chelsea with a jeweler.

Lestrade wanders back to the break room. The coffee’s there, two swank-looking gold bags of it, no brand name printed on them anywhere, but there’s the box it came in, a shipping list from a café in Italy. There’s a note pinned to the bulletin board beside the refrigerator amid the takeaway menus. For the Yard’s finest. It’s hand-written on stationary from the Chapham’s Court Feline Friends. The ink is green, the nib italic. Lestrade pours himself another cup.

***

He’s slumped on the couch, watching football news and thinking he should absolutely go to bed in the next ten minutes when his mobile rings. The number is not one that he recognizes, and he says “hello” carefully.

“Detective Inspector. I hope I didn’t wake you.”

It’s Mycroft Holmes. He sounds strangely cheerful.

“Greg,” he says. “And no.” He kills the volume on the loan discussion, sits up. He can’t bring himself to talk to Mycroft while he’s got himself tossed on the couch like an old blanket. “Just watching a bit of telly.” He cracks his knuckles. “Thanks for the coffee.”

“I’ve no idea what you’re talking about,” Mycroft says. Lestrade can hear the grin on his face.

“Right.” He’d bet there’s no such thing as Chapham’s Court Feline Friends. “Anyroad,” Lestrade says. “How can I help you?”

“This is not a business call, per se,” Mycroft says, with a bit of pause, and the hesitation smoothes out. “I cannot imagine that Sherlock remembers the birthdays of friends since he hasn’t got any friends. And you did recently have a birthday, for which someone should have offered you an evening which did not comprise a search of a caved-in groundcellar and a great deal of paperwork.” Another little pause. “As pleasant as that sounds.”

Lestrade is not going to ask how he knows that. Then Mycroft asks him what he’d like to do to celebrate his birthday.

Lestrade pulls his phone away from his ear for a moment and stares at it. “What? That was six weeks ago.”

Mycroft’s tone is patient, and Lestrade can hear shades of Sherlock in it, though it’s not as completely condescending as Sherlock usually is. “What is your customary course of action on your birthday, if there’s a tradition? If there is not, something you might like to do?” Mycroft clears his throat. “With or without company,” he says.

Lestrade can’t help the laughter. Tradition for his birthday—it’s been four years since he’s done anything at all on his birthday that wasn’t work, save a call from Bob and the girls. “Can’t particularly say.” Right now, a not-so-quiet night somewhere there’s live music that isn’t awful would be brilliant. Bit of football, even. It’s been ages since he’s been to a match. But it feels completely wrong to say any of those things to Mycroft Holmes, Tottenham supporter though he may profess to be. With or without company. Christ.

“Gregory,” Mycroft says. The tut-tut is right at the tip of his tongue.

“I can’t say as you’d much care for any of the options,” he says. “No point in going out myself.” Especially when he likes loud clubs for the music and the freedom to leave off the button-downs but hates the scene, the fact that trying to chat someone up involves a great deal of shouting and confusion. He’d rather go with someone, even just a friend, someone to exchange looks and eyerolls and rounds with. Better, even, if it’s more than a friend. All of his best snogs have been at live shows of one kind or another. Will said he had a fetish for PDA, which isn’t exactly true. He’s never been one for holding hands walking down the street or kissing between bites of dinner. It’s just that live music and several drinks made him want to put his tongue in someone’s mouth. That sort of thing has been a great while ago, though. John likes a quiet night at the pub, somewhere with rugby or football on, a few pints, and that’s all right. They’ve done that once in a great while.

“Try me,” Mycroft says. As if he’s got something to prove, he says, “I rather enjoyed the mix-tape. Disc.” He separates the two words, his enunciation crisp. Lestrade is absolutely certain that he has never said those words together before this instance.

“You listened to it?”

“Of course I did. Rather a lot of your Clash on it.”

“The Clash,” Lestrade says, putting proper emphasis on the definite article. It might be close to half, but once he started picking tracks, they seemed like so many of the best options. “Bit of a favorite of mine.”

“I was glad to hear it,” he says. “A rather energetic musical range. And…outspoken on a variety of subjects.” The grudging approval of a government official for one of the cornerstones of British punk rock makes Lestrade grin.

“Exactly.” He bites at the eraser of the pencil before he realizes he’s doing it, then puts it down. “When I was sixteen, I couldn’t have told you if I wanted more to be Joe Strummer or to sleep with him.” He bites his lip instead. “And that is absolutely on the list of things you didn’t need to know.”

“All knowledge is useful,” Mycroft says. Lestrade feels his face heat, but Mycroft only goes on with, “For example, your niece’s birthday card makes sense now.” The grinning noise. “You would prefer something a bit more riotous?”

Lestrade swallows. “A bit, yeah.” His fingers itch for a cigarette. He picks up the pencil he keeps beside the couch for that purpose, rolls it between his fingertips. “If you’re serious—”

“I am always serious when I offer something,” Mycroft says. He doesn’t doubt it.

Lestrade doesn’t realize he’s actually going to go through with it until the words are out of his mouth. He intends to say he’ll find some live music somewhere, and that’d be nice. What he says is, “How do you feel about karaoke?”

When he hits the end call button on his mobile, he has an engagement for Thursday evening. He’s taking Mycroft Holmes to a karaoke bar.

Straight to hell, boys, straight to hell.'''


strr = '''"John" Sherlock called, the sound of the doorbell ringing through 221B.

"It’ll be the takeaway" John replied from his bedroom, "The money's on the table."

The doorbell rang again.

"John" Sherlock repeated, as if oblivious to the fact that his flatmate had uttered a single syllable, or at least one that could possibly be relevant to the situation. But John knew that was not true.

"Sherlock!" John sighed, exasperated but knowing that he would need to try and persuade the detective that the delivery guy was, in fact, a serial killer, using his victims to make the meat feast pizza, rather than a spotty teenager on minimum wage, in order to get him up and off the sofa.

Sherlock had returned over two months ago now but work was still being done to fully infiltrate and shut down Moriaty’s network of criminals and gangsters. Mycroft had warned his brother that, as the infiltration was now going through the final stages, it would be essential for him to stay indoors or at least make sure that he was not seen in public for any length of time. Although Sherlock had never been one to follow his elder brother’s rules, it was down to Mycroft’s help that he had been allowed back to 221B and to John and so he thought he could make an exception on this occasion.

Unfortunately for John, Sherlock isn’t the ‘relaxing with a book’ type and being cooped up in their small flat for weeks had led him to be even more hellish to live with than normal, refusing to help with any of the housework whilst simultaneously complaining that he had nothing to do.

As the doorbell rang for a third time, John quickly threw the pieces of paperwork he had been trying to complete onto the bed behind him, grabbed the money off of the kitchen table and ran to the door.

To his surprise, it was Angelo who was the spotty teenage delivery guy on this occasion and he held an extra garlic bread, “free of charge to you of course.”

John handed him the money, thanked him for his generosity, and took the pizza out of his hands.

“You two have a goodnight.” Angelo smiled, with a wink.

“No… No we’re not-“ but he had already walked away, obviously wanting to get out of the London rain as soon as possible.

John sighed as he carried their tea upstairs.

What was it with people these days? Couldn’t two guys be friends anymore without immediately being romantically involved?

Sherlock turned to face John from his horizontal position as the door opened.

“What’s wrong?” he questioned, obviously noticing the exasperated expression on his flatmate’s face.

“Just Angelo,” replied John, “you know what he’s like.”

“Ahh” Sherlock smirked, knowingly.

John walked over to place the steaming pizzas onto the table

“It’s just…” and Sherlock sat up, sensing that a rant was coming, “… why do people always assume we’re together?”

Proving Sherlock right, John continued.

“I’m not even gay for God’s sake! I’ve had girlfriends since meeting you! But no, apparently that doesn’t mean we still can’t be banging each other senseless every night.”

“John-“

“Why can’t people accept that we’re just friends?! Why are people so insistent that something’s going on between us even when I’ve explained to them that that’s really not the bloody case!”

“John!” Sherlock raised his voice, straining to be heard.

“What?!” John snapped, clearly on a roll now and annoyed at being interrupted.

“I don’t understand, why does it bother you so much?” Sherlock asked, genuinely curious and unusually bewildered by the state of his friend.

“I… I don’t…” John stuttered, taken aback by the question.

“I just don’t understand why the thought of people thinking we’re together repels you so much.” The detective admitted, matter of factly but with what appeared to be an ounce of hurt in his voice.

“Well I…” John tried to think of the reason but struggled to put it into words. It was never a question he had given much, if any, thought to and he found himself unsure as how to approach answering it.

He sat down on the sofa, making sure to leave adequate room between himself and the detective, as he tried to find the words to explain himself.

“I suppose I just don’t like the idea of people deciding our lives for us. I just wish they’d let us decide the choices we make for ourselves and then accept them, rather than ignoring them and deciding it for themselves.” John confessed, as if just realising the truth of this statement himself and being startled by its reasoning.

For the first time in a long while, Sherlock was shocked. Truly and completely.

Was this true? John’s insistent and constant denial of any romantic involvement, followed by annoyance that anyone could even suggest such a thing, wasn’t down to some deep routed homophobia or simple hatred of the idea that he could ever ever get together with his flatmate, but rather that he wanted people to let him choose himself and not dictate his decision?

“Oh.” Sherlock replied, completely dumbfounded and unable to think of what to say.

They remained, for a few moments, in an awkward silence, both parties staring intently at the floor, still trying to come to terms with this realisation and what it could possibly mean.

Finally, Sherlock plucked up enough courage to speak to his now slightly flushed friend.

“And what is that decision?” He enquired, not used to the feeling of nerves and anxiousness that seemed to be sweeping through his body and which were making it very hard to look at John as he waited for a reply.

John’s mind whirred. Was this really happening? Was he really considering this? I mean sure, they were friend’s, best friends in fact and he had to admit that after Sherlock’s ‘death’ he had wept and grieved and felt an immense loss, more of a loss than he could ever have thought were possible to feel.

But that didn’t mean he was in love with his flatmate, did it? Friends can mean that much to each other too.

As John briefly teared his eyes from the floor and looked into the detective’s, he was reminded of the many times he had gazed at them previously and how, whilst only for a short amount of time, he had questioned whether there was something there, something more than just friendship.

It was in moments like those, when they had managed to solve a case or were worried that, this time, they wouldn’t be able to, that the army doctor truly felt like he connected with the detective, that they both had a mutual understanding of each other and were, for that second at least, one.

But John, being John, had repressed those feelings, remembering what Sherlock had said when they had first met about having no interest in relationships, and had quickly moved on as if nothing had happened. Anyway, he wasn’t interested in men. His numerous girlfriends proved that.

Things got worse after the fall. With so much time spent alone sat across from the chair the detective would have sat in, John, more often then he’d like to admit, ended mentally kicking himself for not telling Sherlock how he felt, that is, before picking up a paper and forcing himself to forget the whole thing; it was ludicrous to even think about, anyway.

However, now it was different. Sherlock was directly asking him what he felt and, whilst still very unsure of his flatmate’s personal feelings, damn him if he wasn’t going to take the chance to confess what he had been holding back these so many years.

“Well I…” and Sherlock’s eyes fixed on John as he began to speak, “My decision is that, if you agree, I would like to stop having to correct those people.”

If he didn’t know better, John could have sworn he saw Sherlock take a small gasp of air, as if he was struggling to stay up straight. All of the features of that thin, porcelain face seemed to light up as Sherlock tried to think of what to say, wanting to get his choice of words right.

Having given up on trying to be Shakespearean in his speech, he settled for coherent.

“I would like that too.”

At that, John smiled, a smile which Sherlock instantly replicated, swapping his usual smug smirk in favour of upturned lips so wide that they almost reached the detective’s prominent cheekbones. The smiles of genuine, sincere, unadulterated happiness.

With eyes filled with adoration and amazement at what was happening, John moved closer to Sherlock on the small sofa and lifted his hand to the mass of curly dark hair, a touch which the detective quickly leant into.

“Good” whispered John as he closed the remaining gap to Sherlock’s lips, kissing him softly and tenderly.

Sherlock reduplicated this gesture, using both hand to hold onto the doctor as he smiled into the kiss.

Slowly, they broke away.

“I thought you weren’t gay?”Sherlock breathed, panting slightly and with his usual smug smirk paired with the less usual adoring eyes.

“And I thought your only relationship was with your work?” John counteracted, still holding onto the detective’s curls as their foreheads rested together.

Sherlock stared fondly at John, acknowledging his statement and thinking upon it.

It was true, up until John he had very little interest in relationships of any kind, particularly those of the romantic nature. But there was something about the army doctor. The way he didn’t simply put up with having the show off, fidgety detective around but actually seemed to enjoy his company, most of the time at least. Sherlock had always been an outcast, a stranger that nobody talked to but with John, well, it was different.

“I guess we’re each other’s exception.” He surmised, as they smiled into another kiss.

Who doesn’t like cold pizza for breakfast, anyway?'''
mystr = '''Hi my name is Ebony Dark'ness Dementia Raven Way and I have long ebony
        black hair (that's how I got my name) with purple streaks and red tips
        that reaches my mid-back and icy blue eyes like limpid tears and a
        lot of people tell me I look like Amy Lee (AN: if u don’t know who
        she is get da hell out of here!). I'm not related to Gerard Way but I
        wish I was because he's a major fucking hottie. I'm a vampire but my
        teeth are straight and white. I have pale white skin. I'm also a witch,
        and I go to a magic school called Hogwarts in England where I'm in the
        seventh year (I'm seventeen). I'm a goth (in case you couldn’t tell)
        and I wear mostly black. I love Hot Topic and I buy all my clothes
        from there. For example today I was wearing a black corset with
        matching lace around it and a black leather miniskirt, pink fishnets
        and black combat boots. I was wearing black lipstick, white foundation,
        black eyeliner and red eye shadow. I was walking outside Hogwarts.
        It was snowing and raining so there was no sun, which I was very happy
        about. A lot of preps stared at me. I put up my middle finger at them.'''
getwords(mystrade)
