# -*- coding: utf-8 -*-
from negiX import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,data,atexit
from gtts import gTTS
from googletrans import Translator
botStart = time.time()

cl = LINE("dtcrf03pi22u@sute.jp", "Towas0328")
channelToken = cl.getChannelResult()
cl.log("TOKEN:" + str(cl.authToken))
ki = LINE("tqsbm025mvwu@sute.jp", "Towas0328")
channelToken = ki.getChannelResult()
ki.log("TOKEN:" + str(cl.authToken))
ki2 = LINE("u5mkv8t71l8h@sute.jp", "Towas0328")
channelToken = ki.getChannelResult()
ki.log("TOKEN:" + str(cl.authToken))
ki3 = LINE("a4kd3fa1b41w@sute.jp", "Towas0328")
channelToken = ki.getChannelResult()
ki.log("TOKEN:" + str(cl.authToken))

print ("=n=e=g=i=n=i=r=a=n=!=")

oepoll = OEPoll(cl)
oepoll = OEPoll(ki)
oepoll = OEPoll(ki2)
oepoll = OEPoll(ki3)
settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)
clMID = cl.profile.mid
kiMID = ki.profile.mid
ki2MID = ki2.profile.mid
ki3MID = ki3.profile.mid
Bots=[clMID,kiMID,ki2MID,ki3MID]
KAC=[cl,ki,ki2,ki3]
wait2 = {
    'setTime':{}
}
setTime = {}
setTime = wait2['setTime']
master=["ue0edee01d554184c78f2a5d68af285c8","ub266c402af91517033f1d9e1779987b0"]
msg_dict = {}
bl = [""]
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ RESTART ]")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=False, indent=4, ensure_ascii=True)
        return False
    except Exception as error:
        logError(error)
        return False
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ error ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMessageWithMention(to, mid):
    try:
        aa = '{"S":"0","E":"3","M":'+json.dumps(mid)+'}'
        text_ = '@x '
        cl.sendMessage(to, text_, contentMetadata={'MENTION':'{"MENTIONEES":['+aa+']}'}, contentType=0)
    except Exception as error:
        logError(error)
def helpmessage():
    helpMessage = """≪neginiran-botのhelpです≫

～一般権限者向け～
☞テスト…権限を確認します
☞速度…このbotの速度を確認します
☞全保護:オン/オフ…全ての保護をオン/オフにします
☞蹴り保護:オン/オフ…蹴り保護をオン/オフにします
☞名前保護:オン/オフ…グループ名の保護をオン/オフにします
☞招待保護:オン/オフ…招待保護をオン/オフにします
☞URL保護:オン/オフ…URL保護をオン/オフにします

～最高権限者向け～
☞権限追加 @…一般権限を付与します
☞権限削除 @…一般権限を削除します

ねぎえるのLINE@
http://line.me/ti/p/%40ubg0555p"""
    return helpMessage     
def lineBot(op):
    try:
        if op.type == 11:
            if settings["np"] == True:
                G = cl.getGroup(op.param1)
                G.name = gname[op.param1]
                cl.updateGroup(G)
        if op.type == 11:
            if settings["up"] == True:
                G = cl.getGroup(op.param1)
                if G.preventJoinByTicket == False:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in master:
                        pass
                    else:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            G = cl.getGroup(op.param1)
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            G = random.choice(KAC).getGroup(op.param1)
                            G.preventJoinByTicket = True
                            random.choice(KAC).updateGroup(G)
        if op.type == 13:
            if op.param3 in clMID:
                if op.param2 in kiMID:
                    G = ki.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventedJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
            if op.param3 in kiMID:
                if op.param2 in ki2MID:
                    G = ki2.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    ki2.updateGroup(G)
                    Ticket = ki2.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventedJoinByTicket = True
                    ki2.updateGroup(G)
                    Ticket = ki2.reissueGroupTicket(op.param1)
            if op.param3 in ki2MID:
                if op.param2 in ki3MID:
                    G = ki3.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    ki3.updateGroup(G)
                    Ticket = ki3.reissueGroupTicket(op.param1)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventedJoinByTicket = True
                    ki3.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
            if op.param3 in ki3MID:
                if op.param2 in clMID:
                    G =cl.getGroup(op.param1)
                    G.preventedJoinByTicket = False
                    cl.updateGroup(G)
                    Ticket = cl.reissueGroupTicket(op.param1)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventedJoinByTicket = True
                    cl.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            print ("[ JOIN ] : " + str(group.name) + "\n招待: " + contact1.displayName + "\n被邀請的人" + contact2.displayName)
            if clMID in op.param3:
                if op.param2 in master:
                    print ("[ NEWJOIN ]新規招待: " + str(group.name))
                    cl.acceptGroupInvitation(op.param1)
                    G.preventedJoinByTicket = False
                    cl.updateGroup(G)
                    invsend = 0
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki2.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki3.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki3.getGroup(op.param1)
                    G.preventedJoinByTicket = True
                    ki3.updateGroup(G)
                    ki3.reissueGroupTicket(op.param1)
                    cl.sendMessage(op.param1,"ねぎえるの保護botです…\n何かあったら↓へ\n\nhttp://line.me/ti/p/%40ubg0555p")
                else:
                    pass
            if settings["ip"] == True:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                cl.cancelGroupInvitation(op.param1, InviterX)
        if op.type == 19:
            if settings["kp"] == True:
                if op.param2 in Bots:
                    pass
                elif op.param2 in master:
                    pass
                else:
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 19:
            if op.param2 in Bots:
                pass
            if op.param2 in master:
                pass
            else:
                if op.param3 in clMID:
                    if op.param2 not in Bots or master:
                        try:
                            G = ki2.getGroup(op.param1)
                            ki2.kickoutFromGroup(op.param1,[op.param2])
                            G.preventJoinByTicket = False
                            ki2.updateGroup(G)
                            Ticket = ki2.reissueGroupTicket(op.param1)
                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                            time.sleep(0.01)
                            G.preventJoinByTicket = True
                            ki2.updateGroup(G)
                        except:
                            G = random.choice(KAC).getGroup(op.param1)
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            G.preventJoinByTicket = False
                            random.choice(KAC).updateGroup(G)
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                            time.sleep(0.01)
                            G.preventJoinByTicket = True
                            random.choice(KAC).updateGroup(G)
                if op.param3 in kiMID:
                    if op.param2 not in Bots or master:
                        try:
                            G = ki3.getGroup(op.param1)
                            ki3.kickoutFromGroup(op.param1,[op.param2])
                            G.preventJoinByTicket = False
                            ki3.updateGroup(G)
                            Ticket = ki3.reissueGroupTicket(op.param1)
                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                            time.sleep(0.01)
                            G.preventJoinByTicket = True
                            ki3.updateGroup(G)
                        except:
                            G = random.choice(KAC).getGroup(op.param1)
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            G.preventJoinByTicket = False
                            random.choice(KAC).updateGroup(G)
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                            time.sleep(0.01)
                            G.preventJoinByTicket = True
                            random.choice(KAC).updateGroup(G)
                if op.param3 in ki2MID:
                    if op.param2 not in Bots or master:
                        try:
                            G = ki.getGroup(op.param1)
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            G.preventJoinByTicket = False
                            ki.updateGroup(G)
                            Ticket = ki.reissueGroupTicket(op.param1)
                            ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            time.sleep(0.01)
                            G.preventJoinByTicket = True
                            ki.updateGroup(G)
                        except:
                            G = random.choice(KAC).getGroup(op.param1)
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            G.preventJoinByTicket = False
                            random.choice(KAC).updateGroup(G)
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                            ki2.acceptGroupInvitationByTicket(op.param1,Ticket)
                            time.sleep(0.01)
                            G.preventJoinByTicket = True
                            random.choice(KAC).updateGroup(G)
                if op.param3 in ki3MID:
                    if op.param2 not in Bots or master:
                        try:
                            G = cl.getGroup(op.param1)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            G.preventJoinByTicket = False
                            cl.updateGroup(G)
                            Ticket = cl.reissueGroupTicket(op.param1)
                            ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            time.sleep(0.01)
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            G = random.choice(KAC).getGroup(op.param1)
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            G.preventJoinByTicket = False
                            random.choice(KAC).updateGroup(G)
                            Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                            ki3.acceptGroupInvitationByTicket(op.param1,Ticket)
                            time.sleep(0.01)
                            G.preventJoinByTicket = True
                            random.choice(KAC).updateGroup(G)
                if op.param3 in master:
                    if op.param2 not in Bots:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 26 or op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0:
                if sender != cl.profile.mid:
                    to = sender
                else:
                    to = receiver
            else:
                to = receiver
            if sender in master:
                if "権限追加 " in msg.text:
                    if msg.toType == 2:
                        print ("[ KENGEN ] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    settings["admin"][target] = True
                                    cl.sendMessage(to, "追加しました")
                                except:
                                    pass
                elif "権限削除 " in msg.text:
                    if msg.toType == 2:
                        print ("[ DKENGEN ] 成功")
                        key = eval(msg.contentMetadata["MENTION"])
                        key["MENTIONEES"][0]["M"]
                        targets = []
                        for x in key["MENTIONEES"]:
                            targets.append(x["M"])
                        if targets == []:
                            pass
                        else:
                            for target in targets:
                                try:
                                    del settings["admin"][target]
                                    cl.sendMessage(to, "削除しました")
                                except:
                                    pass
            if sender in settings["admin"]:
                if msg.text in ["テスト"]:
                    cl.sendMessage(to, "権限を所持しています")
                if msg.text in ["全保護:オン"]:
                    settings["kp"] = True
                    settings["np"] = True
                    settings["up"] = True
                    settings["ip"] = True
                    cl.sendMessage(to, "全ての保護をオンにしました")
                elif msg.text in ["全保護:オフ"]:
                    settings["kp"] = False
                    settings["np"] = False
                    settings["up"] = False
                    settings["ip"] = False
                    cl.sendMessage(to, "全ての保護をオフにしました")
                elif msg.text in ["蹴り保護:オン"]:
                    settings["kp"] = True
                    cl.sendMessage(to, "蹴り保護をオンにしました")
                elif msg.text in ["蹴り保護:オフ"]:
                    settings["kp"] = False
                    cl.sendMessage(to, "蹴り保護をオフにしました")
                elif msg.text in ["名前保護:オン"]:
                    settings["np"] = True
                    cl.sendMessage(to, "グループ名保護をオンにしました")
                elif msg.text in ["名前保護:オフ"]:
                    settings["np"] = False
                    cl.sendMessage(to, "グループ名保護をオフにしました")
                elif msg.text in ["URL保護:オン"]:
                    settings["up"] = True
                    cl.sendMessage(to, "URL保護をオンにしました")
                elif msg.text in ["URL保護:オフ"]:
                    settings["up"] = False
                    cl.sendMessage(to, "URL保護をオフにしました")
                elif msg.text in ["招待保護:オン"]:
                    settings["ip"] = True
                    cl.sendMessage(to, "招待保護をオンにしました")
                elif msg.text in ["招待保護:オフ"]:
                    settings["ip"] = False
                    cl.sendMessage(to, "招待保護をオフにしました")
                elif msg.text in ["保護:ヘルプ"]:
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                elif msg.text in ["速度"]:
                    start = time.time()
                    cl.sendMessage(msg.to, "うーん、この botの速度は…")
                    elapsed_time = time.time() - start
                    cl.sendMessage(msg.to, "≫%ssecかな〜" % (elapsed_time))
                elif msg.text in ["解雇"]:
                    G =cl.getGroup(msg.to)
                    cl.sendMessage(msg.to,"このbotの事が嫌いでも、ねぎえるの事は嫌いにならないでくっちゃい！\n\nお問い合わせ↓\nhttp://line.me/ti/p/%40ubg0555p")
                    cl.leaveGroup(msg.to)
                    ki.leaveGroup(msg.to)
                    ki2.leaveGroup(msg.to)
                    ki3.leaveGroup(msg.to)

    except Exception as error:
        logError(error)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
