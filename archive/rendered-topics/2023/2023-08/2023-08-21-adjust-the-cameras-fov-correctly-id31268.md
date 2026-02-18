# Adjust the camera's FOV Correctly

**Topic ID**: 31268
**Date**: 2023-08-21
**URL**: https://discourse.slicer.org/t/adjust-the-cameras-fov-correctly/31268

---

## Post #1 by @slicer365 (2023-08-21 23:39 UTC)

<p>I created a linear transform for the camera,</p>
<p>and when I moved horizontally,</p>
<p>as shown in the picture,</p>
<p>the object suddenly disappeared.</p>
<p>I knew that when the camera was too close to the object,</p>
<p>it would be out of the FOV,</p>
<p>but when I lengthened the distance, the object should be smaller and smaller,</p>
<p>not suddenly disappear.</p>
<p>Friends, can anyone explain it for me?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/8/a8059c783fd5b7ccd9f5c3fc823bdc4c6bb44099.gif" alt="1" data-base62-sha1="nYoeH134X6JPU2rrCRyFNHtCKRb" width="690" height="361" class="animated"></p>

---

## Post #2 by @pieper (2023-08-21 23:41 UTC)

<p>It’s probably the clipping range.</p>
<p>Try something like this:</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/Endoscopy/Endoscopy.py#L331">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/Endoscopy/Endoscopy.py#L331" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/main/Modules/Scripted/Endoscopy/Endoscopy.py#L331" target="_blank" rel="noopener">Slicer/Slicer/blob/main/Modules/Scripted/Endoscopy/Endoscopy.py#L331</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="321" style="counter-reset: li-counter 320 ;">
          <li>        toParent.SetElement(0, 1, yVec[0])</li>
          <li>        toParent.SetElement(1, 1, yVec[1])</li>
          <li>        toParent.SetElement(2, 1, yVec[2])</li>
          <li>        toParent.SetElement(0, 2, zVec[0])</li>
          <li>        toParent.SetElement(1, 2, zVec[1])</li>
          <li>        toParent.SetElement(2, 2, zVec[2])</li>
          <li></li>
          <li>        self.transform.SetMatrixTransformToParent(toParent)</li>
          <li></li>
          <li>        self.cameraNode.EndModify(wasModified)</li>
          <li class="selected">        self.cameraNode.ResetClippingRange()</li>
          <li></li>
          <li></li>
          <li>class EndoscopyComputePath:</li>
          <li>    """Compute path given a list of fiducials.</li>
          <li>    Path is stored in 'path' member variable as a numpy array.</li>
          <li>    If a point list is received then curve points are generated using Hermite spline interpolation.</li>
          <li>    See https://en.wikipedia.org/wiki/Cubic_Hermite_spline</li>
          <li></li>
          <li>    Example:</li>
          <li>      result = EndoscopyComputePath(fiducialListNode)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @slicer365 (2023-08-21 23:46 UTC)

<p>Thank you very much for your real-time reply，Mr Pieper</p>
<p>I will try <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>

---
