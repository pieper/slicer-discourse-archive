---
topic_id: 33096
title: "Visualize Tracked Ultrasound In 3D With Png Images And Pose"
date: 2023-11-28
url: https://discourse.slicer.org/t/33096
---

# Visualize tracked ultrasound in 3D with PNG images and pose matrices

**Topic ID**: 33096
**Date**: 2023-11-28
**URL**: https://discourse.slicer.org/t/visualize-tracked-ultrasound-in-3d-with-png-images-and-pose-matrices/33096

---

## Post #1 by @ziri (2023-11-28 19:42 UTC)

<p>Hi, I’m trying to create a sequence file from a folder of ultrasound images in png format with poses stored in a csv file and then visualize in 3D.<br>
I successfully created the .mhd header file containing the pose information and the poses can be visualized in Slicer. The file “Scan1.seq.mhd” looks like below:</p>
<blockquote>
<p>ObjectType = Image<br>
NDims = 3<br>
AnatomicalOrientation = RAI<br>
BinaryData = True<br>
BinaryDataByteOrderMSB = False<br>
CenterOfRotation = 0 0 0<br>
CompressedData = False<br>
ElementSpacing = 1 1 1<br>
Offset = 0 0 0<br>
TransformMatrix = 1 0 0 0 1 0 0 0 1<br>
UltrasoundImageOrientation = MFA<br>
UltrasoundImageType = BRIGHTNESS<br>
Seq_Frame0000_ImageToReferenceTransform = 0.25880223 -0.96586309 0.01139754 99.35319738 -0.00294990 0.01100917 0.99993505 19.23409344 -0.96592583 -0.25881905 0.00000000 4.28620653 0.00000000 0.00000000 0.00000000 1.00000000<br>
Seq_Frame0000_ImageToReferenceTransformStatus = OK<br>
Seq_Frame0000_Timestamp = 0.000<br>
Seq_Frame0000_ImageStatus = OK<br>
Seq_Frame0001_ImageToReferenceTransform = 0.25868718 -0.96543371 0.03191713 99.30936271 -0.00826076 0.03082958 0.99949052 18.11578949 -0.96592583 -0.25881905 0.00000000 4.28620653 0.00000000 0.00000000 0.00000000 1.00000000<br>
Seq_Frame0001_ImageToReferenceTransformStatus = OK<br>
Seq_Frame0001_Timestamp = 0.300<br>
Seq_Frame0001_ImageStatus = OK<br>
Seq_Frame0002_ImageToReferenceTransform = 0.25844698 -0.96453726 0.05360077 99.21784580 -0.01387290 0.05177437 0.99856245 16.90844963 -0.96592583 -0.25881905 -0.00000000 4.28620653 0.00000000 0.00000000 0.00000000 1.00000000<br>
Seq_Frame0002_ImageToReferenceTransformStatus = OK<br>
Seq_Frame0002_Timestamp = 0.600<br>
Seq_Frame0002_ImageStatus = OK<br>
Seq_Frame0003_ImageToReferenceTransform = 0.25810672 -0.96326738 0.07414098 99.08820620 -0.01918910 0.07161468 0.99724777 15.78648773 -0.96592583 -0.25881905 -0.00000000 4.28620653 0.00000000 0.00000000 0.00000000 1.00000000<br>
Seq_Frame0003_ImageToReferenceTransformStatus = OK<br>
Seq_Frame0003_Timestamp = 0.900<br>
Seq_Frame0003_ImageStatus = OK<br>
…<br>
ElementDataFile = Scan1.seq.nrrd</p>
</blockquote>
<p>However, when I load this file into slicer as Sequence Metafile, it cannot pull the image data into the Slicer even though the Scan1.seq.nrrd file is under same directory as the .mhd metafile. I created the “Scan1.seq.nrrd” by opening the folder containing png images in slicer as volume, and save it as .nrrd file. I wonder if I should convert the png images into raw data file in a different way?</p>
<p>Also I wonder if I should set the ultrasound image spacing parameter in .mhd file? E.g., if my pixel spacing is 0.27mm, should I change the ElementSpacing = 0.27 0.27 0.27?</p>
<p>I appreciate any help!</p>

---

## Post #2 by @ziri (2023-11-29 03:39 UTC)

<p>Update: I’m still struggling on creating the sequence file correctly, but here is what I have tried so far</p>
<p><strong>Attempt 1: Using the MultiVolume Importer</strong><br>
I tried to use the MultiVolume Importer to open the folder containing my png ultrasound images, and save the MultiVolume node as an nrrd file. Then I load the file in Slicer as Sequence, the result looks good (as shown below).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/347ca644958d32922db5cc5ecab0419ef4f4d86e.png" data-download-href="/uploads/short-url/7ujT6mi0z4zHWO6mtJqzVt39Onc.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/347ca644958d32922db5cc5ecab0419ef4f4d86e_2_517x281.png" alt="image" data-base62-sha1="7ujT6mi0z4zHWO6mtJqzVt39Onc" width="517" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/347ca644958d32922db5cc5ecab0419ef4f4d86e_2_517x281.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/4/347ca644958d32922db5cc5ecab0419ef4f4d86e_2_775x421.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/4/347ca644958d32922db5cc5ecab0419ef4f4d86e.png 2x" data-dominant-color="707078"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">849×462 63 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, if I tried to load the <a href="https://www.dropbox.com/scl/fi/9mlukkkel6d5hfd0676tz/Scan1.seq.nrrd?rlkey=j4fd3rxueam21z95jfr4nwhza&amp;dl=0" rel="noopener nofollow ugc">nrrd file</a> (contains all my images) with my custom <a href="https://www.dropbox.com/scl/fi/35cnf9fdtpbn5vtoc5ir6/Scan1.seq.mhd?rlkey=6qlu189ofmgont9b14tk5ygdr&amp;dl=0" rel="noopener nofollow ugc">mhd file</a>, it will not show the data at all. I’m attaching both files in the links.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa20db6079c61c1b25f1a65e774e7a1e4a2b7960.png" alt="image" data-base62-sha1="zGJLk3NE794xkDrinNXuQJwLGfK" width="481" height="261"></p>
<p>If I open up the nrrd file in text editor, I see it actually contains a header saying the dimension is 4, which violates the <a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/FileSequenceFile.html" rel="noopener nofollow ugc">Sequence file rule</a> of NDims=3.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4eeb48537a207f2a49e8a9e2ad0299168c4cbc0a.png" alt="image" data-base62-sha1="bg9kEJujblLhrWTwmRahLGplQCu" width="448" height="196"></p>
<p><strong>Attempt 2: Creating binary file using numpy array</strong><br>
So I tried to read every image into python and generate the numpy array (dtype=uint8) with size 660 x 616 x 417 (width x height x frames), then save the array into binary file and try to load it with the mhd file again. This time it shows noisy data which looks confusing.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9d2f3ca0622e209d2c14ab19092138684c1e54c.png" data-download-href="/uploads/short-url/qvSiiXnPa5N9VL5v4hPiSuNFA96.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9d2f3ca0622e209d2c14ab19092138684c1e54c_2_517x281.png" alt="image" data-base62-sha1="qvSiiXnPa5N9VL5v4hPiSuNFA96" width="517" height="281" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9d2f3ca0622e209d2c14ab19092138684c1e54c_2_517x281.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9d2f3ca0622e209d2c14ab19092138684c1e54c_2_775x421.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9d2f3ca0622e209d2c14ab19092138684c1e54c.png 2x" data-dominant-color="7F7F87"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">975×530 71.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Can I get any advice on creating a custom sequence file from stored images? Thank you in advance!</p>

---
