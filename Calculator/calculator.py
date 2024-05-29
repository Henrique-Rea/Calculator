def calculo(x):
  global n1,n2,temp, mult, div, soma, sub;
  if(x==mult or x==div or x==soma or x==sub):
    if(x==mult):
      temp = n1*n2
  else:
    print("Deu ruim")

mult=str("*")
div=str("/")
soma=str("+")
sub=str("-")

n1=int(input("Qual o primeiro valor do calculo matemático?"))
aux=str(input("Qual operacao deseja fazer? Represente pelo simbolo: "))
