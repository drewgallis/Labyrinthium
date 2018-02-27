# Labyrinthium [multi dimensional maze] - fun idea I thought about
# Creator: Drew Gallis [dmg7152]
# Project Setup Structure:
#       Basic Implementation [text & algorithms]
#       General UI [Using a precreated python lib]
#       Base UI [Our Own Created Game Graphics]
#       Final UI [Good Graphics, Sleek User Interface, and Extra Additional Setup]
######################################################################################################################
import random


class mazeRunner(object):
    def __init__(self, x=0, y=0, z=0):
        self.maze_size = 0
        self.maze = []

def get_axis(self):
    axis = random.randint(0, 2)
    increment = random.randint(0, 1)
    if increment == 0:  # add
        self.maze[self.maze_size] = [axis, increment]
    else:  # subtract
        self.maze[self.maze_size] = [axis, increment]
        self.maze_size += 1


def reset_axis(self):
    self.maze[self.maze_size] = None
    self.maze_size -= 1
    get_axis(self)


def generate_maze(self, maze_size):
    ##defining default variables
    x = 0  # forward and backward
    y = 1  # up and down
    z = 2  # left and right
    positive_move = 1
    negative_move = 0
    first_flag = True
    valid_axis = True

    for i in range(maze_size):
        self.maze.append(None)

    while self.maze_size < maze_size - 1:
        if first_flag:
            first_flag = False
            get_axis(self)
        else:
            get_axis(self)
            last_axis = self.maze[self.maze_size]
            curr_axis = self.maze[self.maze_size - 1]
            while not valid_axis:
                if last_axis == curr_axis:  # the same move cannot happen
                    reset_axis(self)
                    valid_axis = False
                elif last_axis == [x, positive_move] and curr_axis == [x,
                                                                     negative_move]:  # forward and backward moves cannot happen
                    reset_axis(self)
                    valid_axis = False
                elif last_axis == [y, positive_move] and curr_axis == [y,
                                                                     negative_move]:  # up and down moves cannot happen
                    reset_axis(self)
                    valid_axis = False
                else:
                    valid_axis = True

def getUserPath(self):
    forward = ([0,1],"forward")
    backward = ([0,0],"backward")
    left = ([2,1],"left")
    right = ([2,0],"right")
    up = ([1,1], "up")
    down = ([1,0], "down")
    moves_list = [forward,backward,left,right,up,down]
    winning_run = []
    for i in range(self.maze_size):
        curr_move = self.maze[i]
        for i in range(0, 5 ,1):
            if curr_move == moves_list[i][0]:
                winning_run.append(moves_list[i])
    return winning_run

def main():
    self = mazeRunner()

    name = input("What's your name? ")
    print("hello " + name + " welcome to Labryinthium!")
    user_size = int(input("How big would you like your maze to be? "))

    generate_maze(self, user_size)

    for i in range(self.maze_size):
        print(self.maze[i])

    winning_run = getUserPath(self)
    for i in range(self.maze_size):
        print(winning_run[i])

    location = 0

    while(location < user_size - 1):
        movement = input("Which way would you like to go? [forward, backward, up, down, left, right]")
        if winning_run[location][1] == movement:
            location += 1
            print("you move to the next place in the maze")
        else:
            print("wrong move!!")


main()
