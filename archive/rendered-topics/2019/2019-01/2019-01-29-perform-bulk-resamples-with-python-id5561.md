# Perform bulk resamples with python

**Topic ID**: 5561
**Date**: 2019-01-29
**URL**: https://discourse.slicer.org/t/perform-bulk-resamples-with-python/5561

---

## Post #1 by @Alex_Vergara (2019-01-29 14:37 UTC)

<p>I would like to perform a bulk resampling on several volumes, each volume has another associated who is the reference. I can use the module Resample Image (BRAINS) to do this, but since they are several ones and it is just a matter of defining Image to  warp, Reference image, Output image, interpolation mode and default value and apply, I want to automatize this step.</p>
<p>How can I call recursively the Resample module from within python?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63065456cad1e7366b47b5c09966d867d160a30c.png" alt="" data-base62-sha1="e80PtTm2xf6GdvCYmoDvsL0P100" role="presentation"></p>

---

## Post #2 by @Alex_Vergara (2019-01-29 15:56 UTC)

<p>I am currently having problems with the following code</p>
<pre data-code-wrap="python"><code class="lang-python">    parameters = {'ImageToWarp':itemCT, 'ReferenceImage':itemSPECT, 'OutputImage':clonedNode, 
                          'InterpolationMode':'Lanczos', 'DefaultValue':minCT}
    slicer.cli.run(slicer.modules.brainsresample, None, parameters)
</code></pre>
<p>the output has no data</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/117828f76de0ce02ef7dd77bde5da7025c1016e2.png" data-download-href="/uploads/short-url/2uxyDvucOAZpPXzqV5cvob4Ksam.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/117828f76de0ce02ef7dd77bde5da7025c1016e2_2_690x285.png" alt="image" data-base62-sha1="2uxyDvucOAZpPXzqV5cvob4Ksam" width="690" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/117828f76de0ce02ef7dd77bde5da7025c1016e2_2_690x285.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/117828f76de0ce02ef7dd77bde5da7025c1016e2.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/117828f76de0ce02ef7dd77bde5da7025c1016e2.png 2x" data-dominant-color="080504"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">910×377 5.77 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @Alex_Vergara (2019-01-29 16:05 UTC)

<p>Ok, my mistake, the correct parameter list is</p>
<pre data-code-wrap="python"><code class="lang-python">    parameters = {'inputVolume':itemCT, 'referenceVolume':itemSPECT, 'outputVolume':clonedNode, 
                          'interpolationMode':'Lanczos', 'defaultValue':minCT}
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5de3960de578f0e99297254ac34fdc8821d7fd29.png" data-download-href="/uploads/short-url/doA0mp3R24gv95o2gLt96jPWHHj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5de3960de578f0e99297254ac34fdc8821d7fd29_2_690x285.png" alt="image" data-base62-sha1="doA0mp3R24gv95o2gLt96jPWHHj" width="690" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/d/5de3960de578f0e99297254ac34fdc8821d7fd29_2_690x285.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5de3960de578f0e99297254ac34fdc8821d7fd29.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5de3960de578f0e99297254ac34fdc8821d7fd29.png 2x" data-dominant-color="0D0A0A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">907×375 20.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
