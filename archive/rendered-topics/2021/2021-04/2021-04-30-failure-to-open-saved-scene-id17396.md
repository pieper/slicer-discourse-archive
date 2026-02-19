---
topic_id: 17396
title: "Failure To Open Saved Scene"
date: 2021-04-30
url: https://discourse.slicer.org/t/17396
---

# Failure to open saved scene

**Topic ID**: 17396
**Date**: 2021-04-30
**URL**: https://discourse.slicer.org/t/failure-to-open-saved-scene/17396

---

## Post #1 by @arif (2021-04-30 15:26 UTC)

<p>Hello all ;<br>
When I try to load the slicer format of my saved work, I often get nothing or an error message. My saved work consists fusion images (MRI and PET images) and maybe that is the reason for that. Do you have any suggestions on how to open my saved work properly.<br>
Best Regards<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e80c9bfd8249729b3217e2cfc48851ab420980bb.png" data-download-href="/uploads/short-url/x6NMT5mQiRQzrxip5ciJG58pjKP.png?dl=1" title="axc" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e80c9bfd8249729b3217e2cfc48851ab420980bb_2_690x387.png" alt="axc" data-base62-sha1="x6NMT5mQiRQzrxip5ciJG58pjKP" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e80c9bfd8249729b3217e2cfc48851ab420980bb_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e80c9bfd8249729b3217e2cfc48851ab420980bb_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e80c9bfd8249729b3217e2cfc48851ab420980bb.png 2x" data-dominant-color="A5A5AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">axc</span><span class="informations">1366×768 75.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-04-30 15:28 UTC)

<p>Do you see more error messages in the application log?</p>

---

## Post #3 by @arif (2021-04-30 15:57 UTC)

<p>Hello Andras :</p>
<p>First of all thanks for the swift reply. I clicked to show details and there was only single error message. Can I check for more of a detailed error in Slicer?</p>

---

## Post #4 by @jamesobutler (2021-04-30 16:06 UTC)

<p><a class="mention" href="/u/arif">@arif</a> You can get the full application log by going to “Help-&gt;Report A Bug”. From there the default selection is the current session log, but you can find recent session log files as well. See if you see errors in there.  If you replicate in the current session log you can also use “View-&gt;Error Log” to filter out other messages to limit it to say errors and warnings.</p>

---

## Post #5 by @arif (2021-04-30 16:23 UTC)

<p>Hi James:<br>
Thanks for pointing out. Recent log file is down below.</p>
<p>Errors:</p>
<pre><code class="lang-nohighlight">Error parsing XML in stream at line 39, column 57, byte index 11184: not well-formed (invalid token)
The following modules failed to be instantiated:
   ChangeTracker
loadSourceAsModule - Failed to load file "C:/Users/Yakup/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/ChangeTracker/lib/Slicer-4.11/qt-scripted-modules/ChangeTracker.py"  as module "ChangeTracker" !
Fail to instantiate module  "ChangeTracker"
Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "C:\Users\Yakup\AppData\Local\NA-MIC\Slicer 4.11.20210226\lib\Python\Lib\imp.py", line 170, in load_source
    module = _exec(spec, sys.modules[name])
  File "&lt;frozen importlib._bootstrap&gt;", line 618, in _exec
  File "&lt;frozen importlib._bootstrap_external&gt;", line 678, in exec_module
  File "&lt;frozen importlib._bootstrap&gt;", line 219, in _call_with_frames_removed
  File "C:/Users/Yakup/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/ChangeTracker/lib/Slicer-4.11/qt-scripted-modules/ChangeTracker.py", line 4, in &lt;module&gt;
    import ChangeTrackerWizard
  File "C:\Users\Yakup\AppData\Local\NA-MIC\Slicer 4.11.20210226\NA-MIC\Extensions-29738\ChangeTracker\lib\Slicer-4.11\qt-scripted-modules\ChangeTrackerWizard\__init__.py", line 2, in &lt;module&gt;
    from ChangeTrackerStep import *
ModuleNotFoundError: No module named 'ChangeTrackerStep'

Warnings:
When loading module  "ChangeTrackerSelfTest" , the dependency "ChangeTracker" failed to be loaded.
libpng warning: iCCP: known incorrect sRGB profile
</code></pre>

---

## Post #6 by @jamesobutler (2021-04-30 17:38 UTC)

<p>I do not suspect the ChangeTracker module to be the issue of your loading problems. You should try to find in the log where it reports the loading specific errors. To confirm you can uninstall the ChangeTracker extension from the ExtensionsManager and try loading again.</p>

---

## Post #7 by @lassoan (2021-04-30 18:52 UTC)

<p>It seems that this log does not contain the part where you attempt to load the scene file. Could you please attach the complete log file?</p>

---

## Post #8 by @arif (2021-05-01 15:33 UTC)

<p>So I have tried to load again and took the log screenshot. There seems to be no more information then what is present in the screenshot, if you have any suggestions on acquiring more information regarding this error I can try them too.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af60c48f57cf8db9d1b054f416b7a333b4d52d16.png" data-download-href="/uploads/short-url/p1sSE8IpfV2ddHf67uxhEmDbagS.png?dl=1" title="Untitleds" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af60c48f57cf8db9d1b054f416b7a333b4d52d16.png" alt="Untitleds" data-base62-sha1="p1sSE8IpfV2ddHf67uxhEmDbagS" width="690" height="213" data-dominant-color="E0E5F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitleds</span><span class="informations">1365×423 26.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #9 by @lassoan (2021-05-01 15:39 UTC)

<p>Can you open the .mrml file in a text editor (for example, Visual Studio Code) and chexk what is in line 25 near the 56th character? If there is nothing obvious then it would be great if you could share that mrml file or at least that line so that we can have a look, too.</p>

---

## Post #10 by @arif (2021-05-01 16:15 UTC)

<p>The .mrml file is below as a link:</p>
<p><em>(link has been removed due to potentially containing patient information)</em></p>
<p>Thank you</p>

---

## Post #11 by @lassoan (2021-05-01 16:44 UTC)

<p>The issue is that the patient name contained special characters that were encoded incorrectly.</p>
<p>If recent Windows10 versions, Slicer uses UTF8 encoding for all special characters, so I don’t know why this could have happened. Could you copy-paste here the content of the “Operating system” line in the log (it is near the very top)?</p>

---

## Post #12 by @arif (2021-05-03 11:20 UTC)

<p>Hello Andras</p>
<p>Here is the line that you asked for:</p>
<p>Operating system …: Windows / Professional / (Build 19041, Code Page 65001) - 64-bit</p>

---

## Post #13 by @lassoan (2021-05-04 17:06 UTC)

<p>This version should already fully support utf-8 encoding. Maybe the input used some unusual encoding that the DICOM importer could not interpret. Is there any chance that you can privately share the DICOM image that you imported? (you can send a private message to me by clicking on my username and then on the message icon)</p>

---

## Post #14 by @lassoan (2021-05-09 20:01 UTC)

<p>I’ve investigated the problem further with the provided dataset and the issue was that the input DICOM files used very unusual (ISO 2022 IR 100) encoding, which Slicer does not support. Strings that are stored using this encoding are imported without decoding and the resulting special characters caused syntax error in the saved scene. The syntax errors can be fixed using a text editor (by removing the special characters), but to prevent such issues in the future, I’ve submitted a fix to CTK:</p>
<aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/commontk/CTK/pull/968" target="_blank" rel="noopener">github.com/commontk/CTK</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewbox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/commontk/CTK/pull/968" target="_blank" rel="noopener">BUG: Remove invalid characters from DICOM strings with unsupported character encoding</a>
    </h4>

    <div class="branches">
      <code>commontk:master</code> ← <code>lassoan:dicom-remove-invalid-non-decoded-chars</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2021-05-09" data-time="19:41:37" data-timezone="UTC">07:41PM - 09 May 21 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/lassoan" target="_blank" rel="noopener">
          <img alt="lassoan" src="https://avatars.githubusercontent.com/u/307929?v=4" class="onebox-avatar-inline" width="20" height="20">
          lassoan
        </a>
      </div>

      <div class="lines" title="1 commits changed 1 files with 18 additions and 3 deletions">
        <a href="https://github.com/commontk/CTK/pull/968/files" target="_blank" rel="noopener">
          <span class="added">+18</span>
          <span class="removed">-3</span>
        </a>
      </div>
    </div>
  </div>
</div>

  <div class="github-row">
    <p class="github-body-container">When DICOM strings could not be decoded (because an unsupported encoding was use<span class="show-more-container"><a href="https://github.com/commontk/CTK/pull/968" target="_blank" rel="noopener" class="show-more">…</a></span><span class="excerpt hidden">d) then it was assumed to be encoded as Latin1.
This led to incorrect special characters appearing in the output and in some cases even invalid UTF8 string (causing data corruption - see https://discourse.slicer.org/t/re-failure-to-opening-saved-work/17473/5).

As a workaround, to make decoding issues more visible and avoid having random non-ASCII characters appearing in the output, we replace non-ASCII characters by '?'.

As a proper solution, DCMTK could be used to convert from all DICOM standard encodings. However, for this DMTK must be built with iconv, which seems to be quite complicated (mostly DCMTK's build system handles third-party dependencies in unusual way). Since non-supported encodings are very rare (just a few ISO 2022 IR encodings) it is probably not a serious limitation. For example, DCM4CHEE does not support any of the ISO 2022 IR encodings (https://dcm4chee-arc-cs.readthedocs.io/en/latest/charsets.html).</span></p>
  </div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
