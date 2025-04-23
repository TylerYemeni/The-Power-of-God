import os
def send_whatsapp_adb(number, message):
    os.system(f'adb shell am start -a android.intent.action.SENDTO -d sms:{number} --es sms_body "{message}" --ez exit_on_sent true')
    os.system("adb shell input keyevent 22")  # اختيار زر الإرسال
    os.system("adb shell input keyevent 66")  # تنفيذ
