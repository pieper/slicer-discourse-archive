# Need slicer 4.5.0-2016-06-22 package for MacOs (nighly build)

**Topic ID**: 621
**Date**: 2017-07-04
**URL**: https://discourse.slicer.org/t/need-slicer-4-5-0-2016-06-22-package-for-macos-nighly-build/621

---

## Post #1 by @florianputz (2017-07-04 11:08 UTC)

<p>Hello everyone,</p>
<p>we developed an internal segmentation solution (python module) for <strong>Slicer 4.5-2016-06-22</strong> (Windows version, nightly build).</p>
<p>Everything worked quite fine.</p>
<p>Now, the module is planned to be used on a macOs device.</p>
<p>Unfortunately, <strong>Slicer 4.5-2016-06-22 nighly build isn’t available anymore for download</strong><br>
and <a href="http://slicer.kitware.com/midas3/download/item/244951" rel="nofollow noopener">http://slicer.kitware.com/midas3/download/item/244951</a> etc. always gives a “<strong>Unable to find file on the disk</strong>”-error.</p>
<p>Sadly, there are quite a few errors, when running the python module on later or earlier stable versions of 3DSlicer.</p>
<p>The Slicer 4.5-2016-06-22 nighly package thus would save us quite some time in rewriting the code and testing.</p>
<p>Any help is greatly appreciated.</p>
<p>Thank you</p>
<p>Florian</p>

---

## Post #2 by @lassoan (2017-07-04 16:07 UTC)

<p>We don’t archive all nightly build versions of indefinitely long. I would recommend to update to the latest nightly version. Required changes should be all trivial. Just write what errors you get and we can tell what to change.</p>

---
