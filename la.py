#-*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,data,atexit
from gtts import gTTS
from googletrans import Translator
botStart = time.time()
cl = LINE("reugpsh6ab10@sute.jp", "Towas0328")
cl.log("Auth Token : " + str(cl.authToken))
print ("====Ykino登入成功====")
oepoll = OEPoll(cl)
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
lineSettings = cl.getSettings()
clProfile = cl.getProfile()
clMID = cl.profile.mid
try:
    settings['bot'] = {}
    settings["bot"][clMID] = True
    print ("設置bot清單成功")
except:
    print ("設置bot清單失敗")
myProfile["displayName"] = clProfile.displayName
myProfile["statusMessage"] = clProfile.statusMessage
myProfile["pictureStatus"] = clProfile.pictureStatus
msg_dict = {}
bl = [""]
god = ['ue0edee01d554184c78f2a5d68af285c8']
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ 訊息 ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False    
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def logError(text):
    cl.log("[ 錯誤 ] " + str(text))
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
    helpMessage = """《ねぎにらん無料botのヘルプです》

☞help…このヘルプを表示します
☞mid…あなたのmidを表示します
☞gid…グループのidを表示します
☞speed…速度を表示します
☞グループ作者…グループの作者を確認します
☞既読ポイント設定…既読ポイントを設定します
☞既読ポイント削除…既読ポイントを削除します
☞既読確認…既読をつけた人を確認します(事前に既読ポイントを設定しておく必要があります)
☞歌って…歌います！
☞占って…占います！
☞全蹴り…全蹴りします【ネタ要素含】
☞うんこ…運用時間を表示します
☞ねぎしね…botが退会します

その他
垢情報の共有
投稿情報の共有
送信取り消しの検知
グル色々機能はありますにょ…
無料だから好きなグループに招待して使ってね！"""
    return helpMessage
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            contact = cl.getContact(op.param1)
            print ("[ 5 ] 通知添加好友 名字: " + contact.displayName)
            if settings["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                cl.sendMessage(op.param1, "やっほー{}！ 追加ありがとう！".format(str(contact.displayName)))
                cl.sendMessage(op.param1, "bot購入等のお問い合わせは↓↓↓")
                cl.sendContact(op.param1, "u22db032049b35c0f566a481626daabf8")
                cl.sendMessage(op.param1,"この文章を見た方限定！半bot通常価格3000円(半永久)より500円引きします！スクショをご提示ください！")
        if op.type == 24:
            print ("[ 24 ] 通知離開副本")
            if settings["autoLeave"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 1:
            print ("[1]更新配置文件")
        if op.type == 11:
            group = cl.getGroup(op.param1)
            if op.param1 not in settings["qrprotect"]:
                if op.param2 in settings['admin'] or op.param2 in settings['bot'][op.param1]:
                    pass
                else:
                    gs = cl.getGroup(op.param1)
                    gs.preventJoinByTicket = True
                    cl.updateGroup(gs)
                    invsend = 0
                    #cl.sendMessage(op.param1,cl.getContact(op.param2).displayName + "你沒有權限觸碰網址!")
                    try:
                        kl.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        sb.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            GS = group.creator.mid
            print ("[ 13 ] 通知邀請群組: " + str(group.name) + "\n邀請者: " + contact1.displayName + "\n被邀請者" + contact2.displayName)
            if clMID in op.param3:
                if settings["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1, "ねぎえるの無料botです。\nコマンドリストは｢help｣で表示します。\n半bot購入等のご用命はこちら↓")
                    cl.sendContact(op.param1, "u22db032049b35c0f566a481626daabf8")
                    cl.sendMessage(op.param1,"ねぎにらんbotを友達追加すると半bot割引特典がもらえるかも？？？")
            elif op.param1 not in settings["inviteprotect"]:
                if op.param2 not in settings['admin'] and op.param2 not in settings['bot'][op.param1]:
                    cl.sendMessage(op.param1, "招待保護中です")
                    try:
                        kl.cancelGroupInvitation(op.param1, [op.param3])
                    except:
                        sa.cancelGroupInvitation(op.param1, [op.param3])
                    try:
                        settings['blacklist'][op.param2] = True
                        with open('temp.json', 'w') as fp:
                            json.dump(settings, fp, sort_keys=True, indent=4)
                        cl.sendMessage(op.param1, "対象者をブラリスに追加しました")
                        cl.sendContact(op.param1, op.param2)
                    except:
                        cl.sendMessage(op.param1, "ブラリス追加失敗")
            else:
                if op.param3 in settings['blacklist']:
                    sa.cancelGroupInvitation(op.param1, [op.param3])
                    cl.sendMessage(op.param1, "ブラリスユーザーです")
                    cl.sendContact(op.param1, op.param3)
                elif op.param2 in settings['blacklist']:
                    sa.cancelGroupInvitation(op.param1, [op.param3])
                    cl.sendMessage(op.param1, "ブラリスユーザーです")
                    cl.sendContact(op.param1, op.param3)
        if op.type == 19:
          if op.param3 in settings['admin']:
              kl.kickoutFromGroup(op.param1,[op.param2])
              cl.inviteIntoGroup(op.param1,settings['admin'])
          else:
               pass		
        if op.type == 19:
            contact1 = cl.getContact(op.param2)
            group = cl.getGroup(op.param1)
            contact2 = cl.getContact(op.param3)
            print ("[19]有人把人踢出群組 群組名稱: " + str(group.name) +"\n踢人者: " + contact1.displayName + "\nMid: " + contact1.mid + "\n被踢者" + contact2.displayName + "\nMid:" + contact2.mid )
            if op.param1 not in settings["protect"]:
                if op.param2 in settings['admin'] or op.param2 in settings['bot'][op.param1]:
                    pass
                else:
                    try:
                        kt.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            sb.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                sa.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kl.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                    if op.param3 in settings['bot']:
                        if group.preventedJoinByTicket == True:
                            group.preventedJoinByTicket = False
                        try:
                            ticket = kl.reissueGroupTicket(op.param1)
                            kl.updateGroup(group)
                        except:
                            try:
                                ticket = cl.reissueGroupTicket(op.param1)
                                cl.updateGroup(group)
                            except:
                                try:
                                    ticket = kt.reissueGroupTicket(op.param1)
                                    kt.updateGroup(group)
                                except:
                                    try:
                                        ticket = sb.reissueGroupTicket(op.param1)
                                        sb.updateGroup(group)
                                    except:
                                        ticket = sa.reissueGroupTicket(op.param1)
                                        sa.updateGroup(group)
                        cl.acceptGroupInvitationByTicket(op.param1, ticket)
                        kl.acceptGroupInvitationByTicket(op.param1, ticket)
                        sa.acceptGroupInvitationByTicket(op.param1, ticket)
                        sb.acceptGroupInvitationByTicket(op.param1, ticket)
                        kt.acceptGroupInvitationByTicket(op.param1, ticket)
                        settings["blacklist"][op.param2] = True
                        with open('temp.json', 'w') as fp:
                            json.dump(settings, fp, sort_keys=True, indent=4)
                            cl.sendMessage(op.param1, "ブラリスに追加しました\n" + "MID : " + op.param2)
                            cl.sendContact(op.param1, op.param2)
                        group.preventedJoinByTicket = True
                        sa.updateGroup(group)
        if op.type == 60:
            if op.param2 in settings['blacklist']:
                cl.sendMessage(op.param1, "ブラリスユーザーです")
            else:
                if op.param2 not in settings['bot']:
                    if op.param1 not in settings['wel']:
                        try:
                            arrData = ""
                            text = "%s " %('やぁ')
                            arr = []
                            mention = "@x "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':op.param2}
                            arr.append(arrData)
                            text += mention + 'さん、いらっしゃいませ！\nこのアカウントを友達追加すると半bot割引特典がもらえるかも？？？'
                            cl.sendMessage(op.param1,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    else:
                        cl.sendMessage(op.param1, settings['wel'][op.param1])
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
            if msg._from in settings['blacklist']:
                return
            if msg.contentType == 13:
                if settings["contact"] == True:
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendMessage(msg.to,"[名前]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[ステメ]:\n" + contact.statusMessage + "\n[アイコン]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[ホム画]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.getProfileCoverURL(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                            cl.sendMessage(msg.to,"[名前]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[ステメ]:\n" + contact.statusMessage + "\n[アイコン]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[ホム画]:\n" + str(cu))
            elif msg.contentType == 7:
                stk_id = msg.contentMetadata['STKID']
                stk_ver = msg.contentMetadata['STKVER']
                pkg_id = msg.contentMetadata['STKPKGID']
                number = str(stk_id) + str(pkg_id)
                if sender in settings['limit']:
                    if number in settings['limit'][sender]['stick']:
                        if settings ['limit'][sender]['stick'][number] >= 3:
                            settings ['limit'][sender]['stick']['react'] = False
                        else:
                            settings ['limit'][sender]['stick'][number] += 1
                            settings ['limit'][sender]['stick']['react'] = True
                    else:
                        try:
                            del settings['limit'][sender]['stick']
                        except:
                            pass
                        settings['limit'][sender]['stick'] = {}
                        settings['limit'][sender]['stick'][number] = 1
                        settings['limit'][sender]['stick']['react'] = True
                else:
                    settings['limit'][sender] = {}
                    settings['limit'][sender]['stick'] = {}
                    settings['limit'][sender]['text'] = {}
                    settings['limit'][sender]['stick'][number] = 1
                    settings['limit'][sender]['stick']['react'] = True
                if settings['limit'][sender]['stick']['react'] == False:
                    return
                if to in settings['cc']:
                    command = "->add_sr:" + format(stk_id) + ":" + format(pkg_id) + ":"
                    cl.sendMessage(to, command)
                elif to in settings["checkSticker"]:
                    ret_ = "<<スタンプ情報>>"
                    ret_ += "\n[貼圖ID] : {}".format(stk_id)
                    ret_ += "\n[貼圖包ID] : {}".format(pkg_id)
                    ret_ += "\n[貼圖網址] : line://shop/detail/{}".format(pkg_id)
                    ret_ += "\n[貼圖圖片網址]：https://stickershop.line-scdn.net/stickershop/v1/sticker/{}/ANDROID/sticker.png;compress=true".format(stk_id)
                    ret_ += "\n<<完>>"
                    cl.sendMessage(to, str(ret_))
                    cl.sendImageWithURL(to, path)
                    cl.sendMessage(op.param1,ret_)
                    cl.sendMessage(to, command)
                elif number in settings['sr']:
                    react = settings['sr'][number]
                    cl.sendMessage(to, str(react))
            elif msg.contentType == 16:
                if settings["timeline"] == True:
                    try:
                        msg.contentType = 0
                        f_mid = msg.contentMetadata["postEndUrl"].split("userMid=")
                        s_mid = f_mid[1].split("&")
                        mid = s_mid[0]
                        try:
                            arrData = ""
                            text = "%s " %("[投稿者]\n")
                            arr = []
                            mention = "@x "
                            slen = str(len(text))
                            elen = str(len(text) + len(mention) - 1)
                            arrData = {'S':slen, 'E':elen, 'M':mid}
                            arr.append(arrData)
                            text += mention + "\n[内容]\n " + msg.contentMetadata["text"] + "\n[URL]\n " + msg.contentMetadata["postEndUrl"]
                            cl.sendMessage(msg.to,text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
                        except Exception as error:
                            print(error)
                    except:
                        ret_ = "\n[内容]\n " + msg.contentMetadata["text"]
                        ret_ += "\n[URL]\n " + msg.contentMetadata["postEndUrl"]
                        cl.sendMessage(msg.to, ret_)
            if msg.contentType == 0:
                if text is None:
                    return
                if sender in settings['limit']:
                    if msg.text in settings['limit'][sender]['text']:
                        if settings ['limit'][sender]['text'][msg.text] >= 3:
                            settings ['limit'][sender]['text']['react'] = False
                        else:
                            settings ['limit'][sender]['text'][msg.text] += 1
                            settings ['limit'][sender]['text']['react'] = True
                    else:
                        try:
                            del settings['limit'][sender]['text']
                        except:
                            pass
                        settings['limit'][sender]['text'] = {}
                        settings['limit'][sender]['text'][msg.text] = 1
                        settings['limit'][sender]['text']['react'] = True
                else:
                    settings['limit'][sender] = {}
                    settings['limit'][sender]['stick'] = {}
                    settings['limit'][sender]['text'] = {}
                    settings['limit'][sender]['text'][msg.text] = 1
                    settings['limit'][sender]['text']['react'] = True
                if settings['limit'][sender]['text']['react'] == True:
                    if sender in settings['admin'] or sender in god:
                        if "ブラjック追加" in msg.text:
                            if msg.toType == 2:
                                print ("[Ban] 成功")
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
                                            settings["blacklist"][target] = True
                                            with open('temp.json', 'w') as fp:
                                                json.dump(settings, fp, sort_keys=True, indent=4)
                                                cl.sendMessage(to, "[成功]\nブラリスに追加しました\nmid: " + target)
                                                cl.sendContact(to, target)
                                        except:
                                            pass
                        elif msg.text.lower().startswith("bm"):
                            mid = text.replace("bm ", "")
                            settings["blacklist"][mid] = True
                            with open('temp.json', 'w') as fp:
                                json.dump(settings, fp, sort_keys=True, indent=4)
                                cl.sendMessage(to, "[提示]\n已成功加入黑名單\nMID: " + mid)
                                cl.sendContact(to, mid)
                                cl.sendMessage(mid, "[警告]\n你因為違反yukino使用公約已被列入黑單!!")
                        elif "ブラkック削除" in msg.text:
                            if msg.toType == 2:
                                print ("[UnBan] 成功")
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
                                            del settings["blacklist"][target]
                                            with open('temp.json', 'w') as fp:
                                                json.dump(settings, fp, sort_keys=True, indent=4)
                                                cl.sendMessage(to, "ブラリスから削除しました")
                                        except:
                                            pass
                        elif msg.text.lower().startswith("ubm"):
                                mid = text.replace("ubm ", "")
                                del settings["blacklist"][mid]
                                with open('temp.json', 'w') as fp:
                                        json.dump(settings, fp, sort_keys=True, indent=4)
                                        cl.sendMessage(to, "[成功]\nブラリスから削除しました。\nMID: " + mid)
                                        cl.sendContact(to, mid)
                        elif text.lower() == 'ブラkリス全削除':
                            for mi_d in settings["blacklist"]:
                                settings["blacklist"] = {}
                                cl.sendMessage(to, "ブラリスを全削除しました。")
                        elif msg.text.lower().startswith("fbc:"):
                            bctxt = text.replace("fbc:","")
                            t = cl.getAllContactIds()
                            for manusia in t:
                                cl.sendMessage(manusia,"[好友廣播]\n"+bctxt)
                        elif msg.text.lower().startswith("gbc:"):
                            bctxt = text.replace("gbc:","")
                            n = cl.getGroupIdsJoined()
                            for manusia in n:
                                cl.sendMessage(manusia,"[群組廣播]\n"+bctxt)
                        elif msg.text.lower() == 'rkesetgroup':
                            group = cl.getGroup(to)
                            GS = group.creator.mid
                            cl.sendMessage(to, "[警告]\n開始重新設定群組!!!")
                            try:
                                if to in settings['protect']:
                                    del settings['protect'][to]
                                if to in settings['inviteprotect']:
                                    del settings['inviteprotect'][to]
                                if to in settings['qrprotect']:
                                    del settings['qrprotect'][to]
                                if to in settings['reread']:
                                    del settings['reread'][to]
                                if to in settings['checkSticker']:
                                    del settings['checkSticker'][to]
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                                cl.sendMessage(to, "[警告]\n刪除群組設定成功")
                            except:
                                cl.sendMessage(to, "[ERROR]\n刪除群組設定失敗")
                            try:
                                if to in settings['gm']:
                                    del settings['gm'][to]
                                    with open('temp.json', 'w') as fp:
                                        json.dump(settings, fp, sort_keys=True, indent=4)
                                cl.sendMessage(to, "[警告]\n刪除群組GM成功")
                            except:
                                cl.sendMessage(to, "[ERROR]\n刪除群組GM失敗")
                            cl.sendMessage(to, "[警告]\n開始重新設定群組GM")
                            try:
                                settings['gm'][to] = {}
                                settings['gm'][to][GS] = GS
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                                cl.sendMessage(to, "[警告]\n設定群組GM成功\n群組GM為:")
                                cl.sendContact(to, GS)
                            except:
                                cl.sendMessage(to, "[ERROR]\n設定群組GM失敗")
                            cl.sendMessage(to, "重新設定群組完成如有錯誤請私訊作者!!!")
                    if sender in god:
                        if text.lower() == 'add on':
                            settings["autoAdd"] = True
                            cl.sendMessage(to, "自動で友達追加します")
                        elif text.lower() == 'add off':
                            settings["autoAdd"] = False
                            cl.sendMessage(to, "自動友達追加をオフにしました")
                        elif text.lower() == 'ar on':
                            settings["autoRead"] = True
                            cl.sendMessage(to, "自動已讀已開啟")
                        elif text.lower() == 'ar off':
                            settings["autoRead"] = False
                            cl.sendMessage(to, "自動已讀已關閉")
                        elif text.lower() == 'join on':
                            settings["autoJoin"] = True
                            cl.sendMessage(to, "自動加入群組已開啟")
                        elif text.lower() == 'join off':
                            settings["autoJoin"] = False
                            cl.sendMessage(to, "自動加入群組已關閉")
                        elif text.lower() == 'leave on':
                            settings["autoLeave"] = True
                            cl.sendMessage(to, "自動離開副本已開啟")
                        elif text.lower() == 'leave off':
                            settings["autoLeave"] = False
                            cl.sendMessage(to, "自動離開副本已關閉")
                    if sender in settings['admin'] or sender in god:
                        if msg.text.lower().startswith("一般権限追加 "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    if to not in settings['gm']:
                                        settigs['gm'][to] = {}
                                    if ls not in settings['gm'][to]:
                                        settings['gm'][to][ls] = ls
                                        with open('temp.json', 'w') as fp:
                                            json.dump(settings, fp, sort_keys=True, indent=4)
                                            cl.sendMessage(to, "権限者に追加しました")
                                            cl.sendContact(to, ls)
                                    else:
                                        cl.sendMessage(to, "すでに権限者です")
                        elif msg.text.lower().startswith("一般権限削除 "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    if ls in settings['gm'][to][ls]:
                                        try:
                                            del settings['gm'][to][ls]
                                            with open('temp.json', 'w') as fp:
                                                json.dump(settings, fp, sort_keys=True, indent=4)
                                                cl.sendMessage(to, "権限を剥奪しました")
                                        except:
                                            cl.sendMessage(to, "[ERROR]\n失敗")
                                    else:
                                        cl.sendMessage(to, "権限者ではありません")
                        elif msg.text.lower().startswith("add_wc"):
                            list_ = msg.text.split(":")
                            if to not in settings['wel']:
                                try:
                                    settings['wel'][to] = list_[1]
                                    with open('temp.json', 'w') as fp:
                                        json.dump(settings, fp, sort_keys=True, indent=4)
                                        cl.sendMessage(to, "[提示]\n成功設置群組歡迎訊息\n歡迎訊息: " + list_[1])
                                except:
                                    cl.sendMessage(to, "[ERROR]\n設置群組歡迎訊息失敗!!!")
                            else:
                                cl.sendMessage(to, "[ERROR]\n群組歡迎訊息已存在!!!")
                        elif msg.text.lower().startswith("renew_wc"):
                            list_ = msg.text.split(":")
                            if to in settings['wel']:
                                try:
                                    del settings['wel'][to]
                                    settings['wel'][to] = list_[1]
                                    with open('temp.json', 'w') as fp:
                                        json.dump(settings, fp, sort_keys=True, indent=4)
                                        cl.sendMessage(to, "[提示]\n成功更新群組歡迎訊息\n歡迎訊息: " + list_[1])
                                except:
                                    cl.sendMessage(to, "[ERROR]\n更新群組歡迎訊息失敗!!!")
                            else:
                                cl.sendMessage(to, "[ERROR]\n你正在更新不存在的歡迎訊息!!!")
                        elif text.lower() == ("del_wc"):
                            if to in settings['wel']:
                                try:
                                    del settings['wel'][to]
                                    with open('temp.json', 'w') as fp:
                                        json.dump(settings, fp, sort_keys=True, indent=4)
                                        cl.sendMessage(to, "[提示]\n成功刪除群組歡迎訊息")
                                except:
                                    cl.sendMessage(to, "[ERROR]\n刪除群組歡迎訊息失敗!!!")
                            else:
                                cl.sendMessage(to, "[ERROR]\n你正在刪除不存在的歡迎訊息!!!")
                        elif text.lower() == 'wc':
                            if to in settings['wel']:
                                cl.sendMessage(to, settings['wel'][to])
                            else:
                                cl.sendMessage(to, "[提示]\n使用預設群組歡迎訊息中!!!")
                        elif text.lower() == 'ねぎしね':
                            if msg.toType == 2:
                                ginfo = cl.getGroup(to)
                                try:
                                    cl.sendMessage(to, "さようなら。")
                                    cl.leaveGroup(to)
                                    kl.leaveGroup(to)
                                    sa.leaveGroup(to)
                                    sb.leaveGroup(to)				
                                    del settings['protect'][op.param1]
                                    del settings['inviteprotect'][op.param1]
                                    del settings['qrprotect'][op.param1]
                                    with open('temp.json', 'w') as fp:
                                        json.dump(settings, fp, sort_keys=True, indent=4)
                                except:
                                    pass
                        elif text.lower() == '垢共有:オン':
                            settings["contact"] = True
                            cl.sendMessage(to, "垢情報を共有します")
                        elif text.lower() == '垢共有:オフ':
                            settings["contact"] = False
                            cl.sendMessage(to, "垢情報を共有しません")
                        elif text.lower() == '招待保護:オン':
                            if to in settings["inviteprotect"]:
                                del settings["inviteprotect"][to]
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                            cl.sendMessage(to, "招待保護をオンにしました。")
                        elif text.lower() == '招待保護:オフ':
                            settings["inviteprotect"][to] = to
                            with open('temp.json', 'w') as fp:
                                json.dump(settings, fp, sort_keys=True, indent=4)
                            cl.sendMessage(to, "招待保護をオンにしました。")
                        elif text.lower() == '蹴り保護:オン':
                            if to in settings['protect']:
                                del settings["protect"][to]
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                            cl.sendMessage(to, "蹴り保護をオンにしました。")
                        elif text.lower() == '蹴り保護:オフ':
                            settings["protect"][to] = to
                            with open('temp.json', 'w') as fp:
                                json.dump(settings, fp, sort_keys=True, indent=4)
                            cl.sendMessage(to, "蹴り保護をオフにしました")
                        elif text.lower() == 'URL保護:オン':
                            if to in settings['qrprotect']:
                                del settings["qrprotect"][to]
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                            cl.sendMessage(to, "URL保護をオンにしました。")
                        elif text.lower() == 'URL保護:オフ':
                            settings["qrprotect"][to] = to
                            with open('temp.json', 'w') as fp:
                                json.dump(settings, fp, sort_keys=True, indent=4)
                            cl.sendMessage(to, "URL保護をオフにしました。")
                        elif text.lower() == 'reread on':
                            if to in settings["reread"][to]:
                                del settings["reread"][to]
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                            cl.sendMessage(to, "查詢收回開啟")
                        elif text.lower() == 'reread off':
                            settings["reread"][to] = to
                            with open('temp.json', 'w') as fp:
                                json.dump(settings, fp, sort_keys=True, indent=4)
                            cl.sendMessage(to, "查詢收回關閉")
                        elif text.lower() == 'dm on':
                            settings["detectMention"] = True
                            cl.sendMessage(to, "自動回應開啟")
                        elif text.lower() == 'dm off':
                            settings["detectMention"] = False
                            cl.sendMessage(to, "自動回應關閉")
                        elif text.lower() == 'ck on':
                            settings["checkSticker"][to] = True
                            with open('temp.json', 'w') as fp:
                                json.dump(settings, fp, sort_keys=True, indent=4)
                            cl.sendMessage(to, "確認貼圖開啟")
                        elif text.lower() == 'ck off':
                            del settings["checkSticker"][to]
                            with open('temp.json', 'w') as fp:
                                json.dump(settings, fp, sort_keys=True, indent=4)
                            cl.sendMessage(to, "確認貼圖關閉")
                        elif text.lower() == 'cc on':
                            settings['cc'][to] = True
                            cl.sendMessage(to, "生成貼圖指令開啟")
                        elif text.lower() == 'cc off':
                            del settings['cc'][to]
                            cl.sendMessage(to, "生成貼圖指令關閉")
                    if text.lower() == 'URL招待許可':
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == False:
                                cl.sendMessage(to, "既に許可されています")
                            else:
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                cl.sendMessage(to, "許可しました")
                    elif text.lower() == 'URL招待拒否':
                        if msg.toType == 2:
                            G = cl.getGroup(to)
                            if G.preventedJoinByTicket == True:
                                cl.sendMessage(to, "すでに拒否されています")
                            else:
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)
                                cl.sendMessage(to, "拒否しました")
                    if sender in settings['admin'] or sender in god:				
                      if msg.text in settings['react']:
                          cl.sendMessage(to, settings['react'][msg.text])
                    if text.lower() == 'speed':
                        start = time.time()
                        cl.sendMessage(to, "うーん、このbotの速度は")
                        elapsed_time = time.time() - start
                        cl.sendMessage(to,format(str(elapsed_time)) + "秒")    
                    if text.lower() == 'help':
                            helpMessage = helpmessage()
                            cl.sendMessage(to, str(helpMessage))
                            cl.sendMessage(to, "bot購入等のお問い合わせは↓へ")
                            cl.sendContact(to, "u22db032049b35c0f566a481626daabf8")
                    elif text.lower() == '全蹴り':
                        cl.sendMessage(to, "ちょwwwwwwグル主さーん！！wwwwww今こいつ、このグループ壊そうとしましたよwww追放しないとwwwwww")
                    elif text.lower() == '歌って':
                        cl.sendMessage(to, "嫌です") 
                    elif text.lower() == '全キャンセル':
                        if msg.toType == 2:
                            X = cl.getGroup(msg.to)
                            if X.invitee is not None:
                                gInviMids = (contact.mid for contact in X.invitee)
                                ginfo = cl.getGroup(msg.to)
                                sinvitee = str(len(ginfo.invitee))
                                start = time.time()
                                for cancelmod in gInviMids:
                                    cl.cancelGroupInvitation(msg.to, [cancelmod])
                                elapsed_time = time.time() - start
                                cl.sendMessage(to, "招待をキャンセルしました\nタイム: %s秒" % (elapsed_time))
                                cl.sendMessage(to, "人数:" + sinvitee)
                    elif text.lower() == '全メンション':
                        group = cl.getGroup(msg.to)
                        nama = [contact.mid for contact in group.members]
                        k = len(nama)//100
                        for a in range(k+1):
                            txt = u''
                            s=0
                            b=[]
                            for i in group.members[a*100 : (a+1)*100]:
                                b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                s += 7
                                txt += u'@Negiel \n'
                            cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
                            cl.sendMessage(to, "{} 人でした".format(str(len(nama))))
                    elif text.lower() == 'にあたやらに':
                        if settings["admin"] == {}:
                            cl.sendMessage(to, "うーんと")
                        else:
                            try:
                                mc = "[ 最高権限者 ]\n"
                                for mi_d in settings["admin"]:
                                    mc += "-> " + cl.getContact(mi_d).displayName + "\n"
                                cl.sendMessage(to, mc)
                            except:
                                cl.sendMessage(to, "error")
                    elif text.lower() == 'ブラック確認':
                        if settings["blacklist"] == {}:
                            cl.sendMessage(to, "うーんとね")
                        else:
                            try:
                                mc = "[ ブラリス ]\n"
                                for mi_d in settings["blacklist"]:
                                    mc += "-> " + cl.getContact(mi_d).displayName + "\n"
                                cl.sendMessage(to, mc)
                            except:
                                pass
                    elif text.lower() == 'reactlist':
                        ret_ = "[關鍵字列表]\n"
                        for name in settings['react']:
                            ret_ +="->" + name + "\n"
                        cl.sendMessage(to, ret_)
                    elif text.lower() == '一般権限者':
                        if settings["gm"][to] == {}:
                                cl.sendMessage(to, "うーんとね")
                        else:
                            try:
                                mc = "[ 一般権限者 ]\n"
                                for mi_d in settings["gm"][to]:
                                    mc += "-> " + cl.getContact(mi_d).displayName + "\n"
                                cl.sendMessage(to, mc)
                            except:
                                pass
                    elif text.lower() == 'うんこ':
                        timeNow = time.time()
                        runtime = timeNow - botStart
                        runtime = format_timespan(runtime)
                        cl.sendMessage(to, "運行時間 {}".format(str(runtime)))
                    elif text.lower() == 'ねぎしね':
                    	cl.sendMessage(to,"またね！")
                    	ginfo = cl.getGroup(to)       
                    	cl.leaveGroup(to)
                    elif text.lower() == 'mid':
                        cl.sendMessage(to,"[mid]\n" +  sender)
                    elif text.lower() == 'グループ作者':
                        group = cl.getGroup(to)
                        GS = group.creator.mid
                        cl.sendContact(to, GS)
                    elif text.lower() == 'gid':
                        gid = cl.getGroup(to)
                        cl.sendMessage(to, "[gid]\n" + gid.id)
                    elif text.lower() == '占って':
                    	cl.sendMessage(to,"残念！大凶です！ねぎえるの半botを買うとマシになる！これを見た方限定、定価より500円引き！詳しくは↓へ！(スクショをご提示ください)")
                    	cl.sendMessage(to,"http://line.me/ti/p/%40ubg0555p")
                    elif text.lower() == '招待URL生成':
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "[ GURL ]\nhttp://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "URLはオフです。".format(str(settings["keyCommand"])))
                    elif msg.text.lower().startswith("add_react"):
                        list_ = msg.text.split(":")
                        if list_[1] not in settings['react']:
                            try:
                                settings['react'][list_[1]] = list_[2]
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                                    cl.sendMessage(to, "[新增回應]\n" + "關鍵字: " + list_[1] + "\n回應: " + list_[2])
                            except:
                                cl.sendMessage(to, "[ERROR]\n" + "新增關鍵字失敗")
                        else:
                            cl.sendMessage(to, "[ERROR]\n" + "關鍵字已存在")
                    elif msg.text.lower().startswith("del_react"):
                        list_ = msg.text.split(":")
                        if list_[1] in settings['react']:
                            try:
                                del settings['react'][list_[1]]
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                                    cl.sendMessage(to, "[刪除關鍵字]\n成功刪除關鍵字!!!\n關鍵字: " + list_[1])
                            except:
                                cl.sendMessage(to, "[ERROR]\n刪除關鍵字失敗!!!")
                        else:
                            cl.sendMessage(to, "[ERROR]\n指定刪除的關鍵字並不在列表中!!!")
                    elif msg.text.lower().startswith("renew_react"):
                        list_ = msg.text.split(":")
                        if list_[1] in settings['react']:
                            try:
                                del settings['react'][list_[1]]
                                settings['react'][list_[1]] = list_[2]
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                                    cl.sendMessage(to, "[更新回應]\n成功更新回應!!!\n關鍵字: " + list_[1] + "\n回應: " + list_[2])
                            except:
                                cl.sendMessage(to, "[ERROR]\n更新關鍵字失敗!!!")
                        else:
                            cl.sendMessage(to, "[ERROR]\n指定更新關鍵字並不在列表中!!!")
                    elif msg.text.lower().startswith("add_sr"):
                        list_ = msg.text.split(":")
                        number = str(list_[1]) + str(list_[2])
                        if number not in settings['sr']:
                            try:
                                settings['sr'][number] = list_[3]
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                                    cl.sendMessage(to, "[新增貼圖回應]\n" + "回應: " + list_[3] + "\n系統辨識碼: " + number)
                            except:
                                cl.sendMessage(to, "[ERROR]\n" + "新增貼圖關鍵字失敗")
                        else:
                            cl.sendMessage(to, "[ERROR]\n" + "貼圖關鍵字已存在")
                    elif msg.text.lower().startswith("del_sr"):
                        list_ = msg.text.split(":")
                        number = str(list_[1]) + str(list_[2])
                        if number in settings['sr']:
                            try:
                                del settings['sr'][number]
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                                    cl.sendMessage(to, "[刪除貼圖關鍵字]\n成功刪除貼圖關鍵字!!!\n系統辨識碼: " + number)
                            except:
                                cl.sendMessage(to, "[ERROR]\n刪除貼圖關鍵字失敗!!!")
                        else:
                            cl.sendMessage(to, "[ERROR]\n指定刪除的貼圖關鍵字並不在列表中!!!")
                    elif msg.text.lower().startswith("renew_sr"):
                        list_ = msg.text.split(":")
                        number = str(list_[1]) + str(list_[2])
                        if number in settings['sr']:
                            try:
                                del settings['sr'][number]
                                settings['sr'][number] = list_[3]
                                with open('temp.json', 'w') as fp:
                                    json.dump(settings, fp, sort_keys=True, indent=4)
                                    cl.sendMessage(to, "[更新貼圖回應]\n成功更新貼圖回應!!!\n回應: " + list_[3] + "\n系統辨識碼: " + number)
                            except:
                                cl.sendMessage(to, "[ERROR]\n更新貼圖關鍵字失敗!!!")
                        else:
                            cl.sendMessage(to, "[ERROR]\n指定更新貼圖關鍵字並不在列表中!!!")
                    elif text.lower() == '既読ポイント設定':
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                        hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                        hr = timeNow.strftime("%A")
                        bln = timeNow.strftime("%m")
                        for i in range(len(day)):
                            if hr == day[i]: hasil = hari[i]
                        for k in range(0, len(bulan)):
                            if bln == str(k): bln = bulan[k-1]
                        readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                        if msg.to in read['readPoint']:
                                try:
                                    del read['readPoint'][msg.to]
                                    del read['readMember'][msg.to]
                                    del read['readTime'][msg.to]
                                except:
                                    pass
                                read['readPoint'][msg.to] = msg.id
                                read['readMember'][msg.to] = ""
                                read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                                read['ROM'][msg.to] = {}
                                with open('read.json', 'w') as fp:
                                    json.dump(read, fp, sort_keys=True, indent=4)
                                    cl.sendMessage(msg.to,"既に設定されています")
                        else:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('read.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                cl.sendMessage(msg.to, "既読ポイントを設定しました。")
                    elif text.lower() == '既読ポイント削除':
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                        hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                        hr = timeNow.strftime("%A")
                        bln = timeNow.strftime("%m")
                        for i in range(len(day)):
                            if hr == day[i]: hasil = hari[i]
                        for k in range(0, len(bulan)):
                            if bln == str(k): bln = bulan[k-1]
                        readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                        if msg.to not in read['readPoint']:
                            cl.sendMessage(msg.to,"既読ポイントは設定されていません。")
                        else:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                    pass
                            cl.sendMessage(msg.to, "削除しました。")
                    elif text.lower() == 'なゆたやsr':
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                        hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                        hr = timeNow.strftime("%A")
                        bln = timeNow.strftime("%m")
                        for i in range(len(day)):
                            if hr == day[i]: hasil = hari[i]
                        for k in range(0, len(bulan)):
                            if bln == str(k): bln = bulan[k-1]
                        readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n時間 : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                        if msg.to in read["readPoint"]:
                            try:
                                del read["readPoint"][msg.to]
                                del read["readMember"][msg.to]
                                del read["readTime"][msg.to]
                            except:
                                pass
                            cl.sendMessage(msg.to, "重置已讀點:\n" + readTime)
                        else:
                            cl.sendMessage(msg.to, "已讀點未設定")
                    elif text.lower() == '既読確認':
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                        hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                        hr = timeNow.strftime("%A")
                        bln = timeNow.strftime("%m")
                        for i in range(len(day)):
                            if hr == day[i]: hasil = hari[i]
                        for k in range(0, len(bulan)):
                            if bln == str(k): bln = bulan[k-1]
                        readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\n時間 : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                        if receiver in read['readPoint']:
                            if read["ROM"][receiver].items() == []:
                                cl.sendMessage(receiver,"既  読  ０  人")
                            else:
                                chiya = []
                                for rom in read["ROM"][receiver].items():
                                    chiya.append(rom[1])
                                cmem = cl.getContacts(chiya)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = '《既読済の人達》\n'
                            for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@c\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                            text = xpesan+ zxc
                            try:
                                cl.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                            except Exception as error:
                                print (error)
                            pass
                        else:
                            cl.sendMessage(receiver,"既読ポイントが設定されていません。")
        if op.type == 26:
            try:
                msg = op.message
                try:
                    if msg.toType == 0:
                        cl.log("[%s]"%(msg._from)+msg.text)
                    else:
                        cl.log("[%s]"%(msg.to)+msg.text)
                    if msg.contentType == 0:
                        msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
                except:
                    pass
            except Exception as e:
                print(logError(e))
        if op.type == 65:
            try:
                at = op.param1
                msg_id = op.param2
                if at not in settings["reread"]:
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"] not in bl:
                            cl.sendMessage(at,"[送信取り消し者]\n%s\n[取り消し内容]\n%s"%(cl.getContact(msg_dict[msg_id]["from"]).displayName,msg_dict[msg_id]["text"]))
                            print ["收回訊息"]
                        del msg_dict[msg_id]
                else:
                    pass
            except Exception as e:
                print(e)
        if op.type == 26:
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
                if settings["autoRead"] == True:
                    cl.sendChatChecked(to, msg_id)
                if to in read["readPoint"]:
                    if sender not in read["ROM"][to]:
                        read["ROM"][to][sender] = True
                        cl.log()
                if msg.contentType == 0 and sender not in clMID and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if clMID in mention["M"]:
                                if settings["detectMention"] == True:
                                    contact = cl.getContact(sender)
                                    sendMessageWithMention(to, contact.mid)
                                    cl.sendMessage(to, "(‘ω’)")
                                    time.sleep(0.5)
                                    cl.sendContact(op.param1, "(   ° ͜ʖ ° )")
                                break
        if op.type == 55:
            print ("[ 55 ] 通知讀取消息")
            try:
                if op.param1 in read['readPoint']:
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    backupData()
                else:
                    pass
            except:
                pass
    except Exception as e:
        logError(e)
while True:
    try:
        ops = oepoll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
                lineBot(op)
                oepoll.setRevision(op.revision)
    except Exception as e:
        logError(e)
