import malmo_bootstrap
import argparse

parser = argparse.ArgumentParser(
    prog='malmoext',
    description='Launches one or more Malmo Minecraft instances that can be used to run scenarios')
parser.add_argument(
        '--ports',
        nargs='+',
        default=['10000'],
        help='(Optional) List of ports that determine the number of Malmo Minecraft instances to spawn,'
                + 'and where they should run. Defaults to 10000, implying one instance running on port 10000.')
args = parser.parse_args()

ports = list(map(int, args.ports))
malmo_bootstrap.start(ports)