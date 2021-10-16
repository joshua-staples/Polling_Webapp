from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from .forms import CreatePollForm
from .models import Poll

# Create your views here.
# create the function that handles the request for the home page
def home(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'poll/home.html', context)

# create the function that handles the request for the create page, this view will need to be POST so that it
# can save the data to the database, and the user doesn't see all of that data, and it cannot be changed in the 
# url bar 
# the form is called and then saved which changes the database values otherwise the empty form is passed into the 
# html as the context of the return
def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {
        'form' : form
    }
    return render(request, 'poll/create.html', context)

# # create the function that handles the request for the vote page takes in the request and the poll_id,
# save the data from the selected form field into the poll class (and database)
def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    
    if request.method == 'POST':
        option = request.POST['poll']
        if option == 'option1':
            poll.option_one_count += 1
        elif option == 'option2':
            poll.option_two_count += 1
        elif option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid Form')
        
        poll.save()
        return redirect('results', poll.id)
    
    context = {
        'poll' : poll
    }
    return render(request, 'poll/vote.html', context)

# create the function that handles the request for the results page
# requires the poll id, in order to return the correct polls results
def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    
    context = {
        'poll' : poll
    }
    return render(request, 'poll/results.html', context)

# create the function that handles the request for the all_results page
# should loop through the entire database and return results data for the 
# entire database
def all_results(request):
    polls = Poll.objects.all()
    
    context = {
        'poll' : polls
    }
    return render(request, 'poll/results.html', context)