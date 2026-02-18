# Calling slicer module from a python file

**Topic ID**: 12720
**Date**: 2020-07-24
**URL**: https://discourse.slicer.org/t/calling-slicer-module-from-a-python-file/12720

---

## Post #1 by @Anand_Mulay (2020-07-24 14:28 UTC)

<p>i know we can call the slicer module with command line arguments or calling from a batch file, can i write a python file to call slicer with same same command?</p>

---

## Post #2 by @lassoan (2020-07-24 15:40 UTC)

<p>Yes, of course, you can use standard Python functions to run a process. See for example how it is done in <code>slicer.util.launchConsoleProcess</code> method:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/524979a2e91ff25de690909f141e6afbe1b1c6e5/Base/Python/slicer/util.py#L2347-L2392" target="_blank" rel="noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/524979a2e91ff25de690909f141e6afbe1b1c6e5/Base/Python/slicer/util.py#L2347-L2392" target="_blank" rel="noopener">Slicer/Slicer/blob/524979a2e91ff25de690909f141e6afbe1b1c6e5/Base/Python/slicer/util.py#L2347-L2392</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="2347" style="counter-reset: li-counter 2346 ;">
<li>def launchConsoleProcess(args, useStartupEnvironment=True, cwd=None):</li>
<li>  """Launch a process. Hiding the console and captures the process output.</li>
<li>  The console window is hidden when running on Windows.</li>
<li>  :param args: executable name, followed by command-line arguments</li>
<li>  :param useStartupEnvironment: launch the process in the original environment as the original Slicer process</li>
<li>  :param cwd: current working directory</li>
<li>  :return: process object.</li>
<li>  """</li>
<li>  import subprocess</li>
<li>  if useStartupEnvironment:</li>
<li>    startupEnv = startupEnvironment()</li>
<li>  else:</li>
<li>    startupEnv = None</li>
<li>  import os</li>
<li>  if os.name == 'nt':</li>
<li>    # Hide console window (only needed on Windows)</li>
<li>    info = subprocess.STARTUPINFO()</li>
<li>    info.dwFlags = 1</li>
<li>    info.wShowWindow = 0</li>
<li>    proc = subprocess.Popen(args, env=startupEnv, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True, startupinfo=info, cwd=cwd)</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/524979a2e91ff25de690909f141e6afbe1b1c6e5/Base/Python/slicer/util.py#L2347-L2392" target="_blank" rel="noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Anand_Mulay (2020-07-24 16:23 UTC)

<p>i tried to run slicer using subprocess.Popen and Subprocess.run , but the thing is it is not recognizing the code after the slicer path like  : slicer.exe --python-code “slicer.module…” , it just runs the slicer and now further action.<br>
i’ll give a try to the example you’ve sent and let you know, i think i’m missing something <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:"></p>

---

## Post #4 by @lassoan (2020-07-24 17:47 UTC)

<p>It is all just standard Python, so you can find thousands of examples and many tutorials, documentation on the web. If you still have trouble then copy your complete script here so that we can have a look.</p>

---

## Post #5 by @Anand_Mulay (2020-07-24 17:49 UTC)

<p>yeah, and i found it <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>thank you so much</p>

---

## Post #6 by @lassoan (2020-07-24 18:07 UTC)

<p>Was there anything that you learned that could help others who will have similar needs in the future? Can you share the code snippet that ended up working?</p>

---

## Post #7 by @Anand_Mulay (2020-07-24 18:29 UTC)

<p>Yes here is my code snippet</p>
<blockquote>
<p>import os<br>
import subprocess</p>
<p>os.chmod(‘C:\Program Files\Slicer 4.10.2\slicer.exe’,0o777)</p>
<p>args1= “‘C:\dicomfiles\study’”</p>
<p>arsg2= “‘any other args if any’”</p>
<p>args3 = 'C:\Program Files\Slicer 4.10.2\slicer.exe --python-code ’<br>
args = args3 + args1 + args2<br>
proc = subprocess.Popen(args)<br>
proc.communicate()<br>
returnCode = proc.poll()</p>
</blockquote>
<p>the first thing is i dont know why without the os.chmod i got permission issue,<br>
also any easy way to pass the path as args, as if folder name start with A or T it didn’t work <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>
<p>This community is awesome <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20"></p>

---

## Post #8 by @lassoan (2020-07-24 21:36 UTC)

<aside class="quote no-group" data-username="Anand_Mulay" data-post="7" data-topic="12720">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/anand_mulay/48/6850_2.png" class="avatar"> Anand_Mulay:</div>
<blockquote>
<p>if folder name start with A or T it didn’t work</p>
</blockquote>
</aside>
<p>Backslash <code>\</code> is an escape character in Python string literals. See in this post how you can use backslash characters:</p>
<aside class="quote quote-modified" data-post="14" data-topic="2837">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/subprocess-call-does-not-work/2837/14">Subprocess.call does not work!</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    FYI, since backslash (\) is an escape character in Python, you cannot simply use it in a string literal in Python. 
The easiest is to indicate that you specify a raw string by prepending an r character before the string. This is correct: 
somePath = r"F:\someFolder\python.exe"

If you need to use a regular string then backslash can be entered by typing double-backslash. This is correct: 
somePath = "F:\\someFolder\\python.exe"

You may also use Unix-type separators. This is correct: 
somePath = …
  </blockquote>
</aside>


---

## Post #9 by @lassoan (2021-06-09 12:52 UTC)

<p>A post was split to a new topic: <a href="/t/is-slicers-python-environment-complete/18038">Is Slicer’s Python environment complete?</a></p>

---

## Post #10 by @lassoan (2024-08-16 10:50 UTC)

<p>A post was merged into an existing topic: <a href="/t/the-external-python-program-calls-the-slicer-plug-in-or-installs-the-plug-in-in-other-software/37900/5">The external python program calls the slicer plug-in, or installs the plug-in in other software</a></p>

---
