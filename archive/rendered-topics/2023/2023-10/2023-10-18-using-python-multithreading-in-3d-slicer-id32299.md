---
topic_id: 32299
title: "Using Python Multithreading In 3D Slicer"
date: 2023-10-18
url: https://discourse.slicer.org/t/32299
---

# Using Python multithreading in 3D Slicer

**Topic ID**: 32299
**Date**: 2023-10-18
**URL**: https://discourse.slicer.org/t/using-python-multithreading-in-3d-slicer/32299

---

## Post #1 by @Hunger-beat (2023-10-18 14:56 UTC)

<p>Dear forum，</p>
<p>I am using Python to write an extension module in 3D Slicer. I need sub threads to perform heavy calculations while also interacting with the UI for some data. I used Python’s threading for multithreading programming, but there were some issues.</p>
<p>When I clicked the push button, the child thread started, but only ran a little before stopping. The child thread can only continue working when I slide the mouse over the image window. This makes me very confused. How can I solve this problem?</p>
<pre><code class="lang-auto">    self.ui.pushButton.clicked.connect(self.testButton)
    def testButton(self):
        self.ui.pushButton.setEnabled(False)
        self.thread1 = threading.Thread(target=self.execute)
        self.thread1.start()

    def execute(self):
        count = 10000000
        while count &gt; 0:  # Simulate time-consuming operations
            if count % 100000 == 0:
                print(count)
            count = count-1
        print("Finished")
        self.ui.pushButton.setEnabled(True)
</code></pre>
<p>I have also read some posts and learned that CLI module or QProcess may be a better solution, but currently I still want to use multithreading to solve it.</p>
<p>Thanks for your help!</p>

---

## Post #2 by @cpinter (2023-10-18 14:59 UTC)

<p>If you use threading in Python with <code>threading</code>, those will also run on the main thread, so it will not be executed on a different core. At least as far as I know.</p>
<p>I suggest you take a look at <a href="https://github.com/pieper/SlicerParallelProcessing" class="inline-onebox">GitHub - pieper/SlicerParallelProcessing: Slicer modules for running subprocesses to operate on data in parallel</a><br>
We successfully use it in a project so although <a class="mention" href="/u/pieper">@pieper</a> says it is still experimental, I can confirm that it works.</p>

---

## Post #3 by @pieper (2023-10-18 17:57 UTC)

<p>Yes, multithreading python is complicated by the <a href="https://en.wikipedia.org/wiki/Global_interpreter_lock">Global Interpreter Lock (GIL)</a>.  As <a class="mention" href="/u/cpinter">@cpinter</a> mentioned, the SlicerParallelProcessing extension is set up so you can transfer data with an instance of Slicer’s python environment running in a different process space.  You can access all the python packages you have installed in you PythonSlicer environment, but you cannot access the GUI or MRML data, only the data you explicitly pass to the subprocess.</p>

---

## Post #4 by @Hunger-beat (2023-10-19 03:09 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/cpinter">@cpinter</a> Sorry for the late reply. Thank you both for your suggestions！ I will start learning parallel processing. However, I still don’t understand this sentence enough. If I want to access GUI or MRML data in subprocess, what should I do?</p>
<aside class="quote no-group" data-username="pieper" data-post="3" data-topic="32299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>but you cannot access the GUI or MRML data, only the data you explicitly pass to the subprocess.</p>
</blockquote>
</aside>
<p>Thank you again for your response and contribution to the community.</p>

---

## Post #5 by @lassoan (2023-10-19 03:17 UTC)

<aside class="quote no-group" data-username="Hunger-beat" data-post="1" data-topic="32299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/hunger-beat/48/67898_2.png" class="avatar"> Hunger-beat:</div>
<blockquote>
<p>When I clicked the push button, the child thread started, but only ran a little before stopping. The child thread can only continue working when I slide the mouse over the image window. This makes me very confused.</p>
</blockquote>
</aside>
<p>When you move the mouse over the image window then you yield the GIL, this way all Python threads get a chance to run for a little. You can automate this regular yielding as it is done in the <a href="https://github.com/SimpleITK/SlicerSimpleFilters/blob/master/SimpleFilters/SimpleFilters.py">SimpleFilters module</a>, by calling Python <code>sleep()</code> function regularly using a <code>QTimer</code>.</p>
<p>This technique allows keeping the GUI responsive while some computation is running in the background, but may not improve performance. See some more information about this <a href="https://pythonspeed.com/articles/python-gil/">here</a>.</p>
<p>If you want to improve performance (not just GUI responsiveness):</p>
<ul>
<li>If the code in the background thread does not release the GIL (e.g., pure Python code that operates on Python objects) then execution will not be faster by introducing more threads. You can run the processing code in a different process, for example using ParallelProcessing Slicer extension.</li>
<li>If the code in the background thread releases the GIL for significant time periods then you get true parallelism: your code may use multiple CPU cores. For example, <em>SimpleITK</em> releases the GIL, so if you use SimpleITK filters in your background thread then you will get not just responsive GUI but also processing code running in parallel with Python code. <em>VTK</em> does not release the GIL in Slicer (it would require setting a hidden <code>VTK_PYTHON_FULL_THREADSAFE</code> CMake flag to do so - see <a href="https://stackoverflow.com/questions/65928669/python-vtk-and-gil-release">here</a>).</li>
</ul>
<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/cpinter">@cpinter</a> <a class="mention" href="/u/jcfr">@jcfr</a> If we want to improve Python threading support in Slicer, then we could consider:</p>
<ul>
<li>yielding the Python GIL using a timer (so that Python threads just work, without each developer having to set up this mechanism)</li>
<li>build VTK with <code>VTK_PYTHON_FULL_THREADSAFE=ON</code> (to allow VTK to run in background Python threads without blocking Python code execution on other threads)</li>
</ul>

---

## Post #6 by @Hunger-beat (2023-10-19 03:40 UTC)

<p>Thank you very much for your reply! I think using QTimer may be useful, and I will give it a try later. In addition, I will also try to learn ParallelProcessing to see which method is more suitable for me. Because I have just come into contact with Slicer, I am not very familiar with these. Thank you again for your help!</p>

---

## Post #7 by @cpinter (2023-10-19 08:29 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="32299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>VTK_PYTHON_FULL_THREADSAFE=ON</p>
</blockquote>
</aside>
<p>Are you aware of any drawback related to enabling this flag? It seems a quick and clean way to improve multi-threading if it does not cause other issues. At least much of the Python processing code I have written has VTK calls all over the place, so it seems to be quite relevant.</p>

---

## Post #8 by @lassoan (2023-10-19 12:10 UTC)

<p>The GIL is a mutex, so there is an extra cost in each VTK Python call because of its unlocking and locking. In most cases it is probably insignificant, as Python is very slow anyway. But we should stress test this a bit to make sure we don’t introduce any perceivable slowdown in normal single-threaded operation. We could ask ParaView/VTK developers about this, too, as they have more experience with this.</p>

---

## Post #9 by @pieper (2023-10-19 14:02 UTC)

<p><a class="mention" href="/u/hunger-beat">@Hunger-beat</a> a lot depends on what you are doing in the threads.  This is a longstanding issue.  As you can <a href="https://www.na-mic.org/wiki/2013_Project_Week:Threaded_SimpleITK_Modules">see on this page</a> SimpleITK GIL support was added in 2013, using methods discussed on the VTK mailing list in 2005.  Using a thread and releasing the GIL when calling long-running C or C++ code makes sense since it can run independent of Python.  But it doesn’t make sense if the code is executing Python or interacting with the GUI, which are single threaded.</p>
<aside class="quote no-group" data-username="lassoan" data-post="5" data-topic="32299">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>build VTK with <code>VTK_PYTHON_FULL_THREADSAFE=ON</code></p>
</blockquote>
</aside>
<p>I’ve never tried that, but it might be okay.  I agree we’d need to check if it introduces subtle bugs or performance issues.</p>

---

## Post #10 by @Hunger-beat (2023-10-20 05:39 UTC)

<p>Okay, I understand. I will study carefully. Thank you again for your answers!</p>

---

## Post #11 by @zina (2024-07-15 13:43 UTC)

<p>Did you implement  improve “Python threading support in Slicer” already?</p>

---

## Post #12 by @lassoan (2024-07-15 15:00 UTC)

<p>There has not been much interest in this since this discussion last year (perhaps because threading in Python does not actually mean parallel execution, so not really impactful), so we did not make any changes. You can do the same what is done in SimpleFilters module (calling Python <code>sleep()</code> function regularly using a <code>QTimer</code> - see details above) and let us know if you find it useful.</p>

---
