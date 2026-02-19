---
topic_id: 5530
title: "Segmentation Visible Only In 3D"
date: 2019-01-27
url: https://discourse.slicer.org/t/5530
---

# Segmentation visible only in 3D

**Topic ID**: 5530
**Date**: 2019-01-27
**URL**: https://discourse.slicer.org/t/segmentation-visible-only-in-3d/5530

---

## Post #1 by @David_M (2019-01-27 16:45 UTC)

<p>Operating system: Windows 10<br>
Slicer version:4.10.1 (tried also with 4.10.0)<br>
Expected behavior: see segmentation in 2D<br>
Actual behavior: can see only in 3D!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d025fd322d10f336b3d496128c1329ab24ea6098.png" data-download-href="/uploads/short-url/tHmHI3QRcGkY1LofycD0uqxgD8Y.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d025fd322d10f336b3d496128c1329ab24ea6098_2_690x173.png" alt="image" data-base62-sha1="tHmHI3QRcGkY1LofycD0uqxgD8Y" width="690" height="173" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d025fd322d10f336b3d496128c1329ab24ea6098_2_690x173.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d025fd322d10f336b3d496128c1329ab24ea6098_2_1035x259.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/0/d025fd322d10f336b3d496128c1329ab24ea6098_2_1380x346.png 2x" data-dominant-color="6F707D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1891×475 85 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi</p>
<p>please help me. Unfortunately, the software does not show the painted segment on the 2D screen, just on the 3D. Do you know how can I fix this? It is crucial to me to see them since I need to make a high-resolution segmentation of the hand. Thanks</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5495ac47072da8ee5e9fa4bd4ce2e850388acc7.png" alt="image" data-base62-sha1="uqORtVNKa0Q9hR7fsBw98FAQFWn" width="566" height="471"></p>

---

## Post #2 by @lassoan (2019-01-27 16:51 UTC)

<p>Segmentation can be hidden at 6 places in Segmentations module - check all of them!</p>
<ul>
<li>overall hidden</li>
<li>overall hidden slice view</li>
<li>overall fully transparent slice view</li>
<li>overall not shown in a view</li>
<li>segment-specific hidden slice view</li>
<li>segment-specific fully transparent slice view</li>
</ul>
<p>Click on the image below to see all these controls highlighted:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/2/b2c0ec36f07e1fa48c21c26a6a99a339c921cbe6.png" data-download-href="/uploads/short-url/pvkk8khxpNhqqw897hPTaCrL0uG.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2c0ec36f07e1fa48c21c26a6a99a339c921cbe6_2_223x500.png" alt="image" data-base62-sha1="pvkk8khxpNhqqw897hPTaCrL0uG" width="223" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2c0ec36f07e1fa48c21c26a6a99a339c921cbe6_2_223x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2c0ec36f07e1fa48c21c26a6a99a339c921cbe6_2_334x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/2/b2c0ec36f07e1fa48c21c26a6a99a339c921cbe6_2_446x1000.png 2x" data-dominant-color="ECEDF0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">587×1316 59.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @David_M (2019-01-27 16:58 UTC)

<p>Dear Andras,</p>
<p>Unfortunately I have this weird situation</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/8/f8415a4503aa91a593e2075b2bbba3fc92a93b23.png" data-download-href="/uploads/short-url/zqaqEW6Ho9FvwpWKetf68Y0dUtB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8415a4503aa91a593e2075b2bbba3fc92a93b23_2_690x277.png" alt="image" data-base62-sha1="zqaqEW6Ho9FvwpWKetf68Y0dUtB" width="690" height="277" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8415a4503aa91a593e2075b2bbba3fc92a93b23_2_690x277.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8415a4503aa91a593e2075b2bbba3fc92a93b23_2_1035x415.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/8/f8415a4503aa91a593e2075b2bbba3fc92a93b23_2_1380x554.png 2x" data-dominant-color="73737D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1846×742 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks so much for your help!</p>

---

## Post #4 by @lassoan (2019-01-27 17:00 UTC)

<p>Could you please choose a segment to see if visibility is not turned off for specific segments?<br>
Could you also show a screenshot that shows the slices in the 3D view (to make sure they overlap)?</p>

---

## Post #5 by @David_M (2019-01-27 17:05 UTC)

<p>Sure!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/b/8b0d6591b7b6367c07d83fe87c1a6c44cc2fc95d.png" data-download-href="/uploads/short-url/jQ74obiDpjG36i0RHNjfRknq9dP.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b0d6591b7b6367c07d83fe87c1a6c44cc2fc95d_2_690x230.png" alt="image" data-base62-sha1="jQ74obiDpjG36i0RHNjfRknq9dP" width="690" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b0d6591b7b6367c07d83fe87c1a6c44cc2fc95d_2_690x230.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b0d6591b7b6367c07d83fe87c1a6c44cc2fc95d_2_1035x345.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/b/8b0d6591b7b6367c07d83fe87c1a6c44cc2fc95d_2_1380x460.png 2x" data-dominant-color="70707B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×641 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b5624ea351796ba845b653a5eabb2201fe3b392.png" data-download-href="/uploads/short-url/hB5i6ic4mq4P3YzvD0CNQOAbqFk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b5624ea351796ba845b653a5eabb2201fe3b392_2_690x289.png" alt="image" data-base62-sha1="hB5i6ic4mq4P3YzvD0CNQOAbqFk" width="690" height="289" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b5624ea351796ba845b653a5eabb2201fe3b392_2_690x289.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b5624ea351796ba845b653a5eabb2201fe3b392_2_1035x433.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b5624ea351796ba845b653a5eabb2201fe3b392_2_1380x578.png 2x" data-dominant-color="65656C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1900×796 276 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I hope they are ok.</p>

---

## Post #6 by @lassoan (2019-01-27 17:39 UTC)

<p>How did you create the segmentation? Maybe the segmentation only contain closed surface representation. If that’s the case, either change “Representation in 2D views” to “Closed surface” (or create a binary labelmap representation by clicking on “Create” button in “Binary labelmap” row in Representations section).</p>

---

## Post #7 by @David_M (2019-01-27 17:50 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="5530">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>(or create a binary labelmap representation by clicking on “Create” button in “Binary labelmap” row in Representations</p>
</blockquote>
</aside>
<p>I just clicked the “add segment button” in the segment editor… after a while it did not shown up the segmentation in 2D… I did not do anything…</p>
<p>I tried but apparently it does not work</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/9/a9752b25de72de50c98acbc5c2a4b370f19f51d3.png" alt="image" data-base62-sha1="ob5IWK4GtKCxIXQzvvKhaYJ5VEn" width="507" height="383"></p>

---

## Post #8 by @David_M (2019-01-27 18:06 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bba26169763321052d6498204d4850efa4d7f49.png" alt="image" data-base62-sha1="hExy9f6uFNY5kxhUkQnPy1GxRRD" width="635" height="346"></p>
<p>an interesting thing (maybe) is that if I load the saved data from on a new project (where the" 2d edit view" is functioning) i can t change the position of the slice. It is fixed at the left as in the picture</p>

---

## Post #9 by @lassoan (2019-01-27 18:22 UTC)

<p>You need to load a volume to be able to position slice viewers with the slider at the top (you can still position slice views by Shift+MouseMove in the 3D viewer).</p>
<p>How did you create the segmentation?<br>
What would you like to do (edit the segmentation, compute statistics, …)?</p>

---

## Post #10 by @David_M (2019-01-27 18:55 UTC)

<p>From the <strong>Segment Editor</strong> I just click on the <strong>Add</strong> button… after nearly 12 bones, the segmentation in 2D disappeared.</p>
<p>If I open a new model, it works perfectly.</p>
<p>I need the model to calculate the electromagnetic distributions of currents in the hand. I need to make a precise hand segmentation in order to have reliable values.</p>
<p>I am new to this software. I find it awesome, but this is bad, because after 6 hours of work probably now I can’t see another solution if not start from scratch</p>

---

## Post #11 by @lassoan (2019-01-27 22:22 UTC)

<p>We need to be able to reproduce the problem that you are experiencing to be able to help. Could you record a screen capture video and share that (or give step-by-step description of what you do exactly)?</p>

---

## Post #12 by @David_M (2019-01-28 07:34 UTC)

<div class="lazyYT" data-youtube-id="SLvYU4bODHM" data-youtube-title="Slicer 3D - How to create segments (simple)" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>
<p>Dear Andras, I uploaded here the way I did. Basically, I just added segments, used the threshold, painted the segment (sometimes I used fill between the slices) and in the end of the process I used the smoothing tools (one time for each segment, so for each bone).</p>
<p>I am wondering if there’s an upper limit to the number of segments one can make.</p>
<p>PS my project is a master thesis<br>
PPS I m going to delete that video on youtube as soon as this is solved</p>

---

## Post #13 by @David_M (2019-01-29 12:59 UTC)

<p>ok, I was able to fix the problem just by taking the old segments in a new segmentation!<br>
Since a friend of mine had the same problem, I decided to post the solution</p>
<p>Go to data and drag and drop the segments in a new segmentation (I started from scratch a new segmentation, then did that and it worked)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/7260d78808614ef8de019befdc39e5eb0de81c93.png" data-download-href="/uploads/short-url/gjPUHhMM0euUT0KAf4q6U4cMs1B.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/7260d78808614ef8de019befdc39e5eb0de81c93_2_610x499.png" alt="image" data-base62-sha1="gjPUHhMM0euUT0KAf4q6U4cMs1B" width="610" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/7260d78808614ef8de019befdc39e5eb0de81c93_2_610x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/7260d78808614ef8de019befdc39e5eb0de81c93_2_915x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/2/7260d78808614ef8de019befdc39e5eb0de81c93_2_1220x998.png 2x" data-dominant-color="8A8988"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1352×1108 275 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>If you understand why (sorry I m new to Slicer) maybe you could explain to me, truly thanks for your time!</p>

---

## Post #14 by @lassoan (2019-01-30 01:15 UTC)

<p>I don’t see any issue in the video above (segments are still visible in the slice views).</p>
<p>Note that you can probably segment the image probably 10x faster if after settings threshold range form masking, you paint a small piece in each bone then use Grow from seeds effect to create a complete segmentation.</p>

---

## Post #15 by @David_M (2019-01-30 15:08 UTC)

<p>Yes, in the youtube video I just show how I did as you asked me. After few hours of work like that the segments in the 2D screens disappeared.</p>
<p>Yes I know the grow from seed effect, but unfortunately to make a precise work it’s difficult unfortunately (segmentation of all blood vessels, tendons, fat and so on) from a 1T MRI (too low resolution I guess)… I tried but I always have overlapping and weird boundaries</p>

---

## Post #16 by @lassoan (2019-01-30 19:39 UTC)

<p>Thanks for the clarification.</p>
<p>If you send one of the scenes file where the segments are not visible in 2D then I would investigate why it could happen.</p>

---

## Post #17 by @dmarquette (2021-04-22 09:40 UTC)

<p>Hi!</p>
<p>I have the exact same problem:</p>
<p>Operating System: Ubuntu 20.04.2 LTS<br>
Slicer version: 4.11.20210226<br>
Expected behavior: see segmentation in 2D<br>
Actual behavior: can only see segmentation in 3D (even after checking all 6 locations in the Segmentations module)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c89fed4c40b46accc5efa4d5a4ccd887a4eb763a.png" data-download-href="/uploads/short-url/sCO8qJVm5t7o4J93hgEPRCXDYsa.png?dl=1" title="invisible_segment" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c89fed4c40b46accc5efa4d5a4ccd887a4eb763a_2_690x317.png" alt="invisible_segment" data-base62-sha1="sCO8qJVm5t7o4J93hgEPRCXDYsa" width="690" height="317" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c89fed4c40b46accc5efa4d5a4ccd887a4eb763a_2_690x317.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c89fed4c40b46accc5efa4d5a4ccd887a4eb763a_2_1035x475.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c89fed4c40b46accc5efa4d5a4ccd887a4eb763a_2_1380x634.png 2x" data-dominant-color="696B72"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">invisible_segment</span><span class="informations">1590×731 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Context: The segmentation has been generated by a deep neural network. Its dimensions match the dimensions of the CT scans.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> I can send you the files if you have time to look at it.</p>
<p>Thank you so much for your help <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> !</p>

---

## Post #18 by @lassoan (2021-04-22 12:07 UTC)

<p>Yes, please save the scene as .mrb file, upload it somewhere, post the link here, and I’ll have a look.</p>

---

## Post #19 by @dmarquette (2021-04-23 08:22 UTC)

<p>Here’s the link of the scene saved as an .mrb <a href="https://drive.google.com/file/d/1texx1MC8MXAZ_rrw1UnBB759gXe7OmVg/view?usp=sharing" rel="noopener nofollow ugc">file</a>.<br>
I appreciate your help !</p>

---

## Post #20 by @lassoan (2021-04-23 13:38 UTC)

<p>You don’t see the segments in slice views, because slice views bounds are set to the background volume by default, and the volume is very far from the segmentation:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b14373d8380eab61ac516f984ecb6bbf3e50807c.png" data-download-href="/uploads/short-url/pi91M1BI8bNJliIJ41LBby06s56.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b14373d8380eab61ac516f984ecb6bbf3e50807c_2_530x500.png" alt="image" data-base62-sha1="pi91M1BI8bNJliIJ41LBby06s56" width="530" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/1/b14373d8380eab61ac516f984ecb6bbf3e50807c_2_530x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b14373d8380eab61ac516f984ecb6bbf3e50807c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b14373d8380eab61ac516f984ecb6bbf3e50807c.png 2x" data-dominant-color="9798CF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">638×601 20.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>You can force your slice viewers to show the segmentation by choosing <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#view-cross-reference">“Jump slices - centered” crosshair mode</a> and moving the mouse over to the segmentation in 3D view while holding down Shift key.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/8/38f8fffa67cce70979e56e230aff7d0a2110b423.png" data-download-href="/uploads/short-url/880dwLC7pKx0ysD3HZFJgUQD9Pt.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38f8fffa67cce70979e56e230aff7d0a2110b423_2_477x500.png" alt="image" data-base62-sha1="880dwLC7pKx0ysD3HZFJgUQD9Pt" width="477" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38f8fffa67cce70979e56e230aff7d0a2110b423_2_477x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38f8fffa67cce70979e56e230aff7d0a2110b423_2_715x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/8/38f8fffa67cce70979e56e230aff7d0a2110b423_2_954x1000.png 2x" data-dominant-color="373840"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1165×1220 32.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This issue happens because the geometry if the segmentation is incorrect: the segments have (0,0,0) origin and (1,1,1) spacing. It may also cause problems elsewhere that its scalar type is float. How did you create this segmentation?</p>

---

## Post #21 by @dmarquette (2021-04-23 13:49 UTC)

<p>Thank you for your answer. It makes a lot more sense now!</p>
<p>I’m working on a deep neural network to segment two bones in the hand from CT scans. I preprocess my input scans and save them after resampling. Then, I run my model to predict the segmentation and save it. I’m going to have a look at how I save my model predictions to fix this origin problem.</p>
<p>Thank you for the hint.</p>

---

## Post #22 by @lassoan (2021-04-23 14:37 UTC)

<p>I would recommend using NRRD format, it is much simpler, it has a human-readable header, so you can immediately see if something is off, it is more flexible (as you can store arbitrary custom fields in it). Nifti has many issues, it only make sense to use it for brain imaging (that’s what it is developed for). I know that many people in the AI community use nifti was a general-purpose file format - I hope we can convince them to change this practice.</p>

---

## Post #23 by @dmarquette (2021-04-23 15:24 UTC)

<p>Thanks for the input. Unfortunately, the deep learning framework I’m using (<a href="https://docs.monai.io/en/latest/highlights.html#result-writing" rel="noopener nofollow ugc">MONAI</a>) only supports writing the model outputs as NIfTI files or PNG files for segmentation tasks. So I guess I’ll have to find a way to make it work with this format <img src="https://emoji.discourse-cdn.com/twitter/sweat.png?v=9" title=":sweat:" class="emoji" alt=":sweat:">.</p>

---

## Post #24 by @lassoan (2021-04-23 15:33 UTC)

<p>What deep learning framework do you use?</p>
<p>If the deep learning framework gives you access to the results as a numpy array then you can go and fix the output image (set the correct image origin, spacing, axis directions, and cast to unsigned short or unsigned char) and save it as nrrd (for example, using pynrrd).</p>
<p>If the deep learning framework does not give you access to the data set, only to files, then ask the developers to fix these issues for you.</p>
<p>Deep learning developers are often not familiar with common conventions in medical image computing and don’t preserve essential metadata and choose suboptimal data types and formats. If your collaborators are not sure what fixes they need to make and how, you can direct them to the Slicer forum so that we can help them.</p>

---

## Post #25 by @dmarquette (2021-04-23 15:50 UTC)

<p>I’m using <a href="https://monai.io/" rel="noopener nofollow ugc">MONAI</a> and I do have access to the torch tensor. So, I could convert it to a numpy array and then save it as nrrd. Thanks for the tip <img src="https://emoji.discourse-cdn.com/twitter/+1/2.png?v=9" title=":+1:t2:" class="emoji" alt=":+1:t2:"></p>

---

## Post #26 by @lassoan (2021-04-23 15:53 UTC)

<p>Great. We will work together with MONAI developers at the upcoming Slicer project week to ensure they better integrate with applications.</p>
<p>Did you start from one of their tutorial notebooks? Which one? Maybe just that notebook needs to be fixed up.</p>

---

## Post #27 by @dmarquette (2021-04-26 12:28 UTC)

<p>I used the <a href="https://github.com/Project-MONAI/tutorials/blob/98162169cf5aabfa205fb54bbb1d4f19167c4ba6/3d_segmentation/spleen_segmentation_3d.ipynb" rel="noopener nofollow ugc">spleen tutorial</a> and this <a href="https://github.com/Project-MONAI/tutorials/blob/98162169cf5aabfa205fb54bbb1d4f19167c4ba6/3d_segmentation/torch/unet_evaluation_dict.py" rel="noopener nofollow ugc">script</a> as a basis, and then did some minor tweaks to make it work with my custom dataset. I posted an <a href="https://github.com/Project-MONAI/MONAI/issues/2090#issue-867646561" rel="noopener nofollow ugc">issue</a> today to see how we could fix this problem on MONAI’s GitHub.</p>

---
