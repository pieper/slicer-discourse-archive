---
topic_id: 28774
title: "Ssl Error When Lung Ct Segmenter Is Trying To Instal Light T"
date: 2023-04-06
url: https://discourse.slicer.org/t/28774
---

# SSL error when Lung CT segmenter is trying to instal light-the-torch

**Topic ID**: 28774
**Date**: 2023-04-06
**URL**: https://discourse.slicer.org/t/ssl-error-when-lung-ct-segmenter-is-trying-to-instal-light-the-torch/28774

---

## Post #1 by @wangjianmerci (2023-04-06 03:58 UTC)

<p>Operating system:Windows<br>
Slicer version:5.2.2<br>
Hardware：R7-5800H+32G+3060laptop（6G）<br>
When I want use AI Lung lobe segmenter in 3dslicer 5.2.2, it asked to install <em><strong>light-the-torch</strong></em>.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc15515c0e840c4a960d4657c6214a4310d8a595.jpeg" data-download-href="/uploads/short-url/qPRr8iK7jjfyMxSD4UTgvjCRqtf.jpeg?dl=1" title="微信图片_20230406113641" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc15515c0e840c4a960d4657c6214a4310d8a595_2_690x368.jpeg" alt="微信图片_20230406113641" data-base62-sha1="qPRr8iK7jjfyMxSD4UTgvjCRqtf" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc15515c0e840c4a960d4657c6214a4310d8a595_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc15515c0e840c4a960d4657c6214a4310d8a595_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc15515c0e840c4a960d4657c6214a4310d8a595_2_1380x736.jpeg 2x" data-dominant-color="5E5E65"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20230406113641</span><span class="informations">1920×1024 154 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>But error .<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edcbf45e82f3e40e95ebac2e4300f6f2a8a4cb64.jpeg" data-download-href="/uploads/short-url/xVE886CHm7kOqI0h6HoILtlQj9q.jpeg?dl=1" title="微信图片_20230406113700" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edcbf45e82f3e40e95ebac2e4300f6f2a8a4cb64_2_690x368.jpeg" alt="微信图片_20230406113700" data-base62-sha1="xVE886CHm7kOqI0h6HoILtlQj9q" width="690" height="368" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edcbf45e82f3e40e95ebac2e4300f6f2a8a4cb64_2_690x368.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edcbf45e82f3e40e95ebac2e4300f6f2a8a4cb64_2_1035x552.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edcbf45e82f3e40e95ebac2e4300f6f2a8a4cb64_2_1380x736.jpeg 2x" data-dominant-color="5E5D64"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">微信图片_20230406113700</span><span class="informations">1920×1024 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code class="lang-auto">[Qt] ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 1000 1
Exception ignored in: &lt;function SegmentEditorEffect.__del__ at 0x00000248AFCE1940&gt;
Traceback (most recent call last):
  File "E:/3dslicerreport/3dslicer/Slicer 5.2.2/NA-MIC/Extensions-31382/NvidiaAIAssistedAnnotation/lib/Slicer-5.2/qt-scripted-modules/SegmentEditorNvidiaAIAALib/SegmentEditorEffect.py", line 59, in __del__
    AbstractScriptedSegmentEditorEffect.__del__(self)
AttributeError: type object 'AbstractScriptedSegmentEditorEffect' has no attribute '__del__'
[Qt] QLayout::addChildLayout: layout "" already has a parent
[Qt] ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 1000 1
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/light-the-torch/
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/light-the-torch/
WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/light-the-torch/
WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/light-the-torch/
WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/light-the-torch/
Could not fetch URL https://pypi.org/simple/light-the-torch/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/light-the-torch/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping
ERROR: Could not find a version that satisfies the requirement light-the-torch&gt;=0.5 (from versions: none)
ERROR: No matching distribution found for light-the-torch&gt;=0.5
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping
[Python] Failed to compute results: Command '['E:/3dslicerreport/3dslicer/Slicer 5.2.2/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'light-the-torch&gt;=0.5']' returned non-zero exit status 1.
Traceback (most recent call last):
  File "E:/3dslicerreport/3dslicer/Slicer 5.2.2/NA-MIC/Extensions-31382/PyTorch/lib/Slicer-5.2/qt-scripted-modules/PyTorchUtils.py", line 182, in installTorch
    import light_the_torch._patch
ModuleNotFoundError: No module named 'light_the_torch'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "E:/3dslicerreport/3dslicer/Slicer 5.2.2/NA-MIC/Extensions-31382/LungCTAnalyzer/lib/Slicer-5.2/qt-scripted-modules/LungCTSegmenter.py", line 970, in runProcessing
    self.logic.applySegmentation()
  File "E:/3dslicerreport/3dslicer/Slicer 5.2.2/NA-MIC/Extensions-31382/LungCTAnalyzer/lib/Slicer-5.2/qt-scripted-modules/LungCTSegmenter.py", line 2181, in applySegmentation
    torch = torchLogic.installTorch(askConfirmation=True)
  File "E:/3dslicerreport/3dslicer/Slicer 5.2.2/NA-MIC/Extensions-31382/PyTorch/lib/Slicer-5.2/qt-scripted-modules/PyTorchUtils.py", line 184, in installTorch
    PyTorchUtilsLogic._installLightTheTorch()
  File "E:/3dslicerreport/3dslicer/Slicer 5.2.2/NA-MIC/Extensions-31382/PyTorch/lib/Slicer-5.2/qt-scripted-modules/PyTorchUtils.py", line 206, in _installLightTheTorch
    slicer.util.pip_install('light-the-torch&gt;=0.5')
  File "E:\3dslicerreport\3dslicer\Slicer 5.2.2\bin\Python\slicer\util.py", line 3578, in pip_install
    _executePythonModule('pip', args)
  File "E:\3dslicerreport\3dslicer\Slicer 5.2.2\bin\Python\slicer\util.py", line 3540, in _executePythonModule
    logProcessOutput(proc)
  File "E:\3dslicerreport\3dslicer\Slicer 5.2.2\bin\Python\slicer\util.py", line 3509, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['E:/3dslicerreport/3dslicer/Slicer 5.2.2/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'light-the-torch&gt;=0.5']' returned non-zero exit status 1.
[VTK] Warning: In D:\D\S\S-0\Libs\MRML\Core\vtkMRMLSegmentationDisplayNode.cxx, line 287
[VTK] vtkMRMLSegmentationDisplayNode (000002492002D5C0): vtkMRMLSegmentationDisplayNode::GetSegmentDisplayProperties: no display properties are found for segment ID=, return default
</code></pre>
<p>I tried to install by codes:<br>
<code>slicer.util.pip_install("light-the-torch&gt;=0.5")</code></p>
<pre><code class="lang-auto">&gt;&gt;&gt; slicer.util.pip_install("light-the-torch&gt;=0.5")
WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/light-the-torch/
WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/light-the-torch/
WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/light-the-torch/
WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/light-the-torch/
WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /simple/light-the-torch/
Could not fetch URL https://pypi.org/simple/light-the-torch/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/light-the-torch/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping
ERROR: Could not find a version that satisfies the requirement light-the-torch&gt;=0.5 (from versions: none)
ERROR: No matching distribution found for light-the-torch&gt;=0.5
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/pip/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping
Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "E:\3dslicerreport\3dslicer\Slicer 5.2.2\bin\Python\slicer\util.py", line 3578, in pip_install
    _executePythonModule('pip', args)
  File "E:\3dslicerreport\3dslicer\Slicer 5.2.2\bin\Python\slicer\util.py", line 3540, in _executePythonModule
    logProcessOutput(proc)
  File "E:\3dslicerreport\3dslicer\Slicer 5.2.2\bin\Python\slicer\util.py", line 3509, in logProcessOutput
    raise CalledProcessError(retcode, proc.args, output=proc.stdout, stderr=proc.stderr)
subprocess.CalledProcessError: Command '['E:/3dslicerreport/3dslicer/Slicer 5.2.2/bin/../bin\\PythonSlicer.EXE', '-m', 'pip', 'install', 'light-the-torch&gt;=0.5']' returned non-zero exit status 1.
</code></pre>
<p>How could I solve the problem? Appreciate your help！</p>

---

## Post #2 by @muratmaga (2023-04-06 05:18 UTC)

<aside class="quote no-group" data-username="wangjianmerci" data-post="1" data-topic="28774">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/wangjianmerci/48/17372_2.png" class="avatar"> wangjianmerci:</div>
<blockquote>
<p>How could I solve the problem? Appreciate your help！</p>
</blockquote>
</aside>
<p>Did you try the PyTorch extension? Install the extension, switch to the pytorch module and then choose the automatic method. Then re-try the Lung CT Segmenter</p>

---

## Post #3 by @rbumm (2023-04-06 06:26 UTC)

<p>Yes, please use the PyTorch extension to install the torch dependencies.</p>

---

## Post #4 by @lassoan (2023-04-06 13:09 UTC)

<aside class="quote no-group" data-username="wangjianmerci" data-post="1" data-topic="28774">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/wangjianmerci/48/17372_2.png" class="avatar"> wangjianmerci:</div>
<blockquote>
<p><code>Could not fetch URL https://pypi.org/simple/light-the-torch/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /simple/light-the-torch/ (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))) - skipping</code></p>
</blockquote>
</aside>
<p>It is an SSL error. Most likely you are connecting to the internet via a proxy server/VPN/firewall that messes with your connection. Can you connect to the internet directly?</p>

---

## Post #5 by @wangjianmerci (2023-04-06 16:08 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/muratmaga">@muratmaga</a> <a class="mention" href="/u/lassoan">@lassoan</a> , *Thank you so much, I really appreciate your help!<br>
I reinstall <em><strong>PyTorch extension</strong></em>, and try again. It really works. But download speed is very slow(&lt;30kb/s) cause the <em>Great FireWall</em>. Beacause the slow speed, net had dissconnected many times.<br>
So I meet the dilemma that download speed really slow without a proxy or can not fetch URL via proxy.</p>

---

## Post #6 by @muratmaga (2023-04-06 16:12 UTC)

<p>Whether you use through pip_install or via extension, they are going to bring the same package one way or the other. Perhaps what you can do is to obtain the correct wheel name from the pytorch logs, download in a different manner where you can reconnect and continue (curl? wget?), and once you get a copy of the wheel use the pip_install, but ask to use the local file.</p>

---

## Post #8 by @wangjianmerci (2023-04-07 02:41 UTC)

<p>Thank you for your valuable advice. Actually, I want to figure out a way can download the packages manual, and install locally. But I really don’t how to do in 3dslicer.</p>

---

## Post #9 by @lassoan (2023-04-15 16:44 UTC)

<p>You can download and pip install packages in Slicer’s Python environment the same way as in any other Python environment. The Python interpreter exectuable is <code>PythonSlicer</code>, so you can for example install a package like this: <code>PythonSlicer -m pip install packagename</code></p>

---

## Post #10 by @wangjianmerci (2023-08-02 01:33 UTC)

<p>my computer can’t install <em>lungmask</em> automatically cause the Internet limits.</p>
<pre><code class="lang-auto">Collecting https://github.com/JoHof/lungmask/archive/master.zip
  WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /JoHof/lungmask/archive/master.zip
  WARNING: Retrying (Retry(total=3, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /JoHof/lungmask/archive/master.zip
  WARNING: Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /JoHof/lungmask/archive/master.zip
  WARNING: Retrying (Retry(total=1, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /JoHof/lungmask/archive/master.zip
  WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) after connection broken by 'SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)'))': /JoHof/lungmask/archive/master.zip
ERROR: Could not install packages due to an OSError: HTTPSConnectionPool(host='github.com', port=443): Max retries exceeded with url: /JoHof/lungmask/archive/master.zip (Caused by SSLError(SSLEOFError(8, 'EOF occurred in violation of protocol (_ssl.c:1129)')))

</code></pre>
<p>so  can I  install the package manual ?</p>

---

## Post #11 by @lassoan (2023-08-02 03:48 UTC)

<p>The AI model is stored on github, so you need to resolve your internet connectivity to github. For example, you may try to use a VPN.</p>

---

## Post #12 by @wangjianmerci (2023-08-02 08:54 UTC)

<p>Thank you a lot . I  tried to download on GitHub and installed manual in  terminal. It really  worked.  thanks  again !</p>

---
