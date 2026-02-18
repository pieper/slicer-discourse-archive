# DICOM export of segmentation node

**Topic ID**: 313
**Date**: 2017-05-15
**URL**: https://discourse.slicer.org/t/dicom-export-of-segmentation-node/313

---

## Post #1 by @hgueziri (2017-05-15 18:16 UTC)

<p>Hi everyone,</p>
<p>I am writing a python module and wanted to know if it is possible to export a Segmentation node to a RTSS DICOM <strong>without</strong> its associated DICOM volume ?</p>
<p>In the example of the attached image: I want to export RTSTRUCT without MRI volume.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2634d01eaf5058586ad628e93868f1e77c68ff67.png" alt="image" data-base62-sha1="5rZiiw25gjn3RdsLNY4tHRdfwwL" width="326" height="99"></p>
<p>I used the code from SlicerProstate to create a new study that includes the MR volume and the RTSS, but this solution requires to export both the MR volume and the RTSS.</p>
<p>Many thanks,</p>

---

## Post #2 by @lassoan (2017-05-15 21:23 UTC)

<p>I think this has been addressed in recent versions, but <a class="mention" href="/u/cpinter">@cpinter</a> can confirm within a few days.</p>

---

## Post #3 by @cpinter (2017-05-15 21:46 UTC)

<p>As far as I can remember what was actually resolved when this issue came up last time was the speed of the export, which was drastically slowed down by the automatic importing of the exported DICOM back into the database. The export now takes only a few seconds, so allowing the export of only the RTSS was not implemented. The reasons:</p>
<ol>
<li>As RTSS represents structures as planar contours, a master volume is needed in many cases to determine the planes to do the cutting.</li>
<li>DICOM requires references from RTSS to an anatomical volume (3006,0014, and 3006,0016, both type 1), so exporting them both is necessary to make the exported DICOM valid.</li>
</ol>
<p>If you don’t need the MRI image, you can remove it after the export.</p>

---

## Post #4 by @hgueziri (2017-05-15 23:04 UTC)

<p>Hi Csaba,</p>
<p>Thanks for the quick answer.</p>
<p>Actually, the speed of the export is fine and works just good on a local computer. The problem is that our workflow uses the internal network to process the data. So, each time we export the RTSS, we have to wait about 10 min for the DICOM to be exported first.</p>
<p>One solution would be to export everything locally then send the required RTSS through the network (not sure if it is possible with the actual settings). Is it possible to export the DICOM on a temporary location without the dialog window popping?</p>
<p>Thanks<br>
Houssem</p>

---

## Post #5 by @cpinter (2017-05-16 07:07 UTC)

<p>Exporting to a temporary location should be the way to go, I agree.<br>
I’m on my way to the airport so cannot prepare you a script, but here’s one that does export programmatically, bypassing the GUI<br>
<aside class="onebox whitelistedgeneric">
  <header class="source">
      <img src="https://cfl.dropboxstatic.com/static/images/favicon-vflUeLeeY.ico" class="site-icon" width="32" height="32">
      <a href="https://www.dropbox.com/s/j4cmpv5x7hupewy/20160826_DICOMVolumeExport_MatthewMouawad.py?dl=0" target="_blank">Dropbox</a>
  </header>
  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:214/200;"><img src="https://cfl.dropboxstatic.com/static/images/logo_catalog/glyph_m1%402x.png" class="thumbnail" width="214" height="200"></div>

<h3><a href="https://www.dropbox.com/s/j4cmpv5x7hupewy/20160826_DICOMVolumeExport_MatthewMouawad.py?dl=0" target="_blank">Dropbox - Link not found</a></h3>

<p>Dropbox is a free service that lets you bring your photos, docs, and videos anywhere and share them easily. Never email yourself a file again!</p>


  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>
<br>
Things changed in Slicer core since then, so you may need to adjust a few lines.</p>
<p>Let me know how it goes, I can be of better help tomorrow.</p>

---

## Post #6 by @cpinter (2017-05-16 08:38 UTC)

<p>An important piece of information is that instead of using the scalar volume exporter, you will need to use the RT exporter. This means that you’ll need to</p>
<ul>
<li>import DicomRtImportExportPlugin</li>
<li>Instantiate it (bottom of script) like this:<br>
exporter = DicomRtImportExportPlugin.DicomRtImportExportPlugin(tags[…</li>
</ul>
<p>One thing that can make this script a lot shorter is to use examineForExport to automatically populate the exportables that you can pass to the export function. You’ll need to use subject hierarchy items, which you can get by the nodes as explained in the script repo<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_subject_hierarchy_item" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_subject_hierarchy_item</a></p>

---

## Post #7 by @hgueziri (2017-05-16 18:39 UTC)

<p>Thank you Csaba for your help. It works great now.<br>
I used the DicomRtImportExportPlugin. It looks like</p>
<pre><code>import DicomRtImportExportPlugin
exporter = DicomRtImportExportPlugin.DicomRtImportExportPluginClass()
exportables = []
mrSegmentationExportable = exporter.examineForExport(mrSegmentationForExportShItemID)
mrVolumeExportable = exporter.examineForExport(mrVolumeForExportShItemID)
exportables.extend(mrVolumeExportable)
exportables.extend(mrSegmentationExportable)
for exp in exportables:
    exp.directory = temporaryFolderPath
exporter.export(exportables)
</code></pre>
<p>However, if I export only the Segmentations, it does not work but I get no error message.</p>
<p>Houssem</p>

---

## Post #8 by @cpinter (2017-05-17 03:44 UTC)

<p>I’m glad I could be of help. Good job on the script!</p>

---
