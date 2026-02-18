# ExtensionWizard hangs

**Topic ID**: 372
**Date**: 2017-05-24
**URL**: https://discourse.slicer.org/t/extensionwizard-hangs/372

---

## Post #1 by @tdiprima (2017-05-24 14:14 UTC)

<p><strong>Operating system:</strong> Windows 10 and Ubuntu 16<br>
<strong>Slicer version:</strong> 4 (Nightly build – for the past few weeks or so)<br>
<strong>Expected behavior:</strong> ExtensionWizard displays the extensions you can install<br>
Actual behavior: <strong>ExtensionWizard hangs for quite a long time upon startup, with no log output to indicate anything wrong)</strong></p>

---

## Post #2 by @tdiprima (2017-05-24 14:16 UTC)

<p>Screenshot:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e34846bbd1e55dadcb9e6fdc48586954d785161a.png" data-download-href="/uploads/short-url/wqDeHfvT1l6xOTFBctSPMknCUZQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e34846bbd1e55dadcb9e6fdc48586954d785161a_2_690x387.png" alt="image" data-base62-sha1="wqDeHfvT1l6xOTFBctSPMknCUZQ" width="690" height="387" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e34846bbd1e55dadcb9e6fdc48586954d785161a_2_690x387.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e34846bbd1e55dadcb9e6fdc48586954d785161a_2_1035x580.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e34846bbd1e55dadcb9e6fdc48586954d785161a.png 2x" data-dominant-color="F7F8F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1092×614 29.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @jcfr (2017-05-24 14:31 UTC)

<p>Thanks for the feedback. Will have a look shortly and keep you posted.</p>
<p>Look like the associated server is slow, any of these urls are slow to complete:</p>
<ul>
<li><a href="http://slicer.kitware.com/midas3/slicerappstore">http://slicer.kitware.com/midas3/slicerappstore</a></li>
<li><a href="http://slicer.kitware.com/midas3/slicerappstore?os=linux&amp;arch=amd64&amp;revision=26032&amp;category=&amp;search=&amp;layout=layout">http://slicer.kitware.com/midas3/slicerappstore?os=linux&amp;arch=amd64&amp;revision=26032&amp;category=&amp;search=&amp;layout=layout</a></li>
<li><a href="http://slicer.kitware.com/midas3/slicerappstore?os=linux&amp;arch=amd64&amp;revision=26032&amp;category=&amp;search=&amp;layout=empty">http://slicer.kitware.com/midas3/slicerappstore?os=linux&amp;arch=amd64&amp;revision=26032&amp;category=&amp;search=&amp;layout=empty</a></li>
</ul>
<p>This is do to a recent “feature” extracting the current nightly revision. See <a href="https://github.com/midasplatform/slicerappstore/commit/a61ea1989b9c0267e19236a8c10a01f273ee85fd">https://github.com/midasplatform/slicerappstore/commit/a61ea1989b9c0267e19236a8c10a01f273ee85fd</a></p>

---
