# Segment editor outline color and thickness customization

**Topic ID**: 11427
**Date**: 2020-05-05
**URL**: https://discourse.slicer.org/t/segment-editor-outline-color-and-thickness-customization/11427

---

## Post #1 by @muratmaga (2020-05-05 22:35 UTC)

<p>Is there a way to change the default segment outlining color from yellow to something else in the segment editor (and/or edit the line thickness) that we can embed in .slicerrc.py? We are working on images that has a very light background, and yellow outline doesn’t stand out much…</p>

---

## Post #2 by @lassoan (2020-05-05 22:59 UTC)

<p>If by “outlining color” you mean preview color in paint and scissors:</p>
<p>If you work with grayscale images then by slightly adjusting their window/level should make the bright yellow color pop out very nicely.</p>
<p>If you have a fast computer then you can also disable <code>delayedPaint</code> property of qSlicerSegmentEditorPaintEffect - then there is no preview but you paint directly with the segment color.</p>
<p>If you want to make the color adjustable then you can send a pull request that adds get/set method for the color in qSlicerSegmentEditorPaintEffect.cxx and qSlicerSegmentEditorScissorsEffect.cxx.</p>

---

## Post #3 by @cpinter (2020-05-06 08:38 UTC)

<p>I believe that to achieve what you want, these hardcoded values need to be made a property in the effect:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLevelTracingEffect.py#L138" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLevelTracingEffect.py#L138" target="_blank">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLevelTracingEffect.py#L138</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="128" style="counter-reset: li-counter 127 ;">
<li>  self.xyPoints = vtk.vtkPoints()</li>
<li>  self.rasPoints = vtk.vtkPoints()</li>
<li>  self.polyData = vtk.vtkPolyData()</li>
<li>
</li>
<li>  self.tracingFilter = vtkITK.vtkITKLevelTracingImageFilter()</li>
<li>  self.ijkToXY = vtk.vtkGeneralTransform()</li>
<li>
</li>
<li>  self.mapper = vtk.vtkPolyDataMapper2D()</li>
<li>  self.actor = vtk.vtkActor2D()</li>
<li>  actorProperty = self.actor.GetProperty()</li>
<li class="selected">  actorProperty.SetColor( 107/255., 190/255., 99/255. )</li>
<li>  actorProperty.SetLineWidth( 1 )</li>
<li>  self.mapper.SetInputData(self.polyData)</li>
<li>  self.actor.SetMapper(self.mapper)</li>
<li>  actorProperty = self.actor.GetProperty()</li>
<li>  actorProperty.SetColor(1,1,0)</li>
<li>  actorProperty.SetLineWidth(1)</li>
<li>
</li>
<li>def preview(self,xy):</li>
<li>  # Calculate the current level trace view if the mouse is inside the volume extent</li>
<li>
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #4 by @gcsharp (2020-06-02 16:48 UTC)

<p>Is there a way to increase the thickness of a segmentation itself (not the effect)?</p>

---

## Post #5 by @lassoan (2020-06-02 17:08 UTC)

<p>You can customize all these in Segmentations module’s display section.</p>

---

## Post #6 by @gcsharp (2020-06-03 15:14 UTC)

<p>Thanks!  I missed the hidden “Advanced” options.</p>

---
