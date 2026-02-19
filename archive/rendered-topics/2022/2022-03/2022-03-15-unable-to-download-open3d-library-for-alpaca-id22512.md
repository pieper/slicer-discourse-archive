---
topic_id: 22512
title: "Unable To Download Open3D Library For Alpaca"
date: 2022-03-15
url: https://discourse.slicer.org/t/22512
---

# Unable to download open3d library for ALPACA

**Topic ID**: 22512
**Date**: 2022-03-15
**URL**: https://discourse.slicer.org/t/unable-to-download-open3d-library-for-alpaca/22512

---

## Post #1 by @Khanine (2022-03-15 05:42 UTC)

<p>Hi all,</p>
<p>I am trying to run some 3D morphometrics on ALPACA (a program within slicermorph) and every time I try to run it, it tells me “ALPACA requires open3d library. Installation will take a few minutes” then a whole installation sequence takes place in python. However, I keep running into this error and I am not sure how to remedy it.</p>
<p>"ERROR: Command errored out with exit status 1: ‘C:\Users\blakk\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\python-real.exe’ ‘C:\Users\blakk\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Python\Lib\site-packages\pip_vendor\pep517_in_process.py’ prepare_metadata_for_build_wheel ‘C:\Users\blakk\AppData\Local\Temp\tmp2c6x03is’ Check the logs for full command output.<br>
WARNING: You are using pip version 20.3.3; however, version 21.3.1 is available.<br>
You should consider upgrading via the ‘C:\Users\blakk\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\python-real.exe -m pip install --upgrade pip’ command.<br>
Traceback (most recent call last):<br>
File “C:/Users/blakk/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/ALPACA.py”, line 52, in <strong>init</strong><br>
import open3d as o3d<br>
ModuleNotFoundError: No module named ‘open3d’</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/blakk/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/ALPACA.py”, line 56, in <strong>init</strong><br>
slicer.util.pip_install(‘notebook==6.0.3’)<br>
File “C:\Users\blakk\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\Python\slicer\util.py”, line 2876, in pip_install<br>
_executePythonModule(‘pip’, args)<br>
File “C:\Users\blakk\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\Python\slicer\util.py”, line 2851, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “C:\Users\blakk\AppData\Local\NA-MIC\Slicer 4.11.20210226\bin\Python\slicer\util.py”, line 2820, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/blakk/AppData/Local/NA-MIC/Slicer 4.11.20210226/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘notebook==6.0.3’]’ returned non-zero exit status 1."</p>
<p>I appreciate any help possible and thank you in advance.</p>

---

## Post #2 by @smrolfe (2022-03-15 17:48 UTC)

<p>Thanks <a class="mention" href="/u/khanine">@Khanine</a>, we are updating the ALPACA module to use a more recent version of the open3d library to correct this issue. The new version should be available tomorrow through the extension manager, or later today if you’d like to update it manually.</p>

---

## Post #3 by @Khanine (2022-03-15 17:55 UTC)

<p>Thank you so much! I appreciate this a lot!</p>

---

## Post #4 by @smrolfe (2022-03-15 21:58 UTC)

<p><a class="mention" href="/u/khanine">@Khanine</a> The fix is up on the SlicerMorph repo and you should be able to update it through the extension manager tomorrow. You can also correct it in your installation by running the following line in the Python Interactor:</p>
<pre><code class="lang-auto">pip_install('pywinpty==1.1.6')
</code></pre>
<p>and then opening the ALPACA module.</p>

---

## Post #5 by @Sebastian_Rodrigo_Ag (2022-05-11 01:00 UTC)

<p>Hi! i have a similar problem, but in my case the error is:</p>
<p>WARNING: You are using pip version 22.0.3; however, version 22.0.4 is available.<br>
You should consider upgrading via the ‘C:\Users\Slicer\Slicer 5.1.0-2022-05-01\bin\python-real.exe -m pip install --upgrade pip’ command.<br>
Traceback (most recent call last):<br>
File “C:/Users/Slicer/Slicer 5.1.0-2022-05-01/NA-MIC/Extensions-30915/SlicerMorph/lib/Slicer-5.1/qt-scripted-modules/ALPACA.py”, line 149, in <strong>init</strong><br>
slicer.util.pip_install([wheelPath])<br>
File “C:\Users\Slicer\Slicer 5.1.0-2022-05-01\bin\Python\slicer\util.py”, line 3431, in pip_install<br>
_executePythonModule(‘pip’, args)<br>
File “C:\Users\Slicer\Slicer 5.1.0-2022-05-01\bin\Python\slicer\util.py”, line 3394, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “C:\Users\Slicer\Slicer 5.1.0-2022-05-01\bin\Python\slicer\util.py”, line 3363, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/Slicer/Slicer 5.1.0-2022-05-01/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘C:/Users/Sebastián Aguayo/Documents/3D Slicer/open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl’]’ returned non-zero exit status 1.</p>
<p>The line pip_install(‘pywinpty==1.1.6’) doesn’t work for me.</p>
<p>I’m new to slicermorph and thanks in advance for any help</p>

---

## Post #6 by @jamesobutler (2022-05-11 01:51 UTC)

<aside class="quote no-group" data-username="Sebastian_Rodrigo_Ag" data-post="5" data-topic="22512">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sebastian_rodrigo_ag/48/14595_2.png" class="avatar"> Sebastian_Rodrigo_Ag:</div>
<blockquote>
<p>pip_install(‘pywinpty==1.1.6’)</p>
</blockquote>
</aside>
<p>This was only needed for Slicer 4.11.2021026.</p>
<aside class="quote no-group" data-username="Sebastian_Rodrigo_Ag" data-post="5" data-topic="22512">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/sebastian_rodrigo_ag/48/14595_2.png" class="avatar"> Sebastian_Rodrigo_Ag:</div>
<blockquote>
<p>Slicer 5.1.0-2022-05-01</p>
</blockquote>
</aside>
<p>Since you are using recent Slicer preview, you should be able to skip that step. Did you attempt this because you ran into a problem using latest Slicer Preview? Or were you just following some older instructions?</p>

---

## Post #8 by @Sebastian_Rodrigo_Ag (2022-05-11 02:21 UTC)

<p>yes i tried because the loading bar never ends it stays on “Upgrading open3d. This may take a minute…”</p>

---

## Post #9 by @smrolfe (2022-05-11 20:29 UTC)

<p><a class="mention" href="/u/sebastian_rodrigo_ag">@Sebastian_Rodrigo_Ag</a> could you try running these lines from the Python Interactor?</p>
<blockquote>
<p>wheelPath = ‘C:/Users/Sebastián Aguayo/Documents/3D Slicer/open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl’<br>
pip_install([wheelPath])</p>
</blockquote>

---

## Post #10 by @Sebastian_Rodrigo_Ag (2022-05-13 00:07 UTC)

<p>Hello Sara, first of all thank you very much for the answer. I entered the code and it sends me this error:</p>
<blockquote>
<blockquote>
<blockquote>
<p>wheelPath = ‘C:/Users/Sebastián Aguayo/Documents/3D Slicer/open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl’<br>
File “”, line 1<br>
wheelPath = ‘C:/Users/Sebastián Aguayo/Documents/3D Slicer/open3d-0.14.1+816263b-cp39-cp39-win_amd64.whl’<br>
^<br>
SyntaxError: invalid character ‘‘’ (U+2018)<br>
pip_install([wheelPath])<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
NameError: name ‘wheelPath’ is not defined</p>
</blockquote>
</blockquote>
</blockquote>
<p>maybe it’s because of the “´” in Sebastián</p>

---

## Post #11 by @smrolfe (2022-05-13 14:37 UTC)

<p>I have corrected the issue causing the filename bug in the most recent version of ALPACA, could you try updating?</p>

---

## Post #12 by @Sebastian_Rodrigo_Ag (2022-05-23 00:33 UTC)

<p>Should i update slicermorph then? Thank you!</p>

---

## Post #13 by @muratmaga (2022-05-23 15:40 UTC)

<p>Yes, please install the latest stable (5.0.2) and then install SlicerMorph to have the latest changes to the ALPACA. You should no problem with the latest stable.</p>

---
