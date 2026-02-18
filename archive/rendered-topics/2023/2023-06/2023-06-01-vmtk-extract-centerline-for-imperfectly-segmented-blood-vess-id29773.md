# VMTK Extract Centerline for imperfectly segmented blood vessel

**Topic ID**: 29773
**Date**: 2023-06-01
**URL**: https://discourse.slicer.org/t/vmtk-extract-centerline-for-imperfectly-segmented-blood-vessel/29773

---

## Post #1 by @ruili (2023-06-01 14:51 UTC)

<p>Slicer version: 5.2.2<br>
System: MacOS Monterey Version 12.4</p>
<p>Hello all,</p>
<p>I have been trying to use the ‘Extract Centerline’ module from the VMTK toolkit in 3D Slicer to extract the centerline of a region of segmented blood vessels. However, as the segmented mask is not perfect, I have been struggling to extract the complete centerlines.</p>
<p>Here is what I did: after loading the original segmented mask, I created a surface model for it and performed moderate smoothing. The semi-transparent object in yellow in all screenshots attached below shows the surface model. I then switched to the ‘Extract Centerline’ module, manually labelled a list of endpoints, and ran the algorithm to extract <em>centerline model and curves</em> (the centerline model is shown as the green curve in centerline_model_1/2.png), and <em>network model and curves</em> (network curves are shown in various colors in network_curves_1/2.png).</p>
<p>As you can see in the screenshots, the problems with my segmentation mask include disjoint segments of one small vessel, holes in the large vessel, and rough vessel surface, etc. These perhaps imposed many difficulties in the subsequent centerline extraction. Examining the current results from ‘Extract Centerline’, I have the following questions:</p>
<ol>
<li>The extracted <em>centerline model</em> did find the desired centerline for the horizontal large vessel at the top, but I wonder why it missed all of the small vessels going downwards?</li>
<li>Could anyone help explain the difference between the <em>centerline model/curves</em> and the <em>network model/curves</em>, or point me to some documentation?</li>
<li>The <em>network curves</em> does capture the centerline of some small vessels, but it is unable to find the centerline in the disjoint segment. Do people have any suggestions on how one may recover a continuous centerline from disjoint regions in an imperfect segmentation mask that should belong to the same vessel?</li>
<li>The <em>network curves</em> in the large vessel seem to be much more susceptible to holes and peaks in the segmentation mask, thus not quite following the desired centerline that I want to extract. Could anyone help explain why this is the case?</li>
</ol>
<p>Any help would be much appreciated!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1d5601cc8e37f14e780c689bb2dcf21c91c5118.jpeg" data-download-href="/uploads/short-url/yvmdXta2LRESMF9NOZlz0LqWL7W.jpeg?dl=1" title="centreline_model_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1d5601cc8e37f14e780c689bb2dcf21c91c5118_2_628x500.jpeg" alt="centreline_model_1" data-base62-sha1="yvmdXta2LRESMF9NOZlz0LqWL7W" width="628" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1d5601cc8e37f14e780c689bb2dcf21c91c5118_2_628x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1d5601cc8e37f14e780c689bb2dcf21c91c5118_2_942x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/1/f1d5601cc8e37f14e780c689bb2dcf21c91c5118_2_1256x1000.jpeg 2x" data-dominant-color="9D9EC8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">centreline_model_1</span><span class="informations">1782×1418 228 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/8264f6e685fa2a6f1639a3d97cb8c44fe20f7610.jpeg" data-download-href="/uploads/short-url/iBwnXJ6wqqFyR1p5oxPe7fOR3I4.jpeg?dl=1" title="centreline_model_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8264f6e685fa2a6f1639a3d97cb8c44fe20f7610_2_628x500.jpeg" alt="centreline_model_2" data-base62-sha1="iBwnXJ6wqqFyR1p5oxPe7fOR3I4" width="628" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8264f6e685fa2a6f1639a3d97cb8c44fe20f7610_2_628x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8264f6e685fa2a6f1639a3d97cb8c44fe20f7610_2_942x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/8264f6e685fa2a6f1639a3d97cb8c44fe20f7610_2_1256x1000.jpeg 2x" data-dominant-color="9D9EC6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">centreline_model_2</span><span class="informations">1782×1418 244 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13a1de606fedb7d8ef77b1d4ca06dcb9c1605773.jpeg" data-download-href="/uploads/short-url/2NFSbqCqxhl7ySAmG10SP46C5gf.jpeg?dl=1" title="network curves_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13a1de606fedb7d8ef77b1d4ca06dcb9c1605773_2_628x500.jpeg" alt="network curves_1" data-base62-sha1="2NFSbqCqxhl7ySAmG10SP46C5gf" width="628" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13a1de606fedb7d8ef77b1d4ca06dcb9c1605773_2_628x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13a1de606fedb7d8ef77b1d4ca06dcb9c1605773_2_942x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/3/13a1de606fedb7d8ef77b1d4ca06dcb9c1605773_2_1256x1000.jpeg 2x" data-dominant-color="9D9EC8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">network curves_1</span><span class="informations">1782×1418 233 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af3e5aba47e4732b06cf1cf99e93cba7773323c5.jpeg" data-download-href="/uploads/short-url/p0h9mxu6K9UhfxExXan9SICCefX.jpeg?dl=1" title="network curves_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af3e5aba47e4732b06cf1cf99e93cba7773323c5_2_628x500.jpeg" alt="network curves_2" data-base62-sha1="p0h9mxu6K9UhfxExXan9SICCefX" width="628" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af3e5aba47e4732b06cf1cf99e93cba7773323c5_2_628x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af3e5aba47e4732b06cf1cf99e93cba7773323c5_2_942x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/f/af3e5aba47e4732b06cf1cf99e93cba7773323c5_2_1256x1000.jpeg 2x" data-dominant-color="9C9CC6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">network curves_2</span><span class="informations">1782×1418 229 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2023-06-01 16:15 UTC)

<p>Generally speaking, supersampling the images before segmentation may help, e.g. with CropVolume.  Or, if you are most interested in the centerlines you could just paint in your expectation of the connection between the vessel parts based on your knowledge of the anatomy (e.g. they are connected in reality but the images just don’t show it well).</p>

---
