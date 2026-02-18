# Lung CT segmenter

**Topic ID**: 21493
**Date**: 2022-01-17
**URL**: https://discourse.slicer.org/t/lung-ct-segmenter/21493

---

## Post #1 by @opetne (2022-01-17 13:27 UTC)

<p>Operation system: Windows 10<br>
Slcier version: 4.11 20210226</p>
<p>I tried to run the Lung CT segmenter module on a dog CT series.<br>
Preview was ok but after applying I got this error message:<br>
Saving fiducials in root directory …<br>
Saving fiducials in volume directory …<br>
Failed to compute results: expected str, bytes or os.PathLike object, not NoneType<br>
Traceback (most recent call last):<br>
File “C:/Users/petnehazyors/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/LungCTAnalyzer/lib/Slicer-4.11/qt-scripted-modules/LungCTSegmenter.py”, line 397, in onApplyButton<br>
self.saveFiducialsGlobalAndLocal()<br>
File “C:/Users/petnehazyors/AppData/Local/NA-MIC/Slicer 4.11.20210226/NA-MIC/Extensions-29738/LungCTAnalyzer/lib/Slicer-4.11/qt-scripted-modules/LungCTSegmenter.py”, line 465, in saveFiducialsGlobalAndLocal<br>
baseFolder, tail = os.path.split(inputFilename)<br>
File “C:/Users/petnehazyors/AppData/Local/NA-MIC/Slicer 4.11.20210226/bin/…/lib/Python/Lib\ntpath.py”, line 205, in split<br>
p = os.fspath(p)<br>
TypeError: expected str, bytes or os.PathLike object, not NoneType</p>
<p>Where was the problem and how can I solve it?</p>
<p>Thank you in advance</p>

---

## Post #2 by @cpinter (2022-01-17 13:37 UTC)

<p>The error message suggests that maybe empty path was given? I guess not, but double-checking (looking at the log you were kind to paste, it seems it got past the first round of saving). Is this module available for the latest Preview version (almost 5.0 so time to try to switch)? If so, does the error occur in that as well? Thanks!</p>

---

## Post #3 by @opetne (2022-01-17 14:16 UTC)

<p>Dear Csaba,</p>
<p>Thank you for the answer. I ran into another problem trying to download the latest version. It is not possible to download it…</p>
<p>Best,</p>
<p>Ors</p>
<p>Csaba Pinter via 3D Slicer Community &lt;<a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>&gt; ezt írta (időpont: 2022. jan. 17., H, 14:37):</p>

---

## Post #4 by @rbumm (2022-01-18 08:43 UTC)

<p>Thanks for your report.</p>
<p>I just tested the LungCTSegmenter and do not get this exception when loading a CT dataset from my local harddrive.<br>
In your case, <code>inputFilename</code> is obviosly empty for some reason and so the exception is thrown.<br>
Will try to fix this, but:</p>
<p>How did you load the CT data?<br>
What version does LungCTAnalyzer show on your system ?</p>

---

## Post #5 by @rbumm (2022-01-18 08:46 UTC)

<p>How did you try to download it?<br>
I have no problem installing the LungCTAnalyzer extension from the Extensions Manager in 4.11.<br>
Could you provide more details?</p>

---

## Post #6 by @opetne (2022-01-18 09:17 UTC)

<p>Dear Rudolf,</p>
<p>I tried to download the Slicer latest release and this didn’t work.</p>
<p>Best,</p>
<p>Ors</p>
<p>Rudolf Bumm via 3D Slicer Community &lt;<a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>&gt; ezt írta (időpont: 2022. jan. 18., K, 9:46):</p>

---

## Post #7 by @opetne (2022-01-18 09:20 UTC)

<p>Dear Rudolf,</p>
<p>I’ve found the solution for the Lung CT segmenter problem based on your comment. The problem was:</p>
<ol>
<li>I downloaded from our server a series with Radiant</li>
<li>Radiant put 2 series from 2 separate dogs in 1 folder.</li>
<li>Slicer recognized this as two separate examinations</li>
<li>The original folder didn’t contain any information with the same name as Slicer recognised the series.</li>
</ol>
<p>Now I separated the series and made the folders with the appropriate names and it works.</p>
<p>Thank you for the suggestion!</p>
<p>Best regards,</p>
<p>Ors</p>
<p>Rudolf Bumm via 3D Slicer Community &lt;<a href="mailto:slicer@discoursemail.com">slicer@discoursemail.com</a>&gt; ezt írta (időpont: 2022. jan. 18., K, 9:43):</p>

---

## Post #8 by @rbumm (2022-01-18 09:21 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70b047465165012da5a3a48f1c91778a98775ff5.png" data-download-href="/uploads/short-url/g4T9och3SzfjysbswKRbvhFbsd7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70b047465165012da5a3a48f1c91778a98775ff5.png" alt="image" data-base62-sha1="g4T9och3SzfjysbswKRbvhFbsd7" width="690" height="200" data-dominant-color="F9FAF9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">965×281 9.74 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Click one of the preview release buttons, download is starting here without problems …</p>
<p>Your problem will probably be unrelated to these Slicer versions because LungCTAnalyzer works in both stable and preview release.</p>

---

## Post #9 by @rbumm (2022-01-18 09:23 UTC)

<p>Great, I have implemented a small change in the LungCTSegmenter and -Analyzer source (V2.46) to avoid the exception in the future.</p>

---
