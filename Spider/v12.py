from urllib import request


if __name__ == '__main__':

    url = "http://www.renren.com/965187997/profile"

    headers = {
        "Cookie": "anonymid=jfosp2p2-48i1hh; depovince=BJ; _r01_=1; jebe_key=f2e12094-303b-4171-900f-ed304e5a5ba1%7C7629e5c8e0f7f334244eb5436ef05a2c%7C1523070488659%7C1%7C1523070515670; wp_fold=0; jebecookies=a201c15f-9745-40fc-9d32-7112f8cf849f|||||; ick_login=cbfe66e0-743c-46a4-a956-7d692056361d; _de=420A8DC764CD1624FC7C8526DA9A3A25; p=db36f5ff987e7e58c901f6194a22b7007; first_login_flag=1; ln_uact=13119144223; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=1b2976196819d4a57127f5b87ac495f77; societyguester=1b2976196819d4a57127f5b87ac495f77; id=965187997; xnsid=61e9001d; __utma=151146938.742687335.1523070758.1523070758.1523070758.1; __utmc=151146938; __utmz=151146938.1523070758.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=151146938.1.10.1523070758; ver=7.0; loginfrom=null; JSESSIONID=abcIxsy_d_tR06bwXfEkw; _urm_965187997=21"
    }


    req = request.Request(url, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()


    with open("rsp.html", "w") as f:
        f.write(html)
