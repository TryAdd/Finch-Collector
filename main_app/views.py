from django.shortcuts import render


# Create your views here.
class Finch:
    def __init__(self, name, description, eat, weight):
        self.name = name
        self.description = description
        self.eat = eat
        self.weight = weight

finchs = [
    Finch('Brambling','Similar in size and shape to the chaffinch, the male brambling has a black head in summer, and an orange breast with white belly. In flight it shows a long white rump. Gregarious in winter, it may form flocks of many thousands and often joins with chaffinches. Numbers can vary between winters depending on food supplies. It is a Schedule 1 species.','Seeds in winter; insects in summer.', "24g" ),
    Finch('Bullfinch','The male bullfinch is unmistakable with his bright pinkish-red breast and cheeks, grey back, black cap and tail, and bright white rump. The flash of the rump in flight and piping whistled call are usually the first signs of bullfinches being present. They feed voraciously on the buds of various trees in spring and were once a pest of fruit crops','Seeds, buds and insects (for young).',"21-27g" ),
    Finch('Chaffinch','The chaffinch is one of the most widespread and abundant bird in Britian and Ireland. Its patterned plumage helps it to blend in when feeding on the ground and it becomes most obvious when it flies, revealing a flash of white on the wings and white outer tail feathers. It does not feed openly on bird feeders - it prefers to hop about under the bird table or under the hedge. You ll usually hear chaffinches before you see them, with their loud song and varied calls.','Insects and seeds.',"18-29g" )
]


def home(request):
    
    return render(request, 'base.html')

def about(request):
    return render(request, 'index.html')

def finchs_index(request):
    return render(request, 'finchs/index.html', {'finchs': finchs})