from django.shortcuts import render
from . import module


def math_index(request):
    return render(request, "maths/index.html")


# Binomial Distribution
def binomial_distribution(request):
    return render(request, "maths/binomial/binomial.html")


def calculate_binomial_distribution(request):
    if request.method == 'POST':
        user = module.Binomial(request)
        if user.authenticate_values():
            return render(request, "error/index.html",
                          {"error": "Invalid Input", "message": "Inputed Value is not Integer or Decimal value."})
        ans = user.calculate_binomial()
        return render(request, "maths/binomial/calculate.html", {"r": user.r,
                                                                 "ans": ans
                                                                 })
    return render(request, "error/index.html", {"error": "Bad Request",
                                                "message": "Only POST Method is Allowed."})


# Poisson Distribution
def poisson_distribution(request):
    return render(request, "maths/poisson/poisson.html")


def calculate_poisson_distribution(request):
    if request.method == 'POST':
        user = module.Poisson(request)
        if user.authenticate_values():
            return render(request, "error/index.html",
                          {"error": "Invalid Input", "message": "Inputed Value is not Integer or Decimal value."})
        ans = user.calculate_poisson()
        return render(request, "maths/poisson/calculate.html", {"r": user.r,
                                                                "ans": ans
                                                                })
    return render(request, "error/index.html", {"error": "Bad Request",
                                                "message": "Only POST Method is Allowed."})
