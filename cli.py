from .core import VoidTrackCore
import argparse

class VoidtrackCLI(VoidtrackCore):
    def __init__(self):
        super().__init__()
        self.parser = argparse.ArgumentParser(
            description="Voidtrack - Advanced Cybersecurity Toolkit",
            formatter_class=argparse.RawTextHelpFormatter
        )
        self._setup_commands()
    def _setup_commands(self):
        subparsers = self.parser.add_subparsers(dest="command")

        # IP Tracker
        ip_parser = subparsers.add_parser("ip", help="Track IP addresses")
        ip_parser.add_argument("target", help="IP or domain to track")

        # Port Scanner
        scan_parser = subparsers.add_parser("scan", help="Scan ports")
        scan_parser.add_argument("target", help="IP or domain to scan")
        scan_parser.add_argument("-p", "--ports", help="Port range (e.g., 1-1000)")

    def run(self):
        args = self.parser.parse_args()
        self.display_banner()
        
        if args.command == "ip":
            self._track_ip(args.target)
        elif args.command == "scan":
            self._scan_ports(args.target, args.ports)

    def _track_ip(self, target):
        from .modules.ip_tracker import IPTracker
        tracker = IPTracker()
        tracker.track(target)

    def _scan_ports(self, target, ports):
        from .modules.port_scanner import PortScanner
        scanner = PortScanner()
        scanner.scan(target, ports or "1-1024")

if _name_ == "_main_":
    cli = VoidtrackCLI()
    cli.run()