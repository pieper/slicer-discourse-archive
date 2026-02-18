# Segment surface calculation

**Topic ID**: 35655
**Date**: 2024-04-22
**URL**: https://discourse.slicer.org/t/segment-surface-calculation/35655

---

## Post #1 by @FraP (2024-04-22 10:28 UTC)

<p>I am using this script to determine the volume and surface area of my segments.</p>
<pre><code class="lang-auto">segmentationNode = getNode("Segmentation")

# Compute segment statistics
import SegmentStatistics
segStatLogic = SegmentStatistics.SegmentStatisticsLogic()
segStatLogic.getParameterNode().SetParameter("Segmentation", segmentationNode.GetID())
segStatLogic.computeStatistics()
stats = segStatLogic.getStatistics()

# Display volume and surface area of each segment
for segmentId in stats["SegmentIDs"]:
  volume_mm3 = stats[segmentId,"LabelmapSegmentStatisticsPlugin.volume_mm3"]
  surface_mm2 = stats[segmentId, "ClosedSurfaceSegmentStatisticsPlugin.surface_mm2"]
  segmentName = segmentationNode.GetSegmentation().GetSegment(segmentId).GetName()
  print(f"{segmentName} volume = {volume_mm3} mm3")
  print(f"{segmentName} volume = {surface_mm2} mm2")
</code></pre>
<p>The script works fine when the segments are displayed in 3D, but it works only for the volume when the 3D view is off.<br>
When I have too large or complex volume/segments, I cannot display them in 3D because I get this error:</p>
<blockquote>
<p>“Slicer has caught an application error, please save your work and restart.\n\nThe application has run out of memory. Increasing virtual memory size in system settings or adding more RAM may fix this issue.\n\nIf you have a repeatable sequence of steps that causes this message, please report the issue following instructions available at <a href="https://slicer.org" rel="noopener nofollow ugc">https://slicer.org</a>\n\n\nThe message detail is:\n\nException thrown in event: bad array new length”</p>
</blockquote>
<p>I guess the files are too complex for my computer and there is not much I can do about it. Although it is strange because this computer has 192 GB of RAM.</p>
<p>Is there another way to determinate the surface of the segments avoiding 3D visualization?</p>

---

## Post #2 by @cpinter (2024-04-22 13:18 UTC)

<p>What size is the input? Just curious why 192 GB is not enough.</p>
<p>I’m not sure if this helps, but there is a new conversion method to closed surface, which may (not sure!) use less memory. You can enable it like this:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14f6f37d5437898aa9c2533c42a0e5ca4d78e164.png" alt="image" data-base62-sha1="2ZsDFgs30xIT0FRIORz53Z6MQFC" width="443" height="122"></p>

---

## Post #3 by @FraP (2024-04-22 13:49 UTC)

<p>The volume I’m currently working with is a 1.4 GB .vtk file.<br>
The more simple segments are displayed correctly in 3D. But I have a large and perhaps more complex one that cannot be displayed (even if segmented alone).<br>
It is also strange that only about 50GB of RAM are in use when I get the error.</p>
<p>I tried the method you suggested but it only allows a small part of the volume to be displayed and then stops, but no error is shown.</p>

---

## Post #4 by @cpinter (2024-04-22 13:52 UTC)

<p>I assume that the segment in question is not a single object, but maybe a set of disconnected and complex features. In that case calculating the surface may not even make sense. If you don’t insist on calculating the surface area of that segment, I suggest making a clone of the segmentation, removing that segment, and run the calculations on all the other segments.</p>

---
