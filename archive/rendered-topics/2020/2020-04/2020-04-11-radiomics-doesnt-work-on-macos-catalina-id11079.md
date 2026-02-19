---
topic_id: 11079
title: "Radiomics Doesnt Work On Macos Catalina"
date: 2020-04-11
url: https://discourse.slicer.org/t/11079
---

# Radiomics doesn't work on macOS Catalina

**Topic ID**: 11079
**Date**: 2020-04-11
**URL**: https://discourse.slicer.org/t/radiomics-doesnt-work-on-macos-catalina/11079

---

## Post #1 by @Andrea_Barucci1 (2020-04-11 13:55 UTC)

<p>Dear all,</p>
<p>I apologise if this question has already found an answer.<br>
I have not been able to find the solution to this problem.</p>
<p>Despite the version of 3D Slicer I’m trying to run I always face the same error when trying to extract features:</p>
<p>Feature calculation failed.<br>
Feature calculation failed.<br>
Traceback (most recent call last):<br>
File “/Applications/Slicer.app/Contents/Extensions-27931/SlicerRadiomics/lib/Slicer-4.10/qt-scripted-modules/SlicerRadiomics.py”, line 405, in onApplyButton<br>
self.onFinished)<br>
File “/Applications/Slicer.app/Contents/Extensions-27931/SlicerRadiomics/lib/Slicer-4.10/qt-scripted-modules/SlicerRadiomics.py”, line 732, in runCLI<br>
with open(parameterFile, mode=‘w’) as parameterFileFP:<br>
IOError: [Errno 2] No such file or directory: u’/var/folders/2m/y_0dhzcd4wd891w6s6xht4tm0000gn/T/Slicer-andrea/RadiomicsLogicParams.json’</p>
<p>I was able to perform this extraction until I changed operating system, jumping in macOS 10.15.3 Catalina.</p>
<p>Do you know if this problem can be rated to the operating system or instead southing is going wrong in my installation?</p>
<p>Please consider that I’m not an expert user.</p>
<p>Thank you very much in advice for your support</p>
<p>Best regards<br>
Andrea from Italy</p>

---

## Post #2 by @pieper (2020-04-12 16:08 UTC)

<p>Hi -</p>
<p>Probably upgrading the OS changed the temp directory logic a bit.  By default you get the OS assigned tmp and it gets saved in the settings (e.g. so you could change it to a different disk or something if needed).</p>
<p>You can change it in the Application Settings (in Edit menu).</p>
<p>Let us know if that doesn’t work.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/1/81789142b89ba2a98444588ccad27a9e118f7841.png" data-download-href="/uploads/short-url/itlUj8g3Y85Pa36Mf5vzcJFc0BX.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81789142b89ba2a98444588ccad27a9e118f7841_2_690x144.png" alt="image" data-base62-sha1="itlUj8g3Y85Pa36Mf5vzcJFc0BX" width="690" height="144" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81789142b89ba2a98444588ccad27a9e118f7841_2_690x144.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81789142b89ba2a98444588ccad27a9e118f7841_2_1035x216.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/1/81789142b89ba2a98444588ccad27a9e118f7841_2_1380x288.png 2x" data-dominant-color="E3E5E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1588×332 54.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
