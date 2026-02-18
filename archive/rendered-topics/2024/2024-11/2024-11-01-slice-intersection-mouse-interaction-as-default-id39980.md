# Slice intersection mouse interaction as default

**Topic ID**: 39980
**Date**: 2024-11-01
**URL**: https://discourse.slicer.org/t/slice-intersection-mouse-interaction-as-default/39980

---

## Post #1 by @racctor (2024-11-01 11:15 UTC)

<p>Dear all,</p>
<p>I am new to 3D Slicer and have a problem ChatGPT clearling cant explain to me <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"> So help would be appreciated:</p>
<p>I have a CT scan of my skull with the volume “10” series. I visualized the volume using volume rendering and in parallel used slice intersection interaction to re-orientate my red, green and yellow slice (orthogonal to each other) per hand/mouse. By that I created a nice Frankfort plane and defined a clear midsagittal plane.</p>
<p>I have not created anything in the Transform module or in the Reformat module (chatgpt wanted me to work with these modules, but I think it started to mix things up).</p>
<p>I want to use the new Reformat slices now as the new default. So when I chose the anterior view (e.g.), I pop directly into the new y-axis defined by the intersecting line of my newly created axial and lateral  intersection planes.</p>
<p>What is the easiest way to do that?<br>
Kind regards!</p>

---

## Post #2 by @pieper (2024-11-01 19:38 UTC)

<p>If you mean you want to be able to always load this CT scan using the rotated axes, then ChatGPT was correct to suggest the Transforms module.  You can put the volume under a transform then rotate the skull so that it is in the orientation you prefer and then harden the transform and save the file.  Then it will be in the same orientation when you reload it.</p>

---

## Post #3 by @racctor (2024-11-04 17:48 UTC)

<p>I know that i can use Transform and Resample to create a new grid alignment. Is it somehow possible to do that without the Transform module? I would like to use the reformatted intersection planes as my new coordinate system. E.g.: i rotated the sagittal intersection 2 degrees around the z axis and want my new x and y axis be defined accordingly. I rotated the intersections by hand using mouse interaction though and did not do so by using the transform module.</p>

---
