from django.shortcuts import render, redirect
import random


# Create your views here.
# this function renders the main html page where the user can enter his guess
def game(request):
    # Generate and store a random number between 1 and 100 in session AND render the home page
    request.session['random_number'] = random.randint(1, 100)
    print(random.randint(1, 100))
    return render(request, 'index.html')

#*****************************************************************
def result(request):
    request.session['random_num'] = random.randint(1, 100)
    context = {
    "random_num" : request.session['random_num']
    }
    print(context) 
    return render(request, 'index.html', context )
#***********************************************************************

def guess_number(request):
    # Get the user's guess from the form submission and store it in session
    guess = int(request.POST.get('guess'))
    request.session['user_guess'] = guess
    return redirect('guess_result')

def guess_result(request):
    # Get the stored random number and user guess from session
    #random_number = request.session.get('random_number')
    random_num = random.randint(1, 100)
    request.session['random_num'] = random_num
    user_guess = request.session.get('user_guess')
    print(random_num)

    # Compare the user's guess with the stored random number
    if user_guess == random_num:
        result = "Congratulations! Your guess was correct."
    #elif user_guess < random_num:
        #result = "Your guess was too low."
    else:
        result = "Your guess was too high."

    # Pass the result to the template to render it
    context = {"result": result}
    return render(request, 'guess_result.html', context)

