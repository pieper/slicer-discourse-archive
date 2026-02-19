---
topic_id: 30771
title: "Scripted Module How To Install And Import Tensorflow Cpu On"
date: 2023-07-25
url: https://discourse.slicer.org/t/30771
---

# Scripted Module: How to install and import tensorflow-cpu on M2 Mac

**Topic ID**: 30771
**Date**: 2023-07-25
**URL**: https://discourse.slicer.org/t/scripted-module-how-to-install-and-import-tensorflow-cpu-on-m2-mac/30771

---

## Post #1 by @Geventh (2023-07-25 01:44 UTC)

<p>Hey up until recently I used an Intel Mac and was able to import and use tensorflow and my first ever extension worked fine <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>With the M2 Mac Slicer crashes when the module tries to install tensorflow by <code>slicer.util.pip_install("tensorflow")</code> .</p>
<p>Installing the cpu-only version seems work:   <code>slicer.util.pip_install("tensorflow-cpu")</code> but when I try to import it it seems to crash again. <code>import tensorflow as tf</code></p>
<p>Thanks a lot for your patience.</p>

---

## Post #2 by @lassoan (2023-07-25 02:06 UTC)

<aside class="quote no-group" data-username="Geventh" data-post="1" data-topic="30771">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/geventh/48/66950_2.png" class="avatar"> Geventh:</div>
<blockquote>
<p>With the M2 Mac Slicer crashes when the module tries to install tensorflow by <code>slicer.util.pip_install("tensorflow")</code> .</p>
</blockquote>
</aside>
<p>In recent years, pytorch has become the dominant AI framework in medical image computing and all Slicer extensions use pytorch and not tensorflow. They use the PyTorch Slicer extension to install and configure PyTorch and it runs well on all platforms.</p>
<p>I’m not sure if anyone would want to invest time now into exploring how to install and run tensorflow in Slicer, so if you want to keep using tensorflow then it may be easier to run it outside Slicer’s Python environment. You can keep everything in the same in your Python scripted module except that you use tensorflow in the external Python environment (run the external Python.exe using <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.launchConsoleProcess">slicer.util.launchConsoleProcess</a>).</p>

---

## Post #3 by @Geventh (2023-07-25 13:38 UTC)

<p>I converted my tensorflow model to ONNX format.<br>
<code>slicer.util.pip_install("onnxruntime")</code> works and my extension is able to get similar result!</p>
<p>Is there a guide for optimal deployment of ML models in 3D Slicer?</p>
<p>Also is there proper way to install python libraries (ideally from a requirements.txt file)?<br>
Currently I’m checking/installing them when the Slicer App initialises the Modules:</p>
<pre><code class="lang-auto">for module in requirements:
    try:
        importlib.import_module(module)
    except ModuleNotFoundError:
        slicer.util.pip_install(module)
</code></pre>
<p>Any relevant code example for this:</p>
<pre><code class="lang-auto">slicer.util.launchConsoleProcess
</code></pre>
<p>Thanks for taking your time!</p>

---
