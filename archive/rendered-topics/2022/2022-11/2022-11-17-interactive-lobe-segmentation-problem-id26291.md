# Interactive lobe segmentation problem

**Topic ID**: 26291
**Date**: 2022-11-17
**URL**: https://discourse.slicer.org/t/interactive-lobe-segmentation-problem/26291

---

## Post #1 by @wangjianmerci (2022-11-17 18:33 UTC)

<p>Interactive lobe segmentation seems didn’t work well.  no matter how many fiducials I seleted, five lung lobes can’t be segmented correctly.</p>
<p>Operating system:windows<br>
Slicer version:5.0.3<br>
Expected behavior:five lung lobes segmentations<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc6e5904727a1d8346764615bfa62472914a93de.png" data-download-href="/uploads/short-url/vs1sFuCfBnt5BwfAybNhpwGg8R8.png?dl=1" title="3dslicer ideal" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc6e5904727a1d8346764615bfa62472914a93de_2_689x453.png" alt="3dslicer ideal" data-base62-sha1="vs1sFuCfBnt5BwfAybNhpwGg8R8" width="689" height="453" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc6e5904727a1d8346764615bfa62472914a93de_2_689x453.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/c/dc6e5904727a1d8346764615bfa62472914a93de_2_1033x679.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/c/dc6e5904727a1d8346764615bfa62472914a93de.png 2x" data-dominant-color="A7A9AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3dslicer ideal</span><span class="informations">1181×777 282 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Actual behavior:as see in the picture<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3a4cdf5275685e91599d64c3952a366a3225bbe4.jpeg" data-download-href="/uploads/short-url/8jKoh54Q9RUg9vSLlSzRFqlP2ni.jpeg?dl=1" title="3dslicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a4cdf5275685e91599d64c3952a366a3225bbe4_2_690x366.jpeg" alt="3dslicer" data-base62-sha1="8jKoh54Q9RUg9vSLlSzRFqlP2ni" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a4cdf5275685e91599d64c3952a366a3225bbe4_2_690x366.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a4cdf5275685e91599d64c3952a366a3225bbe4_2_1035x549.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3a4cdf5275685e91599d64c3952a366a3225bbe4_2_1380x732.jpeg 2x" data-dominant-color="64646A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3dslicer</span><span class="informations">1919×1019 189 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @rbumm (2022-11-17 20:25 UTC)

<p>Interactive lobe segmentation is part of the Chest Imaging Platform which is partly outdated and has known problems with certain lung CT datasets. This module will probably be one of the next on our list to fix. If you identify errors and have working fixes we would greatly appreciate a pull request.</p>
<p>In the meantime, you could use the Lung CT Segmenter module of the Lung Ct Analyzer package and its implementation of “lungmask” or “TotalSegmentator” AI packages.<br>
Both offer automatic lung lobe segmentation with Nvidia GPU.</p>
<p><a href="https://github.com/rbumm/SlicerLungCTAnalyzer/wiki/Step-2-Using-Lung-CT-Segmenter-with-AI">Refer to the wiki</a> for the setup which can be a bit tricky. Once set up on a computer with a strong GPU they can be real timesavers.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d7c35b0f8b6cfa2d9af4bce165948af85ba9fe0.jpeg" data-download-href="/uploads/short-url/4cPXOyG6THWF9WSwIiSqbHr5yH6.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d7c35b0f8b6cfa2d9af4bce165948af85ba9fe0_2_690x299.jpeg" alt="image" data-base62-sha1="4cPXOyG6THWF9WSwIiSqbHr5yH6" width="690" height="299" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d7c35b0f8b6cfa2d9af4bce165948af85ba9fe0_2_690x299.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d7c35b0f8b6cfa2d9af4bce165948af85ba9fe0_2_1035x448.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d7c35b0f8b6cfa2d9af4bce165948af85ba9fe0_2_1380x598.jpeg 2x" data-dominant-color="909094"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×833 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @wangjianmerci (2022-11-22 08:23 UTC)

<p>Thank you a lot, rbumm. After 4 days attempts, working with my laptop(16G+RTX3060), I finally failure to use Lung CT Segmenter module of the Lung Ct Analyzer package. I’d like to share some problems I met these days.<br>
First, Python could not install ‘lungmask’ module by ‘pip install git+https://github.com/JoHof/lungmask’. You need use an old script wrapper to install ‘lungmask’, like ‘import pip, pip.main([‘install’, ‘lungmask’])’.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5f3bc988fcff9b6b253ef3d364e27fe4995bfe7.png" data-download-href="/uploads/short-url/z5NbohOPpC3IgumMmxHN56AIE5N.png?dl=1" title="3dslcier2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5f3bc988fcff9b6b253ef3d364e27fe4995bfe7_2_690x368.png" alt="3dslcier2" data-base62-sha1="z5NbohOPpC3IgumMmxHN56AIE5N" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5f3bc988fcff9b6b253ef3d364e27fe4995bfe7_2_690x368.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5f3bc988fcff9b6b253ef3d364e27fe4995bfe7_2_1035x552.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f5f3bc988fcff9b6b253ef3d364e27fe4995bfe7_2_1380x736.png 2x" data-dominant-color="3E3B3C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3dslcier2</span><span class="informations">1929×1029 205 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Second, after ‘lungmask’ installed successfully, new errors loomed. Such as.<br>
‘‘Failed to compute results: unexpected EOF, expected 7749583 more bytes. The file might be corrupted.’’ , “Failed to compute results: std::bad_alloc: bad allocation” and so on.<br>
So I guessed they might be bugs with Windows, and I tried download Linux(Ubuntu) version. But the same problems I met, and 3dslicer would crash  in the end.<br>
Lung lobes segmentation is readly hard! I may need a rest and think how to go on!</p>

---

## Post #4 by @rbumm (2022-11-22 10:20 UTC)

<p>Sorry for keeping you busy for that long time, you should have responded earlier!<br>
We are here to help.</p>
<p>Anyway, it seems as if you might have write access problems when trying to install “lungmask”.<br>
Please do the following:</p>
<p>Install a fresh Windows version of Slicer 5.0.3 below your “Home” directory, where you have full read and write access.<br>
Your “Home” directory is usually at<br>
<code>c:\\users\yourname\ </code><br>
so you could use<br>
<code>c:\\users\yourname\Slicer5.0.3\</code></p>
<p>Start 3D Slicer from there.<br>
Install the Lung CT Analyzer extension again.<br>
Restart 3D Slicer.<br>
Load the CTChest dataset from “Sample Data”</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe283b6596f35eb21d0cbf7a8ecb8dca4f5fc8c4.png" alt="image" data-base62-sha1="AgntoOpZsL96norLLerOTtaABDu" width="238" height="217"></p>
<p>Rerun the lungmask lobe segmentation. Upon the first run, it should automatically install and run “lungmask”.</p>
<p>If you get errors:</p>
<p>Please do a manual install of the “lungmask” AI package within Slicer, enter</p>
<pre><code class="lang-auto">slicer.util.pip_install("git+https://github.com/JoHof/lungmask")
</code></pre>
<p>in the Python Interactor and press enter.</p>
<p>If this results in an error message box, please press “Ok” and paste the complete error message from the Python Interactor here.</p>

---

## Post #5 by @wangjianmerci (2022-11-24 05:31 UTC)

<p>Thank you again, rbumm, you are so kind.<br>
I did what you recommended, and as expected, ‘lungmask’ couldn’t be isntalled automatically.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc6bedb7693e4082117db4418184e52718b09c27.jpeg" data-download-href="/uploads/short-url/qSR01nSW3cEaLf7yBRVdYsauD3x.jpeg?dl=1" title="bugs" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc6bedb7693e4082117db4418184e52718b09c27_2_690x368.jpeg" alt="bugs" data-base62-sha1="qSR01nSW3cEaLf7yBRVdYsauD3x" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc6bedb7693e4082117db4418184e52718b09c27_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc6bedb7693e4082117db4418184e52718b09c27_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc6bedb7693e4082117db4418184e52718b09c27_2_1380x736.jpeg 2x" data-dominant-color="5F5E65"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bugs</span><span class="informations">1920×1024 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I manual installed in the Python Interactor and pressed enter.<br>
<em>slicer.util.pip_install(“git+https://github.com/JoHof/lungmask”)</em><br>
these are follow troubles.</p>
<pre><code class="lang-auto">Python 3.9.10 (main, Jul  8 2022, 02:32:50) [MSC v.1930 64 bit (AMD64)] on win32
&gt;&gt;&gt; slicer.util.pip_install("git+https://github.com/JoHof/lungmask")
Collecting git+https://github.com/JoHof/lungmask
  Cloning https://github.com/JoHof/lungmask to c:\users\wangjian\appdata\local\temp\pip-req-build-8gmwibu8
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Users\WangJian\Slicer 5.0.3\bin\Python\slicer\util.py", line 3527, in pip_install
    _executePythonModule('pip', args)
  File "C:\Users\WangJian\Slicer 5.0.3\bin\Python\slicer\util.py", line 3490, in _executePythonModule
    logProcessOutput(proc)
  File "C:\Users\WangJian\Slicer 5.0.3\bin\Python\slicer\util.py", line 3459, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/WangJian/Slicer 5.0.3/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'git+https://github.com/JoHof/lungmask']' returned non-zero exit status 1.
&gt;&gt;&gt; 
StartSegmentation completed in 1.63 seconds
Saving markups in temp directory ...
Torchlogic module not found
Querying light-the-torch for torch wheel...
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/light-the-torch/
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/light-the-torch/
WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/light-the-torch/
WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/light-the-torch/
WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/light-the-torch/
Could not fetch URL https://pypi.org/simple/light-the-torch/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/light-the-torch/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping
ERROR: Could not find a version that satisfies the requirement light-the-torch&lt;0.4 (from versions: none)
ERROR: No matching distribution found for light-the-torch&lt;0.4
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping
Failed to compute results: Command '['C:/Users/WangJian/Slicer 5.0.3/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'light-the-torch&lt;0.4']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "C:/Users/WangJian/Slicer 5.0.3/NA-MIC/Extensions-30893/LungCTAnalyzer/lib/Slicer-5.0/qt-scripted-modules/LungCTSegmenter.py", line 605, in runProcessing
    self.logic.applySegmentation()
  File "C:/Users/WangJian/Slicer 5.0.3/NA-MIC/Extensions-30893/LungCTAnalyzer/lib/Slicer-5.0/qt-scripted-modules/LungCTSegmenter.py", line 1644, in applySegmentation
    torch = torchLogic.installTorch(askConfirmation=True)
  File "C:/Users/WangJian/Slicer 5.0.3/NA-MIC/Extensions-30893/PyTorch/lib/Slicer-5.0/qt-scripted-modules/PyTorchUtils.py", line 93, in installTorch
    f'{self.wheelURL}'
  File "C:/Users/WangJian/Slicer 5.0.3/NA-MIC/Extensions-30893/PyTorch/lib/Slicer-5.0/qt-scripted-modules/PyTorchUtils.py", line 63, in wheelURL
    self._wheel = self.getTorchUrl()
  File "C:/Users/WangJian/Slicer 5.0.3/NA-MIC/Extensions-30893/PyTorch/lib/Slicer-5.0/qt-scripted-modules/PyTorchUtils.py", line 112, in getTorchUrl
    slicer.util.pip_install('light-the-torch&lt;0.4')
  File "C:\Users\WangJian\Slicer 5.0.3\bin\Python\slicer\util.py", line 3527, in pip_install
    _executePythonModule('pip', args)
  File "C:\Users\WangJian\Slicer 5.0.3\bin\Python\slicer\util.py", line 3490, in _executePythonModule
    logProcessOutput(proc)
  File "C:\Users\WangJian\Slicer 5.0.3\bin\Python\slicer\util.py", line 3459, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/WangJian/Slicer 5.0.3/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'light-the-torch&lt;0.4']' returned non-zero exit status 1.
&gt;&gt;&gt; slicer.util.pip_install("git+https://github.com/JoHof/lungmask")
Collecting git+https://github.com/JoHof/lungmask
  Cloning https://github.com/JoHof/lungmask to c:\users\wangjian\appdata\local\temp\pip-req-build-qgkg9ax7
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Users\WangJian\Slicer 5.0.3\bin\Python\slicer\util.py", line 3527, in pip_install
    _executePythonModule('pip', args)
  File "C:\Users\WangJian\Slicer 5.0.3\bin\Python\slicer\util.py", line 3490, in _executePythonModule
    logProcessOutput(proc)
  File "C:\Users\WangJian\Slicer 5.0.3\bin\Python\slicer\util.py", line 3459, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['C:/Users/WangJian/Slicer 5.0.3/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'git+https://github.com/JoHof/lungmask']' returned non-zero exit status 1.
&gt;&gt;&gt; 
</code></pre>

---

## Post #6 by @rbumm (2022-11-24 08:47 UTC)

<p>You seem to run into problems because git lungmask installation throws ssl certificate errors on your computer.</p>
<p>Please try</p>
<pre><code class="lang-auto">slicer.util.pip_install("lungmask")
</code></pre>
<p>in the Python Interactor and post the result.</p>

---

## Post #7 by @wangjianmerci (2022-11-24 13:07 UTC)

<p>It seems we can manual install ‘lungmask’ with follows codes:</p>
<pre><code class="lang-auto">import pip
pip.main(['install', 'lungmask'])
</code></pre>
<p>or</p>
<pre><code class="lang-auto">slicer.util.pip_install("lungmask")
</code></pre>
<p>And I find what matters finally! My CT file is too big, about 356MB, it run out my laptop’s memory! So when I turn  to use sample datas, everything is OK!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a3e7d4287644356b47a04ea15a07c8bdcb57019.jpeg" data-download-href="/uploads/short-url/hrq8jsyIUYS9CwhgYBuJTjCTkCd.jpeg?dl=1" title="workout" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a3e7d4287644356b47a04ea15a07c8bdcb57019_2_690x368.jpeg" alt="workout" data-base62-sha1="hrq8jsyIUYS9CwhgYBuJTjCTkCd" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a3e7d4287644356b47a04ea15a07c8bdcb57019_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a3e7d4287644356b47a04ea15a07c8bdcb57019_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a3e7d4287644356b47a04ea15a07c8bdcb57019_2_1380x736.jpeg 2x" data-dominant-color="5E5E5F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">workout</span><span class="informations">1920×1024 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Thank you very much, rbumm! I can enjoy the world cup now!<br>
My computer will be upgraded or CT datas should be smaller!</p>

---
