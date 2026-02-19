---
topic_id: 1968
title: "Rotate 3D Image"
date: 2018-01-29
url: https://discourse.slicer.org/t/1968
---

# Rotate 3D image

**Topic ID**: 1968
**Date**: 2018-01-29
**URL**: https://discourse.slicer.org/t/rotate-3d-image/1968

---

## Post #1 by @Ahmed_Soufane (2018-01-29 19:05 UTC)

<p>How to  rotate the 3D image using phython interactor  ?</p>

---

## Post #2 by @cpinter (2018-01-29 19:50 UTC)

<p>This is one way<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/33d2c132595e7379119a0ff1d9f453aac70e4f76/Applications/SlicerApp/Testing/Python/RSNAVisTutorial.py#L341-L342" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/33d2c132595e7379119a0ff1d9f453aac70e4f76/Applications/SlicerApp/Testing/Python/RSNAVisTutorial.py#L341-L342" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/33d2c132595e7379119a0ff1d9f453aac70e4f76/Applications/SlicerApp/Testing/Python/RSNAVisTutorial.py#L341-L342</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="341" style="counter-reset: li-counter 340 ;">
<li>threeDView = layoutManager.threeDWidget(0).threeDView()</li>
<li>slicer.util.clickAndDrag(threeDView)</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #3 by @lassoan (2018-01-29 20:16 UTC)

<p>See also how ScreenCapture module rotates a 3D view:</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/5d294412119bf51f14c3a19ec98f055c1cbe30fe/Modules/Scripted/ScreenCapture/ScreenCapture.py#L943-L1002" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/5d294412119bf51f14c3a19ec98f055c1cbe30fe/Modules/Scripted/ScreenCapture/ScreenCapture.py#L943-L1002" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/5d294412119bf51f14c3a19ec98f055c1cbe30fe/Modules/Scripted/ScreenCapture/ScreenCapture.py#L943-L1002</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="943" style="counter-reset: li-counter 942 ;">
<li>def capture3dViewRotation(self, viewNode, startRotation, endRotation, numberOfImages, rotationAxis,</li>
<li>  outputDir, outputFilenamePattern, captureAllViews = None):</li>
<li>  """</li>
<li>  Acquire a set of screenshots of the 3D view while rotating it.</li>
<li>  """</li>
<li>
</li>
<li>  self.cancelRequested = False</li>
<li>
</li>
<li>  if not os.path.exists(outputDir):</li>
<li>    os.makedirs(outputDir)</li>
<li>  filePathPattern = os.path.join(outputDir, outputFilenamePattern)</li>
<li>
</li>
<li>  renderView = self.viewFromNode(viewNode)</li>
<li>
</li>
<li>  # Save original orientation and go to start orientation</li>
<li>  originalPitchRollYawIncrement = renderView.pitchRollYawIncrement</li>
<li>  originalDirection = renderView.pitchDirection</li>
<li>  renderView.setPitchRollYawIncrement(-startRotation)</li>
<li>  if rotationAxis == AXIS_YAW:</li>
<li>    renderView.yawDirection = renderView.YawRight</li>
</ol></code></pre>

  This file has been truncated. <a href="https://github.com/Slicer/Slicer/blob/5d294412119bf51f14c3a19ec98f055c1cbe30fe/Modules/Scripted/ScreenCapture/ScreenCapture.py#L943-L1002" target="_blank" rel="nofollow noopener">show original</a>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #4 by @Ahmed_Soufane (2018-03-06 02:42 UTC)

<p>Thanks a lot for giving me the code for controlling the rotation of the 3D image. I am using MAC operating software, and the 3D slicer version I am using is is 4.8.0. The code you gave me rotates the image really slowly, as I was trying to define like this  threeDView = layoutManager.threeDWidget(10).threeDView(), in order to allow more rotation to occur when running this on python interactor.  The problem is the moment I execute this on python interactor, in return slicer software force quits itself immediately. Whenever I try to put any number instead of 0 in threeDWidget(number), slicer software quits unexpectedly. I was trying to manipulate the rotation from different axes as this command only allows me to control the image from I to S axes, which means in one direction. I want to know how can I rotate in all directions for the 3D image via python interactor without quitting slicer application unexpectedly. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/9/1942176317d218c1be59b3e8bc8c3c2623f51347.png" data-download-href="/uploads/short-url/3BrxhBvYRZgPZRqAxBLhmzvJZ8X.png?dl=1" title="27%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/1942176317d218c1be59b3e8bc8c3c2623f51347_2_690x67.png" alt="27%20PM" data-base62-sha1="3BrxhBvYRZgPZRqAxBLhmzvJZ8X" width="690" height="67" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/1942176317d218c1be59b3e8bc8c3c2623f51347_2_690x67.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/1942176317d218c1be59b3e8bc8c3c2623f51347_2_1035x100.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/9/1942176317d218c1be59b3e8bc8c3c2623f51347_2_1380x134.png 2x" data-dominant-color="E4E3E1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">27%20PM</span><span class="informations">1570×154 15.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2018-03-06 03:59 UTC)

<aside class="quote no-group" data-username="Ahmed_Soufane" data-post="4" data-topic="1968">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b38774/48.png" class="avatar"> Ahmed_Soufane:</div>
<blockquote>
<p>Thanks a lot for giving me the code for controlling the rotation of the 3D image.</p>
</blockquote>
</aside>
<p>The code does not rotate the 3D image. Do you need to rotate the volume? Then you can apply a transform to the volume and adjust that using sliders.</p>
<aside class="quote no-group" data-username="Ahmed_Soufane" data-post="4" data-topic="1968">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b38774/48.png" class="avatar"> Ahmed_Soufane:</div>
<blockquote>
<p>I am using MAC operating software, and the 3D slicer version I am using is is 4.8.0.</p>
</blockquote>
</aside>
<p>Use 4.8.1. It contains many fixes and improvements.</p>
<aside class="quote no-group" data-username="Ahmed_Soufane" data-post="4" data-topic="1968">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b38774/48.png" class="avatar"> Ahmed_Soufane:</div>
<blockquote>
<p>The code you gave me rotates the image really slowly, as I was trying to define like this  threeDView = layoutManager.threeDWidget(10).threeDView()</p>
</blockquote>
</aside>
<p>As you have probably only one or two 3D viewers (you can get number of 3D widgets from layoutManager), calling <code>layoutManager.threeDWidget(10)</code> is expected to crash your application.</p>
<aside class="quote no-group" data-username="Ahmed_Soufane" data-post="4" data-topic="1968">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b38774/48.png" class="avatar"> Ahmed_Soufane:</div>
<blockquote>
<p>Whenever I try to put any number instead of 0 in threeDWidget(number), slicer software quits unexpectedly.</p>
</blockquote>
</aside>
<p>This is the correct, expected behavior. See above.</p>
<aside class="quote no-group" data-username="Ahmed_Soufane" data-post="4" data-topic="1968">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b38774/48.png" class="avatar"> Ahmed_Soufane:</div>
<blockquote>
<p>I was trying to manipulate the rotation from different axes as this command only allows me to control the image from I to S axes</p>
</blockquote>
</aside>
<p>What command?</p>
<aside class="quote no-group" data-username="Ahmed_Soufane" data-post="4" data-topic="1968">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b38774/48.png" class="avatar"> Ahmed_Soufane:</div>
<blockquote>
<p>I want to know how can I rotate in all directions for the 3D image via python interactor without quitting slicer application unexpectedly.</p>
</blockquote>
</aside>
<p>If you simply want to rotate a 3D view (not the 3D image), then follow what is done in <a href="https://github.com/Slicer/Slicer/blob/f4a792d66b910edc54060566573d13264f3951fc/Modules/Scripted/ScreenCapture/ScreenCapture.py#L968-L983">Screen Capture module</a>.</p>

---

## Post #6 by @Ahmed_Soufane (2018-03-06 23:12 UTC)

<p>I tried the code “Screen Capture module”, but I got the following:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d8651606b5d9fc610fe4119e77df77a798aea23.png" data-download-href="/uploads/short-url/hUrsqASTgxetsCJdgP72kXpHDnt.png?dl=1" title="04%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d8651606b5d9fc610fe4119e77df77a798aea23.png" alt="04%20PM" data-base62-sha1="hUrsqASTgxetsCJdgP72kXpHDnt" width="690" height="197" data-dominant-color="F1DFE7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">04%20PM</span><span class="informations">760×218 29.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
There are lots of parameters that has been not defined, and I do not know where to get them from or define them as the given code fragment discusses several implementations.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28a01c1e2a66cdd493f49286ecf08e678968704e.png" data-download-href="/uploads/short-url/5No8dyhOQUQeg0ssz51TAjdbxSu.png?dl=1" title="23%20PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/8/28a01c1e2a66cdd493f49286ecf08e678968704e.png" alt="23%20PM" data-base62-sha1="5No8dyhOQUQeg0ssz51TAjdbxSu" width="690" height="90" data-dominant-color="F6DADF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">23%20PM</span><span class="informations">732×96 14.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Would you please help me with that…<br>
Thanks</p>

---

## Post #7 by @Ahmed_Soufane (2018-03-06 23:19 UTC)

<p>Almost all the parameters in the given code are not defined, would you please guide me or tell me how to define them in order to rotate the 3D view.<br>
Thank you</p>

---

## Post #8 by @pieper (2018-03-07 00:22 UTC)

<p>Hi Ahmed -</p>
<p>You can’t just cut and paste the module code into the python console.  Instead you will need to read through it and set the needed variables and perhaps adapt the code a bit.  It takes a little thought and experience with python, but it really won’t be too difficult if you practice.</p>
<p>Probably first you want to get comfortable with python as a language, perhaps by doing some online tutorials (like <a href="https://www.codecademy.com/">CodeAcademy</a>) and look at <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting">how python is used in Slicer</a>.</p>
<p>Best,<br>
Steve</p>

---

## Post #9 by @Ahmed_Soufane (2018-03-12 11:51 UTC)

<p>Dear Pieper,<br>
I looked up the links you provided and tried to define the required parameters many times, but I always get many errors as if I am defining the parameters in a wrong way. Would you please help me with this as I am running out of time for the project I am working on, I would really appreciate it if you can help me with this.</p>
<p>Thank you.</p>

---

## Post #10 by @pieper (2018-03-12 14:51 UTC)

<p>You can paste the following into the python console:</p>
<pre><code class="lang-auto">layoutManager = slicer.app.layoutManager()
threeDWidget = layoutManager.threeDWidget(0)
threeDView = threeDWidget.threeDView()
threeDView.yaw()
</code></pre>
<p>The last line does the actual rotation.  To do more sophisticated animation you’ll need to refer to the other code Andras, Csaba and I pointed to.</p>
<p>I added this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_the_3D_View">to the script repository</a> for future reference.</p>

---

## Post #11 by @Ahmed_Soufane (2018-03-12 15:36 UTC)

<p>This way only rotates along one axes, can I use it to rotate along a different axes ?</p>

---

## Post #12 by @pieper (2018-03-12 15:51 UTC)

<p>You can either use the methods on the threeDView:</p>
<p><a href="http://www.commontk.org/docs/html/classctkVTKRenderView.html" class="onebox" target="_blank">http://www.commontk.org/docs/html/classctkVTKRenderView.html</a></p>
<p>Or you can get the active camera from the vtkRenderer (which you can get from the threeDView):</p>
<p><a href="https://www.vtk.org/doc/nightly/html/classvtkRenderer.html" class="onebox" target="_blank">https://www.vtk.org/doc/nightly/html/classvtkRenderer.html</a></p>

---
