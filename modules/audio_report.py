import os
def send_audio_report(target_email: str):
    os.system(f'echo "بلاغ صوتي حول الرقم المشبوه" | mutt -s "بلاغ عاجل" -a samples/fake_voice.mp3 -- {target_email}')
