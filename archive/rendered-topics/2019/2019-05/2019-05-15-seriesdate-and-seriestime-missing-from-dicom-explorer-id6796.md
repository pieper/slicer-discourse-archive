---
topic_id: 6796
title: "Seriesdate And Seriestime Missing From Dicom Explorer"
date: 2019-05-15
url: https://discourse.slicer.org/t/6796
---

# SeriesDate and SeriesTime missing from DICOM explorer

**Topic ID**: 6796
**Date**: 2019-05-15
**URL**: https://discourse.slicer.org/t/seriesdate-and-seriestime-missing-from-dicom-explorer/6796

---

## Post #1 by @torquil (2019-05-15 09:49 UTC)

<p>Hi!</p>
<p>I upgraded from 3D Slicer Nightly 2019-03-18 to 2019-05-11 on Linux, and now the columns “SeriesDate” and “SeriesTime” are missing from the DICOM explorer. These columns are very important for me when comparing different image series. Is it possible to get them back?</p>
<p>Is there some place to configure which columns that are shown?</p>
<p>In the older nightly, I had the following items in the bottom left hand corner of the DICOM<br>
database navigation window:</p>
<p>DICOMRWVMPlugin<br>
DICOMParametricMapPlugin<br>
DICOMPETSUVPlugin<br>
DICOMSegmentationPlugin<br>
DICOMTID1500Plugin<br>
MultiVolumeImporterPlugin<br>
DICOMScalarVolumePlugin<br>
DICOMSlicerDataBundlePlugin</p>
<p>and following four extensions were installed:</p>
<p>DCMQI, PETDICOMExtension, QuantitativeReporting and SlicerDevelopmentToolbox</p>
<p>For the newer nightly, the following is in the bottom left corner of the DICOM window:</p>
<p>DICOMScalarVolumePlugin<br>
DICOMSlicerDataBundlePlugin<br>
MultiVolumeImporterPlugin</p>
<p>and the same extensions are installed.</p>
<p>Best regards,<br>
Torquil Sørensen, Norway</p>

---

## Post #2 by @lassoan (2019-05-15 14:10 UTC)

<p>Series date is the same as study date (except extremely rare cases) and series number tells you what order the series were acquired. You can get the exact series date&amp;time by clicking on Metadata button.</p>
<p>So, overall I don’t see this as a huge issue, but I agree that we should probably show at least the study time and maybe also the series date&amp;time should be shown in the table by default.</p>
<aside class="quote no-group" data-username="torquil" data-post="1" data-topic="6796">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e79b87/48.png" class="avatar"> torquil:</div>
<blockquote>
<p>Is there some place to configure which columns that are shown?</p>
</blockquote>
</aside>
<p>Yes. List and order of displayed fields are stored in the DICOM database (ctkDICOM.sql file, ColumnDisplayProperties table), which you can edit using any SQLite editor (such as <a href="https://sqlitebrowser.org/">this</a>). Set <code>Visibility</code> value to <code>1</code> for <code>SeriesDate</code> and <code>SeriesTime</code> to make these fields show up.</p>

---

## Post #3 by @torquil (2019-05-15 14:36 UTC)

<p>Thanks! I activated the SeriesTime column in the way you proposed, so I can now use the newest Slicer nightly and work as before. It would really slow me down quite a bit if I needed to open the metadata each time I wanted to look at the seriestime value. I’m comparing a lot of data between Slicer and other sources, and all the data is timestamped, so usually I must select data based on the seriestime value. I go back and forth between different data quite a lot, so it would slow me down to have it “buried” inside the metadata.</p>
<ul>
<li>Torquil</li>
</ul>

---

## Post #4 by @lassoan (2019-05-15 16:44 UTC)

<aside class="quote no-group" data-username="torquil" data-post="3" data-topic="6796">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e79b87/48.png" class="avatar"> torquil:</div>
<blockquote>
<p>I can now use the newest Slicer nightly and work as before</p>
</blockquote>
</aside>
<p>Great! This customization feature is new and still has not reached its full potential. We should probably make customization of displayed columns easier (e.g., available in Slicer application settings) because preferences are always user and workflow dependent.</p>
<aside class="quote no-group" data-username="torquil" data-post="3" data-topic="6796">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e79b87/48.png" class="avatar"> torquil:</div>
<blockquote>
<p>usually I must select data based on the seriestime value</p>
</blockquote>
</aside>
<p>I’m just wondering why. Series number is a simple number, guaranteed to be unique within the study, monotonously increasing (except maybe secondary captures and other reports). Looking up series based on date and time is much harder and less robust: there are 12-15 digits to compare, anonymization may shift the date&amp;time values, there may be difference in how various software handle date&amp;time formatting, time zones, etc.</p>

---
