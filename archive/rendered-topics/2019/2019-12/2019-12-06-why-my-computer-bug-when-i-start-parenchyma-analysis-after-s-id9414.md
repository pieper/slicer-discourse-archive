---
topic_id: 9414
title: "Why My Computer Bug When I Start Parenchyma Analysis After S"
date: 2019-12-06
url: https://discourse.slicer.org/t/9414
---

# Why my computer bug when I start parenchyma analysis after segmentation?

**Topic ID**: 9414
**Date**: 2019-12-06
**URL**: https://discourse.slicer.org/t/why-my-computer-bug-when-i-start-parenchyma-analysis-after-segmentation/9414

---

## Post #1 by @Benjamin_Coiffard (2019-12-06 14:37 UTC)

<p>Operating system: MacBookPro11,1 ; intel Core i5; 2,6GHz; RAM 8Go<br>
Slicer version: SlicerCIP 4.10.2</p>
<p>Why my computer bug when I start parenchyma analysis after segmentation?<br>
I can segment lungs and lobes but the software bug when I perform parenchyma analysis to obtain lung densitometry…<br>
Is my computer not powerful enough</p>
<p>Thanks<br>
Benjamin</p>

---

## Post #2 by @pieper (2019-12-06 14:53 UTC)

<p>Hi -</p>
<p>Can you post the error log and more details as described here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Report_a_problem" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Report_a_problem</a></p>
<p>Thanks</p>

---

## Post #3 by @Benjamin_Coiffard (2019-12-06 15:18 UTC)

<p>Hi Steve,<br>
Thank you for your rapid answer.<br>
I’m not a developer so I can’t do anything manually…<br>
I notice first that when I click on Filtering “On” nothing appears.<br>
Second When I apply for parenchyma analysis from my CT images (precising Label Map Volume = None) segmentation appears but no “Histogram” and no “Chart section”.<br>
Then when I apply with Label Map Volume = myCTpartialLungLabelMap (segmentation) it starts analysing and then shut down…<br>
I can’t say anymore.<br>
See screenshot attached if it’s working<br>
Regards<br>
Benjamin<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/3612cedb91dc2cb115261bdf38dd56f0cb5fa823.png" data-download-href="/uploads/short-url/7Im4VmFk7EPa0kit9CsnBweHg6D.png?dl=1" title="Capture d’écran 2019-12-06 à 10.05.49" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3612cedb91dc2cb115261bdf38dd56f0cb5fa823_2_690x431.png" alt="Capture d’écran 2019-12-06 à 10.05.49" data-base62-sha1="7Im4VmFk7EPa0kit9CsnBweHg6D" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3612cedb91dc2cb115261bdf38dd56f0cb5fa823_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3612cedb91dc2cb115261bdf38dd56f0cb5fa823_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3612cedb91dc2cb115261bdf38dd56f0cb5fa823_2_1380x862.png 2x" data-dominant-color="C6C1CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2019-12-06 à 10.05.49</span><span class="informations">2880×1800 1.23 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @jamesobutler (2019-12-06 16:01 UTC)

<p>Nothing happens when you click “Filtering on” because there is <code>AttributeError: QFrame has no attribute named 'setShown'</code>.  This is a problem with the code <a href="https://github.com/acil-bwh/SlicerCIP/blob/develop/Scripted/CIP_/CIP/ui/PreProcessingWidget.py#L200-L204" rel="nofollow noopener">here</a>. <code>setShown</code> is specifically a Qt3 thing that was supported in Qt4 to help with that transition of 3 to 4. That transition happened a long time ago, so not sure how much effort is being put into SlicerCIP recently. Unclear if SlicerCIP will be updated for Slicer5/Slicer-preview which includes the transition to Qt5.</p>
<p><a class="mention" href="/u/jcfr">@jcfr</a> and <a class="mention" href="/u/cpinter">@cpinter</a> have issued some commits to SlicerCIP in the past, but I’m not sure who the best person to contact would be to fix various issues in the code. You say you’re not a developer, but you could potentially create a GitHub account and post an issue to <a href="https://github.com/acil-bwh/SlicerCIP/issues" rel="nofollow noopener">https://github.com/acil-bwh/SlicerCIP/issues</a> detailing the problems that you are seeing.</p>

---

## Post #5 by @jcfr (2019-12-06 22:11 UTC)

<p>Look like this particular issue has been addressed in <a href="https://github.com/acil-bwh/SlicerCIP/commit/115959155cdb5f6bfbeffc6c1f794fcb6bdeb509">https://github.com/acil-bwh/SlicerCIP/commit/115959155cdb5f6bfbeffc6c1f794fcb6bdeb509</a></p>
<p>Thanks  <a class="mention" href="/u/pnardelli">@PNardelli</a>  <img src="https://emoji.discourse-cdn.com/twitter/pray.png?v=9" title=":pray:" class="emoji" alt=":pray:"></p>
<p>Since the extensionIndex is already <a href="https://github.com/Slicer/ExtensionsIndex/blob/4468a15a5ca7cc1ae54d84c7b8abb8286d998eb8/Chest_Imaging_Platform.s4ext#L10-L11">associated</a> with the <code>develop</code> branch where the fix has been integrated, tomorrow extensions should include the fix <img src="https://emoji.discourse-cdn.com/twitter/tada.png?v=9" title=":tada:" class="emoji" alt=":tada:"></p>

---

## Post #6 by @pieper (2019-12-10 20:15 UTC)

<p><a class="mention" href="/u/benjamin_coiffard">@Benjamin_Coiffard</a> are you able to confirm the fix that <a class="mention" href="/u/pnardelli">@PNardelli</a> provide?</p>

---

## Post #7 by @Benjamin_Coiffard (2019-12-10 21:13 UTC)

<p>Hi Steve,<br>
You know those scripts are just Chinese for me.<br>
I tried to put this one in the Python Interactor put it doesn’t work from that point…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d7983f45f2d9d49038423c84263b290b0628d6d.png" data-download-href="/uploads/short-url/b3n6SbuEdvFvn5aYELoGuRqDThH.png?dl=1" title="Capture d’écran 2019-12-10 à 16.11.45" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d7983f45f2d9d49038423c84263b290b0628d6d_2_690x431.png" alt="Capture d’écran 2019-12-10 à 16.11.45" data-base62-sha1="b3n6SbuEdvFvn5aYELoGuRqDThH" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d7983f45f2d9d49038423c84263b290b0628d6d_2_690x431.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d7983f45f2d9d49038423c84263b290b0628d6d_2_1035x646.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4d7983f45f2d9d49038423c84263b290b0628d6d_2_1380x862.png 2x" data-dominant-color="F6F1F1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture d’écran 2019-12-10 à 16.11.45</span><span class="informations">2880×1800 1.03 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @pieper (2019-12-10 21:48 UTC)

<aside class="quote no-group" data-username="Benjamin_Coiffard" data-post="7" data-topic="9414">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/benjamin_coiffard/48/5335_2.png" class="avatar"> Benjamin_Coiffard:</div>
<blockquote>
<p>those scripts are just Chinese for me.</p>
</blockquote>
</aside>
<p>haha <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"></p>
<p>But if you download a new nightly build of Slicer you should be able to install the latest CIP extension.</p>

---

## Post #9 by @Benjamin_Coiffard (2019-12-10 22:55 UTC)

<p>Thanks Steve<br>
But I tried already but I don’t even know how to install the latest CIP extension on 3D Slicer version 11. There is now CIP in the Extensions Manager.<br>
I’m going crazy… I really need to use CIP…</p>

---

## Post #10 by @pieper (2019-12-11 15:16 UTC)

<p>It looks like there are still some problems with the build and that’s why the extension is not showing up.</p>
<p><a class="mention" href="/u/pnardelli">@PNardelli</a> do you know how to fix these?</p>
<p><a href="http://slicer.cdash.org/viewBuildError.php?buildid=1771659" class="onebox" target="_blank">http://slicer.cdash.org/viewBuildError.php?buildid=1771659</a></p>
<p><a href="http://slicer.cdash.org/viewBuildError.php?buildid=1771866" class="onebox" target="_blank">http://slicer.cdash.org/viewBuildError.php?buildid=1771866</a></p>

---
