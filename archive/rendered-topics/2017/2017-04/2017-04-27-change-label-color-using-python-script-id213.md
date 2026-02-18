# Change label color using python script

**Topic ID**: 213
**Date**: 2017-04-27
**URL**: https://discourse.slicer.org/t/change-label-color-using-python-script/213

---

## Post #1 by @brhoom (2017-04-27 13:48 UTC)

<p>Dear all,</p>
<p>how can I combine all the colors in the “label” image to one color using python script.</p>
<p>Thanks</p>
<p>IIbraheem</p>

---

## Post #2 by @lassoan (2017-04-27 14:06 UTC)

<p>Get the image data from the labelmap volume node, and apply <a href="http://www.vtk.org/doc/nightly/html/classvtkImageThreshold.html">vtkImageThreshold</a> filter.</p>

---

## Post #3 by @brhoom (2017-04-27 18:58 UTC)

<p>Thanks Andras. I will try this. I thought there maybe an easier way by using the “ChangeLabelEffect” from the editor module.</p>

---

## Post #4 by @lassoan (2017-04-27 19:18 UTC)

<p>If you want to modify labels from your own script then manipulating the voxels using numpy is probably the simplest. For example, to change all non-zero voxels to 2:</p>
<pre><code>a = slicer.util.array('Output Volume-label')
a[a&gt;0] = 2
</code></pre>
<p>Using the vtkImageThreshold filter would be about 5-6 lines.</p>
<p>If you manipulate segmentations using GUI then I would recommend to use Segment Editor module instead of the old, relatively limited Editor module.</p>

---

## Post #5 by @brhoom (2017-04-27 19:39 UTC)

<p>Thanks for the tips. I think numpy is the fastest way to do this. Could you please share how to write the array back to the volume?<br>
<code>lb= slicer.util.getNode('input-label')</code><br>
<code>lbd = lb.GetImageData()</code><br>
<code>lbd[lbd&gt;0] = 2</code><br>
I can not find sothomig like<br>
<code>lb.SettImageData(lbd)</code></p>

---

## Post #6 by @brhoom (2017-04-27 19:45 UTC)

<p>found it <img src="https://emoji.discourse-cdn.com/twitter/grin.png?v=5" title=":grin:" class="emoji" alt=":grin:"><br>
I forgot to update the dispaly.<br>
these commands are enough:<br>
<code>lb= slicer.util.getNode('input-label')</code><br>
<code>lb[lb&gt;0] = 2</code></p>

---

## Post #7 by @pieper (2017-04-27 21:23 UTC)

<p>Yes, if you just toggle the slice slider the update volume will show up.</p>
<p>But if you want to do it automatically from a script you need to inform VTK/Slicer that numpy has changed the binary data so it will render automatically.</p>
<p>So you need something like this to trigger a redraw</p>
<pre><code class="lang-auto">a = slicer.util.array('Output Volume-label')
a[a&gt;0] = 2
node = slicer.util.getNode('Output Volume-label')
node.GetImageData().GetPointData().GetScalars().Modified()
node.Modified()
</code></pre>

---

## Post #8 by @brhoom (2017-04-28 21:08 UTC)

<p>many thanks for the code.  It helps a lot.</p>

---
