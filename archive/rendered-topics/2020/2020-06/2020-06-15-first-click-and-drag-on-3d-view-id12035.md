# First click-and-drag on 3D view

**Topic ID**: 12035
**Date**: 2020-06-15
**URL**: https://discourse.slicer.org/t/first-click-and-drag-on-3d-view/12035

---

## Post #1 by @ada (2020-06-15 15:26 UTC)

<p>Hi all,<br>
After a first 3D loading, the volume is well displayed and I want to use the mouse to rotate the 3D view.</p>
<p>I do not know why but the first click-and-drag event with the mouse moves one of the ROI side (I control one of the colored points of my ROI) even if my click is not over the node. After releasing the left button, the next click-and-drag allows me to rotate the 3D view.</p>
<p>Is there any function to call in the slicerrc file to avoid the phenomenum?</p>
<p>Best</p>

---

## Post #2 by @pieper (2020-06-15 15:40 UTC)

<p>It sounds like you are volume rendering with the cropping ROI enabled?  You can turn off the visibility and it won’t be visible or selectable.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5bbee767b8c8410eeba99de2605148ebc5947e51.png" alt="image" data-base62-sha1="d5CsuEqdAGOVLgswX0Ey9zyXzaN" width="502" height="250"></p>
<p>If that’s not it, post a screenshot and provide the exact steps.</p>

---

## Post #3 by @ada (2020-06-15 15:44 UTC)

<p>Hello <span class="mention">@pierper</span>,<br>
Yes this is true, but I want to chane the camera rotation without disabling the Display ROI.</p>

---

## Post #4 by @pieper (2020-06-15 15:57 UTC)

<p>I agree it can be inconvenient that the ROI widget grabs all the mouse events, but for now I think you just need to be aware of it, and either turn it off when not using it or maybe zoom out a bit with the mouse wheel before rotating.</p>

---

## Post #5 by @lassoan (2020-06-15 16:58 UTC)

<p>I think <a class="mention" href="/u/ada">@ada</a> refers to the bug that the first interaction in a 3D view after displaying a ROI adjusts that ROI.</p>
<p>As a workaround, you can click once in the 3D view before you click-and-drag the first time you show an annotation ROI.</p>
<p>Since a workaround exists and we will add much better ROI widget to markups module, I don’t think we will fix this bug.</p>

---

## Post #6 by @ada (2020-06-16 12:40 UTC)

<p>Yes <a class="mention" href="/u/lassoan">@lassoan</a> it is exactly what you are describing. I understand.</p>
<p>Nevertheless, is it possible to automatically create a “fake” click on the 3D view with python (as the user could do) ?<br>
For my use, it could be useful to automatically “fake” some mouse clicks</p>

---

## Post #7 by @pieper (2020-06-16 13:03 UTC)

<p>It would be just a workaround, but if you really need to you could use this testing method.</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/276c72e150f62d719f75d1606a47f959557454b2/Base/Python/slicer/util.py#L1948" target="_blank">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/276c72e150f62d719f75d1606a47f959557454b2/Base/Python/slicer/util.py#L1948" target="_blank">Slicer/Slicer/blob/276c72e150f62d719f75d1606a47f959557454b2/Base/Python/slicer/util.py#L1948</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="1938" style="counter-reset: li-counter 1937 ;">
<li>
</li><li>def settingsValue(key, default, converter=lambda v: v, settings=None):</li>
<li>  """Return settings value associated with key if it exists or the provided default otherwise.</li>
<li>
</li><li>  ``settings`` parameter is expected to be a valid ``qt.Settings`` object.</li>
<li>  """</li>
<li>  import qt</li>
<li>  settings = qt.QSettings() if settings is None else settings</li>
<li>  return converter(settings.value(key)) if settings.contains(key) else default</li>
<li>
</li><li class="selected">def clickAndDrag(widget,button='Left',start=(10,10),end=(10,40),steps=20,modifiers=[]):</li>
<li>  """</li>
<li>  Send synthetic mouse events to the specified widget (qMRMLSliceWidget or qMRMLThreeDView)</li>
<li>
</li><li>  :param button: "Left", "Middle", "Right", or "None"</li>
<li>   start, end : window coordinates for action</li>
<li>  :param steps: number of steps to move in, if &lt;2 then mouse jumps to the end position</li>
<li>  :param modifiers: list containing zero or more of "Shift" or "Control"</li>
<li>
</li><li>  .. hint::</li>
<li>  </li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
