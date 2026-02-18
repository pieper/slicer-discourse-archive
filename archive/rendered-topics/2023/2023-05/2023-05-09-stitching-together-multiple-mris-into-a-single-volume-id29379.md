# Stitching together multiple MRIs into a single volume

**Topic ID**: 29379
**Date**: 2023-05-09
**URL**: https://discourse.slicer.org/t/stitching-together-multiple-mris-into-a-single-volume/29379

---

## Post #1 by @div1708 (2023-05-09 14:25 UTC)

<p>Operating system: mac OS Catalina<br>
Slicer version: 5.0.3</p>
<p>Hi all</p>
<p>I am trying to combine 3MRI scans of a forearm/wrist taken at different table positions into a single image volume. They are all of the same patient and I currently have three NIFTI files: hand to wrist (distal), wrist to mid-forearm (middle) and midforearm to elbow (proximal). There is some overlap between the image volumes. I have been trying to use Mikebind’s StitchVolumes Extension to combine the three volumes into a single image of the forearm.</p>
<p>Sadly I have not had much luck - the images seem to be stitching in the wrong order regardless of the order in which I enter them into the extension. I also seem to be losing some of each volume. I have tried to use fiducial registration wizard to apply transforms to ensure images are in the correct location, but this does not seem to work either.</p>
<p>Any help anyone can provide would be much appreciated</p>

---

## Post #2 by @lassoan (2023-05-10 02:57 UTC)

<p>Probably <a class="mention" href="/u/mikebind">@mikebind</a> can help. Probably you need to share your data or reproduce it using a sample data set (e.g., load an image and create 3 partially overlapping volumes using “Crop volume” module).</p>

---

## Post #3 by @div1708 (2023-05-10 09:32 UTC)

<p>thanks for the reply! Happy to upload data but only seem to have the option to upload image file?</p>
<p>thanks again</p>

---

## Post #4 by @gouxinyi09 (2023-05-10 10:59 UTC)

<p>Hello. I met this problem too. I guess that the module “MultiVolumeImporter” may be useful for you.</p>

---

## Post #5 by @lassoan (2023-05-10 12:21 UTC)

<aside class="quote no-group" data-username="div1708" data-post="3" data-topic="29379">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/779978/48.png" class="avatar"> div1708:</div>
<blockquote>
<p>Happy to upload data but only seem to have the option to upload image file?</p>
</blockquote>
</aside>
<p>You can upload your data set anywhere (dropbox, onedrive, google drive, etc.) and post the link here.</p>

---

## Post #6 by @div1708 (2023-05-17 07:34 UTC)

<p>Hi all, managed to overcome this problem. In case anyone finds this problem in future, the issue is that i wasn’t shifting the locations of the different scans properly, which needs to be done in slicerIGT’s fiducial registration wizard, before stitching together in StitchVolumes. Otherwise, the volumes will just overlie each other at the same point in space.</p>
<p>I think that the problem is I wasn’t hardening the linear transform produced by the fiducial registration properly before I tried to stitch the volumes. While it’s dealing with a different topic, this video is the best I’ve seen on how to use transforms (what buttons to press etc): <a href="https://www.youtube.com/watch?v=GkPHEsB9rOI" class="inline-onebox" rel="noopener nofollow ugc">Tutorial: Re-orientation of 3D volumes in 3DSlicer by Dr Jeremy Shaw - YouTube</a></p>
<p>thanks everyone for your help</p>

---
