

def call():
    print('Calling')
    return 'Call Done'


class Phone:
    price = 20000
    color = 'Black'
    brand = "Nokia"
    features = ['camera', 'speaker', 'Hatori']

    def call(self):
        print('Calling Person - 1')

    def send_sms(self, phone, sms):
        text = f'Sending SMS to: {phone} and message: {sms}'
        return text


my_phone = Phone()
print(my_phone.brand)
my_phone.call()
res = my_phone.send_sms(5566, 'Hello there')
print(res)
