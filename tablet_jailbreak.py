#!/usr/bin/env python
# -*- coding: utf-8 -*-
from naoqi import ALProxy
import qi
import sys

def main(ip="192.168.1.100", port=9559):

    try:
        session = qi.Session()
        session.connect("tcp://{}:{}".format(ip, port))
    except RuntimeError:
        print("Unable to establish a session.")
        sys.exit(1)

    try:
        tabletService = session.service("ALTabletService")

        tabletService._installApk(
            "https://github.com/Michdo93/pepper-tablet-jailbreak/releases/download/ADB.WiFi.Reborn/ADB.WiFi.Reborn_3.2.137_apk-dl.com.apk"
        )
        tabletService._installApk(
            "https://github.com/Michdo93/pepper-tablet-jailbreak/releases/download/KingoRoot/KingoRoot.apk"
        )

        tabletService._stopApk("jp.softbank.custombrowser.MainActivity")
        tabletService._stopApk("jp.softbank.custombrowser")
        tabletService._uninstallApps()
        tabletService._stopApk("jp.softbank.tabletbrowser")
        tabletService._stopApk("jp.softbank.custombrowser.MainActivity")
        tabletService._stopApk("jp.softbank.custombrowser")

    except Exception as e:
        print("ERROR:", e)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        main(ip=sys.argv[1])
    else:
        main()
