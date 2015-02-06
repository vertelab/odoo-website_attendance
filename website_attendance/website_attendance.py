# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution, third party addon
#    Copyright (C) 2004-2015 Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from openerp import models, fields, api, _
from openerp.exceptions import except_orm, Warning, RedirectWarning
from openerp import http
from openerp.http import request

class website_hello_world(http.Controller):
    @http.route(['/signin/<string:clicked>', '/signin'], type='http', auth="user", website=True)
    def hello(self, clicked=False):
        cr, uid, context, pool = request.cr, request.uid, request.context, request.registry
        if clicked:
            pool.get('hr.employee').attendance_action_change(cr, uid, uid, context)
        employee = pool.get('hr.employee').browse(cr, uid, uid, context)
        ctx = {
            'signed_in': employee.state == 'present',
            'last': employee.last_sign                  #TODO: justera tiden till rätt tidszon
            }
        return request.render('website_attendance.hello_world', ctx)
