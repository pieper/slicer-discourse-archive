---
topic_id: 6639
title: "Save To Png File Not Aware Of Spacing"
date: 2019-04-29
url: https://discourse.slicer.org/t/6639
---

# Save to png file not aware of spacing

**Topic ID**: 6639
**Date**: 2019-04-29
**URL**: https://discourse.slicer.org/t/save-to-png-file-not-aware-of-spacing/6639

---

## Post #1 by @ButuiHu (2019-04-29 03:27 UTC)

<p>Hi, I’m trying to save a .mhd file to png file to insert in a document. However, 3dslicer seems to be aware of spacing when display .mhd file, but not in saving to .png file.<br>
In 3dslicer, I got this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/676c8c1096c1c6ec2ce570c4f6026168366a90dd.jpeg" data-download-href="/uploads/short-url/eKVJUT4HVyqqwZz2AaEdXD9Ce7P.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/676c8c1096c1c6ec2ce570c4f6026168366a90dd_2_606x500.jpeg" alt="image" data-base62-sha1="eKVJUT4HVyqqwZz2AaEdXD9Ce7P" width="606" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/676c8c1096c1c6ec2ce570c4f6026168366a90dd_2_606x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/676c8c1096c1c6ec2ce570c4f6026168366a90dd.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/676c8c1096c1c6ec2ce570c4f6026168366a90dd.jpeg 2x" data-dominant-color="464646"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">707×583 70.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
after saving as png file:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c5deef5ab77f072ab07e4ca198b528dc9befe32.png" data-download-href="/uploads/short-url/hKcsnLe6w2MDtjj0q4OGYgcpxE6.png?dl=1" title="patient0001_2CH_ED" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c5deef5ab77f072ab07e4ca198b528dc9befe32_2_352x500.png" alt="patient0001_2CH_ED" data-base62-sha1="hKcsnLe6w2MDtjj0q4OGYgcpxE6" width="352" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c5deef5ab77f072ab07e4ca198b528dc9befe32_2_352x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c5deef5ab77f072ab07e4ca198b528dc9befe32_2_528x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c5deef5ab77f072ab07e4ca198b528dc9befe32.png 2x" data-dominant-color="6B6B6B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">patient0001_2CH_ED</span><span class="informations">549×778 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>The spacing is wrong, and it also seems that the the saved png file is brighter.</p>
<p>Images from <a href="http://camus.creatis.insa-lyon.fr/challenge/" class="inline-onebox" rel="noopener nofollow ugc">Camus</a></p>

---

## Post #2 by @lassoan (2019-04-29 14:02 UTC)

<p>Consumer file formats, such as png or jpg, are rarely used in medical image computing (there are good reasons for that). Instead, I would recommend to use research formats, such as .nrrd or .mha.</p>
<p>Just for exporting images or videos to a document or presentation, you can use <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/ScreenCapture" rel="nofollow noopener">Screen Capture</a> module.</p>

---

## Post #4 by @ButuiHu (2019-04-30 02:02 UTC)

<p>Thank you. I  resample the image according to <a href="https://github.com/SimpleITK/SimpleITK/issues/561" rel="nofollow noopener">https://github.com/SimpleITK/SimpleITK/issues/561</a>.</p>

---
