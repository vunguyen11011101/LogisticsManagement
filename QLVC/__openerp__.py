# -*- coding: utf-8 -*-
{
    "name": "Quản Lý Vận Chuyển",  # Tên của module
    "version": "1.0",
    "author": "Nguyen&Huy",  # Ví dụ: "FastAndSafe_Team"
    "description": "Module chức năng quản lý vận chuyển hàng hóa",  # Mô tả module
    "website": "",  # Để trống hoặc điền website của bạn
    "category": "General",  # Phân loại module
    "depends": ["base"],  # Khai báo các module liên quan
    "init_xml": [],  # Không cần sử dụng trong OpenERP 7
    "demo_xml": [],  # Không cần sử dụng trong OpenERP 7
    "update_xml": [
        "vanchuyen_view.xml",      # File view (chứa các định nghĩa view)
        "vanchuyen_menu.xml",      # File menu (chứa các định nghĩa menu và action)
    ],
    "installable": True,  # Cho phép cài đặt module
}