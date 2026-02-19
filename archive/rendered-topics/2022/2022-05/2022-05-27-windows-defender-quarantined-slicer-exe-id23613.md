---
topic_id: 23613
title: "Windows Defender Quarantined Slicer Exe"
date: 2022-05-27
url: https://discourse.slicer.org/t/23613
---

# Windows Defender quarantined Slicer.exe

**Topic ID**: 23613
**Date**: 2022-05-27
**URL**: https://discourse.slicer.org/t/windows-defender-quarantined-slicer-exe/23613

---

## Post #1 by @lassoan (2022-05-27 19:00 UTC)

<p>On my university-managed computer, Slicer.exe disappeared from the install tree. Windows Defender quarantined the executable due to “potentially unwanted behavior”.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0f8abed7dbfc9992fda069d4537c63a266d2ba61.png" alt="image" data-base62-sha1="2duqdxZAVJPT1esG4ePiTiuyxax" width="499" height="411"></p>
<p>It states that it detected <code>Program:Win32/Beareuws.A!ml</code>, which must be a false positive. I’ve submitted the executable to VirusTotal and nothing was detected (just one bogus engine out of 68 indicated “unsafe” without any more information).</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> You have submitted false positives to Microsoft before. Would you be able to submit this Slicer5 <code>Slicer.exe</code> executable?</p>

---

## Post #2 by @jcfr (2022-05-27 19:23 UTC)

<blockquote>
<p>You have submitted false positives to Microsoft before. Would you be able to submit this Slicer5 <code>Slicer.exe</code> executable?</p>
</blockquote>
<p>I will engage with our security team and follow up.</p>

---

## Post #3 by @jcfr (2022-06-10 16:24 UTC)

<p>The file has been submitted for analysis.</p>
<p>This was done following instructions published at <a href="https://docs.microsoft.com/en-us/microsoft-365/security/defender-endpoint/defender-endpoint-false-positives-negatives?view=o365-worldwide#part-4-submit-a-file-for-analysis" class="inline-onebox">Address false positives/negatives in Microsoft Defender for Endpoint - Microsoft Defender for Endpoint | Microsoft Learn</a></p>
<h3><a name="p-79256-results-as-of-20220610-1" class="anchor" href="#p-79256-results-as-of-20220610-1" aria-label="Heading link"></a>Results (as of 2022.06.10)</h3>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a9b1f44cac6f0ea93f84ccdd4192996838f0e54.png" data-download-href="/uploads/short-url/aDZGbJIeIeiouPx31QHNerfUbuk.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a9b1f44cac6f0ea93f84ccdd4192996838f0e54_2_380x500.png" alt="image" data-base62-sha1="aDZGbJIeIeiouPx31QHNerfUbuk" width="380" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a9b1f44cac6f0ea93f84ccdd4192996838f0e54_2_380x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a9b1f44cac6f0ea93f84ccdd4192996838f0e54_2_570x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a9b1f44cac6f0ea93f84ccdd4192996838f0e54_2_760x1000.png 2x" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1177×1547 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-79256-submitted-information-2" class="anchor" href="#p-79256-submitted-information-2" aria-label="Heading link"></a>Submitted information</h3>
<p>The following information were provided:</p>
<ul>
<li>
<p><strong>Select the Microsoft security product used to scan the file</strong>:<br>
<code>Microsoft Defender Antivirus (Windows 10)</code></p>
</li>
<li>
<p><strong>What do you believe this file is?</strong><br>
Incorrectly detected as PUA (potentially unwanted application)</p>
</li>
<li>
<p><strong>Detection name</strong>: <code>Program:Win32/Beareuws.A!ml</code></p>
</li>
<li>
<p><strong>Definition version (recommended)</strong>:<br>
Unknown</p>
</li>
<li>
<p><strong>Additional information:</strong></p>
<p><em>Since the submission form was stripping new lines, I added separator to more clearly identify the paragraph</em></p>
<pre><code class="lang-plaintext">This corresponds to the statically built launcher (C++/Qt)
we shipped within the windows Slicer distribution available
for download at https://download.slicer.org
  
##################################
The false detection has been discussed in 
(1) https://discourse.slicer.org/t/windows-defender-quarantined-slicer-exe/23613 
and
(2) https://discourse.slicer.org/t/windows-security-warning-on-stable/23804
  
##################################
The binary is built using this GitHub project:
https://github.com/commontk/AppLauncher
  
##################################
It downloads (see [1]) a pre-built version of Qt that I built and published here:
https://github.com/jcfr/qt-static-build/releases/tag/applauncher-5.11.2-vs2017
  
##################################
[1] https://github.com/commontk/AppLauncher/blob/c55d1a49844288248f7454624eea416302d895da/appveyor.yml#L36-L39
</code></pre>
</li>
</ul>

---

## Post #4 by @jcfr (2022-06-10 16:25 UTC)

<aside class="quote no-group" data-username="jcfr" data-post="3" data-topic="23613">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jcfr/48/17825_2.png" class="avatar"> jcfr:</div>
<blockquote>
<p><strong>Definition version (recommended)</strong>:<br>
Unknown</p>
</blockquote>
</aside>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/lassoan">@lassoan</a>  Do you have more details regarding this ?</p>

---

## Post #5 by @lassoan (2022-06-10 17:10 UTC)

<p>For me it was the with the latest definition version as of 2022-05-25. I’m not sure if it’s still removes the executable. I’ve tried a manual scan of the Slicer folder and it did not do anything, but maybe because I’ve manually restored the file before.</p>

---
