from rich.table import Table
from rich.live import Live
from rich.panel import Panel
import time

class ScanStats:

    def __init__(self, total):

        self.total = total
        self.scanned = 0
        self.laravel = 0
        self.misconfig = 0
        self.start = time.time()

    def update_scanned(self):
        self.scanned += 1

    def update_laravel(self):
        self.laravel += 1

    def update_misconfig(self):
        self.misconfig += 1

    def render(self):

        elapsed = time.time() - self.start
        speed = round(self.scanned / elapsed, 2) if elapsed else 0

        table = Table.grid()

        table.add_row("Targets", str(self.total))
        table.add_row("Scanned", str(self.scanned))
        table.add_row("Laravel", str(self.laravel))
        table.add_row("Misconfig", str(self.misconfig))
        table.add_row("Speed", f"{speed} req/s")

        return Panel(table, title="Scan Dashboard")
