# Could not find WebEngineProcess.exe

**Topic ID**: 17035
**Date**: 2021-04-12
**URL**: https://discourse.slicer.org/t/could-not-find-webengineprocess-exe/17035

---

## Post #1 by @wujie (2021-04-12 06:35 UTC)

<p>when I debug the Slicer programe,and run the extension manager,make a error “Could not find QtWebEngineProcess.exe”，how can I address it?</p>

---

## Post #2 by @wujie (2021-04-12 06:58 UTC)

<p>I compile slicer using windows.</p>

---

## Post #3 by @pieper (2021-04-12 23:33 UTC)

<p>On my windows machine I’m not seeing a <code>QtWebEngineProcess.exe</code> bundled with Qt, but it does appear in a PySide2 folder.  Did you compile Slicer with PySide2?  I didn’t know that was possible.</p>
<p>In any case installing extensions from the extension manager in your local build is not a supported use case since most C++ libraries won’t work across builds.  But pure python ones would I guess.</p>

---

## Post #4 by @wujie (2021-04-13 01:47 UTC)

<p>Thank you for replying me,I used  the official tutorial to local building.I can’t use PySide2 compiling Slicer</p>

---

## Post #5 by @wujie (2021-04-13 01:48 UTC)

<aside class="quote no-group quote-modified" data-username="wujie" data-post="4" data-topic="17035" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/dbc845/48.png" class="avatar"> wujie:</div>
<blockquote>
<p>感谢您的回复，我使用的是本地建筑的官方教程。我无法使用PySide2编译Slicer</p>
</blockquote>
</aside>
<aside class="quote no-group" data-username="wujie" data-post="4" data-topic="17035" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/w/dbc845/48.png" class="avatar"> wujie:</div>
<blockquote>
<p>Thank you for replying me,I used the official tutorial to local building.I can’t use PySide2 compiling Slicer</p>
</blockquote>
</aside>
<p>Thank you for replying me,I used the official tutorial to local building.I can’t use PySide2 compiling Slicer</p>

---

## Post #6 by @jamesobutler (2021-04-13 02:12 UTC)

<p>I have a QtWebEngineProcess.exe in both my Qt binary installations on Windows and also in my installed Slicer’s bin directory.</p>
<p>Did you select to install the Qt QWebEngine component when installing Qt?<br>
From <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#install-prerequisites" class="inline-onebox" rel="noopener nofollow ugc">Windows — 3D Slicer documentation</a></p>
<blockquote>
<p><a href="https://www.qt.io/download-open-source" rel="noopener nofollow ugc">Qt5</a>: Download Qt universal installer and install Qt 5.15 components: MSVC2019 64-bit, Qt Script, Qt WebEngine.</p>
</blockquote>

---

## Post #7 by @wujie (2021-04-13 07:55 UTC)

<p>Thank you for your reply, I had installed the  Qt QWebEngine componet when installing Qt,and I also have a QtWebEngineProcess.exe in both my Qt binary installations on Windows and in Slicer’s bin directory,but I still have the error “Could not find QtWebEngineProcess.exe”,it may exists the problem of version?</p>

---

## Post #8 by @jamesobutler (2021-04-13 11:26 UTC)

<p>Did your Slicer build finish with errors?</p>

---

## Post #9 by @smallvalthoss (2021-04-24 23:02 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> I am having trouble figuring out how to download Qt5 to be able to build slicer. Do you still need to download from the online installer? I have tried both and am unable to find anything like “\Qt\5.15.0\msvc2019_64\lib\cmake\Qt5”. Any help would be appreciated.</p>

---

## Post #10 by @jamesobutler (2021-04-24 23:16 UTC)

<p>Yes, I use Qt 5.15.2. You can download the installer tool from <a href="https://www.qt.io/download-qt-installer" class="inline-onebox" rel="noopener nofollow ugc">Download Qt: Get Qt Online Installer</a>.</p>
<p>You can read the Slicer build pre-reqs over at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#install-prerequisites" class="inline-onebox" rel="noopener nofollow ugc">Windows — 3D Slicer documentation</a>.</p>

---

## Post #11 by @smallvalthoss (2021-04-25 00:11 UTC)

<p>Hey thank you, for some reason I kept going around in circles on their site… I appreciate it!</p>

---

## Post #12 by @smallvalthoss (2021-04-25 18:52 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="10" data-topic="17035" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>Yes, I use Qt 5.15.2. You can download the installer tool from <a href="https://www.qt.io/download-qt-installer" rel="noopener nofollow ugc">Download Qt: Get Qt Online Installer </a>.</p>
<p>You can read the Slicer build pre-reqs over at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html#install-prerequisites" rel="noopener nofollow ugc">Windows — 3D Slicer documentation </a>.</p>
</blockquote>
</aside>
<p>How long does it usually take for you to build the app?</p>

---

## Post #13 by @lassoan (2021-04-25 21:56 UTC)

<p>In Windows, a full build takes about 6 hours on a desktop, 12 hours on a laptop.</p>

---
