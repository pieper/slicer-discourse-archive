# Rename nodes with python script

**Topic ID**: 33385
**Date**: 2023-12-14
**URL**: https://discourse.slicer.org/t/rename-nodes-with-python-script/33385

---

## Post #1 by @JamesM (2023-12-14 00:44 UTC)

<p>Hello. I have a question. Currently, I am loading more than 10 MRI series per patient, each acquired on different dates, and measuring volumes. However, the node names are inconsistent, and I would like to rename them in chronological order using the date information from DICOM files. I believe I can achieve this by accessing the Python script. Could you provide how to approach this? I’ve also searched through Python script repositories but couldn’t find a solution.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4daf40905c5c5703b7ea735bda0d670255d53912.png" data-download-href="/uploads/short-url/b5eeXHrzeZvXp27aCm4JUDfNCmu.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4daf40905c5c5703b7ea735bda0d670255d53912_2_690x359.png" alt="image" data-base62-sha1="b5eeXHrzeZvXp27aCm4JUDfNCmu" width="690" height="359" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4daf40905c5c5703b7ea735bda0d670255d53912_2_690x359.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4daf40905c5c5703b7ea735bda0d670255d53912_2_1035x538.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/d/4daf40905c5c5703b7ea735bda0d670255d53912_2_1380x718.png 2x" data-dominant-color="DDE9F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1917×999 92.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2023-12-14 00:51 UTC)

<p>You can do something like this example:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#batch-processing" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#batch-processing</a></p>
<p>Iterate through the studies for the patient and query the StudyData using the <code>slicer.dicomDatabase.fileValue</code> method to get the data to sort the data.  You can load the series you want and use SetName to provide a consistent convention.  You may need some special case code to deal with the variability in clinical naming conventions.</p>

---

## Post #3 by @JamesM (2023-12-14 01:29 UTC)

<p>Thanks for the quick response. I have one more question. Can I perform 3D Slicer tasks using Spyder with Python? I want to use Spyder instead of the Python console.</p>

---

## Post #4 by @pieper (2023-12-15 13:08 UTC)

<p>People have done things like that - you can search for it.  I didn’t find it worth the effort but if you have good luck please report back.</p>

---
