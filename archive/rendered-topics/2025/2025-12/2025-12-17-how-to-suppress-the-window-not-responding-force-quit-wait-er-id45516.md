---
topic_id: 45516
title: "How To Suppress The Window Not Responding Force Quit Wait Er"
date: 2025-12-17
url: https://discourse.slicer.org/t/45516
---

# How to suppress the Window not responding - force quit/wait error message in ubuntu?

**Topic ID**: 45516
**Date**: 2025-12-17
**URL**: https://discourse.slicer.org/t/how-to-suppress-the-window-not-responding-force-quit-wait-error-message-in-ubuntu/45516

---

## Post #1 by @Victor_Wayne (2025-12-17 09:04 UTC)

<p>Hello,</p>
<p>In my extension I need to add a particular number of segmentation nodes that are ellipsoidal to the scene. After adding I am transforming them to a particular point one by one.</p>
<p>But when the number of segmentation nodes that need to be added to the scene is high ubuntu throws a pop up saying “Application not responding“ with options for Force quit and Wait.</p>
<p>How can I suppress the pop up from coming up? I added:<br>
<code>StateState(vtkMRMLScene::BatchProcessState)</code></p>
<p>and</p>
<p><code>EndState(vtkMRMLScene::BatchProcessState)</code></p>
<p>In the loop where I add segmentation nodes one by one.</p>
<p>Any help will be appreciated.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @pieper (2025-12-17 17:25 UTC)

<p>You can mix in calls to:</p>
<p><code>slicer.app.processEvents(qt.QEventLoop.ExcludeUserInputEvents)</code></p>

---

## Post #3 by @Victor_Wayne (2025-12-18 04:43 UTC)

<p>Thanks for your suggestion. I am using C++. What is the correct equivalent C++ code for this? And I found out that I can use worker threads to not block the main thread and I also found out that it is not recommended to read, write, delete a MRML node or to add a MRML node to the scene from a worker thread. In my case there is not a lot of heavy, raw computation that doesn’t involve a node. I just create a rotation matrix based on the trajectory I am placing my node on and then for every segmentation node I get the point on that trajectory I create a transformation matrix for that node using the point and the trajectory and then apply the transformation there. Is there any way to do this using worker threads to block the main thread? Because I feel like processEvent is a hack. Is it not? I could be wrong. Do you have suggestions/input on worker threads?</p>

---

## Post #4 by @pieper (2025-12-18 13:29 UTC)

<p>You can look in the Slicer source code to find the application instance for the GUI code and call the same method.  Basically that processEvents call is like flushing stdout to provide feedback to the user without getting any new callbacks, so it’s safe and not really a hack at all.</p>
<p>You can do some processing in threads but the vtk and qt layers are not reentrant, so you have to be careful.  Doing operations on the scene in small chunks and providing feedback to the user is a good way to manage bulk operations in the context of an interactive application.</p>

---

## Post #5 by @Victor_Wayne (2025-12-18 14:48 UTC)

<p>Thank you so much for your reply.</p>
<aside class="quote no-group" data-username="pieper" data-post="4" data-topic="45516">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Doing operations on the scene in small chunks and providing feedback to the user is a good way to manage bulk operations in the context of an interactive application.</p>
</blockquote>
</aside>
<p>Can you please elaborate on this? Are you suggesting me to do these small chunks of operations in a worker thread?</p>

---

## Post #6 by @pieper (2025-12-18 23:06 UTC)

<p>What I mean is that you can process events each time you add a segmentation node, and they will be rendered as they are ready.  If you don’t include the flag to ignore user events and you are adding things in small increments, then people also be interacting with the application as the data is being applied (be careful to disable any GUI elements that could lead to an event loop, say by re-triggering addition of segmentation nodes).  If each one is lightweight enough the updates can be smooth and you don’t need another thread.  But you can use another thread if you have heavy processing to do, but you need to only operate on the GUI, as in add to the mrml scene, from the main thread.</p>

---
