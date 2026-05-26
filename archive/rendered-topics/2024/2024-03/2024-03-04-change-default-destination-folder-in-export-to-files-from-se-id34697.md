---
topic_id: 34697
title: "Change default destination folder in Export to files from segmentations module with python"
date: 2024-03-04
url: https://discourse.slicer.org/t/34697
last_bumped: 2026-04-16T10:18:09.910Z
---

# Change default destination folder in Export to files from segmentations module with python

**Topic ID**: 34697
**Date**: 2024-03-04
**URL**: https://discourse.slicer.org/t/change-default-destination-folder-in-export-to-files-from-segmentations-module-with-python/34697

---

## Post #1 by @garridojuan (2024-03-04 16:27 UTC)

<p>I am developing a tool that automatically opens a segmentation mask and the image in 3D Slicer so that the user can modify it. I do it by using --python-code option when executing slicer from terminal.</p>
<p>I would love to have all format options properly pre-established for better user experience. However, I could not find in the documentation where I can change them in the “Export to files” menu of the Segmentations module.</p>
<p>Thank you in advanced.</p>

---

## Post #2 by @garridojuan (2026-04-16 10:18 UTC)

<p>I found the solution, or a workaround at least. You can control the destination folder used in the <strong>“Export to files”</strong> menu of the Segmentations module through application settings.</p>
<p>The path is stored using <code>qt.QSettings</code>, so you can predefine it programmatically before the export operation.</p>
<p>Here is how you can set it:</p>
<pre data-code-wrap="python"><code class="lang-python">import qt

desiredDestinationFolder = r"here/i/want/my/segmentation"
settings = qt.QSettings()
settings.setValue('ExportSegmentsToFiles/DestinationFolder', desiredDestinationFolder)
</code></pre>
<p>By setting this value in advance, the export dialog will default to your desired folder, improving the user experience when running your automated workflow.</p>

---
