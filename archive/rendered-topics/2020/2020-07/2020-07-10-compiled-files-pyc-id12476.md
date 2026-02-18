# Compiled files .pyc

**Topic ID**: 12476
**Date**: 2020-07-10
**URL**: https://discourse.slicer.org/t/compiled-files-pyc/12476

---

## Post #1 by @ada (2020-07-10 09:30 UTC)

<p>Hello all,</p>
<p>With Slicer4.10.2 I was able to launch custom compiled python files (.pyc).<br>
Nevertheless with the 4.11 version it is no more working (maybe induced by python3).<br>
I have the following error :</p>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “XXXX\Python\Lib\imp.py”, line 170, in load_source<br>
module = _exec(spec, sys.modules[name])<br>
File “”, line 618, in _exec<br>
File “”, line 678, in exec_module<br>
File “”, line 219, in _call_with_frames_removed<br>
File “XXXX”, line XXXX, in <br>
import XXXX as XXXX<br>
ImportError: bad magic number in ‘XXXX’: b’B\r\r\n’</p>
<p>Is anyone know how to do ?<br>
Thank you,<br>
Best</p>

---
