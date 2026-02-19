---
topic_id: 19958
title: "Failing Pip Install Scikit Image On Slicer 4 13 0 2021 09 26"
date: 2021-10-01
url: https://discourse.slicer.org/t/19958
---

# Failing pip_install('scikit-image') on Slicer 4.13.0-2021-09-26 due to missing python-real.exe

**Topic ID**: 19958
**Date**: 2021-10-01
**URL**: https://discourse.slicer.org/t/failing-pip-install-scikit-image-on-slicer-4-13-0-2021-09-26-due-to-missing-python-real-exe/19958

---

## Post #1 by @mikebind (2021-10-01 18:04 UTC)

<p>This worked just fine for me previously on the stable version. This is the initial error message I get:</p>
<p><code>error: Application does NOT exists [C:/Users/mikeb/AppData/Local/NA-MIC/Slicer 4.13.0-2021-09-26/bin/./python-real.exe]</code></p>
<p>Followed by</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.13.0-2021-09-26\bin\Python\slicer\util.py", line 2925, in pip_install
    _executePythonModule('pip', args)
  File "C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.13.0-2021-09-26\bin\Python\slicer\util.py", line 2900, in _executePythonModule
    logProcessOutput(proc)
  File "C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.13.0-2021-09-26\bin\Python\slicer\util.py", line 2869, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/mikeb/AppData/Local/NA-MIC/Slicer 4.13.0-2021-09-26/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'scikit-image']' returned non-zero exit status 1.
</code></pre>
<p>There is, in fact, no python-real.exe in the referenced folder.  Should there be?</p>

---

## Post #2 by @lassoan (2021-10-01 19:33 UTC)

<p><code>pip_install('scikit-image')</code> works for me on Windows with 4.13.0-2021-09-27, and python-real.exe exists on my computer here: <code>c:\Users\andra\AppData\Local\NA-MIC\Slicer 4.13.0-2021-09-27\bin\python-real.exe</code>.</p>
<p>The most likely culprit for a missing executable is a hyper-active antivirus software. Check your quarantined files. Not using third-party antivirus software or disabling automatic file delete/quarantine on the Slicer install folder and then reinstalling Slicer should fix the problem.</p>

---

## Post #3 by @mikebind (2021-10-01 20:32 UTC)

<p>Thank you!! The problem was that Avast antivirus had quarantined the executable. I’m confused why it didn’t tell me about it though. I would have had a hard time figuring this out on my own.</p>

---
