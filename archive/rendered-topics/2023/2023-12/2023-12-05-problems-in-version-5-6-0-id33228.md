---
topic_id: 33228
title: "Problems In Version 5 6 0"
date: 2023-12-05
url: https://discourse.slicer.org/t/33228
---

# Problems in version 5.6.0

**Topic ID**: 33228
**Date**: 2023-12-05
**URL**: https://discourse.slicer.org/t/problems-in-version-5-6-0/33228

---

## Post #1 by @hepato (2023-12-05 13:20 UTC)

<p>I update slicer to version 5.6.0 and some error occured.</p>
<p>1.Maximize or restore views by double click of left key of mouse  stopped working.<br>
2.“patient name” not showed in  DICOM database.</p>
<p>Would you check and repair those problems?</p>

---

## Post #2 by @rbumm (2023-12-05 13:47 UTC)

<p>I can confirm (1), that views do not get maximized by double left click.<br>
Funny enough it has stopped working in 4.11 too … ?!</p>

---

## Post #3 by @hepato (2023-12-05 14:53 UTC)

<p>But It worked in last version of 5.5.0.<br>
At first I wander if It was caused by the update of MacOS system, but other software still work well with double click. So I think that maybe It was caused by the update of slicer.<br>
The function of Maximizing or restoring views can also be done with clicking of the button in the view control bar or right-click menu.<br>
But double clicking is more convenient for me.<br>
Hopeful for its return!</p>

---

## Post #4 by @jcfr (2023-12-05 16:26 UTC)

<aside class="quote no-group" data-username="hepato" data-post="1" data-topic="33228">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/3da27b/48.png" class="avatar"> hepato:</div>
<blockquote>
<p>1.Maximize or restore views by double click of left key of mouse stopped working.</p>
</blockquote>
</aside>
<p>This has been addressed and the fix will be integrated as part the upcoming patch release <code>5.6.1</code></p>
<p>For reference, see <a href="https://discourse.slicer.org/t/new-feature-maximize-view/19581/16" class="inline-onebox">New feature: maximize view - #16 by jcfr</a></p>

---

## Post #5 by @lassoan (2023-12-05 16:58 UTC)

<p>2 posts were split to a new topic: <a href="/t/view-controller-bar-is-thicker-in-slicer-5-6-0/33238">View controller bar is thicker in Slicer-5.6.0</a></p>

---

## Post #7 by @pieper (2023-12-05 16:56 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> now that the styling infrastructure is improved can we easily make the bar thinner?</p>
<p><a class="mention" href="/u/hepato">@hepato</a> Can you provide more info on the missing patient name issue?</p>

---

## Post #8 by @lassoan (2023-12-05 20:20 UTC)

<p>A post was merged into an existing topic: <a href="/t/view-controller-bar-is-thicker-in-slicer-5-6-0/33238/3">View controller bar is thicker in Slicer-5.6.0</a></p>

---

## Post #9 by @hepato (2023-12-06 10:28 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/6099ad99a17a48ca2901468dfb2270f3e5002c07.png" data-download-href="/uploads/short-url/dMz5DUCAPsmh9twEN55mSqUMOkD.png?dl=1" title="截屏2023-12-06 18.20.40" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6099ad99a17a48ca2901468dfb2270f3e5002c07_2_690x431.png" alt="截屏2023-12-06 18.20.40" data-base62-sha1="dMz5DUCAPsmh9twEN55mSqUMOkD" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6099ad99a17a48ca2901468dfb2270f3e5002c07_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6099ad99a17a48ca2901468dfb2270f3e5002c07_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/6099ad99a17a48ca2901468dfb2270f3e5002c07_2_1380x862.png 2x" data-dominant-color="F3F4F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2023-12-06 18.20.40</span><span class="informations">2880×1800 298 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>not happened in old version.</p>

---

## Post #10 by @chir.set (2023-12-06 10:57 UTC)

<aside class="quote no-group" data-username="hepato" data-post="9" data-topic="33228">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/3da27b/48.png" class="avatar"> hepato:</div>
<blockquote>
<p>not happened in old version.</p>
</blockquote>
</aside>
<p>I can confirm that 5.6.0 on Linux <strong>DOES</strong> show the patient name. The error probably lies in the study identification where this field was missed. Reading another study may help.</p>

---

## Post #11 by @hepato (2023-12-06 11:07 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/3/83965f069b347cd832eb76762e77e42b01402126.png" data-download-href="/uploads/short-url/iM4ItN1i9DlQU7A57ynLzVHQvmC.png?dl=1" title="截屏2023-12-06 19.05.27" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83965f069b347cd832eb76762e77e42b01402126_2_690x431.png" alt="截屏2023-12-06 19.05.27" data-base62-sha1="iM4ItN1i9DlQU7A57ynLzVHQvmC" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83965f069b347cd832eb76762e77e42b01402126_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83965f069b347cd832eb76762e77e42b01402126_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/3/83965f069b347cd832eb76762e77e42b01402126_2_1380x862.png 2x" data-dominant-color="E3E7EC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">截屏2023-12-06 19.05.27</span><span class="informations">2880×1800 474 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>try again, still missed</p>

---

## Post #12 by @pieper (2023-12-06 13:13 UTC)

<p><a class="mention" href="/u/hepato">@hepato</a> please link to a public dicom study that replicates the issue.</p>

---

## Post #13 by @hepato (2023-12-06 14:08 UTC)

<aside class="quote no-group" data-username="pieper" data-post="12" data-topic="33228">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>public dicom study</p>
</blockquote>
</aside>
<p>I resolved that problem when I deleted all the files (ctkDICOMTagCache.sql, ctkDICOM.sql) in dicom database.<br>
Maybe some old files in dicom database were not deleted when I uninstall the slicer.<br>
Sorry to bother you and thanks for your answer!</p>

---

## Post #14 by @pieper (2023-12-06 14:34 UTC)

<p>Thanks for reporting back.  We’ll keep an eye out for any similar issues that come up with the dicom database infrastructure.  It’s been around for a long time and is pretty reliable but we are looking at upgrades to improve performance and reliablility.</p>

---
