from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Team,Account
from .forms import SignUpForm,LoginForm,TeamForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages



# def home(request):
#     print(request.user.username)
#     team_name = None
#     if request.method == 'GET':
#         # بررسی می‌کنیم که آیا کاربر تیمی دارد یا خیر
#         if request.user.is_authenticated and request.user.team:
#             team_name = request.user.team.name
#         else:
#             team_name = 'None'
    
#     return render(request, 'home.html', {
#         'team': team_name
#     })


from django.shortcuts import render
from .models import Account

def home(request):
    team_name = 'None'
    if request.method == 'GET' and request.user.is_authenticated:
        try:
            # یافتن کاربر مرتبط در مدل Account
            account = Account.objects.get(id=request.user.id)
            if account.team:
                team_name = account.team.name
        except Account.DoesNotExist:
            pass
    
    return render(request, 'home.html', {
        'team': team_name
    })




def signup(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user=form.save(commit=False)
            user.save()
            login(request,user)
            return redirect('team')
        else:
            messages.error(request,'An error occured during registration')

    return render(request,'signup.html',{
    'form':form
  })



def login_account(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # بررسی وجود کاربر
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # لاگین کردن کاربر
                login(request, user)
                return redirect('home')  # نام URL مربوط به صفحه‌ی home
                
            else:
                return redirect('login')
                
        return render(request, 'login.html', {'form': form})


def logout_account(request):
    logout(request)
    return redirect('login')  # im curious to see the url for this veiw




@login_required
def joinoradd_team(request):
    form = TeamForm(request.POST or None)
    account = Account.objects.get(id=request.user.id)
    if request.method == 'GET':
        if hasattr(account, 'team'):
            return redirect('home')
        else:
            return render(request,'team.html',{
                'form':form
            })
    if request.method == 'POST':
        if form.is_valid():
            team_name=form.cleaned_data['name']
            team , created = Team.objects.get_or_create(name=team_name,defaults={'jitsi_url_path':f'http://meet.jit.si/{team_name}'})
            account.team=team
            account.save()
            return redirect('home')
        else:
            return redirect('home')    



            
    



def exit_team(request):
   if request.method == 'GET':
       account = Account.objects.get(id=request.user.id)
       if hasattr(account,'team'):
           account.team=None
           account.save()
           return redirect('home')    
       else:
           return redirect('home')    