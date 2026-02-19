---
topic_id: 14203
title: "Import Dicom Files"
date: 2020-10-22
url: https://discourse.slicer.org/t/14203
---

# Import DICOM files

**Topic ID**: 14203
**Date**: 2020-10-22
**URL**: https://discourse.slicer.org/t/import-dicom-files/14203

---

## Post #1 by @marianaslicer (2020-10-22 14:00 UTC)

<p>Operating system: windows 7<br>
Slicer version: 4.11.20200930</p>
<p>Hi slicers,</p>
<p>I want to load the dicom data from patient UID from DICOM database.<br>
I have already the series seriesUIDs and now I want to get the same output as:</p>
<p>dicomWidget.detailsPopup.offerLoadables(seriesUIDs, ‘SeriesUIDList’)<br>
dicomWidget.detailsPopup.examineForLoading()<br>
dicomWidget.detailsPopup.loadCheckedLoadables()</p>
<p>But since I’m working with 3Dslicer version 4.11 I would like to know how I get that.<br>
Any idea? I would really appreciate your help.</p>

---

## Post #2 by @lassoan (2020-10-25 05:21 UTC)

<p>DICOM infrastructure has been greatly improved in Slicer-4.11 and you don’t need to use GUI widget classes to load DICOM data.</p>
<p>If you already have the series UID then you can load them like this:</p>
<pre><code class="lang-python">from DICOMLib import DICOMUtils
loadedVolumeNodes = DICOMUtils.loadSeriesByUID(seriesUIDs)
</code></pre>
<p>You can find up-to-date examples for current Slicer version in the current script repository:</p>
<aside class="onebox allowlistedgeneric">
  <header class="source">
      <img src="https://www.slicer.org/w/img_auth.php/6/64/Favicon.ico" class="site-icon" width="16" height="16">
      <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder" target="_blank" rel="noopener">slicer.org</a>
  </header>
  <article class="onebox-body">
    <img src="" class="thumbnail" width="16" height="16">

<h3><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_load_DICOM_files_into_the_scene_from_a_folder" target="_blank" rel="noopener">Documentation/Nightly/ScriptRepository - Slicer Wiki</a></h3>



  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>


---
