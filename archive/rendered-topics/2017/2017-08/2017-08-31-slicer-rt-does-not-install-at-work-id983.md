# Slicer RT does not install at work

**Topic ID**: 983
**Date**: 2017-08-31
**URL**: https://discourse.slicer.org/t/slicer-rt-does-not-install-at-work/983

---

## Post #1 by @aliocha12 (2017-08-31 21:26 UTC)

<p>I use slicer RT to convert dicom to stl for 3d printing bolus. It works fine at home, but I cannot get slicer RT to install at work. Slicer 3D installs fine. Is there a way of downloading the module at home, then importing manually at work from a flash drive? OS: win 64bit.<br>
Thank you.</p>
<p>Alex</p>

---

## Post #2 by @jcfr (2017-08-31 21:51 UTC)

<aside class="quote no-group" data-username="aliocha12" data-post="1" data-topic="983">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b5e925/48.png" class="avatar"> aliocha12:</div>
<blockquote>
<p>cannot get slicer RT to install at work.</p>
</blockquote>
</aside>
<p>If possible, could you share the log (Menu Help → Report a Bug) ? So that we can understand why the download fails from your office.</p>
<aside class="quote no-group" data-username="aliocha12" data-post="1" data-topic="983">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/a/b5e925/48.png" class="avatar"> aliocha12:</div>
<blockquote>
<p>Is there a way of downloading the module at home, then importing manually at work from a flash drive?</p>
</blockquote>
</aside>
<p>Yes. You could download the extension archive from:</p>
<p><a href="http://slicer.kitware.com/midas3/slicerappstore?os=win&amp;arch=amd64&amp;revision=26325&amp;category=&amp;search=slicerrt&amp;layout=layout" class="onebox" target="_blank" rel="noopener">http://slicer.kitware.com/midas3/slicerappstore?os=win&amp;arch=amd64&amp;revision=26325&amp;category=&amp;search=slicerrt&amp;layout=layout</a></p>
<p>Just replace <code>26325</code> with the revision of the nightly build downloaded  from <a href="http://download.slicer.org/">http://download.slicer.org/</a> .</p>
<p>You can also get the revision of your current Slicer install looking at <code>File -&gt; About</code>  or from the python interactor typing <code>slicer.app.repositoryRevision</code></p>
<p>Then, from your office, you can install the extension from file.</p>
<p>See <a href="https://www.slicer.org/wiki/Documentation/4.6/SlicerApplication/ExtensionsManager#Installing_an_extension_without_network_connection" class="inline-onebox">Documentation/4.6/SlicerApplication/ExtensionsManager - Slicer Wiki</a></p>

---

## Post #3 by @aliocha12 (2017-09-25 22:23 UTC)

<p>Jcfr,</p>
<p>That worked, but I noticed that I the “contours” module I usually use to convert DICOM to stl is missing. Would there be a new workflow in v 4.7 for that process? Thank you.</p>
<p>Alex</p>

---

## Post #4 by @lassoan (2017-09-25 23:34 UTC)

<p>In Slicer 4.7, Contours module is replaced by the much more advanced Segmentations module.</p>

---
