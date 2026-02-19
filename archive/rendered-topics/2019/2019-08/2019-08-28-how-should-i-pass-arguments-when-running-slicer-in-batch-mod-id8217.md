---
topic_id: 8217
title: "How Should I Pass Arguments When Running Slicer In Batch Mod"
date: 2019-08-28
url: https://discourse.slicer.org/t/8217
---

# How should I pass arguments when running Slicer in batch mode?

**Topic ID**: 8217
**Date**: 2019-08-28
**URL**: https://discourse.slicer.org/t/how-should-i-pass-arguments-when-running-slicer-in-batch-mode/8217

---

## Post #1 by @hbraunDSP (2019-08-28 20:44 UTC)

<p>I want to run slicer from within python, to execute a script that builds a scene automatically from a JSON file telling it what files to load. I think I’ve solved everything except how to tell slicer the location of the JSON file.  There are several options I can think of:</p>
<ul>
<li>Run <code>Slicer --python-script myscript.py</code>, first setting an environment variable <code>json_file</code> that is then checked by myscript.py.</li>
<li>Run <code>Slicer --python-code mymodule.myscript(&lt;json_file&gt;)</code>, where my code inserts the correct string for &lt;json_file&gt; before running slicer</li>
<li>Same as above, but run <code>Slicer -c</code> instead of <code>Slicer --python_code</code>
</li>
</ul>
<p>All of these feel pretty kludgy for something that seems like it would be common. Is there some other way I’m not thinking of? Is there a preferred way to give arguments when running a python script within Slicer as part of a batch job?</p>

---

## Post #2 by @Sam_Horvath (2019-08-29 15:24 UTC)

<p>Everything after --python-script until the next recognizable flag is passed into the python interpreter:</p>
<p>Run:<br>
<code>./Slicer.exe --no-main-window --python-script test.py param1 param2 param3</code></p>
<p>Where test.py is:<br>
<code>print(sys.argv)</code></p>
<p>You will get this output on the console:<br>
<code>['test.py', 'param1', 'param2', 'param3']</code></p>

---
