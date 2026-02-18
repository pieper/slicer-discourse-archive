# Error when using Endoscopy module

**Topic ID**: 2286
**Date**: 2018-03-11
**URL**: https://discourse.slicer.org/t/error-when-using-endoscopy-module/2286

---

## Post #1 by @hherhold (2018-03-11 13:22 UTC)

<p>Hi,</p>
<p>Getting an error when using Endoscopy module in master build. I loaded in a volume, and through various manipulations, wound up with about 7 default cameras. I went in to “Data” and deleted all but one default camera, and then added 7 fiducials along the desired path. When I hit “Create path”, I get this in the console:</p>
<pre><code>Calculating Path...
Traceback (most recent call last):
  File "/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-scripted-modules/Endoscopy.py", line 220, in onCreatePathButtonClicked
    result = EndoscopyComputePath(fiducialsNode)
  File "/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-scripted-modules/Endoscopy.py", line 387, in __init__
    self.calculatePath()
  File "/Users/hherhold/Development/slicer/build-qt5/Slicer-build/lib/Slicer-4.9/qt-scripted-modules/Endoscopy.py", line 407, in calculatePath
    t, p, remainder = self.step(segment, t, remainder)
TypeError: 'NoneType' object is not iterable
</code></pre>
<p>I’ve had my misunderstandings about how to use cameras and the Endoscopy module before so it’s likely I’m just doing something wrong. But if it’s an actual bug, I’m happy to help debug and fix if someone (<a class="mention" href="/u/pieper">@pieper</a>?) can point me in the right direction.</p>
<p>Thanks!!!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2018-03-11 17:38 UTC)

<p>Unfortunately, currently a new camera node is created each time you load the scene (current camera node does not get overwritten but a new one is created). The Endoscopy module probably only determines the camera node at the beginning and does not update it later. I would not recommend to delete camera nodes to reduce chances of errors.</p>
<p>Screen capture module could be used by recording camera motion to a sequence and then use sequence animation mode in ScreenCapture module. However, there is a problem with clipping range update during replay</p>
<p>I’ll try to find some time later this week to make camera handling a bit more robust.</p>

---

## Post #3 by @lassoan (2018-03-12 00:02 UTC)

<p>I’ve fixed most important issues with the camera node clipping range updates and recording/playback in sequences. It should all work in tomorrow’s nightly build.</p>
<p>Set up recording of camera node changes to a sequence:</p>
<ul>
<li>Go to Sequence browser module</li>
<li>Click the <code>+</code> button to create a new sequence</li>
<li>Select <code>Default Camera Node</code> as <code>Proxy node</code> in the table</li>
</ul>
<p>Record camera motion:</p>
<ul>
<li>Hit record button (red circle) to start recording</li>
<li>Go to Endoscopy module, play a complete fly-through</li>
<li>Hit record button to stop recording</li>
<li>You can use playback controls (play/pause, slider, etc.) on the toolbar to verify the recording</li>
</ul>
<p>Create video file of the fly-through:</p>
<ul>
<li>Go to Screen Capture module</li>
<li>Select <code>sequence</code> as Animation mode</li>
<li>Select sequence browser node</li>
<li>Check <code>Video export</code>
</li>
<li>Click <code>Capture</code>
</li>
</ul>

---

## Post #4 by @nirotu (2018-03-13 14:56 UTC)

<p>Hi Andras:</p>
<p>I am interested in endoscopy module to do a fly-through vessel. I was not able to run the endoscopy module. BTW, is it possible for you to create a youtube presentation showing how to perform fly-through a vessel or airways?</p>
<p>thank you,</p>
<p>A</p>

---
