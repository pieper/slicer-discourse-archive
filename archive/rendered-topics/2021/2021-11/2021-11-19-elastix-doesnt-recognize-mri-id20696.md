---
topic_id: 20696
title: "Elastix Doesnt Recognize Mri"
date: 2021-11-19
url: https://discourse.slicer.org/t/20696
---

# Elastix doesn't recognize MRI

**Topic ID**: 20696
**Date**: 2021-11-19
**URL**: https://discourse.slicer.org/t/elastix-doesnt-recognize-mri/20696

---

## Post #1 by @Vincebisca (2021-11-19 10:24 UTC)

<p>Hello !</p>
<p>I have a little problem: I recently started to use Elastix for automatic CT/MRI registration. It worked fine on the first few cases I tested, however, as I dig into other files in my database, it appears that on many of them Elastix is not able to recognize MRI images and I cannot select them as moving volume. Did anyone experience this before?</p>
<p>Thank you !</p>

---

## Post #2 by @mikebind (2021-11-19 16:17 UTC)

<p>Perhaps make sure that they are loading into Slicer as scalar volumes (as opposed to labelmap volumes)?  Anything which is classified in Slicer as a scalar volume node should definitely be selectable in the fixed and moving volume selectors.</p>

---

## Post #3 by @Vincebisca (2021-11-19 16:30 UTC)

<p>Ok I will check! I see the MRIs in Volumes tho, but in the eventuality, is there a way to make a conversion from Labelmap to Volume?</p>

---

## Post #4 by @mikebind (2021-11-19 17:13 UTC)

<p>The “Volumes” module sees both scalar and labelmap volumes, but you can see which one is by looking in the “Volume Information” section in the “Volume type” field<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4dbb35956fc2cdd0568034a1e0c437fe550ab7dd.png" alt="image" data-base62-sha1="b5DRhf6GV7EKtUA2lAx5fQBz0Vn" width="324" height="335"></p>
<p>You can also easily see what type of node each thing in your scene is by clicking on the “Show MRML ID’s” checkbox in the “Data” module.  This will add a column which shows a unique identifier for each item which also identifies the type of node:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56dd2bc488c0a97633d7ab7dd4b26969cc4dcf5f.png" alt="image" data-base62-sha1="coqUYUr3VI00OIbQNZsGToKCFyf" width="248" height="236"></p>

---

## Post #5 by @Vincebisca (2021-11-23 09:31 UTC)

<p>Hello, thank you for the answer ! I checked my volumes and it appears that the volumes that I’m interested in are “MRMLMulti”, Multi Volumes. I notice that in my sequences, some MRI are Scalar Volumes, and others are Multi Volumes, I don’t know why. Is there a way to convert Multi Volumes to Scalar Volumes?</p>
<p>Thanks !</p>

---

## Post #6 by @mikebind (2021-11-23 16:49 UTC)

<p>If you don’t need volume Sequences or MulitVolumes, you can disable importing volumes as those when loading from DICOM. In the DICOM import module, uncheck these two plugins<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d6888efbcd05a6c90f3e74174823f224ea0f043.png" alt="image" data-base62-sha1="b2MJh0Nt2oHBWs9YO66mu20ENer" width="292" height="260"></p>
<p>Then the images will not load as MultiVolumes.  If there is no reason that these images should be considered as part of a multi-volume sequence, then there is something in their DICOM headers which is confusing the importers.  If you can share the images which load incorrectly it might be helpful in improving the importer plugin code.  However, before you share anywhere, you would need to ensure that all patient information has been stripped out of the DICOM headers.</p>

---

## Post #7 by @Vincebisca (2021-11-26 12:28 UTC)

<p>Hi Mike,</p>
<p>Thanks for the advice! I tried it and here is what happened:</p>
<ul>
<li>
<p>First, when I load MultiVolumes as ScalarVolumes, it loads 2 instead of 1 and they look totally different. I guess that MultiVolumes are an overlay of different volumes fused to get the final outcome? Anyway this is annoying because these MultiVolumes where great since they offered a very sharp contrast on the tumor that I am trying to segment…</p>
</li>
<li>
<p>Then I thought: ok, let’s register 1 of the two sub-volumes with Elastix and apply the obtained transform to the multivolume. However, when I try to use Elastix with the subvolumes, it displays an error:<br>
" Error: Command ‘elastix’ returned non-zero exit status 1. "<br>
I don’t really know what it means or how to fix it (noting that I pre-aligned the volumes to minimize the risk of non-convergence or local minimum).</p>
</li>
</ul>
<p>Do you have any idea about that?</p>
<p>Also, it is quite sensitive data and I am not confident in sharing it sadly… I could take a few screenshots but honestly in that case that wouldn’t help that much I think.</p>

---

## Post #8 by @pieper (2021-11-26 14:04 UTC)

<p>If your data really is best read as a MultiVolume, then you can export a frame of interest using the <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/MultiVolumeExplorer">MultiVolume explorer</a> using the current frame copy option.</p>

---

## Post #9 by @Vincebisca (2021-11-26 14:15 UTC)

<p>Okay, as I understand it I can import a MultiVolume, isolate one of the sequences through the frame copy option, work on registering the subsequence, and then apply the transform to the whole MultiVolume?</p>
<p>Also, I tried Elastix with a set of images which already worked before for me and it did the same error. I have changed computer since then but I don’t know if it may be that Elastix installed wrongly on the new one and thus has an internal issue? 'Cause I see the log going on for a while before having the error display… So I guess it tries to calculate the transform but fails…</p>

---

## Post #10 by @pieper (2021-11-26 14:27 UTC)

<aside class="quote no-group" data-username="Vincebisca" data-post="9" data-topic="20696">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<p>Okay, as I understand it I can import a MultiVolume, isolate one of the sequences through the frame copy option, work on registering the subsequence, and then apply the transform to the whole MultiVolume?</p>
</blockquote>
</aside>
<p>We have been migrating from MultiVolume to Sequences and I’m pretty sure that Sequences will work as you expect under a transform (put Sequence in a Transform and all frames will be transformed) but I haven’t used that feature of MultiVolume (it should at least work for the copied frame).</p>
<aside class="quote no-group" data-username="Vincebisca" data-post="9" data-topic="20696">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vincebisca/48/10722_2.png" class="avatar"> Vincebisca:</div>
<blockquote>
<p>Also, I tried Elastix with a set of images which already worked before for me and it did the same error. I have changed computer since then but I don’t know if it may be that Elastix installed wrongly on the new one and thus has an internal issue? 'Cause I see the log going on for a while before having the error display… So I guess it tries to calculate the transform but fails…</p>
</blockquote>
</aside>
<p>Very hard to say - if you can use a public dataset to replicate the issue and post the details perhaps someone could help diagnose.</p>

---

## Post #11 by @lassoan (2021-11-26 15:00 UTC)

<p>I can confirm that all issues related to multivolume will be resolved if you <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/sequences.html#load-dicom-file-as-sequence-node">load your time sequence as a “Volume sequence”</a> (and not as a “Multivolume”).</p>
<p>To register 3D images within a 4D sequence to each other, you can use SequenceRegistration extension (it uses Elastix internally).</p>
<p>If you have trouble registering 3D volumes using Elastix then make sure they are cropped to the same region (no more than 1-2cm difference), have a reasonable initial pose (no more than 1cm and 5 degrees misalignment), and use the default registration preset. If this works you can go back and try gradually relaxing these conditions.</p>
<p>You can also try the recently added SlicerANTs extension. It seems to be similarly robust as Elastix and it exposes some parameter editing in the module’s graphical user interface.</p>

---
