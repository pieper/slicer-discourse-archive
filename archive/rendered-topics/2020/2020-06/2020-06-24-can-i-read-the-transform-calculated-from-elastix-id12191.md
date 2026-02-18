# Can I read the transform calculated from elastix

**Topic ID**: 12191
**Date**: 2020-06-24
**URL**: https://discourse.slicer.org/t/can-i-read-the-transform-calculated-from-elastix/12191

---

## Post #1 by @timeanddoctor (2020-06-24 05:12 UTC)

<p>I’d like to add an already calculated elastix transform file(txt) to Slicer. However, when I try to add the file to Slicer using the “Add Data” screen, it fails almost silently.</p>

---

## Post #2 by @lassoan (2020-06-25 21:39 UTC)

<p>Unfortunately, elastix uses its own transformation file format, but you can use the <a href="https://github.com/lassoan/SlicerElastix/blob/master/Elastix/Elastix.py#L525"><code>readElastixTransformToVTK</code> function</a> we implemented in SlicerElastix to read an elastix transform. It only supports linear and bspline components.</p>
<p>To make things simpler, you can add your registration parameter set file to SlicerElastix preset list and run Elastix from Slicer. Then the module automatically imports the output transform file into Slicer.</p>

---

## Post #3 by @timeanddoctor (2020-06-26 12:25 UTC)

<p>Compared with the volume create with the SlicerElastix module, there is a huge difference  with aplling the transform.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b06245446c5e2c944e2ee09606a73c6d736d2fd.jpeg" data-download-href="/uploads/short-url/cZeBKcKBHvkMo3kg6ohs4YecRWt.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b06245446c5e2c944e2ee09606a73c6d736d2fd_2_593x500.jpeg" alt="image" data-base62-sha1="cZeBKcKBHvkMo3kg6ohs4YecRWt" width="593" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b06245446c5e2c944e2ee09606a73c6d736d2fd_2_593x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b06245446c5e2c944e2ee09606a73c6d736d2fd_2_889x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5b06245446c5e2c944e2ee09606a73c6d736d2fd_2_1186x1000.jpeg 2x" data-dominant-color="A8A4B6"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1249×1052 446 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @timeanddoctor (2020-06-26 12:33 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d317abd7cd562c73ded1c94a8c0c9671f75d3fbf.jpeg" data-download-href="/uploads/short-url/u7psCO9Jck4jEKFK6mevU3n601x.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d317abd7cd562c73ded1c94a8c0c9671f75d3fbf_2_690x334.jpeg" alt="image" data-base62-sha1="u7psCO9Jck4jEKFK6mevU3n601x" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d317abd7cd562c73ded1c94a8c0c9671f75d3fbf_2_690x334.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d317abd7cd562c73ded1c94a8c0c9671f75d3fbf_2_1035x501.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d317abd7cd562c73ded1c94a8c0c9671f75d3fbf_2_1380x668.jpeg 2x" data-dominant-color="B0ADC7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1490×722 362 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @timeanddoctor (2020-06-26 12:37 UTC)

<p>the mrb file (4.11.0-2020-06-17 r29154 / 2a9d59c)<br>
<a href="https://c-t.work/s/1f0cca770c1642" class="onebox" target="_blank" rel="nofollow noopener">https://c-t.work/s/1f0cca770c1642</a></p>
<p>42majh                 （  24h）</p>

---

## Post #6 by @timeanddoctor (2020-06-26 12:44 UTC)

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/nipy/nipype/blob/4f08c9abd6744f2ef346ebc524590ed1aa0abf75/nipype/interfaces/elastix/utils.py#L46" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/nipy/nipype/blob/4f08c9abd6744f2ef346ebc524590ed1aa0abf75/nipype/interfaces/elastix/utils.py#L46" target="_blank" rel="nofollow noopener">nipy/nipype/blob/4f08c9abd6744f2ef346ebc524590ed1aa0abf75/nipype/interfaces/elastix/utils.py#L46</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="36" style="counter-reset: li-counter 35 ;">
<li>    output_format = traits.Enum('nii.gz', 'nii', 'mhd', 'hdr', 'vtk',</li>
<li>                                argstr='ResultImageFormat',</li>
<li>                                desc='set a new image format for resampled images')</li>
<li>    output_file = File(desc='the filename for the resulting transform file')</li>
<li>
</li><li>
</li><li>class EditTransformOutputSpec(TraitedSpec):</li>
<li>    output_file = File(exists=True, desc='output transform file')</li>
<li>
</li><li>
</li><li class="selected">class EditTransform(BaseInterface):</li>
<li>    """</li>
<li>    Manipulates an existing transform file generated with elastix</li>
<li>
</li><li>    Example</li>
<li>    -------</li>
<li>
</li><li>    &gt;&gt;&gt; from nipype.interfaces.elastix import EditTransform</li>
<li>    &gt;&gt;&gt; tfm = EditTransform()</li>
<li>    &gt;&gt;&gt; tfm.inputs.transform_file = 'TransformParameters.0.txt'  # doctest: +SKIP</li>
<li>    &gt;&gt;&gt; tfm.inputs.reference_image = 'fixed1.nii'  # doctest: +SKIP</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #7 by @lassoan (2020-06-26 14:24 UTC)

<p>It all looks good except:</p>
<ul>
<li>non-linear transforms are only reflected in volume rendering if you harden the transform on the volume</li>
<li>automatic intensity-based registration methods typically cannot converge if initial rotation error was more than a few ten degrees; you can fix this by pre-aligning the volumes by an approximate landmark registration using 3-4 points (using Fiducial registration wizard module of SlicerIGT):</li>
</ul>
<div class="youtube-onebox lazy-video-container" data-video-id="TBHr2wizGTM" data-video-title="Align 3D objects using landmarks in 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=TBHr2wizGTM" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/TBHr2wizGTM/maxresdefault.jpg" title="Align 3D objects using landmarks in 3D Slicer" width="" height="">
  </a>
</div>

<p>The referenced <code>EditTransform</code> function just modifies parts of a transform file, it cannot transform 3D objects.</p>

---
