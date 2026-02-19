---
topic_id: 29929
title: "How To Add Setup File In 3D Slicers Site Package"
date: 2023-06-09
url: https://discourse.slicer.org/t/29929
---

# How to add Setup file in 3D slicer's site-package?

**Topic ID**: 29929
**Date**: 2023-06-09
**URL**: https://discourse.slicer.org/t/how-to-add-setup-file-in-3d-slicers-site-package/29929

---

## Post #1 by @dsa934 (2023-06-09 06:21 UTC)

<p>Operating system: window 10<br>
Slicer version: 5.2.1</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac7858bc189275e0d6ce2900e205df7373db8cd5.png" data-download-href="/uploads/short-url/oBJXUH2XQvKUVTGh7EtbO5RWqeF.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac7858bc189275e0d6ce2900e205df7373db8cd5.png" alt="image" data-base62-sha1="oBJXUH2XQvKUVTGh7EtbO5RWqeF" width="690" height="294" data-dominant-color="222323"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">776×331 13.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<div>
<br>I created a setup.py to use all functions and classes declared in the whole project via "Import Total" declaration.</div>
<p>It works well as intended in my local, but to make it work well in slicer, can I put the setting of this setup file as slicer’s site-package?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/1/614f017dec4376a238424b637b9b428c5f6a5d3c.png" alt="image" data-base62-sha1="dSPAch6QUO3sHT2ZURPkk4eajog" width="507" height="257"></p>
<p>Shouldn’t I just add the packaging file I created to slicer’s site-package?</p>

---

## Post #2 by @dsa934 (2023-06-09 07:39 UTC)

<pre><code class="lang-auto"># install my_python_package into 3d slicer
pip_install('SlicerPathTest-1.0.0-py3-none-any.whl')


# error log
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Users\LJW\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py", line 3571, in pip_install
    _executePythonModule('pip', args)
  File "C:\Users\LJW\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py", line 3533, in _executePythonModule
    logProcessOutput(proc)
  File "C:\Users\LJW\AppData\Local\NA-MIC\Slicer 5.2.1\bin\Python\slicer\util.py", line 3502, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/LJW/AppData/Local/NA-MIC/Slicer 5.2.1/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'SlicerPathTest-1.0.0-py3-none-any.whl']' returned non-zero exit status 1.
</code></pre>
<p>I think this will solve the problem, but what should I do?</p>

---

## Post #3 by @RafaelPalomar (2023-06-10 09:59 UTC)

<p>This is probably due to a wrong path specification for the file<br>
<code>SlicerPathTest-1.0.0-py3-none-any.whl</code>. If you don’t specify the full path to<br>
the file, PythonSlicer will assume the file lies on the default working<br>
directory, which should be the path where the Slicer or PythonSlicer executable<br>
is. Try giving the full path to the file and let us know if it worked out.</p>

---
