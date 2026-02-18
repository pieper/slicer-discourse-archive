# Run a Python script as subprocess from Slicer

**Topic ID**: 22668
**Date**: 2022-03-24
**URL**: https://discourse.slicer.org/t/run-a-python-script-as-subprocess-from-slicer/22668

---

## Post #1 by @lb123 (2022-03-24 12:18 UTC)

<p>Hi,<br>
can you please tell me how I can run a python script as a subprocess from Slicer?<br>
I would like to lauch a python file from the logic of my module.</p>
<p>Thank you</p>

---

## Post #2 by @ebrahim (2022-03-24 12:22 UTC)

<p>Maybe <code>slicer.util.launchConsoleProcess</code> could work for this</p>

---

## Post #3 by @lassoan (2022-03-26 04:21 UTC)

<p>You can also run your Python script as a CLI module. Slicer automatically generates a GUI for specifying inputs and outputs; and you can also run the script as any other CLI module. See a complete example here: <a href="https://github.com/lassoan/SlicerPythonCLIExample" class="inline-onebox">GitHub - lassoan/SlicerPythonCLIExample: Example extension for 3D Slicer that demonstrates how to make a Python script available as a CLI module</a></p>

---

## Post #4 by @lb123 (2022-03-28 07:57 UTC)

<p>Thank you for your reply.</p>
<p>I noticed that the python script runned as a CLI module is much slower than if I run it from an external command prompt.</p>
<p>Do you know any possible reason?</p>
<p>Thank you</p>

---

## Post #5 by @lassoan (2022-03-28 11:16 UTC)

<p>You can get definitive answer by using a Python profiler, but a likely root cause is excessive logging. See more details here:</p>
<aside class="quote quote-modified" data-post="1" data-topic="18742">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/third-party-library-works-slower-inside-slicers-python-shell-why-how-to-do-performance-profiling/18742">Third party library works slower inside Slicer's Python shell - why? how to do performance profiling?</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" style="--category-badge-color: #25AAE2; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Hi, 
I’m trying to use python package <a href="https://github.com/kinverarity1/lasio" rel="noopener nofollow ugc">lasio</a>. It is geological library and its main purpose is to read textual files of format .las 
After installing it (pip install lasio) I can use it as follows: 
import lasio
las = lasio.read("path/to/las/file")    # I provide an example file below

The problem is that if I read this .las file (via command las = lasio.read("path/to/las/file")) in Slicer’s python shell then it works noticeably slower (about 5 seconds) than when I open PythonSlicer.exe in Window…
  </blockquote>
</aside>


---

## Post #6 by @lb123 (2022-03-28 11:43 UTC)

<p>Thank you.</p>
<p>I also tried to run a simple os.system from the logic of my Slicer module:</p>
<pre><code class="lang-auto">import os
.
.
.

path_to_python = "python_path//"
os.system(f"{path_to_python}python.exe myscript.py")
</code></pre>
<p>but I am getting this error:</p>
<pre><code class="lang-auto">module 'os' has no attribute 'add_dll_directory'
</code></pre>
<p>While if I do the same from a Windows command prompt it works well:</p>
<pre><code class="lang-auto">import os
path_to_python = "python_path//"
os.system(f"{path_to_python}python.exe myscript.py")
</code></pre>
<p>Do you know the reason for this behaviour?</p>
<p>Thank you</p>

---

## Post #7 by @lassoan (2022-03-28 12:13 UTC)

<p><code>os.system</code> is a very rudimentary tool, you cannot control the used environment, output redirections, ownership of thr process, etc. Use <code>subprocess</code> instead. Set example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#launch-external-process-in-startup-environment">here</a>.</p>
<p>There is also the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.launchConsoleProcess"><code>slicer.util.launchConsoleProcess</code></a> function that conveniently redirects outputs, sets the environment, hides the console, gives access to the process so that you can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.logProcessOutput">log its outputs</a> or if user requests then terminate the process.</p>
<p>If you want to run Python then you can use Slicer’s Python environment as shown <a href="https://github.com/Slicer/Slicer/blob/b362a139d35373c6cccfff501c3935c482c52024/Base/Python/slicer/util.py#L3287-L3307">here</a>.</p>

---

## Post #8 by @Saima (2023-02-06 04:42 UTC)

<p>Hi Andras,<br>
I have created a slicerpythonscriptedcli module. Is it possible to call subprocess_check_out to run a program using anaconda.</p>
<p>I am using some libraries that are installed in an enviornment in anaconda thats why I am calling the external python to run a program.</p>
<p>Please let me know how can i do it.</p>
<p>I receive the following error:</p>
<p>Traceback (most recent call last):<br>
File “/home/useradmin/Slicer-4.11.20210226-linux-amd64/Scheduler/scheduler/scheduler.py”, line 68, in<br>
main(sys.argv[1], float(sys.argv[2]), sys.argv[3], sys.argv[4], sys.argv[5])<br>
File “/home/useradmin/Slicer-4.11.20210226-linux-amd64/Scheduler/scheduler/scheduler.py”, line 50, in main<br>
command_result = check_output(command_line, env=slicer.util.startupEnvironment())<br>
File “/home/useradmin/Slicer-4.11.20210226-linux-amd64/bin/Python/slicer/util.py”, line 106, in startupEnvironment<br>
startupEnv = slicer.app.startupEnvironment()<br>
AttributeError: module ‘slicer’ has no attribute ‘app’</p>
<p>regards,<br>
Saima</p>

---

## Post #9 by @lassoan (2023-02-06 16:34 UTC)

<p><code>slicer.util.startupEnvironment()</code> requires that you run the script using <code>./Slicer</code> executable (and not using <code>./PythonSlicer</code> executable).</p>
<p>You could get the startup environment by calling the <code>ctkAppLauncherEnvironment::environment(0)</code> method in C++, but the only Python-wrapped class that exposes this method is qSlicerCoreApplication. If you start your Python script using <code>./PythonSlicer</code> then no Qt application class is created, so you would need to add a new C++ class that allows you to call this function.</p>
<aside class="quote no-group" data-username="Saima" data-post="8" data-topic="22668">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>I am using some libraries that are installed in an enviornment in anaconda thats why I am calling the external python to run a program.</p>
</blockquote>
</aside>
<p>It would be much simpler to install the libraries using PyPI into Slicer’s Python environment. What are these libraries?</p>

---

## Post #10 by @Saima (2023-02-07 02:23 UTC)

<p>Its a toolkit, bratstoolkit for tumour segmentation.</p>
<p>regards,<br>
Saima</p>

---

## Post #11 by @Saima (2023-02-07 02:30 UTC)

<p>Hi andras,<br>
can I run check_output or run without env variable and run the process outside the slicer in an anaconda enviornment and get the results and avoid running into error due to startupenviornment.</p>
<p>At this stage I have to not use anything from slicer but after the processing the output is a volume(.nrrd), which I will export and do some processing on it.</p>
<p>regards,<br>
Saima Safdar</p>

---

## Post #12 by @lassoan (2023-02-07 13:58 UTC)

<aside class="quote no-group" data-username="Saima" data-post="10" data-topic="22668">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/9d8465/48.png" class="avatar"> Saima:</div>
<blockquote>
<p>Its a toolkit, bratstoolkit for tumour segmentation.</p>
</blockquote>
</aside>
<p>You can pip install it in Slicer’s Python environment (<code>PythonSlicer.exe -m pip install BraTS-Toolkit</code>). There should be no need to mess with anaconda.</p>
<p>There is a problem that this package pins a very specific version of SimpleITK (and a couple of other Python packages), which makes Slicer remove the special SimpleITK distribution that is bundled with Slicer, so modules that rely on SimpleITK may stop working. See <a href="https://discourse.slicer.org/t/did-sitkutils-pullvolumefromslicer-break-with-slicer-5-2/26863/9" class="inline-onebox">Did sitkUtils.PullVolumeFromSlicer() break with Slicer 5.2? - #9 by lassoan</a> for more details.</p>
<p>Another bad thing about this <a href="https://github.com/neuronflow/BraTS-Toolkit">bratstoolkit</a> is that it comes with the strictest possible copyleft license. If you use this code then you must make all other code in the same project public. Probably you can find other segmentation toolkits that provide similar features and do not come with such heavy restrictions.</p>

---

## Post #13 by @Saima (2023-02-08 03:13 UTC)

<p>Hi Andras,<br>
For the bratstoolkit, may be I could run it outside the slicer and get the results back into the slicer using the subprocess command and make the scripted module.</p>
<p>Is this ok? because if i dont install within slicer I will not have the SimpleITK issue.<br>
The only thing I need for scripted module is how cani display the output or errors like in the<br>
pythonCLi based module. That is a desperate post.</p>
<p>Can you suggest some other tumour segmentation toolkits ?</p>
<p>regards,<br>
Saima</p>

---

## Post #14 by @Saima (2024-05-06 07:59 UTC)

<p>Hi Andras,<br>
I have submitted the batchBrainMRSegmentation extension. The suggestion is to make CLI modules for each of the files I am calling through the main scripted python module.</p>
<p>I started making the cli module. It did install the bratstoolkit but I am getting this error now. Please see below. How can I proceed further. Please help.</p>
<p>Error response from daemon: No such container: greedy_elephant<br>
Error: No such container: greedy_elephant<br>
Error response from daemon: No such container: greedy_elephant<br>
docker: Error response from daemon: could not select device driver “” with capabilities: [[gpu]].<br>
Error: No such container: greedy_elephant<br>
Error: No such container: greedy_elephant<br>
Error: No such container: greedy_elephant<br>
Error: No such container: greedy_elephant<br>
Traceback (most recent call last):<br>
File “/media/useradmin/Disk2/Slicer-5.7.0-2024-03-25-linux-amd64(1)/Slicer-5.7.0-2024-03-25-linux-amd64/lib/Python/lib/python3.9/site-packages/socketio/client.py”, line 280, in connect<br>
self.eio.connect(url, headers=headers, transports=transports,<br>
File “/media/useradmin/Disk2/Slicer-5.7.0-2024-03-25-linux-amd64(1)/Slicer-5.7.0-2024-03-25-linux-amd64/lib/Python/lib/python3.9/site-packages/engineio/client.py”, line 194, in connect<br>
return getattr(self, ‘<em>connect</em>’ + self.transports[0])(<br>
File “/media/useradmin/Disk2/Slicer-5.7.0-2024-03-25-linux-amd64(1)/Slicer-5.7.0-2024-03-25-linux-amd64/lib/Python/lib/python3.9/site-packages/engineio/client.py”, line 300, in _connect_polling<br>
raise exceptions.ConnectionError(<br>
engineio.exceptions.ConnectionError: Connection refused by the server</p>
<p>During handling of the above exception, another exception occurred:</p>
<p>Traceback (most recent call last):<br>
File “/media/useradmin/Disk2/Slicer-5.7.0-2024-03-25-linux-amd64(1)/Slicer-5.7.0-2024-03-25-linux-amd64/SlicerBratsPreprocessor/BratsPreprocessor/BratsPreprocessor.py”, line 79, in <br>
main(sys.argv[2], sys.argv[3], sys.argv[4],  sys.argv[5], sys.argv[6], sys.argv[7])<br>
File “/media/useradmin/Disk2/Slicer-5.7.0-2024-03-25-linux-amd64(1)/Slicer-5.7.0-2024-03-25-linux-amd64/SlicerBratsPreprocessor/BratsPreprocessor/BratsPreprocessor.py”, line 60, in main<br>
prep.single_preprocess(t1File=t1File, t1cFile=t1cFile, t2File=t2File, flaFile=flaFile, outputFolder=outputDir, mode=“gpu”, confirm=True, skipUpdate=False, gpuid=‘0’)<br>
File “/media/useradmin/Disk2/Slicer-5.7.0-2024-03-25-linux-amd64(1)/Slicer-5.7.0-2024-03-25-linux-amd64/lib/Python/lib/python3.9/site-packages/brats_toolkit/preprocessor.py”, line 127, in single_preprocess<br>
self.batch_preprocess(<br>
File “/media/useradmin/Disk2/Slicer-5.7.0-2024-03-25-linux-amd64(1)/Slicer-5.7.0-2024-03-25-linux-amd64/lib/Python/lib/python3.9/site-packages/brats_toolkit/preprocessor.py”, line 168, in batch_preprocess<br>
self._connect_client()<br>
File “/media/useradmin/Disk2/Slicer-5.7.0-2024-03-25-linux-amd64(1)/Slicer-5.7.0-2024-03-25-linux-amd64/lib/Python/lib/python3.9/site-packages/brats_toolkit/preprocessor.py”, line 172, in _connect_client<br>
self.sio.connect(“<a href="http://localhost:5000" rel="noopener nofollow ugc">http://localhost:5000</a>”)<br>
File “/media/useradmin/Disk2/Slicer-5.7.0-2024-03-25-linux-amd64(1)/Slicer-5.7.0-2024-03-25-linux-amd64/lib/Python/lib/python3.9/site-packages/socketio/client.py”, line 283, in connect<br>
self._trigger_event(<br>
File “/media/useradmin/Disk2/Slicer-5.7.0-2024-03-25-linux-amd64(1)/Slicer-5.7.0-2024-03-25-linux-amd64/lib/Python/lib/python3.9/site-packages/socketio/client.py”, line 555, in _trigger_event<br>
return self.handlers[namespace]<a>event</a><br>
TypeError: connect_error() takes 0 positional arguments but 1 was given</p>

---
