# How can I call Slicer.util.getNode function in cpp code?

**Topic ID**: 8255
**Date**: 2019-09-02
**URL**: https://discourse.slicer.org/t/how-can-i-call-slicer-util-getnode-function-in-cpp-code/8255

---

## Post #1 by @JaceYang (2019-09-02 05:55 UTC)

<p>Hello,everyone:<br>
We can get node using Slicer.util.getNode in python console and scripted extensions.But how can I call this function in cpp code?<br>
I want to call the qMRMLThreeDView.resetFocalPoint when I click the Display 3D button to make the 3D model be in the center of the 3D view.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/c/8c1267841eb613518921e770355c2f5a36235b84.png" data-download-href="/uploads/short-url/jZ8haS2z0WuediWOEbUCHPcamdS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c1267841eb613518921e770355c2f5a36235b84_2_690x293.png" alt="image" data-base62-sha1="jZ8haS2z0WuediWOEbUCHPcamdS" width="690" height="293" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c1267841eb613518921e770355c2f5a36235b84_2_690x293.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c1267841eb613518921e770355c2f5a36235b84_2_1035x439.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/c/8c1267841eb613518921e770355c2f5a36235b84_2_1380x586.png 2x" data-dominant-color="B5B4B7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1629×692 29.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
In other words,how can I get the threeDView node in cpp code?<br>
Any help will be appreciated.</p>

---

## Post #2 by @pieper (2019-09-02 13:54 UTC)

<aside class="quote no-group" data-username="JaceYang" data-post="1" data-topic="8255">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jaceyang/48/3686_2.png" class="avatar"> JaceYang:</div>
<blockquote>
<p>We can get node using Slicer.util.getNode in python console and scripted extensions.But how can I call this function in cpp code?</p>
</blockquote>
</aside>
<p>The python api is mostly just a layer on top f the C++ code so you can do the same things.  Have a look at the python implementation and you can map it to the corresponding C++.</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/util.py#L852">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/util.py#L852" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Base/Python/slicer/util.py#L852" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Base/Python/slicer/util.py#L852</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="842" style="counter-reset: li-counter 841 ;">
          <li>    .. deprecated:: 4.13.0</li>
          <li>      Use the universal :func:`loadMarkups` function instead.</li>
          <li>    """</li>
          <li>    return loadMarkups(filename)</li>
          <li></li>
          <li></li>
          <li>def loadMarkupsClosedCurve(filename):</li>
          <li>    """Load markups closed curve from file.</li>
          <li></li>
          <li>    .. deprecated:: 4.13.0</li>
          <li class="selected">      Use the universal :func:`loadMarkups` function instead.</li>
          <li>    """</li>
          <li>    return loadMarkups(filename)</li>
          <li></li>
          <li></li>
          <li>def loadMarkups(filename):</li>
          <li>    """Load node from file.</li>
          <li></li>
          <li>    :param filename: full path of the file to load.</li>
          <li>    :return: loaded node (if multiple nodes are loaded then a list of nodes).</li>
          <li>    """</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p><a href="https://github.com/Slicer/Slicer/blob/b0443c748cb51904dfd82fa603b4353a335e3364/Libs/MRML/Core/vtkMRMLScene.h#L262" class="onebox" target="_blank" rel="noopener">https://github.com/Slicer/Slicer/blob/b0443c748cb51904dfd82fa603b4353a335e3364/Libs/MRML/Core/vtkMRMLScene.h#L262</a></p>

---
