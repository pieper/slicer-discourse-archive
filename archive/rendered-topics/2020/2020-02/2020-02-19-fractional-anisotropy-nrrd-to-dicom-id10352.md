---
topic_id: 10352
title: "Fractional Anisotropy Nrrd To Dicom"
date: 2020-02-19
url: https://discourse.slicer.org/t/10352
---

# Fractional anisotropy nrrd to dicom

**Topic ID**: 10352
**Date**: 2020-02-19
**URL**: https://discourse.slicer.org/t/fractional-anisotropy-nrrd-to-dicom/10352

---

## Post #1 by @HariES (2020-02-19 18:23 UTC)

<p>Dear Sir</p>
<p>I would like to export nrrd as dicom and save.<br>
I tried using dicom export, create dicom series and under data module.<br>
Nothing is worked properly. I may enter some information which I dont know.<br>
Kindly guide to get FA.nrrd into dicom</p>

---

## Post #2 by @Juicy (2020-02-19 21:29 UTC)

<p>Have you tried:</p>
<p>Drag and drop the nrrd file into slicer and load as a volume, then go to data module and right click on the volume and choose Export to DICOM?</p>

---

## Post #3 by @lassoan (2020-02-20 04:13 UTC)

<p><a class="mention" href="/u/juicy">@Juicy</a>’s suggestion above should work well on recent Slicer Preview Releases.</p>
<p>Just one more thing to pay attention to before export: Since (until very recently) DICOM could only store integer values, you need to scale your fractional anisotropy volume from the original intensity range of [0, 1] to something that can be represented accurately enough as integers - for example [0,1000]. You can use Simple Filters module / ShiftScaleImageFilter with scale set to 1000.0.</p>

---

## Post #4 by @HariES (2020-02-23 05:17 UTC)

<p>How to do drag and drop, I am getting no entry signal.<br>
If I export from data I am getting empty images.</p>

---

## Post #5 by @lassoan (2020-02-24 03:39 UTC)

<aside class="quote no-group" data-username="HariES" data-post="4" data-topic="10352">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/haries/48/6045_2.png" class="avatar"> HariES:</div>
<blockquote>
<p>How to do drag and drop</p>
</blockquote>
</aside>
<p>If you have trouble with drag-and-drop then you can use menu: File / Add data.</p>

---

## Post #6 by @HariES (2020-02-24 07:35 UTC)

<p>Shiftscalefilter not accepting integer in while setting scaling. I set FA values (0, 10000) still it shows fractional value.</p>

---

## Post #7 by @lassoan (2020-02-25 04:44 UTC)

<aside class="quote no-group" data-username="HariES" data-post="6" data-topic="10352">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/haries/48/6045_2.png" class="avatar"> HariES:</div>
<blockquote>
<p>Shiftscalefilter not accepting integer in while setting scaling</p>
</blockquote>
</aside>
<p>Scaling value can be integer or floating point, it does not matter. If you mean you would like to convert the image to integer type (I don’t think it is necessary for DICOM export) then you can use Cast Scalar Volume module.</p>
<aside class="quote no-group" data-username="HariES" data-post="6" data-topic="10352">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/haries/48/6045_2.png" class="avatar"> HariES:</div>
<blockquote>
<p>I set FA values (0, 10000) still it shows fractional value.</p>
</blockquote>
</aside>
<p>Where does it show that? Note that usually processing result is saved into a new volume, the original one should still be fractional.</p>

---
