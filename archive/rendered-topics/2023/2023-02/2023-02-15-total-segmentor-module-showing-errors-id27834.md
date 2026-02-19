---
topic_id: 27834
title: "Total Segmentor Module Showing Errors"
date: 2023-02-15
url: https://discourse.slicer.org/t/27834
---

# Total segmentor module showing errors

**Topic ID**: 27834
**Date**: 2023-02-15
**URL**: https://discourse.slicer.org/t/total-segmentor-module-showing-errors/27834

---

## Post #1 by @Newbie-segmentor (2023-02-15 20:46 UTC)

<p>Operating system: Windows 10 Enterprise<br>
Slicer version: 5.2.1<br>
Expected behavior: Automated segmentation of organs<br>
Actual behavior: Showing errors everytime</p>

---

## Post #2 by @lassoan (2023-02-15 20:48 UTC)

<p>If you want to get help to resolve the errors then you need to be more specific, such as copy here the displayed error messages and give us information about your system (GPU model, CUDA version, etc.).</p>

---

## Post #3 by @Newbie-segmentor (2023-02-15 20:43 UTC)

<p>Hello,</p>
<p>I have tried using total segmentor module several times, but failed.<br>
<strong>Error says:</strong><br>
Traceback (most recent call last):<br>
File “C:\Users\singhs40\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 2961, in tryWithErrorDisplay<br>
yield<br>
File “C:/Users/singhs40/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 248, in onApplyButton<br>
self.logic.setupPythonRequirements()<br>
File “C:/Users/singhs40/AppData/Local/NA-MIC/Slicer 5.2.1/NA-MIC/Extensions-31317/TotalSegmentator/lib/Slicer-5.2/qt-scripted-modules/TotalSegmentator.py”, line 524, in setupPythonRequirements<br>
slicer.util.pip_install(totalSegmentatorPackage + (" --upgrade" if upgrade else “”))<br>
File “C:\Users\singhs40\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 3571, in pip_install<br>
_executePythonModule(‘pip’, args)<br>
File “C:\Users\singhs40\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 3533, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “C:\Users\singhs40\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py”, line 3502, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command '[‘C:/Users/singhs40/AppData/Local/NA-MIC/Slicer 5.2.1/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, '<a href="https://github.com/wasserth/TotalSegmentator/archive/master.zip'%5D'" rel="noopener nofollow ugc">https://github.com/wasserth/TotalSegmentator/archive/master.zip’]’</a> returned non-zero exit status 1.</p>
<p>I tried to uninstall and re-install PyTorch by CPU, have installed Git and it shows the same error.</p>
<p>Thank you</p>

---

## Post #5 by @lassoan (2023-02-15 20:52 UTC)

<p>Please exit Slicer and run this command in a Windows command prompt to see some more details:</p>
<p><code>C:\Users\singhs40\AppData\Local\NA-MIC\Slicer 5.2.1\bin\PythonSlicer.EXE -m pip install https://github.com/wasserth/TotalSegmentator/archive/master.zip --upgrade</code></p>

---

## Post #6 by @Newbie-segmentor (2023-02-15 20:54 UTC)

<p>GPU: NVIDIA Quadro P400<br>
Following your command and replying. Thanks</p>

---

## Post #7 by @Newbie-segmentor (2023-02-15 20:58 UTC)

<p>This is the error command prompt shows:</p>
<p>ERROR: Could not install packages due to an OSError: HTTPSConnectionPool(host=‘<a href="http://codeload.github.com" rel="noopener nofollow ugc">codeload.github.com</a>’, port=443): Max retries exceeded with url: /wasserth/TotalSegmentator/zip/refs/heads/master (Caused by SSLError(SSLCertVerificationError(1, ‘[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1129)’)))</p>

---

## Post #8 by @lassoan (2023-02-15 21:01 UTC)

<p>It seems that your computer has some problems with SSL certifications, maybe some overly aggressive corporate proxy server/firewall. You can search the web for <code>certificate verify failed: self signed certificate in certificate chain</code> or ask your IT administators for help.</p>

---

## Post #9 by @Newbie-segmentor (2023-02-15 21:03 UTC)

<p>Yes, it is an aggressive firewall. How to proceed if I get help of administrators?</p>

---
