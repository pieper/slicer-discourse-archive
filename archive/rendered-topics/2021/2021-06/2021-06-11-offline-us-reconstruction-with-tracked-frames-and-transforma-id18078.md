---
topic_id: 18078
title: "Offline Us Reconstruction With Tracked Frames And Transforma"
date: 2021-06-11
url: https://discourse.slicer.org/t/18078
---

# Offline US reconstruction with tracked frames and transformation matrix

**Topic ID**: 18078
**Date**: 2021-06-11
**URL**: https://discourse.slicer.org/t/offline-us-reconstruction-with-tracked-frames-and-transformation-matrix/18078

---

## Post #1 by @Qianqian_Cai (2021-06-11 12:13 UTC)

<p>I am working on the spatial calibration method for freehand ultrasound and would like verify the method by reconstructing the volume offline with the frames + tracked pose data + my derived calibration matrix.</p>
<p>I went through tutorials U-33 (Ultrasound volume reconstruction – offline) and realized I need a config file and a mha file for tracked frames.</p>
<p>My question is how to create my own config file with my 4*4 transformation matrix and how to create the mha file with the US frames in .png and the corresponding tracking data in .csv?</p>
<p>I am still looking for relevant info from the community and the documentation. But any experience related with creating the required xml and mha can help to facilitate my progress. Thanks in advance!</p>

---

## Post #2 by @lassoan (2021-06-11 20:59 UTC)

<p>Here is a complete example, with a set of input files and corresponding command-line arguments.</p>
<p>You can create an mhd file by loading the png stack into 3D Slicer and saving it as a .mhd file. I would recommend using mhd instead of mha because it is easier to add metadata (the mhd text header and the binary pixel data are stored in two separate files).</p>

---

## Post #4 by @Qianqian_Cai (2021-06-14 16:10 UTC)

<p>Thank you for the reply! I am trying to create the .mhd file. But do you have a link for the mentioned complete example? I believe that will be very helpful!</p>

---

## Post #5 by @lassoan (2021-06-14 18:10 UTC)

<p>The example is in the Volume reconstruction tool’s documentation page: <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/ApplicationVolumeReconstructor.html" class="inline-onebox">Plus applications user manual: Volume reconstructor application (VolumeReconstructor)</a></p>

---

## Post #6 by @Qianqian_Cai (2021-07-01 02:31 UTC)

<p>I learnt that .mhd file stores the text header in a sperate .raw file and save the binary pixel data in the .mhd file. But what kinds of information should be write into the text header?</p>
<p>For example, if I have 10 successive frames. Should I just writing a 10 by 6 position data related with each frame? Or should I add additional info such as the transformation matrix, or something else?</p>

---

## Post #7 by @lassoan (2021-07-01 03:18 UTC)

<p>See the specification in <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/FileSequenceFile.html">Plus Toolkit User Manual</a>. You can find lots of example files <a href="https://github.com/PlusToolkit/PlusLibData/tree/master/TestImages">here</a>.</p>

---

## Post #8 by @Qianqian_Cai (2021-07-02 02:55 UTC)

<p>Hi,</p>
<p>I am trying to write the .mha file with the provided MatLab code. I think I am stopped at the “element spacing”. What does that mean? I find a similar attribute in the sample data, which is called PixelDimensions. Do these two both mean the actual distance between pixel and pixel? If so, how can it be a 1-by-3 vector instead of 1-by-2?</p>

---

## Post #9 by @lassoan (2021-07-02 03:31 UTC)

<aside class="quote no-group" data-username="Qianqian_Cai" data-post="8" data-topic="18078">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/qianqian_cai/48/11008_2.png" class="avatar"> Qianqian_Cai:</div>
<blockquote>
<p>I think I am stopped at the “element spacing”. What does that mean?</p>
</blockquote>
</aside>
<p>See the documentation page that I linked above:</p>
<blockquote>
<p>ElementSpacing: Used by the MetaIO image file format to store the point around the image is rotated. This field is not used by Plus and kept only for compatibility with other software, as the spacing is defined per frame. Typical value is 1 1 1.</p>
</blockquote>
<aside class="quote no-group" data-username="Qianqian_Cai" data-post="8" data-topic="18078">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/qianqian_cai/48/11008_2.png" class="avatar"> Qianqian_Cai:</div>
<blockquote>
<p>If so, how can it be a 1-by-3 vector instead of 1-by-2?</p>
</blockquote>
</aside>
<p>An image is always a 3D object, defined in 3D space, even if it contains just a single slice.</p>
<p>If someone defined the image in 2D, then the transformation from world to image space would become a projection matrix. Projection matrices are non-invertible, therefore you would lose the ability to automatically compute transforms between any two coordinate systems.</p>

---

## Post #10 by @Qianqian_Cai (2021-10-01 19:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="18078">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can create an mhd file by loading the png stack into 3D Slicer and saving it as a .mhd file.</p>
</blockquote>
</aside>
<p>Hi,</p>
<p>I was able to load sequence of PNG files as a 3D volume into 3D Slicer following the example video on YouTube. But how do I add the motion sequence corresponding to the image sequence and 4-by-4 calibration matrix as the metadata? I have the motion sequence in excel and the calibration matrix in .txt.</p>
<p>Once the metadata and the images are saved in the mha file, I believe I can finish the volume reconstruction and rendering follow the complete example of Volume reconstructor application (VolumeReconstructor). Thanks!</p>
<p>Best regards,<br>
Qianqian</p>

---

## Post #11 by @lassoan (2021-10-01 22:15 UTC)

<p>You can convert the png stack to grayscale, save as .mhd or .nhdr file format (MetaImage or NRRD files with separate text file for header and raw file for pixel data), and then add the transforms from your excel file to the header file in <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/FileSequenceFile.html">this format</a>. You can find lots of example files <a href="https://github.com/PlusToolkit/PlusLibData/tree/master/TestImages">here</a>.</p>

---
