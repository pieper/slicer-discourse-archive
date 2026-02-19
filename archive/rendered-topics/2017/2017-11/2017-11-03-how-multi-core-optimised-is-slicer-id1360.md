---
topic_id: 1360
title: "How Multi Core Optimised Is Slicer"
date: 2017-11-03
url: https://discourse.slicer.org/t/1360
---

# How multi-core optimised is Slicer?

**Topic ID**: 1360
**Date**: 2017-11-03
**URL**: https://discourse.slicer.org/t/how-multi-core-optimised-is-slicer/1360

---

## Post #1 by @jdx-john (2017-11-03 15:34 UTC)

<p>I am interested to know to what extent Slicer is able to use multiple cores for increased performance. I would expect at least some multi-core support but to what extent would I see performance differences as number of equivalent cores increases (say from 1 up to 8)?</p>
<p>Some systems these days will allow a single core to run much faster if other cores are idle, is Slicer at heart a single-core application which uses additional cores for a few things, or a truly parallelised architecture?</p>

---

## Post #2 by @pieper (2017-11-03 16:05 UTC)

<p>Generally speaking the application itself is single threaded and event driven, but individual algorithms are multithreaded and are very good at leveraging available cores.  Most of this happens at the VTK and ITK levels, where operations like volume filters or reslicing are broken down into ‘slabs’ that are calculated in parallel.</p>
<p>Here’s some background info:</p>
<p><a href="https://itk.org/Doxygen/html/ThreadingPage.html" class="onebox" target="_blank">https://itk.org/Doxygen/html/ThreadingPage.html</a></p>
<p><a href="https://www.vtk.org/Wiki/VTK/Threaded_Image_Algorithms" class="onebox" target="_blank">https://www.vtk.org/Wiki/VTK/Threaded_Image_Algorithms</a></p>

---

## Post #3 by @jdx-john (2017-12-05 14:58 UTC)

<p>Are there any plans to make the application less single-core, especially to decouple the GUI from the main thread? It’s the one ugly part of Slicer in my opinion, the UI locking up and not refreshing when loading datasets is really clunky.</p>

---

## Post #4 by @lassoan (2017-12-05 17:39 UTC)

<p>There is an asynchronous data processing and transfer infrastructure in Slicer that allows background data processing and loading (see vtkSlicerTask). This infrastructure is used by CLI modules, but has not been getting too much attention in the last 5-10 years because loading times are rarely an issue nowadays.</p>
<p>DICOM loading times have dramatically improved in Slicer in the last few months, so we can now import complete CT and MRI studies in 10-20 seconds and load them in 5-10 seconds. However, importing and loading of large 4D studies (consisting of several thousands of frames) may still take a couple of minutes. I agree that it would be nice to improve this further. I would focus on making the loading faster first (by storing file examination result in the database, so there would be no need for on-the-fly examination each time you load a data set). Loading in the background would be nice, but until you loaded the image there is not much to do anyway, so I’m not sure this would be high priority.</p>

---

## Post #5 by @hherhold (2017-12-05 20:46 UTC)

<p>When using Segment Editor with Show 3D enabled, updating the 3D model occurs after the paint editor effect is complete, but nothing can be done until the 3D model is updated. Is it possible to decouple what appears to be a single-threaded operation?</p>
<p>(Does that make sense?)</p>

---

## Post #6 by @lassoan (2017-12-05 20:56 UTC)

<p>Yes, background processing (or alternative, faster 3D display of binary labelmaps) would be useful. We have this issue to track this task: <a href="https://issues.slicer.org/view.php?id=4484">https://issues.slicer.org/view.php?id=4484</a></p>

---

## Post #7 by @hherhold (2017-12-05 21:17 UTC)

<p>Will the update to the current VTK version (and OpenGL 2) make a difference? (meaning, easier to implement)</p>

---

## Post #8 by @lassoan (2017-12-05 21:36 UTC)

<p>Multi-volume rendering will make a huge difference. It will allow us to show segments in 3D without creating a surface mesh.</p>

---

## Post #9 by @cpinter (2017-12-06 00:02 UTC)

<p>Yes it has been in the plans but was not a high priority. Thanks Andras for adding the ticket</p>

---

## Post #10 by @jdx-john (2017-12-07 13:32 UTC)

<p>While I take on board that making everything faster reduces the impact of the problem, I’d still say from the perspective of Windows GUI development (and presumably GUI development in general) it is definitely considered best practices that the UI shouldn’t be blocked by what the application is doing.</p>
<p>I hadn’t realised how long Slicer had been around but it now makes sense it’s roots work this way, because back then this sort of “GUI hangs while something happens” approach was really the norm <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>

---
