class Human(object):
    name = 'wwj'
    love = 'wqy'

    def say(self,speed):
        print speed

wangweijia = Human()
wangweijia.say('wqy')
wangweijia.love = '123'
print wangweijia.love
print wangweijia.name
