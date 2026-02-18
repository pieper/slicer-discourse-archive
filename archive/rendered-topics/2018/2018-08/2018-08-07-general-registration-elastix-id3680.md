# General Registration Elastix

**Topic ID**: 3680
**Date**: 2018-08-07
**URL**: https://discourse.slicer.org/t/general-registration-elastix/3680

---

## Post #1 by @Laura (2018-08-07 13:42 UTC)

<p>Good afternoon,</p>
<p>I try to use “General Registration Elastix” module extension but it tells me</p>
<blockquote>
<p>Traceback (most recent call last):</p>
<p>File "/home/miv/seimpere/.config/NA-MIC/Extensions-27331/SlicerElastix/lib/Slicer-4.9/qt-scripted-modules/Elastix.py", line 327, in onApplyButton</p>
<p>movingVolumeMaskNode = self.movingVolumeMaskSelector.currentNode())</p>
<p>File "/home/miv/seimpere/.config/NA-MIC/Extensions-27331/SlicerElastix/lib/Slicer-4.9/qt-scripted-modules/Elastix.py", line 578, in registerVolumes</p>
<p>ep = self.startElastix(inputParamsElastix)</p>
<p>File "/home/miv/seimpere/.config/NA-MIC/Extensions-27331/SlicerElastix/lib/Slicer-4.9/qt-scripted-modules/Elastix.py", line 485, in startElastix</p>
<p>stdout=subprocess.PIPE, universal_newlines=True)</p>
<p>File "/home/miv/seimpere/Slicer-4.9.0-2018-08-01-linux-amd64/lib/Python/lib/python2.7/subprocess.py", line 390, in <strong>init</strong></p>
<p>errread, errwrite)</p>
<p>File "/home/miv/seimpere/Slicer-4.9.0-2018-08-01-linux-amd64/lib/Python/lib/python2.7/subprocess.py", line 1024, in _execute_child</p>
<p>raise child_exception</p>
<p>OSError: [Errno 2] No such file or directory</p>
</blockquote>
<p>Do you know what’s wrong ?<br>
Thanks<br>
Laura</p>

---

## Post #2 by @lassoan (2018-08-07 14:17 UTC)

<p>I haven’t tried Elastix on Linux. Maybe you need to download and install Elastix manually and then in Slicer in the Elastix registration module, set path of manually installed executable in Advanced settings.</p>

---

## Post #3 by @Laura (2018-08-07 14:25 UTC)

<p>Ok thanks, I try that but it is very strange because 3h ago it was working…</p>

---

## Post #4 by @jcfr (2018-08-07 14:33 UTC)

<p>Hi <a class="mention" href="/u/laura">@Laura</a> ,</p>
<p>I un-flagged your question, feel free to comment and mark it as resolved.</p>

---

## Post #5 by @brhoom (2018-08-07 14:34 UTC)

<p>If it was working before then the binaries has no problem unless you changed them. Try to empty the output folder and restart slicer.</p>

---

## Post #6 by @Laura (2018-08-07 14:45 UTC)

<p>I restore all defaults and reload and install everything again and that works !!! Thanks a lot for your help !</p>

---
