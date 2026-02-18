# 3D ultrasound DICOM import error: 'Reference image in series does not contain geometry information. Please use caution.'

**Topic ID**: 3790
**Date**: 2018-08-16
**URL**: https://discourse.slicer.org/t/3d-ultrasound-dicom-import-error-reference-image-in-series-does-not-contain-geometry-information-please-use-caution/3790

---

## Post #1 by @kylemcclanahan (2018-08-16 05:53 UTC)

<p>Hi,<br>
New Slicer user here.</p>
<p>When trying to Load DICOM images, I receive the above error. When the prompt appears (Do you want to try loading anyway?), and I click yes, I get the following error:</p>
<p>“Could not load: 1: Unnamed series as a scalar volume”</p>
<p>I have found a workaround to get the image loaded into the first pane of Slicer (going to top left and clicking the ‘DATA’ icon with the green arrow pointing up), but once the image is loaded, I go to Volume Rendering &gt; then I select the correct VOlume (only one), and click the eye icon to the left of the Volume name. I have done this using other sample DCM images of the same format, and I was able to see and start editing the Display Presets, etc. I was even able to export it, and get it into an STL format ready for 3d printing (we’re 3d printing fetuses if you couldn’t tell lol).</p>
<p>The issue, is after I click the eye icon, the program hangs for about 5 seconds, then completely crashes. I checked the error logs but I don’t understand enough about this program to begin troubleshooting.</p>
<p>Both the Stable release, as well as the Nightly Build (downloaded today, 8/15/18) act exactly the same way through all of the above. I have noticed 0 differences between the two builds.</p>
<p>I’m going to try to upload screenshots, as I want to provide as much info as possible, in hopes that someone (much more knowledgeable than I) could help me out!<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df83424e7c2e2e833abe75a482228adaecc5edb9.png" alt="b-phase4" data-base62-sha1="vThHdqGPqU09LadBJWtiJWAUNTz" width="672" height="493"></p>
<p>The photos are labeled: phase1,2,3, and b-phase1,2,etc.</p>
<p>I’m sure someone will know what I was doing or how I got there better than I.</p>
<p>Again, please help!<br>
And thank you in advance <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>-Kyle</p>

---

## Post #2 by @ezproxy (2018-08-16 06:36 UTC)

<p>胎儿超声 数据立体化</p>
<p>ultrasound data three-dimensional</p>

---

## Post #3 by @pieper (2018-08-16 12:01 UTC)

<p>It looks like you’ve loaded a screenshot (dicom calls this a ‘secondary capture’) which is why there’s no geometry information for 3D operations.</p>

---

## Post #4 by @kylemcclanahan (2018-08-16 17:26 UTC)

<p>Can you please elaborate?</p>

---

## Post #6 by @kylemcclanahan (2018-08-16 17:33 UTC)

<p>Pardon the ignorance, but I’m not sure how to interpret that. There are only two options on our machine to export as ‘DICOM (dcm)’ or ‘DICOM and DICOM DIR’. I have tried both. Here is a download link for my <a href="https://files.fm/u/hav5d94n" rel="nofollow noopener">Dicom Directory</a> used in this issue. They load as volumes, hence my confusion.<br>
Any help would be appreciated!</p>

---

## Post #7 by @lassoan (2018-08-20 21:14 UTC)

<p>Sorry for the delayed response, I’m just back from vacation. This ultrasound volume is a GE Kretzfile image, which can be loaded into Slicer:</p>
<ul>
<li>install SlicerHeart extension and restart Slicer</li>
<li>delete DICOMDIR file from the folder where you want to import DICOM images from</li>
<li>drag-and-drop the folder to Slicer application window and choose to import the folder into DICOM database</li>
<li>switch to DICOM module</li>
<li>check “Advanced” checkbox</li>
<li>click “Examine” button</li>
<li>check the checkbox in the row of <em>US…</em>, <em>US … (LR)</em>, or <em>US … (HR)</em> in the table at the bottom (for normal, low, or high resolution import)</li>
<li>click “Load” button</li>
</ul>
<p>I’ve pushed a change to SlicerHeart extension to simplify loading in the future, by automatically recognizing this file type (it was not recognized before because the manufacturer name in the DICOM header was not the usual value).</p>
<p>Tips for processing the data set:</p>
<ul>
<li>Pre-processing: create a new segment, segment bright areas of the volume using Threshold effect, remove irrelevant parts from the segmentation (noisy areas, reflections, etc. will be removed, only the skin surface will remain) using Scissors effect.</li>
<li>This pre-processed segment can be exported for 3D printing as is.</li>
<li>You can use this segment as a mask for 3D visualization using volume rendering: Save the scene, install “SegmentEditorExtraEffects” extension, restart Slicer, load the saved scene. Make the segment a bit larger by using Margin effect (3mm growing should work). Use Mask volume to create a masked volume (where areas outside the segment are set to 0). Go to Volume rendering module, select the masked volume, choose MR-Default preset, click eye icon, adjust Shift slider.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d72a93046eed590af894510a2b29ce4a54fc4097.jpeg" data-download-href="/uploads/short-url/uHrS0DJFB04oE0gypYCD0078w5N.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d72a93046eed590af894510a2b29ce4a54fc4097_2_690x469.jpeg" alt="image" data-base62-sha1="uHrS0DJFB04oE0gypYCD0078w5N" width="690" height="469" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d72a93046eed590af894510a2b29ce4a54fc4097_2_690x469.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d72a93046eed590af894510a2b29ce4a54fc4097_2_1035x703.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d72a93046eed590af894510a2b29ce4a54fc4097.jpeg 2x" data-dominant-color="9E9C9E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1260×857 264 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @kylemcclanahan (2018-08-20 22:48 UTC)

<p>You sir, are a Wizard.</p>
<p>I made it as far as the ‘Tips for processing the data set:’ and I got lost. (I’m sure the instructions are super easy for someone who has a general understanding of all of this imaging stuff (I’m a Systems Administrator (seemingly) in over my head trying to find a solution for a client). Any chance you could ‘dumb down’ the Tips for me? Again, apologies for the ignorance here. I’m a total rookie.</p>

---

## Post #9 by @lassoan (2018-08-21 10:55 UTC)

<p>For processing the data set, you may need to learn a bit about image segmentation. Completing these tutorials should help: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation">https://www.slicer.org/wiki/Documentation/Nightly/Training#Slicer4_Image_Segmentation</a></p>

---

## Post #10 by @eddyogi (2018-12-07 14:54 UTC)

<p>Good day.<br>
I’m getting this error too.  I’m using the newest release, 4.10.  I tried the suggestion to install SlicerHeart but it still didn’t work.  The only way I was able to load the file was by using the Data icon like what kylemcclanahan described.  After the file is loaded, I try volume rendering but the output looks horrible (please see attached screen shot).<br>
What am I doing wrong?  Was the dicom file not saved correctly?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce897da7f2728b439205790aa9c9d89b77003fa7.jpeg" data-download-href="/uploads/short-url/tt6VLp6PNt2L4gEeygqTGr8MJdJ.jpeg?dl=1" title="32%20am" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce897da7f2728b439205790aa9c9d89b77003fa7_2_690x431.jpeg" alt="32%20am" data-base62-sha1="tt6VLp6PNt2L4gEeygqTGr8MJdJ" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce897da7f2728b439205790aa9c9d89b77003fa7_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/e/ce897da7f2728b439205790aa9c9d89b77003fa7_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce897da7f2728b439205790aa9c9d89b77003fa7.jpeg 2x" data-dominant-color="74888B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">32%20am</span><span class="informations">1280×800 207 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @lassoan (2019-04-08 19:49 UTC)

<p>3 posts were split to a new topic: <a href="/t/dicom-import-error-of-image-modality-ot-other-reference-image-in-series-does-not-contain-geometry-information/6440">DICOM import error of image modality OT (“other”): ‘Reference image in series does not contain geometry information.’</a></p>

---

## Post #12 by @Fullcalf42 (2022-12-29 19:14 UTC)

<p>I tried loading ultrasound dcm files last night for the first time. I could only see one image of the entire volume in the red view (conventional widescreen). Though there are many files in the data set, only the red view as an image and it is just a single image. If I try to scrub through the frames everything else is blank when the indicator is scrubbed to the left or right of center.</p>
<p>One error I was getting while loading the patient data was ‘Structured Report Objects’ and advised me to install ‘QuantitativeReporting’ extension, so I did but nothing changed.</p>
<p>This morning I updated Slicer to 5.2. Still the same issue. Is there a recommended extension pack to help me load these ultrasounds? I am trying to visualize an ovarian cyst.</p>

---
