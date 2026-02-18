# How to exchange data bewteen Slicer instance and Python CLI during runtime

**Topic ID**: 18357
**Date**: 2021-06-27
**URL**: https://discourse.slicer.org/t/how-to-exchange-data-bewteen-slicer-instance-and-python-cli-during-runtime/18357

---

## Post #1 by @mcfly3001 (2021-06-27 18:07 UTC)

<p>For my project I need to get the table position of a CT system. To get this information I need to connect via SSH to a server and call a command which will then continously write the table position to the stdout. Connecting via SSH and reading the stdout is easily done, though the workflow is basically to endlessly read from the stdout (i.e. an endless loop which reads the current table position).<br>
From what I understood so far, I wanted to create a Python CLI module which does the interfacing with the CT system because CLI is the suggested way for running “long running tasks” in the background. Though now I read somewhere that the results from a CLI are only written back to the scene nodes after the CLI finished the processing. This will not work in my case as the process should run until the application stops and should continously update a transform node.<br>
Is there another way to run such a task in an asynchronous way and update the transform nodes accordingly?</p>

---

## Post #2 by @lassoan (2021-06-27 19:04 UTC)

<p><a href="http://openigtlink.org/">OpenIGTLink</a> is designed for exactly this use case. You can connect to a wide range of imaging and tracking devices using this protocol from Slicer (using <a href="https://github.com/openigtlink/SlicerOpenIGTLink">OpenIGTLink extension</a>).</p>
<p>If you use an optical tracker (NDI, Optirak, Ascension, Claron, etc.), surgical navigation system (BrainLab or Medtronic), or some other position sensors then you can use the <a href="https://plustoolkit.github.io/">Plus toolkit</a> for this and then you don’t need to implement anything.</p>
<p>Alternatively, you can implement OpenIGTLink in your server (instead of a custom protocol). If all else fails, you can write a small Python script that continuously queries the SSH server and  makes the positions available via OpenIGTLink using <a href="https://pypi.org/project/pyigtl/">pyigtl</a>.</p>
<p>Also note that you can perform all kinds of tool calibrations and patient registrations that are needed for image-guided therapy, using <a href="http://slicerigt.org/">SlicerIGT extension</a>.</p>

---

## Post #3 by @mcfly3001 (2021-06-27 19:11 UTC)

<p>Thanks for the many suggestions. For most of our interfaces we are already using OpenIGTLink and we make also use of SlicerIGT. Unfortunately we do not have direct access to the CT system. The only interface that we can use is the SSH connection.<br>
But if I understood correctly, I could create a stand-alone Python application that is connecting to the CT via SSH and acts as an OpenIGTLink server to which our Slicer application connects. This should work, right? Did not think about that, thanks for the ideas!</p>

---

## Post #4 by @lassoan (2021-06-27 19:21 UTC)

<aside class="quote no-group" data-username="mcfly3001" data-post="3" data-topic="18357">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mcfly3001/48/6437_2.png" class="avatar"> mcfly3001:</div>
<blockquote>
<p>I could create a stand-alone Python application that is connecting to the CT via SSH and acts as an OpenIGTLink server to which our Slicer application connects.</p>
</blockquote>
</aside>
<p>Exactly. You can launch this small Python script from Slicer similarly to how <code>slicer.util._executePythonModule</code> works (just skip the part in the end that wait until the processing is completed) or using standard Python <code>subprocess</code> functions.</p>

---
