# Volumes module Histogram responsiveness

**Topic ID**: 15072
**Date**: 2020-12-15
**URL**: https://discourse.slicer.org/t/volumes-module-histogram-responsiveness/15072

---

## Post #1 by @giovform (2020-12-15 13:34 UTC)

<p>Hi, are there any plans to improve the Histogram responsiveness from Volumes module? I have a rather large volume, with dimensions 923x932x1771 and the Histogram is just too slow to be usable in this case. I am using nightly 13.0-2020-12-13 r29523.</p>
<p>Edit:</p>
<p>I subsampled the volume down to 923x932x50, and it is still very slow to update when changing the threshold sliders.</p>

---

## Post #2 by @lassoan (2020-12-15 22:22 UTC)

<p>Histogram in Volumes module is just an illustration. How do you use it?</p>
<p>How long does it take to compute it?<br>
How often does the volume change?<br>
How much physical RAM do you have?<br>
What is the scalar type of the volume?</p>

---

## Post #3 by @pieper (2020-12-15 22:33 UTC)

<p>You can get a good approximate histogram with a small sample, like 1%.  We should probably do this if the volume is large.</p>

---

## Post #4 by @lassoan (2020-12-15 23:42 UTC)

<aside class="quote no-group" data-username="giovform" data-post="1" data-topic="15072">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/giovform/48/4687_2.png" class="avatar"> giovform:</div>
<blockquote>
<p>it is still very slow to update when changing the threshold sliders</p>
</blockquote>
</aside>
<p>It is not necessary to recomputed the histogram when the window/level slider is moved. Maybe it is unnecessarily recomputed we just did not notice it (because usually it is very fast), but maybe it is slow because of slice view or volume rendering updates. How do you know that it is slow due to the histogram computation?</p>

---

## Post #5 by @giovform (2020-12-16 15:55 UTC)

<p>Hello Andras and Pieper, thanks for your reply.</p>
<p>These are my system specs:</p>
<pre><code>Microsoft Windows 10 Pro
Processor AMD Ryzen 7 2700 Eight-Core Processor, 3200 Mhz
RAM 32 GB
GPU NVIDIA GeForce GTX 1660
SSD ADATA SU630
</code></pre>
<blockquote>
<p>How do you know that it is slow due to the histogram computation?</p>
</blockquote>
<p>Because when I close the Histogram collapsible button, the sliding action of the Threshold flows much smoother.</p>
<p>Testing with the sample data “MRHead” (256x256x130), the Threshold sliding response (and Histogram observed region update) is fast, but when testing with the sample data “CTA Abdomen” (441x321x215), the response already becomes poor (while the Histogram is being shown).</p>
<blockquote>
<p>You can get a good approximate histogram with a small sample, like 1%. We should probably do this if the volume is large.</p>
</blockquote>
<p>The volumes I work with are large (900x900x1700 for example). Maybe it would be nice to allow the user to set this sample percentage.</p>

---

## Post #6 by @lassoan (2020-12-17 06:46 UTC)

<p>Thanks for the additional information. I’ve checked the code and indeed <a href="https://github.com/Slicer/Slicer/blob/18a400f3c0508b0e7da5d7488f9350262f3c8c49/Modules/Loadable/Volumes/Widgets/qSlicerScalarVolumeDisplayWidget.cxx#L255-L276"><code>qSlicerScalarVolumeDisplayWidget::updateHistogram()</code></a> is called each time the display node is changed (e.g., you change window/level). This is of course unnecessary and may cause significant slowdown for huge volumes.</p>
<p>To fix this, a check could be added and skip building of the histogram if input image data pointer and modified time (MTime) did not change since the last build. For this, last used image pointer and modified time has to be saved in member variables.</p>
<p>It would be great if you could fix this and send a pull request. Should be just 10-20 lines of code in total.</p>

---

## Post #7 by @giovform (2020-12-17 18:03 UTC)

<p>Right now I was only programming in Python. I’ll find some time to setup everything for C++ and report back here about the development. Thank you <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"></p>

---

## Post #8 by @giovform (2020-12-21 14:56 UTC)

<p>One question: how the updateHistogram function is called when the window/level slider (or threshold slider) is changed (where in the code the connection is made)?</p>
<p>Edit: is this the answer?</p>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/43300c7b9a3b27265c2bc736693cb881f05e3ea9/Modules/Loadable/Volumes/Widgets/qSlicerScalarVolumeDisplayWidget.cxx#L185-L187" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/43300c7b9a3b27265c2bc736693cb881f05e3ea9/Modules/Loadable/Volumes/Widgets/qSlicerScalarVolumeDisplayWidget.cxx#L185-L187" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/43300c7b9a3b27265c2bc736693cb881f05e3ea9/Modules/Loadable/Volumes/Widgets/qSlicerScalarVolumeDisplayWidget.cxx#L185-L187</a></h4>
<pre class="onebox"><code class="lang-cxx"><ol class="start lines" start="185" style="counter-reset: li-counter 184 ;">
<li>qvtkReconnect(oldVolumeDisplayNode, volumeNode ? volumeNode-&gt;GetDisplayNode() :nullptr,</li><li>              vtkCommand::ModifiedEvent,</li><li>              this, SLOT(updateWidgetFromMRML()));</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---

## Post #9 by @pieper (2020-12-21 15:10 UTC)

<p>That looks like the right place, yes.</p>

---
