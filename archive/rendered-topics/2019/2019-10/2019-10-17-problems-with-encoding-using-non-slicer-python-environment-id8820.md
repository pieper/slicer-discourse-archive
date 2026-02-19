---
topic_id: 8820
title: "Problems With Encoding Using Non Slicer Python Environment"
date: 2019-10-17
url: https://discourse.slicer.org/t/8820
---

# Problems with encoding using non-Slicer Python environment

**Topic ID**: 8820
**Date**: 2019-10-17
**URL**: https://discourse.slicer.org/t/problems-with-encoding-using-non-slicer-python-environment/8820

---

## Post #1 by @dloopz (2019-10-17 18:52 UTC)

<p>Hi!</p>
<p>I’m developing an extension for Slicer with a segmentation module. In my “Module.py” file I want to make a call to a python3.py file of my own (outside Slicer-Python environment) using conda environment. I tried different ways to make the call, until I find the last question of the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Python_Scripting#How_to_run_Python_script_using_a_non-Slicer_Python_environment" rel="nofollow noopener">article</a> ( “How to run Python script using a non-Slicer Python environment”) and noticed that I had the same problem described there. But now I have a problem with encodings: hhis is the piece of my code:</p>
<pre><code>command_line = ["/home/dloopz/miniconda3/bin/python", "--version"]
from subprocess import check_output
command_result = check_output(command_line, env=slicer.util.startupEnvironment())
print(command_result)
</code></pre>
<p>and this is the output:</p>
<pre><code>command_result = check_output(command_line, env=slicer.util.startupEnvironment())
  File "/home/dloopz/SoftsLaburo/Slicer-4.10.2-linux-amd64/lib/Python/lib/python2.7/subprocess.py", line 212, in check_output
    process = Popen(stdout=PIPE, *popenargs, **kwargs)
  File "/home/dloopz/SoftsLaburo/Slicer-4.10.2-linux-amd64/lib/Python/lib/python2.7/subprocess.py", line 390, in __init__
    errread, errwrite)
  File "/home/dloopz/SoftsLaburo/Slicer-4.10.2-linux-amd64/lib/Python/lib/python2.7/subprocess.py", line 1024, in _execute_child
    raise child_exception
UnicodeEncodeError: 'ascii' codec can't encode character u'\xf3' in position 9: ordinal not in range(128)
</code></pre>
<p>The problems I had before were similar, but with the “<strong>init</strong>.py” file of Slicer.<br>
Any idea of how to solve this?</p>
<p>Best regards,<br>
Lucca Dellazoppa</p>

---

## Post #2 by @lassoan (2019-10-17 19:03 UTC)

<p>It seems that Python subprocess expects ascii input and/or output. This seems to cause issues quite often (see for example <a href="https://stackoverflow.com/questions/2595448/unicode-filename-to-python-subprocess-call" rel="nofollow noopener">here</a>).</p>
<p>One solution is to only use ascii file and folder names and command-line arguments; or you may implement some of the workarounds suggested in various Python forums.</p>
<p>Slicer-4.10 used Python 2, but Preview Release uses Python 3. If this problem was fixed in Python 3 then you may consider switching to using a Slicer Preview Release.</p>

---

## Post #3 by @dloopz (2019-10-18 14:12 UTC)

<p>Thanks Andras, I’ll look around to the works you mentioned and try to fix it. If I find a solution I post it here.</p>
<p>Lucca</p>

---

## Post #4 by @dloopz (2019-10-25 12:47 UTC)

<p>Hi again!</p>
<p>I can’t find how to solve the problem yet, and need to use the last version of Slicer. I noticed that reinstalling Slicer allows me to run external python3 files, in my miniconda env, but after a day or two, it crashes again. Always the same error, no matter what command_line I use:</p>
<pre><code>command_result = check_output(command_line, env=slicer.util.startupEnvironment())
  File "/home/dloopz/SoftsLaburo/Slicer-4.10.2-linux-amd64/lib/Python/lib/python2.7/subprocess.py", line 212, in check_output
    process = Popen(stdout=PIPE, *popenargs, **kwargs)
  File "/home/dloopz/SoftsLaburo/Slicer-4.10.2-linux-amd64/lib/Python/lib/python2.7/subprocess.py", line 390, in __init__
    errread, errwrite)
  File "/home/dloopz/SoftsLaburo/Slicer-4.10.2-linux-amd64/lib/Python/lib/python2.7/subprocess.py", line 1024, in _execute_child
    raise child_exception
UnicodeEncodeError: 'ascii' codec can't encode character u'\xf3' in position 9: ordinal not in range(128)
</code></pre>
<p>I don’t even know where is that <strong>character u’\xf3’ in position 9</strong>, if my command_line was, for example:</p>
<p><code>command_line = ["/home/dloopz/miniconda3/bin/python", "--version"]</code></p>
<p>Any advice?</p>
<p>Thanks again!<br>
Lucca</p>

---

## Post #5 by @lassoan (2019-10-27 17:18 UTC)

<p>Try recent Slicer preview releases. They use Python3, which probably does not have this Python2 error anymore.</p>

---
