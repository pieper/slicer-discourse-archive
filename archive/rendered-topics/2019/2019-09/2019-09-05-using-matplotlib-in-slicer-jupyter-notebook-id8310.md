---
topic_id: 8310
title: "Using Matplotlib In Slicer Jupyter Notebook"
date: 2019-09-05
url: https://discourse.slicer.org/t/8310
---

# Using matplotlib in Slicer jupyter notebook

**Topic ID**: 8310
**Date**: 2019-09-05
**URL**: https://discourse.slicer.org/t/using-matplotlib-in-slicer-jupyter-notebook/8310

---

## Post #1 by @mikebind (2019-09-05 14:31 UTC)

<p>Hello, I am using Slicer 4.11.0-2019-08-29 with jupyter notebook.  I would like to be able to use matplotlib in the notebook to do things like plot histograms.  I have successfully pip-installed matplotlib with <code>slicer.util.pip_install('matplotlib')</code>, and get no errors with <code>import matplotlib</code>.  However, if I <code>import matplotlib.pyplot as plt</code>, I get the following error message:</p>
<pre><code>Traceback (most recent call last):
  File "&lt;console&gt;", line 1, in &lt;module&gt;
  File "C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.11.0-2019-08-29\lib\Python\Lib\site-packages\matplotlib\pyplot.py", line 2355, in &lt;module&gt;
    switch_backend(rcParams["backend"])
  File "C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.11.0-2019-08-29\lib\Python\Lib\site-packages\matplotlib\pyplot.py", line 221, in switch_backend
    backend_mod = importlib.import_module(backend_name)
  File "C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.11.0-2019-08-29\lib\Python\Lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.11.0-2019-08-29\lib\Python\Lib\site-packages\matplotlib\backends\backend_tkagg.py", line 1, in &lt;module&gt;
    from . import _backend_tk
  File "C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.11.0-2019-08-29\lib\Python\Lib\site-packages\matplotlib\backends\_backend_tk.py", line 6, in &lt;module&gt;
    import tkinter as tk
  File "C:\Users\mikeb\AppData\Local\NA-MIC\Slicer 4.11.0-2019-08-29\lib\Python\Lib\tkinter\__init__.py", line 36, in &lt;module&gt;
    import _tkinter # If this fails your Python may not be configured for Tk
ModuleNotFoundError: No module named '_tkinter'
</code></pre>
<p>I am guessing that, as the error message suggests, the Slicer python may not be configured for Tk (since it uses Qt for GUI), but I’m not sure how to fix this.  I have not had any luck googling to figure out how to install Tk because everywhere I look says “Tk is already included with standard python, you don’t have to install it”.</p>
<p>Any suggestions?  I just want to use matplotlib for basic plotting and data exploration as I am working on algorithm development for a segmentation/processing module.  If there is another easy-to-use alternative which will already work with Slicer that would be fine.  I have a little experience with matplotlib and know it works well with jupyter notebooks, so that’s why I was trying to use that tool.</p>
<p>Thanks for considering and for any suggestions!</p>

---

## Post #2 by @lassoan (2019-09-05 15:40 UTC)

<p>You need to choose a suitable matplotlib backend. See example here:</p>
<aside class="quote quote-modified" data-post="5" data-topic="7162">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/use-full-power-of-python-in-slicer/7162/5">Use full power of Python in Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    I’ve just tried interactive plotting using matplotlib and it works fine for me on Windows. I just had to switch to WXAgg backend. 
Setup: 
pip_install("matplotlib wxPython")

Example interactive plot using matplotlib: 
# Get a volume from SampleData and compute its histogram
import SampleData
import numpy as np
volumeNode = SampleData.SampleDataLogic().downloadMRHead()
histogram = np.histogram(arrayFromVolume(volumeNode), bins=50)

# Set matplotlib to use WXAgg backend
import matplotlib
matplotl…
  </blockquote>
</aside>

<p>Note that you can also use Slicer’s built-in interactive plotting features. The advantage of Slicer plots is that they are directly connected to MRML nodes: if you update a value in a table node then the plot is updated immediately (and you can drag-and-drop points in the plot to change values in a table).</p>

---

## Post #3 by @mikebind (2019-09-05 16:22 UTC)

<p>OK, install works great, I can generate plots and view them with plt.show().  However, the <code>%matplotlib inline</code> magic command for jupyter notebook doesn’t seem to work (gives a syntax error).  Should this work?</p>

---

## Post #4 by @lassoan (2019-09-05 18:38 UTC)

<p>Magic commands are not supported in SlicerJupyter.</p>

---

## Post #5 by @mikebind (2019-09-05 18:39 UTC)

<p>OK, that’s not too bad.  Thanks very much for your help.</p>

---

## Post #6 by @mikebind (2019-09-06 16:03 UTC)

<p>I see that SlicerJupyter’s display() command can put images into the output field.  Is there a way to create a function to do that with a png image I generate?<br>
My ability to read C++ is very limited, but it looks to me like the display function ends up running <code>execute_display_command</code>, which writes the image in some format to standard out.<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/SlicerJupyter/blob/672f13cd141955466ea82033bdfa66a63c021449/JupyterKernel/xSlicerInterpreter.cxx#L166-L185" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerJupyter/blob/672f13cd141955466ea82033bdfa66a63c021449/JupyterKernel/xSlicerInterpreter.cxx#L166-L185" target="_blank" rel="nofollow noopener">Slicer/SlicerJupyter/blob/672f13cd141955466ea82033bdfa66a63c021449/JupyterKernel/xSlicerInterpreter.cxx#L166-L185</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="166" style="counter-reset: li-counter 165 ;">
<li>std::string xSlicerInterpreter::execute_display_command()</li>
<li>{</li>
<li>  show_view_controllers(false);</li>
<li>
</li>
<li>  // Make sure display updates are completed</li>
<li>  qSlicerApplication::application()-&gt;processEvents();</li>
<li>  force_render();</li>
<li>
</li>
<li>  qSlicerLayoutManager* layoutManager = qSlicerApplication::application()-&gt;layoutManager();</li>
<li>  QPixmap screenshot = layoutManager-&gt;viewport()-&gt;grab();</li>
<li>  QByteArray bArray;</li>
<li>  QBuffer buffer(&amp;bArray);</li>
<li>  buffer.open(QIODevice::WriteOnly);</li>
<li>  screenshot.save(&amp;buffer, "PNG");</li>
<li>  QString base64 = QString::fromLatin1(bArray.toBase64().data());</li>
<li>
</li>
<li>  show_view_controllers(true);</li>
<li>
</li>
<li>  return base64.toStdString();</li>
<li>}</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
Could I possibly do something similar from python?  If so, how?</p>

---

## Post #7 by @lassoan (2019-09-06 18:37 UTC)

<p>I’ll have a look and get back to you soon.</p>

---

## Post #8 by @mikebind (2019-09-06 19:07 UTC)

<p>Thanks for taking a look!</p>

---

## Post #9 by @lassoan (2019-09-07 12:08 UTC)

<p>I’ve updated <code>display()</code> function to accept variables and files. You can now display a png file using:</p>
<pre><code>display(filename='MatplotlibExample.png', type="image/png", binary=True)
</code></pre>
<p>                    <a href="https://www.slicer.org/w/images/a/a2/JupyterNotebookMatplotlibExample.png" target="_blank" class="onebox" rel="nofollow noopener">
            <img src="https://www.slicer.org/w/images/a/a2/JupyterNotebookMatplotlibExample.png" width="" height="">
          </a>

</p>
<p>Complete example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Plot_in_Slicer_Jupyter_notebook" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Plot_in_Slicer_Jupyter_notebook</a></p>

---

## Post #10 by @mikebind (2019-09-09 16:31 UTC)

<p>Thanks, this is outstanding.</p>

---
