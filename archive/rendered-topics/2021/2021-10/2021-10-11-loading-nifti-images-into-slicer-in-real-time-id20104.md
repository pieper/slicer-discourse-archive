# Loading nifti images into slicer in real time

**Topic ID**: 20104
**Date**: 2021-10-11
**URL**: https://discourse.slicer.org/t/loading-nifti-images-into-slicer-in-real-time/20104

---

## Post #1 by @saikatsengupta (2021-10-11 19:12 UTC)

<p>Hello,<br>
I am new to slicer and am just getting familiar with this powerful software. A big thanks to all who developed this and continue to support it.</p>
<p>I am working on a problem where I need to visualize images in slicer in ‘real time’ ie as they are coming in from a scanner. The images are being dropped into a local folder as nifti files.  I need to load the newest image automatically into slicer as it comes in. Is there a way to do this ?</p>
<p>Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-10-11 19:40 UTC)

<p>You would normally use <a href="http://openigtlink.org">OpenIGTLink protocol</a> for real-time image streaming from scanners. What software do you use for image acquisition, from what hardware?</p>
<p>Uncompressed nifti file reading could be quite fast, too, but polling the file system for changes might be difficult at high frame rates.</p>

---

## Post #3 by @pieper (2021-10-11 19:56 UTC)

<p>OpenIGTLink would be a good options, but depending on your OS a file system watcher can be efficient.</p>
<p><a href="https://doc.qt.io/qt-5/qfilesystemwatcher.html" class="onebox" target="_blank" rel="noopener">https://doc.qt.io/qt-5/qfilesystemwatcher.html</a></p>
<p>Another option is <a href="https://github.com/pieper/SlicerWeb">SlicerWeb</a> where there is a rest endpoint for <code>POST</code>ing a nrrd file directly into a volume node, and that could be extended to handle nii as well.</p>

---

## Post #4 by @saikatsengupta (2021-10-11 21:00 UTC)

<p>Thanks for your response, Andras. We are using a Philips MRI scanner and use Philips XTC protocol to get images in real time. Frame rates would be around ~1 3D volume/5 sec or 1 2D image/sec at the most.</p>

---

## Post #5 by @saikatsengupta (2021-10-11 21:02 UTC)

<p>Thanks for the suggestions , Steve. It’ll definitely take me some time to explore these options <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=10" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---

## Post #6 by @lassoan (2021-10-11 22:08 UTC)

<aside class="quote no-group" data-username="saikatsengupta" data-post="4" data-topic="20104">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/c77e96/48.png" class="avatar"> saikatsengupta:</div>
<blockquote>
<p>Frame rates would be around ~1 3D volume/5 sec or 1 2D image/sec</p>
</blockquote>
</aside>
<p>This is not a very demanding update rate, so using the file system for data transfer would most likely not lead to significant overhead.</p>
<p>However, OpenIGTLink was been developed exactly for this application (MRI image acquisition and scan plane control for Siemens MRI scanners for robot-assisted interventions) and has several advantages over a basic file-based communication, including:</p>
<ul>
<li>Better performance: File reading would happen in the main thread, blocking the whole application for short periods of time, which can be quite annoying for users during continuous acquisition. In contrast, OpenIGTLink continuously reads data from the network in the background, without blocking the application GUI at all (and takes care of all the necessary synchronization between the main thread and background threads).</li>
<li>Two-way communication: In addition to images (either 2D or 3D), OpenIGTLink also allows you to control scan plane (by sending transforms), start/stop acquisition, switch between imaging modes (using commands), etc.</li>
<li>Simpler implementation: You can implement Philips XTC/OpenIGTLInk bridge in a few dozen lines of Python code, by adding a small OpenIGTLink frontend to <a href="https://www.neurofus.ca/matmri.html">matMRI</a> using <a href="https://pypi.org/project/pyigtl/">pyigtl</a>. You don’t need to worry about multithreading, synchronization, debugging random delays in file systems, etc.</li>
<li>Large ecosystem: There are many tools for real-time image-guided interventional applications based on OpenIGTLink (see for example <a href="http://slicerigt.org/">SlicerIGT</a> and <a href="https://plustoolkit.github.io/">PLUS toolkit</a>). You can record, replay, mix, calibration, synchronize, simulate, broadcast OpenIGTLink data streams. There are many imaging and position tracking tools, various sensors, robotic positioning devices, etc. using OpenIGTLink, so it is easy to integrate all these devices into a system and it is easy to replace any component by another one (e.g., in the lab you can simulate some components just by changing configuration files, without changing any code in your application). You can easily distribute the processing work across several computers if needed and we have examples of how to apply real-time AI processing to image streams.</li>
</ul>

---

## Post #7 by @saikatsengupta (2021-10-14 16:39 UTC)

<p>Thank you very much Andras (and I apologize for my late response).<br>
Yes, we are using MatMRI (thanks Sam Pichardo) , so as you suggest , integrating OpenIGTLink with that would be the most powerful solution.</p>

---
