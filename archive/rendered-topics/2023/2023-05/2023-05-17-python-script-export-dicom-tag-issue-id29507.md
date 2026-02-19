---
topic_id: 29507
title: "Python Script Export Dicom Tag Issue"
date: 2023-05-17
url: https://discourse.slicer.org/t/29507
---

# Python Script - Export DICOM Tag issue

**Topic ID**: 29507
**Date**: 2023-05-17
**URL**: https://discourse.slicer.org/t/python-script-export-dicom-tag-issue/29507

---

## Post #1 by @Markb (2023-05-17 14:20 UTC)

<p>Hi all. I have a python script to automate making a bunch of masked data based on a PET and RTStruct file. As there are quite a few segments per study, and I have hundreds of studies, I want to automate this as much as possible. The mask bit works great, but the next stage is exporting the data as a DICOM dataset.</p>
<p>When I do this manually, I would drag the masked data into the parent folder in the Data scene, and right click Export DICOM. I would select an appropriate folder and leave everything else as default, and this works create but as I can only do one at a time, it is slow and prone to human error.</p>
<p>My script is all set up to create the relevant folders etc. and save the nodes, but with the DICOMExportScalarVolume command, it needs the tags. I was hoping to just copy these from the initial PET data, but I’m struggling to find a way to do this. Any direction would be greatly appreciated.</p>
<p>Thank you</p>

---

## Post #2 by @pieper (2023-05-17 21:24 UTC)

<p>If you look at the source code there’s a comment with an example of copying tags from a study:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/1f99feaa638394effd53b4e14636b28082d6ff8b/Modules/Scripted/DICOMLib/DICOMExportScalarVolume.py#L10">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/1f99feaa638394effd53b4e14636b28082d6ff8b/Modules/Scripted/DICOMLib/DICOMExportScalarVolume.py#L10" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/1f99feaa638394effd53b4e14636b28082d6ff8b/Modules/Scripted/DICOMLib/DICOMExportScalarVolume.py#L10" target="_blank" rel="noopener">Slicer/Slicer/blob/1f99feaa638394effd53b4e14636b28082d6ff8b/Modules/Scripted/DICOMLib/DICOMExportScalarVolume.py#L10</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="1" style="counter-reset: li-counter 0 ;">
          <li>import logging</li>
          <li>
          </li>
<li>import slicer</li>
          <li>
          </li>
<li>#########################################################</li>
          <li>#</li>
          <li>#</li>
          <li>comment = """</li>
          <li>
          </li>
<li class="selected">DICOMExportScalarVolume provides the feature of exporting a slicer</li>
          <li>scalar volume as a DICOM series into local folder.</li>
          <li>
          </li>
<li>This code is slicer-specific and relies on the slicer python module</li>
          <li>for elements like slicer.dicomDatatabase and slicer.mrmlScene</li>
          <li>
          </li>
<li>"""</li>
          <li>#</li>
          <li>#########################################################</li>
          <li>
          </li>
<li>
      </li>
</ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @Markb (2023-05-18 10:02 UTC)

<p>Thank you Steve. I saw that bit of the code commented out and labelled TODO and assumed it was just a bit that wasn’t working yet. I don’t really understand what it is doing at the moment, but I’ll spend some time with it and see if I can digest it.</p>

---

## Post #4 by @pieper (2023-05-18 13:22 UTC)

<p>That’s good that you can investigate and report back what you find.  The <code>tags</code> argument should allow you to populate the headers with the needed values to make valid (or at least usable) dicom files.  Creating valid files for various modalities is tricky, and you may need to check them with a tool like <a href="https://dclunie.com/dicom3tools/dciodvfy.html"><code>dciodvfy</code></a> and make further tweaks, perhaps with pydicom, to make them work for your intended use.</p>

---
