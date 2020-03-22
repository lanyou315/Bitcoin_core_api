#coding=utf-8
#from jsonrpclib import ServerProxy
from bitcoinrpc.authproxy import AuthServiceProxy as ServiceProxy, JSONRPCException
import numpy as np
np.set_printoptions(suppress=True)
import re,time
from time import sleep
class qianbao():
    access = ServiceProxy("http://admin:123456@192.168.0.37:8832")
    def balancebtc(self):
        '''钱包信息'''
        print("钱包信息:",self.access.getwalletinfo(),)
        print("钱包下所有的账户及余额:%s,账户BTC可用余额:%.8f"%(self.access.listaccounts(),self.access.getbalance("*")))
        print("未确认金额：%.8f"%self.access.getunconfirmedbalance())
    def addressbtc(self,account):
        '''钱包地址相关信息-生成钱包、返回对应账户的钱包地址'''
        print("地址总数：%s"%len(self.access.getaddressesbyaccount(account)),"\n","返回分配给特定帐户%s的地址列表:%s"%(account,self.access.getaddressesbyaccount(account)))
        print("生成钱包地址:",self.access.getnewaddress(account))
    def addbalance_usdt(self,address):
        '''指定地址的usdt余额信息'''
        print("钱包所有地址的OMNI:%s"%(self.access.omni_getwalletaddressbalances()))
        print("指定地址%s可用余额OMNI:%s"%(address,self.access.omni_getbalance(address,31)))
    def up_passwd(self,oldpasswd,newpasswd):
        '''修改钱包密码：oldpasswd---旧密码,newpasswd---新密码'''
        print("已修改钱包密码",self.access.walletpassphrasechange(oldpasswd,newpasswd))
    def open_wallet(self,passwd,second):
        '''passwd指钱包密码,second指解锁钱包的有效时间'''
        '''判断钱包是否解锁成功'''
        try:
            assert self.access.walletpassphrase(passwd,second) is None
            print("钱包已解锁，有效时间为%s秒"%second)
            sleep(3)
        except Exception as e:
            print("钱包解锁失败",e)
    def close_wallet(self):
        '''锁定钱包'''
        try:
            self.access.walletlock()
            print("锁定钱包成功！")
        except Exception as e:
            print("锁定钱包失败",e)
    # sleep(2)
    def dkey(self,add):
        '''获取私钥'''
        print("获取该地址(%s)的私钥:"%add,self.access.dumpprivkey(add))
    print("未确认金额："'%.8f'%access.getunconfirmedbalance())
    def sendbtc(self,btc_toaddress,money):


        try:
            #批量发送货币，从指定账户发出
            #order1=[self.access.sendmany("lanyou",{"2N9dyotLGZbH9ARZ6Xuu2svqeruFfuRhyK3":0.5,"2NBznz2az5z94UK8NpKRrEZfJ7oxgbsLP9p":0.3,"2NEaGzMwyg6QofbC4YckhzXdzEq1dTRLteC":0.6,"2N1rtrP3Eqb4G87eKYPydP2B9NTGHNPHJhx":0.5,"2MvXEWEoJS68Qd6LV46noin6GZNoiHsg4bH":1})]
            #order1=self.access.omni_sendtoaddress("mmj6fThQkgXTtysdU5rkqXjLCzjA2NBqAp",0.1)#从提现金额中扣除手续费
            order1=self.access.sendtoaddress(btc_toaddress,money) #从账户中扣除
            print("批量转币成功，转币生成的订单号：%s"%order1)

        except Exception as e:
            print("无法转币！",e)

    def sendusdt(self,fromaddress,toaddress,type,money):
        '''发送地址，目标地址，类型，发送金额'''
        #向指定的比特币地址发送OMNI
        try:
            order1=self.access.omni_sendtoaddress(fromaddress,toaddress,type,money) #发送地址，目标地址，类型，发送金额
            print("批量转币成功，转币生成的订单号：%s"%order1)

        except Exception as e:
            print("无法转币！",e)
    #获取有关钱包交易的详细信息
    #access.keypoolrefill(1000000)
    # print("keypoolrefill done")
    print("交易的详细信息:\n",access.gettransaction("0e7de4c3c713bb30a832a6538f1253fc2b16ae06ceff34baeeaa4cb7194c5c7d"))
    # a=access.listtransactions("lanyou",1)
    # print("交易总数：%d笔,交易记录详情：\n %s"%(len(a),a))
    # sleep(2)
    # print("未确认金额：",access.getunconfirmedbalance())
    def 交易记录(self):
        '''交易记录如下'''
        x=self.access.listtransactions("lanyou",10)    #  “*”代表全部交易记录，“lanyou”代表账户lanyou的交易记录，“”代表默认账户的交易记录
        # print (x)
        # print(len(x))
        print("交易记录如下：\n")
        for i in x:
            '''交易记录如下'''
           # print("交易记录如下")
            print("{'account':'%s','confirmations':'%s','address':'%s','category':'%s','amount':%.8f,'txid':'%s','time':'%s','timereceived':'%s'}"%(i["account"],i["confirmations"],i["address"],i["category"],i["amount"],i["txid"],time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["time"])),time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(i["timereceived"]))))
    #返回当前比特币地址接收付款到这个帐户
    #print(access.getaccountaddress("lanyou"))

a=qianbao()
a.balancebtc()
a.addbalance_usdt('mkUBgvkHgSmUahwqne5EimWMNh2joSWJGg')
#a.addbalance_usdt('mz1KqNig9MeAQbzSNpGkD1d1V1wnkJFwzx')
#a.addressbtc('baling')
#a.up_passwd("123456","xbtmex123456")
#a.open_wallet("12345678",360)   #20
#a.open_wallet("123456",360)   #24
a.open_wallet("omni1234567",360)   #37环境
a.dkey("mkUBgvkHgSmUahwqne5EimWMNh2joSWJGg")
#a.交易记录()
#转BTC 目标地址，发送金额
#a.sendbtc('moha9Afkzv82EscWEnnhmLuCpr7Tq4Ufhb',0.2)
 #转usdt     发送地址，目标地址，类型，发送金额
#a.sendusdt('mz1KqNig9MeAQbzSNpGkD1d1V1wnkJFwzx','mmj6fThQkgXTtysdU5rkqXjLCzjA2NBqAp',1,2)