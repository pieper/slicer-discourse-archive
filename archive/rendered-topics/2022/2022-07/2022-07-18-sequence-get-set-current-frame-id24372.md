# Sequence Get & Set Current Frame

**Topic ID**: 24372
**Date**: 2022-07-18
**URL**: https://discourse.slicer.org/t/sequence-get-set-current-frame/24372

---

## Post #1 by @connorh (2022-07-18 15:01 UTC)

<p>I’m trying to get and set the current ‘frame’ (timepoint) of a vtkMRMLSequenceBrowserNode in python.</p>
<p>I can use <code>browserNode.SelectNextItem(0)</code> to get the current frame without error, but then following that when playing the sequence using default sequence playback tools, I repeatedly get the error in the python interactor <code>TypeError: observe_me() takes 0 positional arguments but 2 were given</code>.</p>
<p>Is there an alternative way to get and set a vtkMRMLSequenceBrowserNode current frame without creating an observer? Or am I doing something else wrong to give me this error?</p>
<p>My sequence browser is observing 2 synchronized sequence nodes (using <code>sequenceBrowser.AddSynchronizedSequenceNodeID()</code>), if this matters.</p>

---

## Post #2 by @connorh (2022-07-25 16:04 UTC)

<p>I was able to get and set the frame/timepoint using the following, and did not get any errors</p>
<pre><code class="lang-auto">#Get current frame
current_frame = browserNode.GetSelectedItemNumber()
#Set frame 
new_frame = 5
browserNode.SetSelectedItemNumber(new_frame)
</code></pre>

---
