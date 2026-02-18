# Set the spin speed in 3D view

**Topic ID**: 1273
**Date**: 2017-10-24
**URL**: https://discourse.slicer.org/t/set-the-spin-speed-in-3d-view/1273

---

## Post #1 by @doc-xie (2017-10-24 13:14 UTC)

<p>Hello everyone!<br>
Could the spin speed of the 3D view be set manually?<br>
In the Edit–Application settings–unit,set the value in frequency and velocity,there is not a little change about the spin speed.<br>
Thanks!</p>

---

## Post #2 by @pieper (2017-10-24 19:12 UTC)

<p>There’s no real direct control because the per-frame render time depends on the complexity of the scene.</p>
<p>You can manually adjust the delay between animation steps by doing something like this in python:</p>
<pre><code class="lang-auto">v = getNode('View1')
v.SetAnimationMs(2000)
</code></pre>
<p>it will work to slow it down, but not really to speed things up.  There are other controls you might want to play with:</p>
<p><a href="http://apidocs.slicer.org/master/classvtkMRMLViewNode.html" class="onebox" target="_blank">http://apidocs.slicer.org/master/classvtkMRMLViewNode.html</a></p>

---

## Post #3 by @lassoan (2017-10-24 21:08 UTC)

<p>I think there is a step size that you can adjust to make the animation go faster (by skipping more).</p>
<p>If you need very high quality rendering and fast spin speed then you can record the spinning animation into a video file using ScreenCapture module.</p>

---

## Post #4 by @doc-xie (2017-10-26 07:15 UTC)

<p>Thanks!<br>
I should set the spin speed with the third part sofeware or ScreenCapture module!<br>
Best,<br>
Doc-xie.</p>

---

## Post #5 by @doc-xie (2017-10-26 07:19 UTC)

<p>Thanks a lot,Professor Steve!<br>
The spin speed can be set with the third-party software or the ScreenCapture module basing on the advice Professor Lassoan tought me.<br>
Have a good weekend!<br>
Doc-xie!</p>

---
