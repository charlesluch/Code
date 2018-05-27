Popen.wait(timeout=60)

# from the docs
proc = subprocess.Popen(...)
try:
    outs, errs = proc.communicate(timeout=60)
except TimeoutExpired:
    proc.kill()
    outs, errs = proc.communicate()
