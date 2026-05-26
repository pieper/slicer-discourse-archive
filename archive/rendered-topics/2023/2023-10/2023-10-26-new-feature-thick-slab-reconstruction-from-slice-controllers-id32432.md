---
topic_id: 32432
title: "New feature: Thick slab reconstruction from slice controllers and views"
date: 2023-10-26
url: https://discourse.slicer.org/t/32432
last_bumped: 2026-04-17T23:18:51.976Z
---

# New feature: Thick slab reconstruction from slice controllers and views

**Topic ID**: 32432
**Date**: 2023-10-26
**URL**: https://discourse.slicer.org/t/new-feature-thick-slab-reconstruction-from-slice-controllers-and-views/32432

---

## Post #1 by @Sam_Horvath (2023-10-26 19:33 UTC)

<p>Thick slab reconstruction (TSR) can now be enabled and modified from the slice controllers and slice views!</p>
<p>Enabling thick slab reconstruction as well as selection of the composite method (min, max, mean or sum) has been available through the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository/volumes.html#thick-slab-reconstruction-and-maximum-minimum-intensity-volume-projections">python console</a>.</p>
<p>Now these options are available through both the slice controller and the right-click context menu on the slice views.  If the interactive option is selected, the thickness, angle and position of the TSR can be adjusted by moving the slice intersections in the slice views.</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Slice Controller (Default)</th>
<th>Slice Controller (Slab Enabled)</th>
<th>Slice Controller (Slab Enabled + Interactive)</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://user-images.githubusercontent.com/219043/272957240-e337b309-b5de-4b3f-8460-36bf40cd9348.png"><img src="https://user-images.githubusercontent.com/219043/272957240-e337b309-b5de-4b3f-8460-36bf40cd9348.png" alt="image" width="656" height="472"></a></td>
<td><a href="https://user-images.githubusercontent.com/219043/272957380-f1aa5747-013a-4223-8436-5d8c6d3dac54.png"><img src="https://user-images.githubusercontent.com/219043/272957380-f1aa5747-013a-4223-8436-5d8c6d3dac54.png" alt="image" width="656" height="472"></a></td>
<td><a href="https://user-images.githubusercontent.com/219043/272957451-b3c06276-84ad-4077-9421-d5d8b4e7ea5d.png"><img src="https://user-images.githubusercontent.com/219043/272957451-b3c06276-84ad-4077-9421-d5d8b4e7ea5d.png" alt="image" width="656" height="472"></a></td>
</tr>
</tbody>
</table>
</div><div class="md-table">
<table>
<thead>
<tr>
<th>Slice Viewer (Handle Interaction )</th>
<th>Slice Viewer (Right-click context menu)</th>
<th>Slice Viewer (slice intersection &amp; Slab &amp; Interactive)</th>
<th>Slice Viewer (Red &amp; Yellow Slab enabled then Linked)</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://user-images.githubusercontent.com/219043/272957969-ae09aab3-e594-4c38-91fa-9159e32364fd.png"><img src="https://user-images.githubusercontent.com/219043/272957969-ae09aab3-e594-4c38-91fa-9159e32364fd.png" alt="image" width="690" height="279"></a></td>
<td><a href="https://user-images.githubusercontent.com/219043/272958224-f556d6a3-58aa-4359-abde-d2634fb16b1f.png"><img src="https://user-images.githubusercontent.com/219043/272958224-f556d6a3-58aa-4359-abde-d2634fb16b1f.png" alt="image" width="408" height="500"></a></td>
<td><a href="https://user-images.githubusercontent.com/219043/272959381-319133e2-d94a-4e61-8285-effa0f48ac3a.png"><img src="https://user-images.githubusercontent.com/219043/272959381-319133e2-d94a-4e61-8285-effa0f48ac3a.png" alt="image" width="690" height="370"></a></td>
<td><a href="https://user-images.githubusercontent.com/219043/272960311-2bbad97c-d7bb-4ee1-ba2e-47814886d5ac.png"><img src="https://user-images.githubusercontent.com/219043/272960311-2bbad97c-d7bb-4ee1-ba2e-47814886d5ac.png" alt="image" width="690" height="334"></a></td>
</tr>
</tbody>
</table>
</div><p>These features are currently available in the preview version of 3D Slicer.</p>
<p><a href="https://github.com/Slicer/Slicer/issues/6965">Issue 1</a>, <a href="https://github.com/Slicer/Slicer/pull/7021">PR 1</a> (slice controller implementation)<br>
<a href="https://github.com/Slicer/Slicer/issues/7083">Issue 2</a>, <a href="https://github.com/Slicer/Slicer/pull/7093">PR 2</a> (slice views implementation)</p>

---

## Post #2 by @Melodicpinpon (2024-02-16 12:25 UTC)

<p>This slice controller is a very good news!<br>
How can I use it?</p>

---

## Post #3 by @jcfr (2024-02-16 14:01 UTC)

<p>After installing Slicer, are you able to enable “Thick Slab Reconstruction” from the Slicer controller ?</p>

---

## Post #4 by @AlexZivelonghi (2024-07-17 11:06 UTC)

<p>Hello, this is a great feature. Is there a way to remove slabs before exporting a snapshot ? It would be really great, since some details can be hided from the slabs</p>

---

## Post #6 by @mohammed_alshakhas (2024-07-17 18:57 UTC)

<p>can i create a lateral cephalometry   from skull ct  with thick slab ?</p>

---

## Post #7 by @ZhsChen (2025-02-11 09:20 UTC)

<p>Hi, very useful tool! Thanks.<br>
However, the slab thickness seems to not work correctly on my data. As you can see in the capture below, the two red lines already cover the whole volume, but the MIP image in the Red view does not really show all vessels. If I increase the interval between the two red lines, more vessels will appear on the MIP image. Do you know why? And how to fix it?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/4/049ece1c35964d7a821b9abd78e4a0290cb6614d.jpeg" data-download-href="/uploads/short-url/ES9bYKTrnDrQm4eCBzJfsKq0qN.jpeg?dl=1" title="ThickSlabRecon-Thickness" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/049ece1c35964d7a821b9abd78e4a0290cb6614d_2_680x500.jpeg" alt="ThickSlabRecon-Thickness" data-base62-sha1="ES9bYKTrnDrQm4eCBzJfsKq0qN" width="680" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/049ece1c35964d7a821b9abd78e4a0290cb6614d_2_680x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/049ece1c35964d7a821b9abd78e4a0290cb6614d_2_1020x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/4/049ece1c35964d7a821b9abd78e4a0290cb6614d_2_1360x1000.jpeg 2x" data-dominant-color="494850"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">ThickSlabRecon-Thickness</span><span class="informations">1792×1317 122 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @pieper (2025-02-11 12:55 UTC)

<p><a class="mention" href="/u/zhschen">@ZhsChen</a> can you share the data or reproduce on public data?</p>

---

## Post #9 by @ZhsChen (2025-02-11 13:43 UTC)

<p>Hi Pieper, I just tried on the DZ-MR_1 data in the sample dataset CBCT-MR Head, same problem occurred. In the two captures below, the projection slabes both cover the whole head, but the MIP images are different.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1af0c17add38679fd3e4c84c976479e9bce3bbf.jpeg" data-download-href="/uploads/short-url/n4jUoWTS8aJqWpJmqPeMFrV91LN.jpeg?dl=1" title="thickness1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1af0c17add38679fd3e4c84c976479e9bce3bbf_2_690x422.jpeg" alt="thickness1" data-base62-sha1="n4jUoWTS8aJqWpJmqPeMFrV91LN" width="690" height="422" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1af0c17add38679fd3e4c84c976479e9bce3bbf_2_690x422.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1af0c17add38679fd3e4c84c976479e9bce3bbf_2_1035x633.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/1/a1af0c17add38679fd3e4c84c976479e9bce3bbf_2_1380x844.jpeg 2x" data-dominant-color="3B3A44"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">thickness1</span><span class="informations">1504×921 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b7403011f7668ee79e02d3e1fe40322d8d0da48.jpeg" data-download-href="/uploads/short-url/d320eDIhPspItsKl9JVb7QsQeKc.jpeg?dl=1" title="thickness2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b7403011f7668ee79e02d3e1fe40322d8d0da48_2_690x422.jpeg" alt="thickness2" data-base62-sha1="d320eDIhPspItsKl9JVb7QsQeKc" width="690" height="422" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b7403011f7668ee79e02d3e1fe40322d8d0da48_2_690x422.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b7403011f7668ee79e02d3e1fe40322d8d0da48_2_1035x633.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/b/5b7403011f7668ee79e02d3e1fe40322d8d0da48_2_1380x844.jpeg 2x" data-dominant-color="3C3B45"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">thickness2</span><span class="informations">1505×922 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #10 by @pieper (2025-02-11 14:14 UTC)

<p>Can you explain why you think the MIP is incorrect?</p>

---

## Post #11 by @ZhsChen (2025-02-11 14:31 UTC)

<p>In the two captures above, I expect the two MIPs (in the Red view) to be exactly the same, since in both images the projection slab covers the whole head (the region outside the head has zero or very low value, and will not be projected to the MIPs).</p>

---

## Post #12 by @ZhsChen (2025-02-11 14:35 UTC)

<p>But they are different. This suggests that the real slab used for projection is smaller than the slab between the two red lines.</p>

---

## Post #13 by @lassoan (2025-02-11 15:58 UTC)

<p>This is the code that sets up thick slab reslicing parameters:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L989-L1023">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L989-L1023" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L989-L1023" target="_blank" rel="noopener">Libs/MRML/Logic/vtkMRMLSliceLogic.cxx</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L989-L1023" rel="noopener"><code>05e03affb</code></a>
</div>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="989" style="counter-reset: li-counter 988 ;">
          <li>void vtkMRMLSliceLogic::UpdateReconstructionSlab(vtkMRMLSliceLogic* sliceLogic, vtkMRMLSliceLayerLogic* sliceLayerLogic)</li>
          <li>{</li>
          <li>  if (!sliceLogic || !sliceLayerLogic || !sliceLogic-&gt;GetSliceNode() || !sliceLayerLogic-&gt;GetSliceNode())</li>
          <li>  {</li>
          <li>    return;</li>
          <li>  }</li>
          <li></li>
          <li>  vtkImageReslice* reslice = sliceLayerLogic-&gt;GetReslice();</li>
          <li>  vtkMRMLSliceNode* sliceNode = sliceLayerLogic-&gt;GetSliceNode();</li>
          <li></li>
          <li>  double sliceSpacing;</li>
          <li>  if (sliceNode-&gt;GetSliceSpacingMode() == vtkMRMLSliceNode::PrescribedSliceSpacingMode)</li>
          <li>  {</li>
          <li>    sliceSpacing = sliceNode-&gt;GetPrescribedSliceSpacing()[2];</li>
          <li>  }</li>
          <li>  else</li>
          <li>  {</li>
          <li>    sliceSpacing = sliceLogic-&gt;GetLowestVolumeSliceSpacing()[2];</li>
          <li>  }</li>
          <li></li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L989-L1023" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Most likely the <code>slabNumberOfSlices</code> and <code>slabSliceSpacingFraction</code> computation has to be fixed.</p>

---

## Post #14 by @Antmaker (2026-04-17 23:18 UTC)

<p>I am able to replicate this behavior on Slicer v.5.10.0 on Linux and am trying to understand this behavior.</p>
<aside class="quote no-group" data-username="lassoan" data-post="13" data-topic="32432">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Most likely the <code>slabNumberOfSlices</code> and <code>slabSliceSpacingFraction</code> computation has to be fixed.</p>
</blockquote>
</aside>
<p>Due to my limited understanding of how 3D Slicer works, I am thinking this is more of my ignorance instead of anything needing fixing.</p>
<p>Could the masters point me in the right direction?</p>
<h3><a name="p-133251-use-case-1" class="anchor" href="#p-133251-use-case-1" aria-label="Heading link"></a>Use Case</h3>
<p>I have a masked scalar volume that I got by using the Mask Scalar Volume module. Now, I am trying to get the Max Intensity Projection (MIP) in coronal view.<br>
However, I am seeing the same behavior as <a href="https://discourse.slicer.org/t/new-feature-thick-slab-reconstruction-from-slice-controllers-and-views/32432/9" class="inline-onebox">New feature: Thick slab reconstruction from slice controllers and views - #9 by ZhsChen</a>.</p>
<h3><a name="p-133251-questions-2" class="anchor" href="#p-133251-questions-2" aria-label="Heading link"></a>Questions</h3>
<p>What is “prescribed slice spacing?” The <a href="https://apidocs.slicer.org/v5.8/classvtkMRMLSliceNode.html#a32489c34dc8daf5d61c8c536f3e5bd16" rel="noopener nofollow ugc">3D Slicer Documentation</a> nor Github source search revealed anything informative unfortunately.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1002">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1002" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1002" target="_blank" rel="noopener nofollow ugc">Libs/MRML/Logic/vtkMRMLSliceLogic.cxx</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1002" rel="noopener nofollow ugc"><code>05e03affb</code></a>
</div>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="992" style="counter-reset: li-counter 991 ;">
          <li>{</li>
          <li>  return;</li>
          <li>}</li>
          <li></li>
          <li>vtkImageReslice* reslice = sliceLayerLogic-&gt;GetReslice();</li>
          <li>vtkMRMLSliceNode* sliceNode = sliceLayerLogic-&gt;GetSliceNode();</li>
          <li></li>
          <li>double sliceSpacing;</li>
          <li>if (sliceNode-&gt;GetSliceSpacingMode() == vtkMRMLSliceNode::PrescribedSliceSpacingMode)</li>
          <li>{</li>
          <li class="selected">  sliceSpacing = sliceNode-&gt;GetPrescribedSliceSpacing()[2];</li>
          <li>}</li>
          <li>else</li>
          <li>{</li>
          <li>  sliceSpacing = sliceLogic-&gt;GetLowestVolumeSliceSpacing()[2];</li>
          <li>}</li>
          <li></li>
          <li>int slabNumberOfSlices = 1;</li>
          <li>if (sliceNode-&gt;GetSlabReconstructionEnabled()</li>
          <li>    &amp;&amp; sliceSpacing &gt; 0</li>
          <li>    &amp;&amp; sliceNode-&gt;GetSlabReconstructionThickness() &gt; sliceSpacing</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The “slice spacing” the getter is getting is the thickness of each slice, thus it is the diff of the mm change as I scroll through the slice viewports.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1006">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1006" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1006" target="_blank" rel="noopener nofollow ugc">Libs/MRML/Logic/vtkMRMLSliceLogic.cxx</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1006" rel="noopener nofollow ugc"><code>05e03affb</code></a>
</div>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="996" style="counter-reset: li-counter 995 ;">
          <li>vtkImageReslice* reslice = sliceLayerLogic-&gt;GetReslice();</li>
          <li>vtkMRMLSliceNode* sliceNode = sliceLayerLogic-&gt;GetSliceNode();</li>
          <li></li>
          <li>double sliceSpacing;</li>
          <li>if (sliceNode-&gt;GetSliceSpacingMode() == vtkMRMLSliceNode::PrescribedSliceSpacingMode)</li>
          <li>{</li>
          <li>  sliceSpacing = sliceNode-&gt;GetPrescribedSliceSpacing()[2];</li>
          <li>}</li>
          <li>else</li>
          <li>{</li>
          <li class="selected">  sliceSpacing = sliceLogic-&gt;GetLowestVolumeSliceSpacing()[2];</li>
          <li>}</li>
          <li></li>
          <li>int slabNumberOfSlices = 1;</li>
          <li>if (sliceNode-&gt;GetSlabReconstructionEnabled()</li>
          <li>    &amp;&amp; sliceSpacing &gt; 0</li>
          <li>    &amp;&amp; sliceNode-&gt;GetSlabReconstructionThickness() &gt; sliceSpacing</li>
          <li>    )</li>
          <li>{</li>
          <li>  slabNumberOfSlices = static_cast&lt;int&gt;(sliceNode-&gt;GetSlabReconstructionThickness() / sliceSpacing);</li>
          <li>}</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The <code>SlabReconstructionOversamplingFactor</code> is something similar to “Oversampling factor” under Segmentation geometry of the Segment Editor module? <a href="https://apidocs.slicer.org/v5.8/classvtkMRMLSliceNode.html#af660d323ab57ce22ea8ffdf3554e921e" rel="noopener nofollow ugc">3D Slicer Documentation</a> also did not specify what this attribute that the getter is getting mean.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1021">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1021" target="_blank" rel="noopener nofollow ugc">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1021" target="_blank" rel="noopener nofollow ugc">Libs/MRML/Logic/vtkMRMLSliceLogic.cxx</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/05e03affb0c0eebde451d452c36fb2d84a5828f6/Libs/MRML/Logic/vtkMRMLSliceLogic.cxx#L1021" rel="noopener nofollow ugc"><code>05e03affb</code></a>
</div>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="1011" style="counter-reset: li-counter 1010 ;">
          <li>      &amp;&amp; sliceSpacing &gt; 0</li>
          <li>      &amp;&amp; sliceNode-&gt;GetSlabReconstructionThickness() &gt; sliceSpacing</li>
          <li>      )</li>
          <li>  {</li>
          <li>    slabNumberOfSlices = static_cast&lt;int&gt;(sliceNode-&gt;GetSlabReconstructionThickness() / sliceSpacing);</li>
          <li>  }</li>
          <li>  reslice-&gt;SetSlabNumberOfSlices(slabNumberOfSlices);</li>
          <li></li>
          <li>  reslice-&gt;SetSlabMode(sliceNode-&gt;GetSlabReconstructionType());</li>
          <li></li>
          <li class="selected">  double slabSliceSpacingFraction = sliceSpacing / sliceNode-&gt;GetSlabReconstructionOversamplingFactor();</li>
          <li>  reslice-&gt;SetSlabSliceSpacingFraction(slabSliceSpacingFraction);</li>
          <li>}</li>
          <li></li>
          <li>//----------------------------------------------------------------------------</li>
          <li>void vtkMRMLSliceLogic::UpdatePipeline()</li>
          <li>{</li>
          <li>  int modified = 0;</li>
          <li>  if ( this-&gt;SliceCompositeNode )</li>
          <li>  {</li>
          <li>    // get the background and foreground image data from the layers</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
