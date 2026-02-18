# Autoshrink lung masks in Lung CT Analyzer and Segmenter

**Topic ID**: 16585
**Date**: 2021-03-16
**URL**: https://discourse.slicer.org/t/autoshrink-lung-masks-in-lung-ct-analyzer-and-segmenter/16585

---

## Post #1 by @rbumm (2021-03-16 19:11 UTC)

<p>Hi all,</p>
<p>By default, lung masks produced by ‘Lung CT Segmenter’ may include pleura, pericardium, and diaphragm at the borderlines. These areas may be wrongly segmented as ‘infiltrated’ or ‘collapsed’ lung parenchyma by ‘Lung CT Analyzer’.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06f0797736c2df3df7c933078ce58b8a0f77ebbc.jpeg" data-download-href="/uploads/short-url/Zo4TIgSDQP2unkHZAX5VknX0IY.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06f0797736c2df3df7c933078ce58b8a0f77ebbc_2_403x500.jpeg" alt="image" data-base62-sha1="Zo4TIgSDQP2unkHZAX5VknX0IY" width="403" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/06f0797736c2df3df7c933078ce58b8a0f77ebbc_2_403x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06f0797736c2df3df7c933078ce58b8a0f77ebbc.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06f0797736c2df3df7c933078ce58b8a0f77ebbc.jpeg 2x" data-dominant-color="5B646D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">557×690 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>A new ‘Lung CT Segmenter’ option now enables shrinking the lung masks by a small constant amount (1 mm).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b7e985e09f1f4d82a7e9c189a172b8af5609eada.png" alt="image" data-base62-sha1="qeXHg36tLnmhY4jqDHYvO1MzCae" width="204" height="95"></p>
<p>Alternatively, the shrinking of the lung masks with variable shrink volumes can be realized by a script call of the newly implemented Lung CT Analyzer logic   ‘shrinkLungMasks’.</p>
<p>Python script example:</p>
<pre><code>import LungCTAnalyzer
from LungCTAnalyzer import LungCTAnalyzerLogic

# switch to module 
slicer.util.selectModule('LungCTAnalyzer')

logic = LungCTAnalyzerLogic()

logic.inputVolume = loadedVolumeNode # you must have loded that before
logic.inputSegmentation = loadedMaskNode  # you must have loded that before
logic.rightLungMaskSegmentID =loadedMaskNode.GetSegmentation().GetSegmentIdBySegmentName("right lung")
logic.leftLungMaskSegmentID =loadedMaskNode.GetSegmentation().GetSegmentIdBySegmentName("left lung")

# shrink masks
val = 1.0
logic.shrinkLungMasks(val)
# do processing with current slider settings
logic.process() 
.
.
</code></pre>
<p>where ‘val’ is a value in millimeters.</p>
<p>The described functionality is available in ‘Lung CT Analyzer’ V 2.36.</p>
<p>Result after mask shrinking (data set part of COVID-19 Open Source project <a href="https://discourse.slicer.org/u/PaoloZaffino">PaoloZaffino</a>):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a6e82c22eb100896fc982e1752e0cd2c1286835.jpeg" data-download-href="/uploads/short-url/1uhxF5X0uPbOSxftKs95Q53ZVhb.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a6e82c22eb100896fc982e1752e0cd2c1286835_2_457x500.jpeg" alt="image" data-base62-sha1="1uhxF5X0uPbOSxftKs95Q53ZVhb" width="457" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a6e82c22eb100896fc982e1752e0cd2c1286835_2_457x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0a6e82c22eb100896fc982e1752e0cd2c1286835_2_685x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/a/0a6e82c22eb100896fc982e1752e0cd2c1286835.jpeg 2x" data-dominant-color="52575D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">711×777 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Best regards<br>
rudolf</p>

---
