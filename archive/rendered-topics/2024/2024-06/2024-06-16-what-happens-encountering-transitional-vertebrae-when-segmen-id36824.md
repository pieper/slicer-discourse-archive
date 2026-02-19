---
topic_id: 36824
title: "What Happens Encountering Transitional Vertebrae When Segmen"
date: 2024-06-16
url: https://discourse.slicer.org/t/36824
---

# What happens encountering `transitional vertebrae` when segmenting the spine in `TotalSegmentator`?

**Topic ID**: 36824
**Date**: 2024-06-16
**URL**: https://discourse.slicer.org/t/what-happens-encountering-transitional-vertebrae-when-segmenting-the-spine-in-totalsegmentator/36824

---

## Post #1 by @jumbojing (2024-06-16 16:58 UTC)

<p>What happens when encountering <a href="https://www.spineinfo.com/conditions/transitional-vertebrae-in-the-spine/" rel="noopener nofollow ugc">transitional vertebrae</a> when segmenting the spine in <a href="https://github.com/wasserth/TotalSegmentator" rel="noopener nofollow ugc">TotalSegmentator</a>?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06096dc2af40452c3fcc303f3a83635301894315.png" data-download-href="/uploads/short-url/Rp453fegWzCIS6ALqIdVmEIQ0B.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06096dc2af40452c3fcc303f3a83635301894315_2_258x500.png" alt="image" data-base62-sha1="Rp453fegWzCIS6ALqIdVmEIQ0B" width="258" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06096dc2af40452c3fcc303f3a83635301894315_2_258x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06096dc2af40452c3fcc303f3a83635301894315_2_387x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06096dc2af40452c3fcc303f3a83635301894315_2_516x1000.png 2x" data-dominant-color="868DA7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">616×1190 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
From <a href="https://osf.io/4skx2/files/osfstorage/5ffb6bebba010902a488faa4" rel="noopener nofollow ugc">vert519</a></p>
<p>How to handle this situation? Who has good advice?</p>

---

## Post #2 by @lassoan (2024-06-16 17:42 UTC)

<p>There is no automated method that works perfectly all the time. Even if the algorithm works perfectly for 99% of the cases, you still need to allow users to perform manually corrections. In medical imaging, 95% is a commonly accepted success rate, so manual corrections/overrides are very important.</p>
<p>If you have a segmentation step in your workflow then you normally allow users to interactively inspect segmentation results and make manual correction as needed. You can simply add a Segment Editor widget in a collapsible section, or you can created a simplified GUI (for example, a few buttons and maybe a segment selector that allow users to hightlight a region in 3D using Scissors tool and move the designated region to another segment).</p>

---

## Post #3 by @jumbojing (2024-10-12 06:38 UTC)

<p><a href="https://github.com/wasserth/TotalSegmentator/issues/373#issue-2582587997" class="inline-onebox" rel="noopener nofollow ugc">What happens encountering transitional vertebrae when segmenting the spine in ttSeg? · Issue #373 · wasserth/TotalSegmentator · GitHub</a>…</p>
<p>I try to segmente 10 spinal <a href="https://osf.io/4skx2/files/osfstorage" rel="noopener nofollow ugc">CT scans</a> , but the <a href="https://drive.google.com/file/d/1hAZHCWXlASQdbdX23-9re57IMfElmmyI/view?usp=sharing" rel="noopener nofollow ugc">results</a> were not very satisfactory Nearly half of the ‘transitional vertebrae?’… Is it a ‘transfer vertebra’ or a segmentation error…? 5 of 10 cases got the <code>result</code> … Maybe I did something wrong?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef2fe33a7c24101a86f5c927791fb81fdcd234a2.png" data-download-href="/uploads/short-url/y7WIhgXqdNMomwxeDhDv00SNk8a.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef2fe33a7c24101a86f5c927791fb81fdcd234a2.png" alt="image" data-base62-sha1="y7WIhgXqdNMomwxeDhDv00SNk8a" width="395" height="500" data-dominant-color="8293AF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">430×544 50 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f057cee6ef5748e3fd27969d97d24bd4a540d712.png" data-download-href="/uploads/short-url/yiaII28OwKcMv6PoLNacrCOvov8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f057cee6ef5748e3fd27969d97d24bd4a540d712.png" alt="image" data-base62-sha1="yiaII28OwKcMv6PoLNacrCOvov8" width="374" height="499" data-dominant-color="8593B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">434×580 42.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2db0d2ee1c1f31d2cb11ccbcd2292d10e832506.png" data-download-href="/uploads/short-url/wmRdT0Jx2juHLtZbOemcuWwWtts.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2db0d2ee1c1f31d2cb11ccbcd2292d10e832506_2_307x500.png" alt="image" data-base62-sha1="wmRdT0Jx2juHLtZbOemcuWwWtts" width="307" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/2/e2db0d2ee1c1f31d2cb11ccbcd2292d10e832506_2_307x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2db0d2ee1c1f31d2cb11ccbcd2292d10e832506.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/2/e2db0d2ee1c1f31d2cb11ccbcd2292d10e832506.png 2x" data-dominant-color="7E90A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">402×654 59.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/758a5bc1b929bbcd39e7560e3c94fbac38d9cdc2.png" data-download-href="/uploads/short-url/gLOikhQR7SgbS5yIynHFHXL30Fs.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/758a5bc1b929bbcd39e7560e3c94fbac38d9cdc2_2_250x500.png" alt="image" data-base62-sha1="gLOikhQR7SgbS5yIynHFHXL30Fs" width="250" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/5/758a5bc1b929bbcd39e7560e3c94fbac38d9cdc2_2_250x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/758a5bc1b929bbcd39e7560e3c94fbac38d9cdc2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/758a5bc1b929bbcd39e7560e3c94fbac38d9cdc2.png 2x" data-dominant-color="798DA5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">346×692 54.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05e6f1e24cac8986e1f4c20624fc2898c6553c27.png" data-download-href="/uploads/short-url/QdbqX9io5jK2EFCClBuxNBMwzZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05e6f1e24cac8986e1f4c20624fc2898c6553c27_2_241x500.png" alt="image" data-base62-sha1="QdbqX9io5jK2EFCClBuxNBMwzZ" width="241" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05e6f1e24cac8986e1f4c20624fc2898c6553c27_2_241x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/05e6f1e24cac8986e1f4c20624fc2898c6553c27_2_361x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05e6f1e24cac8986e1f4c20624fc2898c6553c27.png 2x" data-dominant-color="888EA8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">384×796 72.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><img src="https://emoji.discourse-cdn.com/twitter/point_up_2/2.png?v=12" title=":point_up_2:t2:" class="emoji" alt=":point_up_2:t2:" loading="lazy" width="20" height="20">: Pay attention to adjacent vertebrae with incomplete segmentation of the <strong>same color</strong> . Is it a ‘transfer vertebra’ or a segmentation error…? 5 of 10 cases got the <code>result</code> … Maybe I did something wrong?</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a>@pieper@Juicy@jamesobutler <a class="mention" href="/u/jcfr">@jcfr</a></p>
<p><img src="https://emoji.discourse-cdn.com/twitter/point_right/2.png?v=12" title=":point_right:t2:" class="emoji" alt=":point_right:t2:" loading="lazy" width="20" height="20">(<a href="https://drive.google.com/file/d/1hAZHCWXlASQdbdX23-9re57IMfElmmyI/view?usp=sharing" rel="noopener nofollow ugc">https://drive.google.com/file/d/1hAZHCWXlASQdbdX23-9re57IMfElmmyI/view?usp=sharing</a>)It includes the original CT and segmentation results. Which master can help to try segmentation and compare the segmentation results?</p>
<p>包含了原始的CT和分割结果, 哪位老师帮帮忙尝试分割一下, 并进一步比较分割的结果呢?</p>

---

## Post #4 by @lassoan (2024-10-12 16:18 UTC)

<p>Transitional vertebra (L6, T13) are not labeled by the TotalSegmentator model (<a href="https://github.com/wasserth/TotalSegmentator/issues/88" class="inline-onebox">Spine segmentation format · Issue #88 · wasserth/TotalSegmentator · GitHub</a>). If you encounter such patient cases then you can fix the segmentation using the Scissors effect in Segment Editor module (and do final touch-up using Paint effect, if needed).</p>

---

## Post #5 by @jumbojing (2024-10-14 11:03 UTC)

<p>5 of 10 cases(which may be a special case) got <code>this result👆🏻</code> , well… this <code>ttSeg</code> model is not suitable for fully automated spine segmentation? Are there any other models specifically designed for spine segmentation? <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #6 by @lassoan (2024-10-14 12:35 UTC)

<p>Prevalence of these anatomic variations are not 50%, but rather about 10%. If you have incorrect some segmentation for 50% of the cases then probably there are some other issues.</p>
<p>TotalSegmentator is very robust and readily usable for getting a general anatomic context. For example, if you do lung surgery, then TotalSegmentator’s spine segmentation is perfectly suitable as is.  If you do spine surgery then TotalSegmentator can venerally provide a good initial segmentation (to approximate bounding box for each vertebra) that you can use as input for specialized spine segmentation model. Specialized spine segmentation models are being developed, for example by the team of <a class="mention" href="/u/ron">@Ron</a>.</p>

---
