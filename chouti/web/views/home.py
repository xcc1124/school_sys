#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import copy
import datetime
import json

from django.shortcuts import render, HttpResponse
from django.db.models import F

from web import models
from web.forms.home import IndexForm

from backend.utils.pager import Pagination
from backend.utils.response import BaseResponse, StatusCodeEnum
from backend import commons


def index(request):
    """
    抽屉主页
    :param request:
    :return:
    """
    if request.method == 'GET':
        page = request.GET.get('page', 1)

        str_page = "fenye"
        result = []
        return render(request, 'index.html', {'str_page': str_page, 'news_list': result})



