# How to decide threshold values for different structures in CT based on histogram?

**Topic ID**: 1661
**Date**: 2017-12-14
**URL**: https://discourse.slicer.org/t/how-to-decide-threshold-values-for-different-structures-in-ct-based-on-histogram/1661

---

## Post #1 by @Emily_BM (2017-12-14 19:10 UTC)

<p>how to decide threshold values for different structures in CT based on histogram?<br>
Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @thewtex (2017-12-15 19:29 UTC)

<p>Hi <a class="mention" href="/u/emily_bm">@Emily_BM</a>,</p>
<p>There are many histogram-based thresholding algorithms available in ITK.</p>
<p>Checkout <a href="http://hdl.handle.net/10380/3279" rel="noopener nofollow ugc">this histogram-based thresholding Insight Journal article</a></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/05e7c0773ad23cf36759fadcae7c6323282b5780.jpeg" alt="big" data-base62-sha1="QeUCRl0cGtgOqgIbMydYlsWnyo" width="300" height="300"></p>
<p>or <a href="http://www.insight-journal.org/browse/publication/132" rel="noopener nofollow ugc">this article</a> or the <a href="https://itk.org/Insight/Doxygen/html/group__ITKThresholding.html" rel="noopener nofollow ugc">ITK thresholding classes’ documentation</a>.</p>

---

## Post #3 by @lassoan (2018-05-21 02:20 UTC)

<p>Somehow I’ve come across this old topic now.</p>
<p><a class="mention" href="/u/thewtex">@thewtex</a>, what is your experience, do you find these histogram-based thresholding methods useful in practice?</p>
<p>I usually choose threshold value manually, based on live preview (provided for example by Segment Editor’s Threshold effect). If a good global threshold value exists then I can find it within 5-10 seconds. How automatic methods could make this faster or simpler? Also, don’t you need manual adjustment anyways?</p>
<p>For automated processing, instead of simple global thresholding, we had much better results with grow-cut or watershed based segmentation, with seed regions determined by registering an atlas.</p>

---

## Post #4 by @thewtex (2018-05-21 12:57 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> yes, I find them very useful in practice.</p>
<p>I usually start with the classic (multiple) Otsu threshold, then possibly try other methods.</p>
<p>We could make this faster and simpler in Slicer creating a module that just runs all the automatic thresholding algorithms and displays the results. Something like scikit-image <code>try_all_threshold</code>:</p>
<p><a href="http://scikit-image.org/docs/dev/api/skimage.filters.html#try-all-threshold" rel="nofollow noopener">http://scikit-image.org/docs/dev/api/skimage.filters.html#try-all-threshold</a></p>

---

## Post #5 by @lassoan (2018-05-21 13:28 UTC)

<p>Very interesting. I find that global thresholding is typically usable for only a few structures, such as skin surface, bones, maybe contrasted vessels/tumors, and they always require post-processing.</p>
<p>Can you attach screenshots that illustrate how you use it? What can you usually segment with it? Does it save you time or offer better results in some way than moving a slider manually? Are there some usable links to local/adaptive variants?</p>

---

## Post #6 by @muratmaga (2018-05-22 15:43 UTC)

<p>I would definitely second this feature.</p>

---

## Post #7 by @lassoan (2018-05-22 18:01 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> For what kind of images and structures you would use automatic threshold value recommendation? How long does it take to set the threshold value manually (based on live preview in slice views)? - It is important to know these, because the priority of a feature request is higher if it saves a lot of time and can be used for many cases.</p>

---

## Post #8 by @muratmaga (2018-05-22 19:40 UTC)

<p>My typical use case for this is would be contrast (iodine based) enhanced microCT scans of dissected soft tissues (e.g., from mice or pathology samples), in which diffusion of contrast may vary from sample to sample.  IN these case, I would be calculating some sort of a tissue to total volume fraction. I currently use Fiji for this specific use-case.</p>
<p>The importance of the feature for me is more for reproducibility and being objective more so than saving time.</p>

---

## Post #9 by @lassoan (2018-05-23 16:16 UTC)

<p>Reproducibility is a good point. While usually the difference should be negligible between different operators, it my be still more elegant to say that threshold was selected by using XYZ algorithm.</p>
<p>I’ll add automatic threshold setting to Threshold effect in Segment Editor module.</p>
<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Do you always compute the threshold on the entire image, or on a region of interest / masked region?</p>

---

## Post #10 by @muratmaga (2018-05-23 16:35 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Hard to generalize, but often volumes are already cropped down to contain only the sample of interest. So I am inclined to say entire image.</p>
<p>Mail](<a href="https://go.microsoft.com/fwlink/?LinkId=550986" class="inline-onebox">Outlook</a>) for Windows 10</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/677f06bdf711468707faf594c72c7993f90d2513.png" data-download-href="/uploads/short-url/eLzkAGZovUCazoJL65K1uagmWFJ.png?dl=1" title="77C3A3DB5AF54B56A741600A3E5A8000.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/677f06bdf711468707faf594c72c7993f90d2513.png" width="690" height="0" data-dominant-color="BFCDDB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">77C3A3DB5AF54B56A741600A3E5A8000.png</span><span class="informations">708×1 83 Bytes</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #11 by @lassoan (2018-05-27 14:21 UTC)

<p>I’ve implemented the feature (r27207). It will be available in nightly builds that you download tomorrow or later.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d414f5b58ae867afd2aca8e016cd4397f7e6e88.png" data-download-href="/uploads/short-url/mr8T6N4NfqsimRwgWk1rHBXhSwE.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d414f5b58ae867afd2aca8e016cd4397f7e6e88_2_690x476.png" alt="image" data-base62-sha1="mr8T6N4NfqsimRwgWk1rHBXhSwE" width="690" height="476" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d414f5b58ae867afd2aca8e016cd4397f7e6e88_2_690x476.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/d/9d414f5b58ae867afd2aca8e016cd4397f7e6e88_2_1035x714.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d414f5b58ae867afd2aca8e016cd4397f7e6e88.png 2x" data-dominant-color="F0F1F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1236×853 45.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #12 by @muratmaga (2018-06-18 15:26 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>I finally  tested this. Looks great, thank you. Is there something wrong with Shanbhag method? Everything else seems to produce reasonable threshold, but Shanbhag results in an empty selection (i.e, values too high, MRhead dataset). This is with a nightly from a week ago .</p>

---

## Post #13 by @lassoan (2018-06-18 16:07 UTC)

<p>It is normal that only certain methods provide meaningful threshold for a certain image. Shanbhag method seems to be sensitive to large uniform background regions.</p>

---

## Post #14 by @anandmulay3 (2018-06-20 14:14 UTC)

<p>hi <a class="mention" href="/u/lassoan">@lassoan</a><br>
how can we add this auto threshold method in our scripted module ??<br>
i have seen that triangle gives highest threshold object(metal object etc.)<br>
do we have any method to catch bone??</p>

---

## Post #15 by @lassoan (2018-06-21 02:33 UTC)

<p>You can follow the example <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">here</a> and call <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorThresholdEffect.py#L257">autoThreshold</a> method to compute the threshold.</p>
<p>Note that automatic threshold computation will not solve any difficult segmentation problem. It is mainly for standardizing threshold selection for trivial cases.</p>

---
