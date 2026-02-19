---
topic_id: 35120
title: "How To Pick A Point In Volume Rendering"
date: 2024-03-27
url: https://discourse.slicer.org/t/35120
---

# How to pick a point in volume rendering?

**Topic ID**: 35120
**Date**: 2024-03-27
**URL**: https://discourse.slicer.org/t/how-to-pick-a-point-in-volume-rendering/35120

---

## Post #1 by @zhang-qiang-github (2024-03-27 08:48 UTC)

<p>In 3D slicer, 3D visualization used the volume rendering. And 3D slicer can pick a point from volume rendering. For example:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/c/6c2ba3cf175f64a8da03a03298aecaafadbdc3c3.jpeg" alt="image" data-base62-sha1="fqV419O8zVEJHTayqwfwtCMlCq7" width="653" height="436"></p>
<p>Is <code>vtkPropPicker</code> or <code>vtkCellPicker</code> userd? I can not pick a 3D point from volume rendering.</p>
<p>Any suggestion is appreciated~~~</p>

---

## Post #2 by @cpinter (2024-04-01 12:24 UTC)

<p>I’d probably try starting from this code:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/3903a95c38730e522630569b114825dd0d7c9532/Libs/MRML/DisplayableManager/vtkMRMLThreeDViewInteractorStyle.cxx#L170-L183">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/3903a95c38730e522630569b114825dd0d7c9532/Libs/MRML/DisplayableManager/vtkMRMLThreeDViewInteractorStyle.cxx#L170-L183" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/3903a95c38730e522630569b114825dd0d7c9532/Libs/MRML/DisplayableManager/vtkMRMLThreeDViewInteractorStyle.cxx#L170-L183" target="_blank" rel="noopener">Slicer/Slicer/blob/3903a95c38730e522630569b114825dd0d7c9532/Libs/MRML/DisplayableManager/vtkMRMLThreeDViewInteractorStyle.cxx#L170-L183</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="170" style="counter-reset: li-counter 169 ;">
          <li>//---------------------------------------------------------------------------</li>
          <li>bool vtkMRMLThreeDViewInteractorStyle::QuickPick(int x, int y, double pickPoint[3])</li>
          <li>{</li>
          <li>  vtkRenderer* pokedRenderer = this-&gt;GetInteractor()-&gt;FindPokedRenderer(x, y);</li>
          <li>  vtkInteractorStyle* interactorStyle = vtkInteractorStyle::SafeDownCast(this-&gt;GetInteractor()-&gt;GetInteractorStyle());</li>
          <li>  interactorStyle-&gt;SetCurrentRenderer(pokedRenderer);</li>
          <li>  if (pokedRenderer == nullptr)</li>
          <li>  {</li>
          <li>    vtkDebugMacro("Pick: couldn't find the poked renderer at event position " &lt;&lt; x &lt;&lt; ", " &lt;&lt; y);</li>
          <li>    return false;</li>
          <li>  }</li>
          <li></li>
          <li>  bool quickPicked = (this-&gt;QuickPicker-&gt;Pick(x, y, 0, pokedRenderer) &gt; 0);</li>
          <li>  this-&gt;QuickPicker-&gt;GetPickPosition(pickPoint);</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
