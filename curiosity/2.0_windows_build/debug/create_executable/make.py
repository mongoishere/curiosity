import subprocess

run = subprocess.Popen("""setup.py build""", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

print(run.stdout.read())