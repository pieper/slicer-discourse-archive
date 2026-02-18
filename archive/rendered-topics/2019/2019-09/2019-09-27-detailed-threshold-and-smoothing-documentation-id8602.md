# detailed threshold and smoothing documentation

**Topic ID**: 8602
**Date**: 2019-09-27
**URL**: https://discourse.slicer.org/t/detailed-threshold-and-smoothing-documentation/8602

---

## Post #1 by @DaveB (2019-09-27 22:21 UTC)

<p>Hi,<br>
I’m new to Slicer.  I’m trying to create a bone model of a lumbar spine from CT images (.6 axial images) to 3d print it.  I’ve gone through all the related tutorials I could find. <strong>Is there detailed documentation on the Automatic Threshold and Smoothing options?  I can’t find that anywhere.</strong>  Btw, I’m mostly using Segment Editor.</p>
<p>I’m trying to create a very accurate 3d lumbar model to show to a surgeon.  I’ve tried dozens of threshold ranges and smoothing combinations.  I now have a 3d printed model that’s somewhat realistic, but there’s too much noise (extrusions) and too much smoothing.  For example, many facet joints get filled in no matter which thresholds &amp; smoothing parameters I use.</p>
<p>If I use higher thresholds, then bone disappears.  If I use lower thresholds to get more bone, then the facet joints get filled in regardless of the smoothing kernel size I use.</p>
<p>It would be helpful to have more detailed documentation on these features.  Please point me to that documentation if it exists.</p>
<p>Thanks, dave</p>

---

## Post #2 by @Amine (2019-09-27 22:51 UTC)

<p>Hi, there is no automatic threshold and segmentation that i know about, though you could use a script like <a href="https://gist.github.com/lassoan/5ad51c89521d3cd9c5faf65767506b37" rel="nofollow noopener">this one</a> to get a fast result, but you might have better results doing it manually,<br>
try cropping your volume (crop volume module) with a spacing scale of 0.6x before starting your segmentation, then use the module “Gradient anisotropic diffusion” to filter some of the noise.<br>
after applying your threshold do all the manual finishing you can before using smoothing (and use the smallest kernel size to keep detail).<br>
As for the facet joints it’s almost impossible to get them separated automatically because they are not well visible on the CT slices, they need manual deletion of a vertebra then the use of boolean operations to keep the other (or to use masking operations to draw individual vertebras from the original segment), you might want to check <a href="https://discourse.slicer.org/t/cut-3d-surface-from-the-whole-with-accuracy/8432">this post</a> for the separation part.</p>

---

## Post #3 by @lassoan (2019-09-28 19:40 UTC)

<aside class="quote no-group" data-username="DaveB" data-post="1" data-topic="8602">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/b5a626/48.png" class="avatar"> DaveB:</div>
<blockquote>
<p><strong>Is there detailed documentation on the Automatic Threshold and Smoothing options? I can’t find that anywhere.</strong> Btw, I’m mostly using Segment Editor.</p>
</blockquote>
</aside>
<p>We use ITK’s automatic threshold computation algorithms options. Their documentation is available <a href="https://itk.org/Doxygen/html/group__ITKThresholding.html">here</a>.</p>
<p>Smoothing pipeline consists of a number of VTK filters. See summary <a href="https://discourse.slicer.org/t/segmentation-algorithm-used-in-3d-slicer/7420/3">here</a> and source code <a href="https://github.com/Slicer/Slicer/blob/master/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx">here</a>.</p>
<aside class="quote no-group" data-username="DaveB" data-post="1" data-topic="8602">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/b5a626/48.png" class="avatar"> DaveB:</div>
<blockquote>
<p>If I use higher thresholds, then bone disappears. If I use lower thresholds to get more bone, then the facet joints get filled in regardless of the smoothing kernel size I use.</p>
</blockquote>
</aside>
<p>Vertebrae are very easy to separate on high-resolution CT scans, but on typical patient scans have much lower resolution.</p>
<p><a class="mention" href="/u/amine">@amine</a> gave an excellent answer on how to approach this. In addition to his suggestions, you may also try masked grow from seeds. See <a href="https://lassoan.github.io/SlicerSegmentationRecipes/AortaMaskedGrowFromSeeds/">this segmentation recipe</a> for details and this short demo video:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="8Nbi1Co2rhY" data-video-title="Femur segmentation using masked region growing in 3D Slicer" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=8Nbi1Co2rhY" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/8Nbi1Co2rhY/maxresdefault.jpg" title="Femur segmentation using masked region growing in 3D Slicer" width="" height="">
  </a>
</div>


---
