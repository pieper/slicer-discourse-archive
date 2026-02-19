---
topic_id: 35288
title: "Alpaca Error Open3D"
date: 2024-04-04
url: https://discourse.slicer.org/t/35288
---

# ALPACA Error open3d

**Topic ID**: 35288
**Date**: 2024-04-04
**URL**: https://discourse.slicer.org/t/alpaca-error-open3d/35288

---

## Post #1 by @LeidyMoraV (2024-04-04 14:45 UTC)

<p>When I try to use ALPACA function from SlicerMorph the following message shows up. I’ve tried reinstalling the app, installing the updates and use the python command window, and using the Testing Version of ALPACA, but I keep getting errors.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/087e660f63ca9394026f606f49a496ee00f326eb.png" data-download-href="/uploads/short-url/1d8CULmodGFlRABGqnRihQV5zKj.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/087e660f63ca9394026f606f49a496ee00f326eb_2_690x370.png" alt="image" data-base62-sha1="1d8CULmodGFlRABGqnRihQV5zKj" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/087e660f63ca9394026f606f49a496ee00f326eb_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/087e660f63ca9394026f606f49a496ee00f326eb_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/087e660f63ca9394026f606f49a496ee00f326eb_2_1380x740.png 2x" data-dominant-color="97979C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1913×1028 58 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d935637767a61326c0a9b167a59092605e9b1a1c.png" data-download-href="/uploads/short-url/uZvZIJwKWUwdThwTvasZsBRHkZK.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d935637767a61326c0a9b167a59092605e9b1a1c_2_690x361.png" alt="image" data-base62-sha1="uZvZIJwKWUwdThwTvasZsBRHkZK" width="690" height="361" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d935637767a61326c0a9b167a59092605e9b1a1c_2_690x361.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d935637767a61326c0a9b167a59092605e9b1a1c_2_1035x541.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d935637767a61326c0a9b167a59092605e9b1a1c_2_1380x722.png 2x" data-dominant-color="C5C4C9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1006 91 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">&gt;&gt;&gt; pip_install('notebook==6.0.3')
&gt;&gt;&gt; pip_install('open3d==0.10.0')
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\ProgramData\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py", line 3571, in pip_install
    _executePythonModule('pip', args)
  File "C:\ProgramData\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py", line 3533, in _executePythonModule
    logProcessOutput(proc)
  File "C:\ProgramData\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py", line 3502, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/ProgramData/NA-MIC/Slicer 5.2.1/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'open3d==0.10.0']' returned non-zero exit status 1.
&gt;&gt;&gt; slicer.util.pip_install('notebook==6.0.3')
&gt;&gt;&gt; slicer.util.pip_install('open3d==0.9.0')
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\ProgramData\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py", line 3571, in pip_install
    _executePythonModule('pip', args)
  File "C:\ProgramData\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py", line 3533, in _executePythonModule
    logProcessOutput(proc)
  File "C:\ProgramData\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py", line 3502, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/ProgramData/NA-MIC/Slicer 5.2.1/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'open3d==0.9.0']' returned non-zero exit status 1.
</code></pre>

---

## Post #2 by @muratmaga (2024-04-04 14:48 UTC)

<p>Please try with latest stable version of slicer (5.6.1)</p>

---
