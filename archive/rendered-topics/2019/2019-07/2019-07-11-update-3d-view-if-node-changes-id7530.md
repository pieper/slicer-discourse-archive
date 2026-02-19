---
topic_id: 7530
title: "Update 3D View If Node Changes"
date: 2019-07-11
url: https://discourse.slicer.org/t/7530
---

# Update 3D view if node changes

**Topic ID**: 7530
**Date**: 2019-07-11
**URL**: https://discourse.slicer.org/t/update-3d-view-if-node-changes/7530

---

## Post #1 by @fpsiddiqui91 (2019-07-11 13:48 UTC)

<p>Hello Slicer Developers,</p>
<p>I am quite new to slicer and still in exploring stage. I have developed a small application in which a track can be generated from the given markup</p>
<p>Then I changed the coordinates of the markup simply by</p>
<p><code>Preformatted text</code>markups.SetNthFiducialPositionFromArray(markups.GetNumberOfFiducials() - 1, newCord)<code>Preformatted text</code></p>
<p>Now I want to change the coodinates of the markup in a loop which can easily be done.</p>
<p>The problem is the 3D view is not updating at each iteration after updating the markup Node? is there any command to update the 3D view while the processing the loop.</p>
<p>Thank you</p>

---

## Post #2 by @pieper (2019-07-11 15:28 UTC)

<p>Slicer is event driven, so rendering only happens when all events have been processed.  So you can either call processEvents, like in ScreenCapture, or you can set up a timer to make your changes like in Rock mode for the viewer.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/21dc780a216f077bdd080fdc64073ccf6b5356e0/Modules/Scripted/ScreenCapture/ScreenCapture.py#L831" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/21dc780a216f077bdd080fdc64073ccf6b5356e0/Modules/Scripted/ScreenCapture/ScreenCapture.py#L831" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/21dc780a216f077bdd080fdc64073ccf6b5356e0/Modules/Scripted/ScreenCapture/ScreenCapture.py#L831</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="821" style="counter-reset: li-counter 820 ;">
<li>def getSliceOffsetResolution(self, sliceNode):</li>
<li>  sliceLogic = self.getSliceLogicFromSliceNode(sliceNode)</li>
<li>
</li>
<li>  sliceOffsetResolution = 1.0</li>
<li>  sliceSpacing = sliceLogic.GetLowestVolumeSliceSpacing();</li>
<li>  if sliceSpacing is not None and sliceSpacing[2]&gt;0:</li>
<li>    sliceOffsetResolution = sliceSpacing[2]</li>
<li>
</li>
<li>  return sliceOffsetResolution</li>
<li>
</li>
<li class="selected">def captureImageFromView(self, view, filename, transparentBackground=False):</li>
<li>
</li>
<li>  slicer.app.processEvents()</li>
<li>  if view:</li>
<li>    view.forceRender()</li>
<li>  else:</li>
<li>    # force rendering of all views</li>
<li>    lm = slicer.app.layoutManager()</li>
<li>    for viewIndex in range(lm.threeDViewCount):</li>
<li>      lm.threeDWidget(viewIndex).threeDView().forceRender()</li>
<li>    for sliceViewName in lm.sliceViewNames():</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/commontk/CTK/blob/cccef11c938cc946789ddb25ccc613287a33c56e/Libs/Visualization/VTK/Widgets/ctkVTKRenderView.cpp#L166-L192" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/commontk/CTK/blob/cccef11c938cc946789ddb25ccc613287a33c56e/Libs/Visualization/VTK/Widgets/ctkVTKRenderView.cpp#L166-L192" target="_blank" rel="nofollow noopener">commontk/CTK/blob/cccef11c938cc946789ddb25ccc613287a33c56e/Libs/Visualization/VTK/Widgets/ctkVTKRenderView.cpp#L166-L192</a></h4>
<pre class="onebox"><code class="lang-cpp"><ol class="start lines" start="166" style="counter-reset: li-counter 165 ;">
<li>void ctkVTKRenderViewPrivate::doRock()</li>
<li>{</li>
<li>  Q_Q(ctkVTKRenderView);</li>
<li>  Q_ASSERT(this-&gt;Renderer-&gt;IsActiveCameraCreated());</li>
<li>
</li>
<li>  if (!this-&gt;RockEnabled)</li>
<li>    {</li>
<li>    return;</li>
<li>    }</li>
<li>
</li>
<li>  vtkCamera *camera = this-&gt;Renderer-&gt;GetActiveCamera();</li>
<li>
</li>
<li>  double frac = static_cast&lt;double&gt;(this-&gt;RockIncrement) / static_cast&lt;double&gt;(this-&gt;RockLength);</li>
<li>  double az = 1.5 * cos (2.0 * 3.1415926 * (frac - floor(frac)));</li>
<li>  this-&gt;RockIncrement++;</li>
<li>  this-&gt;RockIncrement = this-&gt;RockIncrement % this-&gt;RockLength;</li>
<li>
</li>
<li>  // Move the camera</li>
<li>  camera-&gt;Azimuth(az);</li>
<li>  camera-&gt;OrthogonalizeViewUp();</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/commontk/CTK/blob/cccef11c938cc946789ddb25ccc613287a33c56e/Libs/Visualization/VTK/Widgets/ctkVTKRenderView.cpp#L166-L192" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @fpsiddiqui91 (2019-07-12 07:34 UTC)

<p>Thank you for your response, it kind of worked for me.</p>
<p>Is there any option in Slicer for dynamic update? My project needs some heavy computations which might need some time for the processing, is there any way that my module keeps on processing meanwhile user can interact in the rendering window?</p>
<p>Thank you for your help</p>

---

## Post #5 by @lassoan (2019-07-12 12:33 UTC)

<p>You can put your computation into a CLI module, which can run in the background. See a Python example here: <a href="https://github.com/lassoan/SlicerPythonCLIExample" rel="nofollow noopener">https://github.com/lassoan/SlicerPythonCLIExample</a></p>

---

## Post #6 by @fpsiddiqui91 (2019-07-12 13:50 UTC)

<p>Thank you Lassoan, This is exactly what I needed.</p>
<p>Thanks alot</p>

---

## Post #7 by @fpsiddiqui91 (2019-07-24 17:14 UTC)

<p>Hello Lassoan,</p>
<p>I am trying to impelment my own CLI module within my python script. My aim is to run my computation on CLI in the background as you have suggested.<br>
I need a guidance on it.</p>
<p>The basic workflow goes like this:</p>
<pre><code>cliNode =slicer.cli.runSync(CLItest(), parameters=param)
</code></pre>
<p>And my CLItest() class is given as:</p>
<pre><code>class CLItest(ScriptedLoadableModuleLogic):
  def logic(self):
    a = testVariables()
    for i in range(0,100):
       a.var1=a.var1+1
       print (a.var1)

print("cliTesttttt")


def name(self):
  pass


class testVariables(ScriptedLoadableModuleLogic):
    var1 = 0
</code></pre>
<p>This program will just print 0 to 100 numbers. it worked fine.</p>
<p>Now I want to give my DWI node as an input to my cli module for further processing.<br>
Can you guide me with it?</p>
<p>Are there any easy approach to do it.</p>
<p>Thanks</p>

---

## Post #8 by @lassoan (2019-07-24 20:18 UTC)

<p>Here is an example Python CLI module that does DWI processing: <a href="https://github.com/SlicerDMRI/SlicerDMRI/tree/master/Modules/CLI/ExtractDWIShells" rel="nofollow noopener">https://github.com/SlicerDMRI/SlicerDMRI/tree/master/Modules/CLI/ExtractDWIShells</a></p>

---
