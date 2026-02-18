# How to package my slicer app at every day 21:00 by a script

**Topic ID**: 25287
**Date**: 2022-09-16
**URL**: https://discourse.slicer.org/t/how-to-package-my-slicer-app-at-every-day-21-00-by-a-script/25287

---

## Post #1 by @jay1987 (2022-09-16 02:23 UTC)

<p>all i know to package slicer app is to generate PACKAGE project<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e713cf577983649daf04bb25de7b59e208095fb5.png" alt="image" data-base62-sha1="wYcJLPBjYF9i0zji5liO3KPMZNP" width="254" height="109"><br>
is there a way to package slicer app by a script  ? in that way i can package slicer app every night after work , and test Engineer can get the app every morning .</p>

---

## Post #2 by @lassoan (2022-09-16 03:02 UTC)

<p>On Windows, we use the built-in Task Scheduler for this.</p>
<p>If you want to just update Slicer and create a package then putting the two commands that build <code>ALL_BUILD</code> and <code>PACKAGE</code> targets should be sufficient.</p>
<p>If you want more complete solution - run all tests, report results to dashboard, build all extensions, etc. - then you can adapt the <a href="https://github.com/Slicer/DashboardScripts">scripts that official Slicer build machines use</a>.</p>

---

## Post #3 by @jay1987 (2022-09-16 03:19 UTC)

<p>thanks lassoan,we will learn the scripts you suggested<br>
we alreay have the ALL_BUILD and PACKAGE project, how to call the PACKAGE project in Window built-in Task Scheduler?</p>

---

## Post #4 by @lassoan (2022-09-16 03:54 UTC)

<p>You can build the <code>ALL_BUILD</code> target with a command like this:</p>
<p><code>"c:\Program Files\Microsoft Visual Studio\2022\Community\Msbuild\Current\Bin\MSBuild.exe" ALL_BUILD.vcxproj /p:Configuration=Release</code></p>
<p>You can put all the build commands in a .bat file and run it using the Task Scheduler. Using the Task Scheduler is straightforward and is also widely documented on the web.</p>

---

## Post #5 by @jay1987 (2022-09-16 05:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="25287">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>/p:Configuration=Release</p>
</blockquote>
</aside>
<p>thank you very much<br>
<a class="mention" href="/u/lassoan">@lassoan</a> it works ,  i think i can have a good dream tonight!</p>

---
