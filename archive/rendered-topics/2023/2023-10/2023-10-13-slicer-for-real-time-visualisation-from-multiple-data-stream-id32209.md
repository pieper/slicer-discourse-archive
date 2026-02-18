# Slicer for real-time visualisation from multiple data streams and sending control commands

**Topic ID**: 32209
**Date**: 2023-10-13
**URL**: https://discourse.slicer.org/t/slicer-for-real-time-visualisation-from-multiple-data-streams-and-sending-control-commands/32209

---

## Post #1 by @heiko (2023-10-13 13:10 UTC)

<p>Hi everybody,</p>
<p>I am aware this question is quite broad, apology for that. I am planning to have a graphical user interface. The main purposes would be to pull data from multiple sources (X-Ray, some electric circuitry, …) and to visualize this in 2D/3D visualisations <strong>in real time</strong>. Furthermore, I want to be able to send control commands to e.g. my electric circuitry, based on user button clicks or evaluations of the incoming data. I am currently trying to decide whether to build my own GUI (e.g. based on QT, pyVista, …) or whether it would be worth to implement such functionality in a Slicer Module. Benefits of Slicer would be that a lot of the functionality, like visualizing 3D modules, potentially also DICOM, and postprocessing of the data etc are conveniently available. For this, I wanted to ask whether there is a considerable overhead when using Slicer to pull realtime data and visualize it, compared to implementing a lightweight GUI? I do need to run the code and analysis of the data in real time, so I was wondering if having slicer as basis would take away a big chunk of computational resources. Would you generally recommend Slicer for the described scenario?</p>
<p>I would appreciate any input or experiences on this.<br>
Thanks a lot!</p>

---

## Post #2 by @pieper (2023-10-13 13:42 UTC)

<p>Yes, Slicer is designed to work well as a platform for real time work.  If your application requires real-time performance, like robot motor control or processing live data streams you probably want to have dedicated processes that communicate with the Slicer interface asynchronously, like is done in PLUS and SlicerROS2.</p>
<p>While it’s possible to reimplement Slicer features (or even just a subset of them) it will be a lot of work to develop and maintain.</p>

---

## Post #3 by @heiko (2023-10-13 13:54 UTC)

<p>Hi Steve,<br>
thanks a lot for the quick reply! We would definitely go for an asynchronous communication interface, as you recommended.</p>
<p>How much freedom does slicer offer in case I want to add visualizations that are not among the default ones? Let’s assume I have an stl and I want to change the surface colors of different triangles in realtime according to outputs of the analysis algorithsm, or similar things. (This is just an example - at this point we have not defined all potential visualizations we might need). I assume this would well be possible, but I am not terribly familiar with the API yet; are there boundaries of the visualization where I might run into a dead-end when committing to slicer?</p>

---

## Post #4 by @lassoan (2023-10-13 13:59 UTC)

<p>All the features you described are already implemented in Slicer + SlicerIGT extension + Plus toolkit. For complex real-time control ROS2 can be useful but for simpler cases (communicate with an Arduino) you can use the serial port interface (if the device is connected to the Slicer computer then you can use SlicerArduino extension, if it is a different computer then you can use Plus Server).</p>
<aside class="quote no-group quote-modified" data-username="heiko" data-post="3" data-topic="32209">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/7ab992/48.png" class="avatar"> heiko:</div>
<blockquote>
<p>How much freedom does slicer offer in case I want to add visualizations that are not among the default ones? Let’s assume I have an stl and I want to change the surface colors of different triangles in realtime according to outputs of the analysis algorithsm, or similar things. I assume this would well be possible, but I am not terribly familiar with the API yet; are there boundaries of the visualization where I might run into a dead-end when committing to slicer?</p>
</blockquote>
</aside>
<p>You can do everything with Slicer as you could do with PyVista (=VTK), as Slicer uses VTK for visualization and it makes all VTK features are available for developers to use in their modules. The advantage of using Slicer vs. starting from scratch is that thousands of features are already implemented, so you don’t need to waste your time with reimplementing those and you can focus on working on what is unique in your system.</p>

---

## Post #5 by @heiko (2023-10-13 14:49 UTC)

<p>Thanks for the clarification, <a class="mention" href="/u/lassoan">@lassoan</a> !</p>
<blockquote>
<p>makes all VTK features are available for developers to use in their modules</p>
</blockquote>
<p>as far as I understand from browsing the forum, this means I can also call the VTK features using Python, correct? Or will there be functionality only exposed in C/C++?</p>

---

## Post #6 by @lassoan (2023-10-13 14:54 UTC)

<p>Yes, you can call all VTK functions from either Python or C++.</p>

---

## Post #7 by @heiko (2023-10-16 14:21 UTC)

<p>Thank you, that covers all questions I had <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
