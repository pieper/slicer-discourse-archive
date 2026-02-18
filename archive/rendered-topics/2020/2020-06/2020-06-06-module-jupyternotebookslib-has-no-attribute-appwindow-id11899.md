# Module 'JupyterNotebooksLib' has no attribute 'AppWindow'

**Topic ID**: 11899
**Date**: 2020-06-06
**URL**: https://discourse.slicer.org/t/module-jupyternotebookslib-has-no-attribute-appwindow/11899

---

## Post #1 by @Vinny (2020-06-06 13:55 UTC)

<p>Hi,</p>
<p>I’m interested in the newly developed feature of displaying Slicer output within Jupyter and have downloaded the Slicer jupyter notebook tutorials from… <a href="https://mybinder.org/v2/gh/lassoan/SlicerNotebooks/master" rel="nofollow noopener">https://mybinder.org/v2/gh/lassoan/SlicerNotebooks/master</a></p>
<p>However, I get the following error message after running the first cell:</p>
<hr>
<p>AttributeError                            Traceback (most recent call last)<br>
In  [1]:<br>
Line 4:</p>
<h2>AttributeError: module ‘JupyterNotebooksLib’ has no attribute ‘AppWindow’</h2>
<p>I can however load volumes within Jupyter and display them:</p>
<p>[success, loadedVolumeNode] = slicer.util.loadVolume(’/home/vinny/temp_data/test/t1.nii’, returnNode=True)</p>
<p>slicernb.ViewDisplay(“OneUpRedSlice”)</p>
<p>Slicer preview release 4.11.0-2020-06-05<br>
OS: Ubuntu 20.04.</p>
<p>Thanks for your help,</p>
<p>Vinny</p>

---

## Post #2 by @lassoan (2020-06-06 14:46 UTC)

<p>Have you completed all <a href="https://github.com/Slicer/SlicerJupyter/blob/master/README.md#setup">installation step</a>? In particular, have you installed ipywidgets in Slicer?</p>

---

## Post #3 by @Vinny (2020-06-06 15:31 UTC)

<p>Hi Andras,</p>
<p>Thanks for the link.  I followed the instructions (including installing ipywidgets) and no longer get the error message regarding a missing AppWindow.  However, the output doesn’t appear to be scaled to 0.5 similar to what is in the tutorial.  If I change the scaling factor, the window size does not change.  Is there anything else I missed?</p>

---

## Post #4 by @lassoan (2020-06-06 15:34 UTC)

<p>Does it work if you set the main window width and height directly?</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/SlicerJupyter/blob/master/JupyterNotebooks/JupyterNotebooksLib/widgets.py#L159" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/SlicerJupyter/blob/master/JupyterNotebooks/JupyterNotebooksLib/widgets.py#L159" target="_blank">Slicer/SlicerJupyter/blob/master/JupyterNotebooks/JupyterNotebooksLib/widgets.py#L159</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="149" style="counter-reset: li-counter 148 ;">
<li>
</li><li>@staticmethod</li>
<li>def setWindowSize(width=None, height=None, scale=None):</li>
<li>    if width is None:</li>
<li>        width = 1280</li>
<li>    if height is None:</li>
<li>        height = 1024</li>
<li>    if scale is not None:</li>
<li>        width *= scale</li>
<li>        height *= scale</li>
<li class="selected">    slicer.util.mainWindow().size = qt.QSize(width, height)</li>
<li>
</li><li>@staticmethod</li>
<li>def setContents(contents):</li>
<li>    if contents=="viewers":</li>
<li>        slicer.util.findChild(slicer.util.mainWindow(), "PanelDockWidget").hide()</li>
<li>        slicer.util.setStatusBarVisible(False)</li>
<li>        slicer.util.setMenuBarsVisible(False)</li>
<li>        slicer.util.setToolbarsVisible(False)</li>
<li>    elif contents=="full":</li>
<li>        slicer.util.findChild(slicer.util.mainWindow(), "PanelDockWidget").show()</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #5 by @Vinny (2020-06-06 15:50 UTC)

<p>If I interpreted it correctly, I changed the width and height as follows:</p>
<p>slicernb.AppWindow.setWindowSize(width=500,height=100)</p>
<p>but the height and width have not changed in the output.</p>
<p>Initially during the installation, a message appeared stating ipywidgets 7.0.0 was  not compatible with ipycanvas.  So I had upgraded it within Slicer to ipywidgets 7.5.1.</p>

---

## Post #6 by @lassoan (2020-06-06 17:08 UTC)

<p>If you execute <code>slicer.util.mainWindow().size = qt.QSize(width, height)</code> then does your main window size change? Maybe the window is maximized? We should then add a call before setting the window size to set normal window state.</p>

---

## Post #7 by @Vinny (2020-06-06 18:01 UTC)

<p>Thanks, I tried your suggestion but the window size still looks maximized.  Please see attached screenshot…perhaps I’m not calling the function properly?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57ebbf645fd95307291957e631c216f551e481fd.png" data-download-href="/uploads/short-url/cxMCRKHRtoyAE9f3SgDTzdcaXsV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57ebbf645fd95307291957e631c216f551e481fd_2_533x499.png" alt="image" data-base62-sha1="cxMCRKHRtoyAE9f3SgDTzdcaXsV" width="533" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57ebbf645fd95307291957e631c216f551e481fd_2_533x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/57ebbf645fd95307291957e631c216f551e481fd_2_799x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/57ebbf645fd95307291957e631c216f551e481fd.png 2x" data-dominant-color="8C8C8C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">888×833 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @lassoan (2020-06-06 18:04 UTC)

<p>Does size change work if you call <code>slicer.util.mainWindow().showNormal()</code> before?</p>

---

## Post #9 by @Vinny (2020-06-06 18:11 UTC)

<p>Thanks Andras, that does the job!  If the call is placed for example:</p>
<p>slicer.util.mainWindow().showNormal()<br>
slicer.util.mainWindow().size = qt.QSize(1200,1200)</p>
<p>Then when the width and height are changed, the window size changes.</p>
<p>With the tutorial set, adding in slicer.util.mainWindow().showNormal() before the slicernb.AppWindow.setWindowSize(scale=0.5) does the job too.</p>

---

## Post #10 by @lassoan (2020-06-06 18:52 UTC)

<p>Thanks for testing, I’ve pushed a <a href="https://github.com/Slicer/SlicerJupyter/commit/56dc86d67214d2ecccd6a569b41f30f7e1709f01">fix</a> to SlicerJupyter.</p>

---

## Post #11 by @Vinny (2020-06-06 21:13 UTC)

<p>Thanks for pushing the fix.  How can I install the latest SlicerJupyter extension with this fix?  I uninstalled the SlicerJupyter extension and re-installed it.  But the window size still does not change.</p>

---

## Post #12 by @lassoan (2020-06-06 21:19 UTC)

<p>Extensions are rebuilt nightly (for each new Preview Release and the latest Stable Release), so you can either wait for that or update the modified .py file on your computer.</p>

---

## Post #13 by @Vinny (2020-06-07 12:23 UTC)

<p>Thanks Andras for your help.  Just downloaded and installed the latest preview release (Version 4.11.0; 2020-06-06; revision 29114) and it works now.</p>

---
