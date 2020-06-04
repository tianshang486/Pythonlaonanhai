class Payment:pass
class Alipay(Payment):
    def __init__(self,name):
        self.name = name
    def pay(self,money):
        dic = {'uname':self.name,'price':money}
        print('%s通过支付宝支付%s钱成功'%(self.name,money))

class WeChat(Payment):
    def __init__(self,name):
        self.name = name
    def pay(self,money):
        dic = {'username':self.name,'money':money}
        print('%s通过微信支付%s钱成功'%(self.name,money))

class Apple(Payment):
    def __init__(self,name):
        self.name = name
    def pay(self,money):
        dic = {'name': self.name, 'number': money}
        print('%s通过苹果支付%s钱成功' % (self.name, money))

class QQpay:
    def __init__(self,name):
        self.name = name
    def pay(self,money):
        print('%s通过qq支付%s钱成功' % (self.name, money))
import sys
def pay(name,price,kind):
    class_name = getattr(sys.modules['__main__'],kind)
    obj = class_name(name)
    obj.pay(price)
    # if kind == 'Wechat':
    #     obj = WeChat(name)
    # elif kind == 'Alipay':
    #     obj = Alipay(name)
    # elif kind == 'Apple':
    #     obj = Apple(name)
    # obj.pay(price)

pay('alex',400,'WeChat')
pay('alex',400,'Alipay')
pay('alex',400,'Apple')
pay('alex',400,'QQpay')

