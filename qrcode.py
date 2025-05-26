import qrcode
# taking upi id as a input
upi_id = input("enter your upi id = ")

#upi: //pay?pa=upi_id&apn=name&am=amount&cu=CURRENCY&tn=MESSAGE

#defining the payment URL based on the UPI ID  the payment app 
# you can modify URLs based on the payment apps you want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=recipient%20name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=recipient%20name&mc=1234'
googlepay_url = f'upi://pay?pa={upi_id}&pn=recipient%20name&mc=1234'

#create qrcode each payment app 
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# save the qrcode to image file (optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

