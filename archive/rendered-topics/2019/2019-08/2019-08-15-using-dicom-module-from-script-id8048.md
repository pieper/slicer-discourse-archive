---
topic_id: 8048
title: "Using Dicom Module From Script"
date: 2019-08-15
url: https://discourse.slicer.org/t/8048
---

# Using Dicom Module from Script

**Topic ID**: 8048
**Date**: 2019-08-15
**URL**: https://discourse.slicer.org/t/using-dicom-module-from-script/8048

---

## Post #1 by @burnhamd (2019-08-15 20:15 UTC)

<p>I would like to load the dicom browser in my slicelet.  Is there an example of doing this?  I am able to access the browser through slicer.modules.dicom.widgetRepresentation, but of course this is empty.</p>
<p>I am assuming I have to set some dicom database to see my dicom datasets, but am at a loss of how to do this.</p>

---

## Post #2 by @pieper (2019-08-15 23:24 UTC)

<p>You can access the instance with <code>slicer.modules.DICOMInstance</code>, but this is created lazily, so you may need to first enter the module, which you can do with:</p>
<pre><code class="lang-auto">slicer.util.mainWindow().moduleSelector().selectModule('DICOM') 
</code></pre>
<p>But typically you shouldn’t need to access the module widget, but instead use the logic and plugins directly.  There are some examples <a href="https://github.com/Slicer/Slicer/blob/aedb7d6702a30b485be952f2c933dfd96f072f02/Applications/SlicerApp/Testing/Python/DICOMReaders.py" rel="nofollow noopener">in the tests</a>.</p>

---

## Post #3 by @cpinter (2019-08-15 23:50 UTC)

<p>I would recommend taking a look in the script repository. There are tons of examples, grouped by topic.<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#DICOM_2" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#DICOM_2</a></p>

---

## Post #4 by @burnhamd (2019-08-19 19:40 UTC)

<p>Ended up using the following call</p>
<p><code>slicer.modules.DICOMWidget.detailsPopup.show()</code></p>

---
