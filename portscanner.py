# SCRIPT CODED BY SHEHAN SULAKSHANA
# FOLLOW ME ON GITHUB & IF YOU ARE SATISFIED, STAR MY REPOSITORIES ❤️


#port scanner func with error handling
def scan(port ,target ):

    try:
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        sock.settimeout(0.5)

        if sock.connect_ex((target , port)) == 0:
            sock.close()
            try :
                service = socket.getservbyport(port, "tcp")
                print(f"\r {Fore.GREEN}[+] Port {port} is open :: Service --> {service} {Style.RESET_ALL}")
                open_ports.append(str(str(port) + " : " + service))
            except Exception :
                print(f"\r {Fore.GREEN}[+] Port {port} is open :: Service --> {Fore.YELLOW}unknown {Style.RESET_ALL}")
                open_ports.append(str(str(port)+ " : "+ "unknown"))

    except Exception as e:
        print(f"\n {Fore.RED}[ERR] Error occured : {e}{Style.RESET_ALL}")


# Save data on a txt file
def save():
    with open("open-ports.txt","w") as f:
        for op in open_ports :
            f.write(op + "\n")
    print(f"\n{Fore.GREEN}[#]{Fore.CYAN} Open port list & services saved in \"open-ports.txt\" {Style.RESET_ALL}")


#main func
def main():
    print(f"{Fore.RED}{'*'*75}{Style.RESET_ALL}")
    print(Fore.RED + pyfiglet.figlet_format("PORT SCANNER", font='Standard'))
    print(f"{Style.BRIGHT}{Back.BLACK}{Fore.LIGHTWHITE_EX}[+]{Fore.BLUE} Script By Shehan Sulakshana {Style.RESET_ALL}")
    print(f"{Style.BRIGHT}{Back.BLACK}[+]{Fore.BLUE} GITHUB : https://github.com/ShehanSulakshana {Style.RESET_ALL} \n")
    print(f"{Fore.RED}{'*'*75}{Style.RESET_ALL}")

    #host or ip input with validations
    while True:
        try:
            target = input("\n[*] Enter target host (IP or domain) : ").strip()
            target = socket.gethostbyname(target)
            break
        except Exception:
            print(f"\n {Fore.RED}[ERR] Enter valid inputs{Style.RESET_ALL}")


    #port range inputs with validations
    while True:
        try :
            print (f"\n[*] Enter the port range (1-65535 ports available) ")
            startP = int(input(" -> Start : "))
            endP = int(input(" -> End   : "))
            if startP != 0 and startP<endP and endP<=65535 and startP<65535:  # validation
                break
            else :
                print(f"\n {Fore.RED}[ERR] Enter valid inputs{Style.RESET_ALL}")
        except ValueError:
            print(f"\n {Fore.RED}[ERR] Enter valid inputs{Style.RESET_ALL}")
        except Exception as e :
            print(f"\n {Fore.RED}[ERR] Error occured : {e}{Style.RESET_ALL}")

    StartTime = time.time() #scan start

    global open_ports
    open_ports = []     #Define open port list as a global list

    #looping through the ports with halo scan animation
    print(f"\n{Fore.GREEN}[#]{Fore.CYAN} Scan {target} from port {startP} to {endP} >>> {Style.RESET_ALL}\n")
    with Halo(text='Scanning...', spinner='dots'):
        for port in range(startP , endP+1):
            scan(port ,target)

    EndTime = time.time() #scan end

    #FINISH
    print (f"\n{Fore.GREEN}[#]{Fore.CYAN} Scan Completed")
    print (f"{Fore.GREEN}[#]{Fore.CYAN} Scanned {str((endP-startP)+1)} ports in {str(round(EndTime-StartTime , 2))} seconds.{Style.RESET_ALL}")

    #FINAL ACTION
    action = input("\n[*] Save & Exit ? (y/n) :").lower().strip()
    if action == "y":
        save()
        sys.exit(f"\n{Back.BLACK}{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX} <============= {Fore.LIGHTRED_EX}Thank YOU !!! , {Fore.LIGHTYELLOW_EX}Don't forget to follow me on Github {Fore.LIGHTMAGENTA_EX}=============> {Style.RESET_ALL}")
    else :
        sys.exit(f"\n{Back.BLACK}{Style.BRIGHT}{Fore.LIGHTMAGENTA_EX} <============= {Fore.LIGHTRED_EX}Thank YOU !!! , {Fore.LIGHTYELLOW_EX}Don't forget to follow me on Github {Fore.LIGHTMAGENTA_EX}=============> {Style.RESET_ALL}")


if __name__ == '__main__':
    import sys, socket, pyfiglet ,time
    from colorama import Fore, Back, Style
    from halo import Halo

    main()