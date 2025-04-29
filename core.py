from colorama import Fore, Style, init

class VoidtrackCore:
    """Core system for VoidTrack cybersecurity toolkit"""
    
    def __init__(self):
        init()
        self.banner = f"""
{Fore.CYAN}
██╗   ██╗ ██████╗ ██╗██████╗  ████████╗██████╗  █████╗  ██████╗██╗  ██╗
██║   ██║██╔═══██╗██║██╔═══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
██║   ██║██║   ██║██║██║   ██║   ██║   ██████╔╝███████║██║     █████╔╝ 
╚██╗ ██╔╝██║   ██║██║██║   ██║   ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ 
 ╚████╔╝ ╚██████╔╝██║██████╔╝    ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗
  ╚═══╝   ╚═════╝ ╚═╝╚═════╝     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
{Style.RESET_ALL}
{' voidtrack '.center(60, '•')}
{' by meso blhaj '.center(60, '•')}
"""

    def display_banner(self):
        """Display the VoidTrack banner"""
        print(self.banner)

    def print_success(self, msg):
        """Print success message with timestamp"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.GREEN}[✓] [{timestamp}] {msg}{Style.RESET_ALL}")

    def print_error(self, msg):
        """Print error message with timestamp"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.RED}[✗] [{timestamp}] {msg}{Style.RESET_ALL}")

    def print_warning(self, msg):
        """Print warning message with timestamp"""
        from datetime import datetime
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"{Fore.YELLOW}[!] [{timestamp}] {msg}{Style.RESET_ALL}")

    # Add these core functions for the launcher to work
    def track_target(self, target):
        from voidtrack.modules.ip_tracker import IPTracker
        tracker = IPTracker()
        result = tracker.track(target)
        if result:
            self.print_success(f"Results for {target}:")
            for key, value in result.items():
                print(f"{key:>12}: {value}")
        return result

    def scan_target(self, target, ports):
        from voidtrack.modules.port_scanner import PortScanner
        scanner = PortScanner()
        open_ports = scanner.scan(target, ports)
        self.print_success(f"Open ports on {target}: {', '.join(map(str, open_ports)) or 'None'}")
        return open_ports

    def start_sniffer(self, interface="eth0", duration=30):
        from voidtrack.modules.packet_sniffer import PacketSniffer
        sniffer = PacketSniffer()
        sniffer.start(interface=interface, duration=duration)