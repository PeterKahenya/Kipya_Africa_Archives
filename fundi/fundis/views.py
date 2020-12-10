from django.shortcuts import render
from django.views import View
import uuid

class FundiView(View):
    def get(self, request):
        # peer_id=str(uuid.uuid4())
        peer_id="d6617451-9b1e-44a3-a60f-40ff8d4367e6"
        return render(request,"fundi.html",{"peer_id":peer_id},None,None,None)
        
