# 3D views synchronized using python

**Topic ID**: 45423
**Date**: 2025-12-09
**URL**: https://discourse.slicer.org/t/3d-views-synchronized-using-python/45423

---

## Post #1 by @PimBeentjes (2025-12-09 15:49 UTC)

<p>I am doing an VR/AR project in 3Dslicer, we open multiple 3D views, for example the black views shown in the image. We also have the blue 3D. We can now synchronize them in slicer by pressing the two interlooped circles, but I was wondering if there is a python function in the slicer library or somewhere else, to automatically synchronize and desynchronize them. I could not find anything on previously posted topics.</p>
<p>Pim</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbc0adacf9f668524da6148c2c716c471b4d8db1.png" data-download-href="/uploads/short-url/zV6EIkPBMrmCdQCsfgSckqxpzpf.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbc0adacf9f668524da6148c2c716c471b4d8db1_2_358x500.png" alt="image" data-base62-sha1="zV6EIkPBMrmCdQCsfgSckqxpzpf" width="358" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/b/fbc0adacf9f668524da6148c2c716c471b4d8db1_2_358x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbc0adacf9f668524da6148c2c716c471b4d8db1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fbc0adacf9f668524da6148c2c716c471b4d8db1.png 2x" data-dominant-color="CAC8C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">445×621 27 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @rfenioux (2025-12-15 10:35 UTC)

<p>That would be the <code>setSliceLink(bool)</code> function of the slice controller.</p>
<p>You can have a look at <a href="https://github.com/Slicer/Slicer/blob/6b52fb4f787d2eadee9870a3443b199168a0874c/Applications/SlicerApp/Testing/Python/RSNAQuantTutorial.py#L199" rel="noopener nofollow ugc">this example</a> to see how to use it (and how to retrieve the slice controller).<br>
Your views need to be in the same viewgroup, but if it works for you with the button it should already be the case.</p>

---

## Post #3 by @PimBeentjes (2025-12-15 10:56 UTC)

<p>Thanks for your response. As far as I know this only works for slice views in slicer. But the views I am using are 3d views and indeed that is also what I see when I try to use this. It gives an error that there is no slice with the corresponding name.</p>
<p>Do you know how it works for 3d views?</p>

---

## Post #4 by @cpinter (2025-12-15 11:05 UTC)

<p>For 3D views a different function is used (<code>SetLinkedControl</code>), see how it is in the source code when you press the button you mentioned:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/6b52fb4f787d2eadee9870a3443b199168a0874c/Libs/MRML/Widgets/qMRMLThreeDViewControllerWidget.cxx#L454">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/6b52fb4f787d2eadee9870a3443b199168a0874c/Libs/MRML/Widgets/qMRMLThreeDViewControllerWidget.cxx#L454" target="_blank" rel="noopener">github.com/Slicer/Slicer</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/6b52fb4f787d2eadee9870a3443b199168a0874c/Libs/MRML/Widgets/qMRMLThreeDViewControllerWidget.cxx#L454" target="_blank" rel="noopener">Libs/MRML/Widgets/qMRMLThreeDViewControllerWidget.cxx</a></h4>

<div class="git-blob-info">
  <a href="https://github.com/Slicer/Slicer/blob/6b52fb4f787d2eadee9870a3443b199168a0874c/Libs/MRML/Widgets/qMRMLThreeDViewControllerWidget.cxx#L454" rel="noopener"><code>6b52fb4f7</code></a>
</div>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="444" style="counter-reset: li-counter 443 ;">
          <li></li>
          <li>  vtkCollection* viewNodes = this-&gt;mrmlScene()-&gt;GetNodesByClass("vtkMRMLViewNode");</li>
          <li>  if (!viewNodes)</li>
          <li>  {</li>
          <li>    return;</li>
          <li>  }</li>
          <li></li>
          <li>  vtkMRMLViewNode* viewNode = nullptr;</li>
          <li>  for (viewNodes-&gt;InitTraversal(); (viewNode = vtkMRMLViewNode::SafeDownCast(viewNodes-&gt;GetNextItemAsObject()));)</li>
          <li>  {</li>
          <li class="selected">    viewNode-&gt;SetLinkedControl(linked);</li>
          <li>  }</li>
          <li>  viewNodes-&gt;Delete();</li>
          <li>}</li>
          <li></li>
          <li>//---------------------------------------------------------------------------</li>
          <li>void qMRMLThreeDViewControllerWidget::setViewLabel(const QString&amp; newViewLabel)</li>
          <li>{</li>
          <li>  Q_D(qMRMLThreeDViewControllerWidget);</li>
          <li>  if (!this-&gt;mrmlThreeDViewNode())</li>
          <li>  {</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @PimBeentjes (2025-12-15 12:35 UTC)

<p>Yes thanks! This function works great I used it like this:</p>
<pre><code>def link3dViews(self):
    lm = slicer.app.layoutManager()
    for name in ["View1", "LeftView", "RightView"]:
        widget = lm.threeDWidget(name)
        if widget and widget.mrmlViewNode():
            widget.mrmlViewNode().SetLinkedControl(True)

def unlink3dViews(self):
    lm = slicer.app.layoutManager()
    for name in ["View1", "LeftView", "RightView"]:
        widget = lm.threeDWidget(name)
        if widget and widget.mrmlViewNode():
            widget.mrmlViewNode().SetLinkedControl(False)
</code></pre>
<p>Only small bug that is happening, both methods are linked to a separate button, but I have to press unlink twice before the view actually unlinks, any idea why?</p>

---

## Post #6 by @PimBeentjes (2025-12-15 13:46 UTC)

<p>Accidently called both functions when trying to only call unlink, so it had to be done twice. This code should work for synchronizing 3d views!</p>

---
