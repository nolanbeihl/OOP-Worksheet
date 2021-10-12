

class AlarmClock:
    def __init__(self,user_time,user_alarm):
        self.time = user_time
        self.alarm = user_alarm
        self.set = True

    def set_alarm(self):
        user_pref = input('Would you like to set the alarm?: ')
        if user_pref == 'yes':
            print('The alarm is set for ' + self.alarm)
        else:
            self.set = False
            print('The alarm is turned off')
    
    def change_time(self):
        user_pref = input('What time would you like to set the time for?: ')
        self.time = user_pref
        print('The time has now been set for ' + self.time)
    
