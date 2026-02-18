# Fail to install itk 5.3rc04.post3 in 3D Slicer

**Topic ID**: 35187
**Date**: 2024-03-31
**URL**: https://discourse.slicer.org/t/fail-to-install-itk-5-3rc04-post3-in-3d-slicer/35187

---

## Post #1 by @Cheyuan_Chang (2024-03-31 12:47 UTC)

<p>Hello, I am using 3Dslicer 5.7 and find problem with installing itk</p>
<p>Is there any problem to solve this installation problem?</p>
<p>The error code was posted below</p>
<p>ERROR: Could not find a version that satisfies the requirement itk-core==5.3rc04.post3 (from itk) (from versions: 5.1.1.post1, 5.1.2, 5.2.0, 5.2.0.post1, 5.2.0.post2, 5.2.1, 5.2.1.post1, 5.3rc4, 5.3rc4.post4, 5.3.0, 5.4rc1, 5.4rc2)<br>
ERROR: No matching distribution found for itk-core==5.3rc04.post3<br>
Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “C:\Users\cycha\AppData\Local\slicer.org\Slicer 5.7.0-2023-12-31\bin\Python\slicer\util.py”, line 3887, in pip_install<br>
_executePythonModule(“pip”, args)<br>
File “C:\Users\cycha\AppData\Local\slicer.org\Slicer 5.7.0-2023-12-31\bin\Python\slicer\util.py”, line 3848, in _executePythonModule<br>
logProcessOutput(proc)<br>
File “C:\Users\cycha\AppData\Local\slicer.org\Slicer 5.7.0-2023-12-31\bin\Python\slicer\util.py”, line 3814, in logProcessOutput<br>
raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)<br>
subprocess.CalledProcessError: Command ‘[‘C:/Users/cycha/AppData/Local/slicer.org/Slicer 5.7.0-2023-12-31/bin/…/bin\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘–pre’, ‘itk==5.3rc4.post3’]’ returned non-zero exit status 1.</p>

---

## Post #2 by @lassoan (2024-03-31 19:17 UTC)

<aside class="quote no-group" data-username="Cheyuan_Chang" data-post="1" data-topic="35187">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cheyuan_chang/48/69826_2.png" class="avatar"> Cheyuan_Chang:</div>
<blockquote>
<p>itk-core==5.3rc04.post3</p>
</blockquote>
</aside>
<p>It is normal that a some very specific ITK release candidate version like <code>5.3rc04.post3</code> is not available on all Python versions on all platforms.</p>
<p>Install a recent enough ITK version should work well. For example: <code>pip_install('itk-core&gt;=5.3')</code></p>

---
