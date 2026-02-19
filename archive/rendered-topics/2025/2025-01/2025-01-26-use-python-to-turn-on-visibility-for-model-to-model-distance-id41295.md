---
topic_id: 41295
title: "Use Python To Turn On Visibility For Model To Model Distance"
date: 2025-01-26
url: https://discourse.slicer.org/t/41295
---

# Use python to turn on visibility for model to model distance scalars and color bars

**Topic ID**: 41295
**Date**: 2025-01-26
**URL**: https://discourse.slicer.org/t/use-python-to-turn-on-visibility-for-model-to-model-distance-scalars-and-color-bars/41295

---

## Post #1 by @evaherbst (2025-01-26 19:30 UTC)

<p>Hello,</p>
<p>I am called the ModeltoModel distance module in Slicer with Python to batch run the distance calculations of several pairs of models.</p>
<p>Is there a way in Python automatically turn on visibility of the scalars from the model-to-model distance and also the heat map bars?</p>
<p>Thank you!</p>

---

## Post #2 by @cpinter (2025-01-29 11:17 UTC)

<p>You need to get the display node of the model node and apply the settings you want on the display node. For example for turning on scalar visibility you can call this function:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLDisplayNode.h#L393">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLDisplayNode.h#L393" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLDisplayNode.h#L393" target="_blank" rel="noopener">Libs/MRML/Core/vtkMRMLDisplayNode.h</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/main/Libs/MRML/Core/vtkMRMLDisplayNode.h#L393" rel="noopener"><code>main</code></a>
</div>



    <pre class="onebox"><code class="lang-h">
      <ol class="start lines" start="383" style="counter-reset: li-counter 382 ;">
          <li>/// Set the shading mode (None, Gouraud, Flat) of the display node.</li>
          <li>/// \sa Shading, GetShading()</li>
          <li>vtkSetMacro(Shading, int);</li>
          <li>/// Get the shading of the display node.</li>
          <li>/// \sa Shading, SetShading()</li>
          <li>vtkGetMacro(Shading, int);</li>
          <li></li>
          <li>/// Set the scalar visibility of the display node.</li>
          <li>/// \sa ScalarVisibility, GetScalarVisibility(), ScalarVisibilityOn(),</li>
          <li>/// ScalarVisibilityOff()</li>
          <li class="selected">vtkSetMacro(ScalarVisibility, int);</li>
          <li>/// Get the scalar visibility of the display node.</li>
          <li>/// \sa ScalarVisibility, SetScalarVisibility(), ScalarVisibilityOn(),</li>
          <li>/// ScalarVisibilityOff()</li>
          <li>vtkGetMacro(ScalarVisibility, int);</li>
          <li>/// Set the scalar visibility of the display node.</li>
          <li>/// \sa ScalarVisibility, SetScalarVisibility(), GetScalarVisibility</li>
          <li>vtkBooleanMacro(ScalarVisibility, int);</li>
          <li></li>
          <li>/// Set the vector visibility of the display node.</li>
          <li>/// \sa VectorVisibility, GetVectorVisibility(), VectorVisibilityOn(),</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>This snippet is for showing scalar bar for volumes. I don’t know if this works for model scalars, but I’d start here<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-color-legend-for-a-volume-node" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-color-legend-for-a-volume-node</a></p>

---

## Post #3 by @evaherbst (2025-02-11 09:34 UTC)

<p>Thank you very much! I will test this</p>

---
