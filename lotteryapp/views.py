from django.shortcuts import render


def index(request):
    def gimma_chance(iterations, variants):
        final_chance = 100
        for i in range(iterations):
            final_chance = final_chance / variants
        return final_chance

    c = gimma_chance(2, 4)

    context = {
        'chance': c,
    }
    return render(request, 'lotteryproject/index.html', context)
