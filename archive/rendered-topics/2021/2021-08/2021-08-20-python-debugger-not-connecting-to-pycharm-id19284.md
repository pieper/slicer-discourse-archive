# Python debugger not connecting to Pycharm

**Topic ID**: 19284
**Date**: 2021-08-20
**URL**: https://discourse.slicer.org/t/python-debugger-not-connecting-to-pycharm/19284

---

## Post #1 by @fullerkj (2021-08-20 15:14 UTC)

<p><strong>Operating system:</strong> Ubuntu 18.04.5 LTS<br>
<strong>Slicer version:</strong> 4.11.20210226<br>
<strong>PyCharm:</strong> 2021.2 (Professional Edition)<br>
<strong>Expected behavior:</strong> I followed the instructions on <a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/master/README.md" class="inline-onebox" rel="noopener nofollow ugc">SlicerDebuggingTools/README.md at master · SlicerRt/SlicerDebuggingTools · GitHub</a> to set up the debugger in Pycharm to Slicer<br>
<strong>Actual behaviour:</strong> PyCharm debug egg path didn’t automatically load in the path.  Found three different folders containing the same pydevd-pycharm.egg file on my computer.  Tried all three and none of them worked (Restarting Slicer each time).  Any other suggestions for me for why this isn’t working?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e6f7fa35ce2d5431a870ee0ee09ad6719a007be.png" data-download-href="/uploads/short-url/mBAk96Rgh6DLgepeWmXrNjIHI5g.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e6f7fa35ce2d5431a870ee0ee09ad6719a007be_2_690x385.png" alt="image" data-base62-sha1="mBAk96Rgh6DLgepeWmXrNjIHI5g" width="690" height="385" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e6f7fa35ce2d5431a870ee0ee09ad6719a007be_2_690x385.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/e/9e6f7fa35ce2d5431a870ee0ee09ad6719a007be_2_1035x577.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9e6f7fa35ce2d5431a870ee0ee09ad6719a007be.png 2x" data-dominant-color="EEE7E5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1179×658 113 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-09-03 05:48 UTC)

<p>I’ve just tested PyCharm remote debugging on Ubuntu and it works well. See <a href="https://github.com/SlicerRt/SlicerDebuggingTools/blob/master/README.md#connection-refused">these notes</a> on how to fix the <code>Connection refused</code> error.</p>

---
