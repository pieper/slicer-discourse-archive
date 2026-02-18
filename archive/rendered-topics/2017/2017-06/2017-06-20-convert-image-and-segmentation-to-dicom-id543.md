# Convert image and segmentation to DICOM

**Topic ID**: 543
**Date**: 2017-06-20
**URL**: https://discourse.slicer.org/t/convert-image-and-segmentation-to-dicom/543

---

## Post #1 by @Josiah_McAllister (2017-06-20 19:20 UTC)

<p>Andras,<br>
I am now trying to convert nrrd files to DICOM. The main image is<br>
converting just fine, but I am not able to figure out how to convert just<br>
the contour, as it does not show up when using “Create a DICOM series.” How<br>
can I also convert this file?</p>

---

## Post #2 by @gcsharp (2017-06-20 20:02 UTC)

<p>You are trying to convert nrrd files into a RT Structure Set using 3D Slicer?  By coincidence, I documented this procedure earlier today.</p>
<ol>
<li>Load all images. At time of load, click “Labelmap” checkbox for each structure</li>
<li>Go to Segmentation module</li>
<li>For “Active segmentation”, choose “Create new segmentation”</li>
<li>For each structure, repeat:<br>
4a) In “Export/Import segments”, choose structure, and import as labelmap</li>
<li>Click on one of the segments, and then click “Edit selected”</li>
<li>Set the “Master volume” to your CT</li>
<li>Go to Data module.</li>
<li>On background, right click choose “Create new subject”</li>
<li>On subject, right click choose “Create child study”</li>
<li>Drag the CT and segmentation node onto the child study</li>
<li>Right click on study, choose “Export to DICOM”</li>
<li>Enjoy your newly created DICOM-RT file</li>
</ol>

---

## Post #3 by @Josiah_McAllister (2017-06-20 20:18 UTC)

<p>When I am loading the images, I am not seeing a “Labelmap” checkbox.</p>

---

## Post #4 by @lassoan (2017-06-20 20:21 UTC)

<aside class="quote no-group" data-username="Josiah_McAllister" data-post="3" data-topic="543" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ccd318/48.png" class="avatar"> Josiah_McAllister:</div>
<blockquote>
<p>When I am loading the images, I am not seeing a “Labelmap” checkbox.</p>
</blockquote>
</aside>
<p>Click “Show options” in the Add data dialog.</p>
<p>If you already have your contours as segmentation you can start at step 7.</p>

---

## Post #5 by @Josiah_McAllister (2017-06-20 20:42 UTC)

<p>I am not seeing a “create new subject” option once I am in the data module,<br>
or any of the steps past 7.</p>

---

## Post #6 by @lassoan (2017-06-20 20:59 UTC)

<p>You should see this when you right-click in the big white empty area in the Subject hierarchy tab of Data module:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26329c81f4fffe173f793fbef785635420658222.png" data-download-href="/uploads/short-url/5rUzQDYLN3pKEPEex9uvkSBEBYS.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26329c81f4fffe173f793fbef785635420658222_2_274x500.png" alt="image" data-base62-sha1="5rUzQDYLN3pKEPEex9uvkSBEBYS" width="274" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/6/26329c81f4fffe173f793fbef785635420658222_2_274x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26329c81f4fffe173f793fbef785635420658222.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/26329c81f4fffe173f793fbef785635420658222.png 2x" data-dominant-color="F2F2F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">384×699 20.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Josiah_McAllister (2017-06-20 21:10 UTC)

<p>That is not what I have. I have version 4.6.2, so I’m not sure if that is<br>
where the difference is.</p>

---

## Post #8 by @lassoan (2017-06-20 21:12 UTC)

<p>4.6.2 is very old (almost a year). Use the latest nightly build.</p>

---

## Post #9 by @Josiah_McAllister (2017-06-21 15:04 UTC)

<p>When I click on export on the final step, nothing happens. Nothing shows up in the folder which I have selected, and the export window doesn’t change or go away.</p>

---

## Post #10 by @lassoan (2017-06-21 16:20 UTC)

<p>Please copy the complete application log (menu: Help / Report a bug). Scrub any patient info from the logs before posting.</p>

---

## Post #11 by @fedorov (2017-06-21 17:06 UTC)

<aside class="quote no-group" data-username="Josiah_McAllister" data-post="1" data-topic="543">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ccd318/48.png" class="avatar"> Josiah_McAllister:</div>
<blockquote>
<p>I am now trying to convert nrrd files to DICOM</p>
</blockquote>
</aside>
<p>There are very different ways to do this, and the approach will be different depending on your specific needs.</p>
<p>Can you explain why you want to convert these nrrd files to DICOM? What do you want to do next with those DICOM files?</p>

---

## Post #12 by @Josiah_McAllister (2017-06-21 18:15 UTC)

<p>It is to test if the files from pyradiomics will be able to run on some new<br>
code we have created. We are trying to verify that our code will correctly<br>
read the images.</p>

---

## Post #13 by @fedorov (2017-06-21 19:44 UTC)

<aside class="quote no-group" data-username="Josiah_McAllister" data-post="12" data-topic="543" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/ccd318/48.png" class="avatar"> Josiah_McAllister:</div>
<blockquote>
<p>It is to test if the files from pyradiomics will be able to run on some new<br>
code we have created. We are trying to verify that our code will correctly<br>
read the images.</p>
</blockquote>
</aside>
<p>I do not understand what you are trying to do. The output from pyradiomics is a table with numbers. pyradiomics does not produce any images.</p>

---

## Post #14 by @brhoom (2017-06-21 19:59 UTC)

<p>There is a plugin in Slicer called “Create a DICOM Series”</p>

---

## Post #15 by @Josiah_McAllister (2017-06-21 20:32 UTC)

<p>I am trying to get another system to output the same numbers as<br>
pyradiomics. However, that other system can only use DICOM images. This is<br>
to check that the other system is outputting the correct numbers.</p>

---

## Post #16 by @fedorov (2017-06-22 02:27 UTC)

<p>Ok, now I understand I think.</p>
<p>The simplest would be to just start with an image dataset that is already in DICOM and compute radiomics features using both tools.</p>

---

## Post #17 by @lassoan (2020-10-10 00:32 UTC)

<p>A post was split to a new topic: <a href="/t/export-segmentation-as-dicom/13970">Export segmentation as DICOM</a></p>

---

## Post #18 by @lassoan (2020-10-10 00:31 UTC)

<p>A post was split to a new topic: <a href="/t/use-segmentation-for-radiomics/13969">Use segmentation for radiomics</a></p>

---
