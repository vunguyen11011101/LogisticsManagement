# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class KienHang(osv.osv):
    _name = 'kienhang'

    _columns = {
        'makien': fields.char('Mã kiện hàng', size=64, required=True, unique=True),
        'tenkien': fields.char('Tên kiện hàng', size=500, required=True),
        'trongluong': fields.float('Trọng lượng (kg)', required=True),
        'kichthuoc': fields.char('Kích thước (Dài x Rộng x Cao)', size=100),
        'gia_tri': fields.float('Giá trị kiện hàng'),
        'donhang_id': fields.many2one('donhang', 'Đơn hàng', ondelete='cascade'),
        'trangthai': fields.selection([
            ('cho_gui', 'Chờ gửi'),
            ('dang_van_chuyen', 'Đang vận chuyển'),
            ('da_nhan', 'Đã nhận')
        ], 'Trạng thái kiện hàng', required=True),
    }

    _defaults = {
        'trangthai': 'cho_gui',  # Trạng thái mặc định là "Chờ gửi"
    }

    def _check_gia_tri(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            if record.gia_tri < 0:  # Kiểm tra nếu giá trị kiện hàng âm
                return False
        return True
    _constraints = [
        (_check_gia_tri, 'Giá trị kiện hàng không được âm!', ['gia_tri'])
]
KienHang()