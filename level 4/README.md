<h1> Level 4 Part 1 <h1>
Distract the Guards
===================

The time for the mass escape has come, and you need to distract the guards so
that the bunny prisoners can make it out! Unfortunately for you, they're
watching the bunnies closely. Fortunately, this means they haven't realized yet
that the space station is about to explode due to the destruction of the
LAMBCHOP doomsday device. Also fortunately, all that time you spent working as
first a minion and then a henchman means that you know the guards are fond of
bananas. And gambling. And thumb wrestling.

The guards, being bored, readily accept your suggestion to play the Banana
Games.

You will set up simultaneous thumb wrestling matches. In each match, two guards
will pair off to thumb wrestle. The guard with fewer bananas will bet all their
bananas, and the other guard will match the bet. The winner will receive all of
the bet bananas. You don't pair off guards with the same number of bananas (you
will see why, shortly). You know enough guard psychology to know that the one
who has more bananas always gets over-confident and loses. Once a match begins,
the pair of guards will continue to thumb wrestle and exchange bananas, until
both of them have the same number of bananas. Once that happens, both of them
will lose interest and go back to guarding the prisoners, and you don't want
THAT to happen!

For example, if the two guards that were paired started with 3 and 5 bananas,
after the first round of thumb wrestling they will have 6 and 2 (the one with 3
bananas wins and gets 3 bananas from the loser). After the second round, they
will have 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they
stop and get back to guarding.

How is all this useful to distract the guards? Notice that if the guards had
started with 1 and 4 bananas, then they keep thumb wrestling! 1, 4 -> 2, 3 -> 4,
1 -> 3, 2 -> 1, 4 and so on.

Now your plan is clear. You must pair up the guards in such a way that the
maximum number of guards go into an infinite thumb wrestling loop!

Write a function answer(banana_list) which, given a list of positive integers
depicting the amount of bananas the each guard starts with, returns the fewest
possible number of guards that will be left to watch the prisoners. Element i of
the list will be the number of bananas that guard i (counting from 0) starts
with.

The number of guards will be at least 1 and not more than 100, and the number of
bananas each guard starts with will be a positive integer no more than
1073741823 (i.e. 2^30 -1). Some of them stockpile a LOT of bananas.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) banana_list = [1, 1]
Output:
    (int) 2

Inputs:
    (int list) banana_list = [1, 7, 3, 21, 13, 19]
Output:
    (int) 0
  
  
  
<h1> Level 4 Part 2 <h1>
  '''
Uh-oh -- you've been cornered by one of Commander Lambdas elite bunny trainers! Fortunately, you grabbed a beam weapon
from an abandoned storeroom while you were running through the station, so you have a chance to fight your way out.
But the beam weapon is potentially dangerous to you as well as to the bunny trainers: its beams reflect off walls,
meaning you'll have to be very careful where you shoot to avoid bouncing a shot toward yourself!
Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage. You also know
that if a beam hits a corner, it will bounce back in exactly the same direction. And of course, if the beam hits either
you or the bunny trainer, it will stop immediately (albeit painfully).
Write a function solution(dimensions, your_position, trainer_position, distance) that gives an array of 2 integers of
the width and height of the room, an array of 2 integers of your x and y coordinates in the room, an array of 2 integers
of the trainer's x and y coordinates in the room, and returns an integer of the number of distinct directions that you
can fire to hit the elite trainer, given the maximum distance that the beam can travel.
The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and the elite trainer are both positioned
on the integer lattice at different distinct positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim].
Finally, the maximum distance that the beam can travel before becoming harmless will be given as an
integer 1 < distance <= 10000.
For example, if you and the elite trainer were positioned in a room with dimensions [3, 2], your_position [1, 1],
trainer_position [2, 1], and a maximum shot distance of 4, you could shoot in seven different directions to hit
the elite trainer (given as vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2].
As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at bearing [-3, -2] b
ounces off the left wall and then the bottom wall before hitting the elite trainer with a total shot distance of sqrt(13),
and the shot at bearing [1, 2] bounces off just the top wall before hitting the elite trainer with a total shot distance of sqrt(5).
'''
