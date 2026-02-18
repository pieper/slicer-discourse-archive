# what thing do I miss to create volume sequence from tiff

**Topic ID**: 20039
**Date**: 2021-10-06
**URL**: https://discourse.slicer.org/t/what-thing-do-i-miss-to-create-volume-sequence-from-tiff/20039

---

## Post #1 by @BingYen (2021-10-06 19:00 UTC)

<p>Hi,<br>
I’m new to Slicer and Python<br>
I want to load 512x512x619x9 uint16 data from microscopy into Slicer as volume sequence data.</p>
<p>First, I save ome.tiff as nrrd (<em>C2withmeta.nrrd</em>) via Fiji after I checked the properties.<br>
I tried load it in slicer but it became 512x512x5571.<br>
Then I used python to edit and save nrrd data via CMD.<br>
(Python 3.8.11 (default, Aug  3 2021, 06:49:12) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32)</p>
<p><a href="https://discourse.slicer.org/t/hdf5-to-nrrd-to-seq-nrrd/18277/4">From this post, I tried to add some header for .seq.nrdd and reshape to make frame as first dimension.</a></p>
<p>Here are the code</p>
<pre><code class="lang-auto">import numpy as np
import nrrd
import os
filename = "~/Desktop/C2nrrd/C2withmeta.nrrd"
filedata, fileheader = nrrd.read(filename)
filedata.shape
(512, 512, 5571)
newdata = filedata.reshape(619,512,512,9)
newheader = {
    'type': 'uint16',
    'encoding': 'raw',
    'endian': 'big',
    'dimension': 4,
    'sizes': [619, 512, 512,9],
    'kinds': ['list', 'domain', 'domain', 'domain'],
    'labels': ['frame', '', '', ''],
    'space': 'right-anterior-superior',
    'space dimension': 3, 
    'space directions': [[0.184687, 0. , 0.  ], [0.   , 0.184687, 0.   ],   [0.   , 0.    , 3.75    ]],
    'space origin': [ 0, 0, 0],
    'space units': ['s','microns', 'microns', 'microns'],
    'measurement frame': [[1., 0., 0.], [0., 1., 0.], [0., 0., 1.]],
    'axis 0 index type': 'numeric',
    'axis 0 index values': tuple(range(0,619))
    }
outname = "~Desktop/C2nrrd/C2new2.nrrd" 
nrrd.write (outname, newdata, newheader)
</code></pre>
<p>I tried save .nrrd or .seq.nrrd and tried load them in slicer as volum or sequence, but all failed.<br>
when I load it as sequence, error</p>
<blockquote>
<p>Error: Loading ~/Desktop/C2nrrd/C2new.seq.nrrd - Failed to read node C2new_1 (vtkMRMLSequenceNode2) from filename=‘~/Desktop/C2nrrd/C2new.seq.nrrd’</p>
</blockquote>
<p>when I load it as volume</p>
<blockquote>
<p>Error: Loading ~/Desktop/C2nrrd/C2new.seq.nrrd -  load failed.</p>
</blockquote>
<p>So I want to know what is the problem?</p>

---

## Post #2 by @lassoan (2021-10-07 05:20 UTC)

<p>There are a number of differences between your header fields and the working example looked. Do not add any extra fields (<code>space dimension</code>, <code>sizes</code>, …) and specify <code>space directions</code>, and <code>set axis 0 index vales</code> as a space separated list.</p>
<p>I would recommend to first start with a small volume, for example 62x512x512x9 (it can be a small patch that you cut from the full volume). If it fails then upload the .seq.nrrd file somewhere and I’ll take a look.</p>

---

## Post #3 by @BingYen (2021-10-07 17:22 UTC)

<p>Thank your reply, lassoan.</p>
<p>In this <a href="https://github.com/SlicerRt/Sequences/issues/31" rel="noopener nofollow ugc">post</a>, there is <code>size</code> field and the <code>space directions</code> looks like it is a 4D list.</p>
<p>So I don’t understand this</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="20039">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do not add any extra fields ( <code>space dimension</code> , <code>sizes</code> , …) and specify <code>space directions</code> , and <code>set axis 0 index vales</code> as a space separated list.</p>
</blockquote>
</aside>
<ol>
<li>
<p>Where should I put <code>size</code> info in my data?</p>
</li>
<li>
<p>What should <code>space directions</code> look like?<br>
<code>[[nan,nan,nan], [0.184687, 0. , 0.  ], [0.   , 0.184687, 0.   ],   [0.   , 0.    , 3.75    ]</code>  ?<br>
or<br>
<code>[nan], [0.184687, 0. , 0.  ], [0.   , 0.184687, 0.   ],   [0.   , 0.    , 3.75    ]</code> ?</p>
</li>
</ol>

---

## Post #4 by @lassoan (2021-10-07 17:56 UTC)

<aside class="quote no-group" data-username="BingYen" data-post="3" data-topic="20039">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bingyen/48/8904_2.png" class="avatar"> BingYen:</div>
<blockquote>
<ul>
<li>Where should I put <code>size</code> info in my data?</li>
</ul>
</blockquote>
</aside>
<p>Nowhere. Size is defined by your numpy array.</p>
<aside class="quote no-group" data-username="BingYen" data-post="3" data-topic="20039">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/bingyen/48/8904_2.png" class="avatar"> BingYen:</div>
<blockquote>
<p>What should <code>space directions</code> look like?</p>
</blockquote>
</aside>
<p>It should be the same as <a href="https://discourse.slicer.org/t/hdf5-to-nrrd-to-seq-nrrd/18277/4">the working example</a> - with three <code>float('nan')</code> values.</p>

---

## Post #5 by @BingYen (2021-10-08 06:32 UTC)

<p>Thank you for reply, lassoan</p>
<p>I found the problem also come from units,<br>
it doesn’t accept others except time,<br>
so I successfully load it in using <code>'units': "s", "","",""</code></p>

---

## Post #6 by @lassoan (2021-10-09 19:49 UTC)

<p>Yes, you need to follow the nrrd standard - see details here: <a href="http://teem.sourceforge.net/nrrd/format.html">http://teem.sourceforge.net/nrrd/format.html</a></p>
<p>Could you post your final, working code snippet for future reference?</p>

---
