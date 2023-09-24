from django.shortcuts import render

# Create your views here. asdsasd
def main(request):
    data={"titulo":"hola"}
    return render(request,'templateAPP1/index.html',data)


def producto(request):
    data={"titulo":"Electronica","imagen":"chancho.jpg",
          "imagen2":"level 5.png","imagen3":"level 5.png"}
    return render(request,'templateAPP1/producto.html',data)
def producto2(request):
    data={"titulo":"Juguete","imagen":"level 5.png",
          "imagen2":"chancho.jpg","imagen3":"level 5.png"}
    return render(request,'templateAPP1/producto.html',data)
def producto3(request):
    data={"titulo":"Ropa","imagen":"level 5.png",
          "imagen2":"level 5.png","imagen3":"chancho.jpg"}
    return render(request,'templateAPP1/producto.html',data)
               
            
