---
topic_id: 47606
title: "TotalSegmentator failed to install required packages"
date: 2026-07-12
url: https://discourse.slicer.org/t/47606
last_bumped: 2026-07-20T14:49:54.862Z
---

# TotalSegmentator failed to install required packages

**Topic ID**: 47606
**Date**: 2026-07-12
**URL**: https://discourse.slicer.org/t/totalsegmentator-failed-to-install-required-packages/47606

---

## Post #1 by @johny723 (2026-07-12 12:28 UTC)

<p>I keep having a similar issue - how do I fix this? Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/d/ad437beb897dacb8b1d1c66d703b4b6e949c8355.jpeg" data-download-href="/uploads/short-url/oILbyexMiGlxXMrhb20MEluuBCZ.jpeg?dl=1" title="Snímek obrazovky 2026-07-12 142815" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad437beb897dacb8b1d1c66d703b4b6e949c8355_2_690x380.jpeg" alt="Snímek obrazovky 2026-07-12 142815" data-base62-sha1="oILbyexMiGlxXMrhb20MEluuBCZ" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad437beb897dacb8b1d1c66d703b4b6e949c8355_2_690x380.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad437beb897dacb8b1d1c66d703b4b6e949c8355_2_1035x570.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/d/ad437beb897dacb8b1d1c66d703b4b6e949c8355_2_1380x760.jpeg 2x" data-dominant-color="A5A4A0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snímek obrazovky 2026-07-12 142815</span><span class="informations">1920×1059 234 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @ebrahim (2026-07-13 19:31 UTC)

<p>Does it work in Slicer 5.12.1? We made a fix related to this in the 5.12.1 patch (<a href="https://github.com/Slicer/Slicer/commit/c2975f21536bc5c6eff0ea91bf279fbb712c20c9" class="inline-onebox">BUG: Disable pip install UI off main thread · Slicer/Slicer@c2975f2 · GitHub</a>)</p>
<p>Related discussion: <a href="https://discourse.slicer.org/t/nninteractive-slicer-client-is-stuck/47550" class="inline-onebox">Nninteractive (slicer client) is stuck</a></p>

---

## Post #3 by @amyers (2026-07-14 13:12 UTC)

<p>I’m not familiar enough with the packacking.py and related code to provide a professional opinion on whether this is truly fixed. My only concern is that it started working for me in 5.12 and I have not updated to 5.12.1. My understanding was the extensions manager server code had been updated to resolve this issue.</p>

---

## Post #4 by @madsmess (2026-07-14 16:25 UTC)

<p>Hi, I’ve been having this same issue. I updated to 5.12.1, and still have the issue. I even tried downgrading to earlier versions, and have the issue (after fully uninstalling and deleting related files). I also tried using MONAI instead, and ran into the same exact error (near verbatim). I tried uninstalling all forms of Python, including any apps that may have their own Python dependencies (VSCode, Pycharm, etc.) because it almost seemed to be unable to find Pytorch despite it being there. I tried the (likely not recommended) method of manually moving/duplicating package scripts into where I know it’s checking, with no luck. I even used pip install to check, and it says Torchgen is already installed, same with torchvision. This is the error message I get:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:/Users/madim/AppData/Local/slicer.org/3D Slicer 5.12.1/slicer.org/Extensions-34624/TotalSegmentator/lib/Slicer-5.12/qt-scripted-modules/TotalSegmentator.py", line 319, in onApplyButton
    self.logic.setupPythonRequirements()
  File "C:/Users/madim/AppData/Local/slicer.org/3D Slicer 5.12.1/slicer.org/Extensions-34624/TotalSegmentator/lib/Slicer-5.12/qt-scripted-modules/TotalSegmentator.py", line 847, in setupPythonRequirements
    if not torchLogic.torchInstalled():
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:/Users/madim/AppData/Local/slicer.org/3D Slicer 5.12.1/slicer.org/Extensions-34624/PyTorch/lib/Slicer-5.12/qt-scripted-modules/PyTorchUtils.py", line 162, in torchInstalled
    metadataPath = [p for p in importlib.metadata.files('torch') if 'METADATA' in str(p)][0]
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not iterable
[Python] Failed to install required packages.
[Python] 'NoneType' object is not iterable
</code></pre>

---

## Post #5 by @madsmess (2026-07-14 19:38 UTC)

<p>Okay so I think I may have fixed it: for me, when I install slicer it automatically wants to be installed inside AppData, so I tried uninstalling it, then reinstalling the latest version just inside my C drive. I did not put it inside any subfolder, and now it appears to be working. I think if you let it install inside AppData the pathing for finding packages gets wonky.</p>

---

## Post #6 by @Emily_Crowe (2026-07-20 14:49 UTC)

<p>Hi Madisyn!  Thanks so much for your tips, I uninstalled and reinstalled Slicer in the C:\ drive and was finally able to download TotalSegmentator. When I tried to run it, I got the following error:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1edb4ace291999550d4c3640e1346d0406f9991a.png" data-download-href="/uploads/short-url/4oY9DKG4b2CZQrjDA3P8dAq62wy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1edb4ace291999550d4c3640e1346d0406f9991a.png" alt="image" data-base62-sha1="4oY9DKG4b2CZQrjDA3P8dAq62wy" width="547" height="191"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">547×191 23 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And noticed it was still pulling a path from AppData.  Do you have any recommendations?  Thanks again!</p>

---
