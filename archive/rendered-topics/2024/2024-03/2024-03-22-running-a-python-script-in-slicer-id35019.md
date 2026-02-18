# Running a python script in slicer

**Topic ID**: 35019
**Date**: 2024-03-22
**URL**: https://discourse.slicer.org/t/running-a-python-script-in-slicer/35019

---

## Post #1 by @Matteboo (2024-03-22 10:31 UTC)

<p>Hello,</p>
<p>I’m trying to run a python script using slicer<br>
I tried</p>
<pre><code class="lang-auto">&gt;&gt;&gt; C:\Users\matte\AppData\Local\slicer.org\Slicer 5.6.0\Slicer.exe --python-script "C:\Users\matte\Documents\Matteo\script\hello_world.py"
  File "&lt;console&gt;", line 1
    C:\Users\matte\AppData\Local\slicer.org\Slicer 5.6.0\Slicer.exe --python-script "C:\Users\matte\Documents\Matteo\script\hello_world.py"
       ^
SyntaxError: unexpected character after line continuation character
&gt;&gt;&gt; "C:\Users\matte\AppData\Local\slicer.org\Slicer 5.6.0\Slicer.exe"--python-script "C:\Users\matte\Documents\Matteo\script\hello_world.py"
  File "&lt;console&gt;", line 1
    "C:\Users\matte\AppData\Local\slicer.org\Slicer 5.6.0\Slicer.exe"--python-script "C:\Users\matte\Documents\Matteo\script\hello_world.py"
                                                                     ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape
</code></pre>
<p>I read <a href="https://discourse.slicer.org/t/run-python-script-from-command-line-not-working/22453" class="inline-onebox">Run python script from command line not working</a> without finding a solution</p>
<p>I’m familiar with coding but I’m new to coding using slicer, if you have any ressources that I could use, I would be very grateful</p>

---

## Post #2 by @Matteboo (2024-03-22 12:53 UTC)

<p>I  found the solution, I needed to type the command in the <strong>Window</strong> command line <strong>not</strong> in the <strong>slicer</strong> command line</p>

---
