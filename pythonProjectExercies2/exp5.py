class WebPush():
    platform = ""
    optin = bool
    global_frequency_capping = ""
    start_date =0
    end_date = 0
    language = ""
    push_type =""

    def send_push(self):
        print("push gonderildi")

class TriggerPus(WebPush):
    trigger_page = ""


class BulkPush(WebPush):
    send_date = 0


class SegmentPush(WebPush):
    segment_name = ""


class PriceAlertPush(WebPush):
    price_info = 0
    discount_rate = 0.0


    def discountPrice(self, price_info, discount_rate):
        x = price_info * discount_rate
        price_info -= x
        return price_info



class InstockPush(WebPush):
    stock_info = bool

    def stockUpdate(self,stock_info):

      if self.stock_info == True:
          return False
      else:
         return True


push1 = PriceAlertPush()
push1.push_type = "PriceAlertPush"
print('\n',"discount price: " , push1.discountPrice(10,1.1),'\n', "push type: ", push1.push_type ,'\n')
push1.send_push()

push2 = InstockPush()
push2.pus_type = "StockUpdate"
print('\n',"stock update: ",push2.stockUpdate(False),'\n' , "push type: ",push2.pus_type,'\n')
push2.send_push()