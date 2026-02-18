# Error when installing matplotib in Slicer

**Topic ID**: 28138
**Date**: 2023-03-02
**URL**: https://discourse.slicer.org/t/error-when-installing-matplotib-in-slicer/28138

---

## Post #1 by @hapkx (2023-03-02 08:28 UTC)

<p>Operating system: Windows11<br>
Slicer version: Slicer 5.0.2</p>
<p>Hi!<br>
I’m trying to install matplotlib package in python-interactor in Slicer 5.0.2 with the following commands:</p>
<pre><code class="lang-auto">from slicer.util import pip_install
pip_install("matplotlib")
import matplotlib.pyplot as plt
</code></pre>
<p>I get the following error:</p>
<pre><code class="lang-auto">WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/matplotlib/
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/matplotlib/
WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/matplotlib/
WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/matplotlib/
WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/matplotlib/
Could not fetch URL https://pypi.org/simple/matplotlib/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/matplotlib/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping
ERROR: Could not find a version that satisfies the requirement matplotlib (from versions: none)
ERROR: No matching distribution found for matplotlib
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping
Traceback (most recent call last):
  File "D:/DESKTOP/ex/module3/module3.py", line 480, in readPic
    pip_install("matplotlib")
  File "E:\Slicer 5.0.2\bin\Python\slicer\util.py", line 3431, in pip_install
    _executePythonModule('pip', args)
  File "E:\Slicer 5.0.2\bin\Python\slicer\util.py", line 3394, in _executePythonModule
    logProcessOutput(proc)
  File "E:\Slicer 5.0.2\bin\Python\slicer\util.py", line 3363, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['E:/Slicer 5.0.2/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'matplotlib']' returned non-zero exit status 1.
...
</code></pre>
<p>as shown in the picture:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/493dc4a91f365eeaf6e24861fbacd398c4863df8.png" data-download-href="/uploads/short-url/arVbYkdBATVfESTpbhLMzJOBXsI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/9/493dc4a91f365eeaf6e24861fbacd398c4863df8.png" alt="image" width="690" height="271" data-dominant-color="F2EEEE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1340×528 50.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
