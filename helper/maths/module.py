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
    e = 2.718

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
