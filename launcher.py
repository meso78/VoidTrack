from .core import VoidTrackCore

class Voidtrack:
    def __init__(self):
        self.engine = VoidTrackCore()
    
    def show_menu(self):
        while True:
            self.engine.display_banner()
            print("\n" + "="*50)
            print("VOIDTRACK MAIN MENU")
            print("1. Track IP/Domain")
            print("2. Scan Ports")
            print("3. Packet Sniffer (Requires sudo)")
            print("4. Exit")
            
            choice = input("Select [1-4]: ").strip()
            
            if choice == "1":
                target = input("Enter IP/Domain: ")
                self.engine.track_target(target)
            elif choice == "2":
                self.run_port_scan()
            elif choice == "3":
                self.run_sniffer()
            elif choice == "4":
                break
            input("\nPress Enter to continue...")

    def run_port_scan(self):
        target = input("Target IP/Domain: ")
        ports = input("Ports (e.g., 80 or 1-1000): ") or "1-1024"
        self.engine.scan_target(target, ports)

    def run_sniffer(self):
        print("\n" + "!"*50)
        print("WARNING: Packet sniffing requires root privileges")
        print("!"*50 + "\n")
        interface = input("Network interface [eth0]: ") or "eth0"
        duration = input("Duration (seconds) [30]: ") or "30"
        self.engine.start_sniffer(interface=interface, duration=int(duration))

if _name_ == "_main_":
    interface = Voidtrack()
    interface.show_menu()