import re
import os
import platform
import socket
import subprocess
from datetime import datetime

import distro
import psutil
from screeninfo import get_monitors
from rich import box
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.align import Align


def get_uptime():
    boot_time = psutil.boot_time()
    now = datetime.now().timestamp()

    uptime_seconds = int(now - boot_time)
    days, remainder = divmod(uptime_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    uptime_str = f"{days}d {hours}h {minutes}m"
    return uptime_str


def get_shell():
    shell = os.environ.get('SHELL')
    os.path.basename(shell) if shell else 'N/A'


def get_de():
    de = os.environ.get('DESKTOP_SESSION') or os.environ.get('XDG_CURRENT_DESKTOP')
    return de if de else 'N/A'


def get_resolution():
    try:
        monitors = get_monitors()
        res = [f"{m.width}x{m.height}" for m in monitors]
        return ','.join(res)
    except Exception:
        return 'N/A'


def get_packages():
    try:
        result = subprocess.run(['dpkg', '--get-selections'],
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            packages = len([line for line in result.stdout.split('\n') if line])
            return str(packages)
        return None
    except Exception:
        return 'N/A'


def get_os():
    return distro.name(pretty=True)


def get_cpu():
    cpu = platform.processor()
    return cpu if cpu else 'N/A'


def get_ram():
    return f'{round(psutil.virtual_memory().total / 1024 ** 3)} GB'


def get_gpu():
    try:
        result = subprocess.run(['lspci'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        gpu_lines = re.findall(r'(VGA compatiable controller|3D controller): (.+)',
                               result.stdout, re.IGNORECASE)
        gpu_names = [gpu[1] for gpu in gpu_lines]
        return ','.join(gpu_names) if gpu_names else 'N/A'
    except Exception:
        return 'N/A'


def get_host():
    return socket.gethostname()


def get_kernal():
    return platform.release()

if __name__ == '__main__':
    console = Console()

    os_info = get_os()
    host = get_host()
    kernal = get_kernal()
    uptime = get_uptime()
    packages = get_packages()
    shell = get_shell()
    resolution = get_resolution()
    de = get_de()
    cpu = get_cpu()
    gpu = get_gpu()
    memory = get_ram()

    table = Table(show_header=True, box=None, padding=(0,1))

    label_color = 'bold cyan'
    value_color = 'white'

    table.add_row(Text('OS:', style=label_color), Text(os_info, style=value_color))
    table.add_row(Text('Host:', style=label_color), Text(host, style=value_color))
    table.add_row(Text('Kernal:', style=label_color), Text(kernal, style=value_color))
    table.add_row(Text('Uptime:', style=label_color), Text(uptime, style=value_color))
    table.add_row(Text('Packages:', style=label_color), Text(packages, style=value_color))
    # table.add_row(Text('Shell:', style=label_color), Text(shell, style=value_color))
    table.add_row(Text('Resolution:', style=label_color), Text(resolution, style=value_color))
    table.add_row(Text('DE/WM:', style=label_color), Text(de, style=value_color))
    table.add_row(Text('CPU:', style=label_color), Text(cpu, style=value_color))
    table.add_row(Text('GPU:', style=label_color), Text(gpu, style=value_color))
    table.add_row(Text('RAM:', style=label_color), Text(memory, style=value_color))

    logo = """
    ###### #####
    #      #    #
    #####  ##### 
    #      #    #
    ###### #####
    """

    logo_text = Text(logo, style='bold yellow')
    logo_panel = Panel.fit(logo_text, border_style='yellow', padding=(0, 2))

    layout = Table.grid(expand=True)
    layout.add_column(justify='left', ratio=1)
    layout.add_column(justify='left', ratio=4)
    layout.add_row(logo_panel, table)
    console.print(Align.left(layout))




