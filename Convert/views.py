from .forms import convertFormLength, convertFormWeight, convertFormTemperature
from django.shortcuts import render, redirect
from .conversion import convert_length, convert_weight, convert_temperature


def ask_page(request):
    result = None
    if request.method == "POST":
        form = convertFormLength(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            first_unit = form.cleaned_data['first_unit']
            second_unit = form.cleaned_data['second_unit']
            print(number)
            print(first_unit)
            print(second_unit)
            print(convert_length(number, first_unit, second_unit))
            result = f'{number}{first_unit} = {convert_length(number, first_unit, second_unit)}{second_unit}'
            return render(request, 'staticfiles/result_page.html', {'result': result})
    else:
        form = convertFormLength()
    context = {
        'form': form,
        'result': result,
    }
    return render(request, "staticfiles/length_page.html", context)


def weigth_page(request):
    result = None
    if request.method == "POST":
        form = convertFormWeight(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            first_unit = form.cleaned_data['first_unit']
            second_unit = form.cleaned_data['second_unit']
            print(number)
            print(first_unit)
            print(second_unit)
            print(convert_weight(number, first_unit, second_unit))
            result = f'{number}{first_unit} = {convert_weight(number, first_unit, second_unit)}{second_unit}'
            return render(request, 'staticfiles/result_page.html', {'result': result})
    else:
        form = convertFormWeight()
    context = {
        'form': form,
        'result': result,
    }
    return render(request, 'staticfiles/weight_page.html', context)

def temperature_page(request):
    result = None
    if request.method == "POST":
        form = convertFormTemperature(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            first_unit = form.cleaned_data['first_unit']
            second_unit = form.cleaned_data['second_unit']
            print(number)
            print(first_unit)
            print(second_unit)
            print(convert_temperature(number, first_unit, second_unit))
            result = f'{number}{first_unit} = {convert_temperature(number, first_unit, second_unit)}{second_unit}'
            return render(request, 'staticfiles/result_page.html', {'result': result})
    else:
        form = convertFormTemperature()
    context = {
        'form': form,
        'result': result,
    }
    return render(request, 'staticfiles/temperature_page.html', context)

def result_page(request):
    return render(request, "staticfiles/result_page.html")

