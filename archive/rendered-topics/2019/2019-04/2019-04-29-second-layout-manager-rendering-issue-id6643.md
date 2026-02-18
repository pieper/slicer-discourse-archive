# Second layout manager rendering issue

**Topic ID**: 6643
**Date**: 2019-04-29
**URL**: https://discourse.slicer.org/t/second-layout-manager-rendering-issue/6643

---

## Post #1 by @jamesobutler (2019-04-29 19:51 UTC)

<p>I have a second layout manager that I’m using in an outside window (Slicer main window not displayed).  Does anyone recognize what this rendering issue might mean? Not setting some size policy correctly?</p>
<pre data-code-wrap="python"><code class="lang-python">layout_widget = slicer.qMRMLLayoutWidget()
layout_widget.setMRMLScene(slicer.mrmlScene)
layout_manager = slicer.qSlicerLayoutManager()
layout_manager.setMRMLScene(slicer.mrmlScene)
layout_widget.setLayoutManager(layout_manager)
slicer.app.setLayoutManager(layout_manager)

slicer_views_layout = self.findChild(qt.QVBoxLayout, "slicer_views_layout")
slicer_views_layout.addWidget(layout_widget)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd1c2afe5cf8292ef83f2cefa1c7608f7d7109f7.png" data-download-href="/uploads/short-url/tguejTMi73iu6lnd2rAhkvrfRlR.png?dl=1" title="layout-manager-problem-1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd1c2afe5cf8292ef83f2cefa1c7608f7d7109f7_2_584x500.png" alt="layout-manager-problem-1" data-base62-sha1="tguejTMi73iu6lnd2rAhkvrfRlR" width="584" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd1c2afe5cf8292ef83f2cefa1c7608f7d7109f7_2_584x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/d/cd1c2afe5cf8292ef83f2cefa1c7608f7d7109f7_2_876x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cd1c2afe5cf8292ef83f2cefa1c7608f7d7109f7.png 2x" data-dominant-color="0F0B0B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">layout-manager-problem-1</span><span class="informations">938×803 7.14 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2019-04-29 19:57 UTC)

<p>and another…<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91de67cb1b163149fde734d5b33573b583c56ef6.png" data-download-href="/uploads/short-url/kOpJy6yBkGDJNZfDK9nOs1HmdAG.png?dl=1" title="layout-manager-problem-2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91de67cb1b163149fde734d5b33573b583c56ef6_2_527x500.png" alt="layout-manager-problem-2" data-base62-sha1="kOpJy6yBkGDJNZfDK9nOs1HmdAG" width="527" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91de67cb1b163149fde734d5b33573b583c56ef6_2_527x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/1/91de67cb1b163149fde734d5b33573b583c56ef6_2_790x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91de67cb1b163149fde734d5b33573b583c56ef6.png 2x" data-dominant-color="0C0B07"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">layout-manager-problem-2</span><span class="informations">834×790 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @cpinter (2019-04-29 20:12 UTC)

<p>I haven’t seen these artifacts before, but it may be because you set the layout manager to Slicer app. This is how a second layout manager is created in an existing slicelet:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/SlicerRt/GelDosimetryAnalysis/blob/master/GelDosimetryAnalysis/GelDosimetryAnalysis.py#L159-L161" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/SlicerRt/GelDosimetryAnalysis/blob/master/GelDosimetryAnalysis/GelDosimetryAnalysis.py#L159-L161" target="_blank" rel="nofollow noopener">SlicerRt/GelDosimetryAnalysis/blob/master/GelDosimetryAnalysis/GelDosimetryAnalysis.py#L159-L161</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="159" style="counter-reset: li-counter 158 ;">
<li>self.layoutWidget = slicer.qMRMLLayoutWidget()
</li>
<li>self.layoutWidget.setMRMLScene(slicer.mrmlScene)
</li>
<li>self.parent.layout().addWidget(self.layoutWidget,2)
</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>So no layout manager is created explicitly and it is not set to the app. I think it should not be set to the app if you use a second window, because the Slicer app layout manager corresponds to the main Slicer window’s layout.<br>
Check out the rest of the file for usage (see <code>self.layoutWidget.layoutManager()</code>).</p>

---

## Post #4 by @jamesobutler (2019-04-29 21:41 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a>, you were correct about setting the layout manager to slicer app causing the issues. I commented out the lines as seen below and the rendering issues have appeared to go away.</p>
<pre><code class="lang-python">layout_widget = slicer.qMRMLLayoutWidget()
layout_widget.setMRMLScene(slicer.mrmlScene)
# layout_manager = slicer.qSlicerLayoutManager()
# layout_manager.setMRMLScene(slicer.mrmlScene)
# layout_widget.setLayoutManager(layout_manager)
# slicer.app.setLayoutManager(layout_manager)

slicer_views_layout = self.findChild(qt.QVBoxLayout, "slicer_views_layout")
slicer_views_layout.addWidget(layout_widget)
</code></pre>

---
