# Set Main Window title to name of opened MRB file

**Topic ID**: 21304
**Date**: 2022-01-01
**URL**: https://discourse.slicer.org/t/set-main-window-title-to-name-of-opened-mrb-file/21304

---

## Post #1 by @Greydon_Gilmore (2022-01-01 22:29 UTC)

<p>Hi all,</p>
<p>I am generating scenes containing patient imaging/segmentation data, saving as MRB, and sending to our clinical team. They often have several Slicer instances opened with different MRB files loaded.</p>
<p>Is it possible to set each Slicer instance Main Window title to the name of the opened MRB file?</p>
<p>Thank you!</p>

---

## Post #2 by @rbumm (2022-01-02 16:29 UTC)

<p>Hi,</p>
<p>Two lines of python code (paste into python console for a test) can set the title of the main window:</p>
<pre><code class="lang-auto">mainWindow = slicer.util.mainWindow()
mainWindow.setWindowTitle("Your title")
</code></pre>

---

## Post #3 by @lassoan (2022-01-02 16:35 UTC)

<p>You can use <code>slicer.mrmlScene.GetURL()</code> to add the mrb file name to the window title.</p>
<p>However, since scene files are always imported (current scene content is not replaced) the mrb file name is not always an accurate description of the scene content. It might be safer to rely on what is shown in Data module or in corner annotations:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4ab6c94a48649e1b458834b3debf843912832171.jpeg" alt="image" data-base62-sha1="aEWWWeq0neP2gYqXXlqwNqp9X9f" width="572" height="471"></p>

---

## Post #4 by @Greydon_Gilmore (2022-01-02 18:19 UTC)

<p><a class="mention" href="/u/rbumm">@rbumm</a> thank you for the code snippet. I combined this with Andras’s suggestion in the <code>.slicerrc.py</code> file. The outcome is exactly what I was looking for.</p>
<pre><code class="lang-auto">import os

@vtk.calldata_type(vtk.VTK_OBJECT)
def onNodeAdded(caller, event, calldata):
	windowTitle = os.path.basename(slicer.mrmlScene.GetURL())
	mainWindow = slicer.util.mainWindow()
	mainWindow.setWindowTitle(windowTitle)

slicer.mrmlScene.AddObserver(slicer.vtkMRMLScene.NodeAddedEvent, onNodeAdded)

</code></pre>

---

## Post #5 by @lassoan (2022-01-03 14:32 UTC)

<p>Thanks for sharing your solution. Updating the window title is a very lightweight operation, so it should not matter that you do it whenever a node is added to the scene. If you just want to do something when a scene is loaded (e.g., because it is a more lengthy operation) then instead of <code>slicer.vtkMRMLScene.NodeAddedEvent</code> you can observe the <code>slicer.vtkMRMLScene.EndImportEvent</code> event instead.</p>

---

## Post #7 by @Greydon_Gilmore (2022-01-04 17:46 UTC)

<p>I’ve made the following correction in the <code>.slicerrc.py</code> file, using <code>slicer.vtkMRMLScene.EndImportEvent</code> instead:</p>
<pre><code class="lang-auto">import os

@vtk.calldata_type(vtk.VTK_OBJECT)
def onEventImportEnd(caller, event):
	windowTitle = os.path.basename(slicer.mrmlScene.GetURL())
	mainWindow = slicer.util.mainWindow()
	mainWindow.setWindowTitle(windowTitle)

slicer.mrmlScene.AddObserver(slicer.vtkMRMLScene.EndImportEvent, onEventImportEnd)
</code></pre>
<p>For completeness, how should I handle the scene close event. Currently, the Main Window title remains when the scene is closed. I would like the title to return back to default when the scene is closed. I initially was going to use <code>slicer.vtkMRMLScene.NodeRemovedEvent</code> but sense this is not the best option</p>

---

## Post #8 by @lassoan (2022-01-04 17:59 UTC)

<aside class="quote no-group" data-username="Greydon_Gilmore" data-post="7" data-topic="21304">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/greydon_gilmore/48/6863_2.png" class="avatar"> Greydon_Gilmore:</div>
<blockquote>
<p>For completeness, how should I handle the scene close event.</p>
</blockquote>
</aside>
<p>You can observe the <code>slicer.vtkMRMLScene.EndCloseEvent</code> to get notified about scene close.</p>

---

## Post #9 by @Greydon_Gilmore (2022-01-04 18:16 UTC)

<p>This is the final solution:</p>
<pre><code class="lang-auto">import os

@vtk.calldata_type(vtk.VTK_OBJECT)
def onEventImportEnd(caller, event):
	windowTitle = os.path.basename(slicer.mrmlScene.GetURL())
	mainWindow = slicer.util.mainWindow()
	mainWindow.setWindowTitle(windowTitle)

@vtk.calldata_type(vtk.VTK_OBJECT)
def onEndClose(caller, event):
	mainWindow = slicer.util.mainWindow()
	mainWindow.setWindowTitle('Slicer')

slicer.mrmlScene.AddObserver(slicer.vtkMRMLScene.EndImportEvent, onEventImportEnd)
slicer.mrmlScene.AddObserver(slicer.vtkMRMLScene.EndCloseEvent, onEndClose)
</code></pre>

---
