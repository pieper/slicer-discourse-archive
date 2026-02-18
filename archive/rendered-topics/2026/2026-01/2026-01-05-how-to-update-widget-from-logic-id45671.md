# How to update widget from logic?

**Topic ID**: 45671
**Date**: 2026-01-05
**URL**: https://discourse.slicer.org/t/how-to-update-widget-from-logic/45671

---

## Post #1 by @Victor_Wayne (2026-01-05 09:47 UTC)

<p>I have a C++ extension module. I am doing boolean mesh operation calculation in a worker thread inside the logic module. I have a function that calculates the volume of a given segmentation node. I need it run as soon as the worker thread finishes and update one label. How can I do it? I already wrote the worker thread function using QtConcurrent::run and QMetaObject::invokeMethod. I can call the volume calculate function from inside the invokeMethod lambda. But how can I update the label from there?</p>

---

## Post #2 by @pieper (2026-01-05 15:11 UTC)

<p>The Slicer architecture discourages having the logic “know” about the gui in terms of linking the code or calling methods.  Instead, the logic can modify the mrml nodes and the gui can observe the nodes to update their state or perform additional processing.  The goal is to make it easier to reuse the logic in non-gui environment or even to swap guis (which we have done in the past).</p>

---

## Post #3 by @Victor_Wayne (2026-01-06 04:19 UTC)

<p>I see. Thanks for the help. I solved this problem by creating a <code>vtkCommand::UserEvent</code> inside a struct. And when I calculate the label I raise an event using the InvokeEvent function and I have connected a slot for that event using qvtkConnect. Would you say that it is a correct approach? After doing this, I am getting the “Application not responding - force quit/wait” pop up in my ubuntu 24 system. That defeats the whole pupose of doing the compute intensive calculation on the worker thread. Do you think the <code>InvokeEvent</code> function caused it? Do you think the modifying and observing the MRML node can solve this problem. I did not get the pop up after moving to the worker thread and before adding the InvokeEvent function.</p>
<p>Thanks for your help.</p>

---

## Post #4 by @lassoan (2026-01-06 13:04 UTC)

<p>Invoking a VTK event from a worker thread that is observed in the main thread would often trigger rendering code from a worker thread, which is expected to hang or crash the application. This is not a Slicer-specific behavior but in general works like this in all multi-threaded GUI application, so you can get advice from any AI chatbot on how to resolve this. But to give a high-level description of how to update data from a worker thread:</p>
<ol>
<li>Main thread passes the ownership of input data to the worker thread (the safest is to create a copy, but if the data is not modified by the worker or the main thread then it may be OK to just pass the pointer of the existing object)</li>
<li>Worker thread processes the input data and writes the result to an output data object</li>
<li>Worker thread passes the ownership of the output data to the main thread (usually via a synchronization object, such as a thread-safe queue, or a Qt queued connection, or <code>vtkApplicationLogic::RequestModified()</code> call)</li>
</ol>
<p>If you want to avoid complexity of implementing thread-safe background processing then you can run your mesh processing in a CLI module (CLI modules are executed on a background thread, Slicer takes care of passing the input and output data between the threads) use the <a href="https://github.com/pieper/SlicerParallelProcessing">ParallelProcessing extension</a> (it runs the processing in a separate process and passes the data via stdin/stdout), or start a separate Python process that communicates with Slicer via OpenIGTLink (the Python process can send/receive data via <a href="https://pypi.org/project/pyigtl/">pyigtl</a>).</p>

---

## Post #5 by @Victor_Wayne (2026-01-07 03:47 UTC)

<p>Thanks for your suggestions. I’ll definitely look into each and every one of your inputs and get back to you if I have anything to ask.</p>

---
