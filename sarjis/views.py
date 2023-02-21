from .parsers.parser import Parser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.http import HttpRequest
from rest_framework import status
from .models import Comic
from .serializers import ComicSerializer
import json
import logging

log = logging.getLogger('sarjis')

@csrf_exempt
def getComic(request, id:int):
    comic = Comic.objects.get(id=id)
    if comic.prev_id is not None:
        return JsonResponse(ComicSerializer(comic, many=False).data, safe=False)
    else:
        return Parser.updateLinks(comic.name, comic)

@csrf_exempt
def getLatest(request, name:str):
    comic_json = Parser.parse(name, "/")
    comic_json['name'] = name
#    if(name == 'vw' or name== 'fokit'):
#        return JsonResponse(status=500, 
#        data={"message": "Error test", "status": "false"}, 
#            safe=False)
    try:
        comic_from_db = Comic.objects.get(perm_link = comic_json['perm_link'])
        return JsonResponse(ComicSerializer(comic_from_db, many=False).data, safe=False)
    except KeyError:
        return JsonResponse(data={"message": "Link to comic " + name + " was not found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR, safe=False)
    except Comic.DoesNotExist:
        comic_serializer = ComicSerializer(data = comic_json, many=False)
        if comic_serializer.is_valid():
            comic = comic_serializer.save()            
            return Parser.updateLinks(name, comic)
        else:
            log.error("Invalid serializer for latest comic: " + comic_serializer.errors)
            return JsonResponse(status=status.HTTP_500_INTERNAL_SERVER_ERROR, error = {
                 "message": [{"Invalid serializer for latest comic: ", comic_serializer.errors}]})

@csrf_exempt
def getAllLatest(request):
    fingerpori = getLatest(request, "fingerpori")
    xkcd = getLatest(request, "xkcd")
    smbc = getLatest(request, "smbc")
    vw = getLatest(request, "vw")
    dilbert = getLatest(request, "dilbert")
    # velho = getLatest(request, "velho")
    fokit = getLatest(request, "fokit")
    pbf = getLatest(request, "pbf")
    luonto = getLatest(request, "luonto")

    return JsonResponse([
                         json.loads(fingerpori.content),
                         json.loads(vw.content),
                         json.loads(xkcd.content),
                         json.loads(smbc.content),
                         json.loads(dilbert.content),
                        #  json.loads(velho.content),
                         json.loads(fokit.content),
                         json.loads(pbf.content),
                         json.loads(luonto.content)
                         ], safe=False)

@csrf_exempt
def getNames(request):    
#    resp.set_cookie(key = 'mycookie', value = 'works')
    return JsonResponse(data=Parser.getComicNames(), safe=False)
