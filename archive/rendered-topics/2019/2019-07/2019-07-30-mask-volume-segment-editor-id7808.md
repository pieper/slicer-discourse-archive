---
topic_id: 7808
title: "Mask Volume Segment Editor"
date: 2019-07-30
url: https://discourse.slicer.org/t/7808
---

# Mask volume- segment editor

**Topic ID**: 7808
**Date**: 2019-07-30
**URL**: https://discourse.slicer.org/t/mask-volume-segment-editor/7808

---

## Post #1 by @Melanie (2019-07-30 09:36 UTC)

<p>Hi all</p>
<p>I have tried masking a volume with segment editor. Can I completely erase the masked volume , so that unmasked bit remains. I want to use elastic registration on the unmasked volume. But as it remains masked, it’s not visible but gets registered as total volume. Thanks</p>

---

## Post #2 by @lassoan (2019-07-30 13:42 UTC)

<p>Mask volume effect does not change the extent of the volume. You can use Crop volume module to make the volume smaller.</p>

---

## Post #3 by @Melanie (2019-07-30 17:12 UTC)

<p>Thanks.</p>
<p>Is there an option to delete / erase part of the volume. I tried surface cut/ scissors but erase outside option doesn’t work. Thanks</p>

---

## Post #4 by @cpinter (2019-07-30 17:37 UTC)

<aside class="quote no-group" data-username="Melanie" data-post="3" data-topic="7808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>erase outside option doesn’t work</p>
</blockquote>
</aside>
<p>It does, both in stable and in nightly. Can you please explain how you try to do it and why do you think it doesn’t work?</p>

---

## Post #5 by @Melanie (2019-07-30 18:24 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a></p>
<p>It works within a segment. But what I tried was to create a segment of the area that I m not interested, then cut it out to leave my interested area as a volume, not making it a STL.</p>
<p>All I m trying to do is create a custom shaped region of interest , and keep it as a volume , not a segment, so I can use elastix on that.<br>
Cropping creates rectangular ROI , I m looking for an option where I can cut and delete a custom area of a CT volume and keep my interested area as a ct volume.</p>
<p>Thanks</p>

---

## Post #6 by @lassoan (2019-07-30 18:27 UTC)

<p>Mask volume effect (provided by SegmentEditorExtraEffects extension) can blank out a volume inside or outside a selected segment.</p>

---

## Post #7 by @muratmaga (2019-07-30 18:29 UTC)

<p>I just tried and works fine with both nightly and stable. However, Slicer doesnt automatically change the volume displayed to the newly created volume. Make sure you are looking at the right volume.</p>

---

## Post #8 by @Melanie (2019-07-30 19:05 UTC)

<p>Thanks ever so much all of you.</p>
<p>Apologies, I m not getting this right.</p>
<p>In segment editor , I add a segment, then with scissors I mark my area of interest and select the option fill outside. Then I add s mask to mask the filled segment. Then I try to register the unmasked bit of the volume with elastix. But this registers the whole volume that’s been masked too, not only the unmasked bit.</p>
<p>Second option I tried was again, went to segment editor, Add segment button then use scissors with the erase outside option. Nothing happened. But if I use the fill outside option it fills.</p>
<p>If I do this to an already created segment/ stl scissors can delete part of the segment.</p>
<p>Thanks</p>

---

## Post #9 by @lassoan (2019-07-30 20:05 UTC)

<aside class="quote no-group" data-username="Melanie" data-post="8" data-topic="7808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>I mark my area of interest and select the option fill outside.</p>
</blockquote>
</aside>
<p>To keep things simple, make the segment cover the region you are interested in. Then, you can us Mask volume effect to blank out the parts outside your region of interest.</p>
<aside class="quote no-group" data-username="Melanie" data-post="8" data-topic="7808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>If I do this to an already created segment/ stl scissors can delete part of the segment.</p>
</blockquote>
</aside>
<p>Yes, this is correct. All effects (Scissors, Surface cut, Paint, etc.) only modify segments. They will not modify any volume nodes.</p>
<aside class="quote no-group" data-username="Melanie" data-post="8" data-topic="7808">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/35a633/48.png" class="avatar"> Melanie:</div>
<blockquote>
<p>Then I try to register the unmasked bit of the volume with elastix.</p>
</blockquote>
</aside>
<p>If you blank out a region of a volume, Elastix will still take those voxels into account. This is probably not what you want.</p>
<p>To make Elastix ignore certain regions then you can specify masks in “Masking” section in “General registration (Elastix)” module. You can create a mask volume by using “Fill inside and outside” option in Mask volume effect.</p>

---

## Post #10 by @Melanie (2019-08-03 10:26 UTC)

<p>Thanks all. This is helpful. I will try it out and see</p>

---

## Post #11 by @Melanie (2019-08-03 19:18 UTC)

<p>I am afraid I did try this, but an error message occurs.</p>
<p>Says- command elastix returned to non zero exit status.</p>
<p>I ve selected my fixed volume, my. moving volume, same mask for both volumes and instructed to create new output volume and new transform. This was the error message came up.<br>
<br>
Also Prof Andras <a class="mention" href="/u/lassoan">@lassoan</a>- I tried clip volume with models extension. In the youtube video it shows the volume can be clipped. Following the exact same steps, my volume disappears once I command apply.</p>
<p>I am not sure whether I am doing something wrong. I ve followed the same steps in the documentation/you tube video. Thanks</p>

---

## Post #12 by @Jainey (2019-08-04 13:37 UTC)

<p>Apologies, Incorrect reply</p>

---
