#coding=utf-8
#from jsonrpclib import ServerProxy
from bitcoinrpc.authproxy import AuthServiceProxy as ServiceProxy, JSONRPCException
import numpy as np
np.set_printoptions(suppress=True)
import re
from time import sleep
class qianbao():
    #access = ServiceProxy("http://admin:123456@192.168.0.24:8332")
    access = ServiceProxy("http://admin:123456@192.168.0.24:8332")
    #print("钱包下所有的账户及余额:%s"%access.listaccounts(),"账户可用余额:%.8f"%access.getbalance())
    def balancebtc(self):
        '''钱包信息'''
        #print("钱包信息:",self.access.getwalletinfo(),)
        print("钱包下所有的账户及余额:%s,\n账户可用余额:%.8f"%(self.access.listaccounts(),self.access.getbalance()))
    #def addressbtc(self):
    def addressbtc(self,account):
        '''钱包地址相关信息-生成钱包、返回对应账户的钱包地址'''
        print("地址总数：",len(self.access.getaddressesbyaccount('')),"\n","返回分配给特定帐户%s的地址列表:"%account,self.access.getaddressesbyaccount(account))
        #print("地址总数：",len(self.access.getaddressesbyaccount()),"\n","返回分配给特定帐户%s的地址列表:"%self.access.getaddressesbyaccount())
        print("生成钱包地址:",self.access.getnewaddress(account))
        # '''把返回分配给特定帐户地址列表打印出来，并保存到“F:\工作相关\数字货币期货系统\钱包\钱包账户-地址.txt”文件中'''
        # f=open(u"F:\工作相关\数字货币期货系统\钱包\钱包账户-地址.txt","w+")
        # a=[self.access.getaddressesbyaccount(""),self.access.getaddressesbyaccount("basecoin"),self.access.getaddressesbyaccount("lanyou")]
        # for i in a:
        #     print("返回分配给特定帐户地址列表如下：\n",format(i),file=f)
        # print("")
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

    # add="2MusJ6DzAw3gTxJUiF9fbx7DCEC5Sp3yDyN"
    # print("获取该地址(%s)的私钥:"%add,access.dumpprivkey(add))
    def sendbtc(self,toaddress,money,):
        # # #向指定的比特币地址发送比特币
        # sendaddress="2MyBydKkLQZRwyuCtm3vpRpZ6YW1efGejKH"
        # self.access.sendtoaddress(sendaddress,0.31) #交易流水号
        # sleep(2)

        try:
            #批量发送货币，从指定账户发出
            #order1=[self.access.sendmany("lanyou",{"2N9dyotLGZbH9ARZ6Xuu2svqeruFfuRhyK3":0.5,"2NBznz2az5z94UK8NpKRrEZfJ7oxgbsLP9p":0.3,"2NEaGzMwyg6QofbC4YckhzXdzEq1dTRLteC":0.6,"2N1rtrP3Eqb4G87eKYPydP2B9NTGHNPHJhx":0.5,"2MvXEWEoJS68Qd6LV46noin6GZNoiHsg4bH":1})]
            #order1=[self.access.sendmany("lanyou",{"2NBbqzSrwL8TU4WJR4jMkBvVsntmnoTYq4i":2})]
            order1=self.access.sendtoaddress(toaddress,money,'','',True)  #从提现金额中扣除手续费
            print("批量转币成功，转币生成的订单号：%s"%order1)
        except Exception as e:
            print("无法转币！",e)
        print("未确认金额："'%.8f'%self.access.getunconfirmedbalance())
    #获取有关钱包交易的详细信息
    #print("最近的交易记录:\n",access.listtransactions("lanyou",100))
    #access.keypoolrefill(1000000)
    # print("keypoolrefill done")
    print("交易的详细信息:\n",access.gettransaction("83cfb139cb43715c3130d0d7520c297bc9ff00e1edee1e87f805373b2025a3db"))
    #print("未确认金额：%.8f"%access.getunconfirmedbalance())
    #print("交易的详细信息:\n",access.gettransaction("86bf576eceaa567765dd23e405e0115abba3c75b224296dcb347436fce18f538"))  2dcd10c120aca816e5dd4d58800e1c87c87e3c88e8d2debd9dde1e4534569064
    # a=access.listtransactions("lanyou",1)
    # print("交易总数：%d笔,交易记录详情：\n %s"%(len(a),a))
    # sleep(2)
    # print("未确认金额：",access.getunconfirmedbalance())
    def 交易记录(self):
        '''交易记录如下'''
        x=self.access.listtransactions('*',10)    #  “*”代表全部交易记录，“lanyou”代表账户lanyou的交易记录，“”代表默认账户的交易记录
        #print (x)
        # print(len(x))
        print("交易记录如下：\n")
        for i in x:
            '''交易记录如下'''
           # print("交易记录如下")
            print("{'account':'%s','confirmations':'%s','address':'%s','category':'%s','amount':%.8f,'txid':'%s','time':'%s','timereceived':'%s'}"%(i["account"],i["confirmations"],i["address"],i["category"],i["amount"],i["txid"],i["time"],i["timereceived"]))
    #返回当前比特币地址接收付款到这个帐户
    #print(access.getaccountaddress("lanyou"))
a=qianbao()
a.balancebtc()
a.addressbtc('')
#a.up_passwd("123456","omni123456")
#a.open_wallet("123456",360)   #20环境
#a.open_wallet("123456",360)   #24环境
#a.open_wallet("omni123456",360)   #37环境
# i=1
# for i in range(50):
#     a.addressbtc("lanyou")
#     i+=1

#a.交易记录()
#a.sendbtc('mwJATEs3mFz92zb6EM8EiXqGtdZPR4zz9L',0.1)