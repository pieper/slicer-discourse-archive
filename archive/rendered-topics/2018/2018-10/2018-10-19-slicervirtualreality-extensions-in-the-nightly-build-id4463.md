# SlicerVirtualReality Extensions in the nightly build

**Topic ID**: 4463
**Date**: 2018-10-19
**URL**: https://discourse.slicer.org/t/slicervirtualreality-extensions-in-the-nightly-build/4463

---

## Post #1 by @Mathieu_Westphal (2018-10-19 11:39 UTC)

<p>According to this blog <a href="https://blog.kitware.com/slicervirtualreality/" rel="nofollow noopener">https://blog.kitware.com/slicervirtualreality/</a>, a SlicerVirtualReality extension should be available in the nightly build of Slicer.</p>
<p>I’ve downloaded revision 27498 and it is nowhere to be found.</p>
<p>Am I missing something here ?</p>

---

## Post #2 by @cpinter (2018-10-19 13:08 UTC)

<p>The SlicerVirtualReality extension does not build since <a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2018-10-13&amp;filtercount=1&amp;showfilters=1&amp;field1=label&amp;compare1=63&amp;value1=VirtualReality">the 13th</a>. The <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1398326">error</a> doesn’t say much (“could not load cache”), but it builds fine on my computer for example. We’re in the process of releasing the next stable (4.10), then we’ll investigate why it has issues on the factory.</p>
<p>I made an installer yesterday. Here’s the <a href="https://www.dropbox.com/s/qgewkjhjo3nlhfd/Slicer-4.9.0-2018-10-16-win-amd64.exe?dl=0">Slicer package</a>, and the <a href="https://www.dropbox.com/s/f9z19pte6nuwqfh/27491-win-amd64-SlicerVirtualReality-gite81f7bc-2018-10-18.zip?dl=0">VR extension</a>. To install the extension from the file, click the “Install Extension from File…” menu item under the wrench icon on the top right of Extension Manager right next to the search field. Then select the extension zip file in the file dialog and click Open.</p>

---

## Post #3 by @lassoan (2018-10-22 17:47 UTC)

<p>Since then Slicer-4.10 has been released and SlicerVirtualReality extension is available for this version.</p>

---
