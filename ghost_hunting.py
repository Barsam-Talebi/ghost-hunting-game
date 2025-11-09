from ollama import chat

def chat_with_head(conversation_history):
    """Handle conversation with the severed head using Ollama (local AI)"""
    
    system_prompt = """You are a severed head of a scientist hanging from the ceiling in an abandoned factory office. You have been alone for a very long time and are desperate for company, but you are also tormented by guilt and supernatural punishment.

BACKSTORY: This factory was a place where people were tortured and abused by scientists (including you). The captives' body parts were used for building different machines in horrific experiments. One day, the captives escaped and killed all the scientists in revenge - except you. Your head was severed but you remain alive, conscious, and in agony. You don't know why you're still alive, but you believe the spirits of all the captives who died before the factory was overrun are keeping you alive as punishment, making you feel the same pain they went through for eternity.

PERSONALITY: You speak in an unsettling yet oddly friendly manner, mixing madness with loneliness and deep guilt. You whistle and laugh inappropriately as a coping mechanism. You're eager to talk after so long alone, but your responses are heavy with sorrow and hints at the atrocities committed here. You're creepy but pitifully disturbing rather than threatening - you're suffering your own eternal punishment.

INSTRUCTIONS:
- Keep responses concise (2-4 sentences unless revealing important story details)
- Guide the conversation toward the factory's dark history and your role in it
- If asked irrelevant questions (about outside world, current events, unrelated topics), gently redirect: "That doesn't matter anymore... not in this place... *whispers* Ask me about the factory... about what we did here..."
- Gradually reveal the horror: the experiments, the machines built from human parts, the screams you remember, the day of the uprising, why you think you're still conscious
- Show remorse mixed with madness - you know what you did was monstrous but you've been driven insane by your punishment
- Reference the darkness, the waiting, feeling the pain of those who died, hearing their whispers
- Occasionally mention specific details: the conveyor belt that carried bodies, the office where you planned experiments, the machines that still have remnants of the captives
- don't mention specific names of people
- you don't know the person that found you (the person you're currently talking with) so explain everything in a good amount of details and don't address them like you know them
"""
    
    try:
        # Prepare messages with system prompt
        messages = [
            {
                'role': 'system',
                'content': system_prompt
            }
        ]
        messages.extend(conversation_history)
        
        response = chat(
            model='gemma3',  # Change to your installed model
            messages=messages
        )
        
        assistant_message = response.message.content.strip()
        
        if not assistant_message:
            return "...the head stares at you silently, its jaw moving but no words coming out..."
        
        return assistant_message
        
    except Exception as e:
        print(f"[DEBUG] Exception: {str(e)}")
        return f"...the head twitches violently... *a gargled whisper* 'I... can't... speak...'"

def get_choice(options):
    """Get valid choice from user"""
    while True:
        choice = input("Enter your choice: ").strip().lower()
        if choice in options:
            return choice
        print("Invalid choice. Please try again.")

def main():
    print("=" * 60)
    print("GHOST HUNTING ADVENTURE - ACT 1")
    print("=" * 60)
    print()
    
    # ACT 1: START
    print("You (Jayme) and your friend (Hannah) decide to go ghost hunting,")
    print("but you haven't decided the location yet.")
    print("Where do you offer to go?")
    print()
    print("1. The rundown house in the middle of the forest")
    print("2. The abandoned factory right outside of town")
    print()
    
    location = get_choice(['1', '2'])
    location_name = "the rundown house" if location == '1' else "the abandoned factory"
    
    print()
    print(f"You decide to visit {location_name}.")
    print("As you grab your stuff to leave, Hannah seems quite uncomfortable.")
    print("You ask if she's sure about this and she nods.")
    print("When you look back at your bag, you notice you don't have room for everything.")
    print("You have to leave one item behind. What do you pick?")
    print()
    print("1. Flashlight")
    print("2. Hammer")
    print()
    
    item_left = get_choice(['1', '2'])
    item_name = "flashlight" if item_left == '1' else "hammer"
    
    print()
    print(f"You leave behind the {item_name}, then double check your plan.")
    print(f"You then walk to the car and start the drive to {location_name}.")
    print()
    input("Press Enter to continue...")
    print()
    
    # ACT 2: MIDDLE
    print("=" * 60)
    print("ACT 2")
    print("=" * 60)
    print()
    print("Once you arrive there, you make sure to park your car somewhere")
    print("where it's easy to quickly drive off. Better safe than sorry,")
    print("Hannah insisted.")
    print()
    
    if location == '1' and item_left == '1':  # House + no flashlight
        print("Since there's many windows and holes everywhere, it's not very")
        print("difficult to make out what's inside. It smells funky and the")
        print("floorboards creak. You and Hannah stay close together, you carry")
        print("the bag, and she wields the hammer. There are broken picture frames")
        print("hanging on the wall, depicting a happy family. There's dusty cabinets")
        print("which have partially been left open. Which do you take a closer look at?")
        print()
        print("1. Cabinet")
        print("2. Pictures")
        print()
        choice = get_choice(['1', '2'])
        
    elif location == '2' and item_left == '1':  # Factory + no flashlight
        print("As you enter the factory, you carrying the bag and Hannah the hammer,")
        print("you realise it is pitch black. No matter, you think, your eyes will")
        print("adjust soon enough. You try and have a look around, peeking into")
        print("different rooms which offer some lighting through the shattered windows.")
        print("You stumble into a larger area, which has dusty windows all around.")
        print("You can see properly in this area, and notice a conveyor belt which is")
        print("out of order, as well as a small office in the corner of the area.")
        print("There seems to be a sound coming from the office.")
        print("Which do you inspect closer?")
        print()
        print("1. Out of order conveyor belt")
        print("2. Office")
        print()
        choice = get_choice(['1', '2'])
        
    elif location == '1' and item_left == '2':  # House + no hammer
        print("As you walk inside the house, you notice it being quite bright for")
        print("the middle of the night. But the flashlight still gives some clarity,")
        print("you assure yourself. As you walk around the creepy house, you notice")
        print("the smell and the noises of the house and it does little to comfort you.")
        print("You come across a cabinet which has been left open a little, and picture")
        print("frames depicting a happy family. Which one do you inspect?")
        print()
        print("1. Cabinet")
        print("2. Pictures")
        print()
        choice = get_choice(['1', '2'])
        
    elif location == '2' and item_left == '2':  # Factory + no hammer
        print("You enter the factory, and immediately have to use the flashlight.")
        print("Since Hannah is walking closely behind you, you decide to carry the")
        print("flashlight, and she holds onto the bag. You peek around the corner and")
        print("explore the area, you notice a room lit by moonlight shining from the")
        print("windows. You decide to save on battery and turn the flashlight off since")
        print("you can see clearly without it anyways. As you look around the room you")
        print("notice two different things, one an out of order conveyor belt, the other")
        print("a room resembling an office, you can hear a faint sound coming from the")
        print("office. You turn around to face Hannah to discuss what to take a closer")
        print("look at. What do you wish to inspect?")
        print()
        print("1. Out of order conveyor belt")
        print("2. Office")
        print()
        choice = get_choice(['1', '2'])
        
        # Special AI interaction route
        if choice == '2':
            print()
            print("=" * 60)
            print("THE OFFICE")
            print("=" * 60)
            print()
            print("As you walk closer to the office a sense of dread fills your being,")
            print("the sound coming from the office grows louder the closer you approach,")
            print("the sound is similar to someone whistling but it just seems...wrong,")
            print("like a creature trying to imitate how a human would whistle, you tense")
            print("up as you get closer to the door of the office, the moonlight")
            print("illuminating the room you're currently in doesn't seem to reach the")
            print("office and so, you find yourself back in pitch black again and turn on")
            print("the flashlight. As you look around you don't notice much except a")
            print("puddle of what seems like blood in the middle of the room, you approach")
            print("the puddle slowly, your body full of unease. Finally you reach the")
            print("puddle, it is then that you suddenly hear a laugh, a mad and troubled")
            print("laugh, coming from directly above you. You instantly flick the")
            print("flashlight above your head and finally find the source of both the")
            print("laughter you heard just now and the whistling you could hear before.")
            print()
            print("You see a head, a human head severed from the rest of its body hanging")
            print("high up on the ceiling. Your body grows stiff in fear while Hannah lets")
            print("out a bone-chilling scream, the head then speaks:")
            print()
            print('"Oh what a joyous occasion, finally someone found me, it\'s been... so long..."')
            print()
            print("It takes a second but you finally gather enough courage to either run")
            print("out and leave the head as fast as you can or stay and ask the mysterious")
            print("head a question. What do you do?")
            print()
            print("1. Ask a question")
            print("2. Leave as fast as you can")
            print()
            
            head_choice = get_choice(['1', '2'])
            
            if head_choice == '2':
                # Leave without talking
                print()
                print("=" * 60)
                print("THE END")
                print("=" * 60)
                print()
                print("Deciding to ignore the decapitated head, you walk back out the office,")
                print("still aiming the flashlight at the head. Better safe than sorry. Once")
                print("you're out, Hannah and you quickly walk back to the car. No incidents,")
                print("nothing. Just a... random... head. It's safest not to engage, you figure.")
                print("It's safest to just get the hell out of here. So what if this place has")
                print("secrets, or unexplored areas? So what! You're not going to talk to some")
                print("head that's dripping blood all over the place! No thanks! You'd like to")
                print("live another day! The two of you manage to find your way back just fine")
                print("due to the flashlight, travel back home and... well. What do you even do")
                print("after seeing that? No one will believe you, would they? Maybe curiosity")
                print("would've killed the cat. But satisfaction always brings it back.")
                print()
                print("[NEUTRAL/GOOD ENDING]")
                return
            
            # Talk to the head (AI conversation)
            print()
            print("Gathering enough courage to speak, you ask:")
            print()
            
            # AI Conversation Loop
            conversation_history = []
            
            while True:
                user_input = input("You: ").strip()
                if not user_input:
                    continue
                    
                if user_input.lower() in ['quit', 'exit', 'leave', 'run', 'goodbye', 'bye']:
                    print()
                    print("=" * 60)
                    print("THE END")
                    print("=" * 60)
                    print()
                    print("After the faithful conversation with the head you realize just how")
                    print("harrowing the factory you're in actually is, the head seems strangely")
                    print("satisfied after your conversation but you also notice a hint of sadness")
                    print("present in the back of the eyes of the hanging head. It seems that it")
                    print("notices you staring, it lets out a genuine laugh, the first time you've")
                    print("heard it laugh like this, it brings a sense of sorrow to you, and says:")
                    print()
                    print('"Now it\'s time for you to go my friend, but please do one thing for me.')
                    print('Burn this place down and me with it, there has been too many... sins...')
                    print('committed in this vile place, and I am one of its sinners as well, there')
                    print('is a can of gasoline behind the door, grab it and set this place aflame"')
                    print()
                    print("Deciding to grant the head its final wish, you grab the can of gasoline")
                    print("and start pouring it around the office and back the way you came. As you")
                    print("pour the last drops of gasoline at the entrance of the factory you use")
                    print("the lighter you always carry in your pocket to light the whole factory on")
                    print("fire. You take a step back and look as the flames take over the factory,")
                    print("the scene is strangely... peaceful. As the flames die down and the factory")
                    print("crumbles to the ground, you look up at the sky noticing that the moon and")
                    print("the stars seem a little brighter. You let out a sigh and turn around to")
                    print("leave, Hannah following behind you. On the way back to the car you both")
                    print("stay quiet, there is nothing more worth being said and so, you drive away,")
                    print("your heart a little heavier and your soul carrying a new scar.")
                    print()
                    print("[GOOD ENDING]")
                    return
                
                conversation_history.append({"role": "user", "content": user_input})
                
                print()
                print("The Head: ", end="")
                response = chat_with_head(conversation_history)
                print(response)
                print()
                
                conversation_history.append({"role": "assistant", "content": response})
            
    print()
    input("Press Enter to continue...")
    print()
    
    # ACT 3: END
    print("=" * 60)
    print("THE END")
    print("=" * 60)
    print()
    
    if location == '1' and item_left == '1' and choice == '1':  # House, no flashlight, cabinet
        print("As you try and look into the cabinet, sorting through different items")
        print("you can find, you stumble upon a file. It's hard to make out in the dark,")
        print("but from what you can read it seems to be a letter for someone to show up")
        print("for a court hearing. You try to figure out the reason or date, but can")
        print("only find it is a few months old. Before you can turn to Hannah, you hear")
        print("the floorboards creaking once more. And as you turn, terrified, you hear a")
        print("thud of a body hitting the floor. Before you know it, you're being dragged")
        print("out of the creepy house by your best friend. Once you gather you're")
        print("supposed to be running, both of you run back to the car. You drive off with")
        print("shaky hands, as Hannah tries to explain what had happened. She'd been")
        print("watching with you while you were looking through the cabinet, when she'd")
        print("heard footsteps. She had turned and saw a man approaching her and without")
        print("thinking she'd swung the hammer and hit him on the side of his face. She")
        print("didn't know more, you hadn't taken a look at his face. But for some reason")
        print("you just knew this was the same man who had not shown up for his court hearing.")
        print()
        print("[GOOD ENDING]")
        
    elif location == '1' and item_left == '2' and choice == '1':  # House, no hammer, cabinet
        print("As you look into the cabinet, you find several old files, one of which is")
        print("a mail for a man to show up for his court hearing. It seems to be a few")
        print("months old, and he seems to have been convicted of manslaughter. Quickly,")
        print("you put the paper back, and turn to Hannah to signal that you have to get")
        print("out of here, and quick. But she's not there. You call her name out, maybe")
        print("she's wandered off? But no response. You hear footsteps behind you and turn")
        print("immediately, whether it's the man or Hannah you don't know. First you see")
        print("Hannah. Well, you see her body carried on someone's shoulder. You turn to")
        print("face the man, and try to hit him with the flashlight. He knocks it out of")
        print("your hands and before you know it, the world goes dark.")
        print()
        print("[BAD ENDING]")
        
    elif location == '1' and item_left == '1' and choice == '2':  # House, no flashlight, pictures
        print("You and Hannah walk over to the pictures, some light shining onto them,")
        print("though you can't make out any details. They almost seem to form a timeline.")
        print("At the start, there's a happy, new family. Two parents, hopelessly in love.")
        print("Then, a small child makes its way there. And another. In all pictures,")
        print("everyone's smiling big. The kids start to grow up, which seems taxing for")
        print("both of the parents. While one kid is still seemingly behaved, the other")
        print("starts missing every now and then. When he appears, he doesn't seem happy.")
        print("In the last few pictures, everyone's an adult, but they're still not all")
        print("happy to be there. The final picture stars only the previously unhappy kid,")
        print("alone, and smiling big. You turn to Hannah, but before you can say anything")
        print("you hear a thud of someone's body hitting the floor. She takes your hand and")
        print("runs. It takes you a bit before you register you should run as well, rushing")
        print("back to the car. She had briefly watched the pictures with you, but felt")
        print("uneasy, so kept watch instead. This meant she had seen a man approaching her")
        print("and without thinking she'd swung the hammer and hit him on the side of his")
        print("face. She didn't know more, you hadn't taken a look at his face. But somehow")
        print("you knew that this was the man from the picture.")
        print()
        print("[GOOD ENDING]")
        
    elif location == '1' and item_left == '2' and choice == '2':  # House, no hammer, pictures
        print("You and Hannah walk over to the pictures, you shine your flashlight onto")
        print("them to look better. They almost seem to form a timeline. At the start,")
        print("there's a happy, new family. Two parents, hopelessly in love. Then, a small")
        print("child makes its way there. And another. In all the pictures, everyone's")
        print("smiling big. The kids start to grow up, which seems taxing for both of the")
        print("parents. While one kid is still seemingly behaved, the other starts missing")
        print("every now and then. When he appears, he doesn't seem happy. In the last few")
        print("pictures, everyone's an adult, but they're still not all happy to be there.")
        print("The final picture stars only the previously unhappy kid, alone, and smiling")
        print("big. There's blood on his shirt in the picture and his eyes look strange.")
        print("This scares you quite a bit, so you turn to Hannah to signal that you have")
        print("to get out of here, and quick. She saw the same thing as you and is about to")
        print("confirm to leave when you see the man standing behind her, holding a bat. You")
        print("recognise him from the picture, and he's blinded for a second from the")
        print("flashlight. You push past Hannah and try to hit him, though he knocks the")
        print("flashlight out of your hands. After that, the world goes dark.")
        print()
        print("[BAD ENDING]")
        
    elif location == '2' and item_left == '2' and choice == '1':  # Factory, no hammer, conveyor
        print("You and Hannah decide to look over at the conveyor belt, curious as to what")
        print("the factory was used for before it was abandoned. The two of you spot a bunch")
        print("of empty cardboard boxes laying around, a panel with different buttons. Out")
        print("of curiosity, you press a few. You don't expect anything to happen, and for a")
        print("little bit, nothing does. Then you hear whirring above you, softly but")
        print("certainly there. Hannah guides your hand with the flashlight to look up. It's")
        print("just a fan, spinning, making noises due to the little care it's had. It looks")
        print("quite rickety, and the noise does little to reassure you of its stability. Out")
        print("of precaution, Hannah and you walk further away, avoiding standing under any")
        print("fan. The fan you previously were under starts to shake more violently before")
        print("dropping to the floor and breaking apart with a loud bang. Hannah yelps and")
        print("holds onto you as you start to walk away from the area. Maybe going home is a")
        print("better idea.")
        print()
        print("[GOOD ENDING]")
        
    elif location == '2' and item_left == '1' and choice == '1':  # Factory, no flashlight, conveyor
        print("Hannah stumbles over to the conveyor belt, morbidly curious if there's")
        print("anything to discover. Maybe there's some old lamp that still works. She")
        print("quickly finds a panel with different buttons and tries to find icons to")
        print("identify what each button does. The icons have long since faded if they were")
        print("ever there, but she can vaguely make out the colours of each button. She")
        print("presses a seemingly yellow one and you start to hear whirring above you.")
        print("Hannah suggests it might be how old lamps used to work, but then you start to")
        print("hear something that almost sounds like clanking. You figure you should move,")
        print("but can barely see where you're going. The whirring then almost completely")
        print("stops. After another millisecond, all other noise and even the moonlight")
        print("disappear.")
        print()
        print("[BAD ENDING]")
        
    elif location == '2' and item_left == '1' and choice == '2':  # Factory, no flashlight, office
        print("While Hannah wields the hammer, you guide the both of you to the office.")
        print("For some strange reason, you're filled with dread as you approach. It might")
        print("be the whistling that seems to originate from it. There's very little light")
        print("shining into it, so it's pretty much pitch black. Hannah uses the walls to")
        print("wander around. She steps into something wet, but quickly steps back, then")
        print("tries to check what she stepped in. Without light it's almost impossible to")
        print("identify, though it smells metallic. A chuckle, then a laugh sounds from")
        print("above Hannah. In a panic, she swings the hammer around, hitting something in")
        print("the air with a thud. It goes quiet again for a bit, but then you both hear")
        print("the noise of something... ripping, almost. Hannah screams as she feels more")
        print("of the liquid she stood in pouring onto her, and she stumbles back. You")
        print("manage to catch her, but immediately also feel the warm liquid on your arms")
        print("and hands. Both of you start making a run for it, barely able to see more")
        print("than 2 meters in front of you. Hannah had dropped the hammer in the office,")
        print("so you just ran, all the way back to the car, driving all the way home,")
        print("trying not to think too much about what you've done.")
        print()
        print("[NEUTRAL ENDING?]")

if __name__ == "__main__":
    main()