# SlicerPreview: python default encoding is troublesome. Is it generally observed?

**Topic ID**: 43826
**Date**: 2025-07-23
**URL**: https://discourse.slicer.org/t/slicerpreview-python-default-encoding-is-troublesome-is-it-generally-observed/43826

---

## Post #1 by @chir.set (2025-07-23 15:38 UTC)

<p>Hello,</p>
<p>On starting SlicerPreview 33801 on Arch Linux, a very long list of decoding errors related to python appears in stdout. The last ones are as below:</p>
<pre><code class="lang-auto">  File "/opt/programs/Test/Slicer-5.9.0-2025-07-22-linux-amd64/lib/Python/lib/python3.12/site-packages/numpy/testing/_private/utils.py", line 1387, in check_support_sve
    output = subprocess.run(cmd, capture_output=True, text=True)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/programs/Test/Slicer-5.9.0-2025-07-22-linux-amd64/lib/Python/lib/python3.12/subprocess.py", line 550, in run
    stdout, stderr = process.communicate(input, timeout=timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/programs/Test/Slicer-5.9.0-2025-07-22-linux-amd64/lib/Python/lib/python3.12/subprocess.py", line 1209, in communicate
    stdout, stderr = self._communicate(input, endtime, timeout)
                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/programs/Test/Slicer-5.9.0-2025-07-22-linux-amd64/lib/Python/lib/python3.12/subprocess.py", line 2153, in _communicate
    stdout = self._translate_newlines(stdout,
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/programs/Test/Slicer-5.9.0-2025-07-22-linux-amd64/lib/Python/lib/python3.12/subprocess.py", line 1086, in _translate_newlines
    data = data.decode(encoding, errors)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc2 in position 12: ordinal not in range(128)
decoding with 'ANSI_X3.4-1968' codec failed
Switch to module:  "Volumes"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
NameError: name 'loadSlicerRCFile' is not defined
Switch to module:  ""
Switch to module:  ""
</code></pre>
<p>Slicer is not usable: no view is available in the default layout though one can be selected, python modules are not loaded, slicerrc is not loaded… nothing python is available.</p>
<p>If this <a href="https://discourse.slicer.org/t/slicerrt-built-from-source-cannot-start/43792/12">hack</a> is applied, an expected running Slicer is observed.</p>
<p>I wish to know:</p>
<ul>
<li>if this is observed on other Linux distributions</li>
<li>if this is observed on non-Linux operating systems.</li>
</ul>
<p>Thank you.</p>

---
