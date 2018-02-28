from django.shortcuts import render, HttpResponse
from asset.AssetInfo import Asset_info
import json
from django.contrib.auth.decorators import login_required

asset = Asset_info(**{})
asset_all = asset.info()


def all_hosts(request):
    """所有数据"""
    return HttpResponse(json.dumps(asset_all))


def api(request):
    query_dict = {}
    for key in request.GET:
        if key == '_':
            continue
        query_dict[key] = request.GET.get(key)
    asset = Asset_info(**query_dict)
    asset_list = asset.info()
    # print(asset_list)
    return HttpResponse(json.dumps(asset_list))


@login_required
def index(request):
    return render(request, 'asset/index.html')



