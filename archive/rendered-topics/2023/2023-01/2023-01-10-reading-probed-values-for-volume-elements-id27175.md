---
topic_id: 27175
title: "Reading Probed Values For Volume Elements"
date: 2023-01-10
url: https://discourse.slicer.org/t/27175
---

# Reading probed values for volume elements

**Topic ID**: 27175
**Date**: 2023-01-10
**URL**: https://discourse.slicer.org/t/reading-probed-values-for-volume-elements/27175

---

## Post #1 by @ZSoltani (2023-01-10 18:59 UTC)

<p>HI ALL,</p>
<p>After using Probe volume with model, is there any way that I can export the HU values of the elements in a readable format? I need them for FE analysis.</p>
<p>p.s. I can see that slicer.util.array() can be used for reading values on each slice, but I’m not sure about how to read the values for the volume elements.</p>
<p>Thank you,</p>
<p>Zahra</p>

---

## Post #2 by @pieper (2023-01-10 22:09 UTC)

<p>I’m not sure what format the FE analysis requires, but you should be able to access the per-vertex values with something like <code>arrayFromModelPointData(n, "NRRDImage")</code> where n is your model node and NRRDImage is your array name from Probe Volume with Model.  Then you can write it out in whatever format you need.</p>

---

## Post #3 by @ZSoltani (2023-01-11 18:17 UTC)

<p>Thank you Steve for your reply. Yes, then I can use the nodal values to calculate the values at integration points that I will need in FE analysis.</p>
<p>For completeness of our FE, is the source code for Probe volume with model available, so that I can look at the algorithm for calculating the nodal values?</p>
<p>Thanks,</p>
<p>Zahra</p>

---

## Post #4 by @mau_igna_06 (2023-01-11 18:24 UTC)

<p>Please have a look here:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/ProbeVolumeWithModel/ProbeVolumeWithModel.cxx">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/ProbeVolumeWithModel/ProbeVolumeWithModel.cxx" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/ProbeVolumeWithModel/ProbeVolumeWithModel.cxx" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/main/Modules/CLI/ProbeVolumeWithModel/ProbeVolumeWithModel.cxx</a></h4>


      <pre><code class="lang-cxx">
#include "ProbeVolumeWithModelCLP.h"

// vtkTeem includes
#include &lt;vtkTeemNRRDReader.h&gt;

// VTK includes
#include &lt;vtkImageData.h&gt;
#include &lt;vtkNew.h&gt;
#include &lt;vtkPolyData.h&gt;
#include &lt;vtkProbeFilter.h&gt;
#include &lt;vtkTransform.h&gt;
#include &lt;vtkTransformFilter.h&gt;
#include &lt;vtkImageChangeInformation.h&gt;

#include "vtkMRMLModelNode.h"
#include "vtkMRMLModelStorageNode.h"

#include &lt;vtksys/SystemTools.hxx&gt;

</code></pre>



  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/main/Modules/CLI/ProbeVolumeWithModel/ProbeVolumeWithModel.cxx" target="_blank" rel="noopener nofollow ugc">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @ZSoltani (2023-01-11 18:28 UTC)

<p>Thank you Mauro.</p>
<p>Zahra</p>

---
