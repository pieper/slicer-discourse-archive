---
topic_id: 8596
title: "Slicer Crashes When Using Qthreadpool To Start Qrunnable In"
date: 2019-09-27
url: https://discourse.slicer.org/t/8596
---

# Slicer crashes when using QThreadPool to start QRunnable in python module

**Topic ID**: 8596
**Date**: 2019-09-27
**URL**: https://discourse.slicer.org/t/slicer-crashes-when-using-qthreadpool-to-start-qrunnable-in-python-module/8596

---

## Post #1 by @Guangshan_Chen (2019-09-27 22:17 UTC)

<p>I Would like to move some jobs to another QThread to avoid the frozen of the main thread (GUI).</p>
<p>I tried python ThreadPoolExecutor to create a thread. However, the child thread is too slow. According to the suggestion of <a href="https://discourse.slicer.org/t/multithreading-in-extension/6941">multithreading-in-extension</a>, I tried QTimer. It also frozen GUI.</p>
<p>Now I am trying QThreadPool by following <a href="https://www.learnpyqt.com/courses/concurrent-execution/multithreading-pyqt-applications-qthreadpool/" rel="nofollow noopener">multithreading in pyqt</a> example:</p>
<pre><code class="lang-auto">import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *

class Worker(qt.QRunnable):
    '''
    Worker thread
    '''

    def __init__(self):
        super(Worker, self).__init__()

    def run(self):
        '''
        Your code goes in this function
        '''
        print("Thread start")
        time.sleep(5)
        print("Thread complete")

class TestWidget(ScriptedLoadableModuleWidget):
    def __init__(self):
        self.thread_pool = qt.QThreadPool()

    def setup(self):
         ScriptedLoadableModuleWidget.setup(self)
         parametersCollapsibleButton = ctk.ctkCollapsibleButton()
         parametersCollapsibleButton.text = "Parameters"
         self.layout.addWidget(parametersCollapsibleButton)

         parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)


         self.listenButton = qt.QPushButton("Test")
         self.listenButton.toolTip = "Test"
         self.listenButton.enabled = True
         self.listenButton.connect('clicked(bool)', self.onListenButton)
         parametersFormLayout.addRow(self.listenButton)

    def onListenButton(self):
        self.worker = Worker() 
        self.thread_pool.start(self.worker)
      
</code></pre>
<p>If I click the button to test it, slicer crashes with the following error:<br>
"<br>
Received signal 11 SEGV_MAPERR 559d00000002<br>
<span class="hashtag">#0</span> 0x7f58faea558f <br>
<span class="hashtag">#1</span> 0x7f58f98d785d <br>
<span class="hashtag">#2</span> 0x7f58faea5a9e <br>
<span class="hashtag">#3</span> 0x7f58e49ff890 <br>
<span class="hashtag">#4</span> 0x7f58eaddfe2d QThreadPoolThread::run()<br>
<span class="hashtag">#5</span> 0x7f58eade9554 QThreadPrivate::start()<br>
<span class="hashtag">#6</span> 0x7f58e49f46db start_thread<br>
<span class="hashtag">#7</span> 0x7f58d877e88f clone<br>
"<br>
I have no idea what is wrong.<br>
Could anyone point me how to create QThread in Slicer with Python? Thanks.</p>

---

## Post #2 by @lassoan (2019-09-28 19:45 UTC)

<p>Python multi-threading is really messy in general and it is further complicated by using a Python interpreter embedded in an application.</p>
<p>I would recommend running background processing in a <a href="https://github.com/lassoan/SlicerPythonCLIExample" rel="nofollow noopener">Python CLI module</a> (which runs processing in a separate process) or implement it in a C++ loadable module (where you can use QThread).</p>

---

## Post #3 by @Guangshan_Chen (2019-09-30 13:44 UTC)

<p>Thank you very much!</p>

---

## Post #4 by @Alex_Vergara (2019-09-30 13:53 UTC)

<p>you can do the following:</p>
<pre><code class="lang-python">    def onListenButton(self):
        self.worker = Worker() 
        original_stdin = sys.stdin # Unlock SlicerPython GIL
        sys.stdin = open(os.devnull)
        try:
            self.thread_pool.start(self.worker)
        except Exception as e: # Is something wrong happens, force to terminate the pool
            self.thread_pool.terminate()
        finally:
            self.thread_pool.join()
            sys.stdin.close() # Restores SlicerPython GIL
            sys.stdin = original_stdin
</code></pre>
<p>This shall work <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=9" title=":wink:" class="emoji" alt=":wink:"></p>

---

## Post #5 by @lassoan (2019-09-30 13:57 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="4" data-topic="8596">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>original_stdin = sys.stdin # Unlock SlicerPython GIL</p>
</blockquote>
</aside>
<p>Do you know what are the side effects of this?</p>

---

## Post #6 by @Alex_Vergara (2019-09-30 13:59 UTC)

<p>yep, if you try to do this more than once slicer crashes, but if you wait  until the end it works pretty well. So you shall enforce some kind of lock yourself.<br>
Oh, and this only works with python3, I forgot to mention this.</p>

---

## Post #7 by @Alex_Vergara (2019-09-30 15:02 UTC)

<p>To elaborate more on this: <code>SlicerPython</code> is attached to the console which is locked by slicer itself, this procedure liberates temporarily the console input and sets a virtual input with no owner (no GIL). If you try to use slicer console while it is calculating, then <code>SlycerPython</code> will not read from it (not that bad). If you try to execute the pool again while is being executed then the system will see colliding threads and will kill slicer.</p>

---

## Post #8 by @Guangshan_Chen (2019-09-30 15:32 UTC)

<p>Thank you very much. I just tried the new code of onListenButton function.<br>
I got the new errors as the following"</p>
<p>Received signal 11 SEGV_MAPERR 0000000000a0<br>
<span class="hashtag">#0</span> 0x7f7f1721558f <br>
<span class="hashtag">#1</span> 0x7f7f15c4785d <br>
<span class="hashtag">#2</span> 0x7f7f17215a9e <br>
<span class="hashtag">#3</span> 0x7f7f00d6f890 <br>
<span class="hashtag">#4</span> 0x7f7f0c259d70 tupledealloc<br>
<span class="hashtag">#5</span> 0x7f7f0c2473c6 _PyCFunction_FastCallDict<br>
<span class="hashtag">#6</span> 0x7f7f0c1eaa9e _PyObject_FastCallDict<br>
<span class="hashtag">#7</span> 0x7f7f0c21045b PyFile_WriteObject<br>
<span class="hashtag">#8</span> 0x7f7f0c21053b PyFile_WriteString<br>
<span class="hashtag">#9</span> 0x7f7f0c326e7a PyTraceBack_Print<br>
<span class="hashtag">#10</span> 0x7f7f0c31abcf print_exception_recursive<br>
<span class="hashtag">#11</span> 0x7f7f0c31bb48 PyErr_Display<br>
<span class="hashtag">#12</span> 0x7f7f0c3237c8 sys_excepthook<br>
<span class="hashtag">#13</span> 0x7f7f0c2473ad _PyCFunction_FastCallDict<br>
<span class="hashtag">#14</span> 0x7f7f0c1eaa9e _PyObject_FastCallDict<br>
<span class="hashtag">#15</span> 0x7f7f0c31bcdc PyErr_PrintEx<br>
<span class="hashtag">#16</span> 0x7f7f10b19a54 PythonQt::handleError()<br>
<span class="hashtag">#17</span> 0x7f7f10bc0de1 PythonQtSignalTarget::call()<br>
<span class="hashtag">#18</span> 0x7f7f10bc0e06 PythonQtSignalTarget::call()<br>
<span class="hashtag">#19</span> 0x7f7f10bc1625 PythonQtSignalReceiver::qt_metacall()<br>
<span class="hashtag">#20</span> 0x7f7f0733c504 QMetaObject::activate()<br>
<span class="hashtag">#21</span> 0x7f7f0824e1f2 QAbstractButton::clicked()<br>
<span class="hashtag">#22</span> 0x7f7f0824e3f4 QAbstractButtonPrivate::emitClicked()<br>
<span class="hashtag">#23</span> 0x7f7f0824ff8e QAbstractButtonPrivate::click()<br>
<span class="hashtag">#24</span> 0x7f7f082500e5 QAbstractButton::mouseReleaseEvent()<br>
<span class="hashtag">#25</span> 0x7f7f10e73a05 PythonQtShell_QPushButton::mouseReleaseEvent()<br>
<span class="hashtag">#26</span> 0x7f7f081994c8 QWidget::event()<br>
<span class="hashtag">#27</span> 0x7f7f10e726d7 PythonQtShell_QPushButton::event()<br>
<span class="hashtag">#28</span> 0x7f7f0815cdac QApplicationPrivate::notify_helper()<br>
<span class="hashtag">#29</span> 0x7f7f08164833 QApplication::notify()<br>
<span class="hashtag">#30</span> 0x7f7f1eee6536 qSlicerApplication::notify()<br>
<span class="hashtag">#31</span> 0x7f7f073114e8 QCoreApplication::notifyInternal2()<br>
<span class="hashtag">#32</span> 0x7f7f0816348f QApplicationPrivate::sendMouseEvent()<br>
<span class="hashtag">#33</span> 0x7f7f081b301d QWidgetWindow::handleMouseEvent()<br>
<span class="hashtag">#34</span> 0x7f7f081b5913 QWidgetWindow::event()<br>
<span class="hashtag">#35</span> 0x7f7f0815cdac QApplicationPrivate::notify_helper()<br>
<span class="hashtag">#36</span> 0x7f7f08163e57 QApplication::notify()<br>
<span class="hashtag">#37</span> 0x7f7f1eee6536 qSlicerApplication::notify()<br>
<span class="hashtag">#38</span> 0x7f7f073114e8 QCoreApplication::notifyInternal2()<br>
<span class="hashtag">#39</span> 0x7f7f0793fe37 QGuiApplicationPrivate::processMouseEvent()<br>
<span class="hashtag">#40</span> 0x7f7f07941d35 QGuiApplicationPrivate::processWindowSystemEvent()<br>
<span class="hashtag">#41</span> 0x7f7f0791bb7b QWindowSystemInterface::sendWindowSystemEvents()<br>
<span class="hashtag">#42</span> 0x7f7ee9fceb8b QPAEventDispatcherGlib::processEvents()<br>
<span class="hashtag">#43</span> 0x7f7f0730fe4a QEventLoop::exec()<br>
<span class="hashtag">#44</span> 0x7f7f07318850 QCoreApplication::exec()<br>
<span class="hashtag">#45</span> 0x7f7f1d90d2aa qSlicerCoreApplication::exec()<br>
<span class="hashtag">#46</span> 0x55bfa73abc87 main<br>
<span class="hashtag">#47</span> 0x7f7ef49eeb97 __libc_start_main</p>

---

## Post #9 by @Alex_Vergara (2019-09-30 16:08 UTC)

<p>instead of using <code>terminate</code> and <code>join</code>, try using <code>quit</code> and <code>wait</code> respectively as they are the recommended with QThreadPool.</p>
<p>Anyways, if you want to try the <code>multiprocessing</code> module</p>
<pre><code class="lang-python">from multiprocessing import Pool

def worker_wrapper(args):
    worker = Worker(*args)
    return worker.run()

original_stdin = sys.stdin # Unlock SlicerPython GIL
sys.stdin = open(os.devnull)
args = tuple('your arguments here, can be empty so you can omit args')
p = Pool(self.CpuCores)
try: # Start producing results
    iresults = p.imap(worker_wrapper, args) # This is an iterator pointer
    p.close()
    for i, result in enumerate(iresults):
        print("performed {} threads".format(i)) # Here you can follow your threads progress ;)

except Exception as e: # Is something wrong happens, force to terminate the pool
    canceled = True # Necesary, no "return False" allowed here
    p.terminate()
    logging.error(e)

finally:
    p.join()
    sys.stdin.close()
    sys.stdin = original_stdin
</code></pre>

---

## Post #10 by @lassoan (2019-09-30 16:24 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="7" data-topic="8596" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>To elaborate more on this: <code>SlicerPython</code> is attached to the console which is locked by slicer itself, this procedure liberates temporarily the console input and sets a virtual input with no owner (no GIL). If you try to use slicer console while it is calculating, then <code>SlycerPython</code> will not read from it (not that bad). If you try to execute the pool again while is being executed then the system will see colliding threads and will kill slicer.</p>
</blockquote>
</aside>
<p>This sounds very fragile. Python CLI or C++ module options are much more reliable. Currently, Slicer’s scheduler runs Python CLIs one by one, but it would be possible to change this so that tasks that do not depend on completion of other tasks could all run in parallel.</p>

---

## Post #11 by @Guangshan_Chen (2019-09-30 16:24 UTC)

<p>Thank you very much! After I try it and get back to you.</p>

---

## Post #12 by @jamesobutler (2019-09-30 18:51 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="10" data-topic="8596">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Currently, Slicer’s scheduler runs Python CLIs one by one, but it would be possible to change this</p>
</blockquote>
</aside>
<p>We previously had a discussion (<a href="https://discourse.slicer.org/t/running-multiple-clis-at-once/7686" class="inline-onebox">Running multiple CLIs at once</a>) about this, but didn’t take any action yet.</p>

---

## Post #13 by @Guangshan_Chen (2019-10-02 19:38 UTC)

<p>Update:</p>
<p>I have sub-process working with ProcessPoolExecutor.</p>

---

## Post #14 by @Alex_Vergara (2019-10-03 08:58 UTC)

<p>May you please add your final solution?</p>

---

## Post #15 by @Guangshan_Chen (2019-10-03 18:31 UTC)

<p>Sure.</p>
<pre><code class="lang-auto">import vtk, qt, ctk, slicer
from slicer.ScriptedLoadableModule import *
from concurrent.futures import ProcessPoolExecutor

def task():
   print("sub process start")
   time.sleep(5)
   print("sub process done")

def task_done(future):
    if future.cancelled():
        print("task is cancelled!")
    elif future.done():
        error = future.exception()
        if error:
            print("task error")
        else:
            print(" task is done")

class TestWidget(ScriptedLoadableModuleWidget):
    def __init__(self):
        self.process_executor = ProcessPoolExecutor(max_workers=3)

    def setup(self):
         ScriptedLoadableModuleWidget.setup(self)
         parametersCollapsibleButton = ctk.ctkCollapsibleButton()
         parametersCollapsibleButton.text = "Parameters"
         self.layout.addWidget(parametersCollapsibleButton)

         parametersFormLayout = qt.QFormLayout(parametersCollapsibleButton)


         self.listenButton = qt.QPushButton("Test")
         self.listenButton.toolTip = "Test"
         self.listenButton.enabled = True
         self.listenButton.connect('clicked(bool)', self.onListenButton)
         parametersFormLayout.addRow(self.listenButton)

    def onListenButton(self):
        original_stdin = sys.stdin
        sys.stdin = open(os.devnull)
        try:
            ex = self.process_executor.submit(task)
            ex.add_done_callback(task_done)
        finally:
            sys.stdin.close()
            sys.stdin = original_stdin
</code></pre>

---

## Post #16 by @Alex_Vergara (2019-10-04 07:40 UTC)

<p>Remember to add a mutex to prevent duplicated calls to <code>onListenButton</code>, if you call it again while it is being executed it will make Slicer to crash.</p>

---

## Post #17 by @Guangshan_Chen (2019-10-04 15:48 UTC)

<aside class="quote no-group" data-username="Alex_Vergara" data-post="16" data-topic="8596">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/alex_vergara/48/15205_2.png" class="avatar"> Alex_Vergara:</div>
<blockquote>
<p>Remember to add a mutex to prevent duplicated calls</p>
</blockquote>
</aside>
<p>Thanks for the suggestion.</p>
<p>I found this poster here talking about using <a href="https://stackoverflow.com/questions/35394373/processpoolexecutor-and-lock-in-python" rel="noopener nofollow ugc">multiprocessing.Manager</a>. Due to the stdin problem, it does not working in Slicer.<br>
I simply set a flag before call the subprocess and reset it in callback function.</p>

---
