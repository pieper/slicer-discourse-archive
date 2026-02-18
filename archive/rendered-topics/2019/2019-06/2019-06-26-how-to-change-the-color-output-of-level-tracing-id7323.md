# How to change the color output of Level tracing

**Topic ID**: 7323
**Date**: 2019-06-26
**URL**: https://discourse.slicer.org/t/how-to-change-the-color-output-of-level-tracing/7323

---

## Post #1 by @steve01 (2019-06-26 21:48 UTC)

<p>Operating system: Mac OS El Capitan 10.11.6<br>
Slicer version: 4.10.2 r28257<br>
expected behavior:<br>
Actual behavior:<br>
I would like to change the color output of Level tracing. I do not know how to program. Is there a way of doing this?</p>

---

## Post #2 by @lassoan (2019-06-27 04:07 UTC)

<p>Could you please attach a screenshot and show there what color you would like to change?</p>

---

## Post #3 by @steve01 (2019-06-27 15:25 UTC)

<p>Hello Andras,</p>
<p>Please see attachment.  The color is currently green. I don’t have any specific color I would like to change it to, I would just like to learn how to change it.</p>
<p>Thank you</p>

---

## Post #4 by @cpinter (2019-06-27 15:42 UTC)

<p>I think it’s hard-coded currently. Here’s what you need to change if you want a different color:<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLevelTracingEffect.py#L143" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLevelTracingEffect.py#L143" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorLevelTracingEffect.py#L143</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="133" style="counter-reset: li-counter 132 ;">
<li>  self.ijkToXY = vtk.vtkGeneralTransform()</li>
<li>
</li>
<li>  self.mapper = vtk.vtkPolyDataMapper2D()</li>
<li>  self.actor = vtk.vtkActor2D()</li>
<li>  actorProperty = self.actor.GetProperty()</li>
<li>  actorProperty.SetColor( 107/255., 190/255., 99/255. )</li>
<li>  actorProperty.SetLineWidth( 1 )</li>
<li>  self.mapper.SetInputData(self.polyData)</li>
<li>  self.actor.SetMapper(self.mapper)</li>
<li>  actorProperty = self.actor.GetProperty()</li>
<li class="selected">  actorProperty.SetColor(1,1,0)</li>
<li>  actorProperty.SetLineWidth(1)</li>
<li>
</li>
<li>def preview(self,xy):</li>
<li>  # Calculate the current level trace view if the mouse is inside the volume extent</li>
<li>
</li>
<li>  # Get master volume image data</li>
<li>  import vtkSegmentationCorePython as vtkSegmentationCore</li>
<li>  masterImageData = self.effect.scriptedEffect.masterVolumeImageData()</li>
<li>
</li>
<li>  self.xyPoints.Reset()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>
<p>You can find this file in the installed folder: [SlicerInstallFolder]\Slicer 4.11.0-2019-MM-DD\lib\Slicer-4.11\qt-scripted-modules\SegmentEditorEffects\SegmentEditorLevelTracingEffect.py</p>

---

## Post #5 by @steve01 (2019-06-27 16:03 UTC)

<p>Is there a list somewhere that shows what colors correspond to the code?</p>

---

## Post #6 by @cpinter (2019-06-27 16:24 UTC)

<p>You can use Google’s color picker by typing “color picker” into google search. If you set the values (multiplied by 255) in the rgb fields then you get the color. Or use any other color picker of your choice.</p>

---

## Post #7 by @steve01 (2019-06-27 16:36 UTC)

<p>I will look into it. Are the rgb fields the areas separated by commas?<br>
sorry really don’t know how to program.</p>

---
