---
topic_id: 9879
title: "Tutorial For Newb Idiot"
date: 2020-01-20
url: https://discourse.slicer.org/t/9879
---

# Tutorial for newb idiot?

**Topic ID**: 9879
**Date**: 2020-01-20
**URL**: https://discourse.slicer.org/t/tutorial-for-newb-idiot/9879

---

## Post #1 by @Thomas_Watson (2020-01-20 08:59 UTC)

<p>Hey all.  Newb idiot here.</p>
<p>I just got a 3d printer.  I’m also the fortunate recipient of nearly a dozen MRI’s on many body parts over the years due to injuries and orthopedic anomolies.</p>
<p>I’ve always wondered how I could model my joints or other parts (brain) w/ MRI images, and stumbled across SLICER.   I’m too incompetent to figure out how to use it with any tutorials I’ve found so far.  Can anyone point me int he right direction?</p>
<p>I’ve got several drives w/ MRI data on them.  Specifically, a DICOM folder which contain the image data, from what I can tell.</p>

---

## Post #2 by @manjula (2020-01-20 20:03 UTC)

<p>Hi,</p>
<p>I think you can have a look at,</p>
<div class="lazyYT" data-youtube-id="MKLWzD0PiIc" data-youtube-title="Tutorial: Preparing Data for 3D Printing Using 3D Slicer" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #3 by @Juicy (2020-01-20 20:21 UTC)

<p>At least to get you started…</p>
<p>If you have a DICOM MRI data set you should have a folder which contains a series of files. These files will just kind of look blank in windows explorer because no windows programs will recognise these.</p>
<p>First open 3d Slicer and then simply drag and drop the folder which contains the DICOM images from the windows explorer window into the 3d slicer window. Slicer will now have a pop up box saying something like “Load into DICOM database” click yes.</p>
<p>Now click the DCM button in the top left corner of the slicer window. A pop up window will now pop up or the options will open in the module GUI area (depending on what version of slicer you have) highlight the scan you want to load from the list and press the load button.</p>
<p>You should now see the image volume displayed in the red (top view) green (front view) and yellow (side view) windows. If you cant see the red green and yellow windows then change through the different options in the view selector button on the top toolbar. Four up works well for most things I do.</p>
<p>Segmenting joints etc from MRI images is quite an advanced topic. Do you have any CT images instead? These are much easier to turn into 3d printable models for a beginner. There is a good blog entry here on <a href="https://www.embodi3d.com/blogs/entry/373-how-to-easily-tell-the-difference-between-mri-and-ct-scan/" rel="nofollow noopener">how to distinguish between CT and MRI</a></p>

---
