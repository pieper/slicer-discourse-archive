---
topic_id: 17804
title: "Running Additional Thread S For Tensorflow Predictions Withi"
date: 2021-05-26
url: https://discourse.slicer.org/t/17804
---

# Running additional thread(s) for Tensorflow predictions within Slicer

**Topic ID**: 17804
**Date**: 2021-05-26
**URL**: https://discourse.slicer.org/t/running-additional-thread-s-for-tensorflow-predictions-within-slicer/17804

---

## Post #1 by @zacbaum (2021-05-26 08:17 UTC)

<p>Hello,</p>
<p>I am using Slicer to perform real-time (and also offline - but that is less affected by this issue) AI-based segmentation of tracked ultrasound images, while concurrently recording the images using Sequences; and in some cases - reconstructing/rendering the segmentations into the 3D viewer simultaneously.</p>
<p>The issue that I have is that when doing the real-time segmentation and reconstruction, the recording frame-rate within Sequences drops as (what I believe to be happening, anyway is) everything runs in the main thread, meaning that a new frame won’t be recorded in Sequences until the Tensorflow AI model has done its prediction on that frame, and the resulting segmentation is added to the volume reconstruction.</p>
<p>What I would like to do is have the recording running on the main thread, and have the AI predictions (and possibly the volume reconstruction) run in a separate thread or process to prevent them from restricting one another.</p>
<p>Any suggestions on best practices (CLI module, using Python’s multi-threading or some other PyPI package for threading, etc.), or any direction on how this could be done would be much appreciated.</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2021-05-26 12:33 UTC)

<p>This might be a use case for the <a href="https://github.com/pieper/SlicerProcesses">SlicerProcesses</a> approach.  Basically it spawns PythonSlicer as worker processes and communicates with them through pickled dictionaries (e.g. of numpy arrays and metadata).  PythonSlicer has the same environment as Slicer, so you can import the same packages but you don’t have access to the Slicer qt app or vtk rendering context of the application.</p>
<p>You might also look at how SimpleFilters releases the python GIL to use python threading.</p>
<p>As you work on this it would be great if you could share a sample script or module of whatever approach works for you as a reference for others who want to solve the same problem in the future.</p>

---

## Post #3 by @zacbaum (2021-05-26 15:42 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a> - Those both seem like simple enough solutions!</p>
<p>Will give them a try and come back with questions or some sample code to share here for others.</p>

---

## Post #4 by @lassoan (2021-05-26 16:36 UTC)

<p>To minimize interference between the GUI application and processing, you can run the prediction in a separate process (even on a separate computer) that communicates with the data acquisition server (Plus) and the GUI (Slicer) using OpenIGTLink. The processing server can send and receive OpenIGTLink messages using <a href="https://github.com/lassoan/pyigtl">pyigtl</a> in a simple loop. The processing server can receive the input images directly from Plus and only send stream the results to Slicer.</p>
<pre><code class="lang-nohighlight"> Plus -&gt;-------------&gt;---------------&gt;- Slicer
         \                         /           
          \                       /            
           -&gt; Processing server -&gt;
</code></pre>

---

## Post #5 by @zacbaum (2021-06-29 09:47 UTC)

<p>For anyone looking to see roughly how I’ve ended up implementing this, see the gist <a href="https://gist.github.com/zacbaum/8b22f0c02c5847919a2b38e09fb63cf5" rel="noopener nofollow ugc">here</a>, which demonstrates a live and offline prediction using the <a href="https://github.com/pieper/SlicerProcesses" rel="noopener nofollow ugc">SlicerProcesses</a> module <a class="mention" href="/u/pieper">@pieper</a> proposed. I’ve inserted some comments to clarify some choices, but this will need to be tailored to a specific application/module when used.</p>
<p>Our previous application which did live predictions, volume reconstruction and recording with Sequences on streamed US images from PLUS obtained ~10FPS recording speed while reconstructing those 10FPS in real-time (on fairly modern hardware). Using the above methods, we obtain ~25-30FPS.</p>
<p>For the offline predictions, which previously took 10-15 seconds and froze the application; things still take the same amount of time, but there is no “locking up” of Slicer while the predictions occur in the background.</p>
<p>I’ve listed some of the key changes/notes below:</p>
<blockquote>
<p>The offline prediction is very similar to the examples provided in that repository, but</p>
<ul>
<li>You must pass a path to the model (or just its weights) to the process as TF models are not picklable</li>
<li>I am using fairly large volumes in the offline predictions, I write to a temporary file instead of purely using stdin and stdout</li>
</ul>
<p>The live prediction is a bit more tricky;</p>
<ul>
<li>Instead of writing just once, we need to be able to write continuously to stdin’s buffer</li>
<li>Then, update the data attribute of the Process object, and call the method which sends the new data</li>
<li>Additionally, with that data - provide an “on” or “off” byte and the size of the data, so we know that we’ve received everything properly in the script</li>
<li>Instead of receiving everything at once when the process finishes, connect a callback to the Process which happens each time stdout is written to</li>
<li>Terminate by switching the active byte “off”</li>
</ul>
</blockquote>
<p>Hopefully this helps others looking to do similar things in the future.</p>

---

## Post #6 by @pieper (2021-06-29 20:59 UTC)

<aside class="quote no-group" data-username="zacbaum" data-post="5" data-topic="17804">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/zacbaum/48/7166_2.png" class="avatar"> zacbaum:</div>
<blockquote>
<p>Hopefully this helps others looking to do similar things in the future.</p>
</blockquote>
</aside>
<p>Nice work <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"> Thanks for posting the follow up info.</p>

---
