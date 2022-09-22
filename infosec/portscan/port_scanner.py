import socket
import common_ports
import re


def get_open_ports(target, port_range, verbose=False):
    open_ports = "" if verbose else [];
    fmt = "{:<8} {:<}\n"
    ip = ""
    if is_address := re.match("\w+(\.\w+)*", target):
        try:
            (host, _, _) = socket.gethostbyaddr(target)
            if host == target:
                open_ports += f"Open ports for {host}\n"
            else:
                open_ports += f"Open ports for {host} ({target})\n"
            open_ports += fmt.format("PORT", "SERVICE")
        except socket.gaierror:
            return "Error: Invalid IP address"
    else:
        try:
            ip = socket.gethostbyname(target)
            if verbose:
                open_ports += f"Open ports for {target} ({ip})\n"
                open_ports += fmt.format("PORT", "SERVICE")
        except socket.gaierror as err:
            return "Error: Invalid ip"

    for p in range(port_range[0], port_range[1] + 1):
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(0.3)
        try:
            # This will only work for ip4, which is what the tests cover.
            # For a real application, we need more consideration.
            # See socket families: https://docs.python.org/3/library/socket.html
            if not sk.connect_ex((target, p)):
                if verbose:
                    service = common_ports.ports_and_services[p]
                    open_ports += fmt.format(p, service)
                else:
                    open_ports.append(p)
        except socket.gaierror:
            return "Error: Invalid IP address"
        finally:
            sk.close()
    open_ports = open_ports.strip() if verbose else open_ports
    return open_ports
