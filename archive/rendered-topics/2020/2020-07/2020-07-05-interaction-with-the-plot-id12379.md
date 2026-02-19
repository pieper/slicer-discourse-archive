---
topic_id: 12379
title: "Interaction With The Plot"
date: 2020-07-05
url: https://discourse.slicer.org/t/12379
---

# Interaction with the plot

**Topic ID**: 12379
**Date**: 2020-07-05
**URL**: https://discourse.slicer.org/t/interaction-with-the-plot/12379

---

## Post #1 by @fpsiddiqui91 (2020-07-05 11:14 UTC)

<p>Dear Developers,</p>
<p>I am developing an app in Slicer to show continuously updated histogram of the data. So far I have managed to achieve this by using plot module:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots</a></p>
<p>For further exploration, I needed to have interaction with the plot. For that, I used click and drag feature and managed to extract the data from the plot.</p>
<p>The problem is, since my plot is constantly updating, I cannot draw a rectangle on the plot. Is there any way to draw a rectangle that can stay over the top of the plot?<br>
Thank you.</p>

---

## Post #2 by @fpsiddiqui91 (2020-07-05 22:43 UTC)

<p>After doing some research, I found a work around but could not yet implement it. What I really want to do is to draw a rectangle over a constantly updating plot view.<br>
I think Qt.Qpainter/ paintEven is the best solution.</p>
<p>however, I dont know how to implement Qpaint over a plot widget.  Can you help me with this? Can you guide me how to modify paintEvent of Plot Widget?</p>
<p>Or is there an alternate solution?</p>
<p>I want something like this: (orange and blue boxes, which can be drawn by a mouse, over a histogram)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/782b6013b93e3bb2c04698b83c341b7fac46cc08.png" data-download-href="/uploads/short-url/h94e6VgjeVj1weplTulZbHTe6kU.png?dl=1" title="Picture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/782b6013b93e3bb2c04698b83c341b7fac46cc08_2_674x500.png" alt="Picture1" data-base62-sha1="h94e6VgjeVj1weplTulZbHTe6kU" width="674" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/782b6013b93e3bb2c04698b83c341b7fac46cc08_2_674x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/782b6013b93e3bb2c04698b83c341b7fac46cc08.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/782b6013b93e3bb2c04698b83c341b7fac46cc08.png 2x" data-dominant-color="D0D5DB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Picture1</span><span class="informations">908×673 21.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @fpsiddiqui91 (2020-07-06 16:58 UTC)

<p>I was wondering if we can have a some functionality in VTK plots? I tried to look into it but could not find the solution. <a class="mention" href="/u/lassoan">@lassoan</a> any tips maybe?  Thank you</p>

---

## Post #4 by @Davide_Punzo (2020-07-07 06:57 UTC)

<p>the selection (and interaction in general) are handled at vtk level:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Kitware/VTK/blob/8b8e188c65c6687109e831316915177e7634eb79/Charts/Core/vtkChartXY.cxx#L1929" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Kitware/VTK/blob/8b8e188c65c6687109e831316915177e7634eb79/Charts/Core/vtkChartXY.cxx#L1929" target="_blank" rel="nofollow noopener">Kitware/VTK/blob/8b8e188c65c6687109e831316915177e7634eb79/Charts/Core/vtkChartXY.cxx#L1929</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="1919" style="counter-reset: li-counter 1918 ;">
<li>  {</li>
<li>    return true;</li>
<li>  }</li>
<li>  else</li>
<li>  {</li>
<li>    return false;</li>
<li>  }</li>
<li>}</li>
<li>
</li><li>//-----------------------------------------------------------------------------</li>
<li class="selected">bool vtkChartXY::MouseButtonReleaseEvent(const vtkContextMouseEvent&amp; mouse)</li>
<li>{</li>
<li>  // Iterate through each corner, and check for a nearby point</li>
<li>  for (size_t i = 0; i &lt; this-&gt;ChartPrivate-&gt;PlotCorners.size(); ++i)</li>
<li>  {</li>
<li>    if (this-&gt;ChartPrivate-&gt;PlotCorners[i]-&gt;MouseButtonReleaseEvent(mouse))</li>
<li>    {</li>
<li>      return true;</li>
<li>    }</li>
<li>  }</li>
<li>
</li></ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>for the selection the class uses some private methods, therefore I advise you to implement the functionality directly in vtk (for example: you could could instantiate an array of selection polygons and use them when interacting with CTRL + left click. In addition you can add an observer to check when the plots are changed and update the selection/fire a signal). Otherwise you would have to expose some of the methods as public or rewrite/copy everything in your code which I don’t advise.</p>

---

## Post #5 by @fpsiddiqui91 (2020-07-07 11:40 UTC)

<p>Thank you for your advice. I have started working on VTK plots. just a little guidance.<br>
can I render vtkchartXY()  in plotwidget-&gt; plotview?</p>
<p>specifically, how to add a view for vtk.vtkContextView()?</p>
<p>Are there any examples in python for this?</p>
<p>Thank you</p>

---

## Post #6 by @Davide_Punzo (2020-07-07 15:23 UTC)

<p>the Slicer plot view widget already set up all the vtk infrastructure (the plot Qt widget uses the vtkchartXY, and the vtkchartXY handles all the vtkplot objects).</p>
<p>You will need only to modify the mouse interaction methods in the vtkchartXY. However, this is not straightforward, and you will need to modify in C++ the class vtkchartXY (then submit a pull request at vtk level and then update the vtk branch used by Slicer). I advise you to go for this path only if you feel comfortable with C++ and have a little bit of knowlege of vtk in C++.</p>
<p>I imagine that alternative solutions are:</p>
<ol>
<li>you create the selection rectangle in Qt (as you suggested) and try to map the Qt view coordinates with the vtk view ones, then simply it will be to get the indexes from the plot objects.</li>
<li>you create in your module GUI some sliders or range buttons which indicates the user selection for the histogram.</li>
</ol>

---

## Post #7 by @fpsiddiqui91 (2020-07-07 15:40 UTC)

<p>Thank you for your detailed response <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a>.</p>
<p>I understand the problem and I have been trying to find the workaround. I have few queries regarding the alternate solution you provided. Can you please guide me on how to draw a selection rectangle on the top of the plot widget?</p>
<p>And How can I set up a Qt mouse interaction event with the plot widget? So far I am using vtk signal to extract the points from the plot.</p>
<pre><code>pv =plotWidget.plotView()

pv.connect("dataSelected(vtkStringArray*, vtkCollection*)",self.onDataSelected)</code></pre>

---

## Post #8 by @fpsiddiqui91 (2020-07-07 16:51 UTC)

<p>Further addition to my queries:</p>
<p>As mentioned above, I am transmitting the VTK signal and added a listener function in python. Is there any way to make similar functions in python which respond to the mouse click and mouse release event over a plot widget. I am sure it is possible. Just a bit guidance on this regard would be helpful.</p>
<p>Thanks alot <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a> for your help.</p>

---

## Post #9 by @Davide_Punzo (2020-07-08 12:23 UTC)

<aside class="quote no-group" data-username="fpsiddiqui91" data-post="7" data-topic="12379">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/f/53a042/48.png" class="avatar"> fpsiddiqui91:</div>
<blockquote>
<p>Can you please guide me on how to draw a selection rectangle on the top of the plot widget?</p>
</blockquote>
</aside>
<p>rethinking about this… I think it is a bad idea. In this way (drawing a rectangle in Qt over the vtk view) the selection will not take into account any resize/move event of the main windows, etc…</p>
<p>Therefore you will need to add properly actors in the vtk view and then perfom the selection. I don’t see an easy solution for doing this in python outside the vtkChartXY class. In general, the implementation will require dirty code/assumptions and to copy/reuse a lot of code and functionality already present in the vtk plot infrastructure.</p>
<p>If you would like such feature I advise to contribute to vtk by properly implement the feature in the C++ vtk infrastructure. Otherwise, you can go for a different/simpler approach, for example:</p>
<ol>
<li>sliders in the module gui for making the selection</li>
<li>placing line plots over the histogram (see as example <a href="https://raw.githubusercontent.com/Punzo/SlicerAstroWikiImages/master/Histogram.png" rel="noopener nofollow ugc">https://raw.githubusercontent.com/Punzo/SlicerAstroWikiImages/master/Histogram.png</a> <a href="https://www.youtube.com/watch?v=5Ag0PzYw0Hk" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=5Ag0PzYw0Hk</a>)</li>
</ol>

---

## Post #10 by @lassoan (2020-07-08 12:35 UTC)

<p>You can also do what is done in the local histogram of Segment Editor’s threshold effect:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="cevlMLyhfK8" data-video-title='Segment Editor: New "Local threshold" effect' data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=cevlMLyhfK8" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/cevlMLyhfK8/maxresdefault.jpg" title='Segment Editor: New "Local threshold" effect' width="" height="">
  </a>
</div>

<p>The implementation is not very simple, but it is fully in Python, available here:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/dad86b0942d07cac25e52d470c3ea4c00f7d6958/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorThresholdEffect.py#L245-L289">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/dad86b0942d07cac25e52d470c3ea4c00f7d6958/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorThresholdEffect.py#L245-L289" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/dad86b0942d07cac25e52d470c3ea4c00f7d6958/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorThresholdEffect.py#L245-L289" target="_blank" rel="noopener">Slicer/Slicer/blob/dad86b0942d07cac25e52d470c3ea4c00f7d6958/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorThresholdEffect.py#L245-L289</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="245" style="counter-reset: li-counter 244 ;">
          <li>self.histogramView = ctk.ctkTransferFunctionView()</li>
          <li>histogramFrame.addWidget(self.histogramView)</li>
          <li>scene = self.histogramView.scene()</li>
          <li>
          <li>self.histogramFunction = vtk.vtkPiecewiseFunction()</li>
          <li>self.histogramFunctionContainer = ctk.ctkVTKPiecewiseFunction(self.scriptedEffect)</li>
          <li>self.histogramFunctionContainer.setPiecewiseFunction(self.histogramFunction)</li>
          <li>self.histogramFunctionItem = ctk.ctkTransferFunctionBarsItem(self.histogramFunctionContainer)</li>
          <li>self.histogramFunctionItem.barWidth = 1.0</li>
          <li>self.histogramFunctionItem.logMode = ctk.ctkTransferFunctionBarsItem.NoLog</li>
          <li>self.histogramFunctionItem.setZValue(1)</li>
          <li>scene.addItem(self.histogramFunctionItem)</li>
          <li>
          <li>self.histogramEventFilter = HistogramEventFilter()</li>
          <li>self.histogramEventFilter.setThresholdEffect(self)</li>
          <li>self.histogramFunctionItem.installEventFilter(self.histogramEventFilter)</li>
          <li>
          <li>self.minMaxFunction = vtk.vtkPiecewiseFunction()</li>
          <li>self.minMaxFunctionContainer = ctk.ctkVTKPiecewiseFunction(self.scriptedEffect)</li>
          <li>self.minMaxFunctionContainer.setPiecewiseFunction(self.minMaxFunction)</li>
      </ol>
    </code></pre>


  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/dad86b0942d07cac25e52d470c3ea4c00f7d6958/Modules/Loadable/Segmentations/EditorEffects/Python/SegmentEditorThresholdEffect.py#L245-L289" target="_blank" rel="noopener">show original</a>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #11 by @fpsiddiqui91 (2020-07-13 12:02 UTC)

<p>Perfect <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/davide_punzo">@Davide_Punzo</a>. Line plot is a good option. I am also looking more into modifying vtkchartxv class.</p>
<p>The suggestion by Lassoan pretty much gives me the desired output. I am gonna move forward with adding the histogram as explained in Segment Editor. Let’s see if I can make any further improvements on it.</p>
<p>Thanks a lot.</p>

---
