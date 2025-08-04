import argparse
from ssh_honeypot import honeypot
from web_honeypot import run_web_honeypot

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--address', type=str, required=True)
    parser.add_argument('-p', '--port', type=int, required=True)
    parser.add_argument('-u', '--username', type=str)
    parser.add_argument('-pw', '--password', type=str)
    parser.add_argument('-s', '--ssh', action="store_true")
    parser.add_argument('-w', '--http', action="store_true")

    args = parser.parse_args()

    try:
        if args.ssh:
            print("[-] Running SSH Honeypot...")
            honeypot(args.address, args.port, args.username, args.password)

        elif args.http:
            print("[-] Running HTTP Wordpress Honeypot...")
            if not args.username:
                args.username = "admin"
            if not args.password:
                args.password = "password"
            print(f"[+] HTTP Honeypot running on port {args.port} with Username: {args.username} Password: {args.password}")
            run_web_honeypot(args.port, args.username, args.password)

        else:
            print("[!] You must specify either SSH (-s) or HTTP (-w) honeypot mode.")

    except Exception as e:
        print(f"[!] Exception: {e}")
        print("... Exiting HONEYPOT ...")
