from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction

# This function will render the home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        pk = request.POST['account']  # if the form is submitted, retrieve which account the user wants to view
        return balance(request, pk)  # call balance function to render that account's balance sheet
    content = {'form': form}
    return render(request, 'checkbook/index.html', content)

# this function will render the create new account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)  # retrieve account form
    # checks if request method is POST
    if request.method == 'POST':
        if form.is_valid():  # check to see if submitted form is valid, if so, saves form
            form.save()  # saves new account
            return redirect('index')  # returns user to home page
    content = {'form': form}  # saves content to the template as a dictionary
    # adds content of form to page
    return render(request, 'checkbook/CreateNewAccount.html', content)

# this function will render the balance page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk) # retrieve requested account by pk
    transactions = Transaction.Transactions.filter(account=pk) # retrieve all of account's transactions
    current_total = account.initial_deposit # create account total variable, starting with initial deposit value
    table_contents = {} # creates a dictionary into which transaction info will be placed
    for t in transactions:
        if t.type == 'Deposit':
            current_total += t.amount
            table_contents.update({t: current_total})
        else:
            current_total -= t.amount
            table_contents.update({t: current_total})
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)

# this function will render the transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pk = request.POST['account']
            form.save()
            return balance(request, pk)
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
