# Importing segmentation into 3d slicer

**Topic ID**: 7080
**Date**: 2019-06-08
**URL**: https://discourse.slicer.org/t/importing-segmentation-into-3d-slicer/7080

---

## Post #1 by @tenzin_kunkyab (2019-06-08 00:44 UTC)

<p>Hi,</p>
<p>I am Tenzin. I would like to ask about a problem I am having.</p>
<p>I did some segmentation on ITK snap and exported into nrrd format file. when I imported that into 3d slicer against a same volume, the segmentation is in a different place.</p>
<p>any idea on how to fix it or why it happens?</p>
<p>best<br>
Tenzin</p>

---

## Post #2 by @lassoan (2019-06-08 01:09 UTC)

<p>Both Slicer and ITK-snap saves images in physical coordinate system, so there should not be any misalignment.</p>
<p>Can you attach a screenshot?</p>
<p>How did you import the segmentation?</p>
<p>How did you load the grayscale volume? From DICOM or other file format?</p>

---

## Post #3 by @tenzin_kunkyab (2019-06-10 19:19 UTC)

<p>Hi Lassoan, I would like to upload the snapshot here. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4fe84a723d87960e3d7dcc4ac62c142a93fd6ab4.png" alt="Capture2" data-base62-sha1="boToR8MtffFmsu2RhVHYaqiBk4Q" width="507" height="394"></p>
<p>And then I went to 3d slicer, dragged the file and uploaded as segmentation.</p>
<p>I loaded the grayscale volume in 3d slicer (just by doing load data) and the files are in dicom. Am I meant to be uploading the file as dicom? (that takes a very long time in 3d slicer to load).</p>
<p>best<br>
Tenzin</p>

---

## Post #4 by @tenzin_kunkyab (2019-06-10 19:30 UTC)

<p>Hi Lassoan,</p>
<p>actually I was able to do it correctly, seems like the volume that I used was wrong. I apologize.</p>
<p>furthermore I would like to ask an additional question, if I want to edit the segmentation in segment editor on 3d slicer (segmentation saved using ITK snap), how can I do that?</p>
<p>best<br>
Tenzin</p>

---

## Post #5 by @Leon (2019-06-11 10:02 UTC)

<p>We more or less have the same problem. For our study we need a surface-mesh from a segmentation that was already done in Mimics.<br>
Strangely enough Mimics doesn’t give you the possibility  to make a real surface-mesh (it always does some sort of smoothing), so I exported the segmentation as a dicomserie and then imported the dicoms into Slicer.<br>
Then I segmented the included Mimics-mask by choosing the proper theshold values. After that I saved the segmentation as an STL without smoothing.</p>
<p>But now, when I import the Slicer-stl back into Mimics, the resulting mask (in red) is offset by about halve the voxelheight in the Z-direction (see screenshot).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21652f1b3aa061680a6388de7384169f9523d848.png" data-download-href="/uploads/short-url/4LqxCsSM886cBByW9eqgUCcBIEg.png?dl=1" title="Screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21652f1b3aa061680a6388de7384169f9523d848.png" alt="Screenshot" data-base62-sha1="4LqxCsSM886cBByW9eqgUCcBIEg" width="611" height="500" data-dominant-color="62593F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot</span><span class="informations">705×576 5.54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>For our study it’s very important that the STL is exactly in the same coördinate system as the dicom!</p>
<p>We discussed this problem and the only thing we came up with for now is that it might be caused by where the application (Mimics, Slicer, …) defines the position of the Z-coördinate; at the top, in the middle or at the bottom of the voxel.<br>
I don’t believe that that will be the case, because I think there are fixed rules for this in the dicom parameters. But we haved got a clue.</p>
<p>Who gave help us in this?</p>

---

## Post #6 by @pieper (2019-06-11 11:53 UTC)

<p>We can’t really debug Mimics here, but if you find any inconsistencies in the way Slicer handles coordinates please do let us know.</p>
<p>Best thing I can suggest is to create some very controlled examples (like a test pattern) and carefully go through each step in the pipeline to look for inconsistencies.</p>

---

## Post #7 by @Leon (2019-06-11 13:20 UTC)

<p>Hello Steve,</p>
<p>I’m not asking to debug Mimics (actually I want to stop using it) but I would like to know what causes this issue. Is it due to how segmentation application handle the dicom coördinates or is there another possible cause for this?</p>
<p>I already found out that the mask has exactly half the voxelheight of (slice thickness is 3mm)</p>

---

## Post #8 by @lassoan (2019-06-11 13:43 UTC)

<aside class="quote no-group" data-username="Leon" data-post="5" data-topic="7080">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar"> Leon:</div>
<blockquote>
<p>I exported the segmentation as a dicomserie</p>
</blockquote>
</aside>
<p>What information object did you use (RTSTRUCT, segmentation, …)?</p>
<p>Can you share with us a sample input image (use a phantom or a publicly available sample data set) and exported segmentation?</p>

---

## Post #9 by @Leon (2019-06-11 14:28 UTC)

<p>Sorry lassoan, but I have no idea what you mean by RTSTRUCT. In Mimics I just use the export the segmentation within the dicom files and then in Slicer resegment them. How the exporting is done, they don’t tell you.</p>
<p>I also can’t give you the sample data for patiënt privacy reasons.</p>
<p>But can you tell what protocol dicom uses for x,y,z? Are there fixed rules for where x, y and z are defined (for instance within the same plane), or can it be that, depending the CT-scanner, the z can be of plane?</p>

---

## Post #10 by @lassoan (2019-06-11 15:24 UTC)

<aside class="quote no-group" data-username="Leon" data-post="9" data-topic="7080">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar"> Leon:</div>
<blockquote>
<p>I also can’t give you the sample data for patiënt privacy reasons.</p>
</blockquote>
</aside>
<p>Please download a DICOM volume from anywhere (e.g., <a href="https://www.cancerimagingarchive.net/">TCIA</a>) and use that for these tests so that you can freely share the results.</p>
<aside class="quote no-group" data-username="Leon" data-post="9" data-topic="7080">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/leon/48/1468_2.png" class="avatar"> Leon:</div>
<blockquote>
<p>But can you tell what protocol dicom uses for x,y,z? Are there fixed rules for where x, y and z are defined (for instance within the same plane), or can it be that, depending the CT-scanner, the z can be of plane?</p>
</blockquote>
</aside>
<p>According to [DICOM standard],(<a href="http://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.2.html#sect_C.7.6.2.1.1" class="inline-onebox">C.7.6.2&nbsp;Image Plane Module</a>) slice position corresponds to center of the voxel: <em>Image Position (0020,0032) specifies the x, y, and z coordinates of the upper left hand corner of the image; it is the center of the first voxel transmitted.</em></p>

---

## Post #11 by @Leon (2019-06-12 07:33 UTC)

<p>Thanks for the information on the dicom coördinates. That was very helpfull.</p>
<p>In the meantime I’ve found what went wrong. It was caused by the fact that the segmentation was done in an older version of Mimics (version 14) and since version 16 they’ve updated their coördinate system.</p>
<p>So thumbs up for Slicer <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=9" title=":+1:" class="emoji" alt=":+1:"> and another reason for me to avoid Mimics <img src="https://emoji.discourse-cdn.com/twitter/unamused.png?v=9" title=":unamused:" class="emoji" alt=":unamused:"> !</p>

---
