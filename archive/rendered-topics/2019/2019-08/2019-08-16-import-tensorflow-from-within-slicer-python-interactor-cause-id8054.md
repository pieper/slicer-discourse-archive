# import tensorflow from within Slicer python interactor causes crash

**Topic ID**: 8054
**Date**: 2019-08-16
**URL**: https://discourse.slicer.org/t/import-tensorflow-from-within-slicer-python-interactor-causes-crash/8054

---

## Post #1 by @gaoyi (2019-08-16 04:39 UTC)

<p>Hi All,</p>
<p>I build Slicer from trunk and pip_install(“tensorflow”) from python interactor within Slicer (Ctrl + 3).<br>
Seems to be successful. Then I “import tensorflow”，but this crashes Slicer without detailed error message.</p>
<p>I tried this:<br>
./Slicer --launch …/python-install/bin/python<br>
Then in this python interpreter, I import tensorflow<br>
And things are fine (no crashing)</p>
<p>But within Slicer it crashes.</p>
<p>Could I have any hint on the direction I should look into?</p>
<p>Thank you!</p>
<p>yi</p>

---

## Post #2 by @lassoan (2019-08-16 04:55 UTC)

<p>Importing tensorflow in Slicer GUI works fine on Windows (using a recent Slicer Preview Release - Slicer-4.11.0-2019-08-13).</p>
<p>What operating system and which Slicer version do you use? Do you have a stack trace of the crash? Have you pip-installed any other packages?</p>
<p>You may try to downgrade tensorflow or switch between GPU/CPU version.</p>

---

## Post #3 by @gaoyi (2019-08-16 05:38 UTC)

<p>Hi Andras,</p>
<p>I’m using Linux Mint 19.1 with gcc 7.3 with nightly Slicer (20190816)</p>
<p>I didn’t pip install other packages except those trigger by tensorflow.</p>
<p>I tried both GPU (tensorflow-gpu) and CPU versions and both crashes.</p>
<p>I don’t have crash trace yet. It just says :<br>
./SlicerApp-real] exit abnormally - Report the problem.</p>
<p>How could I get the trace info?</p>
<p>Thanks!<br>
yi</p>

---

## Post #4 by @lassoan (2019-08-16 12:25 UTC)

<p>I don’t know how to debug this on linux, hopefully others can help.</p>
<p>Alternatively, you can run your Python script as a CLI module. See example <a href="https://github.com/lassoan/SlicerPythonCLIExample" rel="nofollow noopener">here</a>.</p>

---

## Post #5 by @gaoyi (2019-08-16 12:31 UTC)

<p>Thank you Andras!</p>
<p>I’ll investigate the CLI python approach and update with you.</p>
<p>Best,<br>
yi</p>

---

## Post #6 by @jcfr (2019-08-16 15:35 UTC)

<aside class="quote no-group" data-username="gaoyi" data-post="3" data-topic="8054">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/gaoyi/48/4283_2.png" class="avatar"> gaoyi:</div>
<blockquote>
<p>I don’t have crash trace yet. It just says :<br>
./SlicerApp-real] exit abnormally - Report the problem.</p>
</blockquote>
</aside>
<p>You could also generate a core dump and than open it with ddd (or gdb). While there are no debug info available within Release build, it should still provide some useful information.</p>
<p>See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/Debug_Instructions#Analyze_a_segmentation_fault" class="inline-onebox">Documentation/Nightly/Developers/Tutorials/Debug Instructions - Slicer Wiki</a></p>

---

## Post #7 by @gaoyi (2019-08-17 00:12 UTC)

<p>Thanks Jc,</p>
<p>Will do this and report back soon.</p>
<p>Best,<br>
yi</p>

---

## Post #8 by @gaoyi.cn (2019-10-19 03:13 UTC)

<p>Hi Andras,</p>
<p>In trying the python CLI, how could i assign the python environment I want Slicer to run my pythonCLI with?  (Say my python exe is in /opt/anacondaGPU/bin/python)</p>
<p>Thanks for the advice!</p>
<p>Best,<br>
yi</p>

---
