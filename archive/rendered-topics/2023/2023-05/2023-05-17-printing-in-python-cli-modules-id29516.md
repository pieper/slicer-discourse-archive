# Printing in Python CLI modules

**Topic ID**: 29516
**Date**: 2023-05-17
**URL**: https://discourse.slicer.org/t/printing-in-python-cli-modules/29516

---

## Post #1 by @benzwick (2023-05-17 16:53 UTC)

<p>When I print in a Python CLI module, all the messages are displayed after the module has completed. Is there any way to print the messages as they occur in real time during execution?</p>

---

## Post #2 by @pieper (2023-05-17 17:08 UTC)

<p>Python CLI (like C++ CLI) modules are very special purpose.  If they don’t suit your needs you are much better off writing a scripted module, or wrapping your CLI in a more general purpose script.</p>

---

## Post #3 by @benzwick (2023-05-17 17:30 UTC)

<p>I’m developing an <a href="https://github.com/SlicerCBM/SlicerFreeSurferCommands" rel="noopener nofollow ugc">extension</a> to run some FreeSurfer commands inside Slicer. Python CLI modules seem perfect because all I need is a GUI for running existing external commands. So far I have the SynthStrip command implemented and it works very well. The only issue is there is no way to know what is happening while the module is running, which for some commands might take several minutes or longer. As far as I understand, a scripted module would <a href="https://discourse.slicer.org/t/basic-questions-on-cli-modules-vs-scripted-modules/10782/2">block the GUI</a>, which would not be a good trade-off I think.</p>

---

## Post #4 by @pieper (2023-05-17 17:46 UTC)

<p>Right, it makes sense to run these as separate processes, but they don’t need to use the CLI infrastructure, which is really designed to be used for very simple use cases where autogenerating the GUI was preferred.  Basically the original motivation for C++ CLIs was to easily port a bunch of ITK example programs for use in Slicer.</p>
<p>Instead you can launch and manage processes using python, most cleanly with the QProcess inftrastructure, that gives you a clean cross platform signals-and-slots based interface for managing IO.  You may want to build on <a href="https://github.com/pieper/SlicerParallelProcessing/blob/master/Processes/Processes.py">the ParallelProcessing extension</a> or just learn from how it use QProcess.  The same approach is <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/DICOMLib/DICOMProcesses.py">used in the DICOM module</a>.</p>

---

## Post #5 by @lassoan (2023-05-17 18:15 UTC)

<aside class="quote no-group" data-username="benzwick" data-post="3" data-topic="29516">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/benzwick/48/80521_2.png" class="avatar"> benzwick:</div>
<blockquote>
<p>The only issue is there is no way to know what is happening while the module is running</p>
</blockquote>
</aside>
<p>If the process provides some output then you can capture that and print to the output using XML tags described <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel#Showing_Progress_in_an_Application">here</a>.</p>
<p>See for example in ModelMaker CLI module:</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8982bfcb620f311bcff94f153e37f9177f738603.mp4">
  </div><p></p>
<aside class="quote no-group" data-username="benzwick" data-post="3" data-topic="29516">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/benzwick/48/80521_2.png" class="avatar"> benzwick:</div>
<blockquote>
<p>As far as I understand, a scripted module would <a href="https://discourse.slicer.org/t/basic-questions-on-cli-modules-vs-scripted-modules/10782/2">block the GUI</a>, which would not be a good trade-off I think.</p>
</blockquote>
</aside>
<p>You don’t have to block the GUI, especially if work is done in a different process. I find that most often I block the GUI (just leave a <code>Cancel</code> button enabled to allow cancelling the operation) because it makes things a bit simpler. But if you want the user to be able to continue using Slicer then you can use the CLI infrastructure to run executables, or as <a class="mention" href="/u/pieper">@pieper</a> sugested use Qt classes (and to get notified about process via signals/slots); or use Python functions (and use QTimer to check the process state and outputs).</p>

---

## Post #6 by @benzwick (2023-05-19 06:15 UTC)

<p>Thanks for the advice. I’ll try rewriting the extension using scripted modules.</p>

---
