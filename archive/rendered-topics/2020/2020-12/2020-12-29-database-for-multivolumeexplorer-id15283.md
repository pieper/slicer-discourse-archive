# Database for MultiVolumeExplorer

**Topic ID**: 15283
**Date**: 2020-12-29
**URL**: https://discourse.slicer.org/t/database-for-multivolumeexplorer/15283

---

## Post #1 by @Anonymous1 (2020-12-29 20:33 UTC)

<p>Hi!<br>
To use MultiVolumeExplorer I need a database that has the extension dcm. Does anyone know of a biomedical imaging database with that extension?</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-12-30 05:34 UTC)

<p>What kind of data sets are you looking for? What is the overall goal that you would like to achieve?</p>

---

## Post #3 by @Anonymous1 (2020-12-30 08:25 UTC)

<p>I’m looking for CT images of lung cancer and COVID-19. What I want to do is compare the intensity of the affected regions with MultiVolumeExplorer.</p>

---

## Post #4 by @lassoan (2020-12-31 06:19 UTC)

<p>You can download lots of COVID-19 patient data sets from <a href="https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=80969742">TCIA</a>.</p>
<p>MultiVolumeExplorer is for browsing 4D data sets, not for comparing 3D volumes. You can use basic Slicer GUI to view/compare chest CTs - see <a href="https://slicer.readthedocs.io/en/latest/user_guide/getting_started.html#view-data">documentation</a> and <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training">tutorials</a>.</p>
<p>You may find the <a href="https://discourse.slicer.org/t/new-lungctanalyzer-extension-for-lung-ct-segmentation-and-analysis-for-covid-19-assessment/15006">LungCTAnalyzer extension</a> useful. For additional analysis and quantification, you may check out the <a href="https://chestimagingplatform.org/workstation-slicer-cip">Chest Imaging Platform</a>.</p>

---
