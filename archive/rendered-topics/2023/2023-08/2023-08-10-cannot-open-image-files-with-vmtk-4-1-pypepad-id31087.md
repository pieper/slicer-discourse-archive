---
topic_id: 31087
title: "Cannot Open Image Files With Vmtk 4 1 Pypepad"
date: 2023-08-10
url: https://discourse.slicer.org/t/31087
---

# Cannot open image files with VMTK 4.1 PypePad

**Topic ID**: 31087
**Date**: 2023-08-10
**URL**: https://discourse.slicer.org/t/cannot-open-image-files-with-vmtk-4-1-pypepad/31087

---

## Post #1 by @am_49 (2023-08-10 14:32 UTC)

<p>Operating system: Windows 10<br>
Slicer version:<br>
Expected behavior: Reading image files with no errors.<br>
Actual behavior: I just installed VMTK 1.4 via Miniconda in a separate environment. Double clicking on a desktop shortcut opens PypePad. On an attempt to using its File|Open tabs to load .nii or .dcm files, error messages come up on the terminal window, like these ones:</p>
<p>Exception in Tkinter callback<br>
Traceback (most recent call last):<br>
File “C:\Users\Ja\miniconda3\envs\vm\lib\tkinter_<em>init</em>_.py”, line 1558, in <strong>call</strong><br>
return self.func(*args)<br>
File “C:\Users\Ja\miniconda3\envs\vm\lib\site-packages\vmtk\pypepad.py”, line 114, in OpenCommand<br>
for line in openfile.readlines():<br>
File “C:\Users\Ja\miniconda3\envs\vm\lib\encodings\cp1250.py”, line 23, in decode<br>
return codecs.charmap_decode(input,self.errors,decoding_table)[0]<br>
UnicodeDecodeError: ‘charmap’ codec can’t decode byte 0x90 in position 381: character maps to </p>
<p>I reinstalled VMTK few times, using Python 5, Python 6, and a binary Windows installer to no avail. The sys.getdefaultencoding() run on Python returns ‘utf8’.</p>
<p>Please help.</p>

---
