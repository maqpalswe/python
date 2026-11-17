
import urllib.request
import urllib.parse
import json
import time

TOKEN = ""
URL = "https://api.telegram.org/bot" + TOKEN + "/"

# TELEGRAM MENEN BAYLANÍSATUǴÍN FUNKCIYA
def bot(method, params):
    data = urllib.parse.urlencode(params).encode()
    with urllib.request.urlopen(URL + method, data, timeout=40) as r:
        return json.loads(r.read().decode())


# XABAR JIBERIW FUNKCIYASÍ
def xabar_jiberiw(kimge, tekst):
    bot("sendMessage", {"chat_id": kimge, "text": tekst})


# XABARLARDÍ ALÍW FUNKCIYASÍ
def xabarlardi_aliw(hazirgi_offset):
    natiyje = bot("getUpdates", {
        "offset": hazirgi_offset,
        "timeout": 30
    })
    return natiyje["result"]


# BOTTÍŃ TIYKARǴÍ BÓLIMI
offset = 0
print("BOT ISKE TÚSTI!")

while True:
    try:
        jana_xabarlar = xabarlardi_aliw(offset)

        for xabar in jana_xabarlar:
            offset = xabar["update_id"] + 1

            if "message" not in xabar:
                continue

            if "text" in xabar["message"]:
                user_id = xabar["message"]["from"]["id"]
                first_name = xabar["message"]["from"]["first_name"]
                tekst = xabar["message"]["text"]

                print(f"{first_name} jazdi: {tekst}")

                # ===== 6 TAPSÍRMA =====

                bolimler = tekst.split(" ", 1)

                if len(bolimler) < 2:
                    xabar_jiberiw(
                        user_id,
                        "Tapsırma nomerin hám tekstti jazıń!\n"
                        "Mısal: 1 Qaraqalpaqstan"
                    )
                    continue

                nomer = bolimler[0]
                malimat = bolimler[1]

                # 1. TEKSTTI KERI SHÍǴARÍW
                if nomer == "1":
                    juwap = malimat[::-1]
                    xabar_jiberiw(user_id, juwap)

                # 2. HÁRIPLERDI ÚLKEN ETIW
                elif nomer == "2":
                    juwap = malimat.upper()
                    xabar_jiberiw(user_id, juwap)

                # 3. BELGILER SANÍN ANÍQLAW
                elif nomer == "3":
                    juwap = len(malimat)
                    xabar_jiberiw(
                        user_id,
                        f"Tekstte {juwap} belgi bar."
                    )

                # 4. SANNÍŃ KVADRATÍN ESAPLAW
                elif nomer == "4":
                    try:
                        san = int(malimat)
                        kvadrat = san * san
                        xabar_jiberiw(
                            user_id,
                            f"{san} * {san} = {kvadrat}"
                        )
                    except ValueError:
                        xabar_jiberiw(
                            user_id,
                            "Iltimas, pútin san kirgiziń!"
                        )

                # 5. ATTÍ 5 MÁRTE SHÍǴARÍW
                elif nomer == "5":
                    juwap = malimat * 5
                    xabar_jiberiw(user_id, juwap)

                # 6. BOS ORÍNLARDÍ DEFIСKE ALMASTÍRÍW
                elif nomer == "6":
                    juwap = malimat.replace(" ", "-")
                    xabar_jiberiw(user_id, juwap)

                else:
                    xabar_jiberiw(
                        user_id,
                        "1-den 6-ǵa shekem tapsırma nomerin jazıń!"
                    )

    except Exception as qate:
        print("QÁTE:", qate)
        time.sleep(3)
              
