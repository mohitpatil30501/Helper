from math import sqrt, erf


class Binomial:
    def __init__(self, request):
        try:
            self.p = float(request.POST.get('p'))
            self.n = int(request.POST.get('n'))
            self.r = int(request.POST.get('r'))
            self.q = 1 - self.p
        except ValueError:
            self.p = self.q = self.n = self.r = None

    def authenticate_values(self):
        if self.p is None:
            return True
        return False

    @staticmethod
    def factorial(n):
        fact = 1
        while n != 0:
            fact *= n
            n -= 1
        return fact

    @staticmethod
    def combination(n, r):
        return Binomial.factorial(n) / (Binomial.factorial(r) * Binomial.factorial(n - r))

    @staticmethod
    def probability(n, p, q, r):
        return Binomial.combination(n, r) * (p ** r) * (q ** (n - r))

    def calculate_binomial(self):
        answer = [round(Binomial.probability(self.n, self.p, self.q, self.r), 8)]

        sum_numbers = 0
        for r in range(0, self.r + 1):
            sum_numbers += Binomial.probability(self.n, self.p, self.q, r)
        answer.append(round(1 - sum_numbers, 8))

        sum_numbers = 0
        for r in range(0, self.r):
            sum_numbers += Binomial.probability(self.n, self.p, self.q, r)
        answer.append(round(1 - sum_numbers, 8))

        sum_numbers = 0
        for r in range(0, self.r):
            sum_numbers += Binomial.probability(self.n, self.p, self.q, r)
        answer.append(round(sum_numbers, 8))

        sum_numbers = 0
        for r in range(0, self.r + 1):
            sum_numbers += Binomial.probability(self.n, self.p, self.q, r)
        answer.append(round(sum_numbers, 8))

        return answer


class Poisson:
    e = 2.71828

    def __init__(self, request):
        try:
            self.m = int(request.POST.get('m'))
            self.r = int(request.POST.get('r'))
        except ValueError:
            self.m = self.r = None

    def authenticate_values(self):
        if self.m is None:
            return True
        return False

    @staticmethod
    def factorial(n):
        fact = 1
        while n != 0:
            fact *= n
            n -= 1
        return fact

    @staticmethod
    def probability(m, r):
        return ((Poisson.e ** (-m)) * (m ** r)) / Poisson.factorial(r)

    def calculate_poisson(self):
        answer = [round(Poisson.probability(self.m, self.r), 8)]

        sum_numbers = 0
        for r in range(0, self.r + 1):
            sum_numbers += Poisson.probability(self.m, r)
        answer.append(round(1 - sum_numbers, 8))

        sum_numbers = 0
        for r in range(0, self.r):
            sum_numbers += Poisson.probability(self.m, r)
        answer.append(round(1 - sum_numbers, 8))

        sum_numbers = 0
        for r in range(0, self.r):
            sum_numbers += Poisson.probability(self.m, r)
        answer.append(round(sum_numbers, 8))

        sum_numbers = 0
        for r in range(0, self.r + 1):
            sum_numbers += Poisson.probability(self.m, r)
        answer.append(round(sum_numbers, 8))

        return answer


class Normal:
    def __init__(self, request):
        try:
            self.m = float(request.POST.get('m'))
            self.s = float(request.POST.get('s'))
            self.limit = int(request.POST.get('limit'))
            if self.limit == 1:
                self.x = float(request.POST.get('x'))
                self.z = self.a = self.area = None
                self.last_limit = request.POST.get('last')
            else:
                self.x1 = float(request.POST.get('x1'))
                self.x2 = float(request.POST.get('x2'))
                self.z1 = self.z2 = self.a1 = self.a2 = self.area = None
        except ValueError:
            self.m = None

    def authenticate_values(self):
        if self.m is None:
            return True
        return False

    def z_transform(self):
        if self.limit == 1:
            self.z = (self.x - self.m) / self.s
        else:
            self.z1 = (self.x1 - self.m) / self.s
            self.z2 = (self.x2 - self.m) / self.s

    def calculate_normal(self):
        if self.limit == 1:
            self.z_transform()
            self.a = erf((self.x - self.m) / (self.s * sqrt(2))) / 2
            if self.last_limit == "pos-infinity":
                if self.z >= 0:
                    self.area = 0.5 - self.a
                else:
                    self.area = 0.5 + self.a
            else:
                if self.z >= 0:
                    self.area = 0.5 + self.a
                else:
                    self.area = 0.5 - self.a
            return True
        else:
            if self.x1 <= self.x2:
                self.z_transform()
                self.a1 = erf((self.x1 - self.m) / (self.s * sqrt(2))) / 2
                self.a2 = erf((self.x2 - self.m) / (self.s * sqrt(2))) / 2

                self.area = self.a2 - self.a1
                return True
            return False
