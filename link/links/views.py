from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
def register(request):
    return render(request,"index.html")
def sh(request):
    print("Ok")
    if request.method=='POST':
        try:
            link=request.POST.get('value')
            LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                        'i', 'j', 'k', '1', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                        'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            short_link=''
            import random
            for i in range(8):
                short_link+=random.choice(LOCASE_CHARACTERS)
            f=open('data.txt',"w+")
            f.write(f"{short_link},{link}\n")
            f.close()
            return HttpResponse(short_link)
        except Exception as e:
            print(e)

    else:
        HttpResponse("Soory Its an api")

# Create your views here.
def fetch(request,slug):
    print(slug)
    f= open("data.txt","r")
    scanner=f.read().split("\n")
    print(scanner)
    for i in scanner:
        user=i.split(',')
        if user[0]==slug:
            return redirect(user[1])
    HttpResponse("Invalid Link")