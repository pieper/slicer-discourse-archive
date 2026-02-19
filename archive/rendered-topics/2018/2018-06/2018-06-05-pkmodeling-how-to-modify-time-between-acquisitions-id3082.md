---
topic_id: 3082
title: "Pkmodeling How To Modify Time Between Acquisitions"
date: 2018-06-05
url: https://discourse.slicer.org/t/3082
---

# Pkmodeling: How to modify time between acquisitions

**Topic ID**: 3082
**Date**: 2018-06-05
**URL**: https://discourse.slicer.org/t/pkmodeling-how-to-modify-time-between-acquisitions/3082

---

## Post #1 by @bmb777 (2018-06-05 21:48 UTC)

<p>I am currently using the DICOM browser to import a image set with 70 time points/acquisitions that are separated by ~19 seconds, however the software appears to be interpreting the acquisitions as being separated by 10 ms (which I believe corresponds to the TR). Once the DICOM data has been loaded the file name says sorted by Imagepositionpatient+Instancenumber which may be the cause of the misreading of the acquisition time frame. I was wondering the best way to manually correct this?</p>

---

## Post #2 by @fedorov (2018-06-05 22:05 UTC)

<p><a class="mention" href="/u/bmb777">@bmb777</a> there is currently no interface in the GUI for this, but it is easy to do:</p>
<ol>
<li>import and load the DCE series as a multivolume into Slicer using DICOM Browser. To make sure it is loaded as a multivolume, you can toggle “Advanced” view in the DICOM Browser and see something like this after you examine the dataset:</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66cf68dab83a534e0f96120dce62776c981c5abd.png" alt="image" data-base62-sha1="eFv4EdcSNNuy28CUsjwUcVUdOgt" width="659" height="192"></p>
<ol start="2">
<li>
<p>save the loaded multivolume as a .nhdr file using “Save data” option:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac0035fcf4c960a92768cf70979c369cdd38d286.png" alt="image" data-base62-sha1="oxAzL1uxPDLcx88JNNAQOvhGCDs" width="539" height="284"></p>
</li>
<li>
<p>open the .nhdr file in a text editor, you will see the following item in the header that contains time stamps for the individual temporal frames:</p>
</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87f781b66e2cfc0922fae14ec862c09c53e7cb89.png" data-download-href="/uploads/short-url/joOJPhHh7jUPop6ctcJRqHkA0fD.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87f781b66e2cfc0922fae14ec862c09c53e7cb89.png" alt="image" data-base62-sha1="joOJPhHh7jUPop6ctcJRqHkA0fD" width="690" height="137" data-dominant-color="728393"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">733×146 19.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="4">
<li>update those time stamps with the proper temporal resolution (make sure timestamps are in milliseconds, since this is what PkModeling expects!), you can conveniently make that string as follows:</li>
</ol>
<pre data-code-wrap="python"><code class="lang-python">for i in numpy.arange(0,19000*70,19000): print("%d," % i, end='')
</code></pre>
<ol start="5">
<li>load the updated .nhdr file into Slicer, it should now show the updated temporal resolution.</li>
</ol>
<p>Let us know if this resolves the problem for you.</p>
<p>Also, if you can suggest a generic strategy how the proper temporal resolution could be populated for this dataset from the content of the existing DICOM attributes, this would be extremely helpful!</p>

---

## Post #3 by @bmb777 (2018-06-06 18:43 UTC)

<p>This resolves the issue, thanks. As for a strategy to correct this, I emailed the MRI technician to determine if the information needed is present in the DICOM attributes and will update this post when he responds.</p>

---
