import webview
import pyqrcode
import os
import tkinter as tk
from tkinter import filedialog
import subprocess
import platform
import base64
from io import BytesIO

class QRAPI:
    def __init__(self):
        self.last_dir = None  # เก็บ path โฟลเดอร์ล่าสุด

    def generate_qr(self, name, link):
        if not name.strip() or not link.strip():
            empty_img = "data:image/png;base64,"
            webview.windows[0].evaluate_js(f"showQR('{empty_img}', 'กรุณากรอกข้อมูลให้ครบ')")
            return

        # เลือกโฟลเดอร์เก็บไฟล์
        root = tk.Tk()
        root.withdraw()
        directory = filedialog.askdirectory(title="เลือกโฟลเดอร์เก็บ QR Code")
        root.destroy()

        if not directory:
            webview.windows[0].evaluate_js("showQR('placeholder.png', 'ยกเลิกการสร้าง QR')")
            return

        self.last_dir = directory  # เก็บโฟลเดอร์ล่าสุด

        # สร้าง QR และบันทึกไฟล์
        file_name = os.path.join(directory, f"{name}.png")
        qr = pyqrcode.create(link)
        qr.png(file_name, scale=8)

        # แปลง QR เป็น Base64 ส่งให้ WebView
        buffer = BytesIO()
        qr.png(buffer, scale=8)
        img_base64 = base64.b64encode(buffer.getvalue()).decode()
        webview.windows[0].evaluate_js(
            f"showQR('data:image/png;base64,{img_base64}', 'Create {file_name} Finished!')"
        )

        return "Done"

    def open_last_directory(self):
        if not self.last_dir:
            return "No folder available"

        system = platform.system()
        if system == "Windows":
            os.startfile(self.last_dir)
        elif system == "Darwin":  # macOS
            subprocess.Popen(["open", self.last_dir])
        else:  # Linux
            subprocess.Popen(["xdg-open", self.last_dir])

        return "Folder opened"

# สร้างหน้าต่าง
api = QRAPI()
webview.create_window("QR Code Generator", "index.html", js_api=api, width=500, height=600)
webview.start()
