#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt6.QtWidgets import QApplication, QWidget
import codecs
import os
from pathlib import Path
import websocket
import threading
import time
import json
import subprocess


app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(True)

BasePath = '/Applications/Walnut.app/Contents/Resources/'
# BasePath = ''  # test


class window1(QWidget):
    def __init__(self):
        super().__init__()
        home_dir = str(Path.home())
        tarname1 = "WalnutAppPath"
        self.fulldir1 = os.path.join(home_dir, tarname1)
        if not os.path.exists(self.fulldir1):
            os.mkdir(self.fulldir1)

        self.initUI()

    def initUI(self):
        tarname2 = "api.txt"
        fulldir2 = os.path.join(self.fulldir1, tarname2)
        if not os.path.exists(fulldir2):
            with open(fulldir2, 'a', encoding='utf-8') as f0:
                f0.write('')
        api = codecs.open(fulldir2, 'r', encoding='utf-8').read()

        if api != '':
            websocket.enableTrace(True)
            ws = websocket.WebSocketApp(api,
                                        on_open=self.on_open,
                                        on_message=self.on_message,
                                        on_error=self.on_error,
                                        on_close=self.on_close)
            ws.run_forever()

    def notify(self, CMD, title, text):
        subprocess.call(['osascript', '-e', CMD, title, text])

    def on_message(self, ws, message):
        message_data = json.loads(message)
        if message_data['type'] == 'heartbeat':
            pass
        else:
            tarname4 = "places.txt"
            fulldir4 = os.path.join(self.fulldir1, tarname4)
            if not os.path.exists(fulldir4):
                with open(fulldir4, 'a', encoding='utf-8') as f0:
                    f0.write('')
            places = codecs.open(fulldir4, 'r', encoding='utf-8').read()
            if '+' in places:
                places_list = places.split('+')
                for i in range(len(places_list)):
                    if places_list[i] in message_data['message']:
                        cmd = """
                            tell application "/Applications/Walnut.app/Contents/Auto/WalnutAlarm.app"
                                activate
                            end tell"""
                        try:
                            subprocess.call(['osascript', '-e', cmd])
                        except Exception as e:
                            pass
            else:
                if places in message_data['message']:
                    cmd = """
                        tell application "/Applications/Walnut.app/Contents/Auto/WalnutAlarm.app"
                            activate
                        end tell"""
                    try:
                        subprocess.call(['osascript', '-e', cmd])
                    except Exception as e:
                        pass

            CMD = '''
                on run argv
                    display notification (item 2 of argv) with title (item 1 of argv)
                end run'''
            self.notify(CMD, "Earthquake happened!",
                        f"Message: {message_data['message']}\nSource: Customized API")
    def on_error(self, ws, error):
        with open(BasePath + 'errorfile.txt', 'w', encoding='utf-8') as f0:
            f0.write(str(error))
        CMD = '''
        	on run argv
        		display notification (item 2 of argv) with title (item 1 of argv)
        	end run'''
        self.notify(CMD, "Walnut: Emergent Earthquake Alarm",
                    f"Error. Please try again.")

    def on_close(self, ws, close_status_code, close_msg):
        CMD = '''
            on run argv
                display notification (item 2 of argv) with title (item 1 of argv)
            end run'''
        self.notify(CMD, "Walnut: Emergent Earthquake Alarm",
                    f"Walnut closed.")

    def on_open(self, ws):
        def run(*args):
            tarname6 = "interval.txt"
            fulldir6 = os.path.join(self.fulldir1, tarname6)
            if not os.path.exists(fulldir6):
                with open(fulldir6, 'a', encoding='utf-8') as f0:
                    f0.write('0')
            interval = codecs.open(fulldir6, 'r', encoding='utf-8').read()
            gap = 2
            if interval != '':
                if interval == '0':
                    gap = 1
                if interval == '1':
                    gap = 2
                if interval == '2':
                    gap = 5
                if interval == '3':
                    gap = 10
            count = 0
            while True:
                count += 1
                time.sleep(gap)
                ws.send("Hello %d" % count)
                if count % 1000 == 0:
                    time.sleep(1)
                    count = 0
            #ws.close()
        thread = threading.Thread(target=run)
        thread.start()


if __name__ == '__main__':
    w1 = window1()
    app.exec()
