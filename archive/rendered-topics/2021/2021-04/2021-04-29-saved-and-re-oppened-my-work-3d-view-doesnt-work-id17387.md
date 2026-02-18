# Saved and re-oppened my work - 3d view doesnt work

**Topic ID**: 17387
**Date**: 2021-04-29
**URL**: https://discourse.slicer.org/t/saved-and-re-oppened-my-work-3d-view-doesnt-work/17387

---

## Post #1 by @safalstha (2021-04-29 21:01 UTC)

<p>Hi,</p>
<p>I saved my work recently, and I reopened and I see this. The mask is hidden and I have the bone show which showcases the knee area.</p>
<p>I’m trying to segment each bone, i.e femur tibia and patella… however, before I saved the work I could see the bone 3d view but after I opened my save I see this which I cannot get rid of.</p>
<p>p.s I saved my work and reopened it within a 10min time frame.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/8/e8585b66cae8b110c7104fd598bcbb43287211b8.png" data-download-href="/uploads/short-url/x9q4MQv18exRLiSQ7jr8BGO98bm.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8585b66cae8b110c7104fd598bcbb43287211b8_2_690x370.png" alt="1" data-base62-sha1="x9q4MQv18exRLiSQ7jr8BGO98bm" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8585b66cae8b110c7104fd598bcbb43287211b8_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8585b66cae8b110c7104fd598bcbb43287211b8_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/8/e8585b66cae8b110c7104fd598bcbb43287211b8_2_1380x740.png 2x" data-dominant-color="808484"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1920×1032 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2021-04-30 03:02 UTC)

<p>You probably have another segmentation or model that occludes the view. You can hide or delete them in Data module.</p>
<p>When you load a saved scene, only open the .mrml file it will load all the other files. If you load the .mrml file and data files, too, then you will end up with having multiple copies of the data files (loaded once by the .mrml file and loaded again because you selected the data files).</p>

---

## Post #3 by @safalstha (2021-05-01 15:22 UTC)

<p>thank you so much, it worked and i have done alot of work. also thank you for suggesting me to use the segmentextra package.</p>

---
