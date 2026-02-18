# Moose Extension was ERROR

**Topic ID**: 44998
**Date**: 2025-11-08
**URL**: https://discourse.slicer.org/t/moose-extension-was-error/44998

---

## Post #1 by @akmal871026 (2025-11-08 04:51 UTC)

<p>Dear All,</p>
<p>I am faced problem since install dependencies for Moose Extension.</p>
<p>Traceback (most recent call last):</p>
<p>File “D:\Slicer 5.8.1\bin\Python\slicer\util.py”, line 3303, in tryWithErrorDisplay</p>
<p>yield</p>
<p>File “D:/Slicer 5.8.1/slicer.org/Extensions-33241/SlicerMOOSE/lib/Slicer-5.8/qt-scripted-modules/MOOSE.py”, line 150, in button_install_dependencies_clicked</p>
<p>self.dependency_manager.install_all_dependencies()</p>
<p>File “D:/Slicer 5.8.1/slicer.org/Extensions-33241/SlicerMOOSE/lib/Slicer-5.8/qt-scripted-modules/MOOSE.py”, line 98, in install_all_dependencies</p>
<p>self.install_moosez()</p>
<p>File “D:/Slicer 5.8.1/slicer.org/Extensions-33241/SlicerMOOSE/lib/Slicer-5.8/qt-scripted-modules/MOOSE.py”, line 60, in install_moosez</p>
<p>slicer.util.pip_install(“moosez&gt;=3.1.1”)</p>
<p>File “D:\Slicer 5.8.1\bin\Python\slicer\util.py”, line 3942, in pip_install</p>
<p>_executePythonModule(“pip”, args)</p>
<p>File “D:\Slicer 5.8.1\bin\Python\slicer\util.py”, line 3896, in _executePythonModule</p>
<p>logProcessOutput(proc)</p>
<p>File “D:\Slicer 5.8.1\bin\Python\slicer\util.py”, line 3862, in logProcessOutput</p>
<p>raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)</p>
<p>subprocess.CalledProcessError: Command ‘[‘D:/Slicer 5.8.1/bin/../bin\\PythonSlicer.EXE’, ‘-m’, ‘pip’, ‘install’, ‘moosez&gt;=3.1.1’]’ returned non-zero exit status 1.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a2333f9b89e0d0982d9a1cbd9844fc629d90f65.png" data-download-href="/uploads/short-url/60LtvmxZHWK5CckvkUwO3Y5sC4B.png?dl=1" title="Screenshot 2025-11-08 125011" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/a/2a2333f9b89e0d0982d9a1cbd9844fc629d90f65.png" alt="Screenshot 2025-11-08 125011" data-base62-sha1="60LtvmxZHWK5CckvkUwO3Y5sC4B" width="516" height="234"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-11-08 125011</span><span class="informations">516×234 12.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2025-11-08 05:00 UTC)

<aside class="quote no-group" data-username="akmal871026" data-post="1" data-topic="44998">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/akmal871026/48/11642_2.png" class="avatar"> akmal871026:</div>
<blockquote>
<p>slicer.util.pip_install(“moosez&gt;=3.1.1”)</p>
</blockquote>
</aside>
<p>I believe the developers updated their extension to use a newer version of moosez that is technically Python 3.10 or newer compatible. Therefore it is likely the extension is no longer compatible with Slicer 5.8 which uses Python 3.9. Instead try latest Slicer Preview (soon to be Slicer 5.10 stable) as it uses Python 3.12.</p>

---
