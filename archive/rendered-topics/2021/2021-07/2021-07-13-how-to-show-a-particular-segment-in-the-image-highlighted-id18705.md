# How to Show a particular segment in the image highlighted

**Topic ID**: 18705
**Date**: 2021-07-13
**URL**: https://discourse.slicer.org/t/how-to-show-a-particular-segment-in-the-image-highlighted/18705

---

## Post #1 by @tpvagenas (2021-07-13 18:37 UTC)

<p>Hello, I need to correct some manual segmentations I had received for the project I am working on as part of my PhD thesis. The problem is that I have a volume file and a segmentation file and the segmentation file has 200 segmented regions in it. And beyond that I have to do this for more images. I want to scan each one and evaluate the segmentation. I believe that it would be very helpful to click on each of the segmented region and the region to be highlighted in the slices of the 3d image. Is this possible with 3d slicer? To become more clear I would like to select each one of the segments and locate it interactively in slices by having the borders or the whole region highlighted in some way.<br>
Thank you very much</p>

---

## Post #2 by @pieper (2021-07-13 20:08 UTC)

<p>If you right-click on a segment in the list you can use the Jump Slices menu to center it in all the views and you can toggle visibility with the eye icon.</p>

---

## Post #3 by @tpvagenas (2021-07-14 09:43 UTC)

<p>Thank you for the respond. I have tried this feature, but it is a bit difficult to make a fast check in a slice where there are 5-10 segmented regions (where colors are distinguishable). Is there any other way to highlight each segment by selecting it and observe it on the image?</p>

---

## Post #4 by @lassoan (2021-07-14 23:27 UTC)

<p>Of course, there are many ways to highlight a segment. The easiest is to right-click and choose “Show only this segment”, but you can adjust 2D/3D opacity, color, etc. for each segment individually. You can also export the segments to models and organize them into a tree hierarchy. That way you can show/hide entire branches at once.</p>
<p>If you have specific requirements (make the current segment opaque, while all the others 50% transparent) then you can write a very simple scripted module and place a segmentation node selector and a segment list widget. You can then add an observer to the segment list and whenever the user changes the selected segment then you would update the opacities of the segments. It probably requires just 20-30 lines of code.</p>

---

## Post #5 by @tpvagenas (2021-07-20 15:11 UTC)

<p>Could you give me more information about the second option using module scripts. I have never written module scripts for 3dslicer. How can I get the selected segment and update whenever need it (change the selected segment with mouse)? As I can see so far if I have the segment id, I can change the opacity of the current segment. Also I will need to jump to the selected segment in the image. Could you tell me more about the functions I will need?</p>

---

## Post #6 by @rbumm (2021-07-20 17:17 UTC)

<p>Try the “Extension manager” under “Developer tools”.</p>
<p>When you “Create extension” here, it gets populated with a sample project (give it a new name)  that is very useful for making your own personal extension. You can edit the python source code with your preferred text editor, “Reload” the new extension within 3D Slicer, and test it.</p>
<p>Concerning the necessary functions, I am afraid that it will need some deep searches into similar projects.</p>
<p>A great starting point for common scripts is the script repository:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html</a></p>

---

## Post #7 by @lassoan (2021-07-20 19:21 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/api.html#tutorials">Programming tutorials</a> such as the PerkLab Slicer programming tutorial can also help getting started with module development.</p>

---

## Post #8 by @Moh_d_Al-Watary (2022-06-25 08:07 UTC)

<p>I also want to do such things, as I want to make it clear via color coded regarding different bony segments on the skull. So. please do you have a video demonstration of what you have explained here. Thank you so much</p>

---

## Post #9 by @lassoan (2022-06-28 16:13 UTC)

<p>The recommended way was adding a short Python script that observes a segment list widget and sets the opacity of the selected segment to 100% and makes the opacity of other segments 50% or less. There is no video demonstration for this, but you can find most of the necessary code snippets in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">Slicer Script Repository</a>.</p>

---
