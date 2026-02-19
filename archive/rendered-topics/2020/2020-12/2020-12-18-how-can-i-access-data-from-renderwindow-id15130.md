---
topic_id: 15130
title: "How Can I Access Data From Renderwindow"
date: 2020-12-18
url: https://discourse.slicer.org/t/15130
---

# How can I access data from renderWindow?

**Topic ID**: 15130
**Date**: 2020-12-18
**URL**: https://discourse.slicer.org/t/how-can-i-access-data-from-renderwindow/15130

---

## Post #1 by @Tesla2678 (2020-12-18 07:09 UTC)

<p>Hello There,</p>
<p>I want to make the slicer showed in the “Red” widget curve.<br>
From<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8214b843bac794024d97f40cecd09bf0051b5786.jpeg" data-download-href="/uploads/short-url/iyKsI7fttos4N91NYsRq0tpFVgq.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8214b843bac794024d97f40cecd09bf0051b5786_2_690x126.jpeg" alt="image" data-base62-sha1="iyKsI7fttos4N91NYsRq0tpFVgq" width="690" height="126" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8214b843bac794024d97f40cecd09bf0051b5786_2_690x126.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8214b843bac794024d97f40cecd09bf0051b5786_2_1035x189.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8214b843bac794024d97f40cecd09bf0051b5786.jpeg 2x" data-dominant-color="454237"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1035×189 69.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
To<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0eebbf9ca4a4c5f690a2725126fe3783b8aa576b.jpeg" data-download-href="/uploads/short-url/27ZLWSYZLIdW9xoO3bVGi8c0AQ3.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0eebbf9ca4a4c5f690a2725126fe3783b8aa576b_2_690x150.jpeg" alt="image" data-base62-sha1="27ZLWSYZLIdW9xoO3bVGi8c0AQ3" width="690" height="150" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0eebbf9ca4a4c5f690a2725126fe3783b8aa576b_2_690x150.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0eebbf9ca4a4c5f690a2725126fe3783b8aa576b.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/e/0eebbf9ca4a4c5f690a2725126fe3783b8aa576b.jpeg 2x" data-dominant-color="707687"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">979×213 52.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>In order to do this, I am trying to get slice data before it was rendered.<br>
I have no idea how to do this, I can only get the “renderWindow” from each “sliceView”.<br>
How can I access the slice data and process it?</p>
<blockquote>
<blockquote>
<blockquote>
<p>renWin=slicer.app.layoutManager().sliceWidget(“Red”).sliceView().renderWindow()</p>
</blockquote>
</blockquote>
</blockquote>
<blockquote>
<blockquote>
<blockquote>
<p>render=renWin.GetRenderers().GetFirstRenderer()</p>
</blockquote>
</blockquote>
</blockquote>

---

## Post #2 by @lassoan (2020-12-19 06:15 UTC)

<p>A post was merged into an existing topic: <a href="/t/how-to-make-the-slicer-displayed-bend/15067">How to make the slicer displayed bend?</a></p>

---

## Post #3 by @lassoan (2020-12-19 06:15 UTC)



---
