# Fastest way to load DICOM

**Topic ID**: 9317
**Date**: 2019-11-27
**URL**: https://discourse.slicer.org/t/fastest-way-to-load-dicom/9317

---

## Post #1 by @fbordignon (2019-11-27 20:12 UTC)

<p>Hi guys, firstly I would like to acknowledge the great work the Slicer team is doing. The software is really great!<br>
I am from a startup company from Brazil that is working with CT images of rock samples from well cores (133mm of diameter per 900mm of length), core plugs (1 in. in diameter by 2 in length) and micro plugs (3mm in diameter). Slicer is being really helpful in loading the data and manipulating it.</p>
<p>For the well cores case, we need to load a lot of them inside slicer for processing. They are the rock cylindrical core of a oil well, which can be several hundred meters long (region of interest only). Therefore, we need to load several hundred cores inside slicer to process, visualize and interpret them as a whole set.</p>
<p>Now to my question: What is the fastest way to load them inside slicer. I don’t care about dicom metadata, and patient IDs or stuff like that. I only care about the pixel size and slice distance for maintaining the original size and distances inside the image.</p>
<p>I’ve been doing with a temporary dataset as suggested by cpinter <a href="https://discourse.slicer.org/t/how-to-convert-dicom-files-to-nrrd/540/11" class="inline-onebox">How to convert dicom files to nrrd</a><br>
The idea is to load the volume and do not work with dicom anymore.</p>

---

## Post #2 by @lassoan (2019-11-27 21:13 UTC)

<aside class="quote no-group" data-username="fbordignon" data-post="1" data-topic="9317">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fbordignon/48/5269_2.png" class="avatar"> fbordignon:</div>
<blockquote>
<p>What is the fastest way to load them inside slicer.</p>
</blockquote>
</aside>
<p>Use the latest Slicer Preview Release, as DICOM import speed is greatly improved.</p>
<p>If you get scans one by one then you can import them one by one (by drag-and-dropping to the application window), loading them using DICOM browser, then save them as .nrrd.</p>
<p>If you have hundreds of files already then you can write a short Python script that iterates through all your data. You can use tools or scripts described in the topic that you referred above, or you can use a use/customize a simple script like this:</p>
<pre data-code-wrap="python"><code class="lang-python">dicomDataDir = 'c:/tmp/inputDicomFiles'
outputDir = 'c:/tmp/outputNrrdFiles'

import DICOMLib
import re
DICOMLib.importDicom(dicomDataDir)
dicomFiles = slicer.util.getFilesInDirectory(dicomDataDir)
loadablesByPlugin, loadEnabled = DICOMLib.getLoadablesFromFileLists([dicomFiles])
loadedNodeIDs = DICOMLib.loadLoadables(loadablesByPlugin)
for loadedNodeID in loadedNodeIDs:
    node = slicer.mrmlScene.GetNodeByID(loadedNodeID)
    safeFileName = re.sub(r'(?u)[^-\w.]', '', node.GetName().strip().replace(' ', '_'))
    slicer.util.saveNode(node, '{0}/{1}.nrrd'.format(outputDir, safeFileName))
</code></pre>

---

## Post #3 by @pieper (2019-11-27 21:31 UTC)

<p>Hi <a class="mention" href="/u/fbordignon">@fbordignon</a> -</p>
<p>Another option that could really speed things up is to bypass dicom parsing entirely.  If you know that the slices are all the same dimensions and spacing, and have a predictable filename convention like img0000.dcm, img0001.dcm etc, then you can take advantage of the <code>data file</code> and <code>byte skip</code> options and make a <code>.nhdr</code> file for each scan that corresponds to a slicer volume.  See more info <a href="http://teem.sourceforge.net/nrrd/format.html">on the nrrd format page</a>.</p>

---

## Post #4 by @fbordignon (2019-11-28 18:04 UTC)

<p>Thanks, lassoan. I am already using the latest nightly and python scripts to do that. I will take a look if your solution improves the loading time for my case.</p>
<p>pieper, your reply is something closer of what I was looking for. I will try to do that and post here the results. Thanks</p>

---

## Post #5 by @lassoan (2019-11-28 18:42 UTC)

<p>If you need to convert a DICOM image to NRRD only once and then you always use NRRD then having nhdr headers to load them will not help, as you need to parse the files once anyway. Also, loading will be much slower, every time you load the image (while if you convert to a single-file NRRD once, then loading will be very fast). Also, I don’t think NRRD supports per-file custom header size at all, so creating a .nhdr file that loads frames from many DICOM files might not be even feasible.</p>
<p>If you use latest Slicer Preview Release then you should be able to import hundreds of files per second (DICOM parsing time is negligible, and indexing should take just a few seconds in total). However, loading the image data from DICOM takes longer because several strategies for reading the images are evaluated.</p>
<p>Overall, for optimal performance, I would suggest to import and load the image from DICOM and save as uncompressed single-file NRRD.</p>

---

## Post #6 by @pieper (2019-11-28 19:06 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> - The nhdr <code>data size</code> option of -1 will auto-calculate the header size if the dimensions are correct and the data is uncompressed.  From what <a class="mention" href="/u/fbordignon">@fbordignon</a> said I believe he has a bunch of samples that are all in the same pattern, so parsing the dicom may not be needed at all.</p>

---
