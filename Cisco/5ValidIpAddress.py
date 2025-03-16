import re


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if "." in queryIP:
            octets = queryIP.split(".")
            if len(octets) != 4:
                return "Neither"
            if any(octet.startswith("0") and len(octet) != 1 for octet in octets):
                return "Neither"
            if any(
                not octet.isdecimal() or not (0 <= int(octet) < 2**8)
                for octet in octets
            ):
                return "Neither"
            return "IPv4"

        if ":" in queryIP:
            hextets = queryIP.split(":")
            if len(hextets) != 8:
                return "Neither"
            hextet_re = re.compile(r"^[0-9a-fA-F]{1,4}$")
            if any(not hextet_re.fullmatch(hextet) for hextet in hextets):
                return "Neither"
            return "IPv6"

        return "Neither"
