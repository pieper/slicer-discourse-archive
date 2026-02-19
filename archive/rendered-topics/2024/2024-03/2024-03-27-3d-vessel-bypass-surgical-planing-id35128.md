---
topic_id: 35128
title: "3D Vessel Bypass Surgical Planing"
date: 2024-03-27
url: https://discourse.slicer.org/t/35128
---

# 3d vessel bypass surgical planing

**Topic ID**: 35128
**Date**: 2024-03-27
**URL**: https://discourse.slicer.org/t/3d-vessel-bypass-surgical-planing/35128

---

## Post #1 by @mvergnat (2024-03-27 12:30 UTC)

<p>Dear Dr Lasso and all member of the 3D Slicer community,</p>
<p>Thx for all the magnificent work you do for helping healing of patients.</p>
<p>Now I have a new question:<br>
I don’t exactly know to where it belongs <strong>support? Feature request? Development?</strong><br>
I want to do 3d simulation of vessel bypass</p>
<p>I find the cardiac module baffle planner very ingenious,<br>
But this could also be very useful:</p>
<p>For example fontan surgery consist on implanting a tube from inferior vena cava to Pulmonary arteries (CHOP is the biggest center of fontan in USA)<br>
It would be nice if I could do surgical planning as follows:</p>
<ul>
<li>Define your begin of tube (3d location, form (circle or ovale or whatever))= proximal anastomosis</li>
<li>Define your end of tube (3d location, form (circle or ovale or whatever))= distal anastomosis (where do you want to implant the tube)</li>
<li>Define the path of your tube (straight, curved, multiple intermediate points?, if possible intermediate surface changes??? (would be awesome))</li>
<li>Define the thickness of your tube<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2590870d02444c4e39cde22890e7fc176296f42b.jpeg" data-download-href="/uploads/short-url/5mjjxLZDGr5Ihodr2GWs8ydKZ4v.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2590870d02444c4e39cde22890e7fc176296f42b_2_690x398.jpeg" alt="image" data-base62-sha1="5mjjxLZDGr5Ihodr2GWs8ydKZ4v" width="690" height="398" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2590870d02444c4e39cde22890e7fc176296f42b_2_690x398.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/5/2590870d02444c4e39cde22890e7fc176296f42b_2_1035x597.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/5/2590870d02444c4e39cde22890e7fc176296f42b.jpeg 2x" data-dominant-color="E5E7EA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1358×785 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ul>
<p>This could help all vessel bypass, BUT also could be used for tunnelling prediction (is the surgeon going to do a stenosis through tunnelling a cavity to another cavity…)</p>
<p>I know there is a “draw tube” but there is limited flexibility.<br>
If I find a mathematician that speaks Pithon, is it possible that he develop himself such a module??</p>
<p>Thanks for help.</p>
<p>mathieu</p>

---

## Post #2 by @pieper (2024-03-27 13:02 UTC)

<aside class="quote no-group" data-username="mvergnat" data-post="1" data-topic="35128">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/ac8455/48.png" class="avatar"> mvergnat:</div>
<blockquote>
<p>If I find a mathematician that speaks Pithon, is it possible that he develop himself such a module??</p>
</blockquote>
</aside>
<p>It requires some effort to learn, but it is our goal to facilitate such novel developments.</p>

---

## Post #3 by @mvergnat (2024-04-01 19:36 UTC)

<p>Thank you Steve!!<br>
How much time do you think it is required to build a module? (for a python user)<br>
I want to make it as much simple as possible, of course.<br>
in total, 10 hours? 24 hours?<br>
of course I wont do it by myself.</p>
<p>by the way, I am surprised/sad that my proposal does no meet enthusiasm,<br>
I found the idea pretty attractive (fontan prediction).<br>
cheers<br>
thx for your interest!</p>

---

## Post #4 by @pieper (2024-04-01 20:22 UTC)

<p>Hi <a class="mention" href="/u/mvergnat">@mvergnat</a> - your enthusiasm is appreciated and while I can’t comment on the clinical aspects what you describe sounds very cool.</p>
<p>The amount of development time really depends on the developers involved and how complex and well-specified the task is.  I have to say, in my experience the timespans are often months or years, not hours.  You can get a sense by looking for modules with comparable complexity, e.g. in VMTK or in SlicerHeart and you’ll see long histories of iterating over the design/code/test cycle to result in something that’s really usable and accurate.</p>
<p>That said, Slicer as a platform typically greatly accelerates this process compared to starting from scratch since so many important building blocks already exist, like dicom support, curves, segmentations, etc.  And even if it takes a few months of work if may still be worth the effort.</p>
<p>Maybe someone from the SlicerHeart team can comment on how close the ideas in your post are to what’s already implemented.  Maybe it’s already possible and I’m not aware or it’s easier than I think.</p>

---

## Post #5 by @lassoan (2024-04-02 12:01 UTC)

<p><a class="mention" href="/u/mvergnat">@mvergnat</a> A conduit planner module is in the works, which does something very similar what you described. Usually we release tools publicly into SlicerHeart extension when the corresponding paper is published but you may contact Matt Jolley (<a class="mention" href="/u/mattjolley">@mattjolley</a> here or at his CHOP email) to see if it is possible to get early access.</p>

---

## Post #6 by @mvergnat (2024-04-02 12:10 UTC)

<p>excellent/awesome!!!</p>
<p>once again:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7c619a0d4916f872a7686942a183264aa6cf2e6.jpeg" alt="image" data-base62-sha1="zlUmukGa0jjFaWvbuIdbpapviaq" width="176" height="176"><br>
many thx for your very kind support and suggestion!! Dr lasso!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/04b6c595eb9f02e68bfc5f8559bac73fbde0dc34.jpeg" data-download-href="/uploads/short-url/FHuNiYgP9EtJkQd8eR6hvTNSFC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04b6c595eb9f02e68bfc5f8559bac73fbde0dc34_2_345x240.jpeg" alt="image" data-base62-sha1="FHuNiYgP9EtJkQd8eR6hvTNSFC" width="345" height="240" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04b6c595eb9f02e68bfc5f8559bac73fbde0dc34_2_345x240.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04b6c595eb9f02e68bfc5f8559bac73fbde0dc34_2_517x360.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/04b6c595eb9f02e68bfc5f8559bac73fbde0dc34_2_690x480.jpeg 2x" data-dominant-color="E1D0B0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">728×508 76.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>more than grateful!<br>
I’ll proceed!</p>

---
