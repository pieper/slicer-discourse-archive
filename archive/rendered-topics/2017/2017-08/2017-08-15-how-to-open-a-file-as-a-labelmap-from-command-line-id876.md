---
topic_id: 876
title: "How To Open A File As A Labelmap From Command Line"
date: 2017-08-15
url: https://discourse.slicer.org/t/876
---

# How to open a file as a LabelMap from command line?

**Topic ID**: 876
**Date**: 2017-08-15
**URL**: https://discourse.slicer.org/t/how-to-open-a-file-as-a-labelmap-from-command-line/876

---

## Post #1 by @Valerie_Sydnor (2017-08-15 16:42 UTC)

<p>Operating system: Linux<br>
Slicer version: 4.5.0<br>
Expected behavior: LabelMap file will open as a Volume with “LabelMap” checked in Volume Information, and will appear as Current LabelMapVolume in the display<br>
Actual behavior: LabelMap file opens as a regular volume</p>
<p>Hi,</p>
<p>Is there a way to specify that a given image/file is a LabelMap when opening the image/file with Slicer from the command line? Currently,</p>

---

## Post #2 by @lassoan (2017-08-15 16:51 UTC)

<p>It should work well. What command did you use?</p>

---

## Post #3 by @Fernando (2017-08-15 18:27 UTC)

<p>Have you tried this?<br>
<aside class="onebox githubblob">
  <header class="source">
      <a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L341-L344" target="_blank" rel="nofollow noopener">github.com</a>
  </header>
  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L341-L344" target="_blank" rel="nofollow noopener">Slicer/Slicer/blob/master/Base/Python/slicer/util.py#L341-L344</a></h4>
<pre class="onebox"><code class="lang-py"><ol class="start lines" start="341" style="counter-reset: li-counter 340 ;">
<li>properties = {}</li>
<li>return loadNodeFromFile(filename, filetype, properties, returnNode)</li>
<li>
</li>
<li>def loadModel(filename, returnNode=False):</li>
</ol></code></pre>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
</p>

---

## Post #4 by @fedorov (2017-08-15 18:51 UTC)

<p>Indeed, it does not load as a label map even if I rename the file to include <code>-label</code> prefix.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/fernando">@Fernando</a> the user is asking how to load as label map from the command line (passing the file name as an argument to the Slicer application from command line, I assume), not programmatically.</p>

---

## Post #5 by @lassoan (2017-08-15 19:08 UTC)

<p>This works for me on a recent nightly version:</p>
<pre><code>slicer.util.loadLabelVolume(r'c:\Users\msliv\Documents\test.nrrd')
</code></pre>
<p>Could you test if it works for you, too?</p>

---

## Post #6 by @pieper (2017-08-15 19:14 UTC)

<p>Or to use that from the command line:</p>
<pre><code class="lang-auto">~/Desktop/Slicer.app/Contents/MacOS/Slicer --python-code "slicer.util.loadLabelVolume('/Users/pieper/data/shere.nrrd')"
</code></pre>

---

## Post #7 by @Valerie_Sydnor (2017-08-15 20:02 UTC)

<p>Yes I was looking to load a label map from the command line, passing the file.nrrd as an argument to Slicer as <a class="mention" href="/u/fedorov">@fedorov</a> indicated.<br>
<a class="mention" href="/u/pieper">@pieper</a>’s solution is just what I was looking for! Thanks to all.</p>

---
