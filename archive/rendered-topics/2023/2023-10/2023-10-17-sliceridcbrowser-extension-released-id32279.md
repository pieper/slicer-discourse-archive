---
topic_id: 32279
title: "Sliceridcbrowser Extension Released"
date: 2023-10-17
url: https://discourse.slicer.org/t/32279
---

# SlicerIDCBrowser extension released!

**Topic ID**: 32279
**Date**: 2023-10-17
**URL**: https://discourse.slicer.org/t/sliceridcbrowser-extension-released/32279

---

## Post #1 by @fedorov (2023-10-17 18:36 UTC)

<p>We are happy to announce that <a href="https://github.com/ImagingDataCommons/SlicerIDCBrowser">SlicerIDCBrowser</a> extension of 3D Slicer is now available, and can be accessed via the Slicer Extensions Manager both in the stable 5.4.0 and preview releases of 3D Slicer that can be downloaded <a href="https://download.slicer.org/">here</a>.</p>
<p>This new extension aims to simplify access to the data available in IDC by allowing you to browse through the collections available, and select individual items to download and add to the Slicer DICOM database as you can see in the demo below.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="m_jfSTWIYvc" data-video-title="SlicerIDCBrowser extension demo" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=m_jfSTWIYvc" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/m_jfSTWIYvc/maxresdefault.jpg" title="SlicerIDCBrowser extension demo" width="690" height="388">
  </a>
</div>

<p>Behind the scenes, the extension uses the same mechanism as documented in <a href="https://learn.canceridc.dev/data/downloading-data">IDC Download instructions</a>, automatically downloading <code>s5cmd</code> binaries suitable for your platform, fetching the data from cloud buckets using <code>s5cmd</code>, and eliminating the need to use command line.</p>
<p>There are many improvements we have in mind for this extension (you can see the known issues/features considered here: <a href="https://github.com/ImagingDataCommons/SlicerIDCBrowser" class="inline-onebox">GitHub - ImagingDataCommons/SlicerIDCBrowser: A 3D Slicer extension to support access to the content of NCI Imaging Data Commons</a>) - and you are welcome to contribute to its development if you like! If there are features you would like to see added, or if you have any feedback about this extension, please let us know.</p>
<hr>
<p>Cross-posted from <a href="https://discourse.canceridc.dev/t/sliceridcbrowser-extension-released/515" class="inline-onebox">SlicerIDCBrowser extension released! - Announcements - Imaging Data Commons</a>.</p>

---

## Post #2 by @fedorov (2024-06-19 20:25 UTC)

<p>Recently, we added a feature to this extension that allows you to specify ID of the collection, DICOM patient, study, or series available in Imaging Data Commons, and download the corresponding files to you computer from Slicer. The video below demonstrates how you can access those identifiers and how you can use this new feature.</p>
<div class="youtube-onebox lazy-video-container" data-video-id="_KQDL9JzMB4" data-video-title="SlicerIDCBrowser: Downloading content selected in IDC Portal" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=_KQDL9JzMB4" target="_blank" class="video-thumbnail" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/_KQDL9JzMB4/maxresdefault.jpg" title="SlicerIDCBrowser: Downloading content selected in IDC Portal" width="690" height="388">
  </a>
</div>


---
