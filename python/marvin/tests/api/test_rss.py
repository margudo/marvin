# !usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Licensed under a 3-clause BSD license.
#
# @Author: Brian Cherinka
# @Date:   2017-05-19 17:47:12
# @Last modified by:   Brian Cherinka
# @Last Modified time: 2017-06-26 14:07:12

from __future__ import print_function, division, absolute_import
from marvin.tests.api.conftest import ApiPage
import pytest


# @pytest.fixture()
# def page(client, request, init_api):
#     blue, endpoint = request.param
#     page = ApiPage(client, 'api', endpoint)
#     yield page


# @pytest.fixture()
# def params(release):
#     return {'release': release}


@pytest.mark.parametrize('page', [('api', 'getRSS')], ids=['getrss'], indirect=True)
class TestGetRss(object):

    @pytest.mark.parametrize('reqtype', [('get'), ('post')])
    def test_plateifu_success(self, galaxy, page, params, reqtype):
        data = {}
        page.load_page(reqtype, page.url.format(name=galaxy.plateifu), params=params)
        page.assert_success(data)

    @pytest.mark.parametrize('reqtype', [('get'), ('post')])
    @pytest.mark.parametrize('name, missing, errmsg', [(None, 'release', 'Missing data for required field.'),
                                                       ('badname', 'name', 'String does not match expected pattern.'),
                                                       ('84', 'name', 'Shorter than minimum length 4.')],
                             ids=['norelease', 'badname', 'shortname'])
    def test_plateifu_failure(self, galaxy, page, reqtype, params, name, missing, errmsg):
        if name is None:
            page.route_no_valid_params(page.url.format(name=galaxy.plateifu), missing, reqtype=reqtype, errmsg=errmsg)
        else:
            page.route_no_valid_params(page.url.format(name=name), missing, reqtype=reqtype, params=params, errmsg=errmsg)


@pytest.mark.parametrize('page', [('api', 'getRSSAllFibers')], ids=['getrssfibers'], indirect=True)
class TestGetRssFibers(object):

    @pytest.mark.parametrize('reqtype', [('get'), ('post')])
    def test_plateifu_success(self, galaxy, page, params, reqtype):
        data = {'wavelength': []}
        page.load_page(reqtype, page.url.format(name=galaxy.plateifu), params=params)
        page.assert_success()
        assert len(page.json['data'].keys()) == 172

    @pytest.mark.parametrize('reqtype', [('get'), ('post')])
    @pytest.mark.parametrize('name, missing, errmsg', [(None, 'release', 'Missing data for required field.'),
                                                       ('badname', 'name', 'String does not match expected pattern.'),
                                                       ('84', 'name', 'Shorter than minimum length 4.')],
                             ids=['norelease', 'badname', 'shortname'])
    def test_plateifu_failure(self, galaxy, page, reqtype, params, name, missing, errmsg):
        if name is None:
            page.route_no_valid_params(page.url.format(name=galaxy.plateifu), missing, reqtype=reqtype, errmsg=errmsg)
        else:
            page.route_no_valid_params(page.url.format(name=name), missing, reqtype=reqtype, params=params, errmsg=errmsg)
