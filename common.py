from datetime import datetime
import subprocess

from humanize import naturaldelta
import psutil
from psutil import Process
import os
import signal


def convert_to_GB( input_bytes ):
	return round(input_bytes / (1024 * 1024 * 1024), 1)


def kill_proc_tree(
		pid, sig=signal.SIGTERM, include_parent=True, timeout=None, on_terminate=None
		):
	"""Kill a process tree (including grandchildren) with signal
    "sig" and return a (gone, still_alive) tuple.
    "on_terminate", if specified, is a callback function which is
    called as soon as a child terminates.
    """
	if pid == os.getpid():
		raise RuntimeError("I refuse to kill myself")
	parent = psutil.Process(pid)
	children = parent.children(recursive=True)
	if include_parent:
		children.append(parent)
	for p in children:
		p.send_signal(sig)
	gone, alive = psutil.wait_procs(children, timeout=timeout, callback=on_terminate)
	return (gone, alive)


def get_list_of_py( only_alias=False ) -> [psutil.Process, str]:
	process_list: [psutil.Process] = psutil.process_iter()
	for p in process_list:
		if p.name().startswith("python") or p.name().startswith("telegram-bot-api"):
			if only_alias:
				try:
					yield p.cmdline()[-1]
				except IndexError:
					continue
			else:
				yield p


def get_full_info( given_alias: str ) -> Process:
	for process in get_list_of_py():
		if given_alias == process.cmdline()[-1]:  # assume alias is the last arg
			return process


def start_program( path, arg ):
	"""
    Activates the virtualenv 'env' inside path and executes the arg

    :param path: path of the program's dir
    :param arg:
    :return:
    """
	cmd = f"source env/bin/activate; nohup {arg} &"
	subprocess.Popen(cmd, shell=True, cwd=path, executable="/bin/bash")


def str_uptime( secs: float ):
	return naturaldelta(secs)


def update_repo( path ):
	"""
    Fetches the latest update of the repo located at path

    :param path:
    :return:
    """
	cmd = "git pull"
	try:
		return {"exit-code": 0,
		        "output": subprocess.check_output(
			        cmd, shell=True, cwd=path,
			        executable="/bin/bash", universal_newlines=True)
		        }
	except subprocess.CalledProcessError as e:
		return {"exit-code": e.returncode, "output": e.stderr}
