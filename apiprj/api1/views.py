from django.http import HttpResponse
from django.core import serializers
from django.utils.simplejson import dumps
from oauth_service.utils import oauth_required

import modelwrap 

@oauth_required
def articles_show(request):
    board_id = request.GET['board_id']
    article_id = int(request.GET['article_id'])
    article = modelwrap.get_article(board_id, article_id)
    ret = dumps(article, ensure_ascii=False) 
    return HttpResponse(ret)
    
@oauth_required
def users_show(request):
    id = request.GET['user_id']
    user = modelwrap.get_user(id)
    ret = dumps(user, ensure_ascii=False)
    return HttpResponse(ret)
    
@oauth_required
def users_lookup(request):
    id_list = request.GET['user_id'].split(',')
    users = map(modelwrap.get_user, id_list)
    ret = dumps(users, ensure_ascii=False)
    return HttpResponse(ret)
 
def boards_lookup(request):
    board_list = request.GET['board_id'].split(',')
    boards = map(modelwrap.get_board, board_list)
    ret = dumps(boards, ensure_ascii=False)
    return HttpResponse(ret)

@oauth_required
def articles_list(request):
    page = 0
    per_page = 20
    
    # get request parameter 
    board_id = request.GET['board_id']
    if request.GET.has_key('page'):
        page = int(request.GET['page'])
    if request.GET.has_key('per_page'):
        per_page = int(request.GET['per_page'])

    # make json object to return
    ret_item = {'option': {'board_id': board_id,
                           'page': page,
                           'per_page': per_page},
                'articles': modelwrap.get_articles(board_id, page, per_page)}
    ret = dumps(ret_item, ensure_ascii=False)

    return HttpResponse(ret)
