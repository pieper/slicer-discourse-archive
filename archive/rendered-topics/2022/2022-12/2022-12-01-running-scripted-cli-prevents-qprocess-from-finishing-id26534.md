# Running scripted-cli prevents QProcess from finishing

**Topic ID**: 26534
**Date**: 2022-12-01
**URL**: https://discourse.slicer.org/t/running-scripted-cli-prevents-qprocess-from-finishing/26534

---

## Post #1 by @brandus1 (2022-12-01 12:16 UTC)

<p>I have a module where I periodically run an instance of a subclass of QProcess, which is basically identical to <a class="mention" href="/u/pieper">@pieper</a> 's Process class in <a href="https://github.com/pieper/SlicerParallelProcessing/blob/master/Processes/Processes.py" rel="noopener nofollow ugc">SlicerParallelProcessing</a>.</p>
<p>I use this class to run a python script that polls an API in a server. When the process finishes, it gets destroyed and another one is called after 2 seconds (using a QTimer).</p>
<p>Everything works fine until I call a scripted cli module at some point. Basically, as soon as a scripted-cli module runs, the QProcess hangs - it does not emit the finished() signal anymore.  The script runs fine without errors, I checked the standard output and no problem there. It just doesn’t finish.</p>
<p>It does not have anything to do with what the scripted-cli module does: it happens with my module or even the standard cli module produces by the Extension Wizard.</p>
<p>Note: the problem does not happen if your run a c++ cli module</p>
<p>I am not very familiar with the underlyings of PythonSlicer or QTClI, but I think it might have something to do with them.</p>
<p>Any idea?</p>

---

## Post #2 by @pieper (2022-12-03 15:45 UTC)

<p>CLI modules are run in independent threads, while python code runs in the main thread, so that may be the difference.  If you are still having trouble try to create a minimal example that others can test with and help you debug.</p>

---
