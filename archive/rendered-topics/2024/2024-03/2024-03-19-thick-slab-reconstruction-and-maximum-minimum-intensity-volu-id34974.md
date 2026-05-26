---
topic_id: 34974
title: "Thick slab reconstruction and maximum/minimum intensity volume projections"
date: 2024-03-19
url: https://discourse.slicer.org/t/34974
last_bumped: 2026-04-15T03:23:35.544Z
---

# Thick slab reconstruction and maximum/minimum intensity volume projections

**Topic ID**: 34974
**Date**: 2024-03-19
**URL**: https://discourse.slicer.org/t/thick-slab-reconstruction-and-maximum-minimum-intensity-volume-projections/34974

---

## Post #1 by @ddii (2024-03-19 13:35 UTC)

<p>How do you change the slice thickness?</p>
<h3><a name="p-108430-thick-slab-reconstruction-and-maximumminimum-intensity-volume-projections-1" class="anchor" href="#p-108430-thick-slab-reconstruction-and-maximumminimum-intensity-volume-projections-1" aria-label="Heading link"></a>Thick slab reconstruction and maximum/minimum intensity volume projections</h3>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#thick-slab-reconstruction-and-maximum-minimum-intensity-volume-projections">
  <header class="source">

      <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#thick-slab-reconstruction-and-maximum-minimum-intensity-volume-projections" target="_blank" rel="noopener nofollow ugc">slicer.readthedocs.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#thick-slab-reconstruction-and-maximum-minimum-intensity-volume-projections" target="_blank" rel="noopener nofollow ugc">Script repository — 3D Slicer  documentation</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This way does not work anymore…</p>

---

## Post #2 by @Antmaker (2026-04-15 01:07 UTC)

<p>I was trying to understand Slab Reconstruction by following <a href="https://discourse.slicer.org/t/new-feature-thick-slab-reconstruction-from-slice-controllers-and-views/32432">New feature: Thick slab reconstruction from slice controllers and views</a> and the code snipper provided above. I am not sure how to proceed as I am still learning the ins and outs of 3D Slicer. Below are what I tried and found.</p>
<h2><a name="p-133194-reproducing-the-code-snippet-1" class="anchor" href="#p-133194-reproducing-the-code-snippet-1" aria-label="Heading link"></a>Reproducing the Code Snippet</h2>
<p>The code snippet from the script repository doesn’t work for me either. The thickness value (top right corner of axis view) nor the spacings between the two red lines (in the coronal and sagittal views) change.</p>
<p>When checking the SlabNumberOfSlices and SlabSliceSpacingFraction using <code>reslice.GetSlabNumberOfSlices()</code> and <code>reslice.GetSlabSliceSpacingFraction()</code>, the previous set values have reverted back to the original values.</p>
<pre><code class="lang-auto">

&gt;&gt;&gt; # Code snippet from script respository
&gt;&gt;&gt; sliceNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNodeRed")
&gt;&gt;&gt; appLogic = slicer.app.applicationLogic()
&gt;&gt;&gt; sliceLogic = appLogic.GetSliceLogic(sliceNode)
&gt;&gt;&gt; sliceLayerLogic = sliceLogic.GetBackgroundLayer()
&gt;&gt;&gt; reslice = sliceLayerLogic.GetReslice()
&gt;&gt;&gt; reslice.SetSlabModeToMean()
&gt;&gt;&gt; reslice.GetSlabNumberOfSlices()          # PRE - checking
1
&gt;&gt;&gt; reslice.GetSlabSliceSpacingFraction()    # PRE - checking
0.30000001192093007
&gt;&gt;&gt; reslice.SetSlabNumberOfSlices(10)        # mean of 10 slices will computed
&gt;&gt;&gt; reslice.SetSlabSliceSpacingFraction(0.3) # spacing between each slice is 0.3 pixel (total 10 * 0.3 = 3 pixel neighborhood)
&gt;&gt;&gt; 
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; reslice.GetSlabNumberOfSlices()          # POST - checking to make sure the property changed
10
&gt;&gt;&gt; reslice.GetSlabSliceSpacingFraction()    # POST - checking to make sure the property changed
0.3
&gt;&gt;&gt; sliceNode.Modified()
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt;
&gt;&gt;&gt; reslice.GetSlabNumberOfSlices()          # Reverted back after running Modified()
1
&gt;&gt;&gt; reslice.GetSlabSliceSpacingFraction()    #  Reverted back after running Modified()
0.30000001192093007
</code></pre>
<h2><a name="p-133194-what-kind-of-worked-2" class="anchor" href="#p-133194-what-kind-of-worked-2" aria-label="Heading link"></a>What Kind of Worked</h2>
<p>However, this code snippet below worked and I can see the thickness value (top-right of axis view) and the spacing between the two red lines increase.</p>
<pre><code class="lang-auto">&gt;&gt;&gt; sliceNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSliceNodeRed")
&gt;&gt;&gt; sliceNode.SetSlabReconstructionType(slicer.vtkMRMLSliceNode().GetSlabReconstructionType())
&gt;&gt;&gt; sliceNode.SetSlabReconstructionThickness(10)
&gt;&gt;&gt; sliceNode.GetSlabReconstructionThickness() 
10.0
</code></pre>
<h2><a name="p-133194-troubleshooting-attempts-3" class="anchor" href="#p-133194-troubleshooting-attempts-3" aria-label="Heading link"></a>Troubleshooting Attempts</h2>
<ul>
<li>3D Slicer uses MVC architecture pattern (<a href="https://www.robarts.ca/computerassistedsurgery/3d_slicer_architecture/index.html" rel="noopener nofollow ugc">src</a>) and the code snippet was changing the logic (controller) and the viewer is not updated. Thus, I have tried running <code>reslice.Update()</code>, and <code>reslice.update()</code> but the view did not update.</li>
<li>I tried looking into the API documentation but cannot find any information on the update methods for <code>vtkmodules.vtkImagingCore.vtkImageReslice</code> objects.</li>
<li>Thus, I looked into the Doxygen-style documentation and found <code>void vtkMRMLSliceLogic::UpdateSliceNode</code> but am not sure how to call it from the Python API.</li>
<li>I tried digging further into <a href="https://discourse.slicer.org/t/new-feature-thick-slab-reconstruction-from-slice-controllers-and-views/32432">this thread</a> but it neither helped me understand how the Slab Reconstruction works nor provided any hints to where to find the Python API.</li>
</ul>
<h2><a name="p-133194-environment-4" class="anchor" href="#p-133194-environment-4" aria-label="Heading link"></a>Environment</h2>
<pre><code class="lang-auto"># `sw_vers` output
ProductName:            macOS
ProductVersion:         26.4.1
BuildVersion:           25E253

# `Slicer --version` output
Slicer 5.10.0
</code></pre>

---

## Post #3 by @Antmaker (2026-04-15 03:23 UTC)

<p><a class="mention" href="/u/ddii">@ddii</a> is correct that the example no longer works. The reason and solution are laid out in <a href="https://discourse.slicer.org/t/2d-mip-maximum-intensity-projection-not-works-in-slicer-5-6-1/36272">2D MIP (maximum intensity projection) not works in Slicer 5.6.1</a>.</p>

---
