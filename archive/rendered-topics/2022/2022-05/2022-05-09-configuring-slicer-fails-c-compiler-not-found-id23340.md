---
topic_id: 23340
title: "Configuring Slicer Fails C Compiler Not Found"
date: 2022-05-09
url: https://discourse.slicer.org/t/23340
---

# Configuring Slicer fails - C compiler not found

**Topic ID**: 23340
**Date**: 2022-05-09
**URL**: https://discourse.slicer.org/t/configuring-slicer-fails-c-compiler-not-found/23340

---

## Post #1 by @cpinter (2022-05-09 10:11 UTC)

<p>I am rebuilding everything due to the change of version to 5, and on one of the machines I use (after building successfully on another) I’m getting this error.</p>
<pre><code class="lang-auto">c:\d\S5R&gt;"c:\Program Files\CMake\bin\cmake.exe" c:\d\Slicer -G "Visual Studio 17 2022" -DQt5_DIR:PATH=c:\Qt\5.15.2\msvc2019_64\lib\cmake\Qt5 -DSlicer_USE_SimpleITK:BOOL=OFF
-- Setting C++ standard
-- Setting C++ standard - C++14
-- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.19044.
-- The C compiler identification is unknown
-- The CXX compiler identification is unknown
CMake Error at CMakeLists.txt:51 (project):
  No CMAKE_C_COMPILER could be found.
CMake Error at CMakeLists.txt:51 (project):
  No CMAKE_CXX_COMPILER could be found.
</code></pre>
<p>What I did:</p>
<ul>
<li>Install VS 2022 (Community) from scratch
<ul>
<li>Made sure it installs Windows SDK (10.0.19041.0) (searching online, it seemed to be the problem for others)</li>
</ul>
</li>
<li>Started VS 2022 (I remembered from earlier versions that setup is fully finalized when starting)</li>
<li>Checked the files MSBuild.exe and cl.exe, they seem to be in the right place (exactly the same as on the machine it built well)</li>
<li>Did a Repair on VS 2022</li>
<li>Restarted the machine a few times</li>
</ul>
<p>Does anyone has an idea what it may be? Thanks a lot!</p>

---

## Post #2 by @cpinter (2022-05-09 10:14 UTC)

<p>In <code>CMakeError.log</code> I see this<br>
<code>LINK : fatal error LNK1104: cannot open file 'ucrtd.lib'</code><br>
Could it be that the Windows SDK I have is not compatible with the Windows version?</p>

---

## Post #3 by @cpinter (2022-05-09 10:21 UTC)

<p>It turns out I manually had to install the latest Windows SDK (downloaded from <a href="https://developer.microsoft.com/en-us/windows/downloads/windows-sdk/">here</a>) and then configure got past this error.</p>
<p>Sorry for the noise; maybe for someone this topic will solve the same issue.</p>

---

## Post #4 by @Alex_Fergosen (2023-03-13 00:24 UTC)

<p>I just register to say thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
You saved me after 2 days wasting of time</p>

---
