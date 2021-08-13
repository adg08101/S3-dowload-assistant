from datetime import datetime
import time
import psutil
import mouse
import easygui as eg
import subprocess
import keyboard
import os


def main(proc_id=0, rec=0, mode='manual',
         root=r'C:\Users\Owner\Downloads\Telegram Desktop\S3DesktopManager 1.6.3\S3DesktopManager.exe',
         download_path='', txt_file='', sleep_time=10, file_name=''):

    downloaded = {}

    if download_path != '':
        downloaded_dir_content = os.listdir(download_path)
        for d in range(len(downloaded_dir_content)):
            downloaded[downloaded_dir_content[d]] = os.path.getsize(download_path + '\\' + downloaded_dir_content[d])

    if len(downloaded) > 1:
        for key in downloaded:
            file_size = downloaded[key]
            break
        if txt_file != '':
            file = open(txt_file, "r")
            lines = file.readlines()
            for line in lines:
                for key in downloaded:
                    if key in line and downloaded[key] == file_size:
                        lines.remove(line)
            output_file = open(txt_file, "w")
            for line in lines:
                output_file.writelines(line)
            output_file.close()

    if proc_id == 0 and mode != 'text_file':
        for i in range(99999):
            try:
                proc = psutil.Process(i)
                if proc.name() == 'S3DesktopManager.exe':
                    proc_id = i
                    break
            except psutil.NoSuchProcess:
                pass
    else:
        proc = psutil.Process(proc_id)

    time.sleep(sleep_time)

    recv_t = psutil.net_io_counters(pernic=True, nowrap=True)['Wi-Fi'].bytes_recv

    res = 'Online'
    if recv_t - rec < 100000:
        res = 'Fallen'

    print(mode, res, str(((recv_t - rec) / 1024) / sleep_time), str(sleep_time), datetime.now())

    rec = recv_t

    if res == 'Fallen' and mode == 'manual':
        eg.indexbox(msg='Process has fallen',
                    title='S3Download: download has fallen',
                    choices=['Ok'],
                    image='')
    elif res == 'Fallen' and mode == 'auto':
        proc.kill()
        time.sleep(sleep_time + (sleep_time * 0.5))
        subprocess.Popen(root)
        time.sleep(sleep_time)
        keyboard.send('space')
        proc_id = 0
        mouse.move(x=905, y=225, duration=0.5)
        mouse.click()
        keyboard.send('space')
        time.sleep(sleep_time * 2)
    elif res == 'Fallen' and mode == 'auto_tune':
        time.sleep(sleep_time + (sleep_time * 0.5))
        time.sleep(sleep_time)
        mouse.move(x=140, y=280, duration=0.2)
        mouse.right_click()
        mouse.move(x=180, y=540, duration=0.2)
        time.sleep(sleep_time)
        mouse.right_click()
        time.sleep(sleep_time / sleep_time)
        keyboard.send('space')
    elif mode == 'text_file':
        pass

    main(proc_id=proc_id, rec=rec, mode=mode, download_path=download_path, txt_file=txt_file, file_name=file_name)


if __name__ == '__main__':
    s3_list = os.listdir(r'C:\Users\Owner\Desktop\S3\TXT')
    for file in s3_list:
        if 'txt' in file:
            txt_file_name = file
            break
    file = txt_file_name
    path = 'C:\\Users\\Owner\\Desktop\\S3\\' + file.replace('.txt', '')
    txt = 'C:\\Users\\Owner\\Desktop\\S3\\TXT\\' + file

    main(mode='auto_tune', download_path=r'C:\Users\Owner\Desktop\S3\@GPCubanS3 The Forest v1', txt_file=txt,
         file_name=file)
