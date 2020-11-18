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


# Normal Distribution
def normal_distribution(request):
    return render(request, "maths/normal/normal.html")


def calculate_normal_distribution(request):
    if request.method == 'POST':
        user = module.Normal(request)
        if user.authenticate_values():
            return render(request, "error/index.html",
                          {"error": "Invalid Input", "message": "Inputed Value is not Integer or Decimal value."})
        ans = user.calculate_normal()
        if ans:
            if user.limit == 1:
                return render(request, "maths/normal/calculate.html", {"z": round(user.z, 3),
                                                                       "a": round(user.a, 5),
                                                                       "limit": user.limit,
                                                                       "area": round(user.area, 5),
                                                                       })
            return render(request, "maths/normal/calculate.html", {"z1": round(user.z1, 3),
                                                                   "z2": round(user.z2, 3),
                                                                   "a1": round(user.a1, 5),
                                                                   "a2": round(user.a2, 5),
                                                                   "limit": user.limit,
                                                                   "area": round(user.area, 5),
                                                                   })
        return render(request, "error/index.html", {"error": "Not Possible Condition",
                                                    "message": "Lower is Not be +ve if Greater is -ve"})
    return render(request, "error/index.html", {"error": "Bad Request",
                                                "message": "Only POST Method is Allowed."})
