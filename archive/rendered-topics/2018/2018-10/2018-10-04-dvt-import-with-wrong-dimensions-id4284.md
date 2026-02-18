# DVT import with wrong dimensions

**Topic ID**: 4284
**Date**: 2018-10-04
**URL**: https://discourse.slicer.org/t/dvt-import-with-wrong-dimensions/4284

---

## Post #1 by @Christoph_Chris (2018-10-04 15:01 UTC)

<p>Operating system: WIndows 10<br>
Slicer version: 4.8.1</p>
<p>Problem: iam trying to import a single dicom file of a patients dvt. The sagittal and coronal dimension are not correct. iam wondering if this is a problem during importing the file or is it just an issue of viewing settings`</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8f25a3b9094020cfd4af91d741c324ff5f986a67.jpeg" data-download-href="/uploads/short-url/kqkV4RRito4JlaIE6SqwM6XdKOb.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f25a3b9094020cfd4af91d741c324ff5f986a67_2_656x500.jpeg" alt="PNG" data-base62-sha1="kqkV4RRito4JlaIE6SqwM6XdKOb" width="656" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f25a3b9094020cfd4af91d741c324ff5f986a67_2_656x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f25a3b9094020cfd4af91d741c324ff5f986a67_2_984x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8f25a3b9094020cfd4af91d741c324ff5f986a67_2_1312x1000.jpeg 2x" data-dominant-color="4B4B57"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1380×1051 265 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @cpinter (2018-10-04 15:20 UTC)

<p>Do you use the DICOM browser module to load the image?</p>

---

## Post #3 by @Christoph_Chris (2018-10-04 15:49 UTC)

<p>when i do this, it shows a warning: " there is no pixel data attribute for the dicom objects…" ; and when i try to load it, it shows: “could not load … scalar volume”</p>
<p>The file is straight from our dvt machine an is showing properly in the software provided by the manufacturer</p>
<p>thanks!</p>

---

## Post #4 by @lassoan (2018-10-04 16:46 UTC)

<p>I’m not sure what you mean by “DVT machine”. Can you tell  the name of manufacturer and model?</p>
<p>Most likely the machine exports DICOM images incorrectly. If you have a service contract then you should be able to report this to the manufacturer and they should fix it in a future software release. If you can share an anonymized or non-patient data set then we can give you the details about what should be changed exactly.</p>
<p>Some Dolphin CBCT machines use slice thickness field incorrectly, which results in similarly distorted images. Maybe your device has the same issue. This problem can be fixed by DICOM Patcher module:</p>
<ul>
<li>Install latest nightly version of Slicer (and use that for the next steps)</li>
<li>Delete this data set from Slicer DICOM database (DICOM module)</li>
<li>Use “DICOM Patcher” module on your data set, make sure “Generate slice position for multi-frame volumes” is enabled</li>
<li>Re-import the data set into Slicer DICOM database</li>
</ul>

---

## Post #5 by @Christoph_Chris (2019-02-20 20:04 UTC)

<p>Hello,<br>
sorry it took me a while to reproduce the problem.<br>
you were right the patcher module fixed the problem of the wrong dimensions, but now the slices are mirrored (probably they were mirrored from the beginning, i just didnt realise)<br>
i uploaded an anonymized dataset to my dropbox. maybe you could have a look. (<a href="https://www.dropbox.com/sh/dmrgdv5ov7i5dh0/AABran4WXSe7u9rtOWMejKoya?dl=0" rel="nofollow noopener">https://www.dropbox.com/sh/dmrgdv5ov7i5dh0/AABran4WXSe7u9rtOWMejKoya?dl=0</a>)<br>
by dvt machinne, i mean a cone beam CT. the manufacturer is Kavo, but i dont know the exact model</p>
<p>Thank you!</p>

---
