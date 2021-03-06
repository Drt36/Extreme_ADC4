from django.shortcuts import render
from booking.models import Asset
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.
 
#to display all data stored in the model asset using api
def api_dataall(request):
   asset = Asset.objects.all()
   dict_value = {
      "asset": list(asset.values("asset_Title", "asset_Type", "asset_Price","asset_purpose","asset_Location",))
   }
   return JsonResponse(dict_value)

#to display data using primary key using api
def api_dataspecific(request, pk=None):
       asset = Asset.objects.get(pk=pk)
       return JsonResponse({"asset_Title":asset.asset_Title, "asset_Type":asset.asset_Type, "asset_Price":asset.asset_Price,"asset_purpose":asset.asset_purpose,"asset_Location":asset.asset_Location})

#to add data in the model asset using api
@csrf_exempt
def api_dataadd(request):
   a = Asset()
   if request.method == "POST":
       decoded_data = request.body.decode('utf-8')
       asset_data = json.loads(decoded_data)
       a.asset_Title = asset_data['asset_Title']
       a.asset_Type =asset_data['asset_Type']
       a.asset_Price =asset_data['asset_Price']
       a.asset_purpose=asset_data['asset_purpose']
       a.asset_Location =asset_data['asset_Location']


       a.save()
       return JsonResponse({"message": " Adding New Asset Completed"})
 
   else:
       return JsonResponse({"asset_Title":a.asset_Title, "asset_Type":a.asset_Type,
        "asset_Price":a.asset_Price,"asset_purpose":a.asset_purpose,"asset_Location":a.asset_Location})

#to update data of the model asset using api
@csrf_exempt
def api_dataupdate(request, pk=None):
   asset =Asset.objects.get(pk=pk)
   if request.method == "PUT":
       decoded_data = request.body.decode('utf-8')
       asset_data = json.loads(decoded_data)
       asset.asset_Title = asset_data['asset_Title']
       asset.asset_Type =asset_data['asset_Type']
       asset.asset_Price =asset_data['asset_Price']
       asset.asset_purpose=asset_data['asset_purpose']
       asset.asset_Location =asset_data['asset_Location']
       asset.save()
       return JsonResponse({"message": " Asset Update Completed"})
 
   else:
      return JsonResponse({"asset_Title":asset.asset_Title, "asset_Type":asset.asset_Type,
        "asset_Price":asset.asset_Price,"asset_purpose":asset.asset_purpose,"asset_Location":asset.asset_Location})

#to delete data of the model asset using api
@csrf_exempt
def api_datadelete(request, pk=None):
   asset = Asset.objects.get(pk=pk)
   if request.method == "DELETE":
       asset.delete()
       return JsonResponse({"message": " Asset Delete Completed"})
 
   else:
       return JsonResponse({"asset_Title":asset.asset_Title, "asset_Type":asset.asset_Type,
        "asset_Price":asset.asset_Price,"asset_purpose":asset.asset_purpose,"asset_Location":asset.asset_Location})

#for pagination using api 
def api_assetpagination(request, PAGENO):
   SIZE = 2
   skip = SIZE * (PAGENO-1)
   asset = Asset.objects.all()[skip:PAGENO*SIZE]
   dict = {
       "assets": list(asset.values("asset_Title", "asset_Type", "asset_Price","asset_purpose","asset_Location"))
   }
   return JsonResponse(dict)
