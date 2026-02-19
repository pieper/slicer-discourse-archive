---
topic_id: 17883
title: "Whitematteranalysis Subject Space Problem"
date: 2021-05-31
url: https://discourse.slicer.org/t/17883
---

# Whitematteranalysis subject space problem

**Topic ID**: 17883
**Date**: 2021-05-31
**URL**: https://discourse.slicer.org/t/whitematteranalysis-subject-space-problem/17883

---

## Post #1 by @ferru (2021-05-31 12:23 UTC)

<p>Operating system: Mac OS<br>
Slicer version: 4.11<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi,<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74d8ba359818cf88d4c81313dbea4b1953256807.png" data-download-href="/uploads/short-url/gFFIOBGMPShgOVSMBpPhixTyCOj.png?dl=1" title="Captura de Pantalla 2021-05-31 a la(s) 01.10.23" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74d8ba359818cf88d4c81313dbea4b1953256807_2_690x405.png" alt="Captura de Pantalla 2021-05-31 a la(s) 01.10.23" data-base62-sha1="gFFIOBGMPShgOVSMBpPhixTyCOj" width="690" height="405" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/4/74d8ba359818cf88d4c81313dbea4b1953256807_2_690x405.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74d8ba359818cf88d4c81313dbea4b1953256807.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/74d8ba359818cf88d4c81313dbea4b1953256807.png 2x" data-dominant-color="7A7693"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Pantalla 2021-05-31 a la(s) 01.10.23</span><span class="informations">888×522 412 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I run de pipeline to perform the whole-brain tractography parcellation using the WMA. software and the anatomically ORG white matter atlas.<br>
This includes the “wm_harden_transform.py” to transforms the fiber clusters in the atlas space back to the DWI subject space (Ussing “-i” in the command).<br>
Finally I get the anatomical fibers, but they are not in the subject or the atlas space (see picture).</p>
<p>Any suggestions?</p>
<p>Thanks a lot</p>

---

## Post #2 by @lassoan (2021-05-31 19:21 UTC)

<p>DICOM and all medical image computing software standardized on using LPS coordinate system in files. It was painful to achieve this in 3D Slicer (only reached it in Slicer-4.11), but now we are fully compliant. See more information <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide/Slicer#Slicer_5.0:_Models_are_saved_in_LPS_coordinate_system_by_default">here</a>.</p>
<p>In your case, probably the simplest is to specify to Slicer that the input model is in RAS by changing this line:</p>
<aside class="onebox githubblob">
  <header class="source">

      <a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/3b1a57b1e7593ab99496851de17c61e33758a45b/bin/harden_transform_with_slicer.py#L16" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerDMRI/whitematteranalysis/blob/3b1a57b1e7593ab99496851de17c61e33758a45b/bin/harden_transform_with_slicer.py#L16" target="_blank" rel="noopener">SlicerDMRI/whitematteranalysis/blob/3b1a57b1e7593ab99496851de17c61e33758a45b/bin/harden_transform_with_slicer.py#L16</a></h4>



  <pre class="onebox">    <code class="lang-py">
      <ol class="start lines" start="6" style="counter-reset: li-counter 5 ;">
          <li>import shutil</li>
          <li>
          </li>
<li>def harden_transform(polydata, transform, inverse, outdir):</li>
          <li>    </li>
          <li>    polydata_base_path, polydata_name = os.path.split(polydata)</li>
          <li>    output_name = os.path.join(outdir, polydata_name)</li>
          <li>    </li>
          <li>    if os.path.exists(output_name):</li>
          <li>        return</li>
          <li>    </li>
          <li class="selected">    check_load, polydata_node = slicer.util.loadModel(str(polydata), 1)</li>
          <li>    if not check_load:</li>
          <li>        print('Could not load polydata file:', polydata)</li>
          <li>        return</li>
          <li>
          </li>
<li>    check_load, transform_node = slicer.util.loadTransform(str(transform), 1)</li>
          <li>    if not check_load:</li>
          <li>        print('Could not load transform file:', transform)</li>
          <li>        return</li>
          <li>
          </li>
<li>    if polydata_node.GetPolyData().GetNumberOfCells() == 0:</li>
      </ol>
    </code>
  </pre>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>To this (to use a lower level API that allows specification of the coordinate system of the loaded model):</p>
<pre><code class="lang-python">slicer.util.loadNodeFromFile(str(polydata), 'ModelFile',
  {'coordinateSystem': slicer.vtkMRMLModelStorageNode.CoordinateSystemRAS},
  returnNode=True)
</code></pre>

---

## Post #3 by @ferru (2021-06-04 19:17 UTC)

<p>Thanks Andras for your answer.<br>
I use the Slicer 4.11v and I can choose the coordinate system before loading the model (RAS or LPS) but neither of the two works (see picture for the T_CST_left tract)</p>
<p>Best regards</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ceb267e3b0ee646ab3772b4d8a6139c34c9ac963.jpeg" data-download-href="/uploads/short-url/tuwAGanm3gDj9RuD0eC3s5i6cuv.jpeg?dl=1" title="Captura de Pantalla 2021-06-04 a la(s) 16.16.24" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ceb267e3b0ee646ab3772b4d8a6139c34c9ac963_2_690x416.jpeg" alt="Captura de Pantalla 2021-06-04 a la(s) 16.16.24" data-base62-sha1="tuwAGanm3gDj9RuD0eC3s5i6cuv" width="690" height="416" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/ceb267e3b0ee646ab3772b4d8a6139c34c9ac963_2_690x416.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ceb267e3b0ee646ab3772b4d8a6139c34c9ac963.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ceb267e3b0ee646ab3772b4d8a6139c34c9ac963.jpeg 2x" data-dominant-color="7E7FA7"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Captura de Pantalla 2021-06-04 a la(s) 16.16.24</span><span class="informations">892×538 109 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-06-04 19:50 UTC)

<p>NRRD image file coordinate system is very well defined, surface mesh coordinate systems are also clearly defined (as long as you know if LPS or RAS axis directions are used), so if there is misalignment then it is how the data is created or processed. You need to contact WMA software developers, for example by submitting a bug report to their repository. Copy here the link to the submitted bug report for future reference.</p>

---
