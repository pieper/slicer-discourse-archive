---
topic_id: 21430
title: "Issues When Calling Another Python Environment In A Cli Modu"
date: 2022-01-12
url: https://discourse.slicer.org/t/21430
---

# Issues when calling another python environment in a CLI module

**Topic ID**: 21430
**Date**: 2022-01-12
**URL**: https://discourse.slicer.org/t/issues-when-calling-another-python-environment-in-a-cli-module/21430

---

## Post #1 by @Mathieu_Leclercq (2022-01-12 23:52 UTC)

<p>Hello,<br>
I am developing an extension for Slicer that offers a GUI for runnning 3D surface segmentation. The GUI and the segmentation algorithm both work fine separately, but I need to call my own python environment in the extension code to start the process automatically. The idea is to execute in a scripted cli module a command with os.system() that runs the segmentation program in the right environment. I was able to make it work on a local environment on my machine, even when both python versions are different. But there are errors when trying to do it from Slicer’s Python. At first I had issues because __sysconfingdata__linux_x86_64-linux-gnu.py file was missing. I followed the instructions written on page 394 of <a href="https://readthedocs.org/projects/slicer/downloads/pdf/latest/" rel="noopener nofollow ugc">3D Slicer documentation</a>, but now the error that I get is “AssertionError: SRE module mismatch”. I added a wrapper script (bash script) to try and fix the issue but I still get the same error:</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “/path/to/segmentationfile/segmentation_code.py”, line 16, in <br>
import argparse<br>
File “/tools/Slicer4/Slicer-4.13.0-2021-09-18-linux-amd64/lib/Python/lib/python3.6/argparse.py”, line 89, in <br>
import re as _re<br>
File “/tools/Slicer4/Slicer-4.13.0-2021-09-18-linux-amd64/lib/Python/lib/python3.6/re.py”, line 123, in <br>
import sre_compile<br>
File “/tools/Slicer4/Slicer-4.13.0-2021-09-18-linux-amd64/lib/Python/lib/python3.6/sre_compile.py”, line 17, in <br>
assert _sre.MAGIC == MAGIC, “SRE module mismatch”<br>
AssertionError: SRE module mismatch</p>
</blockquote>
<p>As you can see python looks for argparse.py in the Slicer Python library, even though I explicitely provide another python path when executing the segmentation script.<br>
One thing to note is that I don’t have this issue when running the same command from my main scripted module. The script for the segmentation runs without error. However I need this to work through a CLI module in order for the GUI to not freeze while the script is running.</p>

---

## Post #2 by @pieper (2022-01-13 00:46 UTC)

<p>You can use <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L3012-L3043"><code>slicer.util.launchConsoleProcess(args)</code></a> instead of <code>os.system</code> to use your native environment instead of the Slicer one.</p>

---
