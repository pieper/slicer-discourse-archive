---
topic_id: 13243
title: "Elastix 2D 3D Registration Incorrect Ray Cast"
date: 2020-08-31
url: https://discourse.slicer.org/t/13243
---

# Elastix 2d/3d Registration Incorrect Ray Cast

**Topic ID**: 13243
**Date**: 2020-08-31
**URL**: https://discourse.slicer.org/t/elastix-2d-3d-registration-incorrect-ray-cast/13243

---

## Post #1 by @Henry_Cope (2020-08-31 01:53 UTC)

<p>Good Evening,</p>
<p>I’m trying to use the general registration elastix module to register a 3d CT volume I have to an Xray. Before trying my data, I used the 2d/3d test data that comes with Elastix. I tried to register a volume of a head to an xray taken from the sagittal plane view. The module says that it has completed registration and then generates an xray to show the alignment is correct. However, when I compare Xrays, I can see that the volume has not been transformed at all. I’m not sure what’s going wrong here. The only red text I see in the python interactor says that “toVTKString is deprecated” and “‘returnNode’ argument is deprecated.Loaded node is now returned directly if <code>returnNode</code> is not specified.”</p>
<p>Volume to be registered:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/516a1ee4ea8e42df55249ec0a263a32b2ec23b49.png" alt="image" data-base62-sha1="bCe2kASCfbLJmu59u7OhGCkbbJf" width="526" height="371"><br>
Fixed “volume” Xray:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f937da320af33f5cd1f0cf1e4806d27f26ab6cd6.png" alt="image" data-base62-sha1="zyGyiuIbG1osR4vtcGHnXdwtaF8" width="247" height="245"><br>
Resultant Xray:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfa4ec6d9863d3019ad311d38155135c6b2344a6.png" alt="image" data-base62-sha1="tCUbnc5apXgrm1QHBEi5Y5ATw34" width="237" height="303"><br>
View of the control panel setup:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/008ccff757137d7b6dac08a6dd12e01b42974724.png" data-download-href="/uploads/short-url/4RGIVr830novZ0qe6HFPv1h1pG.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/008ccff757137d7b6dac08a6dd12e01b42974724_2_467x500.png" alt="image" data-base62-sha1="4RGIVr830novZ0qe6HFPv1h1pG" width="467" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/008ccff757137d7b6dac08a6dd12e01b42974724_2_467x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/008ccff757137d7b6dac08a6dd12e01b42974724_2_700x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/008ccff757137d7b6dac08a6dd12e01b42974724.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">756×808 24.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-08-31 04:19 UTC)

<p>2D/3D registration is a hard problem. You need to carefully set the initial pose close to the solution, but there may be other tricks, too. I would recommend to ask for help on the <a href="https://groups.google.com/g/elastix-imageregistration">Elastix mailing list</a>.</p>

---

## Post #3 by @Henry_Cope (2020-08-31 20:46 UTC)

<p>Hi Mr. Lasso,<br>
Thank you for your suggestions. I did send an email to the mailing list and have yet to receive a reply. I should also mention I brought the same predicament to the elastix-imageregistration google group a month ago and didn’t receive a reply.<br>
I understand that elastix is outside of your jurisdiction, but I’m hoping you might be able to help me anyway. I looked through the temporary folder and think I found the issue. The final transform parameters correctly register the 3d volume via rotations. Somehow, the rotation parameters of the transform are being lost. I think it might have something to do with the finalraycastinterpolator. My question is this, is it possible to extract the Transform parameters as a Slicer Transform (.h5 file)? I’ve copied the output of my final parameters.txt file:</p>
<p>(Transform “EulerTransform”)<br>
(NumberOfParameters 6)<br>
(TransformParameters 0.001208 -0.000358 0.000508 -0.349885 -0.072703 1.776385)<br>
// This is the transform I’d like to extract<br>
(InitialTransformParametersFileName “NoInitialTransform”)<br>
(UseBinaryFormatForTransformationParameters “false”)<br>
(HowToCombineTransforms “Compose”)</p>
<p>// Image specific<br>
(FixedImageDimension 3)<br>
(MovingImageDimension 3)<br>
(FixedInternalImagePixelType “float”)<br>
(MovingInternalImagePixelType “float”)<br>
(Size 256 256 1)<br>
(Index 0 0 0)<br>
(Spacing 1.1453800000 1.1453800000 1.0000000000)<br>
(Origin -145.4980000000 -146.8890000000 381.7660000000)<br>
(Direction 1.0000000000 0.0000000000 0.0000000000 0.0000000000 1.0000000000 0.0000000000 0.0000000000 0.0000000000 1.0000000000)<br>
(UseDirectionCosines “true”)</p>
<p>// EulerTransform specific<br>
(CenterOfRotationPoint 0.0000000000 0.0000000000 0.0000000000)<br>
(ComputeZYX “false”)</p>
<p>// ResampleInterpolator specific<br>
(ResampleInterpolator “FinalRayCastInterpolator”)<br>
(FocalPoint 0.540000 -0.850000 -813.234000 )<br>
(PreParameters -0.009475 -0.006807 -0.030067 0.000000 0.000000 0.000000 )<br>
(Threshold 1000.000000)</p>
<p>// Resampler specific<br>
(Resampler “DefaultResampler”)<br>
(DefaultPixelValue 0.000000)<br>
(ResultImageFormat “mhd”)<br>
(ResultImagePixelType “float”)<br>
(CompressResultImage “false”)</p>

---

## Post #4 by @lassoan (2020-08-31 20:54 UTC)

<p>Unfortunately, Elastix uses a custom transformation file format, but we have implemented a reader in Slicer that can handle linear and bspline transforms:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/lassoan/SlicerElastix/blob/master/Elastix/Elastix.py#L525-L694" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/lassoan/SlicerElastix/blob/master/Elastix/Elastix.py#L525-L694" target="_blank" rel="noopener">lassoan/SlicerElastix/blob/master/Elastix/Elastix.py#L525-L694</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="525" style="counter-reset: li-counter 524 ;">
<li>  def readElastixTransformToVTK(self, filename, outputGeneralTransform):</li>
<li>    """</li>
<li>    Append transform stored in filename (and recursively, initial transform</li>
<li>    referenced in that transform file) to outputGeneralTransform</li>
<li>    """</li>
<li>    if self.readElastixLinearTransformToVTK(filename, outputGeneralTransform):</li>
<li>      return True</li>
<li>    elif self.readElastixBsplineTransformToVTK(filename, outputGeneralTransform):</li>
<li>      return True</li>
<li>    logging.warning("Cannot interpret transform file: {0}".format(filename))</li>
<li>    return False</li>
<li>
</li><li>  def readElastixLinearTransformToVTK(self, filename, outputGeneralTransform):</li>
<li>    """</li>
<li>    Example transform file that this method can parse:</li>
<li>
</li><li>(Transform "EulerTransform")</li>
<li>(NumberOfParameters 6)</li>
<li>(TransformParameters 0.022507 0.013835 0.013726 7.760838 4.879223 -0.014589)</li>
<li>(InitialTransformParametersFileName "NoInitialTransform")</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/lassoan/SlicerElastix/blob/master/Elastix/Elastix.py#L525-L694" target="_blank" rel="noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>It should be able to read the computer Euler transform, but you can <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools#:~:text=%20Start%20debugging%20%201%20In%20Slicer%3A%0AOpen%20the,paused.%20Slicer%20will%20become%20unresponsive%20until...%20More%20">attach a debugger</a> in the converter and see where things go wrong.</p>

---
