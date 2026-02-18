# Synchronize display scale across slice viewers

**Topic ID**: 4547
**Date**: 2018-10-26
**URL**: https://discourse.slicer.org/t/synchronize-display-scale-across-slice-viewers/4547

---

## Post #1 by @stephan (2018-10-26 17:59 UTC)

<p>Hi,<br>
is there a quick way to synchronize the zoom factor across slice viewers?<br>
Thanks<br>
Stephan</p>

---

## Post #2 by @lassoan (2018-10-26 21:44 UTC)

<p>Yes. Long-click on slice view link icon and enable hot-linking. Maybe it only synchronizes views that have the same orientation. If this is the case then you may need to write a few-line Python script that observes zoom factor changes in slice views and adjusts zoom factor in all the others.</p>

---

## Post #3 by @stephan (2018-10-29 19:34 UTC)

<p>Hi Andras,</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="4547">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe it only synchronizes views that have the same orientation.</p>
</blockquote>
</aside>
<p>Yes, that is correct.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="4547">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If this is the case then you may need to write a few-line Python script that observes zoom factor changes in slice views and adjusts zoom factor in all the others.</p>
</blockquote>
</aside>
<p>Unfortunately, this is literally the first time ever I opened the Python interactor. But at least, some googling brought me this far, and it does what I want it to</p>
<pre><code>redSlice = slicer.app.layoutManager().sliceWidget('Red').mrmlSliceNode()
yellowSlice = slicer.app.layoutManager().sliceWidget('Yellow').mrmlSliceNode()

redFOV = redSlice.GetFieldOfView()
yellowSlice.SetFieldOfView(redFOV[0], redFOV[1], redFOV[2])
</code></pre>
<p>However, it would be nice to not always have to call the zoom alignment manually. Is there some zoom change event to hook an observer to (in <a href="https://www.vtk.org/doc/nightly/html/classvtkCommand.html" rel="noopener nofollow ugc">vtkCommand</a> I could not find something that looked very promising, but maybe I just missed it)?</p>
<p>Thank you<br>
Stephan</p>

---

## Post #4 by @lassoan (2018-11-01 02:35 UTC)

<p>Nice work! I’ve extended your example with slice node observers, which update field of view in all other slice nodes automatically when a slice node is changed: see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Synchronize_zoom_factor_between_slice_views">complete script here</a>.</p>

---

## Post #5 by @stephan (2018-11-01 14:24 UTC)

<p>Great, thank you <a class="mention" href="/u/lassoan">@lassoan</a> . That’s exactly what I was looking for.</p>
<p>I just added a tiny bit of additional functionality, namely to toggle zoomSync on and off.</p>
<pre><code>slicer.updatingSliceNodes = False
slicer.zoomSync = False

slicer.sliceNodes = [slicer.app.layoutManager().sliceWidget(viewName).mrmlSliceNode()
    for viewName in slicer.app.layoutManager().sliceViewNames()]

def sliceModified(caller, event):
    if slicer.updatingSliceNodes:
        # prevent infinite loop of slice node updates triggering slice node updates
        return
    slicer.updatingSliceNodes = True
    fov = caller.GetFieldOfView()
    for sliceNode in slicer.sliceNodes:
        if sliceNode != caller:
            sliceNode.SetFieldOfView(*fov)
    slicer.updatingSliceNodes = False

def toggleZoomSync():
    if slicer.zoomSync: 
        # zoom sync is on already, therefore observer function is alread hooked, should be unhooked
        for sliceNode in slicer.sliceNodes:
            sliceNode.RemoveObserver(sliceNode.zoomChangeObserverTag)
        slicer.zoomSync = False
    else: 
        # zoom sync is off --&gt; toogle to on (register observer function)
        for sliceNode in slicer.sliceNodes:
            sliceNode.zoomChangeObserverTag = sliceNode.AddObserver(vtk.vtkCommand.ModifiedEvent, sliceModified)
        slicer.zoomSync = True

toggleZoomSync()
</code></pre>
<p>After running this code snippet once, calls to</p>
<p><code>toggleZoomSync()</code></p>
<p>toggle slice zoom synchronization on/off.</p>

---
