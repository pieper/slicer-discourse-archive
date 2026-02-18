# Can't use `launchConsoleProcess`

**Topic ID**: 24414
**Date**: 2022-07-20
**URL**: https://discourse.slicer.org/t/cant-use-launchconsoleprocess/24414

---

## Post #1 by @keri (2022-07-20 16:33 UTC)

<p>Hi,</p>
<p>From this <a href="https://discourse.slicer.org/t/calling-slicer-module-from-a-python-file/12720">topic</a> I’m trying to run simple command and see output in Slicer Log messages:</p>
<pre><code class="lang-python">slicer.util.launchConsoleProcess([sys.executable, '-c', 'print(\"Hi\")'])
</code></pre>
<p>I get the output in Python console <code>&lt;Popen: returncode: None args: ['C:/C/r/python-install/bin/PythonSlicer.exe'...&gt;</code></p>
<p>But I hoped to see <code>Hi</code> in Log Messages.</p>
<p>Maybe I misunderstand something?</p>

---

## Post #2 by @keri (2022-07-20 17:01 UTC)

<p>Of it seems I needed to read data from returned <code>Popen</code>:</p>
<pre><code class="lang-python">p = slicer.util.launchConsoleProcess([sys.executable, '-c', 'print(\"Hi\")'])
print(p.stdout.read())
</code></pre>
<p>But is there a way to run subprocess with stdout to Slicer Log message?<br>
Something similar to:</p>
<pre><code class="lang-python">subprocess.run(my_cmd, stdout=slicer.stdout)
</code></pre>

---

## Post #3 by @lassoan (2022-07-20 17:35 UTC)

<p><code>slicer.util.launchConsoleProcess</code> is typically used with <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.logProcessOutput"><code>slicer.util.logProcessOutput</code></a> to wait for the execution to complete and forward the process output to the application log.</p>

---

## Post #4 by @keri (2022-07-20 17:56 UTC)

<p>Thank you,</p>
<p>Is there a way to do such thing on the background i.e. without stopping Slicer?</p>
<p>I’ve seen <a href="https://discourse.slicer.org/t/running-a-module-in-parallel/12641/3">similar topic</a> and does <a class="mention" href="/u/pieper">@pieper</a> 's solution with <a href="https://github.com/pieper/SlicerParallelProcessing" rel="noopener nofollow ugc">SlicerProcesses extension</a> is able to help me? I’m going to execute heavy computation that may take long time and it would be pretty attractive to run it on the background and to see all output somwhere in Slicer GUI.<br>
Haven’t tested SlicerParallelProcessing yet.</p>
<p>And the latest option probably is python cli module, but it scares me a little as it claims to write GUI in XML <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #5 by @lassoan (2022-07-20 19:27 UTC)

<p>If you only need to run one long processing at a time then you can use the CLI infrastructure (either calling C++ or Python CLI modules). If you start multiple CLI modules then they are executed one after the other, so if you want to run several of them in parallel then you would need to improve the CLI infrastructure or use another mechanism.</p>
<p>SlicerProcesses manages many long-running tasks in parallel, so you can use this for managing your background processes.</p>
<p>You can manage processes manually, too - launching them using <code>launchConsoleProcess</code> and monitor their status, gather output from them using customized versions of <code>logProcessOutput</code> (see for example in <a href="https://github.com/lassoan/SlicerElastix/blob/3e9ef490ee6a6f901daa3280af112950f6af13ec/Elastix/Elastix.py#L708-L739">SlicerElastix</a>).</p>
<p>Probably SlicerProcesses would be the best solution for your needs.</p>

---

## Post #6 by @keri (2022-07-20 22:11 UTC)

<p>Is it ok to run threads in python within Slicer?<br>
For example create python module and create thread:</p>
<pre><code class="lang-python">  def threaded_function(self, arg):
    from time import sleep
    for i in range(arg):
      print("running")
      sleep(1)

  thread = Thread(target = self.threaded_function, args = (10, ))
  thread.start()
</code></pre>
<p>from a first glance it works: the text “running” appears with some time step (definately not 1 second but still) and I’m able to use Slicer while it is executing.</p>

---

## Post #7 by @lassoan (2022-07-20 22:25 UTC)

<p>I would only use threads for very short, very frequent operations (where launching a separate process would be a significant overhear) or that needs complex interaction with the scene or when operating on extremely large data (that would cause significant extra memory usage to copy into another thread). For most other cases, launching a separate process for background processing is preferable, because it is:</p>
<ul>
<li>interruptible (you cannot force a thread to stop from the same process, but you can always terminate a separate process)</li>
<li>safer (if an algorithm crashes in a subprocess then it won’t crash the main application, but if an algorithm crashes in a background thread of the main application then it will make the main application crash)</li>
<li>more versatile (you can run any binary, you can run code in a different virtual Python environment, etc.)</li>
</ul>

---

## Post #8 by @keri (2022-07-20 22:33 UTC)

<p>That makes sense.<br>
Thank you for sharing these ideas, haven’t thought about it.</p>

---

## Post #9 by @keri (2022-07-21 12:49 UTC)

<p>It seems I’ve found a curious solution to the issue - <a href="https://doc.qt.io/qt-6/qprocess.html" rel="noopener nofollow ugc">QProcess</a>.<br>
Advantages: usability of signals/slots when new data is available on the stream, when finished etc.</p>
<pre><code class="lang-python"># somwhere in setup
self.qprocess = qt.QProcess()
# without `qt.QProcess.MergedChannels` onProcessReadyReadStandardOutput called only once at the end of the subprocess execution
self.qprocess.setProcessChannelMode(qt.QProcess.MergedChannels)
self.qprocess.connect('readyReadStandardOutput()', self.onProcessReadyReadStandardOutput)
self.qprocess.connect('errorOccurred(qt.QProcess.ProcessError)', self.onProcessErrorOccured)
self.qprocess.connect('finished(int)', self.onProcessFinished)

#.........................................................................

# slots
def onProcessReadyReadStandardOutput(self):
  print("QProcess output:\t", str(self.qprocess.readAllStandardOutput()))

def onProcessErrorOccured(self, err : qt.QProcess.ProcessError):
  print("QProcess error:\t", str(err))

def onProcessFinished(self, exitCode : int):
  print("QProcess finished:\t", str(exitCode))

def onStartButtonClicked(self):
  self.qprocess.setProgram('C:\\my.exe')
  self.qprocess.setArguments(['-E', 'my_command'])
  self.qprocess.start() # or startDetached(): as I understood even if app is closed detached process will still be running
  # the code goes further without stopping execution
</code></pre>
<p>This doesn’t block Slicer or python and output appears in the console as it becomes ready.</p>
<p>Are there any disadvantages?</p>
<p>Few links that helped me:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://forum.qt.io/topic/108032/get-output-stream-from-qprocess">
  <header class="source">
      <img src="https://forum.qt.io/assets/uploads/system/favicon.ico?v=500i9cmpogn" class="site-icon" width="32" height="32">

      <a href="https://forum.qt.io/topic/108032/get-output-stream-from-qprocess" target="_blank" rel="noopener nofollow ugc" title="10:39AM - 23 October 2019">Qt Forum – 23 Oct 19</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.gravatar.com/avatar/6c847b5f02c58bd4cd95bd886a3ba7dd?size=192&amp;d=mm" class="thumbnail onebox-avatar" width="192" height="192">

<h3><a href="https://forum.qt.io/topic/108032/get-output-stream-from-qprocess" target="_blank" rel="noopener nofollow ugc">Get output stream from QProcess</a></h3>

  <p>Hello, this is my code:     QProcess process;     process.start("sudo apt update");     process.waitForFinished(-1);      QString stdout = process.readAllStandardOutput();     QString stderr = process.readAllStandardError();  I have 3 questions:  How...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://forum.qt.io/topic/75454/qprocess-readall-and-qprocess-readallstandardoutput-both-return-an-empty-string-after-qprocess-write-is-run/5">
  <header class="source">
      <img src="https://forum.qt.io/assets/uploads/system/favicon.ico?v=500i9cmpogn" class="site-icon" width="32" height="32">

      <a href="https://forum.qt.io/topic/75454/qprocess-readall-and-qprocess-readallstandardoutput-both-return-an-empty-string-after-qprocess-write-is-run/5" target="_blank" rel="noopener nofollow ugc" title="11:55PM - 24 January 2017">Qt Forum – 24 Jan 17</a>
  </header>

  <article class="onebox-body">
    <img src="https://www.gravatar.com/avatar/b3a6c65cdd121a35b1dcf348c6b0c9b6?size=192&amp;d=mm" class="thumbnail onebox-avatar" width="192" height="192">

<h3><a href="https://forum.qt.io/topic/75454/qprocess-readall-and-qprocess-readallstandardoutput-both-return-an-empty-string-after-qprocess-write-is-run/5" target="_blank" rel="noopener nofollow ugc">QProcess::readAll and QProcess::readAllStandardOutput both return an empty...</a></h3>

  <p>Hi all note: this might become confusing, please bare with me! To get a basic sense of what I want to do: QProcess runs a command by QProcess::start("sh -c \"cd /tmp/tempdir ; ./my_script --option file.txt ; echo $?\" ")  The script expects input...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>P.S. another option is to use <code>QTimer()</code> and send signals every say 10 seconds to do the updates (read output) but somewhere near each update (once in 10 seconds) the GUI may freeze for a half of a second (probably when signal is emitted)</p>

---

## Post #10 by @pieper (2022-07-21 18:24 UTC)

<p>Yes, a <a href="https://github.com/pieper/SlicerParallelProcessing/blob/master/Processes/Processes.py#L206">SlicerParallelProcessing <code>Process</code> is a subclass of <code>QProcess</code></a> so it has all the advantages of using signals and slots to integrate with the event loop of the app.</p>
<p>A <code>QTimer</code> could be helpful to give some progress information to the user, but yes, I’d suggest relying on the signals to determine when there is data ready to read so you don’t block.</p>

---
