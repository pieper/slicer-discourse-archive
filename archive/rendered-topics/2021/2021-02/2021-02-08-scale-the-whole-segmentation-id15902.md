# Scale the whole segmentation

**Topic ID**: 15902
**Date**: 2021-02-08
**URL**: https://discourse.slicer.org/t/scale-the-whole-segmentation/15902

---

## Post #1 by @Aep93 (2021-02-08 17:37 UTC)

<p>Hello,<br>
How can we scale up/down a whole segmentation?<br>
I want to do it in segment editor by changing the size of the main volume, but it seems that my RAM is not enough for that. I am wondering whether there is a way to scale a segmentation without changing the size of the main volume.<br>
Thanks in advance</p>

---

## Post #2 by @muratmaga (2021-02-08 18:04 UTC)

<aside class="quote no-group" data-username="Aep93" data-post="1" data-topic="15902">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>How can we scale up/down a whole segmentation?</p>
</blockquote>
</aside>
<p>Can you clarify what you mean by this?<br>
If you want to increase the resolution of your segmentation, you can use the segment geometry settings Oversampling option to do that. Putting in 2 as an oversampling factor will increase the memory usage 8 folds. So if you don’t have enough RAM on your computer you may encounter issues or sluggishness. <a href="https://discourse.slicer.org/t/computer-slows-down-after-volume-is-oversampled/15743/17">See this thread</a></p>
<p>If this is not what you want to do, please explain more.</p>

---

## Post #3 by @Aep93 (2021-02-08 18:45 UTC)

<p>Thank you for your explanations <a class="mention" href="/u/muratmaga">@muratmaga</a>. Actually what I want to do is to make the whole model smaller for exporting related tasks and post processing. Therefore, the main volume is not important for me at this step and I do not need it anymore. Therefore, I wanted to know  the easiest way to scale down a segmentation/model without changing the main volume.</p>

---

## Post #4 by @Aep93 (2021-02-08 19:14 UTC)

<p>I get this error when I want to scale down the volume:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cf9b5998ef6d247aaac634c08de5306f6ebc186f.png" alt="image" data-base62-sha1="tCzFFWmMYBqcMMF78mAscwgyYPR" width="501" height="345"><br>
Any help is greatly appreciated.</p>

---

## Post #5 by @lassoan (2021-02-08 19:20 UTC)

<p>As the error message states, you need to increase swap size in your system settings or add more RAM if you want to oversample the segmentation or input volume.</p>
<p>However, from what you describe, it seems that you want to decimate the segmentation (reduce number of points and triangles in the mesh without changing its geometry), which can be achieved using “Decimation” module (after exporting the segmentation to closed surface).</p>

---

## Post #6 by @muratmaga (2021-02-08 19:28 UTC)

<aside class="quote no-group" data-username="Aep93" data-post="4" data-topic="15902">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>I get this error when I want to scale down the volume:</p>
</blockquote>
</aside>
<p>What module/function are you using that generates this error?</p>

---

## Post #7 by @Aep93 (2021-02-08 19:45 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I tried to use Decimation module but it seems that it is not what I want. In fact, I want to change the geometry somehow. I want to make my whole model smaller and not reducing the number of points of the same size model.</p>

---

## Post #8 by @Aep93 (2021-02-08 19:45 UTC)

<p>I got this in “Segmentation geometry” section of the segment editor module.</p>

---

## Post #9 by @lassoan (2021-02-08 19:51 UTC)

<aside class="quote no-group" data-username="Aep93" data-post="7" data-topic="15902">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>I tried to use Decimation module but it seems that it is not what I want. In fact, I want to change the geometry somehow.</p>
</blockquote>
</aside>
<p>You can change physical scale of segmentations when you <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#export-segmentation-to-model-surface-mesh-file">export to files</a> or using Surface Toolbox module (Scale mesh) or apply a transform in Transforms module (scaling factors are the 3 diagonal values in the first 3 columns).</p>

---

## Post #10 by @muratmaga (2021-02-08 19:51 UTC)

<p>Remember it is the option is to oversample. If you are trying to reduce the detail, you need to put a number less than 1. However, this may cause loss of detail in your segmentation.</p>
<p>Perhaps you can first export the segmentation as a model, and then use the <code>Surface Toolbox</code>'s Decimation option to reduce the model detail.</p>

---

## Post #11 by @Aep93 (2021-02-08 19:55 UTC)

<p>Thank you very much <a class="mention" href="/u/lassoan">@lassoan</a>. I think the “Surface Toolbox” is very close to what I want. Just one question:<br>
How can we increase the limitation of the number of input decimals. It seems that only two decimals can be used as scale factor by default.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/436eac6809c464b96c67360ee05331291f607670.png" data-download-href="/uploads/short-url/9Cx6Exl6x3fRwOYSxcJ1lBnHh3W.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/436eac6809c464b96c67360ee05331291f607670_2_690x90.png" alt="image" data-base62-sha1="9Cx6Exl6x3fRwOYSxcJ1lBnHh3W" width="690" height="90" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/436eac6809c464b96c67360ee05331291f607670_2_690x90.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/436eac6809c464b96c67360ee05331291f607670.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/436eac6809c464b96c67360ee05331291f607670.png 2x" data-dominant-color="E6E6E6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">723×95 7.58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @Aep93 (2021-02-08 19:57 UTC)

<p>Thank you very much for your response <a class="mention" href="/u/muratmaga">@muratmaga</a>. I think the best way for me is to use “Surface toolbox” module as you mentioned and there I can scale down my model.</p>

---

## Post #13 by @lassoan (2021-02-08 19:59 UTC)

<aside class="quote no-group" data-username="Aep93" data-post="11" data-topic="15902">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>How can we increase the limitation of the number of input decimals. It seems that only two decimals can be used as scale factor by default.</p>
</blockquote>
</aside>
<p>You can increase the decimal digits by hitting <kbd>Ctrl</kbd>+<kbd>+</kbd>.</p>
<p>However, both the need to scale down the model and use a very specific many-digit scaling factor are things that should normally not needed. Why do you need to change the physical scale of your model?</p>

---

## Post #14 by @Aep93 (2021-02-08 21:51 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I want to scale my segmentation (which is related to a very small organ) to its real physical dimensions and export it.<br>
One question:<br>
Does this combination (ctrl and +) work in all modules of slicer for increasing decimal digits? For me, it works in the “Surface Toolbox” module but it seems not to be working in the “Create models” module. Do you have any ideas in this regard?<br>
Thanks in advance</p>

---

## Post #15 by @lassoan (2021-02-08 21:59 UTC)

<p>This keyboard shortcut is enabled by default in all ctkDoubleSpinBox widgets. We can enable it in Create Models module, too.</p>

---

## Post #16 by @Aep93 (2021-02-08 22:02 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. How should I enable it? Is this possible for you to kindly enable it?</p>

---

## Post #17 by @lassoan (2021-04-27 02:32 UTC)

<p>I’ve enabled it now. You can enter arbitrary number of decimals in SlicerIGT extension from tomorrow (in latest Slicer Preview Release and if you update SlicerIGT in latest Stable Release).</p>

---

## Post #18 by @Aep93 (2021-04-27 02:44 UTC)

<p>Thank you so much <a class="mention" href="/u/lassoan">@lassoan</a>.</p>

---

## Post #19 by @Qazi (2022-06-03 18:45 UTC)

<p>Hi there,</p>
<p>would scaling up/down change the volume (quantification) using segment statistics? If yes, by which factor you can correct it? e.g. if your  scaling factor is 0.2, and your volume reading on segment statistics is 20000cm3, do you need to multiply the 20000 with 0.2^3 to get the correct volume of the segment? or if there is any other way to get the correct value for volume. Thanks</p>

---

## Post #20 by @mau_igna_06 (2022-06-05 11:08 UTC)

<p>Appply a limear transform woth values on the doagonal thay rqusl your svaleFactor</p>
<p>Sorry Im on my hpone</p>

---
