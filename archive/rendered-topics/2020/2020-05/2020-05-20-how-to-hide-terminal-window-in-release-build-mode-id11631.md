# How to hide terminal window in release build mode?

**Topic ID**: 11631
**Date**: 2020-05-20
**URL**: https://discourse.slicer.org/t/how-to-hide-terminal-window-in-release-build-mode/11631

---

## Post #1 by @leemoncn (2020-05-20 08:39 UTC)

<p>I build slicer 4.10.2 in release mode. When i run slicer, it still have terminal window. How to hide terminal in release build mode?(OS: Windows 10)</p>

---

## Post #2 by @cpinter (2020-05-20 09:26 UTC)

<p>I believe you need to disable the “Slicer_BUILD_WIN32_CONSOLE” CMake variable.</p>
<p>By the way, I strongly suggest using a recent preview version. 4.10.2 is more than a year and a half old, and the current preview is quite stable, given that we are approaching 5.0.</p>

---

## Post #3 by @JiaLei (2021-10-13 06:51 UTC)

<p>I build release mode by the latest version of Slicer on Windows10, and I set cmake variable “-DSlicer_BUILD_WIN32_CONSOLE:BOOL=OFF”. But the terminal still exists.</p>
<p>My commands:</p>
<pre><code class="lang-auto">C:\D\S4R&gt; cmake -A x64 -DCMAKE_BUILD_TYPE:STRING=Release -DQt5_DIR:PATH=C:\Qt\5.15.2\msvc2019_64\lib\cmake\Qt5 -DSlicer_BUILD_WIN32_CONSOLE:BOOL=OFF C:\D\S4
C:\D\S4R&gt; cmake --build . --config Release
</code></pre>

---
