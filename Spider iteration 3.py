#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name spider is used
spider = trtl.Turtle()

#create spider body
spider.pensize(40)
spider.circle(20)

#configure spider legs
num_legs = 8
leg_size = 90
z = 360 / num_legs
print("z1=", z)
spider.pensize(5)
n = 0

#draw legs
while (n < num_legs):
  spider.goto(0,20)
  spider.setheading(z*n)
  spider.forward(leg_size)
  n = n + 1
  print ("z*n=", z*n)
spider.hideturtle()

wn = trtl.Screen()
wn.mainloop()