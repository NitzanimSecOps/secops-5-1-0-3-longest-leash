# Paste your RouteEntry and RoutingTable from 5.1.0.2 here, then add the two new methods.


class RouteEntry:
    def __init__(self, network: str, mask: str, next_hop: str | None, interface: str):
        pass


class RoutingTable:
    def __init__(self):
        pass

    def add_route(self, entry: RouteEntry) -> None:
        pass

    def __str__(self) -> str:
        pass

    def ip_matches_route(self, ip_address: str, route_entry: RouteEntry) -> bool:
        pass

    def lookup(self, dst_ip: str) -> RouteEntry | None:
        pass
