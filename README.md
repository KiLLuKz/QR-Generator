# QR Generator

QR Generator เป็นโปรแกรมสร้าง QR Code แบบง่าย ทำด้วย **Python** และใช้ **PyWebView** เป็น GUI สามารถสร้างไฟล์ QR เป็นรูปภาพ `.png` และเลือกโฟลเดอร์เก็บไฟล์ได้

---

## ฟีเจอร์หลัก

- สร้าง QR Code จากข้อความหรือ URL  
- เลือกโฟลเดอร์สำหรับเก็บ QR Code  
- แสดงผล QR Code ในหน้า GUI พร้อมข้อความสถานะ  
- เปิดโฟลเดอร์ที่บันทึก QR Code ได้ทันที  
- Build เป็น `.exe` สำหรับ Windows ด้วย **PyInstaller**

---

## เทคโนโลยี

- Python 3.11+  
- PyWebView  
- pyqrcode  
- Tkinter (สำหรับเลือกโฟลเดอร์)  
- base64 / io (สำหรับแปลง QR เป็น Base64 เพื่อแสดงใน GUI)

---

## วิธีติดตั้ง 
1.Downlaod ที่ Releases
