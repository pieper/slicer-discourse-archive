---
topic_id: 12273
title: "Alter Number Of Points Which Makes Up Vtk Curve"
date: 2020-06-29
url: https://discourse.slicer.org/t/12273
---

# Alter number of points which makes up VTK curve

**Topic ID**: 12273
**Date**: 2020-06-29
**URL**: https://discourse.slicer.org/t/alter-number-of-points-which-makes-up-vtk-curve/12273

---

## Post #1 by @mjg (2020-06-29 15:54 UTC)

<p>Hello,</p>
<p>Is there some way to take an existing Slicer VTK curve node, say it is defined by 4 initial points I have placed, and increase the number of points along the curve to be a number such as 100, such that the curve shape remains the same, but now there are 100 points defining the shape?</p>
<p>If there is no built-in VTK method for such functionalities, is there a method by which I could find the curve equation and then add points manually along the curve?</p>
<p>Thank you!</p>

---

## Post #2 by @muratmaga (2020-06-29 16:15 UTC)

<p>Resample curves within the Markups tool does exactly that. Perhaps <a class="mention" href="/u/smrolfe">@smrolfe</a> can point out to the specific code.</p>

---

## Post #3 by @smrolfe (2020-06-29 17:00 UTC)

<p>Yes, you can find the code to do this, with the option to constrain to a surface,<br>
in the onApplyCurveResamplingPushButton call back here:<br>
</p><aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/c36f2d0a4e585c84f91546e3710cc9ef9444201b/Modules/Loadable/Markups/qSlicerMarkupsModuleWidget.cxx#L2571" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/c36f2d0a4e585c84f91546e3710cc9ef9444201b/Modules/Loadable/Markups/qSlicerMarkupsModuleWidget.cxx#L2571" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/c36f2d0a4e585c84f91546e3710cc9ef9444201b/Modules/Loadable/Markups/qSlicerMarkupsModuleWidget.cxx#L2571</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="2561" style="counter-reset: li-counter 2560 ;">
<li>    }</li>
<li>  // set the display node from the logic defaults</li>
<li>  if (!this-&gt;markupsLogic())</li>
<li>    {</li>
<li>    return;</li>
<li>    }</li>
<li>  this-&gt;markupsLogic()-&gt;SetDisplayNodeToDefaults(displayNode);</li>
<li>}</li>
<li>
</li><li>//-----------------------------------------------------------------------------</li>
<li class="selected">void qSlicerMarkupsModuleWidget::onApplyCurveResamplingPushButtonClicked()</li>
<li>{</li>
<li>  Q_D(qSlicerMarkupsModuleWidget);</li>
<li>
</li><li>  double resampleNumberOfPoints = d-&gt;resampleCurveNumerOfOutputPointsSpinBox-&gt;value();</li>
<li>  if (resampleNumberOfPoints &lt;= 1)</li>
<li>    {</li>
<li>    return;</li>
<li>    }</li>
<li>
</li><li>  vtkMRMLMarkupsCurveNode* inputNode = vtkMRMLMarkupsCurveNode::SafeDownCast(d-&gt;MarkupsNode);</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #6 by @mjg (2020-06-29 18:29 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/smrolfe">@smrolfe</a>  Thank you for the help!</p>

---
