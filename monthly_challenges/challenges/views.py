from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Study 1 hour every day",
    "february": "Go to the gym 3 times a week",
    "march": "Learn Django for at least 20 min every day",
    "april": "Stretch and do PT every day",
    "may": "Walk for at least 20 min every day",
    "june": "Study 1 hour every day",
    "july": "Learn Django for at least 20 min every day",
    "august": "Study 1 hour every day",
    "september": "Study 1 hour every day",
    "october": "Study 1 hour every day",
    "november": "Study 1 hour every day",
    "december": "Study 1 hour every day",
}


# Create your views here.


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    print(months)
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    print(redirect_month)
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("this month isn't supported")
