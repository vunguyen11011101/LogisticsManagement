# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class DoiTacGiaoHang(osv.osv):
    _name = 'doitacgiaohang'

    _columns = {
        'name': fields.char('Tên đối tác giao hàng', size=200, required=True),
        'sdt': fields.char('Số điện thoại liên hệ', size=15, required=True),
        'email': fields.char('Email', size=200),
        'diachi': fields.text('Địa chỉ công ty', required=True),
        'ghichu': fields.text('Ghi chú thêm'),
    }

DoiTacGiaoHang()