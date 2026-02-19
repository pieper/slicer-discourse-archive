---
topic_id: 38016
title: "Padding The Segmentation Geometry"
date: 2024-08-23
url: https://discourse.slicer.org/t/38016
---

# Padding the segmentation geometry

**Topic ID**: 38016
**Date**: 2024-08-23
**URL**: https://discourse.slicer.org/t/padding-the-segmentation-geometry/38016

---

## Post #1 by @muratmaga (2024-08-23 18:02 UTC)

<p>I have a bunch of 3D models that I need to edit (I do not have the original segmentation). I need to run dilation on these models but as imported the geometry of the segmentation is too tight to do any dilation (I end up with straight edges). So this is I have been doing:</p>
<ol>
<li>Load the model into scene</li>
<li>Convert it to a binary labelmap</li>
<li>Use the crop tool (non-intepolation) to expand the volume dimensions about 50% in each axis and overwrite itself (to keep the scene cleaner).</li>
<li>Go to segmentations, create a blank segmentation, then scroll down to import/export, choose the operation as import, input type as the labelmap, and the input node as the expanded labelmap.</li>
</ol>
<p>My expectation at this point the segmentation geometry would have been the same as the labelmap, but it is not.</p>
<p>geometry for the labelmap:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/0813730e3204fba5436cb0c884870119f9616a55.jpeg" data-download-href="/uploads/short-url/19runvxuUC2EiSLz1Z34Mqq1VFH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0813730e3204fba5436cb0c884870119f9616a55_2_690x469.jpeg" alt="image" data-base62-sha1="19runvxuUC2EiSLz1Z34Mqq1VFH" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0813730e3204fba5436cb0c884870119f9616a55_2_690x469.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0813730e3204fba5436cb0c884870119f9616a55_2_1035x703.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/0813730e3204fba5436cb0c884870119f9616a55_2_1380x938.jpeg 2x" data-dominant-color="E3E3E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1524×1038 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
geometry for segmentation<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64a9330e666f1c29056ca95db82384aede9b0a69.jpeg" data-download-href="/uploads/short-url/emufOS9iSs1p31NueUxPmgyNVNf.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64a9330e666f1c29056ca95db82384aede9b0a69_2_690x460.jpeg" alt="image" data-base62-sha1="emufOS9iSs1p31NueUxPmgyNVNf" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64a9330e666f1c29056ca95db82384aede9b0a69_2_690x460.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64a9330e666f1c29056ca95db82384aede9b0a69_2_1035x690.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/64a9330e666f1c29056ca95db82384aede9b0a69_2_1380x920.jpeg 2x" data-dominant-color="E3E4E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1538×1026 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now when I run the dilation, I still get the straight edges indicating the segment geometry is not expanding. What am I missing here?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac3398612182cdd4f750c253415350284a1c5793.png" data-download-href="/uploads/short-url/ozmFmGA3LbUqf1wpOFZ7bMGQPzd.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac3398612182cdd4f750c253415350284a1c5793_2_222x499.png" alt="image" data-base62-sha1="ozmFmGA3LbUqf1wpOFZ7bMGQPzd" width="222" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac3398612182cdd4f750c253415350284a1c5793_2_222x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac3398612182cdd4f750c253415350284a1c5793_2_333x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac3398612182cdd4f750c253415350284a1c5793_2_444x998.png 2x" data-dominant-color="262012"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">732×1648 79.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-08-23 19:40 UTC)

<p>Turns out the solution to this is to initiate the segmentation first (using the padded labelmap as the source geometry) and then import the contents of the labelmap into that segmentation.</p>
<p>However, I still think the original workflow I presented should be supported. If I am specifying a labelmap to be imported, I expect the geometry of the segmentation to match the extend of the volume, not its contents.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a></p>

---

## Post #3 by @lassoan (2024-08-23 21:07 UTC)

<p>This behavior is indeed complex, but well documented. Options for expanding segmentation is described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">here</a>. Let us know if you have any questions or suggestions.</p>

---

## Post #4 by @muratmaga (2024-08-23 22:35 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="38016">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Let us know if you have any questions or suggestions.</p>
</blockquote>
</aside>
<p>Actually I do: I am following the instructions to paint beyond extends, which says ‘If you want to extend the segmentation to a larger region then you need to modify segmentation’s geometry using “Specify geometry” button.’</p>
<p>Where is that button? Dimension fields are not editable for me?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/0/8054eb892c4ae74a01996bc29fcab116de8b158f.jpeg" data-download-href="/uploads/short-url/ijh3vBXnAVIFp1ywtWgrTVjDQYv.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8054eb892c4ae74a01996bc29fcab116de8b158f_2_686x500.jpeg" alt="image" data-base62-sha1="ijh3vBXnAVIFp1ywtWgrTVjDQYv" width="686" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8054eb892c4ae74a01996bc29fcab116de8b158f_2_686x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8054eb892c4ae74a01996bc29fcab116de8b158f_2_1029x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/0/8054eb892c4ae74a01996bc29fcab116de8b158f_2_1372x1000.jpeg 2x" data-dominant-color="E3E3E3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1632×1188 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2024-08-24 06:33 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="38016">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Where is that button?</p>
</blockquote>
</aside>
<p>It seems that you have found it, but in general if you want to find information on a button that is mentioned on a documentation page and it is not a link then you can search for its name on that page, in the search box in the Slicer documentation, or ask an AI chatbot. I’ll make it a link to make it easier.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="4" data-topic="38016">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Dimension fields are not editable for me?</p>
</blockquote>
</aside>
<p>That section shows what will be the resulting geometry. It would not be user-friendly if the user would need to blindly type some values there. Instead, you can choose an ROI or another node that is larger or smaller to change the size or position. Do you have any suggestions for changing the GUI or documentation to make this more clear for users?</p>

---
