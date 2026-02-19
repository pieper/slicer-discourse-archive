---
topic_id: 6435
title: "Slicerdcm2Nii Extension Not Visible In Extension Manager Des"
date: 2019-04-08
url: https://discourse.slicer.org/t/6435
---

# SlicerDcm2nii extension not visible in Extension Manager despite successful build

**Topic ID**: 6435
**Date**: 2019-04-08
**URL**: https://discourse.slicer.org/t/slicerdcm2nii-extension-not-visible-in-extension-manager-despite-successful-build/6435

---

## Post #1 by @ljod (2019-04-08 16:45 UTC)

<p>Hi we are trying to make the SlicerDCM2nii extension (<a href="https://github.com/SlicerDMRI/SlicerDcm2nii" rel="nofollow noopener">https://github.com/SlicerDMRI/SlicerDcm2nii</a>) available again to users. It has built successfully on Mac (with a few warnings but no errors) and Linux (no warnings), but it does not appear in the extension manager or on the online web Slicer appstore. It has no dependencies on other modules in its CMake files, so we are not sure what is wrong.</p>
<p>Does anyone have a suggestion of what is wrong or where to look?  Thanks!!</p>
<p><a href="http://slicer.cdash.org/buildSummary.php?buildid=1558630" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/buildSummary.php?buildid=1558630</a><br>
<strong>Site Name:</strong>  <a href="http://slicer.cdash.org/viewSite.php?siteid=862" rel="nofollow noopener">factory-south-macos.kitware </a><br>
<strong>Build Name:</strong>  28092-SlicerDcm2nii-git91ea4d6-g+±64bits-Qt5.10-Release<br>
<strong>Stamp:</strong>  20190408-0300-Extensions-Nightly<br>
<strong>Time:</strong>  2019-04-08T13:13:50 UTC<br>
<strong>Type:</strong>  Extensions-Nightly</p>

---

## Post #2 by @jcfr (2019-04-08 17:58 UTC)

<p>Looking at the dashboard, it has been built on macOS and Linux:</p>
<p><a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2019-04-08&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerDCM2nii" class="onebox" target="_blank" rel="noopener">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2019-04-08&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerDCM2nii</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/14cc2dad5439e59b0075d58ccbd1036393993e83.png" data-download-href="/uploads/short-url/2XYZYJb5uhocWlEPvLu3NOrgqXx.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14cc2dad5439e59b0075d58ccbd1036393993e83_2_690x163.png" alt="image" data-base62-sha1="2XYZYJb5uhocWlEPvLu3NOrgqXx" width="690" height="163" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14cc2dad5439e59b0075d58ccbd1036393993e83_2_690x163.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14cc2dad5439e59b0075d58ccbd1036393993e83_2_1035x244.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/4/14cc2dad5439e59b0075d58ccbd1036393993e83_2_1380x326.png 2x" data-dominant-color="CFD8D1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1585×376 47.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But there are errors on windows. See <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1558053" class="inline-onebox">CDash</a></p>
<p>This file need to be updated: <a href="https://github.com/rordenlab/dcm2niix/blob/development/console/nii_dicom_batch.cpp" class="inline-onebox">dcm2niix/console/nii_dicom_batch.cpp at development · rordenlab/dcm2niix · GitHub</a></p>
<p>Errors related to <code>abs</code> can be fixed using <code>fabs</code>.</p>
<p>Errors related to <code>getline</code> could be fixed by updating the code to use <a href="http://www.cplusplus.com/reference/istream/istream/getline/">istream::getline</a> instead</p>

---

## Post #3 by @ljod (2019-04-08 18:18 UTC)

<p>Thanks JC this is very helpful for fixing the errors. But the extension, despite building on Mac and Linux, does not show up in the extension manager on those platforms. Do you have any idea why this would happen?</p>

---

## Post #4 by @ljod (2019-04-11 16:18 UTC)

<p>JC do you know if there some problem with the way this extension is set up? It is not being distributed through the Extension Manager, and it is not visible in the online app store at <a href="http://slicer.kitware.com/midas3/slicerappstore" rel="nofollow noopener">http://slicer.kitware.com/midas3/slicerappstore</a>. (Thanks to Chris Rorden, the code now compiles on all platforms.)</p>
<p>Before Isaiah left, on his last day the extension did show up in the nightly, so my assumption is that it should show up again now that it compiles…</p>
<p>Here is the latest compilation result:<br>
<a href="http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerDCM2nii" class="onebox" target="_blank" rel="nofollow noopener">http://slicer.cdash.org/index.php?project=SlicerPreview&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=SlicerDCM2nii</a></p>

---
