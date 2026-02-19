---
topic_id: 754
title: "Add Environment Variable For Slicer Application"
date: 2017-07-24
url: https://discourse.slicer.org/t/754
---

# Add environment variable for Slicer application

**Topic ID**: 754
**Date**: 2017-07-24
**URL**: https://discourse.slicer.org/t/add-environment-variable-for-slicer-application/754

---

## Post #1 by @moselhy (2017-07-24 14:28 UTC)

<p>Hello,</p>
<p>With all the great new nightly builds for Slicer, the installed executables obviously reside in different folders for different versions (e.g. %PROGRAMFILES%\Slicer 4.7.0-2017-07-22\Slicer.exe). I think it would be a good idea to add an option “Change SLICERPATH environment variable” to the highlighted portion of the installation program so that the user’s custom shortcuts that use Slicer.exe don’t have to be changed every time they install a newer version of Slicer.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f583ef3d8aa62f53017751a782b93b1a4594d6f.png" data-base62-sha1="92n95COcmCJlM31bME6370MpqLJ" width="498" height="385"></p>
<p>This is what it currently is now, where the user has to change the target every time they install Slicer.exe to a different folder (i.e. new version of Slicer):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc2492eb0b04d3999b1e8723b440f8e3c9cfc0e6.png" data-download-href="/uploads/short-url/zYyGgIXkr2QGh6E199p3XIhrpmS.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fc2492eb0b04d3999b1e8723b440f8e3c9cfc0e6_2_418x500.png" data-base62-sha1="zYyGgIXkr2QGh6E199p3XIhrpmS" width="418" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/fc2492eb0b04d3999b1e8723b440f8e3c9cfc0e6_2_418x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc2492eb0b04d3999b1e8723b440f8e3c9cfc0e6.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc2492eb0b04d3999b1e8723b440f8e3c9cfc0e6.png 2x" data-dominant-color="F3F4F4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">541×647 21.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is what I am suggesting, where the user does not have to change the target every time they install Slicer.exe to a different folder:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44346284d4485da178e2b4fbcd28c11af1db0140.png" data-download-href="/uploads/short-url/9JmHws9327XDCGsyuoBkGAfMeYg.png?dl=1" title="image.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/44346284d4485da178e2b4fbcd28c11af1db0140_2_347x500.png" data-base62-sha1="9JmHws9327XDCGsyuoBkGAfMeYg" width="347" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/44346284d4485da178e2b4fbcd28c11af1db0140_2_347x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44346284d4485da178e2b4fbcd28c11af1db0140.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/44346284d4485da178e2b4fbcd28c11af1db0140.png 2x" data-dominant-color="F3F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">443×637 20.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Please let me know your opinions on this.</p>
<p>MM</p>

---

## Post #2 by @lassoan (2017-07-24 14:35 UTC)

<p>What we envision for this is that extension would create the shortcut for itself. For example, when you install your module, it could show a “Pin to Start menu” button, which would create the shortcut to the appropriate Slicer version.</p>
<p>We haven’t implemented this in any modules yet, but we would be very interested and can give you any help you need.</p>

---

## Post #3 by @moselhy (2017-07-24 14:39 UTC)

<p>The reason I am suggesting this is because some users (including myself and labmates) use Python scripts without the use of a custom extension, such as <a href="https://github.com/moselhy/HyperpolarizedSegmentStats" rel="nofollow noopener">this script</a>. To utilize the script, the user can just add a shortcut linking to Slicer.exe and using the --python-script argument. With an environment variable pointing to Slicer’s program path, it would be very convenient for the script users.</p>

---

## Post #4 by @lassoan (2017-07-24 15:53 UTC)

<p>A global environment variable could be easily corrupted unintentionally (just by some one installing or uninstalling a new Slicer version could break things). So, automatic creation and update of such a variable does not seem feasible in general, but if you don’t particularly care which Slicer version you will find, then you can use file association information, which defines what program to use to open Slicer scene files (.mrml and .mrb), which is typically the version that you installed last time.</p>
<p>On Windows, you can retrieve it by <code>ftype</code> command:</p>
<pre><code>c:\&gt;ftype Slicer
Slicer="C:\Program Files\Slicer 4.7.0-2017-07-22\Slicer.exe" "%1"
</code></pre>
<p>So, to run a Python script from .bat file you can do this:</p>
<pre><code>@echo off

REM Get Slicer executable in SlicerExecutable environment variable
for /f "delims== tokens=2" %%a in ('ftype Slicer') do set SlicerExecutable=%%a
set SlicerExecutable=%SlicerExecutable:~0,-5%

REM Start a Python script in Slicer
%SlicerExecutable% --python-code "print('It works!')"</code></pre>

---

## Post #6 by @lassoan (2021-06-09 14:00 UTC)

<p>On Windows, recent Slicer Preview Releases (Slicer-4.13) registers the <code>Slicer</code> application during install. This makes it possible to use <code>start</code> command to launch Slicer. For example, this command on the command-line starts Slicer and loads an image:</p>
<pre><code class="lang-auto">start Slicer c:\Users\andra\OneDrive\MRHead.nrrd
</code></pre>

---
