# Slicer VMTK LevelSetSegmentation no Start

**Topic ID**: 18184
**Date**: 2021-06-17
**URL**: https://discourse.slicer.org/t/slicer-vmtk-levelsetsegmentation-no-start/18184

---

## Post #1 by @Elias_Karabelas (2021-06-17 12:37 UTC)

<p>Hi all,<br>
so filling out the basics:</p>
<p>Operating system: Ubuntu 20.04<br>
Slicer version: 4.11.20210226</p>
<p>Expected behavior: Generating a LevelSetSegmentation of a bunch of coronaries.</p>
<p>Actual behavior: So I was able to install the VMTK Extension and also able to create a vesselness. However when I start to use the LevelSetSegmentation I can put seeds and stoppers and hit preview but then I cannot click on the Start button. Did I forget to do anything beforehand?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d1d77ca74af02c4d3025e274e0d1f619be1a7b2.png" data-download-href="/uploads/short-url/hQOOKy5NL7NRUZpATvfz2KyAapY.png?dl=1" title="Bildschirmfoto vom 2021-06-17 08-28-17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d1d77ca74af02c4d3025e274e0d1f619be1a7b2_2_690x287.png" alt="Bildschirmfoto vom 2021-06-17 08-28-17" data-base62-sha1="hQOOKy5NL7NRUZpATvfz2KyAapY" width="690" height="287" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d1d77ca74af02c4d3025e274e0d1f619be1a7b2_2_690x287.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d1d77ca74af02c4d3025e274e0d1f619be1a7b2_2_1035x430.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7d1d77ca74af02c4d3025e274e0d1f619be1a7b2_2_1380x574.png 2x" data-dominant-color="828287"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Bildschirmfoto vom 2021-06-17 08-28-17</span><span class="informations">3840×1600 1.11 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-06-17 13:40 UTC)

<p>After Preview is completed, Start button should become available. Do you see an error in the Python console?</p>

---

## Post #3 by @Elias_Karabelas (2021-06-17 15:25 UTC)

<p>That’s the output of the python console:</p>
<p>Loading with imageIOName: GDCM<br>
Traceback (most recent call last):<br>
File “/home/karabele/software/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/LevelSetSegmentation.py”, line 288, in onPreviewButtonClicked<br>
self.start(True)<br>
File “/home/karabele/software/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/LevelSetSegmentation.py”, line 583, in start<br>
for n in xrange(numberOfSliceNodes):<br>
NameError: name ‘xrange’ is not defined<br>
Traceback (most recent call last):<br>
File “/home/karabele/software/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/LevelSetSegmentation.py”, line 288, in onPreviewButtonClicked<br>
self.start(True)<br>
File “/home/karabele/software/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/LevelSetSegmentation.py”, line 583, in start<br>
for n in xrange(numberOfSliceNodes):<br>
NameError: name ‘xrange’ is not defined<br>
Traceback (most recent call last):<br>
File “/home/karabele/software/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/LevelSetSegmentation.py”, line 288, in onPreviewButtonClicked<br>
self.start(True)<br>
File “/home/karabele/software/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/LevelSetSegmentation.py”, line 583, in start<br>
for n in xrange(numberOfSliceNodes):<br>
NameError: name ‘xrange’ is not defined<br>
Traceback (most recent call last):<br>
File “/home/karabele/software/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/LevelSetSegmentation.py”, line 288, in onPreviewButtonClicked<br>
self.start(True)<br>
File “/home/karabele/software/Slicer-4.11.20210226-linux-amd64/NA-MIC/Extensions-29738/SlicerVMTK/lib/Slicer-4.11/qt-scripted-modules/LevelSetSegmentation.py”, line 583, in start<br>
for n in xrange(numberOfSliceNodes):<br>
NameError: name ‘xrange’ is not defined</p>

---

## Post #4 by @Elias_Karabelas (2021-06-17 15:26 UTC)

<p>seems to be that LevelSetSegmentation uses Python2 instead of Python3</p>

---

## Post #5 by @lassoan (2021-06-17 15:54 UTC)

<p>Yes, probably there are a few similar Python2/3 incompatibilites. It would be great if you could fix them and send a pull request to the <a href="https://github.com/vmtk/SlicerExtension-VMTK/">SlicerVMTK extension</a>. Thank you!</p>

---

## Post #6 by @Elias_Karabelas (2021-06-18 07:39 UTC)

<p>Hi Andras,<br>
so fixing the xrange makes the module work. However documentation on the levelsetsegmentation is a bit sparse. According to github of SlicerVMTK I should be able to segment a coronary artery tree. But I’m not quite sure how. I tried to add a few diameter seeds and also stoppers and thought I might add a stopper at each end of the tree, however this will always segment just one part of the coronary tree.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/704d375d47dbf3d1b6a72c3471cc1125b3739d58.jpeg" data-download-href="/uploads/short-url/g1sUwSBpgX64oaCXsjS2LYrBzRK.jpeg?dl=1" title="SlicerScreenshot.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/704d375d47dbf3d1b6a72c3471cc1125b3739d58_2_517x217.jpeg" alt="SlicerScreenshot.PNG" data-base62-sha1="g1sUwSBpgX64oaCXsjS2LYrBzRK" width="517" height="217" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/704d375d47dbf3d1b6a72c3471cc1125b3739d58_2_517x217.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/704d375d47dbf3d1b6a72c3471cc1125b3739d58_2_775x325.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/704d375d47dbf3d1b6a72c3471cc1125b3739d58_2_1034x434.jpeg 2x" data-dominant-color="88858B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">SlicerScreenshot.PNG</span><span class="informations">1920×807 317 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I added a Screenshot showing my progress so far.</p>

---

## Post #7 by @lassoan (2021-06-18 21:23 UTC)

<p>It can only segment one curve at a time, not a complete tree. You could change the code so that it can take multiple input points and extract multiple curves.</p>
<aside class="quote no-group" data-username="Elias_Karabelas" data-post="6" data-topic="18184">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/elias_karabelas/48/11286_2.png" class="avatar"> Elias_Karabelas:</div>
<blockquote>
<p>so fixing the xrange makes the module work</p>
</blockquote>
</aside>
<p>Great! Please <a href="https://github.com/vmtk/SlicerExtension-VMTK/pulls">send a pull request</a> with your changes.</p>

---

## Post #8 by @ricslator (2022-09-12 06:32 UTC)

<aside class="quote no-group" data-username="Elias_Karabelas" data-post="3" data-topic="18184">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/elias_karabelas/48/11286_2.png" class="avatar"> Elias_Karabelas:</div>
<blockquote>
<p>NameError: name ‘xrange’ is not defined</p>
</blockquote>
</aside>
<p>You’re probably using Python3, where xrange has become range.</p>
<p>The error message ‘xrange’ is not defined would seem to indicate that you are trying to run a Python 2 codebase with Python 3 . In Python 2, an iterable object is often created with xrange() method , usually in a “for loop”, which behaves very similarly to a generator. In Python 3, range() method is implemented the same as the <a href="http://net-informations.com/python/pro/xrange.htm" rel="noopener nofollow ugc">xrange</a>() method , so there is no dedicated xrange(). So, if you use xrange() in Python 3, it will generate NameError:name ‘xrange’ is not defined error.</p>

---
