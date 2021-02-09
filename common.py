import subprocess

import psutil
from psutil import Process
import os
import signal


def kill_proc_tree(pid, sig=signal.SIGTERM, include_parent=True,
                   timeout=None, on_terminate=None):
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
    gone, alive = psutil.wait_procs(children, timeout=timeout,
                                    callback=on_terminate)
    return (gone, alive)


def get_list_of_py(only_alias = False) -> list:
    process_list: [psutil.Process] = psutil.process_iter()
    for p in process_list:
        if p.name().startswith('python'):
            if only_alias:
                try:
                    yield p.cmdline()[2]
                except IndexError:
                    continue
            else:
                yield p


def get_full_info(given_alias: str) -> Process:
    for process in get_list_of_py():
        if given_alias == process.cmdline()[-1]:  # assume alias is the last arg
            return process


def start_program(path, arg):
    """
    Activates the virtualenv 'env' inside path and executes the arg

    :param path: path of the program's dir
    :param arg:
    :return:
    """
    cmd = f'source env/bin/activate; {arg}'
    subprocess.Popen(cmd, shell=True,
                     cwd=path,
                     executable='/bin/bash')


def update_repo(path):
    """
    Fetches the latest update of the repo located at path

    :param path:
    :return:
    """
    cmd = 'git pull'
    return subprocess.check_output(cmd, shell=True,
                                   cwd=path,
                                   executable='/bin/bash',
                                   universal_newlines=True)
