---
topic_id: 40185
title: "How Does Create Closed Surface Representation Work"
date: 2024-11-13
url: https://discourse.slicer.org/t/40185
---

# How does create closed surface representation work ?

**Topic ID**: 40185
**Date**: 2024-11-13
**URL**: https://discourse.slicer.org/t/how-does-create-closed-surface-representation-work/40185

---

## Post #1 by @Fleur_Gaudfernau (2024-11-13 21:55 UTC)

<p>Hello,<br>
I could not find any answer to this rather simple question online.<br>
I’m trying different methods for extracting meshes from brain segmentations.<br>
I’ve tried several times the Marching Cube algorithm and the results are always ugly. However, the “export closed surface representation” in 3D slicer works very well.<br>
I would like to include this function into a data preprocessing pipeline.<br>
I understand that some smoothing of the segmentation is involved, but I can’t find the code behind this functionality or at least the name of the algorithm.<br>
Any help would be appreciated.<br>
Thanks<br>
Fleur</p>

---

## Post #2 by @cpinter (2024-11-14 12:08 UTC)

<p>Actually this has been discussed various times on the forum. Unfortunately the search function is extremely bad. Maybe try a bit more, but here’s a basic answer:</p>
<p>The conversion is part of a multi-representation mechanism, which is described in this paper and thesis:<br>
<a href="https://labs.cs.queensu.ca/perklab/wp-content/uploads/sites/3/2024/02/Pinter2019_Manuscript.pdf">Manuscript of the paper</a><br>
<a href="https://qspace.library.queensu.ca/handle/1974/26422">Thesis</a><br>
The actual algorithm changed a bit in the sense that an alternative filter, the relatively new surface nets method has been added. But the default algorithm is the same as what is described in these sources.</p>
<p>You say you couldn’t find the code, so I assume that would help as well:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx#L246">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx#L246" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx#L246" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Libs/vtkSegmentationCore/vtkBinaryLabelmapToClosedSurfaceConversionRule.cxx#L246</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="236" style="counter-reset: li-counter 235 ;">
          <li>  vtkPointData* pointData = closedSurfacePolyData-&gt;GetPointData();</li>
          <li>  if (pointData!=nullptr)</li>
          <li>  {</li>
          <li>    pointData-&gt;RemoveArray("ImageScalars");</li>
          <li>  }</li>
          <li></li>
          <li>  return true;</li>
          <li>}</li>
          <li></li>
          <li>//----------------------------------------------------------------------------</li>
          <li class="selected">bool vtkBinaryLabelmapToClosedSurfaceConversionRule::CreateClosedSurface(vtkOrientedImageData* orientedBinaryLabelmap,</li>
          <li>  vtkPolyData* closedSurfacePolyData, std::vector&lt;int&gt; labelValues)</li>
          <li>{</li>
          <li>  if (!closedSurfacePolyData)</li>
          <li>  {</li>
          <li>    vtkErrorMacro("Convert: Target representation is not poly data");</li>
          <li>    return false;</li>
          <li>  }</li>
          <li></li>
          <li>  // Check validity of source and target representation objects</li>
          <li>  if (!orientedBinaryLabelmap)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Fleur_Gaudfernau (2024-11-14 13:39 UTC)

<p>Thanks a lot !<br>
Do you know if there is a python version of this code ? At least for the default algorithm (flying edges) ?</p>

---

## Post #4 by @cpinter (2024-11-14 13:53 UTC)

<p>There is no Python version. But it is extremely simple to port to Python. However, I suggest using the infrastructure of Slicer. It has been an immense task to make everything work correctly, so although it may seem easy, you could find yourself in a difficult situation if you start reimplementing it from scratch.</p>

---
