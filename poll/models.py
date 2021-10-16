from django.db import models

class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    
    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count
   
    def option_one_perc(self):
        if self.option_one_count == 0:
            return 0
        else:
            return int((self.option_one_count / self.total()) * 100)
    
    def option_two_perc(self):
        if self.option_two_count == 0:
            return 0
        else:
            return int((self.option_two_count / self.total()) * 100)
    
    def option_three_perc(self):
        if self.option_three_count == 0:
            return 0
        else:
            return int((self.option_three_count / self.total()) * 100)
    
    