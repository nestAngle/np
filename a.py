# -*- coding: utf-8 -*-
from linepy import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse,timeit,data,atexit
from gtts import gTTS
from googletrans import Translator
botStart = time.time()

#登入驗證
cl = LINE()
channelToken = cl.getChannelResult()
cl.log("TOKEN:" + str(cl.authToken))
print ("======login成功=====")

oepoll = OEPoll(cl)
settingsOpen = codecs.open("temp.json","r","utf-8")
settings = json.load(settingsOpen)
clMID = cl.profile.mid
KAC=[cl]
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{},
    'ajm':""
}
setTime = {}
setTime = wait2['setTime']
master=['ub8278328ab250ef71fbeb1d5c95f5e71',clMID]
msg_dict = {}
bl = [""]
ajm = [""]
def cTime_to_datetime(unixtime):
    return datetime.datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def restartBot():
    print ("[ REBOT ] 機器重啟")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=False, indent=4, ensure_ascii=True)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=False, indent=4, ensure_ascii=True)
        return False
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
    helpMessage = """≪この半botのhelpです≫
    
☞me…自分の連絡先を表示します
☞追加URL…自分の追加URLを表示します
☞自動参加:オン/オフ…自動参加をオン/オフにします
☞参加挨拶:オン/オフ…自動参加時の挨拶をオン/オフにします
☞参加挨拶変更:(text)…自動参加時の挨拶を変更します
☞一斉送信:(text)…入っている全グループに一斉送信します
☞垢表示 @…メンションしたユーザーのアカウントを表示します
☞mid @…メンションしたユーザーのmidを表示します
☞連絡先:(mid)…midで連絡先を表示します
☞速度…このbotの速度を計測します

☞ブラリス追加 @...メンションでブラリスに追加します
☞ブラリス追加:(mid)…midでブラリスに追加します
☞ブラリス解除 @…メンションでブラリスから解除します
☞ブラリス解除:(mid)…midでブラリスから解除します
☞ブラリス全解除…全てのブラリスを解除します
☞ブラリス確認…登録されているブラリスを確認します
☞ブラリス排除…グループからブラリスを排除します
☞ブラリス全排除…入っている全グループからブラリスを排除します

☞グル名:(text)…グループ名を変更します
☞グループ情報…グループ情報を表示します
☞Mk @...メンションでユーザーを蹴ります
☞Nk …指定した名前のユーザーを蹴ります
☞mid招待: …midでユーザーを招待します
☞全招待キャンセル…全ての招待をキャンセルします【規制注意】
☞全蹴り…メンバーを全蹴りします【規制注意】
☞既読ポイント設定…既読ポイントを設定します
☞既読確認…既読した人を確認します(事前に既読ポイント設定を行ってください)
☞招待URL生成…招待URLを生成します
☞招待URL許可…招待URLを許可します
☞招待URL拒否…招待URLを拒否します

ねぎえるのLINE@
http://line.me/ti/p/%40ubg0555p"""
    return helpMessage     
def lineBot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if settings["ajfm"] == True:
                cl.sendMessage(op.param1,wait2['ajm'])
        if op.type == 11:
            group = cl.getGroup(op.param1)
            contact = cl.getContact(op.param2)
        if op.type == 13:
            contact1 = cl.getContact(op.param2)
            contact2 = cl.getContact(op.param3)
            group = cl.getGroup(op.param1)
            print ("[ JOIN ] 收到群組邀請: " + str(group.name) + "\n邀請的人: " + contact1.displayName + "\n被邀請的人" + contact2.displayName)
            if settings["autoJoin"] == True:
                if op.param3 in master:
                    print ("[ NEWJOIN ]使用者邀請加入群組: " + str(group.name))
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendMessage(op.param1,wait2['ajm'])
                else:
                    pass
        if op.type == 24:
                cl.leaveRoom(op.param1)
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
                if "Mk " in msg.text:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        if target in master:
                            pass
                        else:
                            try:
                                cl.kickoutFromGroup(to,[target])
                            except:
                                pass
                elif "Nk:" in msg.text:
                    name = msg.text.replace("Nk:",'')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendMessage(msg.to,"見つかりませんでした")
                    else:
                        for target in targets:
                            try:
                                cl.kickoutFromGroup(msg.to,[target])
                            except:
                                cl.sendMessage(msg.to,'エラー')
                elif "mid招待:" in msg.text:
                    midd = msg.text.replace("mid招待:","")
                    cl.findAndAddContactsByMid(midd)
                    cl.inviteIntoGroup(msg.to,[midd])
                elif msg.text in ["全蹴り"]:
                    group = cl.getGroup(msg.to)
                    _name = msg.text.replace("全蹴り","")
                    targets = []
                    for g in group.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                            for target in targets:
                                try:
                                    cl.kickoutFromGroup(msg.to,[target])
                                except:
                                	cl.sendMessage(msg.to, "エラー")
                elif msg.text in ["停止"]:
                    cl.sendMessage(to, "半botを停止します。")
                    restartBot()
                elif msg.text in ["自動参加:オン"]:
                    settings["autoJoin"] = True
                    cl.sendMessage(to, "自動参加をオンにしました")
                elif msg.text in ["自動参加:オフ"]:
                    settings["autoJoin"] = False
                    cl.sendMessage(to, "自動参加をオフにしました")
                elif msg.text in ["参加挨拶:オン"]:
                    settings["ajfm"] = True
                    cl.sendMessage(to, "自動参加挨拶をオンにしました")
                elif msg.text in ["参加挨拶:オン"]:
                    settings["ajfm"] = False
                    cl.sendMessage(to, "自動参加挨拶をオフにしました")
                elif "参加挨拶変更:" in msg.text:
                    text = msg.text.replace("参加挨拶変更:","")
                    if text in [""," ","\n",None]:
                        cl.sendMessage(msg.to,"変更できない文字が含まれています")
                    else:
                        wait2['ajm'] = text
                        cl.sendMessage(msg.to,"%s\n\nに変更しました" % text)
                elif "追加URL" == msg.text:
                    ids = cl.reissueUserTicket(0,3)
                    cl.sendMessage(msg.to,"http://line.me/ti/p/%s" % ids)
                elif "ブラリス追加 " in msg.text:
                    if msg.toType == 2:
                        print ("[ JBAN ] 成功")
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
                                    cl.sendMessage(to, "追加しました")
                                except:
                                    pass
                elif "ブラリス追加:" in msg.text:
                    mmid = msg.text.replace("ブラリス追加:","")
                    print ("[ JMBAN ] 成功")
                    try:
                        settings["blacklist"][mmid] = True
                        cl.sendMessage(to, "追加しました。")
                    except:
                        pass
                elif msg.text in ["ブラリス全解除"]:
                    for mi_d in settings["blacklist"]:
                        settings["blacklist"] = {}
                    cl.sendMessage(to, "ブラリスを全削除しました")
                elif "ブラリス解除:" in msg.text:
                    mmid = msg.text.replace("ブラリス解除:","")
                    print ("[ UMBAN ] 成功")
                    try:
                        del settings["blacklist"][mmid]
                        cl.sendMessage(to, "解除しました")
                    except:
                        pass
                elif "ブラリス解除 " in msg.text:
                    if msg.toType == 2:
                        print ("[ UBAN ] 成功")
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
                                    cl.sendMessage(to, "解除しました")
                                except:
                                    pass
                elif msg.text in ["ブラリス確認"]:
                    if settings["blacklist"] == {}:
                        cl.sendMessage(to, "ブラリスはいません")
                    else:
                        mc = "ブラックリスト"
                        for mi_d in settings["blacklist"]:
                            mc += "\n☞" + cl.getContact(mi_d).displayName
                        cl.sendMessage(to, mc)
                elif msg.text in ["ブラリス排除"]:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in settings["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            print ("1")
                            cl.sendMessage(to, "ブラリスはいません")
                            return
                        for jj in matched_list:
                            cl.kickoutFromGroup(to, [jj])
                            cl.sendMessage(to, "さようなら。")
                elif msg.text in ["ブラリス全排除"]:
                    gid = cl.getGroupIdsJoined()
                    group = cl.getGroup(to)
                    gMembMids = [contact.mid for contact in group.members]
                    ban_list = []
                    for tag in settings["blacklist"]:
                        ban_list += filter(lambda str: str == tag, gMembMids)
                    if ban_list == []:
                        cl.sendMessage(to, "ブラリスはいません")
                    else:
                        for i in gid:
                            for jj in ban_list:
                                cl.kickoutFromGroup(i, [jj])
                            cl.sendMessage(i, "さようなら。")
                elif "一斉送信:" in msg.text:
                    bctxt = text.replace("一斉送信:","")
                    n = cl.getGroupIdsJoined()
                    for manusia in n:
                        cl.sendMessage(manusia,(bctxt))
                elif msg.text.lower().startswith("垢表示 "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        cl.sendContact(to, ls)
                elif msg.text.lower().startswith("mid "):
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if mention["M"] not in lists:
                                lists.append(mention["M"])
                        ret_ = "mid"
                        for ls in lists:
                            ret_ += "\n" + "\n" + ls
                        cl.sendMessage(msg.to, str(ret_))
                elif "連絡先:" in msg.text:
                    mmid = msg.text.replace("連絡先:","")
                    cl.sendContact(to, mmid)
                elif msg.text in ["help"]:
                    helpMessage = helpmessage()
                    cl.sendMessage(to, str(helpMessage))
                elif text.lower() == '運行時間':
                    timeNow = time.time()
                    runtime = timeNow - botStart
                    runtime = format_timespan(runtime)
                    cl.sendMessage(to, "運行時間 {}".format(str(runtime)))
                elif msg.text in ["既読ポイント設定"]:
                    cl.sendMessage(msg.to, "既読ポイントを設定しました")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                elif msg.text in ["既読確認"]:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                chiya += rom[1] + "\n"
                        cl.sendMessage(msg.to, "既読を付けた人達 %s\n[%s]" % (wait2['readMember'][msg.to],setTime[msg.to]))
                    else:
                        cl.sendMessage(msg.to, "既読ポイントが設定されていません")
                elif "グル名:" in msg.text:
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("グル名:","")
                        cl.updateGroup(X)
                        cl.sendMessage(msg.to,"変更しました")
                    else:
                        cl.sendMessage(msg.to,"グル外では使えません")
                elif text.lower() == 'me':
                    sendMessageWithMention(to, sender)
                    cl.sendContact(to, sender)
                elif msg.text in ["全招待キャンセル"]:
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
                        cl.sendMessage(to, "取り消しました" )
                    else:
                        cl.sendMessage(to, "招待はありませんでした")
                elif msg.text in ["速度"]:
                    time0 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
                    str1 = str(time0)
                    start = time.time()
                    cl.sendMessage(to,'速度\n' + str1 + '秒')
                elif msg.text in ["招待URL生成"]:
                    if msg.toType == 2:
                        group = cl.getGroup(to)
                        if group.preventedJoinByTicket == False:
                            ticket = cl.reissueGroupTicket(to)
                            cl.sendMessage(to, "招待URLを生成したよ☆\n(※今までにこのbotが発行したURLは使えなくなりました。)\n\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                        else:
                            cl.sendMessage(to, "招待URLを生成したよ☆\n(※今までにこのbotが発行したURLは使えなくなりました。)\n\nhttps://line.me/R/ti/g/{}".format(str(ticket)))
                elif msg.text in ["招待URL許可"]:
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == False:
                            cl.sendMessage(to, "既に許可されています")
                        else:
                            G.preventedJoinByTicket = False
                            cl.updateGroup(G)
                            cl.sendMessage(to, "許可しました")
                elif msg.text in ["招待URL拒否"]:
                    if msg.toType == 2:
                        G = cl.getGroup(to)
                        if G.preventedJoinByTicket == True:
                            cl.sendMessage(to, "既に拒否されています")
                        else:
                            G.preventedJoinByTicket = True
                            cl.updateGroup(G)
                            cl.sendMessage(to, "拒否しました")
                elif msg.text in ["グループ情報"]:
                    group = cl.getGroup(to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Negiel"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventedJoinByTicket == True:
                        gQr = "拒否"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    else:
                        gQr = "許可"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                        path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                        ret_ = "#─グループ情報─#"
                        ret_ += "\nグループ名 : {}".format(str(group.name))
                        ret_ += "\ngid : {}".format(group.id)
                        ret_ += "\nグループ作者 : {}".format(str(gCreator))
                        ret_ += "\nグループ人数 : {}".format(str(len(group.members)))
                        ret_ += "\n招待中の人数 : {}".format(gPending)
                        ret_ += "\nURLの状態 : {}".format(gQr)
                        ret_ += "\n招待URL : {}".format(gTicket)
                        cl.sendMessage(to, str(ret_))
                        cl.sendImageWithURL(to, path)
                elif msg.text in ["全メンション"]:
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
                            txt += u'@ \n'
                        cl.sendMessage(to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n▪" + Name
                        wait2['ROM'][op.param1][op.param2] = "▪" + Name
                else:
                    pass
            except:
                pass
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