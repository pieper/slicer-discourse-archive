---
topic_id: 16443
title: "Change Speed For Rock 3D"
date: 2021-03-09
url: https://discourse.slicer.org/t/16443
---

# Change speed for Rock 3D?

**Topic ID**: 16443
**Date**: 2021-03-09
**URL**: https://discourse.slicer.org/t/change-speed-for-rock-3d/16443

---

## Post #1 by @hherhold (2021-03-09 01:48 UTC)

<p>Is there a way in Python to specify/change the speed for the Rock 3D view? I’ve found where to change the increment and length (little fuzzy on what increment does…) but I haven’t found a way to change how quickly it rotates. Is this possible?</p>
<p>Thanks!</p>

---

## Post #2 by @lassoan (2021-03-09 02:03 UTC)

<p>These are all the variables that control speed and range of rock and spin:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/CTK/blob/9a9573ec4e0653ee96fe02823ac7ee66b40d3b44/Libs/Visualization/VTK/Widgets/ctkVTKRenderView.h#L39..L49" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/9a9573ec4e0653ee96fe02823ac7ee66b40d3b44/Libs/Visualization/VTK/Widgets/ctkVTKRenderView.h#L39..L49" target="_blank" rel="noopener">commontk/CTK/blob/9a9573ec4e0653ee96fe02823ac7ee66b40d3b44/Libs/Visualization/VTK/Widgets/ctkVTKRenderView.h#L39..L49</a></h4>
<pre class="onebox"><code class="lang-h"><ol class="start lines" start="29" style="counter-reset: li-counter 28 ;">
<li>class vtkCamera;</li>
<li>class vtkRenderer;</li>
<li>
<li>/// \ingroup Visualization_VTK_Widgets</li>
<li>class CTK_VISUALIZATION_VTK_WIDGETS_EXPORT ctkVTKRenderView : public ctkVTKAbstractView</li>
<li>{</li>
<li>  Q_OBJECT</li>
<li>  Q_PROPERTY(bool orientationWidgetVisible READ orientationWidgetVisible</li>
<li>             WRITE setOrientationWidgetVisible)</li>
<li>  Q_PROPERTY(double zoomFactor READ zoomFactor WRITE setZoomFactor)</li>
<li class="selected">  Q_PROPERTY(double pitchRollYawIncrement READ pitchRollYawIncrement WRITE setPitchRollYawIncrement)</li>
<li>  Q_ENUMS(RotateDirection)</li>
<li>  Q_PROPERTY(RotateDirection pitchDirection READ pitchDirection WRITE setPitchDirection)</li>
<li>  Q_PROPERTY(RotateDirection rollDirection READ rollDirection WRITE setRollDirection)</li>
<li>  Q_PROPERTY(RotateDirection yawDirection READ yawDirection WRITE setYawDirection)</li>
<li>  Q_PROPERTY(RotateDirection spinDirection READ spinDirection WRITE setSpinDirection)</li>
<li>  Q_PROPERTY(bool spinEnabled READ spinEnabled WRITE setSpinEnabled)</li>
<li>  Q_PROPERTY(double spinIncrement READ spinIncrement WRITE setSpinIncrement)</li>
<li>  Q_PROPERTY(int animationIntervalMs READ animationIntervalMs WRITE setAnimationIntervalMs)</li>
<li>  Q_PROPERTY(bool rockEnabled READ rockEnabled WRITE setRockEnabled)</li>
<li>  Q_PROPERTY(int rockLength READ rockLength WRITE setRockLength)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>If you find these insufficient then have a look at the implementation in the cpp file and suggest what else should be made configurable.</p>

---

## Post #3 by @hherhold (2021-03-09 14:19 UTC)

<p><code>animationIntervalMs</code> is what I was looking for.</p>
<p>THANKS!</p>

---
