# Show ECG curve plot

**Topic ID**: 23291
**Date**: 2022-05-05
**URL**: https://discourse.slicer.org/t/show-ecg-curve-plot/23291

---

## Post #1 by @connorh (2022-05-05 18:58 UTC)

<p>Hi Robin,<br>
it has been a while but was this ever solved? I am wondering the same thing.</p>
<p>I have a 4D cardiac dataset and I also have ECG voltage tracings for a cardiac cycle. I would like to enable playback through my 4D cardiac dataset while showing where on the ECG voltage tracing we are. I figured this might be achieved through qMRMLPlotWidgets in my UI, but can’t figure out how to plot to them…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/7/9763a108d27701d32a0d708a25986000b8b77eff.jpeg" data-download-href="/uploads/short-url/lBfyeWdCbdrJNgbHqqI0FPjG9FJ.jpeg?dl=1" title="4D Playback w ECG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9763a108d27701d32a0d708a25986000b8b77eff_2_510x500.jpeg" alt="4D Playback w ECG" data-base62-sha1="lBfyeWdCbdrJNgbHqqI0FPjG9FJ" width="510" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9763a108d27701d32a0d708a25986000b8b77eff_2_510x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9763a108d27701d32a0d708a25986000b8b77eff_2_765x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9763a108d27701d32a0d708a25986000b8b77eff_2_1020x1000.jpeg 2x" data-dominant-color="4B93D2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4D Playback w ECG</span><span class="informations">1920×1881 82.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-05-05 21:58 UTC)

<p>You can read the ECG signals to a table node. See for example how it is done in the UltrasoundImage3D reader:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/SlicerHeart/SlicerHeart/blob/bdbffde05b8193d04bf945bf4d5037c73b8d4a27/UltrasoundImage3dReader/UltrasoundImage3dReader.py#L190-L196">
  <header class="source">

      <a href="https://github.com/SlicerHeart/SlicerHeart/blob/bdbffde05b8193d04bf945bf4d5037c73b8d4a27/UltrasoundImage3dReader/UltrasoundImage3dReader.py#L190-L196" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerHeart/SlicerHeart/blob/bdbffde05b8193d04bf945bf4d5037c73b8d4a27/UltrasoundImage3dReader/UltrasoundImage3dReader.py#L190-L196" target="_blank" rel="noopener">SlicerHeart/SlicerHeart/blob/bdbffde05b8193d04bf945bf4d5037c73b8d4a27/UltrasoundImage3dReader/UltrasoundImage3dReader.py#L190-L196</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="190" style="counter-reset: li-counter 189 ;">
          <li>ecg = source.GetECG()</li>
          <li>tableNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode", baseName+" ECG")</li>
          <li>ecgSamples = self.safeArrayToNumpy(ecg.samples)</li>
          <li>numberOfSamples = len(ecgSamples)</li>
          <li>ecgTimestamps = np.arange(ecg.start_time, ecg.start_time+numberOfSamples*ecg.delta_time, ecg.delta_time)</li>
          <li>trigTimes = self.safeArrayToNumpy(ecg.trig_times)</li>
          <li>slicer.util.updateTableFromArray(tableNode, [ecgTimestamps, ecgSamples, trigTimes], ["time", "ecg", "triggerTimes"])</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>You can find some more plotting examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#plots">script repository</a> and more explanations in the documentation (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/plots.html">user guide</a>, <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#plots">developer guide</a>).</p>
<p>If you want to display a view outside the view layout (I would not recommend that, because it is probably better to choose or create an appropriate view layout instead) then you can follow this example:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/580a2bb67a7dc750941c45d49e0c76f23a737a9b.png" data-download-href="/uploads/short-url/cyPO6tPmzj0HElPdIwh5QA1V4WT.png?dl=1" title=""><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/580a2bb67a7dc750941c45d49e0c76f23a737a9b_2_690x420.png" alt="" data-base62-sha1="cyPO6tPmzj0HElPdIwh5QA1V4WT" role="presentation" width="690" height="420" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/580a2bb67a7dc750941c45d49e0c76f23a737a9b_2_690x420.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/8/580a2bb67a7dc750941c45d49e0c76f23a737a9b_2_1035x630.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/8/580a2bb67a7dc750941c45d49e0c76f23a737a9b.png 2x" data-dominant-color="C6C7CA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">1035×630 93.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<aside class="quote quote-modified" data-post="12" data-topic="20242">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/plotting-the-signals/20242/12">Plotting the signals</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    I could not reproduce any crash with the scripts above, so maybe the issue is how you fill the tables with real data. I’ve made a couple of fixes and improvement (fix order of views, fit plot to the view, adjust labeling, etc.) and this is the result: 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fe3edd87094a9e201bcbf42f7f8a03d8cd77b39.png" data-download-href="/uploads/short-url/boK3tawewWs5PBIRvUb4n4FZetj.png?dl=1" title="image">[image]</a> 
The updated code: 
def SetLayout(nChannels):
    customLayout=(
    "&lt;layout type=\"horizontal\" split=\"true\"&gt;" 
        "&lt;item&gt;"
            "&lt;layout type=\"vertical\" split=\"true\"&gt;"
                "&lt;item&gt;"
                    "&lt;vi…
  </blockquote>
</aside>

<p>There is also a simpler example in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-slice-view-outside-the-view-layout">script repository</a>.</p>
<p>To display a marker on the signal, I would recommend to add a series that has a single point or vertical line segment and add that to the chart.</p>

---

## Post #4 by @connorh (2022-05-06 20:12 UTC)

<p>Thank you Dr. Lasso for the help! I guess my question is specific to the qMRMLPlotWidget, or something equivalent so that I can plot the ECG waveform within my extension UI. For example, using the QT designer I have added 3 qMRMLPlotWidgets to my UI, with the intent of plotting a 3-lead ECG overlaid with my playback tools:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/e/7e5b1bb77ef001aa636f48e95c4b59dd28a8bf49.png" data-download-href="/uploads/short-url/i1NmjepQF3Hjj2uT4iE2DJSN6SB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e5b1bb77ef001aa636f48e95c4b59dd28a8bf49_2_517x129.png" alt="image" data-base62-sha1="i1NmjepQF3Hjj2uT4iE2DJSN6SB" width="517" height="129" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e5b1bb77ef001aa636f48e95c4b59dd28a8bf49_2_517x129.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e5b1bb77ef001aa636f48e95c4b59dd28a8bf49_2_775x193.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/e/7e5b1bb77ef001aa636f48e95c4b59dd28a8bf49_2_1034x258.png 2x" data-dominant-color="A5E3E7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1428×358 10.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What I’m looking for is something similar to this line of code, except to plot a vtkMRMLPlotChartNode into my UI rather than the standard Slicer Plotting Layout.<br>
<code>slicer.modules.plots.logic().ShowChartInLayout(plotChartNode)</code></p>
<p>I’ve tried to pull the equivalent of what I’m running within my extension:</p>
<pre><code class="lang-auto">
viewNode = self.logic.createECGPlotNode()
self.ui.qMRMLPlotWidget1.setMRMLPlotViewNode(viewNode) #This is what doesn't seem to be working

def createECGPlotNode():

    #Create Dummy Data
    lead1 = np.random.randint(1,100,2000)
    lead1ecg = np.array(lead1)
    t_step = 0.01 #10ms steps
    t = np.linspace(0,len(lead1)*t_step,len(lead1))

    data_to_plot = np.column_stack((t,lead1ecg))

    tableNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLTableNode", "ECGTable")
    slicer.util.updateTableFromArray(tableNode, data_to_plot)
    tableNode.GetTable().GetColumn(0).SetName("Time")
    tableNode.GetTable().GetColumn(1).SetName("Voltage")
    
    plotSeriesNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotSeriesNode", "PlotSeriesNode")
    plotSeriesNode.SetAndObserveTableNodeID(tableNode.GetID())
    plotSeriesNode.SetXColumnName("Time")
    plotSeriesNode.SetYColumnName("Voltage")
    plotSeriesNode.SetPlotType(plotSeriesNode.PlotTypeScatter)
    
    plotChartNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotChartNode")
    plotChartNode.AddAndObservePlotSeriesNodeID(plotSeriesNode.GetID())

    viewNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLPlotViewNode","ViewNode")
    viewNode.SetPlotChartNodeID(plotChartNode.GetID())

    #If I put slicer.modules.plots.logic().ShowChartInLayout(plotChartNode) here, then it plots properly to usual display

    return viewNode
</code></pre>

---

## Post #5 by @lassoan (2022-05-10 04:14 UTC)

<p>You need to make sure the layout manager does own your view nodes. See <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#show-a-slice-view-outside-the-view-layout">example in the script repository</a>.</p>

---

## Post #6 by @whu (2022-06-11 04:54 UTC)

<p>Dear Sir,<br>
once the 4D data was loaded into slicer, how to reference the data using python script?</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="23291">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><code>ecg = source.GetECG()</code></p>
</blockquote>
</aside>
<p>especially the source ?  We don’t need to reload the data as the example .</p>

---

## Post #7 by @lassoan (2022-06-12 01:17 UTC)

<p>What file format did you load your data from?</p>
<p>The example above was for Image3dAPI reader, which has that <code>source</code> object. You don’t need to use that object because the reader creates a table node from the ECG data that you can easily visualize using Plots module.</p>
<p>If you are interested in showing ECG then you may join <a class="mention" href="/u/connorh">@connorh</a> at the upcoming <a href="https://projectweek.na-mic.org/">project week</a> to work on cardiac data reading and visualization.</p>

---

## Post #8 by @whu (2022-06-12 13:11 UTC)

<p>The DICOM file exported by QLab, and patched in Slicer.<br>
thanks, I will try to focus on the project week.</p>

---

## Post #9 by @lassoan (2022-06-13 04:30 UTC)

<p>Unfortunately, the Cartesian images exported by QLab do not contain any ECG data.</p>

---
