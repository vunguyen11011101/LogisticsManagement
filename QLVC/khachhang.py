# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class KhachHang(osv.osv):
    _name = 'khachhang'

    _columns = {
        'name': fields.char('Họ tên khách hàng', size=200, required=True),
        'sdt': fields.char('Số điện thoại', size=15, required=True),
        'email': fields.char('Email', size=200),
        'diachi': fields.text('Địa chỉ khách hàng', required=True),
        'loaikh': fields.selection([
            ('gui', 'Khách gửi'),
            ('nhan', 'Khách nhận')
        ], 'Loại khách hàng', required=True),
        'ghichu': fields.text('Ghi chú thêm'),
    }

KhachHang()