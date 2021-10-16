from django.db import models

# create a class called Poll that will hold all of the data for a poll. 
# this data will then be saved into a database using the models function from django.db
class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    
    # return the total number of votes
    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count

    # return the percentage of votes for option 1
    def option_one_perc(self):
        if self.option_one_count == 0:
            return 0
        else:
            return int((self.option_one_count / self.total()) * 100)
    
    # return the percentage of votes for option 2
    def option_two_perc(self):
        if self.option_two_count == 0:
            return 0
        else:
            return int((self.option_two_count / self.total()) * 100)
    
    # return the percentage of votes for option 3
    def option_three_perc(self):
        if self.option_three_count == 0:
            return 0
        else:
            return int((self.option_three_count / self.total()) * 100)
    
    