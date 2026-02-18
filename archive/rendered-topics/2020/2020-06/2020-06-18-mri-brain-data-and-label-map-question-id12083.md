# MRI Brain data and label map question

**Topic ID**: 12083
**Date**: 2020-06-18
**URL**: https://discourse.slicer.org/t/mri-brain-data-and-label-map-question/12083

---

## Post #1 by @harry1511 (2020-06-18 02:49 UTC)

<p>Hi,<br>
I am working on a visualization project, and has acquired few datasets of healthy brain (NIFTI format). I managed to open and extract the datasets out as series of .png, and this is used as a flipbook texture that will be read inside Unreal Engine 4 with a raymarching material. Everything is good.</p>
<p>Now I need to create highlight areas to differentiate parts of the brain (frontal lobe, temporal lobe…etc). My current solution is to create segmentations of different parts, convert it to label maps, export them out as series of .png and use as masks inside UE4. Problem is, I am creating the segments manually using Paint, Grow seeds, Water Shed…etc, this is so intensive to edit, and not super accurate, lots of fuzzy noises. So questions are:</p>
<p>1/ Is there a better way to create label maps for different parts of the brain?<br>
2/ I saw this: <a href="https://github.com/mhalle/spl-brain-atlas" rel="nofollow noopener">https://github.com/mhalle/spl-brain-atlas</a>, and think I may use their pre-computed label maps and apply to my datasets, but how do I do that? I opened their scene, I can’t see any.<br>
3/ Up until now, I need to use another software to export out a flipbook texture from my datasets, I don’t see any function/extension inside Slicer can help me do that, so is there any?</p>
<p>I am a 3D game artist, so I am familiar with other 3D packages/techniques in games, but quite frankly, not a radiologist, or medical expert. So it is really hard for me to understand all the terminologies, and techniques that are common in radiology field (even file format is so alien!). Plus, the tutorials about Slicer are either outdated, or not good at all. So I appreciate if you all can point me at the right direction.</p>
<p>Thank you.</p>
<p>Operating system: Windows 10<br>
Slicer version: 4.10.2</p>

---
