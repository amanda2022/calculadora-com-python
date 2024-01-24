def calculadora ():
    num1 = float(input("digite o primeiro numero"));
    num2 = float(input("digite o segundo numero"));
    operacao = input("escolha a operacao: +, -, *, /");
   
    if(operacao == "+"):
  
     soma = num1 + num2;
     print(soma);
 
    elif(operacao == "-"):

     sub = num1 - num2
     print(sub);
 
    elif(operacao == "*"):
    
     mult = num1*num2
     print(mult);
 
    elif(operacao == "/"):
 
        if(num1 != 0):
           div = num1 / num2;
        
    else:
        print("Não é possível dividir por zero");
    print(div)


calculadora();