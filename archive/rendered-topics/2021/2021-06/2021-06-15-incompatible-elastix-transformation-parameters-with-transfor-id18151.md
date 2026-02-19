---
topic_id: 18151
title: "Incompatible Elastix Transformation Parameters With Transfor"
date: 2021-06-15
url: https://discourse.slicer.org/t/18151
---

# Incompatible Elastix transformation parameters with Transforms module

**Topic ID**: 18151
**Date**: 2021-06-15
**URL**: https://discourse.slicer.org/t/incompatible-elastix-transformation-parameters-with-transforms-module/18151

---

## Post #1 by @HodaGH (2021-06-15 21:22 UTC)

<p>Hi,</p>
<p>The resulting transform parameters from parameters file or elastix log are different from what I see in the transforms module and this is happening for all my registrations.<br>
For example this is in the transform parameter file<br>
(TransformParameters -0.03651878797625225 0.003033123843879148 -0.0006397282655260022 9.21029262141312 -27.286980280721142 252.7584809282367)<br>
And this is what I see in the Transform Module:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9dc182e9711dfef781cf1c98bf5368b544ad952.png" data-download-href="/uploads/short-url/xmONEmogHvKLUkljNuL4tvj67Au.png?dl=1" title="Screen Shot 2021-06-15 at 5.20.29 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9dc182e9711dfef781cf1c98bf5368b544ad952.png" alt="Screen Shot 2021-06-15 at 5.20.29 PM" data-base62-sha1="xmONEmogHvKLUkljNuL4tvj67Au" width="690" height="492" data-dominant-color="323233"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-06-15 at 5.20.29 PM</span><span class="informations">1068×762 25.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Which is the correct one?</p>
<p>Thank you.</p>

---

## Post #2 by @HodaGH (2021-06-16 00:25 UTC)

<p>here is another example with more difference</p>
<p>(TransformParameters -0.10761595892949985 0.034073286732973586 -0.00008801191874278422 12.692584965893245 -31.151640872040343 145.8404685931222)</p>
<p>but this in the Transforms module<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ec0f369cbde36b72e2bb95ba2cc5791e2856ce9.png" data-download-href="/uploads/short-url/6FBmfAtJJ0gl9Sj6Qpcf9dnexdv.png?dl=1" title="Screen Shot 2021-06-15 at 8.24.37 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2ec0f369cbde36b72e2bb95ba2cc5791e2856ce9.png" alt="Screen Shot 2021-06-15 at 8.24.37 PM" data-base62-sha1="6FBmfAtJJ0gl9Sj6Qpcf9dnexdv" width="690" height="485" data-dominant-color="323333"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-06-15 at 8.24.37 PM</span><span class="informations">1074×756 26.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @mikebind (2021-06-16 18:03 UTC)

<p>Elastix and Slicer represent the transformation differently.  You might notice that there are only 6 numbers in the Elastix representation of the transform, whereas there are 12 in the Slicer representation. The Elastix representation parameters are 3 rotation and 3 translation parameters. The Slicer representation is a 4x4 homogeneous affine transformation matrix.  The translation parts might differ either because</p>
<ul>
<li>the order of translation vs rotation may differ between the two representations,</li>
<li>because a “CenterOfRotationPoint” was specified in the Elastix file, or</li>
<li>because Slicer is representing the “fixed to moving” transform and Elastix is representing the “moving to fixed” transform (these are inverses of each other).</li>
</ul>
<p>I think it is likely the last one (moving to fixed vs fixed to moving), but I would need to take a closer look and do some testing to be 100% sure.</p>
<p>The following code shows exactly how Slicer converts from the Elastix version to the matrix version.</p>
<aside class="onebox githubblob">
  <header class="source">

      <a href="https://github.com/lassoan/SlicerElastix/blob/master/Elastix/Elastix.py#L537-L619" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerElastix/blob/master/Elastix/Elastix.py#L537-L619" target="_blank" rel="noopener nofollow ugc">lassoan/SlicerElastix/blob/master/Elastix/Elastix.py#L537-L619</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="537" style="counter-reset: li-counter 536 ;">
          <li>  def readElastixLinearTransformToVTK(self, filename, outputGeneralTransform):</li>
          <li>    """</li>
          <li>    Example transform file that this method can parse:</li>
          <li>
          </li>
<li>(Transform "EulerTransform")</li>
          <li>(NumberOfParameters 6)</li>
          <li>(TransformParameters 0.022507 0.013835 0.013726 7.760838 4.879223 -0.014589)</li>
          <li>(InitialTransformParametersFileName "NoInitialTransform")</li>
          <li>(UseBinaryFormatForTransformationParameters "false")</li>
          <li>(HowToCombineTransforms "Compose")</li>
          <li>...</li>
          <li>// EulerTransform specific</li>
          <li>(CenterOfRotationPoint 0.0002500000 0.0002500000 0.0000000000)</li>
          <li>(ComputeZYX "false")</li>
          <li>
          </li>
<li>    """</li>
          <li>    f = open(filename, 'r')</li>
          <li>    fileContents = f.read()</li>
          <li>    f.close()</li>
          <li>    fileContents = fileContents.split("\n")</li>
      </ol>
    </code>
  </pre>

  This file has been truncated. <a href="https://github.com/lassoan/SlicerElastix/blob/master/Elastix/Elastix.py#L537-L619" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
