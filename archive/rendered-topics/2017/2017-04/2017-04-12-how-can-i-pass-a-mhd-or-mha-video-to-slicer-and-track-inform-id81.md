# How can I pass a .mhd or .mha video to Slicer and track information from the camera?

**Topic ID**: 81
**Date**: 2017-04-12
**URL**: https://discourse.slicer.org/t/how-can-i-pass-a-mhd-or-mha-video-to-slicer-and-track-information-from-the-camera/81

---

## Post #1 by @f.cnunez (2017-04-12 09:03 UTC)

<p>Hi,<br>
I’m new to Slicer and I’m trying to pass a .mha video to Slicer obtained with ORB-Slam2 (and the track information) using Plus application and OpenIGTLink in Slicer. I create the .mha video using a set of .png images with ImageJ but when I try to launch the server, it fails because the .mha file doesn’t have the timestamp information. Is there a way to put the timestamp in this file from a text file or from the name of each frame (the name of each frame is the timestamp)?. Also, I’m trying to pass track information of the camera used in this video calculated with ORB-Slam2 and I would like to know if there’s a way to pass track information with Plus to Slicer.</p>

---

## Post #2 by @lassoan (2017-04-12 11:31 UTC)

<p>The sequence metafile header is just a text file that you can easily generate using any programming language. The file format specification is available here:<br>
<a href="http://perk-software.cs.queensu.ca/plus/doc/nightly/user/FileSequenceMetafile.html" class="onebox" target="_blank">http://perk-software.cs.queensu.ca/plus/doc/nightly/user/FileSequenceMetafile.html</a><br>
And there are several sample files in your Plus installation package.<br>
Use the .mhd variant of the format because then the image data and header are two separate files, so it is easier to modify/generate the header.</p>
<p>Also note that you can load the sequence metafile directly to Slicer and replay there: install Sequences extension and use file name with .seq.mha or .seq.mhd (just add .seq before the regular file extension to indicate to Slicer that it is a sequence).</p>

---
