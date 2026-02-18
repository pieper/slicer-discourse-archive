# Slowness when calling SetBackgroundVolumeID() to show data in Yellow slice view

**Topic ID**: 29258
**Date**: 2023-05-02
**URL**: https://discourse.slicer.org/t/slowness-when-calling-setbackgroundvolumeid-to-show-data-in-yellow-slice-view/29258

---

## Post #1 by @Mubariz_Afzal (2023-05-02 19:29 UTC)

<p>Hi all,</p>
<p>We are working on an extension to 3D Slicer that often uses a large number of small images (&gt;100). However I came across some consistent slowness that is seen when using the  <code>SetBackgroundVolumeID()</code> function. I was able to create some Python code that can replicate the problem using a small PNG image.</p>
<pre><code class="lang-auto">import time

# Import lots of data
for i in range(200):
  slicer.util.loadVolume("/path/to/test.png")

layoutManager = slicer.app.layoutManager()
shNode = slicer.mrmlScene.GetSubjectHierarchyNode()

# Get ids of loaded data
dataIDs = []
shNode.GetItemChildren(shNode.GetSceneItemID(), dataIDs)

# Fuction to time duration of SetBackgroundVolumeID() call
def timeFunction(colour, dataID):
  sliceWidget = layoutManager.sliceWidget(colour)
  compositeNode = sliceWidget.mrmlSliceCompositeNode()

  print(f"Slice orientation: {sliceWidget.sliceOrientation}")

  s = time.time()
  compositeNode.SetBackgroundVolumeID(str(dataID))
  e = time.time()

  timeElapsed = e - s
  print(f"Time to call SetBackgroundVolumeID(): {timeElapsed}")

  return timeElapsed

# Code to determine the average time per each slice view
yellowTimes = []
greenTimes = []
redTimes = []

for id in dataIDs:
  yellowTimes.append(timeFunction("Yellow", id))
  greenTimes.append(timeFunction("Green", id))
  redTimes.append(timeFunction("Red", id))

print(f"Average time to call SetBackgroundVolumeID() for yellow slice view: {sum(yellowTimes) / len(yellowTimes)}")
print(f"Average time to call SetBackgroundVolumeID() for green slice view: {sum(greenTimes) / len(greenTimes)}")
print(f"Average time to call SetBackgroundVolumeID() for red view: {sum(redTimes) / len(redTimes)}")

</code></pre>
<p>I found the following results:</p>
<p>200 images</p>
<blockquote>
<p>Average time to call SetBackgroundVolumeID() for yellow slice view: 0.016587159633636474<br>
Average time to call SetBackgroundVolumeID() for green slice view: 0.0006015706062316895<br>
Average time to call SetBackgroundVolumeID() for red view: 0.0005157172679901123</p>
</blockquote>
<p>1000  images</p>
<blockquote>
<p>Average time to call SetBackgroundVolumeID() for yellow slice view: 0.3258379149436951<br>
Average time to call SetBackgroundVolumeID() for green slice view: 0.0015380308628082276<br>
Average time to call SetBackgroundVolumeID() for red view: 0.0014937591552734374</p>
</blockquote>
<p>The slowness can be quite noticeable when 500+ images are loaded. It wouldn’t be an issue if the speed was the same across each slice view but the Yellow slice view seems to slow at greater rate than the other slice views. Would anyone be able to help debug this? Thank you!</p>
<p>test.png<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/c/2ca24e315dc4f0508c2d366fcbf3d90bd41e2f61.png" alt="test" data-base62-sha1="6mQKhyx3ned0NZBj5ygUzNlFeuZ" width="402" height="368"></p>

---

## Post #2 by @lassoan (2023-05-02 19:34 UTC)

<p>We usually don’t store this many volume nodes in the scene, but put them in a sequence. You can then recall them from the sequence as needed (each sequence browser node can show one volume of the sequence).</p>
<p>If you work with video recording then you can save and replay with lossy video compression using IGSIO extension, which can further improve speed and storage space usage.</p>

---
