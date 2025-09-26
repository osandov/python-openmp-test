# Copyright (c) Meta Platforms, Inc. and affiliates.
# SPDX-License-Identifier: LGPL-2.1-or-later

import os
from threading import Condition, Thread

import myomp

print("-", end="", flush=True)
NUM_THREADS = 12
condition = Condition()


def thread_func():
    with condition:
        condition.wait()


try:
    threads = [Thread(target=thread_func) for _ in range(NUM_THREADS)]
    for thread in threads:
        thread.start()
finally:
    with condition:
        condition.notify_all()
    for thread in threads:
        thread.join()

print("_", flush=True)

pid = os.fork()
if pid == 0:
    os._exit(0)
else:
    _, wstatus = os.waitpid(pid, 0)
    assert os.WIFEXITED(wstatus)
    assert os.WEXITSTATUS(wstatus) == 0
