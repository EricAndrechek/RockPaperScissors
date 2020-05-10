My high school had a science fair and I wanted to win. There were multiple categories including environmental sciences, chemistry, physics, engineering, and programming. My friend and I love to code, and we decided to challenge ourselves by creating a robotic hand that will use a camera and machine learning to beat you every time in rock paper scissors. We had two weekends to work on it before the science fair.

# The Brains
In order to detect what a person played, we needed an eye so to speak that would capture the play as fast as possible and send the data to the brain. We decided we would set up a green poster on a wooden mount and have a camera face that, almost like a green screen.

![The green poster board setup](https://miro.medium.com/max/1148/0*WdYLDOVwHve-TMMh)

This meant the persons’ hand would have a neon green background making it easy to see the contrast and detect the hand. We mounted a raspberry pi and raspberry pi camera facing the green screen at a specified distance so that exactly all of the green poster was in the frame and nothing else was.

![Picture from the camera](https://miro.medium.com/max/1400/0*SFqMxVRxZxdRAJ25)
We also attached an ultrasonic sensor near the camera so it could start the program if it was tripped.

![Sensors and camera looking at the poster](https://miro.medium.com/max/1148/0*zmVBBxPHpwgTdgHy)

# The Hand
After our raspberry pi found a hand, took a picture and decided what the human played, we needed to have our robot play. We decided to make a robot hand like this:

![Our inspiration for our robot’s hand](https://miro.medium.com/max/1250/0*132PKAwPk2-0NvBB.jpg)
By mounting servo motors on the arm and attaching them to the ends of the strings, the strings will pull when the servos are activated. We built a hand like this and attached it to our raspberry pi. Unfortunately, the raspberry pi does not have a great motor controller and so the servos moved the hand much too slow. We used nanpy to plug our Arduino into our raspberry pi and control it as a slave. This allowed the raspberry pi to control the hand within milliseconds.

![The robot hand controlled with servos](https://miro.medium.com/max/700/1*nYb-jB6XmLqIc4454p5O6g.gif)

# Putting it Together
After attaching our hand with our raspberry pi brain, we added a speaker to allow it to say rock paper scissors as it plays. Here's a working video of it after being all put together:

[![The finished product!](https://i.vimeocdn.com/video/780505125.webp?mw=500&mh=889)](https://player.vimeo.com/video/334271632)

# Results
We won the programming category, engineering category, the most votes overall, and 1st place overall and won a total of $40! It was also posted on Twitter and Reddit racking up views and upvotes there. We even had the [World Rock Paper Scissors Association](https://www.wrpsa.com/) ask us if they could use our video for ‘training purposes’.
