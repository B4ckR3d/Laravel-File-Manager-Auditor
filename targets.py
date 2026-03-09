import ipaddress

def expand_cidr(cidr):

    ips = []

    net = ipaddress.ip_network(cidr, strict=False)

    for ip in net.hosts():
        ips.append(str(ip))

    return ips


def load_targets(args):

    targets = []

    if args.target:
        targets.append(args.target)

    if args.file:
        with open(args.file) as f:
            targets.extend(f.read().splitlines())

    if args.cidr:
        targets.extend(expand_cidr(args.cidr))

    return targets
