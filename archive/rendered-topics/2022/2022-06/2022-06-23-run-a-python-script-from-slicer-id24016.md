# Run a python script from Slicer

**Topic ID**: 24016
**Date**: 2022-06-23
**URL**: https://discourse.slicer.org/t/run-a-python-script-from-slicer/24016

---

## Post #1 by @koeglfryderyk (2022-06-23 23:48 UTC)

<p>I want to run a custom python script from slicer in a custom virtual environment.</p>
<p>I tried:</p>
<ul>
<li>
<code>slicer.util.launchConsoleProcess()</code>, as suggested <a href="https://discourse.slicer.org/t/run-a-python-script-as-subprocess-from-slicer/22668">here</a>, but I couldn’t figure out how to specify my custom venv</li>
<li>I tried using <code>subprocess.call(cmd, shell=True, executable='/bin/bash')</code>, where <code>cmd = "source path/to/venv/bin/activate; python3 path/to/script.py</code> (I tried this with <code>.</code> instead of source or without source but nothing worked)</li>
</ul>
<p>I also tried a somewhat convoluted way that was the closest to working: <code>subprocess.run(command_line, env=slicer.util.startupEnvironment())</code>, where <code>command_line=["path/to/venv/bin/python3.7", "path/to/intermediate/script.py"]</code> and the intermediate python file contains an os.system call with the venv and ‘real’ script specified</p>
<ul>
<li>I wrote that it partially worked because I get a return code of 0, and the loading circle in slicer appears for a moment - so I’m guessing the ‘real’ script started but then closed after a moment<br>
(the script I want to run is a script that continuously sends data to Slicer, where my extension then uses this data to update markups)</li>
</ul>
<p>It seemed to me like I tried all the options that If found here on Discourse, but maybe I missed something.</p>

---

## Post #2 by @lassoan (2022-06-24 04:49 UTC)

<p>I would expect that <code>launchConsoleProcess</code> would work if you launch a wrapper bash script (that activates the virtual environment and launches your Python script). Maybe first start with a very simple script (e.g., that prints a short message or creates a new file).</p>
<p>Is there a particular reason you cannot run your script in Slicer’s virtual Python environment (using <code>PythonSlicer</code> executable)?</p>

---

## Post #3 by @koeglfryderyk (2022-06-24 14:12 UTC)

<p>I just tried using a bash script but I also couldn’t make it work.</p>
<p>That’s my script (which I can execute on my mac) - the python file creates a dummy directory:</p>
<pre><code class="lang-auto">#! /usr/bin/env python
source /Users/fryderykkogl/Documents/university/master/thesis/code.nosync/venvs.nosync/mpipe/bin/activate
python3 /Users/fryderykkogl/Documents/university/master/thesis/code.nosync/x-nav/x.py
</code></pre>
<p><br>
I run it with<br>
<code>slicer.util.launchConsoleProcess(["/Users/fryderykkogl/Documents/university/master/thesis/code.nosync/x-nav/wrapper.sh"])</code></p>
<p>I first got a permission error which I fixed with chmod but now I get this error which I cannot get rid of:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "/Applications/Slicer_debug.app/Contents/bin/Python/slicer/util.py", line 3384, in launchConsoleProcess
    proc = subprocess.Popen(args, env=startupEnv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, cwd=cwd)
  File "/Applications/Slicer_debug.app/Contents/lib/Python/lib/python3.9/subprocess.py", line 951, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/Applications/Slicer_debug.app/Contents/lib/Python/lib/python3.9/subprocess.py", line 1821, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
OSError: [Errno 8] Exec format error: '/Users/fryderykkogl/Documents/university/master/thesis/code.nosync/x-nav/wrapper.sh'
</code></pre>
<p><br>
I don’t think there is a reason, but I also can’t figure out how to use PythonSlicer from within Slicer. I can use PythonSlicer from my terminal, but I run into the same problems as with my venv when I do it in Slicer</p>
<p>A note on ‘the big picture’ - I want to have a button in my custom extension, which when pressed, executes this custom script</p>

---

## Post #4 by @pieper (2022-06-24 17:50 UTC)

<p>You need to add <code>/bin/bash</code> as the first element of the list being passed to <code>launchConsoleProcess</code>.</p>

---

## Post #5 by @koeglfryderyk (2022-06-24 23:14 UTC)

<p>That helped, thanks!!</p>
<p>However, my script now crashes at this line of code:<br>
<code>cap = cv2.VideoCapture(0)</code></p>
<p>(again, it crashes only when I try to execute it through Slicer - it runs fine when executed through my terminal)</p>
<p>I accessed the results of <code>p = launchConsoleProcess()</code> with <code>p.communicate()</code> and this was the error:</p>
<pre><code class="lang-auto">OpenCV: not authorized to capture video (status 0), requesting...
</code></pre>
<p>Also, Python crashes and I get a report which, amongst other things, says:</p>
<blockquote>
<p>This app has crashed because it attempted to access privacy-sensitive data without a usage description. The app’s Info.plist must contain an com.apple.security.device.camera key with a string value explaining to the user how the app uses this data.</p>
</blockquote>
<p>When I try to run <code>cap = cv2.VideoCapture(0)</code> in the Slicer Python console I get a similar error:</p>
<blockquote>
<p>This app has crashed because it attempted to access privacy-sensitive data without a usage description. The app’s Info.plist must contain an NSCameraUsageDescription key with a string value explaining to the user how the app uses this data.</p>
</blockquote>
<p>I can’t figure out how to add this information to the Info.plist file</p>

---

## Post #6 by @koeglfryderyk (2022-06-24 23:42 UTC)

<p>I added those two lines to the Info.plist file that I found in <code>/Applications/Slicer.app/Contents/Info.plist</code></p>
<pre><code class="lang-auto">&lt;key&gt;com.apple.security.device.camera&lt;/key&gt;
&lt;string&gt;used_to_track_your_hand&lt;/string&gt;
&lt;key&gt;NSCameraUsageDescription&lt;/key&gt;
&lt;string&gt;also_used_to_track_your_hand&lt;/string&gt;
</code></pre>
<p>Now it seems that the code runs further (it doesn’t crash at <code>cap = cv2.VideoCapture(0)</code>), but <code>capcap.isOpened()</code> returns <code>False</code> and the it I get such a message:</p>
<pre><code class="lang-auto">'OpenCV: not authorized to capture video (status 0), requesting...\nOpenCV: camera failed to properly initialize!
</code></pre>

---

## Post #7 by @pieper (2022-06-25 16:29 UTC)

<p>Those sound like permission issues with opencv and macOS at this point.  Perhaps just run Slicer as root with sudo.</p>

---

## Post #8 by @koeglfryderyk (2022-06-25 17:49 UTC)

<p>That unfortunately didn’t change anything.</p>
<p>I also tried adding <code>sudo</code> as an argument before <code>/bin/bash/</code> (and disabled the need for a password when using <code>sudo</code>), but this also didn’t change anything</p>

---
