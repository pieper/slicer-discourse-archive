# Exporting segmentation problem

**Topic ID**: 6813
**Date**: 2019-05-16
**URL**: https://discourse.slicer.org/t/exporting-segmentation-problem/6813

---

## Post #1 by @David_M (2019-05-16 10:20 UTC)

<p>Operating system: windows 7<br>
Slicer version: 4.10.1<br>
Expected behavior: Exporting the segmentation I see on the screen<br>
Actual behavior: Exporting extra volume</p>
<p>Hi, I would like to report this issue, that I can’t fix.</p>
<p>I made a segmentation<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e67091d84d7e4a9d53d122bf34f7da0b60b21c6e.png" alt="image" data-base62-sha1="wSyZR6V1y9HbFeEh9eV8Mnv0954" width="278" height="460"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d09bdb8f141b01dd8196bd3ee6c787288f783be2.png" alt="image" data-base62-sha1="tLreIj1oRUly5l5Slet5nEFq6s2" width="319" height="350"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70e4ca840aab84e997fe58a1fb3ea550439124ce.jpeg" data-download-href="/uploads/short-url/g6HESoG1GlV6SqED3FCDNJthtoy.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70e4ca840aab84e997fe58a1fb3ea550439124ce_2_690x377.jpeg" alt="image" data-base62-sha1="g6HESoG1GlV6SqED3FCDNJthtoy" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/70e4ca840aab84e997fe58a1fb3ea550439124ce_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70e4ca840aab84e997fe58a1fb3ea550439124ce.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/70e4ca840aab84e997fe58a1fb3ea550439124ce.jpeg 2x" data-dominant-color="9793A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">752×411 53.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
and this model is empty inside.</p>
<p>But when I export the segmentation<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/669205c49fe9cabe2028ea55acc5c778a8213d56.png" alt="image" data-base62-sha1="eDnykS1yjWohGyODOsIRyDNQgXY" width="230" height="147"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/2049944186ecd0994d8825e17b3d09025cc60d4a.png" alt="image" data-base62-sha1="4BCV8DDYSUMGr6z5jJHHQbgMtdg" width="618" height="280"></p>
<p>and I import the exported model as segmentation<br>
the model is full<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c0d5f022d98511ef7fef644ebd651caa624fa4d9.png" alt="image" data-base62-sha1="rvU28phToxXwlTPBBIH5SrhqiUx" width="308" height="444"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7c2d31222ad63f415535a159ae5755db9cee81a.png" alt="image" data-base62-sha1="svaqqdDtBlYOvnuliSDGAtMpyRA" width="412" height="325"></p>
<p>How can I fix this?</p>
<p>I even try to modify it again, making the label map end export it again. But that did not work</p>
<p>Thanks in advance for your help</p>

---

## Post #2 by @lassoan (2019-05-16 15:13 UTC)

<p>This is a known problem (see <a href="https://issues.slicer.org/view.php?id=4693" rel="nofollow noopener">issue in the bugtracker</a>) that affects display of some complex segmentations based on the closed surface representation. So, your segmentation is good, it is just a display issue.</p>
<p>Workaround until the display issue is fixed:</p>
<ul>
<li>Go to Segmentations module</li>
<li>In Representations section, click Create button in “Binary labelmap” row</li>
<li>In Display / Advanced section, select “Binary labelmap” for “Representation in 2D views”</li>
</ul>

---

## Post #5 by @lassoan (2021-07-02 03:33 UTC)

<p>For anybody who finds this issue - the display issue was fixed some time ago, so workarounds are not needed anymore.</p>

---
