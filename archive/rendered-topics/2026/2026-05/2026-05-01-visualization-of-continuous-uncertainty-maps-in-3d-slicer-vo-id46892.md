---
topic_id: 46892
title: "Visualization Of Continuous Uncertainty Maps In 3D Slicer Vo"
date: 2026-05-01
url: https://discourse.slicer.org/t/46892
---

# Visualization of continuous uncertainty maps in 3D Slicer (volume appears uniform color)

**Topic ID**: 46892
**Date**: 2026-05-01
**URL**: https://discourse.slicer.org/t/visualization-of-continuous-uncertainty-maps-in-3d-slicer-volume-appears-uniform-color/46892

---

## Post #1 by @Alexia_Canosa_Rojo (2026-05-01 17:07 UTC)

<p>Hi,</p>
<p>I am trying to visualize a continuous uncertainty map (entropy-based) generated from a deep learning segmentation model in 3D Slicer.</p>
<p>The NIfTI file contains floating-point values (not binary), with a range approximately between 0 and 0.35 and millions of unique values. However, when I load it in Slicer, it appears as a uniform color (no visible gradient), even when using it as a foreground volume with opacity and applying different colormaps (e.g., Inferno, Hot).</p>
<p>I have already tried:</p>
<ul>
<li>Disabling auto window/level and manually adjusting the range</li>
<li>Changing colormaps</li>
<li>Overlaying it on the PET volume</li>
<li>Verifying that the data is continuous using Python (many unique values)</li>
</ul>
<p>Despite this, the map still looks flat (single color), instead of showing a smooth gradient.</p>
<p>My questions are:</p>
<ol>
<li>How should continuous scalar volumes be visualized correctly in 3D Slicer?</li>
<li>Is there a recommended way to rescale or normalize the data for better visualization?</li>
<li>Could Slicer be interpreting the volume incorrectly (e.g., as labelmap instead of scalar)?</li>
</ol>
<p>Any guidance would be greatly appreciated.</p>
<p>Thanks!</p>

---

## Post #2 by @pieper (2026-05-01 17:43 UTC)

<p>That should be supported with no problem in Slicer.  Maybe you could share an example.  Maybe it’s not being saved as float or maybe there’s something else going on.</p>

---

## Post #3 by @Alexia_Canosa_Rojo (2026-05-01 18:00 UTC)

<p>Thanks for your reply!</p>
<p>I checked the file in Python using nibabel, and it is indeed stored as a floating-point volume (float32) with a large number of unique values (millions), so it is definitely not binary.</p>
<p>For example:</p>
<ul>
<li>min ≈ 0.0</li>
<li>max ≈ 0.35</li>
<li>number of unique values &gt; 2 million</li>
</ul>
<p>However, in Slicer it still appears as a uniform color, even when:</p>
<ul>
<li>loaded as a scalar volume</li>
<li>used as a foreground with opacity over the PET</li>
<li>applying different colormaps (Inferno, Hot)</li>
<li>manually adjusting window/level</li>
</ul>
<p>I suspect the issue might be related to the value distribution being very skewed (most voxels close to zero), so the contrast is not well represented.</p>
<p>Do you think rescaling (e.g., percentile-based normalization) before loading into Slicer would be the correct approach? Or is there a recommended way in Slicer to visualize such highly skewed scalar volumes?</p>
<p>This link contains the NIfTI file if needed: <a href="https://drive.google.com/file/d/1M_4hVtoldng_uQpgJwLan57OOZFdETz4/view?usp=share_link" rel="noopener nofollow ugc">https://drive.google.com/file/d/1M_4hVtoldng_uQpgJwLan57OOZFdETz4/view?usp=share_link</a></p>
<p>Thanks again!</p>

---

## Post #4 by @pieper (2026-05-01 18:09 UTC)

<p>Thanks for sharing the file, something must have happened when you saved that converted to integer.</p>
<p>Here’s what it looks like in slicer:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd28ea2a3be1b17dd31ffe4ee9bae307ba8f7e3a.png" data-download-href="/uploads/short-url/tgVxwP9X3jGtXVAy3sSo23fXT8S.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd28ea2a3be1b17dd31ffe4ee9bae307ba8f7e3a_2_596x500.png" alt="image" data-base62-sha1="tgVxwP9X3jGtXVAy3sSo23fXT8S" width="596" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd28ea2a3be1b17dd31ffe4ee9bae307ba8f7e3a_2_596x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd28ea2a3be1b17dd31ffe4ee9bae307ba8f7e3a_2_894x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd28ea2a3be1b17dd31ffe4ee9bae307ba8f7e3a.png 2x" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1088×912 70.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And here’s what nibabel says:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; a = nibabel.load("/tmp/CHUP-029_high_uncertainty_total.nii.gz")
&gt;&gt;&gt; print(a.header.get_data_dtype())
uint8
</code></pre>

---
