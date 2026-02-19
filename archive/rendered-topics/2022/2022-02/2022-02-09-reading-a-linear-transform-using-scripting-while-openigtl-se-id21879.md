---
topic_id: 21879
title: "Reading A Linear Transform Using Scripting While Openigtl Se"
date: 2022-02-09
url: https://discourse.slicer.org/t/21879
---

# Reading a Linear Transform using scripting while openigtl server keeps sending transform messages

**Topic ID**: 21879
**Date**: 2022-02-09
**URL**: https://discourse.slicer.org/t/reading-a-linear-transform-using-scripting-while-openigtl-server-keeps-sending-transform-messages/21879

---

## Post #1 by @srivastavava (2022-02-09 20:19 UTC)

<p>Hi,<br>
I have a linear transform that I receive from a OpenIGTL Server. I am using the openigtlinkIF module to receive this transform in 3d slicer. I want to read the transform message and place a fiducial by extracting the RAS coordinates from the linear message. Can someone please help me with the script to perform the reading of the transform and placement of the fiducial while I’m receiving the transforms in realt time ?</p>

---

## Post #2 by @lassoan (2022-02-09 23:01 UTC)

<p>This feature is already implemented in several modules. For example:</p>
<ul>
<li>there is a C++ module in SlicerIGT extension - <code>Collect Points</code> - that does exactly what you describe: record transforms into fiducials</li>
<li>if you want to reconstruct catheter paths from tracking sensors then you can use <a href="https://github.com/SlicerIGT/SlicerPathReconstruction">PathReconstruction extension</a>
</li>
<li>if you want to record and analyze hand and tool motion, you can use <a href="http://perktutor.org/">Perk Tutor extension</a>
</li>
<li>if you just need a simple example of how to collect points and display the results in real-time then you can have a look at <a href="https://github.com/SlicerIGT/SlicerTrackingErrorInspector/blob/master/TrackingErrorMapping/TrackingErrorMapping.py">TrackingErrorMapping module</a> in TrackingErrorInspector extension</li>
</ul>

---

## Post #3 by @srivastavava (2022-02-11 14:57 UTC)

<p>Thank you, Andras… to that… if I want to extend the functionality to view these markup fiducials in slice views in real time, how should I go about it ?</p>

---

## Post #4 by @lassoan (2022-02-11 15:31 UTC)

<p>As you can see from these many examples, everything is very flexible, customizable, extensible. What functionality would you like to add?</p>

---
