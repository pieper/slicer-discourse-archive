---
topic_id: 44151
title: "Transform Clarifications"
date: 2025-08-20
url: https://discourse.slicer.org/t/44151
---

# Transform Clarifications

**Topic ID**: 44151
**Date**: 2025-08-20
**URL**: https://discourse.slicer.org/t/transform-clarifications/44151

---

## Post #1 by @tbugajski (2025-08-20 22:06 UTC)

<p>Hi SAM team,</p>
<p>I have a quick question regarding the transformation outputs when creating a partial volume. Based on the photo below, I would assume that combining {bone}.tfm and {bone}_PVOL2AUT.tfm would give the result of {bone}_DICOM2AUT.tfm.</p>
<p>As I understand it, the {bone}.tfm <strong><span class="bbcode-u">non-rigid</span></strong> transform contains a scaling parameter to properly scale the dimensionless bone TIFF into the world space. The {bone}_PVOL2AUT.tfm <strong><span class="bbcode-u">rigid</span></strong> transform then places that model into AUT space.</p>
<p>However, when viewing the {bone}_DICOM2AUT.tfm transform, it does not have any scaling parameters associated with it. Therefore, if I were to apply this transform to the dimensionless bone TIFF, wouldn’t it be improperly scaled? Am I missing something here?</p>
<p>Thanks for your time in advance!</p>
<p>P.S. - I am wondering if there will eventually be more details regarding the outputs of the transform file. I am trying to understand the difference between Parameters and FixedParameters.</p>
<p>Cheers,</p>
<p>Tomasz</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e557ee3bb4cf472f99c1e77173945de09e9bef05.png" data-download-href="/uploads/short-url/wIRJkCBPG3BcBirkzS2vHSM1o8Z.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/5/e557ee3bb4cf472f99c1e77173945de09e9bef05.png" alt="image" data-base62-sha1="wIRJkCBPG3BcBirkzS2vHSM1o8Z" width="690" height="495" data-dominant-color="F7F7EF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">852×612 21.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @John_Holtgrewe (2025-08-21 16:45 UTC)

<p>Hi Tomasz,</p>
<p>You are correct. The {bone}_DICOM2AUT.tfm transform (and {bone}_PVOL2AUT.tfm) does not have any scaling parameters.</p>
<p>The {bone}.tfm transform does scale the bone TIFF; however, the transform places the volume in the DICOM space rather than the world space. The {bone}_scale.tfm does scale the bone TIFF and place it in the world space.</p>
<p>There are multiple ways to transform the un-scaled bone TIFF to the AUT space using the transforms. One way is to apply {bone}.tfm to scale and transform the volume to the DICOM space and then apply the {bone}_DICOM2AUT.tfm transform. Another way is to apply the  {bone}_scale.tfm transform and then apply the {bone}_PVOL2AUT.tfm transform.</p>
<p>Here are figures that show the results of applying these transforms:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d0b15d7dd8aa8b7b3f155481e3ba8dd5cf8153f.png" data-download-href="/uploads/short-url/6qteEBvVpNNP92ttgyr4HmzeDIX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/d/2d0b15d7dd8aa8b7b3f155481e3ba8dd5cf8153f.png" alt="image" data-base62-sha1="6qteEBvVpNNP92ttgyr4HmzeDIX" width="304" height="328"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">304×328 48.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/967e60b67c9361ae99b7f1677307f8c8be2da0bf.png" data-download-href="/uploads/short-url/ltknN1GyukhuNjSLfafBORymCOX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/6/967e60b67c9361ae99b7f1677307f8c8be2da0bf.png" alt="image" data-base62-sha1="ltknN1GyukhuNjSLfafBORymCOX" width="467" height="330"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">467×330 39.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/216a118e56869a8ab3e6cc400a4fdd09ca8f070a.png" data-download-href="/uploads/short-url/4LB0ssVmZqxtqvYHUxcfB5gT0M2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/216a118e56869a8ab3e6cc400a4fdd09ca8f070a.png" alt="image" data-base62-sha1="4LB0ssVmZqxtqvYHUxcfB5gT0M2" width="393" height="353"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">393×353 52.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8af7dbb0c197b2e1bd7d1110d6906f6c3dd8ff1.png" data-download-href="/uploads/short-url/xcqLbVz6XKtzY4eUJxUsjaFRjdn.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8af7dbb0c197b2e1bd7d1110d6906f6c3dd8ff1_2_690x357.png" alt="image" data-base62-sha1="xcqLbVz6XKtzY4eUJxUsjaFRjdn" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8af7dbb0c197b2e1bd7d1110d6906f6c3dd8ff1_2_690x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8af7dbb0c197b2e1bd7d1110d6906f6c3dd8ff1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8af7dbb0c197b2e1bd7d1110d6906f6c3dd8ff1.png 2x" data-dominant-color="A7A4C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">701×363 52.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7ad50bdd34e013807c40983e9ae778c18500f386.png" data-download-href="/uploads/short-url/hwCHsXrsrZPtiHlf16WhNC6RhmS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7ad50bdd34e013807c40983e9ae778c18500f386_2_690x336.png" alt="image" data-base62-sha1="hwCHsXrsrZPtiHlf16WhNC6RhmS" width="690" height="336" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7ad50bdd34e013807c40983e9ae778c18500f386_2_690x336.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7ad50bdd34e013807c40983e9ae778c18500f386.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7ad50bdd34e013807c40983e9ae778c18500f386.png 2x" data-dominant-color="A7A4C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">808×394 60.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I agree, looking at the flow chart from the readthedocs does make it seem like the way you were applying the transforms should have resulted in the same outcome. This is something we can revisit on our end and work on to better explain the workflow of applying the transforms. I hope this answered your question about the transforms. Let me know if you have any additional questions or feedback!</p>

---

## Post #3 by @tbugajski (2025-08-21 17:49 UTC)

<p>Hi John,</p>
<p>Thanks for the clarification. This makes sense now, especially when considering the definitions supplied within the same document (I forgot those were in there!):</p>
<ul>
<li>
<p><strong>Transforms:</strong></p>
<ul>
<li>
<p><code>{bone}.tfm</code>: Non-rigid transform that translates and scales the <code>{bone}.tif</code> volume to its spatial location within the segmented CT-DICOM.</p>
</li>
<li>
<p><code>{bone}_DICOM2AUT.tfm</code>: Transformation from DICOM space into Autoscoper (AUT) space.</p>
</li>
<li>
<p><code>{bone}_PVOL2AUT.tfm</code>: Transformation from world space into Autoscoper (AUT) space.</p>
</li>
<li>
<p><code>{bone}_scale.tfm</code>: Scaling matrix that converts the volume from image space to world space.</p>
</li>
<li>
<p><code>{bone}_t.tfm</code>: Translation matrix moving between the world origin and the location of the partial volume within the segmented CT-DICOM.</p>
</li>
</ul>
</li>
</ul>
<p>Based on this information, would this pipeline I modified from the original image make sense?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c92442ae3a21f31fa5a6a8201f77ec08ee0dad9.png" data-download-href="/uploads/short-url/hM0zZ2aozsq80A12vTHB3ibNQsp.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c92442ae3a21f31fa5a6a8201f77ec08ee0dad9_2_690x419.png" alt="image" data-base62-sha1="hM0zZ2aozsq80A12vTHB3ibNQsp" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c92442ae3a21f31fa5a6a8201f77ec08ee0dad9_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c92442ae3a21f31fa5a6a8201f77ec08ee0dad9_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/c/7c92442ae3a21f31fa5a6a8201f77ec08ee0dad9_2_1380x838.png 2x" data-dominant-color="E2E1D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1806×1097 223 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Lastly, I do want to mention that the documentation and figures are all greatly appreciated. It is valuable to us end-users to understand the processes that occur behind the scenes of SAM.</p>
<p>Tomasz</p>

---

## Post #4 by @Amy_Morton (2025-08-29 15:17 UTC)

<p>Hey <a class="mention" href="/u/tbugajski">@tbugajski</a></p>
<p>One of the tricky considerations for using Autoscoper is that the tiff volume will be internally represented in a specific (if colloquial) way.  PVOL2AUT accommodates for this.</p>
<p>As <a class="mention" href="/u/john_holtgrewe">@John_Holtgrewe</a> pointed out (thanks John!) the PVOL is essentially the tiff stack subvolume with appropriate scaling- but still located at the origin, and the flow diagram contradicts our other graphics somewhat (we’ll work on updating!)</p>
<p>All intermediary transforms are provided and detailed fyi but we also attempted to streamline post-processing by calculating exporting STL models in AUT space, such that autoscoper bvr .tra outputs can be directly applied ot the AUT{bone}.stl for global motion.</p>
<p>If you generated a local anatomical cs- you can likewise apply DICOM2AUT for that bone to visually and mathematically appropriate the cs (and respectively apply you tra)</p>

---

## Post #5 by @tbugajski (2025-08-29 15:28 UTC)

<p>Hey Amy,</p>
<p>Thanks for the clarifications. I did notice the ‘Models’ folder that contains the models in AUT space. These have been extremely helpful for visualization purposes. I will be on the lookout for those updated diagrams.</p>
<p>Cheers,</p>
<p>Tomasz</p>

---
