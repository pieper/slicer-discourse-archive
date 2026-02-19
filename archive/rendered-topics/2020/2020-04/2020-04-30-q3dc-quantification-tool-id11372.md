---
topic_id: 11372
title: "Q3Dc Quantification Tool"
date: 2020-04-30
url: https://discourse.slicer.org/t/11372
---

# Q3DC Quantification Tool

**Topic ID**: 11372
**Date**: 2020-04-30
**URL**: https://discourse.slicer.org/t/q3dc-quantification-tool/11372

---

## Post #1 by @Joao_L (2020-04-30 21:06 UTC)

<p>Operating system:<br>
Slicer version: 5.0<br>
Expected behavior: Calculating angle between two lines using Q3DC Quantificatio tool.<br>
Actual behavior: When choosing landmarks of two different stl. archives and selecting the options “calculate pich”, “calculate roll” and “calculate yaw”, I click “calculate” expecting find the angle measures right below, but an advise “ERROR, norm of your vector is 0! DEFINE A VECTOR!” appears. I’ve tried selecting the stl. archives and their corresponding landmarks in “model of reference” and “connected landmarks”, but it didn’t work. Can anybody help me with that?</p>

---

## Post #2 by @lassoan (2020-05-01 16:28 UTC)

<p>Double-check your points. <em>“ERROR, norm of your vector is 0! DEFINE A VECTOR!”</em> message is displayed when you choose the same position for two endpoints of a line.</p>

---

## Post #3 by @yf025 (2020-05-04 08:28 UTC)

<p>Where did you get slicer 5.0？</p>

---

## Post #4 by @jamesobutler (2020-05-04 12:26 UTC)

<p><a class="mention" href="/u/yf025">@yf025</a> Slicer 5.0 is not released, but Slicer 4.11 preview will eventually become it, if you want to try out the latest features that will be included in the release.</p>

---

## Post #5 by @Joao_L (2020-05-04 17:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="11372" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Double-check your points. <em>“ERROR, norm of your vector is 0! DEFINE A VECTOR!”</em> message is displayed when you choose the same position for two endpoints of a line.</p>
</blockquote>
</aside>
<p>Thank you for your answer.</p>

---

## Post #6 by @Joao_L (2020-05-04 17:31 UTC)

<p>I checked the points - they were not at the same position. It worked when I reduced the landmark’s size from 2.1 to 1mm. Seems like a bug, I don’t know. If you can help with one more thing: now that I got the measures I want, I can’t select the number inside the cell to copy and paste it in excel. Do you know any way to export this values?</p>

---

## Post #7 by @James_Hoctor (2020-05-05 14:15 UTC)

<p>Click on the “Export” button beneath the table.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8751cc12555ea89f8b26c65e98a0b393e7be49c.png" data-download-href="/uploads/short-url/sBkpaYUVpV7vY2odcj4q5MhPkeM.png?dl=1" title="Screenshot from 2020-05-05 09-58-24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8751cc12555ea89f8b26c65e98a0b393e7be49c_2_465x500.png" alt="Screenshot from 2020-05-05 09-58-24" data-base62-sha1="sBkpaYUVpV7vY2odcj4q5MhPkeM" width="465" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8751cc12555ea89f8b26c65e98a0b393e7be49c_2_465x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8751cc12555ea89f8b26c65e98a0b393e7be49c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8751cc12555ea89f8b26c65e98a0b393e7be49c.png 2x" data-dominant-color="F5F5F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2020-05-05 09-58-24</span><span class="informations">656×704 44.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The menu to the left of this button can be used to select the directory in which to save. The file name will always be “angle.csv”.</p>
<p>Better ways to save and perhaps even copy-paste are coming in the future.</p>

---

## Post #8 by @Joao_L (2020-05-05 21:16 UTC)

<p>Thank you very much!</p>

---

## Post #9 by @lassoan (2020-05-25 14:12 UTC)

<p>A post was merged into an existing topic: <a href="/t/exporting-values-of-angle-between-two-lines-q3dc-doesnt-work/11694/2">Exporting values of “angle between two lines” (Q3DC) doesn’t work</a></p>

---
