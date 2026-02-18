# Get Segmentation layer

**Topic ID**: 3312
**Date**: 2018-06-27
**URL**: https://discourse.slicer.org/t/get-segmentation-layer/3312

---

## Post #1 by @Fernando (2018-06-27 09:41 UTC)

<p>Hi all,</p>
<p>In my <code>.slicerrc.py</code> I create a slider to visualize MIPs of different slab thicknesses on all views:</p>
<pre><code class="lang-auto">logics = getSlicesLogics()
nodes = getSlicesNodes()
for sliceNode, sliceLogic in zip(nodes, logics):
    layers = [
        sliceLogic.GetBackgroundLayer(),
        sliceLogic.GetForegroundLayer(),
        sliceLogic.GetLabelLayer(),
    ]
    for layer in layers:
        reslice = layer.GetReslice()
        reslice.SetSlabModeToMax()
        reslice.SetSlabNumberOfSlices(int(value))
        reslice.SetSlabSliceSpacingFraction(0.5)
        sliceNode.Modified()
</code></pre>
<p>How do I get access to the Segmentation layer? There is no <code>sliceLogic.GetSegmentationLayer()</code>.</p>

---

## Post #2 by @ihnorton (2018-06-27 12:07 UTC)

<p><code>.slicerrc.py</code> execution happens very early in the application loading process. If something is missing that you would normally find in the command prompt, it usually means that the corresponding library hasn’t been fully loaded yet. Probably the simplest option is to create a scripted module with your functionality. If you still want to use <code>slicerrc</code>, then you can hook up delayed loading with the <code>onStartupCompleted</code> event. See:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/SlicerStartupCompletedTestHelperModule.py#L19" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/SlicerStartupCompletedTestHelperModule.py#L19" target="_blank">Slicer/Slicer/blob/master/Applications/SlicerApp/Testing/Python/SlicerStartupCompletedTestHelperModule.py#L19</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="9" style="counter-reset: li-counter 8 ;">
<li>  ScriptedLoadableModule.__init__(self, parent)</li>
<li>  self.parent.title = "SlicerStartupCompletedTest"</li>
<li>  self.parent.categories = ["Testing.TestCases"]</li>
<li>  self.parent.contributors = ["Jean-Christophe Fillion-Robin (Kitware), Andras Lasso (PerkLab)"]</li>
<li>  self.parent.widgetRepresentationCreationEnabled = False</li>
<li>
</li>
<li>  self.testOutputFileName = os.environ['SLICER_STARTUP_COMPLETED_TEST_OUTPUT']</li>
<li>  if os.path.isfile(self.testOutputFileName):</li>
<li>   os.remove(self.testOutputFileName)</li>
<li>
</li>
<li class="selected">  slicer.app.connect("startupCompleted()", self.onStartupCompleted)</li>
<li>
</li>
<li>  print("SlicerStartupCompletedTestHelperModule initialized")</li>
<li>
</li>
<li>def onStartupCompleted(self):</li>
<li>  print("StartupCompleted emitted")</li>
<li>  import os</li>
<li>  fd = os.open(self.testOutputFileName, os.O_RDWR|os.O_CREAT)</li>
<li>  os.write(fd, 'SlicerStartupCompletedTestHelperModule.py generated this file')</li>
<li>  os.write(fd, 'when slicer.app emitted startupCompleted() signal\n')</li>
<li>  os.close(fd)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>For example, you might put the delay loaded code in a separate file, and do something like this in <code>slicerrc.py</code>:</p>
<pre><code class="lang-auto">def load_delayed():
  execfile("/path/to/delay_load.py")

slicer.app.connect("startupCompleted()", load_delayed)
</code></pre>

---

## Post #3 by @Fernando (2018-06-27 12:50 UTC)

<p>Hi <a class="mention" href="/u/ihnorton">@ihnorton</a>,</p>
<p>Thanks for your answer. I might have not been totally clear. There isn’t anything missing on startup in my case, the slice nodes don’t have a <code>GetSegmentationLayer</code> method even in the Python console. That’s a name I made up in order to explain what I wanted to do.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> might be able to help, I think he worked on this when the Segmentations framework was included in the core.</p>

---

## Post #4 by @cpinter (2018-06-27 14:18 UTC)

<p>Hi Fernando,<br>
Segmentation is a totally different animal than the other layers. As it’s not a volume, it has its own 2D displayable manager. It’s more complicated than the volume one because it can show the labelmap as well as the closed surface. In order to do the same thing for segmentations, we’d need to implement slab mode in vtkMRMLSegmentationDisplayableManager2D and add the same options to vtkMRMLSegmentationDisplayNode.</p>

---

## Post #5 by @Fernando (2018-06-27 14:33 UTC)

<p>Ok <a class="mention" href="/u/cpinter">@cpinter</a>, thanks for the info.</p>

---
