---
topic_id: 2930
title: "Read Position From Txt File"
date: 2018-05-25
url: https://discourse.slicer.org/t/2930
---

# Read position from txt file

**Topic ID**: 2930
**Date**: 2018-05-25
**URL**: https://discourse.slicer.org/t/read-position-from-txt-file/2930

---

## Post #1 by @val.dil (2018-05-25 11:51 UTC)

<p>Hello everybody,<br>
I want to develop a system that read a position from a file in real time, through OpenIGTlink, and send it to the Slicer.<br>
The file has to be read at the same time that it is modified. I found a node “vtkMRMLStorableNode::GetModifiedSinceRead()” that do this, but it works in real time and with openigtlink?<br>
Do you think that it’s better and easier to implement a thread for the writing-reading-sending process?<br>
Thanks for your helping.</p>

---

## Post #2 by @lassoan (2018-05-25 12:45 UTC)

<p><a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ApplicationPlusServer.html">PlusServer application</a> in <a href="http://www.plustoolkit.org">Plus toolkit</a> can already read positions and orientations (and images) from <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/FileSequenceFile.html">text files</a> and send them to Slicer through OpenIGTLink. No need to develop any new software for this. PlusServer can also connect to real hardware (tracking system, sensors, imaging devices, etc).</p>

---

## Post #3 by @val.dil (2018-05-25 14:01 UTC)

<p>I don’t think that i can use PlusServer app, because my device is not compatible with it.</p>

---

## Post #4 by @lassoan (2018-05-25 16:14 UTC)

<p>What device do you have? You can either add support for your device (more learning, less coding), or implement a PlusServer clone that can communicate with your device and send OpenIGTLink messages to Slicer.</p>

---

## Post #5 by @val.dil (2018-05-26 16:29 UTC)

<p>Actually, I already develop a c++ code that acquire the position from the device and save it on a file, so i just want to find an optimal way to transfer this position on 3Dslicer. Do you think that i should implement a thread?<br>
However, as a second way, your suggestion is very interesting. Can you please give me more information about that?<br>
Thanks for your helping.</p>

---

## Post #6 by @lassoan (2018-05-26 18:22 UTC)

<p>Follow examples in OpenIGTLink library for creating a simple server or client that sends tracking data. Slicer can connect to that using OpenIGTLinkIF module and takes care of multithreading and real-time scene updates.</p>

---
