import requests
import re
import url_target
import send_mail


def check_bb(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'}
    response = requests.get(url, headers=headers)
    res_str = str(response.content)
    sold_out = re.search(">Sold Out</button>", res_str)
    webpage_status = re.search("2-Year Accidental Geek",res_str)
    if (sold_out!=0) & (webpage_status!=0):
        sold_out = True
    if (sold_out == 0) & (webpage_status !=0):
        sold_out = False
    if webpage_status == 0:
        raise Exception("Error! Need Human Verification")
    in_stock = not sold_out
    return in_stock


def check_wm(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'}
    response = requests.get(url, headers=headers)
    res_str = str(response.content)
    sold_out = re.search("prod-blitz-copy-message\">This item is <b>out of stock</b>.", res_str)
    webpage_status = re.search("<span itemprop=\"name\">Video Games</span>",res_str)
    if (sold_out!=0) & (webpage_status!=0):
        sold_out = True
    if (sold_out == 0) & (webpage_status !=0):
        sold_out = False
    if webpage_status == 0:
        raise Exception("Error! Need Human Verification")
    in_stock = not sold_out
    return in_stock


def main():
    status1 = check_bb(url_target.BB_PS5)
    status2 = check_bb(url_target.BB_PS5DE)
    status3 = check_wm(url_target.WM_PS5)
    status4 = check_wm(url_target.WM_PS5DE)

    stock_list = []
    if status1:
        stock_list.append("BestBuy has PS5 Console Now; ")
    if status2:
        stock_list.append("BestBuy has PS5 Digital Now; ")
    if status3:
        stock_list.append("Walmart has PS5 Console Now; ")
    if status4:
        stock_list.append("Walmart has PS5 Digital Now; ")

    str1_mail = " "

    if len(stock_list) == 0:
        print("Out stock for all")
    else:
        for i in stock_list:
            str1_mail = str1_mail + i

        mail_text = "PS5 in Stock! " + str1_mail
        send_mail.send_mail(url_target.receiver, mail_text)


if __name__ == "__main__":
    main()