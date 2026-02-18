# Plotting: select point on click?

**Topic ID**: 3568
**Date**: 2018-07-24
**URL**: https://discourse.slicer.org/t/plotting-select-point-on-click/3568

---

## Post #1 by @ihnorton (2018-07-24 16:34 UTC)

<p>Is there a plot mode allowing click-to-select a point, rather than dragging the selection box? I only want to select one point at a time. Thanks.</p>

---

## Post #2 by @lassoan (2018-07-24 17:00 UTC)

<p>Currently, single point selection on click is not available in plot view. It would not be difficult to add a new interaction mode, in <a href="https://github.com/Slicer/Slicer/blob/badd435e439d3435444f27acaa2dd9fe4aa5a7d0/Libs/MRML/Widgets/qMRMLPlotView.cxx#L690-L712">qMRMLPlotView</a> that would map vtkChart::NOTIFY to LEFT_BUTTON event and then add an event handler for the notification that would select the clicked point. <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> or I would be happy to help/review if you decide to implement it.</p>
<p>What would you like to use this for? Note that you can define a custom label for each point that is displayed in the tooltip when you hover over a point with the mouse (labels are defined in the “Labels Column” table column that you set in Plots module / Series).</p>

---

## Post #3 by @mschumaker (2018-07-24 17:19 UTC)

<p>That’s a feature I’d also be interested in. I’d use it to allow a user to click on a point in a chart, which would then take them back to another workflow step where they set the value of that point.</p>

---

## Post #4 by @lassoan (2018-07-24 17:26 UTC)

<aside class="quote no-group" data-username="mschumaker" data-post="3" data-topic="3568">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mschumaker/48/1395_2.png" class="avatar"> mschumaker:</div>
<blockquote>
<p>take them back to another workflow step where they set the value of that point</p>
</blockquote>
</aside>
<p>Note that you can change the value of any point by directly dragging in the plot (if you switch interaction mode to “move points”). Of course this may not be optimal for all use cases, as you may want to use a different GUI or apply some constraints - I just wanted to make sure that you are aware of this feature.</p>

---

## Post #5 by @ihnorton (2018-07-24 17:29 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="3568">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>What would you like to use this for?</p>
</blockquote>
</aside>
<p>We are porting a matlab GUI in which we plot a slice-wise quantity, and one of the interaction modes provides a vertical slider on the plot to control which slice is displayed. Plotting a point per slice with a callback on click-to-select seems like the simplest approximation for now.</p>

---

## Post #6 by @Davide_Punzo (2018-07-24 18:04 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="3568">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Currently, single point selection on click is not available in plot view. It would not be difficult to add a new interaction mode, in <a href="https://github.com/Slicer/Slicer/blob/badd435e439d3435444f27acaa2dd9fe4aa5a7d0/Libs/MRML/Widgets/qMRMLPlotView.cxx#L690-L712" rel="noopener nofollow ugc">qMRMLPlotView</a> that would map vtkChart::NOTIFY to LEFT_BUTTON event and then add an event handler for the notification that would select the clicked point. <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> or I would be happy to help/review if you decide to implement it.</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/ihnorton">@ihnorton</a>. Unfortunately it is not straightforward to implement, because there is no single selection click at VTK level. The Andras suggestion is good, but even better will be to implement it at VTK level and expose it in Slicer as a new interaction mode (such as the click and move).</p>

---

## Post #7 by @Davide_Punzo (2018-07-24 18:06 UTC)

<p>Rethink about it, the click and drag can be constrained both on X and Y. The result will be that you select the point. However, at the moment it is not possible to select multiple points (one selection after another, let’s say) which had few bugs (and we have to force the selection to be on after the release of the click). In principle this can be implemented (at VTK level) and it should not be too difficult. At the moment, I haven’t the time to implement it, but I’ll be glad to review any PR. I may do it in future when I’ll have some free time (: .</p>

---

## Post #8 by @Davide_Punzo (2018-07-26 11:43 UTC)

<p>Done!</p>
<p>here VTK PR: <a href="https://gitlab.kitware.com/vtk/vtk/merge_requests/4531" rel="nofollow noopener">https://gitlab.kitware.com/vtk/vtk/merge_requests/4531</a><br>
here Slicer PR: <a href="https://github.com/Slicer/Slicer/pull/994" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/994</a></p>
<p>this selects (left click) one point in the plot view if using the pan, selection points and free-hand select point interaction modes (so if you click a point, the left click will do the single point selection, otherwise it will do still the interaction chosen in the plotView controller). In addition pressing the key U removes the current selection. Still, there can be only one selection at time: a subsequent selection will delete the previous one.</p>
<p>Video: <a href="https://www.dropbox.com/s/vzue6tmchm3vltq/SinglePointSelection.webm?dl=0" rel="nofollow noopener">https://www.dropbox.com/s/vzue6tmchm3vltq/SinglePointSelection.webm?dl=0</a></p>
<p>Remember that there is an high level Slicer API method for connecting the VTK selection to your modules:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/50774a8691293659f2867e5e92ef0e285de00f0e/Libs/MRML/Widgets/qMRMLPlotView.cxx#L622-L669" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/50774a8691293659f2867e5e92ef0e285de00f0e/Libs/MRML/Widgets/qMRMLPlotView.cxx#L622-L669" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/50774a8691293659f2867e5e92ef0e285de00f0e/Libs/MRML/Widgets/qMRMLPlotView.cxx#L622-L669</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="622" style="counter-reset: li-counter 621 ;">
<li>void qMRMLPlotViewPrivate::emitSelection()</li>
<li>{</li>
<li>Q_Q(qMRMLPlotView);</li>
<li>
</li>
<li>if (!q-&gt;chart())</li>
<li>  {</li>
<li>  return;</li>
<li>  }</li>
<li>
</li>
<li>const char *PlotChartNodeID = this-&gt;MRMLPlotViewNode-&gt;GetPlotChartNodeID();</li>
<li>
</li>
<li>vtkMRMLPlotChartNode* plotChartNode = vtkMRMLPlotChartNode::SafeDownCast</li>
<li>  (this-&gt;MRMLScene-&gt;GetNodeByID(PlotChartNodeID));</li>
<li>if (!plotChartNode)</li>
<li>  {</li>
<li>  return;</li>
<li>  }</li>
<li>
</li>
<li>vtkNew&lt;vtkStringArray&gt; mrmlPlotSeriesIDs;</li>
<li>vtkNew&lt;vtkCollection&gt; selectionCol;</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/50774a8691293659f2867e5e92ef0e285de00f0e/Libs/MRML/Widgets/qMRMLPlotView.cxx#L622-L669" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Punzo/SlicerAstro/blob/8387dcdf49b206899c85c8422013b94a61f1972d/AstroModeling/qSlicerAstroModelingModuleWidget.cxx#L833-L852" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Punzo/SlicerAstro/blob/8387dcdf49b206899c85c8422013b94a61f1972d/AstroModeling/qSlicerAstroModelingModuleWidget.cxx#L833-L852" target="_blank" rel="nofollow noopener">Punzo/SlicerAstro/blob/8387dcdf49b206899c85c8422013b94a61f1972d/AstroModeling/qSlicerAstroModelingModuleWidget.cxx#L833-L852</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="833" style="counter-reset: li-counter 832 ;">
<li>qMRMLPlotWidget* plotWidget = layoutManager-&gt;plotWidget(0);</li>
<li>
</li>
<li>if(!plotWidget)</li>
<li>  {</li>
<li>  qCritical() &lt;&lt; "qSlicerAstroMomentMapsModuleWidget::setMRMLScene : "</li>
<li>                 "plotWidget not found!";</li>
<li>  return;</li>
<li>  }</li>
<li>
</li>
<li>qMRMLPlotView* plotView = plotWidget-&gt;plotView();</li>
<li>if(!plotView)</li>
<li>  {</li>
<li>  qCritical() &lt;&lt; "qSlicerAstroMomentMapsModuleWidget::setMRMLScene : "</li>
<li>                 "plotView not found!";</li>
<li>  return;</li>
<li>  }</li>
<li>
</li>
<li>QObject::connect(plotView, SIGNAL(dataSelected(vtkStringArray*, vtkCollection*)),</li>
<li>                 this, SLOT(onPlotSelectionChanged(vtkStringArray*, vtkCollection*)));</li>
<li>
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #9 by @ihnorton (2018-07-26 14:11 UTC)

<aside class="quote no-group" data-username="Davide_Punzo" data-post="8" data-topic="3568">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>here VTK PR</p>
</blockquote>
</aside>
<p>Thanks!</p>
<aside class="quote no-group" data-username="Davide_Punzo" data-post="8" data-topic="3568">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>so if you click a point, the left click will do the single point selection, otherwise it will do still the interaction chosen in the plotView controller</p>
</blockquote>
</aside>
<p>Is it possible to make this selection mode exclusive?</p>

---

## Post #10 by @Davide_Punzo (2018-07-26 14:15 UTC)

<p>you are welcome.</p>
<blockquote>
<p>Is it possible to make this selection mode exclusive?</p>
</blockquote>
<p>do you mean to have a new interaction mode in the plot view controller combo box? If it is this it can be done, I didn’t want to add an another interaction mode, however for me it is fine. <a class="mention" href="/u/lassoan">@lassoan</a> what do you think about it?</p>

---

## Post #11 by @ihnorton (2018-07-26 14:29 UTC)

<aside class="quote no-group" data-username="Davide_Punzo" data-post="10" data-topic="3568">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/davide_punzo/48/66104_2.png" class="avatar"> Davide_Punzo:</div>
<blockquote>
<p>do you mean to have a new interaction mode in the plot view controller combo box?</p>
</blockquote>
</aside>
<p>I couldn’t tell for sure from the code/your comment: does click-to-select with this PR require also enabling one of the other selection modes – box/freehand? (I would like to allow only click-to-select)</p>

---

## Post #12 by @Davide_Punzo (2018-07-26 14:33 UTC)

<blockquote>
<p>does click-to-select with this PR require also enabling one of the other selection modes – box/freehand?</p>
</blockquote>
<p>with the current PR, you will be able to use the click one point selection also with the pan interaction mode. Will that work for you?</p>
<p>in the <a href="https://www.dropbox.com/s/vzue6tmchm3vltq/SinglePointSelection.webm?dl=0" rel="noopener nofollow ugc">video</a> I show how does work both with the pan view and the select points interaction</p>

---

## Post #13 by @ihnorton (2018-07-26 14:41 UTC)

<p>Ok, I see. Eventually we may want to be able to select with pan disabled, but not critical for now – this is great and sufficient to port the GUI.</p>

---

## Post #14 by @Davide_Punzo (2018-07-26 14:55 UTC)

<blockquote>
<p>Ok, I see. Eventually we may want to be able to select with pan disabled, but not critical for now – this is great and sufficient to port the GUI.</p>
</blockquote>
<p>In the case, for allowing only the clickSelectPoint interaction, it will be needed to change the following if condition in the VTK chartXY method:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://gitlab.kitware.com/Punzo/vtk/blob/SingleClickSelection/Charts/Core/vtkChartXY.cxx#L1911-1915">
  <header class="source">
      <img src="https://gitlab.kitware.com/uploads/-/system/appearance/favicon/1/KitwareMarkIcon.png" class="site-icon" width="32" height="32">

      <a href="https://gitlab.kitware.com/Punzo/vtk/blob/SingleClickSelection/Charts/Core/vtkChartXY.cxx#L1911-1915" target="_blank" rel="noopener nofollow ugc">GitLab</a>
  </header>

  <article class="onebox-body">
    <img width="64" height="64" src="https://gitlab.kitware.com/uploads/-/system/project/avatar/1854/vtk_logo-main1.png" class="thumbnail onebox-avatar">

<h3><a href="https://gitlab.kitware.com/Punzo/vtk/blob/SingleClickSelection/Charts/Core/vtkChartXY.cxx#L1911-1915" target="_blank" rel="noopener nofollow ugc">Charts/Core/vtkChartXY.cxx · SingleClickSelection · Davide Punzo / VTK · GitLab</a></h3>

  <p>Visualization Toolkit</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>and add the clickSelectPoint interaction in combobox in the GUI of the plot controller and set the (click)ActionToButton of the chart for the specific interaction mode here:<br>
<a href="https://github.com/Punzo/Slicer/blob/SingleClickSelection/Libs/MRML/Widgets/qMRMLPlotView.cxx#L697-L720" class="onebox" target="_blank" rel="noopener nofollow ugc">https://github.com/Punzo/Slicer/blob/SingleClickSelection/Libs/MRML/Widgets/qMRMLPlotView.cxx#L697-L720</a></p>

---
