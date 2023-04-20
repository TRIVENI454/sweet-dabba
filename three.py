#INPUT & OUTPUT PRG
pin,cash=input('enter pin&cash:').split(' ')  
print('pin&cash are',pin,cash)
cashvalue=int(cash)
print('type of cash is:',type(cashvalue))
atmamount= 5000
remainingamount= atmamount-cashvalue
print('take your cash',cash,remainingamount,sep='@@@',end='\t')
print('thank you') 