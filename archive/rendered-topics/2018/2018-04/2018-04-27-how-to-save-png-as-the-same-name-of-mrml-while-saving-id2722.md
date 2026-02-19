---
topic_id: 2722
title: "How To Save Png As The Same Name Of Mrml While Saving"
date: 2018-04-27
url: https://discourse.slicer.org/t/2722
---

# How to save .png as the same name of .mrml while saving

**Topic ID**: 2722
**Date**: 2018-04-27
**URL**: https://discourse.slicer.org/t/how-to-save-png-as-the-same-name-of-mrml-while-saving/2722

---

## Post #1 by @thedeadspace8 (2018-04-27 16:19 UTC)

<p>Alright, so I’m new to this software. But I understood how to load a .nii file and then save it.<br>
It thankfully saves both in .png and .mrml format (i don’t understand why in .mrml). Anyway, the png file by default saves as ‘Master Scene View’. But I want it to save as the name of the .mrml file and each time, I end up copy pasting this to that.<br>
For example,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/929e9265c61b250b2e22683a7d1600d07583713d.png" data-download-href="/uploads/short-url/kV3rRgp2JKzxvbllwtRNk4axYId.png?dl=1" title="3D%20slicer%20Forum" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/929e9265c61b250b2e22683a7d1600d07583713d_2_690x216.png" alt="3D%20slicer%20Forum" data-base62-sha1="kV3rRgp2JKzxvbllwtRNk4axYId" width="690" height="216" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/929e9265c61b250b2e22683a7d1600d07583713d_2_690x216.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/929e9265c61b250b2e22683a7d1600d07583713d_2_1035x324.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/929e9265c61b250b2e22683a7d1600d07583713d.png 2x" data-dominant-color="E0E7EE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3D%20slicer%20Forum</span><span class="informations">1043×328 28.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Here, the .png file shows ‘Master Scene View’. Can this be changed to the name of the .mrml file by default?</p>

---

## Post #2 by @lassoan (2018-04-27 20:08 UTC)

<p>You can go to Data module and rename the scene view node. By default, node name is used as file name. You can also use these scripts to take screenshot and save to file: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Capture</a></p>

---
