#-- Libraries and dependencies used:
sys
time
pygame, including pygame.sprite and pygame.font
(cx_Freeze used for creating executable)



#-- Installation / Execution
Run with Python:
1. Install pygame
2. Run alien_invasion.py in Python terminal

Run without Python:
1. Open build/exe.win-amd64-3.11/alien_invasion.exe


#-- What I learned
This was a great project! I learned so much Python, in particular how to start piecing together the little bits and pieces into a large project. I feel so much more comfortable with classes and functions now. I had so much fun working with pygame that I actually ordered a book called "Invent Your Own Computer Games with Python" by Al Sweigart in order to continue developing with pygame.

I attempted some customization in a sandbox copy of the alien_invasion folder. I had it in my head that I could start adding some power ups to be had, but it proved much more difficult than I thought it might be and I didn't succeed. I thought about a power up that would alter the settings for the bullet to increase its size and/or speed, or to triplicate the bullet. I also considered a power up that would create bullets that plowed through all aliens in path, instead of stopping after one collision. Perhaps after I finish working through the new book I bought I'll be able to customize some more.

The one piece of customization I did include was creating an executable file so I could send the game to people who don't have Python and a development environment installed. It took me a couple hours to troubleshoot it and get it right, but as of this writing the .exe file is working correctly and I'm so excited that it worked. I feel confident that I can convert projects into executables going forward.

The most important thing I learned with this project is the absolute necessity for version control. I was about 2/3 of the way through the project when something broke. I backtracked for about an hour or two trying to figure out where the break happened, and I just couldn't find it. I had to start over. When I started over I added git to my routine and pushed to github regularly in case a break happened again. I will never work on a large project with git again. I learned my lesson. (https://github.com/ashleyrreiss/csc121)