---
topic_id: 14258
title: "Slicerradiomics Error"
date: 2020-10-26
url: https://discourse.slicer.org/t/14258
---

# slicerradiomics error

**Topic ID**: 14258
**Date**: 2020-10-26
**URL**: https://discourse.slicer.org/t/slicerradiomics-error/14258

---

## Post #1 by @firatoz (2020-10-26 19:29 UTC)

<p>When using Slicer Radiomics in 4.13 version I get this error:</p>
<p>RadiomicsCLI standard error:</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/Yi�it/AppData/Roaming/NA-MIC/Extensions-29434/SlicerRadiomics/lib/Slicer-4.13/cli-modules/SlicerRadiomicsCLI.py”, line 7, in<br>
from radiomics.scripts import parse_args<br>
File “C:\Users\Yi�it\AppData\Roaming\NA-MIC\Extensions-29434\SlicerRadiomics\Lib\site-packages\radiomics_<em>init</em>_.py”, line 15, in<br>
from . import imageoperations<br>
File “C:\Users\Yi�it\AppData\Roaming\NA-MIC\Extensions-29434\SlicerRadiomics\Lib\site-packages\radiomics\imageoperations.py”, line 7, in<br>
import SimpleITK as sitk<br>
ModuleNotFoundError: No module named ‘SimpleITK’</p>
<p>I will be glad if you help me</p>

---

## Post #2 by @muratmaga (2020-10-26 19:35 UTC)

<p>As indicated in the download page currently preview (v4.13 series) is unstable, and may not work as intended. Your best option is to use the stable (v4.11-20200930) until changes to preview is finished.</p>

---

## Post #3 by @firatoz (2020-10-27 09:20 UTC)

<p>I tried it on version 4.11 today but got a similar error again:</p>
<p>RadiomicsCLI standard error:</p>
<p>Traceback (most recent call last):<br>
File “C:/Users/Yi�it/AppData/Roaming/NA-MIC/Extensions-29402/SlicerRadiomics/lib/Slicer-4.11/cli-modules/SlicerRadiomicsCLI.py”, line 7, in<br>
from radiomics.scripts import parse_args<br>
File “C:\Users\Yi�it\AppData\Roaming\NA-MIC\Extensions-29402\SlicerRadiomics\Lib\site-packages\radiomics_<em>init</em>_.py”, line 15, in<br>
from . import imageoperations<br>
File “C:\Users\Yi�it\AppData\Roaming\NA-MIC\Extensions-29402\SlicerRadiomics\Lib\site-packages\radiomics\imageoperations.py”, line 6, in<br>
import pywt<br>
ModuleNotFoundError: No module named ‘pywt’</p>

---

## Post #4 by @pieper (2020-10-27 09:52 UTC)

<aside class="quote no-group" data-username="firatoz" data-post="3" data-topic="14258">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/firatoz/48/8611_2.png" class="avatar"> firatoz:</div>
<blockquote>
<p>“C:\Users\Yi�it\</p>
</blockquote>
</aside>
<p>Looks like things are getting confused by a special (non US) character in your home directory path.  Try installing Slicer in a different path, like c:\Slicer or similar.</p>

---

## Post #5 by @muratmaga (2020-10-27 15:02 UTC)

<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="14258">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Try installing Slicer in a different path, like c:\Slicer or similar.</p>
</blockquote>
</aside>
<p>Well I don’t think <a class="mention" href="/u/firatoz">@firatoz</a> can. That’s the extension (not the application), which goes directly into the AppData under user folder (which has the special character), when extension manager is used.</p>
<p><a class="mention" href="/u/firatoz">@firatoz</a> you can follow this instructions, and download the Radiomics extension for your specific slicer version manually and then to a folder that that doesn’t include any non-ascii characters: <a href="https://www.slicer.org/wiki/Documentation/4.3/SlicerApplication/ExtensionsManager#How_to_manually_install_an_extension_.3F" class="inline-onebox">Documentation/4.3/SlicerApplication/ExtensionsManager - Slicer Wiki</a></p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> is this an Slicer issue or Radiomics extension issue?</p>

---

## Post #6 by @firatoz (2020-10-27 17:09 UTC)

<p>I downloaded the slicer radiomics. " lib / Slicer-X.Y / cli-modules and lib / Slicer-X.Y / qt-scripted-modules"  these files exist but there is no file " lib / Slicer-X.Y / qt-loadable-modules" that I need to copy into module settings.</p>

---

## Post #7 by @muratmaga (2020-10-27 17:11 UTC)

<p>There might not be one. Go ahead and restart Slicer and try again.</p>

---

## Post #8 by @pieper (2020-10-27 17:33 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="5" data-topic="14258">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Well I don’t think <a class="mention" href="/u/firatoz">@firatoz</a> can. That’s the extension (not the application), which goes directly into the AppData under user folder (which has the special character), when extension manager is used.</p>
</blockquote>
</aside>
<p>You are right, this is perhaps something we should fix.  On mac the extensions go into the application installation folder, which is cleaner I would say.</p>
<p>Anyway, perhaps <a class="mention" href="/u/firatoz">@firatoz</a> can move the extension folder and then edit the paths in the Application Settings → Modules paths to match.</p>

---

## Post #9 by @firatoz (2020-10-27 17:46 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> I tried many times in versions 4.13 and 4.11, unfortunately I cannot install it manually.</p>

---

## Post #10 by @muratmaga (2020-10-27 17:48 UTC)

<p>Can you try what <a class="mention" href="/u/pieper">@pieper</a> suggested?</p>
<p>Install via extension mechanism, then move the folder out of problematic path (e.g., to something like C:/Radiomics or something), and then modify the module paths from application settings accordingly?</p>

---

## Post #11 by @firatoz (2020-11-04 20:47 UTC)

<p>i changed the location of the extension to C: / Radiomics but it still didn’t work.  I have tried it on other computers, unfortunately I cannot run Radiomics.  I wonder if this could be a software bug that needs to be fixed</p>

---

## Post #12 by @muratmaga (2020-11-04 21:07 UTC)

<p>Can you send the log file from the instance where you have it in c:/radiomics?</p>

---

## Post #13 by @lassoan (2020-11-04 21:29 UTC)

<aside class="quote no-group" data-username="firatoz" data-post="3" data-topic="14258">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/firatoz/48/8611_2.png" class="avatar"> firatoz:</div>
<blockquote>
<p>ModuleNotFoundError: No module named ‘pywt’</p>
</blockquote>
</aside>
<p>This is a known issue, you need to manually install two Python packages (copy-paste two lines of code into the Python console) - see details <a href="https://github.com/Radiomics/SlicerRadiomics/issues/62#issuecomment-716766021">here</a>. It is expected to be fixed very soon.</p>
<p>Note that special characters in paths should not be an issue if you use latest stable Slicer release and <em>Windows 10 Version 1903 (May 2019 Update)</em> or later (see <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#operating-system-versions">documentation</a>).</p>

---
