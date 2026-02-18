# Elastix to accept a non-linear initial transform (-t0 TransformParameters.txt)

**Topic ID**: 19817
**Date**: 2021-09-22
**URL**: https://discourse.slicer.org/t/elastix-to-accept-a-non-linear-initial-transform-t0-transformparameters-txt/19817

---

## Post #1 by @Magi (2021-09-22 19:00 UTC)

<p>Hi,</p>
<p>in regards to the Slicer module ‘General Registration (Elastix)’…</p>
<p>could someone please modify the elastix registration code/GUI to accept an initial transform from outside elastix? This is not a linear transform, this is a displacement field type vtkMRMLTransformNode or vtkMRMLGridTransformNode). it would be very helpful if one can select the initial transform from the GUI (please see a snapshot below circled in red) that can be passed to elastix to warp the moving image before starting the registration and add the transform to the composite transform at the end of registration. I’ve edited the GUI and can pass the initial transform to elastix code but I have tried editing the elastix code to process the initial transform, and it turned out to be a little more challenging that I thought. I do understand that the initial transform is a text file in certain format, but unfortunately it’s hard to manually modify the text file when it is not a linear transform and elastix/slicer doesn’t have a tool for converting a gridTransform to a format (text file) readable by elastix.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7da3212f84e9f06bcb410c1aace737c25eb7ab4.png" data-download-href="/uploads/short-url/uNw8yJpiD8JNZC7Hi2CtKaUQlMw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d7da3212f84e9f06bcb410c1aace737c25eb7ab4.png" alt="image" data-base62-sha1="uNw8yJpiD8JNZC7Hi2CtKaUQlMw" width="517" height="234" data-dominant-color="F3F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">914×415 9.48 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I believe I read something similar to this request from someone else on the forum. I think this is a much needed feature in elastix and would make it more accessible and useable by many. I do realize there are other modules and extensions like the ANTs and BRAINs modules, but I do need to do this in elastix.</p>
<p>I’ve already modified the GUI and Im familiar with the code so if someone could point me in the right direction on how to do that it would be great. unless it’s a quick fix and can be committed to a nighlty build for us to download.</p>
<p>Thank you very much.</p>

---

## Post #2 by @lassoan (2021-09-23 00:58 UTC)

<p>Elastix transforms diverged from ITK transforms and now the only common representation that both Eastix and ITK (and all ITK-based applications, such as Slicer) understand is a displacement field image. If you have any non-linear transform then you can convert it to a displacement field using Transforms module, save it to a file and use that in Elastix as an input.</p>

---

## Post #3 by @Magi (2021-09-23 02:13 UTC)

<p>Yes, I’ve used the transforms module and converted my initial transform to a displacement field, but unfortunately, this displacement field is not readable by elastix. It seems that elastix expects either a BSpline or a linear transform, even though the output from elastix is a displacement field in itself (when using the ‘force grid output transform’ checkbox), but elastix never reads this output transform, it only saves and reloads it into slicer. maybe the developers can help make that change to their code…?</p>

---

## Post #4 by @lassoan (2021-09-23 02:51 UTC)

<p>I would assume that Elastix can read a displacement field. It has a <code>(Transform "DeformationFieldTransform")</code> - see <a href="https://elastix.lumc.nl/doxygen/parameter.html">https://elastix.lumc.nl/doxygen/parameter.html</a>. You can submit a question to <a href="https://github.com/SuperElastix/elastix/issues" class="inline-onebox">Issues · SuperElastix/elastix · GitHub</a> to clarify.</p>
<p>If you cannot get Elastix to read the initial transform then you can harden that transform on the input image.</p>

---

## Post #5 by @Magi (2021-09-23 19:52 UTC)

<p>Thank you for pointing that out. I did not know about the DeformationFieldTransform. I was too focused on the python code itself <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"> I went ahead and tried that with elastix but getting errors already. I suppose I’m not passing it correctly to elastix. I basically created a text file named it TransformParameters.txt with the following text (taken from elastix manual):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db91d272a4061d773de4bc46e8f8ada4065154be.png" data-download-href="/uploads/short-url/vkoZheD0ubIMxHqTtEqUM03H1wy.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db91d272a4061d773de4bc46e8f8ada4065154be_2_690x97.png" alt="image" data-base62-sha1="vkoZheD0ubIMxHqTtEqUM03H1wy" width="690" height="97" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db91d272a4061d773de4bc46e8f8ada4065154be_2_690x97.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/db91d272a4061d773de4bc46e8f8ada4065154be_2_1035x145.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/b/db91d272a4061d773de4bc46e8f8ada4065154be.png 2x" data-dominant-color="F4F4F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1039×147 15.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>then added the file path name to the following statement using the elastix code<br>
(InitialTransformParametersFileName “\file path…\TransformParameters.txt”)</p>
<p>not sure if I’m doing it correctly thou, any ideas?</p>
<p>I’m also going to post this question to the SuperElastix as well. thanks for the link.</p>
<p>BTW: I’m trying to do this without hardening the transform.</p>

---

## Post #6 by @mikebind (2021-09-23 21:51 UTC)

<p>I used to try to avoid hardening transforms because I wanted to perform only non-destructive manipulations.  However, I’ve found that a lot of things are easier (like using Elastix) if I just use the image with the hardened transform, so nowadays I just clone the original volume, harden the transform on the cloned volume, and proceed with the modified cloned volume as the input to whatever next step I am doing (e.g. an Elastix registration).  Then, for example,  I can concatenate the resulting transform with the original transform and apply that to the original volume.  Often, I can then discard the cloned version with the hardened transform, and the only real cost has been a temporary increase in memory usage (for the cloned volume) and maybe a little extra computational time. I have found this clone-harden-compute-discard a far more efficient use of my time as a developer than trying to modify or augment tools which don’t automatically respect the presence of transforms soft-applied to volumes.</p>

---

## Post #7 by @Magi (2021-09-24 19:07 UTC)

<p>Thanks for sharing Mike. I was basically thinking the same thing. so maybe I’ll take both Andras and your advice for now and try hardening transforms. thank you guys again for sharing your thoughts. it’s certainly helpful to know what others are doing.</p>

---
