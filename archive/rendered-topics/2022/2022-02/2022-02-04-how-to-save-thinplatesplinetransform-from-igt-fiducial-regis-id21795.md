# How to save ThinPlateSplineTransform (from IGT Fiducial registration) as a deformation field?

**Topic ID**: 21795
**Date**: 2022-02-04
**URL**: https://discourse.slicer.org/t/how-to-save-thinplatesplinetransform-from-igt-fiducial-registration-as-a-deformation-field/21795

---

## Post #1 by @Mukund (2022-02-04 02:32 UTC)

<p>Hi, I was able to successfully use IGT Fiducial registration wizard for manually registering images (with “Transform” option set to “Warping”, which uses thin plate splines) . Next I would like to use the generated transform file independently to map separate set of points from ‘From/Source’ image space to ‘Target’ image space (and vice versa).</p>
<p>I tried two approach:</p>
<ol>
<li>Trying to export transform as deformation field nrrd-&gt; Fails with an error “Cannot save FILENAME to FILENAME.nrrd”</li>
<li>Trying to load the saved transform into using itk::TransformFileReader → ITK seems to not recognizing this type of transform - “ThinPlateSplineKernelTransform_double_3_3”</li>
</ol>
<p>It’s looking like my only recourse would be to bypass the transform file entirely and only store the fiducial points and load them in ITK and create the transform there directly.</p>
<p>Thank you for the wonderful tool! Would appreciate any more direct way to resolve this issue.</p>

---

## Post #2 by @lassoan (2022-02-04 03:51 UTC)

<aside class="quote no-group" data-username="Mukund" data-post="1" data-topic="21795">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mukund/48/14149_2.png" class="avatar"> Mukund:</div>
<blockquote>
<p>Trying to export transform as deformation field nrrd-&gt; Fails with an error “Cannot save FILENAME to FILENAME.nrrd”</p>
</blockquote>
</aside>
<p>A TPS transform cannot be saved as a displacement field, but you can convert it to a grid transform in Transforms module Convert section to convert it to a grid transform (can be saved as an ITK transform or nrrd file) or a vector image (can be saved as a nrrd file). See some information <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#save-transform">here</a>. If the instructions are not clear or detailed enough then let us know and we’ll improve the documentation accordingly.</p>
<aside class="quote no-group" data-username="Mukund" data-post="1" data-topic="21795">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mukund/48/14149_2.png" class="avatar"> Mukund:</div>
<blockquote>
<p>Trying to load the saved transform into using itk::TransformFileReader → ITK seems to not recognizing this type of transform - “ThinPlateSplineKernelTransform_double_3_3”</p>
</blockquote>
</aside>
<p>You can save the transform to ITK transform file and ITK can read it. This is how we save and load the transforms in Slicer. Make sure your ITK is built with ThinPlateSplineKernelTransform registered in the transform IO factory (if you don’t build ITK then you can request this from the maintainer of your ITK distribution).</p>

---
