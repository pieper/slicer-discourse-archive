# How to load volume in the subprocess in python?

**Topic ID**: 27245
**Date**: 2023-01-15
**URL**: https://discourse.slicer.org/t/how-to-load-volume-in-the-subprocess-in-python/27245

---

## Post #1 by @jay1987 (2023-01-15 08:32 UTC)

<p>i have tryed to use SlicerParallelProcessing<br>
SlicerParallelProcessing can’t import slicer.util package</p>

---

## Post #2 by @pieper (2023-01-15 18:19 UTC)

<p>The examples use PythonSlicer, which is just the python interpreter part of Slicer, not the full app.  In the examples I use the stdin/stdout of PythonSlicer to pass data back and forth, which fits some processing workflows.  It would be possible to use the same process management techniques to run the Slicer app, perhaps with <code>--no-main-window</code> and then exchange data using other channels, like tempfiles or the WebServer, but there are no examples of that right now.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/pieper/SlicerParallelProcessing/blob/master/Processes/Processes.py#L227">
  <header class="source">

      <a href="https://github.com/pieper/SlicerParallelProcessing/blob/master/Processes/Processes.py#L227" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/pieper/SlicerParallelProcessing/blob/master/Processes/Processes.py#L227" target="_blank" rel="noopener">pieper/SlicerParallelProcessing/blob/master/Processes/Processes.py#L227</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="217" style="counter-reset: li-counter 216 ;">
          <li>  self.name = "Process"</li>
          <li>  self.processState = "Pending"</li>
          <li>  self.scriptPath = scriptPath</li>
          <li>  self.success = True</li>
          <li>
          </li>
<li>def run(self, logic):</li>
          <li>  self.connect('stateChanged(QProcess::ProcessState)', self.onStateChanged)</li>
          <li>  self.connect('started()', self.onStarted)</li>
          <li>  self.finishedSlot = lambda exitCode, exitStatus : self.onFinished(logic, exitCode, exitStatus)</li>
          <li>  self.connect('finished(int,QProcess::ExitStatus)', self.finishedSlot)</li>
          <li class="selected">  self.start("PythonSlicer", [self.scriptPath,])</li>
          <li>
          </li>
<li>def onStateChanged(self, newState):</li>
          <li>  msg = f'{self.name}: state: {Process.QProcessStateNames[self.state()]}'</li>
          <li>
          </li>
<li>  # qt.QProcess.UnknownError usually means that there is no error, therefore</li>
          <li>  # to prevent polluting the logs and confusint users, we don't print UnknownError.</li>
          <li>  if self.error() != qt.QProcess.UnknownError:</li>
          <li>    msg += f', last error: {Process.QProcessErrorNames[self.error()]}'</li>
          <li>
          </li>
<li>  logging.info(msg)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @jay1987 (2023-01-16 01:04 UTC)

<p>thank you pieper<br>
now i run a Slicer main App,and i want to use some feather of Slicer to Run SlicerParallelProcessing , so i need to start a second and third Slicer Sub App to do that. and pass data with stdin/stdout</p>

---

## Post #4 by @pieper (2023-01-16 18:09 UTC)

<p>Unfortunately you can’t communicate with the Slicer app via stdin/stdout, but you can have several instances running at the same time.</p>

---

## Post #5 by @jay1987 (2023-01-17 00:47 UTC)

<p>if i want to use some feather of slicer in multi thread or multi process , can i write multithread in C++ function, and invoke the function use python script?</p>

---

## Post #6 by @pieper (2023-01-17 22:20 UTC)

<p>If you are building Slicer from source you can add C++ code.  We typically use Qt, VTK or ITK for implementing C++ features.</p>
<p>If you want to use a slicer binary, you could compile a separate executable and run it from Slicer and pass data, either with the ParallelProcessing extension or with the Slicer CLI Execution Model (see, for example, <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/SlicerExecutionModel">this page</a>).</p>

---

## Post #7 by @jay1987 (2023-01-18 00:44 UTC)

<p>thank you very much <a class="mention" href="/u/pieper">@pieper</a></p>

---
