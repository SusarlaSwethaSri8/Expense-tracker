from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from accounts.models import Profile
import calendar
from django.contrib import messages



@login_required
def dashboard(request):
    profile = get_object_or_404(Profile, user=request.user)
    expenses = Expense.objects.filter(user=request.user)

    total = sum(exp.amount for exp in expenses)

    # Monthly breakdown
    monthly_expenses = {}
    for expense in expenses:
        month = expense.date.strftime('%B %Y')
        monthly_expenses[month] = monthly_expenses.get(month, 0) + expense.amount

    # Check if over budget
    if total > profile.budget:
        messages.warning(request, "⚠️ You have exceeded your budget!")

    context = {
        'profile': profile,
        'total': total,
        'monthly_expenses': monthly_expenses
    }
    return render(request, 'dashboard.html', context)

@login_required
def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'edit_expense.html', {'form': form})


@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    if request.method == 'POST':
        expense.delete()
        return redirect('expense_list')
    return render(request, 'delete_confirm.html', {'expense': expense})

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(request, 'expense_list.html', {'expenses': expenses})

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('home')  # Or another page
    else:
        form = ExpenseForm()
    return render(request, 'add_expense.html', {'form': form})

@login_required
def home(request):
    return render(request,'home.html')
