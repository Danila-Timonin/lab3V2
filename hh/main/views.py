from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from .forms import VisitorForm, StoreForm, ProductForm, PurchaseForm, ReviewForm, RegistrationForm
from .models import Visitor, Store, Purchase, Product, Review
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth import login as user_login


def is_men(user):
    return user.groups.filter(name='Менеджеры').exists()


@login_required
def profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'main/profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            # Создание пользователя
            user = User.objects.create_user(username=username, email=email, password=password)

            # Назначение пользователя в соответствующую группу
            if role == 'buyer':
                group = Group.objects.get(name='Покупатели')
            else:
                group = Group.objects.get(name='Менеджеры')
            user.groups.add(group)

            # Вход пользователя после успешной регистрации
            user_login(request, user)

            return redirect('product')
    else:
        form = RegistrationForm()
    return render(request, 'main/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login(request, user)
            return redirect('product')
        else:
            return render(request, 'main/login.html', {'error_message': 'Неправильное имя пользователя или пароль.'})
    return render(request, 'main/login.html')


def exp(request):
    return render(request, 'main/exp.html')


@login_required
@user_passes_test(is_men, login_url='exp')
def index(request):
    visitor = Visitor.objects.all()
    return render(request, 'main/visitor.html', {'visitors': visitor})


@login_required
@user_passes_test(is_men, login_url='exp')
def visitor_create(request):
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VisitorForm()
    return render(request, 'main/visitor_create.html', {'form': form})


@login_required
@user_passes_test(is_men, login_url='exp')
def visitor_update(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        form = VisitorForm(request.POST, instance=visitor)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = VisitorForm(instance=visitor)
    return render(request, 'main/visitor_update.html', {'form': form, 'visitor': visitor})


@login_required
@user_passes_test(is_men, login_url='exp')
def visitor_delete(request, pk):
    visitor = get_object_or_404(Visitor, pk=pk)
    if request.method == 'POST':
        visitor.delete()
        return redirect('home')
    return render(request, 'main/visitor_delete.html', {'visitor': visitor})


@login_required
def store(request):
    store = Store.objects.all()
    return render(request, 'main/store.html', {'store': store})


@login_required
@user_passes_test(is_men, login_url='exp')
def store_create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = StoreForm()
    return render(request, 'main/store_create.html', {'form': form})


@login_required
@user_passes_test(is_men, login_url='exp')
def store_update(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = StoreForm(instance=store)
    return render(request, 'main/store_update.html', {'form': form, 'store': store})


@login_required
@user_passes_test(is_men, login_url='exp')
def store_delete(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        store.delete()
        return redirect('store')
    return render(request, 'main/store_delete.html', {'store': store})


@login_required
def product(request):
    product = Product.objects.all()
    return render(request, 'main/product.html', {'products': product})


@login_required
@user_passes_test(is_men, login_url='exp')
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm()
    return render(request, 'main/product_create.html', {'form': form})


@login_required
@user_passes_test(is_men, login_url='exp')
def product_update(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('store')
    else:
        form = StoreForm(instance=store)
    return render(request, 'main/store_update.html', {'form': form, 'store': store})


@login_required
@user_passes_test(is_men, login_url='exp')
def product_delete(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        store.delete()
        return redirect('store')
    return render(request, 'main/store_delete.html', {'store': store})


@login_required
@user_passes_test(is_men, login_url='exp')
def purchase(request):
    purchase = Purchase.objects.all()
    return render(request, 'main/purchase.html', {'purchase': purchase})


@login_required
@user_passes_test(is_men, login_url='exp')
def purchase_create(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase')
    else:
        form = PurchaseForm()
    return render(request, 'main/purchase_create.html', {'form': form})


@login_required
@user_passes_test(is_men, login_url='exp')
def purchase_update(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            return redirect('purchase')
    else:
        form = PurchaseForm(instance=purchase)
    return render(request, 'main/purchase_update.html', {'form': form})


@login_required
@user_passes_test(is_men, login_url='exp')
def purchase_delete(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    if request.method == 'POST':
        purchase.delete()
        return redirect('purchase')
    return render(request, 'main/purchase_delete.html', {'purchase': purchase})


@login_required
def review(request):
    reviews = Review.objects.all()
    return render(request, 'main/review.html', {'reviews': reviews})


@login_required
@user_passes_test(is_men, login_url='exp')
def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review')
    else:
        form = ReviewForm()
    return render(request, 'main/review_create.html', {'form': form})


@login_required
@user_passes_test(is_men, login_url='exp')
def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'main/review_update.html', {'form': form, 'review': review})


@login_required
@user_passes_test(is_men, login_url='exp')
def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.delete()
        return redirect('review')
    return render(request, 'main/review_delete.html', {'review': review})