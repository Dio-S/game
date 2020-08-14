import time
import random
playerhp = int(15)
mercenaryhp = int(15)
archerhp = int(15)
playerpunch = int(5)
playersword = int(7)
playerinfinity = int(999)
playerkick = random.randint (2, 8)
time.sleep(2)
print ('What is your name?')
Name = input()
print (str('Welcome, ') + (Name))
print ("Welcome to this adventure. Your best friend has been taken by an evil creature underground. It's YOUR job to rescue him!")
time.sleep(3)
print ('You Jump into the hole to find the evil creature. However, there is a mercenary blocking your way.')
time.sleep(4)
print (str('Battle! ') + (Name) + (' vs MERCENARY'))
time.sleep(2)
print ('Punch always does 5 damage. Kick can do anywhere between 2 and 8 damage. Choose wisely!')
time.sleep(2)
#Creating loop here
while mercenaryhp > 0 and playerhp > 0:
    playerkick = random.randint (2, 8)
    mercenaryattack = random.randint (2, 6)
    print (Name, 'has', playerhp, 'HP and MERCERNARY has', mercenaryhp, 'HP')
    time.sleep(2)
    print ('Type one of the following moves')
    time.sleep(1)
    move = input('Punch, Kick: ')
    if move.upper() == 'KICK' or 'PUNCH' or 'INFINITY' :
        if move.upper() == 'KICK':
            print ('You chose', move,'.', 'you did', playerkick, 'damage!'  )
            print ('MERCENARY has', mercenaryhp-playerkick, 'HP remaining')
            mercenaryhp = mercenaryhp-playerkick
            time.sleep(1)
        if move.upper() == 'PUNCH':
            print ('You chose', move,'.', 'you did', playerpunch, 'damage!'  )
            print ('MERCENARY has', mercenaryhp-playerpunch, 'HP remaining')
            mercenaryhp = mercenaryhp-playerpunch
            time.sleep(1)
        if move.upper() == 'INFINITY':
            print ('You chose', move,'.', 'you did', playerinfinity, 'damage!'  )
            print ('MERCENARY has', mercenaryhp-playerinfinity, 'HP remaining')
            mercenaryhp = mercenaryhp-playerinfinity
            time.sleep(1)
    if mercenaryhp > 0:
        print ('Mercenary Attacks!!', mercenaryattack, 'Damage to', Name)
        playerhp = playerhp-mercenaryattack
        time.sleep(1)
    if mercenaryhp < 1:
        print ('Congratulations', Name, ', you have defeated MERCENARY!')
        time.sleep(1)
        print ('Mercenary dropped wooden sword. Wooden sword is now an optional attack.')
    if playerhp < 1:
        print ('Sorry', Name, ', you have been defeated by MERCENARY!')
        time.sleep(2)
        print('Wow, you died already? That sucks. You cannot continue now, so good luck in the afterlife.')
        time.sleep(4)
        exit()
time.sleep(3)
print('Wow, you beat that big tough dude already? You must be very skilled. But, now there is an archer coming your way.')
time.sleep(4)
print ('Battle!', Name, 'vs ARCHER')
time.sleep(1)
print ('Punch always does 5 damage. Kick can do anywhere between 2 and 8 damage. Sword does 7 damage, but you get hit with 1 damage as recoil. Choose wisely!')
time.sleep(3)
playerhp = int(15)
while archerhp > 0 and playerhp > 0:
    playerkick = random.randint (2, 8)
    archerattack = random.randint (5,7)
    print (Name, 'has', playerhp, 'HP and ARCHER has', archerhp, 'HP')
    time.sleep(2)
    print ('Type one of the following moves')
    time.sleep(1)
    move = input('Punch, Kick, Sword: ')
    if move.upper() == 'KICK' or 'PUNCH' or 'SWORD' :
        if move.upper() == 'KICK':
            print ('You chose', move,'.', 'you did', playerkick, 'damage!'  )
            print ('ARCHER has', archerhp-playerkick, 'HP remaining')
            archerhp = archerhp-playerkick
            time.sleep(1)
        if move.upper() == 'PUNCH':
            print ('You chose', move,'.', 'you did', playerpunch, 'damage!'  )
            print ('ARCHER has', archerhp-playerpunch, 'HP remaining')
            archerhp = archerhp-playerpunch
            time.sleep(1)
        if move.upper() == 'SWORD':
            print ('You chose', move,'.', 'you did', playersword, 'damage!'  )
            print ('ARCHER has', archerhp-playersword, 'HP remaining')
            archerhp = archerhp-playersword
            playerhp = playerhp-1
            print ('You have taken 1 HP damage recoil. You have', playerhp, ' HP remaining.')
            time.sleep(1)
        if move.upper() == 'INFINITY':
            print ('You chose', move,'.', 'you did', playerinfinity, 'damage!'  )
            print ('ARCHER has', archerhp-playerinfinity, 'HP remaining')
            archerhp = archerhp-playerinfinity
            time.sleep(1)
    if archerhp > 0:
        print ('Archer Attacks!!', archerattack, 'Damage to', Name)
        playerhp = playerhp-archerattack
        time.sleep(1)
    if archerhp < 1:
        print ('Congratulations', Name, ', you have defeated ARCHER!')
        time.sleep(1)
        print ('Archer dropped Armor. Armor gives you more HP at the beginning of your battles.')
    if playerhp < 1: 
        print ('Sorry', Name, ', you have been defeated by ARCHER!')
        time.sleep(2)
        print('You got killed by the archer? Man, that sucks. You died.')
        time.sleep(3)
        exit()
time.sleep(3)
playerhp = int(18)
print ('Thanks to the Armor, you now have 18 HP. Great Job!')
time.sleep(3)
print("You are now underground, all alone. It doesn't seem you can get back up through the hole, so you keep walking, trying to find your friend.")
time.sleep(2)
print('You hear heavy breathing. It seems to be coming from the right. You walk towards it and...')
time.sleep(2)
print("It's a Prisoner, all chained up to the wall. He says 'Please save me!'")
print (str(Name) + (', will you save him?'))
response1 = input('Yes or No?  ')
if response1.upper() == 'YES' or 'NO' :
    if response1.upper() == 'YES' :
        print("You set the prisoner free. He turns out to be a murder hobo and stabs you with a knife made out of a leg bone. You died.")
        time.sleep(3)
        exit()
    if response1.upper() == 'NO' :
        print('You did not set the prisoner free. Instead, you decide to steal a knife from him.')
time.sleep(2)
print ("You gained the Prisoner's Knife! This has no benefits, It just means you are a jerk that stole from a prisoner.")
time.sleep(3)
print("Someone saw you steal from the prisoner. That's not good.")
time.sleep(3)
print ('"Threat Spotted" The Figure says. Engaging Forceful Euthanasia.')
print (str(Name) + (', Will you run away?'))
response1 = input('Yes or No?  ')
if response1.upper() == 'YES' or 'NO' :
    if response1.upper() == 'YES' :
        print("You Ran Away You catch a glimpse of the Figure. It seems to be a Robot. You Shamelessly run away. Coward.")
    if response1.upper() == 'NO' :
        print('You decided to stay and fight. However, it shoots you in the head with a revolver. You die.')
        time.sleep(3)
        print('Did you die in one hit? Shame. Shame. Shame.')
        time.sleep(3)
        exit()
time.sleep(2)
print('You actually ran away! Wow. Good to see you actually have concern for your life.')
time.sleep(3)
print('You managed to escape. Right now, you are behind a rock.')
time.sleep(2)
print('It seems that the Robot from earlier is shooting at you.')
time.sleep(2)
print('The Robot dropped its revolver.')
response2 = input('Will you grab it? YES or NO?  ')
if response2.upper() == 'YES' or 'NO' :
    if response1.upper() == 'YES' :
        print("You Obtained the revolver. Wow, you got a big boost.")
        revolverdamage = int(10)
    if response1.upper() == 'NO' :
        print('You decide to leave the gun')
        time.sleep(2)
        print('The Robot Grabbed the revolver and shot a hole straight through your arm You died.')
        time.sleep(3)
        ('WOW. I bet this is not your first time dying. I know you will just restart the program. Seeya.')
        time.sleep(3)
        exit()
time.sleep(3)
print('The Revolver is good against flying enemies, but not strong tanks.')
time.sleep(3)
print ('The Robot Challenges you. There is no escape this time.')
time.sleep(3)
robothp = int(19)
while robothp > 0 and playerhp > 0:
    revolverdamage = random.randint(3, 10)
    robotattack = random.randint(6, 9)
    playerkick = random.randint (2, 8)
    print (Name, 'has', playerhp, 'HP and ROBOT has', robothp, 'HP')
    time.sleep(2)
    print ('Type one of the following moves')
    time.sleep(1)
    move = input('Punch, Kick, Sword, Revolver: ')
    if move.upper() == 'KICK' or 'PUNCH' or 'INFINITY' or 'REVOLVER' or 'SWORD' :
        if move.upper() == 'KICK':
            print ('You chose', move,'.', 'you did', playerkick, 'damage!'  )
            print ('Robot has', robothp-playerkick, 'HP remaining')
            robothp = robothp-playerkick
            time.sleep(1)
        if move.upper() == 'PUNCH':
            print ('You chose', move,'.', 'you did', playerpunch, 'damage!'  )
            print ('Robot has', robothp-playerpunch, 'HP remaining')
            robothp = robothp-playerpunch
            time.sleep(1)
        if move.upper() == 'INFINITY':
            print ('You chose', move,'.', 'you did', playerinfinity, 'damage!'  )
            print ('ROBOT has', robothp-playerinfinity, 'HP remaining')
            robothp = robothp-playerinfinity
            time.sleep(1)
        if move.upper() == 'REVOLVER':
            print ('You chose', move,'.', 'you did', revolverdamage, 'damage!'  )
            print ('ROBOT has', robothp-revolverdamage, 'HP remaining')
            robothp = robothp-revolverdamage
            time.sleep(1)
        if move.upper() == 'SWORD':
            print ('You chose', move,'.', 'you did', playersword, 'damage!'  )
            print ('ROBOT has', robothp-playersword, 'HP remaining')
            robothp = robothp-playersword
            time.sleep(1)
        if robothp > 0:
            print ('Robot Attacks!!', robotattack, 'Damage to', Name)
            playerhp = playerhp-robotattack
            time.sleep(1)
    if robothp < 1:
        print ('"Please... Spare... Me..." The Robot says. You blast a hole right through its hard drive.')
        time.sleep(1)
        print ('Robot dropped a name Tag. It says XQ-1764')
    if playerhp < 1:
        print ('Sorry', Name, ', you have been defeated by Robot!')
        time.sleep(2)
        print('Jeez, that robot did not want to give up. He is strong AF. You died, BTW.')
        time.sleep(4)
        exit()
time.sleep(5)
playerhp = 18
robotchance = 0
megainfinity = 99999999999999999999999999999
placemat = 0
print ('The Robot is dead (kinda?). The Robot has a hard outer shell that is still intact, and you can make armor out of it.')
time.sleep(3)
print ('Will you take it? There is a 50% chance the Robot will explode if you touch it, though.')
choice1 = input('Will you Take it? Yes or No?  ')
if choice1.upper() == 'YES' or 'NO' :
    if choice1.upper() == 'YES' :
        robotchance = random.randint(1, 2)
        if robotchance == 1 :
            print ('You took the armor. You got a +4 HP boost.')
            playerhp = 22
            placemat = 1
        if robotchance == 2 :
            print ('You died because the Robot Blew Up. That sucks, bro.')
            time.sleep(2)
            exit()
        
    if choice1.upper() == 'NO' :
        print('You decided to not risk it.')
time.sleep(3)
print ('OK, we are back on track to finding your friend.')
time.sleep(2)
print ('You catch a glimpse of something in the distance. It seems to be the monster that abducted your friend.')
time.sleep(2)
print ('Chase It?')
response1 = input('Yes or No?  ')
if response1.upper() == 'YES' or 'NO' :
    if response1.upper() == 'YES' :
        print("You chased after the monster.")
    if response1.upper() == 'NO' :
        print('You did not chase after the monster. It got away, and now you commit suicide.')
        time.sleep(3)
        exit()
time.sleep(2)
print ("'HELP ME!' Your friend calls out to you. Before you can think, the monster tries to abduct you, too!")
time.sleep(3)
monsterhp = 21
while monsterhp > 0 and playerhp > 0:
    revolverdamage = random.randint(4, 8)
    monsterattack = random.randint(7, 8)
    playerkick = random.randint (2, 8)
    print (Name, 'has', playerhp, 'HP and MONSTER has', monsterhp, 'HP')
    time.sleep(2)
    print ('Type one of the following moves')
    time.sleep(1)
    move = input('Punch, Kick, Sword, Revolver: ')
    if move.upper() == 'KICK' or 'PUNCH' or 'INFINITY' or 'REVOLVER' or 'SWORD' or 'MEGA INFINITY' :
        if move.upper() == 'KICK':
            print ('You chose', move,'.', 'you did', playerkick, 'damage!'  )
            print ('Monster has', monsterhp-playerkick, 'HP remaining')
            monsterhp = monsterhp-playerkick
            time.sleep(1)
        if move.upper() == 'PUNCH':
            print ('You chose', move,'.', 'you did', playerpunch, 'damage!'  )
            print ('Monster has', monsterhp-playerpunch, 'HP remaining')
            monsterhp = monsterhp-playerpunch
            time.sleep(1)
        if move.upper() == 'INFINITY':
            print ('You chose', move,'.', 'you did', playerinfinity, 'damage!'  )
            print ('Monster has', monsterhp-playerinfinity, 'HP remaining')
            monsterhp = monsterhp-playerinfinity
            time.sleep(1)
        if move.upper() == 'REVOLVER':
            print ('You chose', move,'.', 'you did', revolverdamage, 'damage!'  )
            print ('Monster has', monsterhp-revolverdamage, 'HP remaining')
            monsterhp = monsterhp-revolverdamage
            time.sleep(1)
        if move.upper() == 'SWORD':
            print ('You chose', move,'.', 'you did', playersword, 'damage!'  )
            print ('Monster has', monsterhp-playersword, 'HP remaining')
            robothp = monsterhp-playersword
            time.sleep(1)
        if move.upper() == 'MEGA INFINITY':
            print ('You chose', move,'.', 'you did', megainfinity, 'damage!'  )
            print ('Monster has', monsterhp-megainfinity, 'HP remaining')
            monsterhp = monsterhp-megainfinity
            time.sleep(1)
        if monsterhp > 0:
            print ('Monster Attacks!!', monsterattack, 'Damage to', Name)
            playerhp = playerhp-monsterattack
            time.sleep(1)
    if monsterhp < 1:
        print ('You beat the monster. It seems to be ecaping, though.')
        time.sleep(1)
        print ('The Monster escaped. It dropped a Dark Crystal.')
    if playerhp < 1:
        print ('Sorry', Name, ', you have been defeated by the Monster!')
        time.sleep(2)
        print('The Monster Slaughtered you. It took your friend and got away. You died.')
        time.sleep(4)
        exit()
if placemat == 0 :
    playerhp = 18
if placemat == 1 :
    playerhp = 22
print ('You seem to be at a 3-way fork in the road from here. You can only go one way.')
time.sleep(2)
direction = input('Which way will you go? LEFT, RIGHT, or FORWARD?  ')
if direction.upper() == 'LEFT' or 'RIGHT' or 'FORWARD' :
    if direction.upper() == 'LEFT' :
        print ('You went left. You find yourself in front of a castle. You step inside the castle.')
        time.sleep(2)
        print("'WHO DARES TO ENTER MY CASTLE?!' A loud booming voice asks.")
        time.sleep(2)
        print ("That's not good. That is the king, and you have upset him by entering his castle.")
        time.sleep(2)
        print ("'DO YOU HAVE ANY BUSINESS HERE?' The king asks. He notices the Dark Crystal. 'Where did you get that?' The King asks.")
        time.sleep(3)
        print ("'I will give you A Legendary Sword for that Crystal!' He says. 'It will do massive damage and help you greatly.' The king says.")
        leftchoice = input('Will you give him the crystal? YES or NO?  ')
        if leftchoice.upper == 'YES' or 'NO' :
            if leftchoice.upper() == 'YES' :
                print ('You gave the dark Crystal to the king')
                time.sleep(2)
                print ('"FOOL" the king says. "You thought it would give you the sword? IDIOT. Die."')
                time.sleep(2)
                exit()
            if leftchoice.upper() == 'NO' :
                print ('You are really going to disobey me, the KING?')
                time.sleep(2)
                print ('You got out of there as quick as you could.')
    if direction.upper() == 'RIGHT' :
        

                
