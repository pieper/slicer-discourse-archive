# Main application response, sub threading rendering

**Topic ID**: 19225
**Date**: 2021-08-17
**URL**: https://discourse.slicer.org/t/main-application-response-sub-threading-rendering/19225

---

## Post #1 by @xianger-qi (2021-08-17 11:47 UTC)

<p>I have a question. If my application window has 2 slicer rendering windows, and each rendering window consumes 50ms to render a framerate, and backend  sends rendering request with 10 frequency. that indicate the application can’t response user event like mouse press, key press and so on. how can i deal with this, so why don’t move the rendering window into sub thread, that can solve this problem?</p>

---

## Post #2 by @pieper (2021-08-17 20:20 UTC)

<p>When you perform the render it’s actually triggering the processing pipeline to update all the data and since lot of the code in VTK is not thread safe it would not be possible to run those in separate threads.  Many of the processing steps are themselves multithreaded so depending on the scene you may already be getting good thread performance.  Best approach is to use a profiler to see where time is being spent and maybe you can rearrange the processing or otherwise optimize the code.</p>

---

## Post #3 by @xianger-qi (2021-08-18 01:57 UTC)

<p>yes. i know that vtk rendering window base on qt library, whose event loop code in QVTKInteractor that use the same event loop with QApplication. But if use vtk self event loop vtkRenderWindowInteractor in separate threads, which can move rendering tasks to sub threads. in my view, there are another method to attend this goal which is offscreen rendering in separate threads then inform main application to draw.</p>

---

## Post #4 by @lassoan (2021-08-18 05:06 UTC)

<aside class="quote no-group" data-username="xianger-qi" data-post="1" data-topic="19225">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/xianger-qi/48/11944_2.png" class="avatar"> xianger-qi:</div>
<blockquote>
<p>each rendering window consumes 50ms to render a framerate</p>
</blockquote>
</aside>
<p>This is unusually long. Do you use volume rendering or display models with hundreds of thousands of points? What CPU and GPU do you have? What operating system do you use? Do you build Slicer or you use an official release?</p>
<p>If you want to speed up rendering then start with profiling. See if the bottleneck is really rendering or some other filter pipeline updates. There is a good chance that the rendering is fast, but there are some filter updates that take time. You can then see if you can speed up those filters by optimizing them, making it multi-threaded, leverage the GPU for that processing, etc. You may also simplify your data (subsample images, decimate models) and show those variants during interactions and render the full-resolution data when the interaction ended.</p>
<p>You also need to evaluate how much it costs and how much speed you can gain by upgrading your hardware vs. working on performance optimizations in the software. For a research project, hardware costs should not matter (as you only need to build a handful of systems), but if you develop a commercial application that is targeted to run on cheap hardware of tens of thousands of users then it is worth to spend time on software optimizations.</p>

---

## Post #5 by @xianger-qi (2021-08-18 05:39 UTC)

<p>thanks for the replying! I totally understand your suggestions about hardware improving, model separating multiple levels, etc. the example above maybe improper so that you don’t understand the question. Supposing, There are a backend process which modifies the data model state and send render request with a high frequency, which causes the main application can’t response external user events. If the application has multiple render windows, the problem become more serious. In my view, separating the vtk render window event loop from main application which is solution to solve the problem?</p>

---

## Post #6 by @lassoan (2021-08-18 05:55 UTC)

<p>If you need to run some complex processing in background threads that should not be a problem at all. This is done for example whenever you run a CLI module, or run image processing using Simple Filters module, or index DICOM images, or send/receive data sets via OpenIGTLink.</p>
<p>To implement custom processing in the same process, you can implement your processing as a CLI module (that is executed in a background thread, but a limitation is that up to one CLI module can run in the background at a time, other requests are queued), or implement synchronization between the threads yourself.</p>
<p>If it is OK to run processing in separate threads (should be OK for most use cases) then you can implement your processing in a Python scripted CLI module (same limitation applies that only one CLI runs at a time), or you can launch processing on multiple processes at the same time using <a href="https://github.com/pieper/SlicerProcesses">SlicerProcesses module</a>, or launch multiple processes and send/receive data objects using <a href="http://openigtlink.org/">OpenIGTLink</a>.</p>

---

## Post #7 by @pieper (2021-08-18 12:00 UTC)

<p><a class="mention" href="/u/xianger-qi">@xianger-qi</a> this is a great topic and if you find ways to speed up the rendering I hope you will report back what you find.</p>
<p>As <a class="mention" href="/u/lassoan">@lassoan</a> and I have pointed out, the first priority is to identify exactly what is actually taking time and you can decide if it’s essential computation or something that can be optimized.  Profiling is essential for this.  Sometimes you can do this with simple logging or timers in your code.  Or you can use a tool like <a href="http://www.codersnotes.com/sleepy/">very sleepy on windows</a>, perf on linux, or Instruments or Activity Monitor on mac.</p>

---

## Post #8 by @xianger-qi (2021-08-18 12:14 UTC)

<p>Thanks a lot ! I build the application base on qt and vtk, and instance a qt mainwindow, and place 4 vtk render windows using the class vtkRenderWindowInteractor. I invoke the  method of vtkRenderWindowInteractor in separate thread not the qt gui thread. In this way, i can render in sub thread and won’t block the gui event loop.</p>

---
