# Nearly Success, but ("Timeout was reached")

**Topic ID**: 22703
**Date**: 2022-03-27
**URL**: https://discourse.slicer.org/t/nearly-success-but-timeout-was-reached/22703

---

## Post #1 by @whu (2022-03-27 00:13 UTC)

<p>new version Slicer version by git; Qt 5.15.2; VS 2019.<br>
The compile result show:<br>
========= 生成: 成功 46 个，失败 1 个，最新 1 个，跳过 3 个 ==========</p>
<p>Log file for error:</p>
<p>49&gt;  CMake Error at C:/Slicer/SlicerSource/CMake/ExternalData.cmake:1113 (message):<br>
49&gt;<br>
49&gt;<br>
49&gt;    Object MD5=c9957d62f0bda84055b4f41f4eef28ef not found at:<br>
49&gt;<br>
49&gt;      <a href="https://github.com/Slicer/SlicerTestingData/releases/download/MD5/c9957d62f0bda84055b4f41f4eef28ef" rel="noopener nofollow ugc">https://github.com/Slicer/SlicerTestingData/releases/download/MD5/c9957d62f0bda84055b4f41f4eef28ef</a> (“Timeout was reached”)<br>
49&gt;<br>
49&gt;<br>
49&gt;C:\VS2019\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(241,5): error MSB8066: “C…</p>
<p>why?<br>
The data can be downloaded Manually, why in the compile process?</p>
<p>Waiting for help . thanks</p>

---

## Post #2 by @whu (2022-03-28 11:10 UTC)

<p>thanks for focusing. Finally this kind of error matters little.</p>

---

## Post #3 by @lassoan (2022-03-28 11:24 UTC)

<p>This was a network error. Must likely your internet connection was too slow or disconnected during the download.</p>

---
