# Resampling in the direction where labelmap spans only one slice

**Topic ID**: 30789
**Date**: 2023-07-25
**URL**: https://discourse.slicer.org/t/resampling-in-the-direction-where-labelmap-spans-only-one-slice/30789

---

## Post #1 by @msahin (2023-07-25 19:06 UTC)

<p>Hi everyone,</p>
<p>I am working on extracting radiomics features from MR images. In my dataset, some ROIs span only a single slice. On imageoperations.py I read a comment saying “Do not resample in those directions where labelmap spans only one slice.” I was wondering about the reason for this. Is there a way within PyRadiomics to allow me to resample such cases to make them isotropic?</p>
<p>Thanks,<br>
Meryem</p>

---

## Post #2 by @msahin (2023-07-26 10:47 UTC)

<p>I have found a way to resample such cases. I have changed a line in imageoperations.py from:</p>
<pre><code class="lang-auto"> # Do not resample in those directions where labelmap spans only one slice.
  maskSize = numpy.array(maskNode.GetSize())
  resampledPixelSpacing = numpy.where(bb[Nd_mask:] != 1, resampledPixelSpacing, maskSpacing)
</code></pre>
<p>to:</p>
<pre><code class="lang-auto"> # Do not resample in those directions where labelmap spans only one slice.
  maskSize = numpy.array(maskNode.GetSize())
  resampledPixelSpacing = numpy.where(bb[Nd_mask:] != 0, resampledPixelSpacing, maskSpacing)
</code></pre>
<p>This seemed to help with my problem.</p>

---
