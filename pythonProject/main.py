import easygui
from tqdm import tqdm
import time

text = "please enter password"
title = "Secure login"
fields = ["password"]
default_values = []
password = ['1376']
password_input = easygui.multpasswordbox(text, title, fields, default_values)
if password_input == password:
    easygui.msgbox("access granted")
else:
    easygui.msgbox("wrong password, please restart")
    exit()

for i in tqdm(range(101), desc="Loading…", ascii=False, ncols=75):
    time.sleep(0.01)
log_1 = "hi"
print("Completed.")
title = "Secure file"
choices = ["introduction", "log 1", "log 2", "log 3", "log 4", "log 5", "log 6", "log 7", "log 8", "photos", "send "
                                                                                                             "virus"]
msg = "Please make selection of log"
preselect = None
run = True
callback = None
continue1 = True


def main():
    var = easygui.multchoicebox(msg, title, choices, preselect, callback, run)
    if var == ['introduction']:
        easygui.msgbox("""Introduction: 04/26/1998 Welcome to my log or I guess my memorial, if you are reading this 
        I did not make it back to earth, if I did make it back you would not need to read this but whatever. If you 
        don't know me this is my life. I was born in San Jose California in 1973, I never had a very easy life and my 
        family was always fighting. When my family fought I would escape to the roof and look towards the stars and 
        wonder if there was anything out there. I would dream of one day going to a new world where there is no more 
        fighting and only peace. As I grew up it became increasingly aware to all the people in my life that I was 
        different, at the age of 11 I was at a grade 10 learning level, this got the attention of some very powerful 
        people. When I was 16 I was sitting at home when we had a knock at the door. When I opened the door I was 
        face to face with a smaller woman and two big burly men. She would ask if she could come when I asked why she 
        would tell me that they found something. She would take out a photo of a planet that was dark brown, 
        covered in clouds, and a clear liquid with a dark tint to it. When I would ask what the photos were of, 
        she would tell me they found a planet between Mars and Jupiter where they had detected some sort of life. She 
        would explain to me that they are looking for young minds to help with the exploration of the planet. I would 
        reflect on looking to the stars and dreaming of a planet with only peace and would accept the offer. Over 
        several years I would train and attempt to discover information about the new planet, we would make great 
        strides but would always fall short of any real information. Eventually in 1992 I would be approached 
        privately by the director of the program, he would tell me that because of the lack of information gained our 
        program would be shut down. The program director would tell me we have one last option, to send one of us to 
        space and that he would like me to go…and I accepted. Over the coming months I would train for space 
        exploration as the engineering branch would build the best spacecraft ever made…well for all I know it might 
        not be considering I have had no contact with anyone for years. So in 1994 I would make the worst mistake of 
        my life and leave earth. The ship I was in was completely self-sustaining for years and would convert CO2 
        back to O2, it was made out of non corrosive materials and instead of using thrusters it would use compressed 
        air. This is the point where my logs begin and you can read the rest""")
        ccbox = easygui.ynbox(msg="Would you like to continue", title='Secure choice', choices=["yes", "No"])
        if ccbox == True:
            main()
        else:
            exit()
    elif var == ['log 1']:
        easygui.msgbox("""Log 1: The landing
        05/13/1994
        I have officially landed on this new planet yet to be named. My initial readings of this planets are as follows
        
        Reading 1: There are no Alkaline metals detected near surface level
        
        Reading 2: the planet's atmosphere is made up of N2, not traces of Oxygen
        
        Reading 3: The planet is -63C
        
        Reading 4: The air is mostly made of N2 with insignificant traces of other gasses
        
        As the systems boot up and I am able to get my exploration suit up I can get more information. Stay tune
        """)
        ccbox = easygui.ynbox(msg="Would you like to continue", title='Secure choice', choices=["yes", "No"])
        if ccbox == True:
            main()
        else:
            exit()
    elif var == ['log 2']:
        easygui.msgbox("""Log 2: First steps 05/17/1994 Today I took my first steps on the new planet and have found 
        some very peculiar information. The first one I found was that the gravity of the planet is the same as earth 
        at 9.807 m/s². The gravity means that the planet has the exact same mass as earth. Probably the most 
        important information I found was that the planet is completely covered in liquid Ammonia. It is unclear the 
        importance of the ammonia but if it is as important as I think it could be, it would explain a lot about the 
        planet. """)
        ccbox = easygui.ynbox(msg="Would you like to continue", title='Secure choice', choices=["yes", "No"])
        if ccbox == True:
            main()
        else:
            exit()
    elif var == ['log 3']:
        easygui.msgbox("""Log 3: Ammonia is the Solvent of life and the main constituent of the hydrosphere 
        03/28/1995 I have discovered that liquid ammonia makes up 70 percent of the planet(the exact amount of water 
        on earth). This poses questions about the life we discovered, how do they survive without water? The clouds 
        in the sky seem to never leave and are almost always raining, this is due to the enthalpy of evaporation 
        being only half that of water. Because ammonia being the solvent of life and the main constituent of the 
        hydrosphere water, I believe that the reason that we could not find any Alkali metals are because Ammonia 
        over hundreds of years or even thousands it had dissolved them and through streams of Ammonia and the Ammonia 
        rain it would bring Alkaline metals to the see, that also being why the sea is slightly dark because of the 
        dissolved alkaline metals. The ground is stained with corrosion because of the years of ammonia staining it. 
        Interestingly that means that whatever creature is on this planet will have a very different digestive system 
        then the animals on earth. """)
        ccbox = easygui.ynbox(msg="Would you like to continue", title='Secure choice', choices=["yes", "No"])
        if ccbox == True:
            main()
        else:
            exit()
    elif var == ['log 4']:
        easygui.msgbox("""The planet as we have previously known is in between Jupiter and Mars which keeps its 
        average temperature -63c which allows the Ammonia to stay a liquid instead of gas. The planet is surrounded 
        by large moons which will often block out the sun which freezes the Ocean meaning there is likely little to 
        no fish. The planet because of its mass and gravitational pull rotates around the sun at the same speed as 
        earth but because it is farther away from the sun the time it takes to get around it is much longer which 
        means the seasons are longer. In the ocean the top is frozen over but at the bottom because of the core of 
        the planet heating up the ammonia, it is a liquid. I have found very thick plants, when i pulled them from 
        the ground i discovered that the plants have long roots that burrow down to where the planets core warms the 
        roots more and filtered Ammonia lives in pockets, the ammonia in the pockets have Alkaline metals dissolved 
        in them which give the plants some extra nutrients, the plants when they have enough nutrients will have its 
        roots shrivel to avoid too much ammonia. The thick layers on the planet are hydrophobic which means that it 
        has a nonpolar coating on it, the plants will take the ammonia and along with other nutrients in the ground 
        to make the plant grow big, note that it is like seaweed. It is believed that these plants drop seeds which 
        are carried to the ocean by streams, once it enters the ocean it will get sucked into underwater vents that 
        will trap the seeds in ammonia pockets that are warmer where the seed will begin to grow. Now it's time to 
        establish the regions the planet is split into 3 zones Black zone Green zone Red zone 

        The black zone is the coldest and has the least information about, it is called that because the black zone 
        does not get any sun for years and we believe that one day it might become sunny for only a few hours. In 
        hospitable and no life. We believe that it can get down to -180c which is just before the point the air would 
        freeze 
        
        The Green Zone is the warmest and is along the equator. It stays between -50c to -65c year round and is where 
        any life would live. The green zone has a dark ground and ammonia seas with brownish green foliage, 
        it has large hills that are corroded and dangerous to climb, because it is always raining the ground is 
        almost always muddy. When it is not raining the ground gets dry and bridled. This is where i stay with my ship 
        
        The Red Zone is a mixture of the black zone and the green zone. It gets a good amount of sun and is safe 
        enough to explore but not live, it stays between -75 and -110. Low chance of life. Often covered in ice and 
        snow, with large mountains, the feeling of a great abyss fills this land and it makes me feel almost like 
        it is cursed. 
        
        The planet does not have a consistent moon to reflect light off of so at night one side of the world is pitch 
        black
        
        This world was not what I thought it would be. I want to go home and see my family again
        """)
        ccbox = easygui.ynbox(msg="Would you like to continue", title='Secure choice', choices=["yes", "No"])
        if ccbox == True:
            main()
        else:
            exit()
    elif var == ['log 5']:
        easygui.msgbox("""Log 5: Life 2/04/1996 Allas i have found life, and i'm underwhelmed. The discovery of life 
        were small cretaceous creatures. The crust on the creatures is nonpolar which allows for the ammonia to pour 
        off of it easily, upon cutting it open we discover that their thick skin is also to keep them warm in the 
        cold. They get their food from the plants I found earlier. From cutting the creature open I was able to 
        discover that the mouth and stomach are filled with stronger acid than most creatures on earth which I 
        believe is to neutralize the Ammonia, this is also a sign that they do drink Ammonia. From observations of 
        the creatures they are slow and docile. When a moon blocks out the sun they will burrow to avoid the cold and 
        will hibernate until the sunlight arrives again. The creatures swim in the sea but are not dependent on the 
        ocean it seems. There is no reason to believe that there is anything on the bottom of the ocean because the 
        living conditions are so horrible, there is no salt in the sea which means that the ocean might not stay 
        liquid when in the winter in certain areas. """)
        ccbox = easygui.ynbox(msg="Would you like to continue", title='Secure choice', choices=["yes", "No"])
        if ccbox == True:
            main()
        else:
            exit()
    elif var == ['log 6']:
        easygui.msgbox("""Log 6:Ammonia data sheet
        4/11/1996
        
        
        Ammonia
        Balanced Chemical formula
        NH3
        Molar mass
        17
        polar
        Polar
        Melting point
        -77.3
        Boiling point
        -33.34
        PH level
        11.6
        Density at stp
        681g/l
        3D shape
        Trigonal pyramid
        Density
        
        
        Enthalpy of evaporation
        23.35
        Notes
        The hydrogen bonds are weaker than waters
        Ammonia is corrosive
        Chemicals mix with Ammonia just as good and sometimes better than water
        Can dissolve alkaline metals
        The surface tension is a third of water
        Heat capacity
        80.8 j/mol k""")
        ccbox = easygui.ynbox(msg="Would you like to continue", title='Secure choice', choices=["yes", "No"])
        if ccbox == True:
            main()
        else:
            exit()
    elif var == ['log 7']:
        easygui.msgbox("""Log 7:Research finished(merry christmas) 12/25/1997 Today I have finished my list of 
        information about this land and it is as follows This world is made up of 70% liquid Ammonia, the planet is 
        in between Jupiter and Mars which makes the average temperature -63 in the green zone which allows a liquid 
        ammonia ocean in the green zone. Life on this planet is scarce and beside small cretaceous creatures and 
        microscopic organisms the planet is void of life. Around 20% of the planet is uninhabitable, another 30% is 
        dangerous, and 50% is relatively safe, the atmosphere is composed of Nitrogen with small traces of other 
        gasses. The plants and organisms live off of Ammonia as a solvent, which is done by having stronger acid in 
        their stomach and have hexamine lining their digestive system which stops their organs from corrosion. The 
        Green Zone stays between -50 and -65 and in the Red Zone it is between -75 and -110, in the Black Zone it is 
        unknown but we can assume it is up to -180 because there is no evidence that the nitrogen thins out. There 
        are always clouds in the sky because the Enthalpy of evaporation is quite low and it is most likely raining 
        pure Ammonia. Seasons last from months to years because of its distance from the sun and the rotation speed 
        of the planet. The Gravity of the planet is the same as earth which means that the planet also has the same 
        mass of earth, the air pressure is slightly different than earths would be at -63 but not enough to notice. 
        Much of the world is covered in corrosion from the consistent amount of ammonia and no alkali metals can be 
        detected even close to the surface but can be found closer to the core of the planet. The Alkali metals can 
        be found mixed in with the sea water which keeps it from being a clear liquid. Speaking of the core, 
        it keeps the bottom of the ocean warm which keeps it from freezing. Plants also have roots that can go down 
        very far to get to warmer pockets of Ammonia. It is believed that all the plants take years to leave the 
        ground due to them having to travel so far. We believe that when plants drop seeds they go down rivers into 
        the ocean which will move the seeds through vents in the ocean which plants the seeds in warm Ammonia 
        pockets. Most plants and animals have a non-polar surface to keep ammonia off. In the Black and Red zones it 
        snows when it gets to -110. Sometimes the moons of the planet will block out the sun for days at a time which 
        will freeze the land, during which time the cretaceous creatures will burrow underground to stay warm and it 
        will kill off a large amount of plants. In short the life on this planet was not what we expected and we will 
        not be able to colonize the planet. Merry Christmas to everyone back home I miss you<3 """)
        ccbox = easygui.ynbox(msg="Would you like to continue", title='Secure choice', choices=["yes", "No"])
        if ccbox == True:
            main()
        else:
            exit()
    elif var == ['log 8']:
        easygui.msgbox("""Log 8: No hope 09/15/1998 I have been on this planet for years and my oxygen tanks seem to 
        be failing. HQ has left me in the dark and cut contact once they got all the data. I guess this is it for me, 
        if anyone reads this please send a message to my family and let them know that i found a planet without 
        violence. But most importantly take down the organization that sent me. I have attached a remote virus to 
        destroy their systems and delete all evidence of this planet, as my dying wish is to send the virus. You can 
        find it at the very bottom of the Index """)
        ccbox = easygui.ynbox(msg="Would you like to continue", title='Secure choice', choices=["yes", "No"])
        if ccbox == True:
            main()
        else:
            exit()
    elif var == ['photos']:
        ccbox = easygui.ynbox(msg="Would you like to continue", title='Secure choice', choices=["yes", "No"])
        if ccbox == True:
            main()
        else:
            exit()
    elif var == ['send virus']:
        print("Sending")
        for i in tqdm(range(101), desc="Loading…", ascii=False, ncols=75):
            time.sleep(0.01)
        print("complete")
        ccbox = easygui.ynbox(msg="Would you like to continue", title='Secure choice', choices=["yes", "No"])
        if ccbox == True:
            main()
        else:
            exit()


main()
