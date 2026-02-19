---
topic_id: 23589
title: "Error With Export Segmentation To Dicom"
date: 2022-05-25
url: https://discourse.slicer.org/t/23589
---

# Error with export segmentation to DICOM

**Topic ID**: 23589
**Date**: 2022-05-25
**URL**: https://discourse.slicer.org/t/error-with-export-segmentation-to-dicom/23589

---

## Post #1 by @melvlad27 (2022-05-25 16:46 UTC)

<p>When I want to export my segmentation, I see this message in my log.</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "C:/Users/AppData/Local/NA-MIC/Slicer 5.0.2/NA-MIC/Extensions-30822/QuantitativeReporting/lib/Slicer-5.0/qt-scripted-modules/DICOMSegmentationPlugin.py", line 367, in export
    exporter.export(exportable.directory, segFileName, metadata)
  File "C:/Users/AppData/Local/NA-MIC/Slicer 5.0.2/NA-MIC/Extensions-30822/QuantitativeReporting/lib/Slicer-5.0/qt-scripted-modules/DICOMSegmentationPlugin.py", line 565, in export
    raise RuntimeError("%s:\n\n%s" % (cliNode.GetStatusString(), cliNode.GetErrorText()))
RuntimeError: Completed with errors:
</code></pre>

---

## Post #2 by @lassoan (2022-05-25 16:49 UTC)

<p>I’ve just tested segmentation DICOM export using Slicer-5.0.2 on Windows and it worked well for me.</p>
<p>Please provide more logs (above and below this message). That may give us hints about what went wrong.</p>
<p>If the logs are not informative enough then we would need an example scene that reproduces this error. You can use your data set if it is anonymized, or use any of the example data sets in Slicer or other public data sets.</p>

---
