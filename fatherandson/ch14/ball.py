class Ball:

    # publid method
    def bound(self):
        print('hello')

    # private method
    def __bound(self):
        print('haha')


ball = Ball()
ball.color = 'red'
print(ball.color)
# print(ball.size)
print(ball)
ball.bound()
# ball.__bound() #this will raise an ERROR
ball._Ball__bound() # But you can call private method this way!
print(ball.__dict__)