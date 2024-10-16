from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import stock
from django.contrib.auth.models import User,auth
# from django.contrib.auth import authenticate,login
from django.contrib import messages
from tradingview_ta import TA_Handler, Interval
import tradingview_ta

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    # default = TRADER.objects.create(uname='abc',uemail='xyz',upassword="123")
    # default.save()
    if request.method=='POST':
        username=request.POST['uname']
        email=request.POST['uemail']
        password1=request.POST['upass']
        password2=request.POST['upass1']
    
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('register')
            else:
                user=User.objects.create(username=username,email=email)
                user.set_password(password1)
                user.save()
                return redirect(login) 
        else:
            messages.info(request, 'Password not same')
            return redirect('register')
    else:        
        return render(request,'register.html')
    
    # return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        email=request.POST['uemail']
        password=request.POST['upass']
        
        user = auth.authenticate(username=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request,'Credentials Invalid!')
            return redirect('login')
    else:    
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('login')

def strat(request):
    if request.method=='POST':
        return render(request, 'strat.html')
    else:
        return render(request,'index.html')


def recc(request):
    if request.method=='POST':
        
        stk = request.POST['index']
        mingle = request.POST['single']
        timeInt =request.POST['timeInt']
        stock_cnt=[]
        
        
        bnf=['HDFCBANK','ICICIBANK','KOTAKBANK','AXISBANK','SBIN',
         'INDUSINDBK','BANKBARODA','AUBANK','FEDERALBNK','BANDHANBNK','IDFCFIRSTB','PNB']

        finnif=['HDFCBANK','ICICIBANK','SBIN','BAJFINANCE','AXISBANK','KOTAKBANK','BAJAJFINSV','SBILIFE','PFC','IDFC',
                'LICHSGFIN','SBICARD','MUTHOOTFIN','HDFCAMC','ICICIGI','ICICIPRULI','SHRIRAMFIN','CHOLAFIN','HDFCLIFE','RECLTD']

        nifty = ['ADANIENT','ADANIPORTS','HINDALCO','HEROMOTOCO','INFY','HCLTECH','WIPRO','LT','ONGC','BHARTIARTL',
                'COALINDIA','GRASIM','UPL','M_M','CIPLA','BPCL','TCS','HINDUNILVR','HDFCLIFE','TATACONSUM','BRITANNIA',
                'ASIANPAINT','TECHM','LTIM','ULTRACEMCO','POWERGRID','EICHERMOT','NESTLEIND','MARUTI','KOTAKBANK',
                'SBILIFE','SUNPHARMA','ICICIBANK','APOLLOHOSP','DIVISLAB','RELIANCE','TITAN','DRREDDY','HDFCBANK',
                'ITC','NTPC','BAJFINANCE','SBIN','TATAMOTORS','BAJAJ_AUTO','BAJAJFINSV','TATASTEEL','JSWSTEEL',
                'AXISBANK','INDUSINDBK']
        
        time = [Interval.INTERVAL_1_MINUTE, Interval.INTERVAL_5_MINUTES, Interval.INTERVAL_15_MINUTES, Interval.INTERVAL_30_MINUTES,
                Interval.INTERVAL_1_HOUR, Interval.INTERVAL_2_HOURS, Interval.INTERVAL_4_HOURS, Interval.INTERVAL_1_DAY,
                Interval.INTERVAL_1_WEEK, Interval.INTERVAL_1_MONTH]

        def meh(index):
            cnt=1
            stock_cnt=[]
            for pp in index:
                SYMBOL=TA_Handler(symbol=pp, screener='india',exchange='NSE', interval=INTV)
                output=str(SYMBOL.get_analysis().summary)
                stock_cnt.append(str(cnt)+". "+pp+" "+output)
                cnt+=1
            return stock_cnt

        def single(stock):
            SYMBOL=TA_Handler(symbol=stock,screener='india',exchange='NSE',interval=INTV)
            output=str(SYMBOL.get_analysis().summary)
            stock_cnt=str("1: "+stock+" "+output)
            return stock_cnt

        INTV = time[int(timeInt)]
        indexx=False
        if stk == '1':
            stock_cnt=meh(nifty)
            indexx=True
        elif stk == '2':
            stock_cnt=meh(bnf)
            indexx=True
        elif stk == '3':
            stock_cnt=meh(finnif)
            indexx=True
        else:
            stock_cnt=single(mingle)

        reckon=[]
                
        if(indexx):
            for stockRecc in stock_cnt:
                details= stock()
                deets=stockRecc.split()
                details.sname=deets[1]
                details.srecc=deets[3][1:-2]
                details.sbuy=deets[5][:-1]
                details.ssell=deets[7][:-1]
                details.sneut=deets[9][:-1]
                reckon.append(details)
                
        else:
            details=stock()
            deets=stock_cnt.split()
            details.sname=deets[1]
            details.srecc=deets[3][1:-2]
            details.sbuy=deets[5][:-1]
            details.ssell=deets[7][:-1]
            details.sneut=deets[9][:-1]
            reckon.append(details)
            
        strBuy, strSell, buy, sell, neutral = 0,0,0,0,0
        
        for gg in reckon:
            if gg.srecc == 'STRONG_BUY':
                strBuy+=1
            elif gg.srecc == 'STRONG_SELL':
                strSell+=1
            elif gg.srecc == 'BUY':
                buy+=1
            elif gg.srecc == 'SELL':
                sell+=1
            else:
                neutral+=1

        
        return render(request,'recc.html',{'details':reckon,'strBuy':strBuy,'strSell':strSell,'buy':buy,'sell':sell,'neutral':neutral})
    else:
        return render(request, 'login.html')