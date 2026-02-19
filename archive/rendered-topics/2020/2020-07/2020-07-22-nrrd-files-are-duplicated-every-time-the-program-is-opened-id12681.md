---
topic_id: 12681
title: "Nrrd Files Are Duplicated Every Time The Program Is Opened"
date: 2020-07-22
url: https://discourse.slicer.org/t/12681
---

# nrrd files are duplicated every time the program is opened 

**Topic ID**: 12681
**Date**: 2020-07-22
**URL**: https://discourse.slicer.org/t/nrrd-files-are-duplicated-every-time-the-program-is-opened/12681

---

## Post #1 by @sndkf (2020-07-22 13:43 UTC)

<p>Hello.</p>
<p>Every time 3D Slicer is opened, I load the files I need from a directory and 3D Slicer automatically creates duplicates of all these files. They’re usually named “filename_1nrrd” and it has lead to the situation where I now have a string of files with names leading up to “VolumeProperty_1_1_1_1_1_1.vp”.</p>
<p>This appears to be a default setting as I’ve experienced it both on Windows 10 and macOS Catalina (Slicer 4.11 and 4.10) but I cant find how to change it.</p>
<p>Normally I just manually delete the duplicates before I begin working but, in addition to be irritating, this duplication system occasionally makes changes to the original files that cannot be undone. As shown in the picture, the colours on my original segmentation have all been set to to same shade of grey, and the only duplicates have differential colours (though they don’t have the original colours for the each organ).</p>
<p>Any advice to rectify this and prevent such behaviour in the future is greatly appreciated as it affects my productivity.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/f/ef20fef5c6d446c9ce8c5ccf633adadb2f69e66f.jpeg" data-download-href="/uploads/short-url/y7qO9rpkI1bxk1OegJ6hfNGArXp.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef20fef5c6d446c9ce8c5ccf633adadb2f69e66f_2_375x500.jpeg" alt="image" data-base62-sha1="y7qO9rpkI1bxk1OegJ6hfNGArXp" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef20fef5c6d446c9ce8c5ccf633adadb2f69e66f_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef20fef5c6d446c9ce8c5ccf633adadb2f69e66f_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/ef20fef5c6d446c9ce8c5ccf633adadb2f69e66f_2_750x1000.jpeg 2x" data-dominant-color="94948F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1512×2016 1.66 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-07-22 14:02 UTC)

<p>Nodes are automatically renamed when loaded from files so that you can distinguish them more easily. For example, if you load “abc.nrrd” file twice so that you transform one and compare it to the other then you would want to be able to distinguish them without manually renaming.</p>
<p>If there are no duplicate filenames then there should be no renaming. So I would recommend to load each file only once.</p>
<p>Your problem may be because you load both the scene (mrml) file (which loads all the necessary files already) and each individual data files. You can avoid duplicate loading by drag-and-dropping only the scene (mrml) file to the Slicer application window. Simply double-clicking on the scene file in file explorer may work, too.</p>

---

## Post #3 by @sndkf (2020-07-22 14:30 UTC)

<p>Thanks, I wasn’t aware that the scene file loaded the other files.</p>
<p>I’m also having trouble with the ‘level tracing’ tool in the segment editor module. It used to work as expected but currently it doesn’t track the cursor very well at all, and often highlights a tiny region enclosing only 2 or 3 pixels and gets stuck there. I cannot move backwards as my segmentations don’t open properly on slicer 4.10. Any advice on how to rectify this?</p>

---

## Post #4 by @lassoan (2020-07-22 14:34 UTC)

<p>Level trace effect has not changed in recent years. It requires the view to be aligned with the segmentation axis. If they are not aligned then a warning icon appears near the master volume selector and clicking it will adjust the slice orientation. If this does not fix the problem then please create a new topic (this topic is about file duplication in the scene).</p>

---
