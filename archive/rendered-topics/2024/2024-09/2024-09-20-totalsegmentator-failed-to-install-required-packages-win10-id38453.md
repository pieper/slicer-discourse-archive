# TotalSegmentator: Failed to install required packages (win10)

**Topic ID**: 38453
**Date**: 2024-09-20
**URL**: https://discourse.slicer.org/t/totalsegmentator-failed-to-install-required-packages-win10/38453

---

## Post #1 by @zhang_zhixiong (2024-09-20 05:30 UTC)

<p>Failed to install Python dependencies:<br>
Command ‘[‘C:/ProgramData/slicer.org/Slicer 5.7.0-2024-09-03/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘pandas’]’ returned non-zero exit status 1.</p>

---

## Post #2 by @lassoan (2024-09-20 05:32 UTC)

<p>Please follow <a href="https://github.com/lassoan/SlicerTotalSegmentator?tab=readme-ov-file#failed-to-compute-results-error-the-first-time-trying-to-use-this-slicer-module">these instructions</a>. Thank you!</p>

---

## Post #3 by @zhang_zhixiong (2024-09-20 06:00 UTC)

<p>Computer configuration: NVIDIA GeForce RTX 4070 Ti, Intel(R) Core™ i9-10850K CPU <span class="mention">@3.60GHz</span>, 128GB RAM</p>

---

## Post #4 by @zhang_zhixiong (2024-09-20 06:03 UTC)

<p>WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by ‘SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))’: /simple/pandas/<br>
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by ‘SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))’: /simple/pandas/<br>
WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by ‘SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))’: /simple/pandas/<br>
WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by ‘SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))’: /simple/pandas/<br>
WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by ‘SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))’: /simple/pandas/<br>
Could not fetch URL <a href="https://pypi.org/simple/pandas/:" rel="noopener nofollow ugc">https://pypi.org/simple/pandas/:</a> There was a problem confirming the ssl certificate: HTTPSConnectionPool(host=‘<a href="http://pypi.org" rel="noopener nofollow ugc">pypi.org</a>’, port=443): Max retries exceeded with url: /simple/pandas/ (Caused by SSLError(SSLEOFError(8, ‘EOF occurred in violation of protocol (_ssl.c:1129)’))) - skipping<br>
ERROR: Could not find a version that satisfies the requirement pandas (from versions: none)<br>
ERROR: No matching distribution found for pandas<br>
Traceback (most recent call last):<br>
File “C:/ProgramData/slicer.org/Slicer 5.7.0-2024-09-18/slicer.org/Extensions-33015/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py”, line 717, in setupPythonRequirements<br>
import pandas<br>
ModuleNotFoundError: No module named ‘pandas’</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “C:/ProgramData/slicer.org/Slicer 5.7.0-2024-09-18/slicer.org/Extensions-33015/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py”, line 274, in onApplyButton<br>
self.logic.setupPythonRequirements()<br>
File “C:/ProgramData/slicer.org/Slicer 5.7.0-2024-09-18/slicer.org/Extensions-33015/TotalSegmentator/lib/Slicer-5.7/qt-scripted-modules/TotalSegmentator.py”, line 719, in setupPythonRequirements<br>
slicer.util.pip_install(“pandas”)<br>
File “C:\ProgramData\slicer.org\Slicer 5.7.0-2024-09-18\bin\Python\slicer\util.py”, line 3927, in pip_install<br>
_executePythonModule(“pip”, args)<br>
File “C:\ProgramData\slicer.org\Slicer 5.7.0-2024-09-18\bin\Python\slicer\util.py”, line 3888, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “C:\ProgramData\slicer.org\Slicer 5.7.0-2024-09-18\bin\Python\slicer\util.py”, line 3854, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/ProgramData/slicer.org/Slicer 5.7.0-2024-09-18/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘pandas’]’ returned non-zero exit status 1.<br>
[Python] Failed to install required packages.<br>
[Python] Command ‘[‘C:/ProgramData/slicer.org/Slicer 5.7.0-2024-09-18/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘pandas’]’ returned non-zero exit status 1.</p>

---

## Post #5 by @zhang_zhixiong (2024-09-20 06:05 UTC)

<p>I am not a computer major, do not know how to solve</p>

---

## Post #6 by @lassoan (2024-09-20 16:37 UTC)

<aside class="quote no-group" data-username="zhang_zhixiong" data-post="4" data-topic="38453">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zhang_zhixiong/48/77975_2.png" class="avatar"> zhang_zhixiong:</div>
<blockquote>
<p>EOF occurred in violation of protocol</p>
</blockquote>
</aside>
<p>Thanks, this additional information helps a lot. It is likely that your institution interferes with your internet access.</p>
<p>You can find several similar topics, see for example <a href="https://discourse.slicer.org/t/error-when-installing-matplotib-in-slicer/28141">[1]</a> and <a href="https://discourse.slicer.org/t/about-using-totalsegmentator/34539/3">[2]</a>.</p>
<p>Probably the simplest solution is to install Slicer and extensions on a computer with proper internet access and then copy that Slicer to the computers where you need to use it. Slicer is fully portable, so if you only copy the Slicer installation folder and downloaded TotalSegmentator weights from your user folder then it should all work.</p>

---

## Post #7 by @zhang_zhixiong (2024-09-23 03:22 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/4/f4a27cb7ada0224890da25083d6aa88b3ad2912a.png" alt="bug" data-base62-sha1="yU8D3zE2Eq3sZFpv2jOiEmZnsGS" width="482" height="388"></p>
<p>I find PyTorch doesn’t seem to be installed. How can I fix it</p>

---

## Post #8 by @lassoan (2024-09-23 03:27 UTC)

<p>You can choose a GPU (cuda) computation backend and click install.</p>
<p>However, since you seem to have an internet connectivity issue, you need to do this on a different computer or ask help from local IT personnel to get usable internet connection.</p>

---

## Post #9 by @zhang_zhixiong (2024-09-23 03:59 UTC)

<p>My network can get online, are you talking about my 3D slicer network connection problem? How to fix it?</p>

---

## Post #10 by @lassoan (2024-09-23 04:21 UTC)

<p>It is not a 3D Slicer network connection problem, but an issue with your computer network settings (e.g., invalid/temporary SSL certificates issued by Zscaler or similar network security software on your computer) or your internet connection (e.g., aggressive proxy server preventing internet access of applications).</p>

---

## Post #11 by @zhang_zhixiong (2024-09-23 05:44 UTC)

<p>Ouch! How to solve this problem? Please give me some Pointers! So how do you do that?</p>

---
