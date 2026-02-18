# How to run python .py file from windows terminal

**Topic ID**: 28740
**Date**: 2023-04-04
**URL**: https://discourse.slicer.org/t/how-to-run-python-py-file-from-windows-terminal/28740

---

## Post #1 by @mukund_shah (2023-04-04 06:55 UTC)

<p>Slicer.exe --python-script “/full/path/to/myscript.py” --no-splash --no-main-window i am using this command in windows terminal but its showing error<br>
<strong>The command Slicer.exe was not found, but does exist in the current location. Windows PowerShell does not load commands from the current location by default.</strong></p>
<p>I am going to place where my slicer exe file is i.e <strong>C:\Users\mukun\AppData\Local\NA-MIC\Slicer 4.11.20210226</strong> but its still not working ,kindly tell what am i doing wrong here?</p>

---

## Post #2 by @rbumm (2023-04-04 07:03 UTC)

<p>Provide the full path to Slicer.exe between quotes in your script command or add the 3D Slicer home folder to your PATH variable (if you work on Windows).</p>

---

## Post #3 by @mukund_shah (2023-04-04 07:05 UTC)

<p>I did give this which is the full path r"E:\research_ppr\slicer_path_to_markup.py"</p>

---

## Post #4 by @rbumm (2023-04-04 07:12 UTC)

<p>Add something like “C:\Users\yourname\AppData\Local\NA-MIC\Slicer 5.2.2\Slicer.exe”, depending on where you installed Slicer, to your script …</p>

---

## Post #5 by @mukund_shah (2023-04-04 08:46 UTC)

<p>Thanks ,the first only worked ,my mistake was I was not using command prompt of anaconda navigator</p>

---
