# Slicer crash when call multiprocessing

**Topic ID**: 1044
**Date**: 2017-09-13
**URL**: https://discourse.slicer.org/t/slicer-crash-when-call-multiprocessing/1044

---

## Post #1 by @anqiang-12sigma (2017-09-13 20:29 UTC)

<p>I want to use python multiprocessing, but it makes slicer crash.</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:\Program Files\Slicer 4.7.0-2017-08-16\lib\Python\Lib\multiprocessing\process.py", line 249, in _bootstrap
    sys.stdin.close()
AttributeError: 'PythonQtStdInRedirect' object has no attribute 'close'
</code></pre>
<p>Does slicer have plans to fully support Python3 and PyQt5?</p>

---

## Post #2 by @lassoan (2017-09-13 20:38 UTC)

<p>You can already build Slicer with Qt5, probably we’ll update to Qt5 in a couple of weeks.</p>
<p>We plan to move to Python3 when all Slicer’s dependencies support Python3.</p>
<p>PyQt uses GPL license, which is incompatible with Slicer’s more permissive BSD-type license (we use PythonQt, which is LGPL).</p>

---

## Post #3 by @anqiang-12sigma (2017-09-25 15:09 UTC)

<p>I found PythonQt too many bugs, why not replace it with PySide? It’s also LGPL.</p>

---

## Post #4 by @lassoan (2017-09-25 18:49 UTC)

<p>PySide seems to be only for Qt4 (<a href="https://wiki.qt.io/PySide">https://wiki.qt.io/PySide</a>). Is PySide2 complete and stable, supporting Python3 and latest Qt5?</p>
<p>We don’t experience any issues with Qt wrapping using PythonQt, so unless we run into some major problems in the future, it is not likely Slicer would switch.</p>
<p>Do you know what would be some advantages of using PySide2 compared to PythonQt? What “bugs” you experienced with PythonQt? Are you sure you using it correctly? Have you reported the errors to PythonQt?</p>

---

## Post #5 by @anqiang-12sigma (2017-09-26 00:57 UTC)

<ol>
<li>multiprocsssing can not work</li>
<li>QAbstractItemModel createIndex overide error</li>
<li>setItemDelegateForColumn crash</li>
<li>Delegate can not work normally</li>
</ol>
<p>The code runs fine on PyQt</p>

---

## Post #6 by @lassoan (2017-09-26 02:28 UTC)

<p>The issues that you describe do not seem to be difficult to address; except the last one, which I don’t understand. I would suggest to submit your questions (with more specific description of the problem) to <a href="https://sourceforge.net/p/pythonqt/discussion/" class="inline-onebox">PythonQt / Discussion</a>.</p>
<p>There are some differences compared to PySide (see <a href="http://pythonqt.sourceforge.net/Features.html">http://pythonqt.sourceforge.net/Features.html</a>), but there doesn’t seem to be any major limitation in PythonQt. The beauty of PythonQt is that it is so small and simple that it is easy to develop and maintain it, even for a small team. PySide has some advantages, mainly the larger user community, but I don’t think that would justify the huge work that would be required to migrate Slicer and all extensions. It is probably a better investment to spend that time with fixing issues or adding more features to Slicer.</p>
<blockquote>
<p>The code runs fine on PyQt</p>
</blockquote>
<p>PyQt is irrelevant for us due to its restrictive license.</p>

---

## Post #7 by @anqiang-12sigma (2017-09-26 02:52 UTC)

<p>I have already submitted a question on sourceforge.<br>
<a href="https://sourceforge.net/p/pythonqt/discussion/631393/thread/4529adde/" rel="nofollow noopener">Model/View/Delegate some problems!</a></p>

---

## Post #8 by @lassoan (2017-09-26 02:57 UTC)

<p>To increase the chance that your questions will be answered on sourceforge, post only one question in a topic and provide much more details including a complete example that reproduces the problem.</p>

---

## Post #9 by @John_DiMatteo (2019-03-19 19:30 UTC)

<p>You can work around the Slicer <code>PythonQtStdInRedirect</code> multiprocessing crash by temporarily changing sys.stdin.  For example, the below multiprocessing works in slicer:</p>
<pre><code>from multiprocessing import Pool
import sys, os
import math

original_stdin = sys.stdin
sys.stdin = open(os.devnull)
try:
  p = Pool(5)
  print(p.map(math.sqrt, [4, 8, 16]))
finally:
  sys.stdin.close()
  sys.stdin = original_stdin</code></pre>

---

## Post #10 by @pieper (2020-02-07 18:37 UTC)

<p>Thanks <a class="mention" href="/u/john_dimatteo">@John_DiMatteo</a> for sending the <code>Pool</code> recipe.  Did you also get it working for <code>multiprocessing.Process</code>?  I’m looking for something that will work robustly on all platforms and I’m thinking I’ll use <code>subprocess</code> with <code>PythonSlicer</code>.</p>

---

## Post #11 by @Alex_Vergara (2020-02-08 20:03 UTC)

<p>This trick does not work on Windows, and will never work. Although it works perfectly on Mac and linux.</p>

---

## Post #12 by @pieper (2020-02-08 20:17 UTC)

<p>Thanks for the info <a class="mention" href="/u/alex_vergara">@Alex_Vergara</a>.  Yes, I did some testing and now I’m thinking I’ll use <code>QProcess</code> since it has a very clean API and is already integrated with the signals/slots event loop.  Turns out it’s pretty straightforward to start a <code>PythonSlicer</code> process and send pickled data back and forth through stdin/stdout.  Will share some sample code if I get something working well on all platforms.</p>

---

## Post #13 by @Alex_Vergara (2020-02-10 10:52 UTC)

<aside class="quote no-group" data-username="pieper" data-post="12" data-topic="1044">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>QProcess</p>
</blockquote>
</aside>
<p>You will end up by facing the same problem in Windows:</p>
<ul>
<li><a href="https://stackoverflow.com/questions/23397/whats-the-best-way-to-duplicate-fork-in-windows" class="inline-onebox" rel="noopener nofollow ugc">python - What's the best way to duplicate fork() in windows? - Stack Overflow</a></li>
<li><a href="https://stackoverflow.com/questions/2738809/whats-the-equivalence-of-os-fork-on-windows-with-python" class="inline-onebox" rel="noopener nofollow ugc">What's the equivalence of os.fork() on Windows with Python? - Stack Overflow</a></li>
</ul>
<p>There is simply not solution available to Windows. The multiprocessing shall be done in a separate script with the <code>if self.__name__ == "main"</code> trick</p>
<ul>
<li><a href="https://stackoverflow.com/questions/419163/what-does-if-name-main-do" class="inline-onebox" rel="noopener nofollow ugc">python - What does if __name__ == "__main__": do? - Stack Overflow</a></li>
</ul>
<p>In this last case the script itself must be called in a way that it is the main module, otherwise the multiprocessing spawn will just create several non functioning processes. This is a real fault in windows conception. The best explanation is <a href="https://stackoverflow.com/a/52476456/10059284" rel="noopener nofollow ugc">this</a></p>

---

## Post #14 by @pieper (2020-02-10 13:51 UTC)

<p>Agreed, Windows and Unix took very different approaches years ago and it’s caused a lot of complexity.</p>
<p>For my particular use case the QProcess approach is working well for me on both Windows and Mac.  In particular we have some computationally intense single threaded python code we want to apply to a set of data already loaded in Slicer.  So launching a PythonSlicer instances and sending them the data will work.  I don’t exactly want to fork the whole Slicer process anyway and may at some point want to run these processes on another machine, e.g. via ssh.  I’m still working on complete examples and then I’ll push some code.</p>

---

## Post #15 by @pieper (2020-02-10 20:41 UTC)

<p>Here’s the example using QProcess:</p>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://github.githubassets.com/favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://github.com/pieper/SlicerProcesses" target="_blank">GitHub</a>
  </header>
  <article class="onebox-body">
    <img src="https://avatars2.githubusercontent.com/u/126077?s=400&amp;v=4" class="thumbnail onebox-avatar" width="60" height="60">

<h3><a href="https://github.com/pieper/SlicerProcesses" target="_blank">pieper/SlicerProcesses</a></h3>

<p>Slicer modules for running subprocesses to operate on data in parallel - pieper/SlicerProcesses</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #17 by @Alex_Vergara (2020-02-11 14:37 UTC)

<p>I have successfully translated your code into mine with some caveats:</p>
<ul>
<li>Basically you need to decode the stdout to the correct data type, it is not enough to ask pickle to do it</li>
<li>You need to deepcopy your input data</li>
<li>You can add a progress bar <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:">
</li>
</ul>
<pre><code class="lang-python">import qt
import json
import pickle
import slicer
import copy
import numpy as np

from Logic import logging, utils
from slicer.ScriptedLoadableModule import *

#
# ProcessesLogic
#

class ProcessesLogic(ScriptedLoadableModuleLogic):

    def __init__(self, parent = None, maximumRunningProcesses=None, completedCallback=lambda : None):
        super().__init__(parent)
        self.results = {}
        if not maximumRunningProcesses:
            cpu_cores, cpu_processors, lsystem = utils.getSystemCoresInfo()
            self.maximumRunningProcesses = cpu_cores
        self.completedCallback = completedCallback

        self.QProcessStates = {0: 'NotRunning', 1: 'Starting', 2: 'Running',}

        self.processStates = ["Pending", "Running", "Completed"]
        self.processLists = {}
        for processState in self.processStates:
            self.processLists[processState] = []

        self.canceled = False
        self.ProgressDialog = slicer.util.createProgressDialog(
                parent=None, value=0, maximum=100)
        labelText = "Processing ..."
        self.ProgressDialog.labelText = labelText
        self.ProgressDialog.show()
        slicer.app.processEvents()

    def setMaximumRunningProcesses(self, value):
        self.maximumRunningProcesses = value

    def saveState(self):
        state = {}
        for processState in self.processStates:
            state[processState] = [process.name for process in self.processLists[processState]]
        self.getParameterNode().SetAttribute("state", json.dumps(state))

    def state(self):
        return json.loads(self.getParameterNode().GetAttribute("state"))

    def addProcess(self, process):
        self.processLists["Pending"].append(process)
        self.ProgressDialog.maximum = len(self.processLists["Pending"])

    def run(self):
        while len(self.processLists["Pending"]) &gt; 0:
            if len(self.processLists["Running"]) &gt;= self.maximumRunningProcesses:
                break
            process = self.processLists["Pending"].pop()
            process.run(self)
            self.processLists["Running"].append(process)
            self.saveState()

    def onProcessFinished(self,process):
        self.processLists["Running"].remove(process)
        self.processLists["Completed"].append(process)
        self.ProgressDialog.value += 1
        slicer.app.processEvents()
        self.saveState()
        if len(self.processLists["Running"]) == 0 and len(self.processLists["Pending"]) == 0:
            for process in self.processLists["Completed"]:
                k, v = process.result[0], process.result[1]
                self.results[k] = v
            self.ProgressDialog.close()
            self.completedCallback()
        if self.ProgressDialog.wasCanceled:
            self.canceled = True
        else:
            self.run()

class Process(qt.QProcess):
    """TODO: maybe this should be a subclass of QProcess"""

    def __init__(self, scriptPath):
        super().__init__()
        self.name = "Process"
        self.processState = "Pending"
        self.scriptPath = scriptPath
        self.debug = False
        self.logger = logging.getLogger("Dosimetry4D.qprocess")

    def run(self, logic):
        self.connect('stateChanged(QProcess::ProcessState)', self.onStateChanged)
        self.connect('started()', self.onStarted)
        finishedSlot = lambda exitCode, exitStatus : self.onFinished(logic, exitCode, exitStatus)
        self.connect('finished(int,QProcess::ExitStatus)', finishedSlot)
        self.start("PythonSlicer", [self.scriptPath,])

    def onStateChanged(self, newState):
        self.logger.info('-'*40)
        self.logger.info(f'qprocess state code is: {self.state()}')
        self.logger.info(f'qprocess error code is: {self.error()}')

    def onStarted(self):
        self.logger.info("writing")
        if self.debug:
            with open("/tmp/pickledInput", "w") as fp:
                fp.buffer.write(self.pickledInput())
        self.write(self.pickledInput())
        self.closeWriteChannel()

    def onFinished(self, logic, exitCode, exitStatus):
        self.logger.info(f'finished, code {exitCode}, status {exitStatus}')
        stdout = self.readAllStandardOutput()
        self.usePickledOutput(stdout.data())
        logic.onProcessFinished(self)

class ConvolutionProcess(Process):
    """This is an example of running a process to operate on model data"""

    def __init__(self, scriptPath, initDict, iteration):
        super().__init__(scriptPath)
        self.initDict = copy.deepcopy(initDict)
        self.iteration = iteration
        self.name = f"Iteration {iteration}"

    def pickledInput(self):
        return pickle.dumps(self.initDict)

    def usePickledOutput(self, pickledOutput):
        output = np.frombuffer(pickledOutput, dtype=float)
        #output = pickle.loads(pickledOutput)
        self.result = [self.iteration, output]
</code></pre>

---

## Post #18 by @Alex_Vergara (2020-02-11 14:40 UTC)

<p>Remaining question, Have you tested this in Windows??</p>

---

## Post #19 by @lassoan (2020-02-11 15:00 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="17" data-topic="1044">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>it is not enough to ask pickle to do it</p>
</blockquote>
</aside>
<p>It should be possible to define custom pickling methods for VTK and MRML classes. It would be nice if you could look into this. It may be more elegant than implementing some custom serialization solution for each project.</p>

---

## Post #20 by @Alex_Vergara (2020-02-11 15:05 UTC)

<p>In my case I just output a numpy array in the cpu intensive calculation. But you are right, standard pickling methods would be great, specially for generic intensive computations.</p>
<p>This algorithm can be made generic for any process that basically a class that accepts dictionaries as input (any kind of data wrapped into a dictionary), watch my convolution class:</p>
<pre><code class="lang-python">import numpy as np
import pickle
import sys
import Logic.logging as logging

class Convolution:
    '''convolution class to be runned either sequentially or parallel
    for parallel execution a wrapper class must be implemented as:
        def multi_run_wrapper(args):
            convolution = Convolution(*args) 
            return convolution.convolute()
    where args must be a tuple with
        args = (indexes, p0, DVK, distance_kernel, dens_array, act_array, num, boundary)
    '''
    def __init__(self, indexes, p0, DVK, distance_kernel, dens_array, act_array, num, boundary):
        self.logger = logging.getLogger('Dosimetry4D.convolution')
        self.indexes=indexes
        self.p0=p0
        self.DVK=DVK
        self.distance_kernel=distance_kernel
        self.dens_array=dens_array
        self.act_array=act_array
        self.num=num

    def convolute(self):
        ''' Non homogeneous convolution in a list of voxel (vectorized)
            Variable density correction by distance
        '''

        res = np.zeros_like(self.indexes, dtype=float)
        .....    Computation     .....

        return res

try:
    pickledInput = sys.stdin.buffer.read()
    input = pickle.loads(pickledInput)

    convolution = Convolution(**input) # Making the convolution pickable
    output = convolution.convolute() # Invoking the function is now thread safe

    sys.stdout.buffer.write(pickle.dumps(output))
except Exception as e:
    print(e)
</code></pre>
<p>And the calling method is</p>
<pre><code class="lang-python">                    logic = ProcessesLogic()
                    scriptPath = self.script_path / "Logic" / "Convolution.py"

                    chunks = 100 # to avoid overheading 
                    iteration = 0
                    args1 = {  # wrap arguments for multithreading
                            'p0':p0, 
                            'DVK':self.DVK, 
                            'distance_kernel':self.distanceKernel, 
                            'dens_array':self.densityArray, 
                            'act_array':self.activityArray,
                            'num': num, 
                            'boundary':'repeat'
                    } 
                    while acc &lt; length1:
                        stepsize = max(1, min(int(length1/chunks), length1-acc))
                        lindex = copy.deepcopy(args1)
                        lindex['indexes'] = np.array(indexes[acc:acc + stepsize])
                        convolutionProcess = ConvolutionProcess(scriptPath, lindex, iteration)
                        logic.addProcess(convolutionProcess)
                        acc += stepsize
                        iteration += 1
                    
                    results=[]
                    self.logger.info(f"Launching convolution in {self.CpuCores} CPU cores")
                    slicer.app.processEvents()

                    try:
                        logic.run()
                        canceled = logic.canceled
                    except Exception as e:
                        print(e)
                        return False
</code></pre>

---

## Post #21 by @Alex_Vergara (2020-02-11 15:24 UTC)

<p>For reference, when you use the pickle method to decode the output you will usually get the following error:</p>
<pre><code class="lang-bash">  File "/Users/alexvergaragil/Documents/GIT/dosimetry4d/Dosimetry4D/Logic/Process.py", line 131, in usePickledOutput
    output = pickle.loads(pickledOutput)
_pickle.UnpicklingError: could not find MARK
</code></pre>
<p>This only means pickle does not know how to read the output</p>

---

## Post #22 by @pieper (2020-02-11 18:45 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="18" data-topic="1044" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Remaining question, Have you tested this in Windows??</p>
</blockquote>
</aside>
<p>Yes, my repository works on both windows and mac.</p>

---

## Post #23 by @pieper (2020-02-11 18:52 UTC)

<p>Hi - thanks for testing and for the comments <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>
<p>Let’s move some of the concrete ideas to <a href="https://github.com/pieper/SlicerProcesses/issues">github issues for this repo</a>.</p>
<p>Regarding standard pickling for vtk/Slicer objects yes, I looked into to that but it’s not in my critical path.  There is something in tvtk for pickling.  If this processes approach turns out to fill a general need there are lots of ways to improve it.  I’ll add some notes about potential next steps in the readme file.</p>

---
