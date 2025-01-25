# Define characters
define mc = Character("[player_name]", color="#c8ffc8")
define n = Character("Narrator", color="#ffffff")
define ms = Character("Mysterious Stranger", color="#c8c8ff")
define rose = Character("Rose", color="#ffb7c5")
define mr_chen = Character("Mr. Chen", color="#8b4513")
define sarah = Character("Sarah", color="#d8bfd8")

define config.overlay_screens = ["kindness_tracker"]

# Game variables
default kindness_points = 0
default player_name = ""
default quests_completed = {
    "cat_quest": False,
    "garden_quest": False,
    "sarah_quest": False
}

# Tree growth animations and images
image tree_seed = "images/tree_seed.png"
image tree_sprout = "images/tree_sprout.png"
image tree_sapling = "images/tree_sapling.png"
image tree_full = "images/full_tree.png"

image tree_grow1:
    yalign 0.5
    xalign 0.5
    "tree_seed"
    pause 1.5
    "tree_sprout" with Dissolve(3.0)

image tree_grow2:
    "tree_sprout"
    pause 0.5
    "tree_sapling" with Dissolve(1.0)

image tree_grow3:
    "tree_sapling"
    pause 0.5
    "tree_full" with Dissolve(1.0)

label menu_to_day1:
    scene black with dissolve
    show text "Day 1" with dissolve
    pause 2.0
    hide text with dissolve
    jump day1_morning

label day1_to_day2:
    scene black with dissolve
    show text "Day 2" with dissolve
    pause 2.0
    hide text with dissolve
    jump day2_morning

label day2_to_day3:
    scene black with dissolve
    show text "Day 3" with dissolve
    pause 2.0
    hide text with dissolve
    jump day3_morning

label start:
    scene bg menu
    python:
        player_name = renpy.input("What is your name?", length=32)
        player_name = player_name.strip()
        if not player_name:
            player_name = "Player"
    
    jump menu_to_day1

label day1_morning:
    scene bg bedroom
    
    n "The warm sunlight filters through the curtains, gently waking you up. Today marks the start of your new chapter in this little community."
    
    menu:
        "How do you feel about your new start?"
        
        "Excited about the possibilities":
            $ kindness_points += 5
            mc "I can't wait to see what opportunities this place holds!"
            
        "Nervous but hopeful":
            $ kindness_points += 3
            mc "It's a bit scary, but something about this place feels right."
            
        "Uncertain":
            mc "I wonder if moving here was the right choice..."
    
    n "Step outside and explore the neighborhood."
    
    jump day1_community_board

label day1_community_board:
    scene bg community_board
   
    n "You spot a wooden community board under a large oak tree."

    menu:
        "What catches your attention?"
       
        "Missing Cat Poster" if not quests_completed["cat_quest"]:
            $ kindness_points += 5
            jump cat_search
           
        "Garden Help Needed" if not quests_completed["garden_quest"]: 
            $ kindness_points += 5
            jump garden_cleanup_quest
           
        "New Mom Needs Help" if not quests_completed["sarah_quest"]:
            $ kindness_points += 5
            jump sarah_help_quest
           
        "Keep walking":
            $ kindness_points -= 2
            jump day1_night


label cat_search_quest:
    $ olive_found = True
    call maze_game
    
    rose "Oh thank goodness! You found Olive!"
    
    menu:
        "How do you respond?"
        
        "Happy to help":
            $ kindness_points += 5
            mc "It was my pleasure. Everyone needs help sometimes."
            
        "Accept the reward":
            mc "Those cookies look delicious, thank you!"
            
    jump day1_night

label garden_cleanup_quest:
    $ garden_helped = True
    call garden_minigame
    
    mr_chen "You have good hands for this work."
    
    menu:
        "Your response?"
        
        "Ask to learn more":
            $ kindness_points += 5
            mc "Could you teach me about gardening?"
            
        "Modest acceptance":
            $ kindness_points += 3
            mc "Thank you, I enjoyed helping."
            
    jump day1_night

label day1_night:
    scene bg bedroom_night
    
    n "The moonlight streams through your window."
    
    if quests_completed["cat_quest"]:
        n "You think about Olive's happy reunion with Rose."
    if quests_completed["garden_quest"]:
        n "Your hands still smell of earth from the garden."

    menu:
        "Write in your journal about:"
        
        "The connections you made":
            $ kindness_points += 5
            mc "Small acts of kindness really do matter..."
            
        "Your personal growth":
            $ kindness_points += 3
            mc "I'm starting to find my place here."
            
        "Just sleep":
            mc "Time to rest..."

    if  10 < kindness_points > 20:
        scene bg menu with dissolve
        n "The seed in your garden begins to glow..."
        show tree_grow1 with dissolve
        pause 4.0
        n "A small sprout emerges, pulsing with gentle light."

    if  20 < kindness_points > 30:
        scene bg menu with dissolve
        n "The sprout glows brighter..."
        show tree_grow2 with dissolve
        pause 4.0
        n "It's growing stronger, just like your community bonds."
        
    if kindness_points >= 30:
        scene bg menu with dissolve
        n "The tree reaches its full splendor..."
        show tree_grow3 with dissolve
        pause 4.0
        n "A beacon of kindness for the whole community."
    
    jump day1_to_day2

label day2_morning:
    scene bg bedroom
   
    n "Morning sunlight streams through your window."
   
    menu:
        n "Choose your daily affirmation:"
       
        "I am capable of creating positive change":
            $ kindness_points += 5
            mc "Yesterday showed me even small actions ripple outward."
           
        "I am enough just as I am":
            $ kindness_points += 5
            mc "I don't need to prove anything. Being here is enough."
           
        "I am open to new possibilities":
            $ kindness_points += 5
            mc "Each day brings new chances to connect."
           
        "Skip affirmation":
            mc "Let's just get started..."

    jump day2_community_board

label day2_community_board:
    scene bg community_board
   
    n "You spot a wooden community board under a large oak tree."

    menu:
        "What catches your attention?"
       
        "Missing Cat Poster" if not quests_completed["cat_quest"]:
            $ kindness_points += 5
            jump maze_game
           
        "Garden Help Needed" if not quests_completed["garden_quest"]: 
            $ kindness_points += 5
            jump garden_cleanup_quest
           
        "New Mom Needs Help" if not quests_completed["sarah_quest"]:
            $ kindness_points += 5
            jump sarah_help_quest

        "Keep walking":
            $ kindness_points -= 2
            jump day2_night

label day2_night:
    scene bg bedroom_night
   
    if quests_completed["garden_quest"]:
        n "Your hands still carry the garden's earthen scent."
       
    menu:
        "Evening reflection:"
       
        "Write in journal":
            $ kindness_points += 5
            mc "Each connection makes this place feel more like home."
           
        "Water the glowing seed":
            $ kindness_points += 4
            mc "It seems to pulse stronger each day."
           
        "Call family":
            $ kindness_points += 3
            mc "I should share these experiences with loved ones."
           
        "Sleep early":
            mc "Tomorrow brings new opportunities."
    
    if  10 < kindness_points > 20:
        scene bg menu with dissolve
        n "The seed in your garden begins to glow..."
        show tree_grow1 with dissolve
        pause 4.0
        n "A small sprout emerges, pulsing with gentle light."

    if  20 < kindness_points > 30:
        scene bg menu with dissolve
        n "The sprout glows brighter..."
        show tree_grow2 with dissolve
        pause 4.0
        n "It's growing stronger, just like your community bonds."

    if kindness_points >= 30:
        scene bg menu with dissolve
        n "The tree reaches its full splendor..."
        show tree_grow3 with dissolve
        pause 4.0
        n "A beacon of kindness for the whole community."

    jump day2_to_day3

label day3_morning:
    scene bg bedroom
   
    menu:
        n "Your final morning affirmation:"
       
        "I bring light wherever I go":
            $ kindness_points += 5
            mc "Like the glowing tree, every act of kindness spreads light."
           
        "My community grows stronger through caring":
            $ kindness_points += 5
            mc "We're all connected, growing together."
           
        "I am connected to those around me":
            $ kindness_points += 5
            mc "This place truly feels like home now."
           
        "Skip affirmation":
            mc "Time to face the day."

    jump day3_community_board

label day3_community_board:
    scene bg community_board
   
    n "The community board has some new requests..."

    menu:
        "What will you do today?"
       
        "Missing Cat Poster" if not quests_completed["cat_quest"]:
            $ kindness_points += 5
            jump maze_game
           
        "Garden Help Needed" if not quests_completed["garden_quest"]:
            $ kindness_points += 5
            jump garden_cleanup_quest
           
        "Help Sarah" if not quests_completed["sarah_quest"]:
            $ kindness_points += 5
            jump sarah_help_quest
   
    jump day3_night

label day3_night:
    scene bg bedroom_night
   
    n "Your final evening in our story arrives."
   
    menu:
        "Final reflection:"
       
        "Write in journal":
            $ kindness_points += 5
            mc "These past days have changed me..."

        "Visit the glowing tree":
            $ kindness_points += 5
            mc "It's grown so much, just like my connections here."
           
        "Thank your neighbors":
            $ kindness_points += 5
            mc "Everyone has made me feel so welcome."

    if  10 < kindness_points > 20:
        scene bg menu with dissolve
        n "The seed in your garden begins to glow..."
        show tree_grow1 with dissolve
        pause 4.0
        n "A small sprout emerges, pulsing with gentle light."

    if  20 < kindness_points > 30:
        scene bg menu with dissolve
        n "The sprout glows brighter..."
        show tree_grow2 with dissolve
        pause 4.0
        n "It's growing stronger, just like your community bonds."
        
    if kindness_points >= 30:
        scene bg menu with dissolve
        n "The tree reaches its full splendor..."
        show tree_grow3 with dissolve
        pause 4.0
        n "A beacon of kindness for the whole community."

    jump game_end

label game_end:
    if kindness_points >= 50:
        "Your kindness has transformed the community!"
    elif kindness_points >= 30:
        "You've made a positive impact on your neighbors."
    else:
        "There's always room to grow..."
        
    return