---
topic_id: 42332
title: "Input Orientation And Axis Indexing In Pyradiomics Simpleitk"
date: 2025-03-27
url: https://discourse.slicer.org/t/42332
---

# Input Orientation and Axis Indexing in PyRadiomics (SimpleITK vs NumPy)

**Topic ID**: 42332
**Date**: 2025-03-27
**URL**: https://discourse.slicer.org/t/input-orientation-and-axis-indexing-in-pyradiomics-simpleitk-vs-numpy/42332

---

## Post #1 by @valosekj (2025-03-27 17:14 UTC)

<p>Is there a specific orientation (axis order) expected by Pyradiomics when processing input images? I’m asking in the context of <a href="https://insightsoftwareconsortium.github.io/SimpleITK-Notebooks/Python_html/03_Image_Details.html#Conversion-between-numpy-and-SimpleITK" rel="noopener nofollow ugc">the opposite axes indexing between numpy/nibabel and SimpleITK </a>:</p>
<blockquote>
<p>SimpleITK and numpy indexing access is in opposite order!</p>
<p>SimpleITK: image[x,y,z]<br>
numpy: image_numpy_array[z,y,x]</p>
</blockquote>
<p>Since <a href="https://github.com/AIM-Harvard/pyradiomics?tab=readme-ov-file#3rd-party-packages-used-in-pyradiomics" rel="noopener nofollow ugc">Pyradiomics uses SimpleITK internally</a>, should the input axis order be interpreted as <code>x, y, z</code>?</p>
<p>If so, does this imply the following mapping for the <code>force2Ddimension</code>?</p>
<ul>
<li><code>0</code> == <code>x</code> == axial</li>
<li><code>1</code> == <code>y</code> == coronal</li>
<li><code>2</code> == <code>z</code> == sagittal</li>
</ul>
<details>
<summary> force2Ddimension details</summary>
<blockquote>
<pre data-code-wrap="json"><code class="lang-json">force2Ddimension: 0  # axial slices, for coronal slices, use dimension 1 and for sagittal, dimension 2
</code></pre>
</blockquote>
<aside class="onebox githubblob" data-onebox-src="https://github.com/AIM-Harvard/pyradiomics/blob/dea5faf55f486d6f7233561401d8da91d07ce0ad/examples/exampleSettings/exampleMR_NoResampling.yaml#L68-L72">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/pyradiomics/blob/dea5faf55f486d6f7233561401d8da91d07ce0ad/examples/exampleSettings/exampleMR_NoResampling.yaml#L68-L72" target="_blank" rel="noopener nofollow ugc">github.com/AIM-Harvard/pyradiomics</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/AIM-Harvard/pyradiomics/blob/dea5faf55f486d6f7233561401d8da91d07ce0ad/examples/exampleSettings/exampleMR_NoResampling.yaml#L68-L72" target="_blank" rel="noopener nofollow ugc">examples/exampleSettings/exampleMR_NoResampling.yaml</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/AIM-Harvard/pyradiomics/blob/dea5faf55f486d6f7233561401d8da91d07ce0ad/examples/exampleSettings/exampleMR_NoResampling.yaml#L68-L72" rel="noopener nofollow ugc"><code>dea5faf55</code></a>
</div>



    <pre class="onebox"><code class="lang-yaml">
      <ol class="start lines" start="68" style="counter-reset: li-counter 67 ;">
          <li># Forced 2D extracion:</li>
          <li># This allows to calculate texture features using anisotropic voxels (although it assumes that voxels are isotropic</li>
          <li># in-plane). This is an alternative to resampling the image to isotropic voxels.</li>
          <li>force2D: true</li>
          <li>force2Ddimension: 0  # axial slices, for coronal slices, use dimension 1 and for sagittal, dimension 2.</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

</details>
<p>Does Pyradiomics automatically reorder axes internally to match SimpleITK’s conventions (<code>x, y, z</code>), or is it the user’s responsibility to ensure the input image has the correct orientation?</p>

---

## Post #2 by @pieper (2025-03-27 18:27 UTC)

<p>I don’t recall exactly what pyradiomics does, but I believe it resamples the segmentation to match the geometry of the source image (or maybe the other way around).</p>
<p>Keep in mind that medical images can be acquired in many different orientations, so you should not make assumptions about the relationship between world space and index space.  In Slicer that information is in the <code>ijkToRAS</code> matrix and related ones.  See this info: <a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html">https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html</a></p>

---

## Post #3 by @valosekj (2025-03-27 19:03 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="42332">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Keep in mind that medical images can be acquired in many different orientations, so you should not make assumptions about the relationship between world space and index space</p>
</blockquote>
</aside>
<p>You’are right! This is exactly why I want to reorient all my images to the same orientation before calling <code>pyradiomics</code>. Please note that I’m calling <code>pyradiomics</code> from the CLI, not via Slicer.</p>
<p>I should have mentioned in my first comment what I meant by axial, coronal, and sagittal, so clarifying it now:</p>
<ul>
<li><code>0</code> == <code>x</code> == axial == Superior-Inferior</li>
<li><code>1</code> == <code>y</code> == coronal == Anterior-Posterior</li>
<li><code>2</code> == <code>z</code> == sagittal == Right-Left</li>
</ul>
<p>(<a href="https://github.com/AIM-Harvard/pyradiomics/blob/dea5faf55f486d6f7233561401d8da91d07ce0ad/examples/exampleSettings/exampleMR_NoResampling.yaml#L68-L72" rel="noopener nofollow ugc">source</a> for numbers <code>0, 1, 2</code> and planes <code>axial, coronal, saggital</code>; <a href="https://insightsoftwareconsortium.github.io/SimpleITK-Notebooks/Python_html/03_Image_Details.html#Conversion-between-numpy-and-SimpleITK" rel="noopener nofollow ugc">source</a> for <code>x, y, z</code>)</p>
<p>Which effectively translates into SAR (<strong>S</strong>uperior-<strong>A</strong>nterior-<strong>R</strong>ight) orientation, right?</p>
<p>This is however contradicted by <a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html#itk" rel="noopener nofollow ugc">this source</a>:</p>
<blockquote>
<p>ITK uses the LPS convention.</p>
</blockquote>

---

## Post #4 by @pieper (2025-03-27 19:18 UTC)

<p>Just to restate what I said earlier, the 0, 1, 2 and x, y, z in image space that you are referring to do not correspond to any particular world space direction or slicing plane.  That mapping is defined by an affine matrix.</p>
<p>You’ll need to study the pyradiomics code, but as I recall it takes care of the resampling for you.</p>
<p>But if you want to make sure all your test data is anatomically aligned, you need to be sure to understand and apply the transformations I’ve described.</p>

---

## Post #5 by @valosekj (2025-03-30 21:41 UTC)

<p>Thank you!</p>
<p>Just to confirm I understand it correctly, let me illustrate what I mean by an example:</p>
<ul>
<li>I have two types of 3D MRI images: T2w axial images and T2w sagittal images.</li>
<li>T2w axial images have a high in-plane resolution in the axial plane and thick slices in the superior-inferior (S-I) axis.</li>
<li>T2w sagittal images have a high in-plane resolution in the sagittal plane and thick slices in the right-left (R-L) axis.</li>
<li>I reoriented both images to the <a href="https://slicer.readthedocs.io/en/latest/user_guide/coordinate_systems.html#anatomical-coordinate-system" rel="noopener nofollow ugc">RAS coordinate system</a></li>
</ul>
<p>When inspecting the reoriented images using <code>SimpleITK</code>, I get the following:</p>
<pre data-code-wrap="python"><code class="lang-python">&gt;&gt;&gt; import SimpleITK as sitk
&gt;&gt;&gt; image_ax = sitk.ReadImage('sub-001_acq-ax_T2w_RAS.nii.gz')
&gt;&gt;&gt; image_ax.GetSpacing()
(0.5624999403953552, 0.5625000596046448, 3.7499988079071045)


&gt;&gt;&gt; import SimpleITK as sitk
&gt;&gt;&gt; image_sag = sitk.ReadImage('sub-001_acq-sag_T2w_RAS.nii.gz')
&gt;&gt;&gt; image_sag.GetSpacing()
(3.4499998092651367, 0.48828125, 0.4882812798023224)
</code></pre>
<ul>
<li>the axial image (<code>sub-001_acq-ax_T2w_RAS.nii.gz</code>) has correctly the highest spacing (i.e., thick slices) in the last dimension (<code>S-I</code>)</li>
<li>the sagittal image (<code>sub-001_acq-sag_T2w_RAS.nii.gz</code>) has correctly the highest spacing in the first dimension (<code>R-L</code>)</li>
</ul>
<p>Then it matches the <a href="https://github.com/AIM-Harvard/pyradiomics/blob/dea5faf55f486d6f7233561401d8da91d07ce0ad/examples/exampleSettings/exampleMR_NoResampling.yaml#L72" rel="noopener nofollow ugc">pyradiomics</a> example, which states:</p>
<blockquote>
<p>force2Ddimension: 0  # axial slices, for coronal slices, use dimension 1 and for sagittal, dimension 2.</p>
</blockquote>

---

## Post #6 by @joshuacwnewton (2025-04-11 16:57 UTC)

<aside class="quote no-group" data-username="valosekj" data-post="3" data-topic="42332">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/valosekj/48/79834_2.png" class="avatar"> valosekj:</div>
<blockquote>
<ul>
<li><code>0</code> == <code>x</code> == axial == Superior-Inferior</li>
<li><code>1</code> == <code>y</code> == coronal == Anterior-Posterior</li>
<li><code>2</code> == <code>z</code> == sagittal == Right-Left</li>
</ul>
</blockquote>
</aside>
<p>Just popping in to try to clarify what <a class="mention" href="/u/valosekj">@valosekj</a> is referring to by the above quote.</p>
<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="42332">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Just to restate what I said earlier, the 0, 1, 2 and x, y, z in image space that you are referring to do not correspond to any particular world space direction or slicing plane. That mapping is defined by an affine matrix.</p>
</blockquote>
</aside>
<p>We’re coming from the world of NIFTI1 images, <code>nibabel</code>, and FSL (specifically tools like the FSLeyes image viewer and <code>fslhd</code>). As far as I understand:</p>
<ul>
<li>For <code>nibabel</code> and FSL, affine matrices are assumed to <a href="https://nipy.org/nibabel/coordinate_systems.html#the-affine-matrix-as-a-transformation-between-spaces" rel="noopener nofollow ugc">always map the voxel array to RAS+ world space</a>.</li>
<li>However, in voxel space, the array can be “reoriented” (i.e. axes transposition and inversion). For FSL, this can be done with <code>fslswapdim</code>. In order to preserve the “always maps to RAS+” assumption, if the data array is changed, then the affine will be changed in kind.</li>
<li>The tool <code>fslhd</code> reports the header information in NIFTI1 image files. Part of the output information is the axis ordering corresponding to the qform/sform affine matrices. For example, on a sample image I’ve picked out, the command reports:<pre><code class="lang-auto">sto_xyz:1       0.000000 0.000000 1.000000 -32.219284 
sto_xyz:2       -1.000000 0.000000 0.000000 31.786606 
sto_xyz:3       0.000000 1.000000 0.000000 -19.321671 
sto_xyz:4       0.000000 0.000000 0.000000 1.000000 
sform_xorient   Anterior-to-Posterior
sform_yorient   Inferior-to-Superior
sform_zorient   Left-to-Right
</code></pre>
</li>
<li>Because of this information, our lab will refer to such images in shorthand as “AIL-/PSR+ images”. In other words, for this example image, the voxel-space array has an orientation associated with it (<code>0 = x = AP</code>, <code>1 = y = IS</code>, <code>2 = z = LR</code>), but only because of the inherent assumption that the affine will always map to RAS+ physical space.
<ul>
<li>Side note: This can be intuited via the above affine. The <code>-1</code> in the first column flips the so-called “PSR+ image” to be ASR+, and the non-diagonal matrix reorients the axes from ASR+ to RAS+. This kind of intuition is part of why we find it helpful to describe voxel space in physical terms.</li>
</ul>
</li>
<li><em>((For reference, the reason why we describe images in “voxel space terms” is because we do a lot of Python-based image processing where we operate directly on the array using tools such as <code>numpy</code>, <code>skimage</code>, <code>scipy</code>, <code>dipy</code>, etc. Since we process the array using tools that ignore the context of the image header, it is important for us to know which array axes map to which physical axes (which then get universally transformed into RAS+ physical coordinates by the affine matrix).))</em></li>
</ul>
<p>So, I suppose what <a class="mention" href="/u/valosekj">@valosekj</a> is truly asking is:</p>
<ul>
<li>Assuming the images have an affine that universally maps the array to RAS+ physical coordinates, does axis order matter in voxel space?</li>
<li>In other words, will “reorienting” the image in voxel space (i.e. modifying the data array + header in tandem) make any difference for <code>pyradiomics</code>, given the assumption that the affine will always map the array to RAS+?</li>
</ul>
<p>Kind regards,<br>
Joshua</p>

---

## Post #7 by @joshuacwnewton (2025-04-11 18:44 UTC)

<p>OK, I think we have found the source of our confusion:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/AIM-Harvard/pyradiomics/blob/dea5faf55f486d6f7233561401d8da91d07ce0ad/examples/exampleSettings/exampleMR_NoResampling.yaml#L68-L72">
  <header class="source">

      <a href="https://github.com/AIM-Harvard/pyradiomics/blob/dea5faf55f486d6f7233561401d8da91d07ce0ad/examples/exampleSettings/exampleMR_NoResampling.yaml#L68-L72" target="_blank" rel="noopener nofollow ugc">github.com/AIM-Harvard/pyradiomics</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/AIM-Harvard/pyradiomics/blob/dea5faf55f486d6f7233561401d8da91d07ce0ad/examples/exampleSettings/exampleMR_NoResampling.yaml#L68-L72" target="_blank" rel="noopener nofollow ugc">examples/exampleSettings/exampleMR_NoResampling.yaml</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/AIM-Harvard/pyradiomics/blob/dea5faf55f486d6f7233561401d8da91d07ce0ad/examples/exampleSettings/exampleMR_NoResampling.yaml#L68-L72" rel="noopener nofollow ugc"><code>dea5faf55</code></a>
</div>



    <pre class="onebox"><code class="lang-yaml">
      <ol class="start lines" start="68" style="counter-reset: li-counter 67 ;">
          <li># Forced 2D extracion:</li>
          <li># This allows to calculate texture features using anisotropic voxels (although it assumes that voxels are isotropic</li>
          <li># in-plane). This is an alternative to resampling the image to isotropic voxels.</li>
          <li>force2D: true</li>
          <li>force2Ddimension: 0  # axial slices, for coronal slices, use dimension 1 and for sagittal, dimension 2.</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>In this code snippet, the comment implies that 0 = axial, 1 = coronal, and 2 = sagittal. This was confusing for us because we are used to RAS+ orientation (see my <a href="https://discourse.slicer.org/t/input-orientation-and-axis-indexing-in-pyradiomics-simpleitk-vs-numpy/42332/6">previous post</a>).</p>
<p>However, I then found a documentation page on <a href="https://pyradiomics.readthedocs.io/en/latest/customization.html?highlight=force2ddimension" rel="noopener nofollow ugc">force2Ddimension</a> which says:</p>
<blockquote>
<p><code>force2Ddimension</code> [0]: int, range 0-2. Specifies the ‘slice’ dimension for a by-slice feature extraction. A value of 0 represents the native acquisition plane for the images (usually axial for CT and axial, coronal or sagittal for MRI).</p>
</blockquote>
<p>In other words, it seems that the code snippet’s comments were written from a CT-specific perspective (0 = axial), whereas we’re coming from an MRI perspective (0 = sagittal = LR, because our affines are RAS+ based).</p>
<p>I think the confusion has been cleared up? In our case, it seems that we should (A) make sure our voxel-space images are in RAS+ orientation (possibly irrelevant), (B) that the affine transforms the image into RAS+ world space (more relevant?), and (C) select <code>2</code> to specify the SI axis (i.e. axial slices). (Note: using <code>2</code> for axial slices is what we are used to in our processing.)</p>
<p>Kind regards,<br>
Joshua</p>

---

## Post #8 by @pieper (2025-04-11 18:49 UTC)

<p><a class="mention" href="/u/joostjm">@JoostJM</a> or <a class="mention" href="/u/fedorov">@fedorov</a> can you jump in here?</p>

---
