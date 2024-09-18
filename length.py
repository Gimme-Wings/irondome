char1 = "#"
char2 = "="
title = "Mojo really likes his pancakes fresh out of the oven"
length_title = len(title)
print(length_title)
box_length = 52
#this will help in the subtraction it is the 2 blank spaces around the title
title_space = 2
#this determines how much white space between the border and the second char
char2_spacing = ((box_length)-(length_title)-(6)-(4)-title_space)//2
#determine how many characters are used on the title line
box_content = box_length - title_space - 6 -4
# how many extra spaces above the box length would have to be added
if  (length_title - box_content) > 0:
    add_space = length_title - box_content +2
    long_space = 4

else:
    add_space = 0
    long_space = 0
print(add_space)


#no hard coding of exactly how many char1's to print
long_line = char1*(box_length + add_space)
#the border of line 2, 3, and 4 on both side
box_side = (char1*2)
#char2 times 3 so that it can be used later
decor = char2*3
#line 2 and 4 with all the blank space in the middle
char2_spacing = char2_spacing + long_space
short_line = (box_side) + (" "*((box_length + add_space )- 4)) + (box_side)
#for even title because the box length is even it will line up evenly in the center
even_title_line = (box_side) + (" " * (char2_spacing)) + (decor)+ " "+(title) +" "+(decor) + (" " * (char2_spacing + long_space)) +(box_side)
#in the case that the title is odd like the word title for example the right border will be off set by one white space due to
#how the math for the spacing is calculated
odd_title_line = (box_side) + (" " * (char2_spacing + 4)) + (decor)+ " "+(title) +" "+(decor) + (" " * (char2_spacing+1 +long_space)) +(box_side)


#start print of long line
print(long_line)
#print left border then space then right border
print(short_line)
#determine if title is even or odd using a mod function and therefore which function to print to center the title in the box
if length_title %2 ==0:
    print(even_title_line)
else:
    print(odd_title_line)
#as above print left border then space then right border
print(short_line)
#print long line with no stops
print(long_line)
#finish the program
