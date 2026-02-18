# Loading specific series by ID

**Topic ID**: 8847
**Date**: 2019-10-21
**URL**: https://discourse.slicer.org/t/loading-specific-series-by-id/8847

---

## Post #1 by @prorai (2019-10-21 13:05 UTC)

<p>DICOMScalarVolumePluginClass() -  i’m using this plugin to load scalar volume from a dicom folder ,<br>
how can i load only specific series with specific images/slices under that series ID</p>

---

## Post #2 by @pieper (2019-10-21 14:37 UTC)

<p>You can use the dicom database methods to determine the specific files / instances for any series and provide that to load.   These examples should help:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#DICOM_2" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#DICOM_2</a></p>

---
