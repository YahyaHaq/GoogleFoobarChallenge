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


class Boundry:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.upper = None
        self.lower = None
        self.left = None
        self.right = None

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def calculate_line_between_2_points(self,point):
        x1 = self.x
        x2 = point.x
        y1 = self.y
        y2 = point.y
        if x1 == x2:
            m = None
            b = x1
        else:
            m = (y1 - y2) / (x1 - x2)
            b = (x1 * y2 - x2 * y1) / (x1 - x2)
        return Line(m,b)

    def __repr__(self):
        return "({},{})".format(self.x,self.y)


class Line:
    def __init__(self,m,b):
        self.m = m
        self.b = b



    def print_line(self):
        if self.m is None:
            string = "x={}".format(self.b)
        else:
            string = "y = {}x + {}".format(self.m, self.b)
        print(string)

    def reflect_line_from_another_line(self,Line,intersecting_point):
        '''

        :param intersecting_point: the point where the two lines intersect
        :param Line: line upon which incident line touches and upon which it reflects. will get this line from
                find_incident_boundry function
        :return: reflected line cordinates that updates m and c of the object
        '''

        #M3 IS SLOPE OF RESULTING REFLECTED LIGHT
        #M1 IS SLOPE OF OUR LINE
        #M2 IS SLOPE OF SURFACE
        M1 = self.m
        M2 = Line.m
        if M1 is None or M2 is None:
            if M2 is None:
                if M1 == 0:
                    M3 = None
                else:
                    M3 = (M1 ^ 2 - 1) / 2 * M1
            elif M1 is None:
                if M2 == 0:
                    M3 =  None
                else:
                    M3 = (M2 ^ 2 - 1) / 2 * M2
        else:
            M3 = ((2 * M1) + (M2 * pow(M1, 2)) - M2) / (2 * M1 * M2 - pow(M1, 2) + 1)

        if M3 is not None:
            intercept = intersecting_point.y - (M3*intersecting_point.x)
        else:
            intercept = intersecting_point.x


        return (M3,intercept)



    def calculate_point_of_intersection(self,Line):
        '''

        :param Line: the line upon which our line intersects and meets
        :return: an object of the point class where the two lines intersect
        '''
        #y = M1x + B1
        #y = M2x + B2
        M1 = self.m
        M2 = Line.m
        B1 = self.b
        B2 = Line.b
        if M1 is None or M2 is None:
            if M1 is None and M2 is None:
                return None
            elif M1 is None:
                x = B1
                y = M2 * x + B2
            else:
                x = B2
                y = M1 * x + B1
        else:
            x = (B2 - B1) / (M1 - M2)
            y = M1*x + B1
        return Point(x,y)

    def Find_Incident_Boundry(self,incident_tuple,boundary,start=False):
        '''

        :param incident_tuple: the line upon which the line hits or passes through
        :param boundary: an object of class boundry
        :param start: to see if we have started this off or has the line been reflected of the surface or not
        :return: returns a Line object showing the boundry upon which the line hits
        '''
        #if start is True then the incident tuple is on the boundry we want to find
        if start:
            for i in range(4):
                point = self.calculate_point_of_intersection(boundary[i])

    def check_point(self,point):
        '''

        :param point: an object of class point
        :return: True of False depending upon which point lies on the line or not
        '''
        pass

    def multiple_reflections(self,incident_point,number_of_reflections):
        '''

        :param incident_point: the point upon which the line hits
        :param number_of_reflections:
        :return: line equations every time the line is reflected
        '''
        pass



def get_boundry(x_limit,y_limit):
    boundry = []
    boundry.append(Line(0,y_limit))
    boundry.append(Line(0, 0))
    boundry.append(Line(None, 0))
    boundry.append(Line(None, x_limit))
    return boundry



def main():
    p1 = Point(1,1)
    p2 = Point(1.5,2)

    L1 = p1.calculate_line_between_2_points(p2)
    L1.print_line()
    L2 = Line(0,2)
    L2.print_line()
    p3 = L2.calculate_point_of_intersection(L1)
    print(p3)

    L3= L1.reflect_line_from_another_line(L2, p3)
    print(L3)

    x_limit = 3
    y_limit = 2
    boundry = get_boundry(x_limit, y_limit)




if __name__ == '__main__':
    main()
