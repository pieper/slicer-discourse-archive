# sitk error. Input for "LabelStatisticsImageFilter" does not match the primary input's size

**Topic ID**: 20326
**Date**: 2021-10-24
**URL**: https://discourse.slicer.org/t/sitk-error-input-for-labelstatisticsimagefilter-does-not-match-the-primary-inputs-size/20326

---

## Post #1 by @Fabio_Nunes (2021-10-24 23:18 UTC)

<p>Hello dear members,</p>
<p>I’ve been working with pyradiomics to try to analyse a segment of pericardial fat. I will replicate the code bellow. Unfortunatly I cannot attach the files here as the upload option does not allow for nrrd files to be uploaded.</p>
<pre><code class="lang-auto">import os
import SimpleITK
import six
from radiomics import featureextractor

imageName =  '/home/my_name/Desktop/image.nrrd'
maskName = '/home/my_name/Desktop/mask.nrrd'

params = '/home/my_name/pyradiomics/examples/exampleSettings/Params.yaml'

extractor = featureextractor.RadiomicsFeatureExtractor(params)

result = extractor.execute(imageName, maskName)
for key, val in six.iteritems(result):
  print("\t%s: %s" %(key, val))

</code></pre>
<p>Once I run the code I get the following error message (see attached image)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bb83d0da38819f40c2397423b7cf53086b76bb2.png" data-download-href="/uploads/short-url/mdyJHgEsYax6TI2wV8G0z2v8LEm.png?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bb83d0da38819f40c2397423b7cf53086b76bb2_2_690x285.png" alt="Untitled" data-base62-sha1="mdyJHgEsYax6TI2wV8G0z2v8LEm" width="690" height="285" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bb83d0da38819f40c2397423b7cf53086b76bb2_2_690x285.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bb83d0da38819f40c2397423b7cf53086b76bb2_2_1035x427.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9bb83d0da38819f40c2397423b7cf53086b76bb2_2_1380x570.png 2x" data-dominant-color="212323"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1604×664 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Has anyone encountered this problem before? Thank you,</p>

---

## Post #2 by @lassoan (2021-10-26 03:03 UTC)

<p>It seems that pyradiomics requires the segmentation mask’s geometry (origin, spacing, axis directions, and extents) to match the analyzed volume’s geometry.</p>

---
