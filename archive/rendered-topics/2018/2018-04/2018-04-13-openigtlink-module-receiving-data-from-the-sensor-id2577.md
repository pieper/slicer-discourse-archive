---
topic_id: 2577
title: "Openigtlink Module Receiving Data From The Sensor"
date: 2018-04-13
url: https://discourse.slicer.org/t/2577
---

# OpenIGTLink module receiving data from the sensor

**Topic ID**: 2577
**Date**: 2018-04-13
**URL**: https://discourse.slicer.org/t/openigtlink-module-receiving-data-from-the-sensor/2577

---

## Post #1 by @wpgao (2018-04-13 03:07 UTC)

<p>Hi all,</p>
<p>How to obtain the message with a complicate data structure, such as head info plus two 4x4 matrices, sent from the sensor via network using openIGTLink?<br>
Many thanks!</p>
<p>Operating system: win 7<br>
Slicer version: 4.8.1<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @ungi (2018-04-13 15:17 UTC)

<p>Hi,</p>
<p>Create an OpenIGTLink connector in the OpenIGTLinkIF module. Find it under the IGT category in the modules list. If you activate the connection, it will automatically generate a transform node in the Slicer scene, and update it any time it receives a new OpenIGTLink message with the same device name.<br>
You may find useful related information in these tutorials: <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="nofollow noopener">http://www.slicerigt.org/wp/user-tutorial/</a></p>
<p>Tamas</p>

---

## Post #3 by @wpgao (2018-04-16 02:45 UTC)

<aside class="quote no-group" data-username="ungi" data-post="2" data-topic="2577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ungi/48/78573_2.png" class="avatar"> ungi:</div>
<blockquote>
<p>nIGTLink</p>
</blockquote>
</aside>
<p>Hi Tamas,</p>
<p>Thanks for your help! In my application, there are two EM sensors embedded in a flexible instrument. There is a standalone software in charge of communication with the EM sensors and sent a message containing the two 4x4 matrices derived from two sensors to 3D Slicer (server). I have tried to create an OpenIGTLink connector, and it does work. But it can not be obtained from vtkMRMLLinearTransformNode, because there are two matrices in a message are sent to 3D Slicer. So can you give me some advice how to get this message, or any examples?<br>
Thanks again!</p>
<p>Wenpeng</p>

---

## Post #4 by @lassoan (2018-04-16 03:15 UTC)

<p><a class="mention" href="/u/wpgao">@wpgao</a> What EM tracker do you use?</p>

---

## Post #5 by @wpgao (2018-04-16 03:56 UTC)

<p>Hi Lassoan,</p>
<p>We use NDI aurora v2. Two 5DOF sensors were embedded in a flexible instrument!<br>
We want to show the pose (orientation and position) of two sensors in 3D slicer!</p>
<p>Wenpeng</p>

---

## Post #6 by @lassoan (2018-04-16 14:23 UTC)

<p>Then you can simply use <a href="http://www.plustoolkit.org">Plus toolkit</a> to interface with your hardware. It is extensively tested to work well with Slicer.</p>

---

## Post #7 by @wpgao (2018-04-17 02:51 UTC)

<p>Hi Lasso,</p>
<p>Thanks for your help!<br>
Is there any advice on how to develop a module to receive the data sent from the API provided by NDI (we have source code and modify it as a client using OpenIGTLink lib)</p>
<p>Wenpeng</p>

---

## Post #8 by @lassoan (2018-04-17 03:17 UTC)

<p>No need to develop any module. You can use Plus Server for connecting NDI tracker and broadcast data through OpenIGTLink. OpenIGTLinkIF module in Slicer can connect to Plus Server, receive transforms and update corresponding transforms in the scene in real-time. See <a href="http://www.slicerigt.org/wp/user-tutorial/">SlicerIGT tutorials</a> for step-by-step instructions.</p>

---

## Post #9 by @wpgao (2018-04-21 09:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="2577">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>step-by-step instructions.</p>
</blockquote>
</aside>
<p>thanks for your help!</p>

---
