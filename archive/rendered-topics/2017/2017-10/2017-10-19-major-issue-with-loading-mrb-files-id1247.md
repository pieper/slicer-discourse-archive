---
topic_id: 1247
title: "Major Issue With Loading Mrb Files"
date: 2017-10-19
url: https://discourse.slicer.org/t/1247
---

# Major Issue with loading .mrb files

**Topic ID**: 1247
**Date**: 2017-10-19
**URL**: https://discourse.slicer.org/t/major-issue-with-loading-mrb-files/1247

---

## Post #1 by @stevenagl12 (2017-10-19 16:16 UTC)

<p>I have been saving files as mrb files. I realized today, while going through my registrations, that the full body scans that had previously been used for segmentation (which were all different), had somehow gotten reduced to copies of the second full body volume. I have no idea how this happened as until a couple weeks ago there was no issue. I have the original files that I had segmented, but when I pulled them all into the same scene and subsequently started registration all of the volumes except the volume I registered to have turned into duplicates of the first moving volume. Here is an example:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/21fa2db24812b5e854bc608d3a4359bfad2d1d68.png" data-download-href="/uploads/short-url/4QzLdaYTTffJF8urnyp2jq7P9kk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21fa2db24812b5e854bc608d3a4359bfad2d1d68_2_690x373.png" alt="image" data-base62-sha1="4QzLdaYTTffJF8urnyp2jq7P9kk" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21fa2db24812b5e854bc608d3a4359bfad2d1d68_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21fa2db24812b5e854bc608d3a4359bfad2d1d68_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/1/21fa2db24812b5e854bc608d3a4359bfad2d1d68_2_1380x746.png 2x" data-dominant-color="2C2C2C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 254 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/633266e288a35c80547b72cd547c6273baae0d58.png" data-download-href="/uploads/short-url/e9xfOJIG1O2yA2qkIJxizqsW3sk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/633266e288a35c80547b72cd547c6273baae0d58_2_690x373.png" alt="image" data-base62-sha1="e9xfOJIG1O2yA2qkIJxizqsW3sk" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/633266e288a35c80547b72cd547c6273baae0d58_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/633266e288a35c80547b72cd547c6273baae0d58_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/633266e288a35c80547b72cd547c6273baae0d58_2_1380x746.png 2x" data-dominant-color="2A292A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 251 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cb1b3924090b3fa602c6b02c2a911a1c10344b8.png" data-download-href="/uploads/short-url/8EVn3j8XqUwSQN7vAdERpjXJeo8.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cb1b3924090b3fa602c6b02c2a911a1c10344b8_2_690x373.png" alt="image" data-base62-sha1="8EVn3j8XqUwSQN7vAdERpjXJeo8" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cb1b3924090b3fa602c6b02c2a911a1c10344b8_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cb1b3924090b3fa602c6b02c2a911a1c10344b8_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cb1b3924090b3fa602c6b02c2a911a1c10344b8_2_1380x746.png 2x" data-dominant-color="2A292A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 254 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Here are some examples of the original files when I reloaded them all prior to saving as a mrb file:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e70d6054f7906a51b34fa5455ae7bab8d909badc.jpeg" data-download-href="/uploads/short-url/wXYXaa74YilyzFiG14NZhdB1KnG.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e70d6054f7906a51b34fa5455ae7bab8d909badc_2_690x373.jpg" alt="image" data-base62-sha1="wXYXaa74YilyzFiG14NZhdB1KnG" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e70d6054f7906a51b34fa5455ae7bab8d909badc_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e70d6054f7906a51b34fa5455ae7bab8d909badc_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e70d6054f7906a51b34fa5455ae7bab8d909badc_2_1380x746.jpg 2x" data-dominant-color="2F2F2F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 364 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/908e62cd261b1849188e69441013153549a4cdfd.png" data-download-href="/uploads/short-url/kCNOBy8ukhTFPhQmofDqaDVcQP3.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/908e62cd261b1849188e69441013153549a4cdfd_2_690x373.png" alt="image" data-base62-sha1="kCNOBy8ukhTFPhQmofDqaDVcQP3" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/908e62cd261b1849188e69441013153549a4cdfd_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/908e62cd261b1849188e69441013153549a4cdfd_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/908e62cd261b1849188e69441013153549a4cdfd_2_1380x746.png 2x" data-dominant-color="292829"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 238 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2017-10-19 16:33 UTC)

<p>When a volume node contains an empty image, then when you select it in the slice view, the previously selected volume may remain selected. Can you confirm that in your case the volumes that appear to be the same as the “first moving volume” are actually valid? You can verify that by zooming in/out (if you don’t have a valid image then you cannot zoom in/out) and showing only that volume as background volume (select None as foreground volume).</p>

---

## Post #3 by @stevenagl12 (2017-10-19 18:20 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e9cdb432d7d119946c75753728557341aec551d5.jpeg" data-download-href="/uploads/short-url/xmjY5z06PzV7ZBR1cySpE4Ao6tT.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e9cdb432d7d119946c75753728557341aec551d5_2_690x373.jpg" alt="image" data-base62-sha1="xmjY5z06PzV7ZBR1cySpE4Ao6tT" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e9cdb432d7d119946c75753728557341aec551d5_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e9cdb432d7d119946c75753728557341aec551d5_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/e9cdb432d7d119946c75753728557341aec551d5_2_1380x746.jpg 2x" data-dominant-color="5B5A5B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 504 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/933e5d1289bfdd98e0c13e17265ed73af5510a53.jpeg" data-download-href="/uploads/short-url/l0zNGS9rHICCCCclDabw3TT2nYL.jpg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/933e5d1289bfdd98e0c13e17265ed73af5510a53_2_690x373.jpg" alt="image" data-base62-sha1="l0zNGS9rHICCCCclDabw3TT2nYL" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/933e5d1289bfdd98e0c13e17265ed73af5510a53_2_690x373.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/933e5d1289bfdd98e0c13e17265ed73af5510a53_2_1035x559.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/933e5d1289bfdd98e0c13e17265ed73af5510a53_2_1380x746.jpg 2x" data-dominant-color="4A494A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 453 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2017-10-19 19:44 UTC)

<p>Can you reproduce the issue?<br>
Do you have scenes that you can load individually and they appear correctly but when you load them all into one scene they show up differently?<br>
Can you share those scenes so that we can investigate?<br>
Do you get any warnings or errors when you load the scene?</p>

---

## Post #5 by @stevenagl12 (2017-10-19 19:55 UTC)

<p>I can reproduce the issue. The scenes within the compression fo the mrb files that I had with the registrations all load incorrectly. Is there a file size limitation that can cause issues like this as I just created a separate mrb file with specific segmentations and volumes (shortening the amount significantly), and it seems to load fine thus far and appears to at least register them fine? Haven’t tried saving them and reloading them yet.</p>

---

## Post #6 by @lassoan (2017-10-19 19:58 UTC)

<p>If you run out of memory then anything can happen. How much RAM do you have? How much virtual memory have you configured for your system? What is the size of all data sets in the scene (uncompressed)? Is there any error logged during scene loading? Can you share the data sets?</p>

---

## Post #7 by @stevenagl12 (2017-10-19 20:24 UTC)

<p>So I’m working on a desktop with 32 GBs of RAM. The virtual memory configuration is the default configuration when downloaded as I have no knowledge of how to adjust it or anything. Each scene is approximately 680 MBs I believe uncompressed as the mrb files saved for each individual are about 300,000-350,000 KBs. There was no error logged when I loaded them. Unfortunately, the school is working on being able to share our data, but currently, we are not allowed as it is all from our human gift program and the families need to sign off.</p>

---

## Post #8 by @lassoan (2017-10-19 20:46 UTC)

<p>To investigate or fix the problem, it is essential to be able to reproduce it. If you cannot share the images, then blank out the images with some simple shapes (you can do that using Segment Editor / Mask volume; after installing SegmentEditorExtraEffects extension) save the scene, and see if you can reproduce the problem using these modified images. Or save the images in nhdr format and then delete the pixel data (.raw file) and send all the other files.</p>

---

## Post #9 by @stevenagl12 (2017-10-19 22:31 UTC)

<p>I’m sorry, I’m not fully understanding what you are asking me to do. Are you asking me to decompress the mrb files that aren’t loading properly, and use those with the segment editor operation and send the scenes? Or are you asking me to just sent the scenes and such of the files individually that I pull into Slicer?</p>

---

## Post #10 by @lassoan (2017-10-19 23:24 UTC)

<p>I would need the scene files to reproduce the problem. You would not like to share the data because the image data, but actually I don’t need voxel data, an image filled with some solid color is just as good.</p>
<p>So, I suggest to blank out the voxel data in your images so that you can share the scenes.</p>
<p>You can mask volume using sgment editor as I described above. But maybe it is even simpler to use numpy to set all voxels in the image to a constant value (and use a different constant value in each file) - see here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Modify_voxels_in_a_volume</a></p>
<p>Once you have blanked out voxel data in your images, save the scene, and share with us (it should be no problem sharing them, as there original image data is not there anymore).</p>

---

## Post #11 by @stevenagl12 (2017-10-23 16:04 UTC)

<p>I think I figured out the problem anyways. My CPU and Memory were being maxed out and my storage was 2 GBs shy of being full. In fact, when I tried running it last the whole computer overloaded and shut down.</p>

---

## Post #12 by @lassoan (2017-10-23 17:12 UTC)

<p>Thanks for the update. In general, most software act randomly (crash, report various errors, etc) if they run out of memory. As a rule of thumb, allocate at least 10x more virtual memory than the sum of size of all data that you load (backed up by as much physical memory as possible).</p>

---
