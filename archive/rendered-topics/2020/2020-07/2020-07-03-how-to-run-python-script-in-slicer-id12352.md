# How to run python script in Slicer?

**Topic ID**: 12352
**Date**: 2020-07-03
**URL**: https://discourse.slicer.org/t/how-to-run-python-script-in-slicer/12352

---

## Post #1 by @SummerZ2020 (2020-07-03 08:13 UTC)

<p>Operating system:Win10<br>
Slicer version:4.11.0(2020.6.15)<br>
Expected behavior:The saveLabel.py should be run when I run <code>C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-15&gt;Slicer.exe --python--script C:\Users\310091560\Desktop\saveLabel.py</code> in the command line window.<br>
Actual behavior: nothing happened except the Slicer main window(python interactor) openning.</p>
<p>Is this command line <code>C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-15&gt;Slicer.exe --python--script C:\Users\310091560\Desktop\saveLabel.py</code> right to run a python script?<br>
Thanks in advance.</p>
<p>BTW, is the tutorial “[<a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools" class="inline-onebox" rel="noopener nofollow ugc">Documentation/Nightly/Extensions/DebuggingTools - Slicer Wiki</a>](<a href="http://Visual" rel="noopener nofollow ugc">http://Visual</a> Python debugging in PyCharm)” updated according to the 4.11 version? I cannot find the Python debugger extension and the  “Python debugger”  module (in  “Developer Tools”  category).<br>
Thanks again.</p>

---

## Post #2 by @lassoan (2020-07-03 15:55 UTC)

<aside class="quote no-group quote-modified" data-username="SummerZ2020" data-post="1" data-topic="12352">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/summerz2020/48/7137_2.png" class="avatar"> SummerZ2020:</div>
<blockquote>
<p>C:\ProgramData\NA-MIC\Slicer 4.11.0-2020-06-15&gt;Slicer.exe --python–script C:\Users\310091560\Desktop\saveLabel.py</p>
</blockquote>
</aside>
<p>The correct argument name is <code>--python-script</code> and not <code>--python--script</code>.</p>

---

## Post #3 by @SummerZ2020 (2020-07-08 01:39 UTC)

<p>So simple mistake, I should be more careful. Thanks a lot.</p>

---

## Post #4 by @Gokce_Guven (2023-07-30 20:18 UTC)

<p>Hi Mr. Lasso,</p>
<p>I am trying to run a python script from Slicer 5.3.0 version on Ubuntu 22.04 OS. When I run it from the terminal like this:</p>
<p>./Slicer --python-script /home/username/ls.py</p>
<p>it gives this error eventhough I have tkinter on my system:<br>
/lib/python3.9/ls.py<br>
Switch to module:  “Welcome”<br>
Loading Slicer RC file [/home/gokce/.slicerrc.py]<br>
:1: DeprecationWarning: The symbol module is deprecated and will be removed in future versions of Python<br>
NOTE: You must install tkinter on Linux to use MouseInfo. Run the following: sudo apt-get install python3-tk python3-dev<br>
Switch to module:  “”<br>
Switch to module:  “”</p>
<p>When I put the ls.py script inside the folder: /home/username/Slicer-5.3.0-2023-07-29-linux-amd64/lib/Python/lib/python3.9/ folder and start the slicer and import the ls script from the python console and call a function from the ls script it gives this error:</p>
<pre><code class="lang-auto">&gt;&gt;&gt; import ls
&gt;&gt;&gt; ls.start()
  File "&lt;console&gt;", line 1
    import ls
             ^
SyntaxError: multiple statements found while compiling a single statement
&gt;&gt;&gt; 
</code></pre>
<p>How should I proceed?</p>
<p>Thanks in advance</p>

---

## Post #5 by @lassoan (2023-07-31 01:11 UTC)

<p>Slicer uses its own virtual Python environment (you don’t need to install Python in your system). If you want to install a package in Sicer’s virtual Python environment then you can use the <code>pip_install</code> convenience function in the Slicer Python console.</p>

---

## Post #6 by @lassoan (2023-07-31 02:27 UTC)

<p><code>SyntaxError: multiple statements found while compiling a single statement</code> error means that statements are not separated by newline or semicolon (<code>;</code>). Maybe during copy-paste, the newline character gets replaced by a space? You may try to copy-paste from a different software or add semicolon after each statement (<code>import ls; ls.start()</code>).</p>
<p>I would not recommend to put any files into the Python library folder (<code>/home/username/Slicer-5.3.0-2023-07-29-linux-amd64/lib/Python/lib/python3.9/</code>). Instead you can put it anywhere and run it by calling as you did (<code>./Slicer --python-script /home/username/ls.py</code>). You can ignore the deprecation warning. When Slicer will upgrade to a Python version that does not contain tkinter anymore (or even before that) you can switch to Qt, which is already bundled with Slicer.</p>

---

## Post #7 by @Gokce_Guven (2023-07-31 08:00 UTC)

<p>Dear Mr. Lasso, thanks a lot for the detailed and fast response. When I run it from the terminal like this:</p>
<pre><code class="lang-auto"> ./Slicer --python-script ../ls.py 
Switch to module:  "Welcome"
Loading Slicer RC file [/home/gokce/.slicerrc.py]
&lt;string&gt;:1: DeprecationWarning: The symbol module is deprecated and will be removed in future versions of Python
NOTE: You must install tkinter on Linux to use MouseInfo. Run the following: sudo apt-get install python3-tk python3-dev
Switch to module:  ""
Switch to module:  ""
</code></pre>
<p>I forgot to add that the slicer is opening for a second and closing itself. The ls.py script is using lung segmenter plugin in slicer and the same code is working on Windows. I want to run it on Ubuntu 22.04.2, I do not know what is wrong. I have tried many possible solutions that I have found on web. When I call the code from the python console without space like this:</p>
<pre><code class="lang-python">Python 3.9.10 (main, Jul 30 2023, 03:07:06)

[GCC 7.3.1 20180303 (Red Hat 7.3.1-5)] on linux2

&gt;&gt;&gt;

Loading Slicer RC file [/home/username/.slicerrc.py]

&gt;&gt;&gt; import ls;ls.start()
&gt;&gt;&gt;
</code></pre>
<p>it is not giving any output, I cannot understand what may be possibly wrong.</p>

---

## Post #8 by @Gokce_Guven (2023-07-31 10:45 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> Hi Mr. Lasso,</p>
<p>I have tried to comment out one of my python package “pyautogui” and uninstall it from the Slicer, then my code worked. I wanted to take screenshots of the segmentation for each data with pyautogui. Do you have any suggestion for collecting the screenshots for each data?</p>
<p>Thanks in advance</p>

---

## Post #9 by @lassoan (2023-07-31 11:46 UTC)

<p>You can use the Screen Capture module to take screenshots. See the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#screen-capture">script repository</a> for examples.</p>

---

## Post #10 by @Gokce_Guven (2023-07-31 12:36 UTC)

<p>thanks a lot Mr. Lasso, that solved my problem<br>
Have a great day</p>

---
