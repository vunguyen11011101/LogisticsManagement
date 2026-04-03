# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

class DonHang(osv.osv):
    _name = 'donhang'

    _columns = {
        'madon': fields.char('Mã đơn hàng', size=20, required=True, unique=True),
        'khachgui_id': fields.many2one('khachhang', 'Khách gửi hàng', required=True),
        'khachnhan_id': fields.many2one('khachhang', 'Khách nhận hàng', required=True),
        'doitacgiaohang_id': fields.many2one('doitacgiaohang', 'Đối tác giao hàng'),
        'ngaygui': fields.date('Ngày gửi hàng', required=True),
        'ngaydukien': fields.date('Ngày dự kiến giao hàng'),
        'tongtrongluong': fields.float('Tổng trọng lượng kiện hàng'),
        'tongchiphi': fields.float('Tổng chi phí vận chuyển'),
        'trangthai': fields.selection([
            ('moi', 'Mới tạo'),
            ('dang_xu_ly', 'Đang xử lý'),
            ('dang_van_chuyen', 'Đang vận chuyển'),
            ('hoan_thanh', 'Hoàn thành'),
            ('huy', 'Hủy')
        ], 'Trạng thái đơn hàng', required=True),
        'kienhang_ids': fields.one2many('kienhang', 'donhang_id', 'Danh sách kiện hàng'),
    }

    # Sử dụng trường 'madon' để hiển thị
    def name_get(self, cr, uid, ids, context=None):
        result = []
        for record in self.browse(cr, uid, ids, context=context):
            name = record.madon 
            result.append((record.id, name))
        return result
    
    # tổng chi phí không được âm
    def _check_tongchiphi(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            if record.tongchiphi < 0:  # Kiểm tra nếu tổng chi phí âm
                return False
        return True

    def _check_ngaygui_ngaydukien(self, cr, uid, ids, context=None):
        for record in self.browse(cr, uid, ids, context=context):
            if record.ngaygui and record.ngaydukien and record.ngaygui > record.ngaydukien:
                return False
        return True    
    
    
    _constraints = [
        (_check_ngaygui_ngaydukien, 'Ngày gửi phải nhỏ hơn hoặc bằng ngày dự kiến!', ['ngaygui', 'ngaydukien']),
        (_check_tongchiphi, 'Tổng chi phí không được âm!', ['tongchiphi'])
    ]

DonHang()