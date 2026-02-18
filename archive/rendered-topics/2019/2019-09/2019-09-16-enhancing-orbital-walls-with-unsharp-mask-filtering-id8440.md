# Enhancing Orbital Walls With Unsharp Mask Filtering

**Topic ID**: 8440
**Date**: 2019-09-16
**URL**: https://discourse.slicer.org/t/enhancing-orbital-walls-with-unsharp-mask-filtering/8440

---

## Post #1 by @Juicy (2019-09-16 03:15 UTC)

<p>Hello all,</p>
<p>I was looking into ways to make segmenting eye orbits a bit easier (for bio models in the public hospital)</p>
<p>I found this handy list of hints <a href="https://discourse.slicer.org/t/segmentation-of-thin-surfaces/2332/2">segmentation of thin surfaces</a></p>
<p>I have also read through the masters thesis which was also linked in this post: <a href="https://discourse.slicer.org/t/high-quality-segmentation-of-the-orbital-walls/2345/4">Masters Thesis</a></p>
<p>First I  cropped the volume around the orbit and made it have isotropic voxels, I also halved the size of the voxels so the volume is higher resolution (all with crop volume module).</p>
<p>The thesis mentioned Richardson Lucy Deconvolution and Unsharp Mask filtering. I managed to find both of these in the simple filters module but I must admit I have no idea how to use them. The thesis mentioned Richardson Lucy Deconvolution with 80 iterations works well so I tried that with 80 iterations and all other settings default and my computer usually crashes horrendously.</p>
<p>With Unsharp mask filtering I cannot get it to run and always get this error:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e09e17d7802e598cc6feb6d2a10c16fd9b372ba9.jpeg" data-download-href="/uploads/short-url/w33FjsM9k9n4yzG0ukhylQO26Eh.jpeg?dl=1" title="Unsharp%20Mask%20Filter%20Error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e09e17d7802e598cc6feb6d2a10c16fd9b372ba9_2_690x456.jpeg" alt="Unsharp%20Mask%20Filter%20Error" data-base62-sha1="w33FjsM9k9n4yzG0ukhylQO26Eh" width="690" height="456" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e09e17d7802e598cc6feb6d2a10c16fd9b372ba9_2_690x456.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e09e17d7802e598cc6feb6d2a10c16fd9b372ba9_2_1035x684.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e09e17d7802e598cc6feb6d2a10c16fd9b372ba9_2_1380x912.jpeg 2x" data-dominant-color="A8A8AE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Unsharp%20Mask%20Filter%20Error</span><span class="informations">1399×925 200 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there anyone who knows how to use these filters? We make a lot of bio models in the public hospital to assist with surgery and any way to save time on segmenting orbits would be very helpful.</p>
<p>Thanks very much.</p>

---

## Post #2 by @Amine (2019-09-16 19:39 UTC)

<p>Hi, i executed  Richardson Lucy Deconvolution filter without any problems, did you try with less iterations?</p>
<p>as for Unsharp Mask image filter, try running this script on the python interactor to fix the volume before running the filter: first rename your volume to <code>Master</code> then run this script:</p>
<blockquote>
<p>import SimpleITK as  sitk<br>
import sitkUtils<br>
input_vol = getNode(“Master”)<br>
output_vol = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLScalarVolumeNode’, “Fixed Master”)<br>
inputImage = sitkUtils.PullVolumeFromSlicer(input_vol)<br>
caster = sitk.CastImageFilter()<br>
pixelID = sitk.sitkFloat32<br>
caster.SetOutputPixelType(pixelID)<br>
inputImage = caster.Execute(inputImage)<br>
sitkUtils.PushVolumeToSlicer(inputImage, output_vol)</p>
</blockquote>

---

## Post #3 by @Juicy (2019-09-17 02:28 UTC)

<p>Hi Amine,</p>
<p>Thank you very much for your help. The code worked great. I had to change all the " symbols and the ’ symbols for it to work as they seemed to have changed format in the copy and pasting process somewhere.</p>
<p>I guess this code does the same thing as changing the volume type to ‘float’ in the ‘cast scalar volume’ module?</p>
<p>The Unsharp mask filtering gave excellent results. The following is an image of a segmented orbit with no filters applied. The volume has just been cropped and converted to isotropic voxels and b spline interpolation using the ‘crop volume’ module.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbdcc8e03defd78dfa59d70330c1dd166d94ffd5.jpeg" data-download-href="/uploads/short-url/t5rXeRiTsyW4Sb12lVHRFnPfw7b.jpeg?dl=1" title="Unfiltered" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbdcc8e03defd78dfa59d70330c1dd166d94ffd5_2_397x375.jpeg" alt="Unfiltered" data-base62-sha1="t5rXeRiTsyW4Sb12lVHRFnPfw7b" width="397" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbdcc8e03defd78dfa59d70330c1dd166d94ffd5_2_397x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbdcc8e03defd78dfa59d70330c1dd166d94ffd5_2_595x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/cbdcc8e03defd78dfa59d70330c1dd166d94ffd5_2_794x750.jpeg 2x" data-dominant-color="837C74"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Unfiltered</span><span class="informations">841×793 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The following is the segmented orbit with some filtering done on the volume:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/d/0d6c6f72b9db715108e1b0315868e1c0acb3b7ec.jpeg" data-download-href="/uploads/short-url/1UKwMABoWMugooKdlZw5plR2cKU.jpeg?dl=1" title="After%20Processing" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d6c6f72b9db715108e1b0315868e1c0acb3b7ec_2_396x375.jpeg" alt="After%20Processing" data-base62-sha1="1UKwMABoWMugooKdlZw5plR2cKU" width="396" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d6c6f72b9db715108e1b0315868e1c0acb3b7ec_2_396x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d6c6f72b9db715108e1b0315868e1c0acb3b7ec_2_594x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0d6c6f72b9db715108e1b0315868e1c0acb3b7ec_2_792x750.jpeg 2x" data-dominant-color="807B79"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">After%20Processing</span><span class="informations">841×795 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is a really big improvement and saves between half an hour to an hour of manual painting slice by slice.</p>
<p>Here is what I did:</p>
<ol>
<li>
<p>Import the DICOM images, make an ROI around the orbit of interest. Then crop the volume with isotropic voxels selected and b spline interpolation.</p>
</li>
<li>
<p>Once the volume is cropped I go to the ‘Cast Scalar Volume’ module and convert the volume to ‘float’.</p>
</li>
<li>
<p>Then go to the Simple filters module and select Unsharp Mask Image Filter. Choose the cropped volume as an input and create a new output volume. The settings which worked the best for me were sigmas = 1x1x1, Amount = 2 and Threshold = 40.</p>
</li>
</ol>
<p>Increasing the sigmas seemed to fatten up the walls but result in more noisyness. Increasing the amount seems to increase the definition of the orbital walls but the noise seems to increase with it. The threshold of 40 seemed to be optimal for reducing the noise in the soft tissue without creating many holes in the orbital walls (for this particular scan at least). I imagine for CBCT scans then these settings would not apply.</p>
<p>Another option I found was to leave the threshold at 0 (which creates higher noise in the soft tissue) and then use the ‘Gradient Anisotropic Diffusion’ filter to reduce the soft tissue noise without affecting the enhanced orbital walls. This actually produced a slightly better result but of course means another step in the process.</p>
<p>Also as a weird side effect the edge between the skin of the face and the air seemed to be significantly enhanced so it showed up in the segmentation. I subsequently deleted the skin with the islands effect in segment editor but this could be a good way of segmenting the bone and the skin easily without including any of the soft tissue in between.</p>

---

## Post #4 by @lassoan (2019-09-17 02:41 UTC)

<p>This looks awesome and it will get even better!</p>
<p>Using the new “Wrap Solidify” effect (provided by SurfaceWrapSolidify extension) by Sebastien Andress you can ensure that discontinuous contours/missing pieces are connected to form a nice solid object.</p>
<p>Example on a very low quality image:</p>
<p>Input (obtained with simple thresholding, without any resampling, filtering, etc):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/4/444f9a130f799e4d315e2224b47779e9ee0f9875.png" data-download-href="/uploads/short-url/9Kj0Suf5hA2OKtmO2Wz2o0JsVrn.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/444f9a130f799e4d315e2224b47779e9ee0f9875_2_690x361.png" alt="image" data-base62-sha1="9Kj0Suf5hA2OKtmO2Wz2o0JsVrn" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/444f9a130f799e4d315e2224b47779e9ee0f9875_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/444f9a130f799e4d315e2224b47779e9ee0f9875_2_1035x541.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/4/444f9a130f799e4d315e2224b47779e9ee0f9875_2_1380x722.png 2x" data-dominant-color="7A7E7C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1743×913 343 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Result of “Wrap Solidify” using “Deep Hull”: the orbital wall is a nice continuous surface</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/2/c2bca550a620b5da559b9c25749e4594874d83a4.png" data-download-href="/uploads/short-url/rMINEQiRnR1yqMZuKPSVv0OW7wU.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2bca550a620b5da559b9c25749e4594874d83a4_2_690x360.png" alt="image" data-base62-sha1="rMINEQiRnR1yqMZuKPSVv0OW7wU" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2bca550a620b5da559b9c25749e4594874d83a4_2_690x360.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2bca550a620b5da559b9c25749e4594874d83a4_2_1035x540.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/2/c2bca550a620b5da559b9c25749e4594874d83a4_2_1380x720.png 2x" data-dominant-color="7C817F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1750×914 331 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would expect that running solidification on the filtered image would provide very good quality segmentation.</p>

---

## Post #5 by @Juicy (2019-09-17 03:05 UTC)

<p>Thanks! That looks really interesting. I will look into that.</p>

---

## Post #6 by @sandress (2019-09-17 11:18 UTC)

<p>This looks like a nice application for the filter.<br>
I’d suggest trying the following settings:</p>
<ul>
<li>Offset First Shrinkwrap: 5mm -&gt; It approaches to the outside of the segmentation</li>
<li>Spacing First Remesh: 5mm^3 -&gt; since it approaches, the resolution doesn’t need to be that high</li>
<li>Spacing Second Shrinkwrap (actually should be Remesh, changes in next release): 1mm^3 or lower, this will be the output resolution</li>
<li>Iterations first shrinkwrap: 2</li>
<li>Iterations Second Shrinkwrap: 3-8 -&gt; depending on the result, if some flat holes are not covered, try enlarging this number</li>
<li>raycast search: 10mm -&gt; probably especially the orbita will be covered, which is a large hole.</li>
<li>raycast result: about 2mm -&gt; if you try to raycast into small holes, this number should be small, if not, it should be bigger.</li>
</ul>
<p>Sorry about this weird naming of the parameters, we are still thinking about a better naming to make this filter more understandable. For more details please see the <a href="https://github.com/sebastianandress/Slicer-SurfaceWrapSolidify" rel="nofollow noopener">github</a> page.</p>

---

## Post #7 by @Juicy (2020-01-28 20:46 UTC)

<p>I finally got around to trying out the Wrap Solidify effect.</p>
<p>I have not had much luck with orbits. I cannot get the effect to stop filling in the orbit. I have played with a lot of the settings including Carve out Cavities and Number of iterations but it does not seem to change the effect. Also the settings seem to be pretty different to what is shown above, I guess mine is a later release?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecbd06c9bed7ec3c5b98898dd920e190a9a2b83e.jpeg" data-download-href="/uploads/short-url/xMhFzhpIP4WasFjlMyAR6zo67ls.jpeg?dl=1" title="ForumPic" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecbd06c9bed7ec3c5b98898dd920e190a9a2b83e_2_690x401.jpeg" alt="ForumPic" data-base62-sha1="xMhFzhpIP4WasFjlMyAR6zo67ls" width="690" height="401" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecbd06c9bed7ec3c5b98898dd920e190a9a2b83e_2_690x401.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ecbd06c9bed7ec3c5b98898dd920e190a9a2b83e_2_1035x601.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ecbd06c9bed7ec3c5b98898dd920e190a9a2b83e.jpeg 2x" data-dominant-color="A3AAA5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ForumPic</span><span class="informations">1315×765 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I was also playing with this effect for segmenting a pelvis and some femurs. These segments typically end up with lots of surface holes which is painful to fill in. The wrap surface effect did an excellent job of making a lovely smooth segment which closely matched the shape of the bone. Thanks very much for putting in the time to make this extension it saves A LOT of time with superior results!</p>

---

## Post #8 by @lassoan (2020-01-29 04:37 UTC)

<p>The effect should work well for orbit segmentation, but you need to pay attention to a few things:</p>
<ol>
<li>Make sure the orbital socket is only open from anterior direction. You can draw a few walls using Scissors effect to close down openings.</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aee42d1791fb5d7ae77d8c99221067ab1160325b.png" alt="image" data-base62-sha1="oX9WAwtLE2ROuF1JanZ9nGFrfe3" width="442" height="423"></p>
<ol start="2">
<li>Make sure “Carve out cavities” is enabled. If the orbit is filled up then decrease “Minimal cavities diameter” (around 15-25mm should work). If the orbital wall is fractured, incomplete then increase “Minimal cavities diameter” (and/or lower the intensity threshold value that extracted the bones from the image - that makes the bone surface more continuous and less and smaller holes to fill).</li>
</ol>

---

## Post #9 by @lassoan (2020-04-22 12:09 UTC)

<p>We have greatly improved the Wrap Solidify effect. Filling of the orbit can now be prevented very easily.</p>

---

## Post #10 by @Juicy (2020-04-22 19:47 UTC)

<p>Great, thanks for the update on this. I will give it a try some time.</p>

---
