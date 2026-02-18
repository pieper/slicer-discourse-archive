# Open Volume as virtual stack

**Topic ID**: 41922
**Date**: 2025-02-28
**URL**: https://discourse.slicer.org/t/open-volume-as-virtual-stack/41922

---

## Post #1 by @mstvan (2025-02-28 16:01 UTC)

<p>Hello,</p>
<p>Can I open image sets in Slicer as virtual stacks similarly to Fiji (ImageJ)? This would be great when dealing with image stacks that are not stored on the computer (but on a hard drive).</p>

---

## Post #2 by @muratmaga (2025-02-28 16:06 UTC)

<p>I am not sure what you mean by “imagestacks not stored on computer but hard drive”.</p>
<p>Virtual stacks in Fiji allows loading datasets that are larger than memory, so only portions of the data is read, while you are navigating the stack.</p>
<p>That is not possible in Slicer, all the data needs to be reloaded into the memory. You can achieve the same level of functionality by increasing the virtual memory size (up to a point. If your image stack is couple terabytes, then of course it won’t work).</p>

---

## Post #3 by @mstvan (2025-02-28 19:07 UTC)

<p>Hi Murat,</p>
<p>Thank you for the fast response. I meant “external drive.” Many of the datasets I am working on require cropping as the first step, and in many cases, I don’t copy the original files to my computer’s hard drive but open them as virtual stacks in FIJI, crop them, and save the end product (which is much smaller) to my computer’s hard drive. When I try doing this with Slicer, it takes much longer than using FIJI’s virtual stack approach.</p>
<p>All the best:</p>
<p>István</p>

---

## Post #4 by @muratmaga (2025-02-28 19:18 UTC)

<p>Have you tried the <code>ImageStacks</code> module in SlicerMorph? If you need cropping it does it way better than Fiji, since it allows you to retain the spatial relationship of the cropped region with regards to the whole volume. In a nutshell, you load the whole sequence in low resolution mode, then set your ROI for the region you want to extract, and then reprocess it as a separate object with ROI constraints and change the resolution to full quality.<br>
What will give you in the end is only the contents of the ROI at the full resolution, and you get to set the ROI in 3D, not in just slice view.</p>
<p>See the full tutorial: <a href="https://github.com/SlicerMorph/Tutorials/tree/main/ImageStacks" class="inline-onebox" rel="noopener nofollow ugc">Tutorials/ImageStacks at main · SlicerMorph/Tutorials · GitHub</a></p>

---

## Post #5 by @mstvan (2025-03-01 15:32 UTC)

<p>Hi Murat,</p>
<p>It worked! I loaded the imagestack in slicermoprh, trimmed and rotated the low-res volume, cropped it with the Crop Volume module, then reloaded the high-res volume. It was loaded in according to the new settings. Amazing!</p>
<p>I have only one question left, though: the only step I’m still using ImageJ for is creating image stacks (often I receive multi-TIFF files) for Slicermorph. Is there any way in Slicer to save data into image sets?</p>
<p>Thanks a lot!</p>

---

## Post #6 by @mstvan (2025-03-01 15:52 UTC)

<p>I gave the wrong sequence in my previous response, I first reloaded the high res volume and only then cropped it with the crop volume. Anyway, it works.</p>
<p>Thanks!</p>

---

## Post #7 by @muratmaga (2025-03-02 03:27 UTC)

<p>If you look at the tutorial, you will see that you don’t need to use the crop volume, and do everything inside the ImageStacks.</p>
<ol>
<li>Load the volume low res in ImageStacks</li>
<li>Set the ROI to be retained</li>
<li>Create a new Output Volume</li>
<li>Set the option Region of Interest option to the ROI you created in step <span class="hashtag-raw">#2</span></li>
<li>Set the quality to Full Resolution<br>
then Hit Load files to load the contents of the ROI at full resolution as a new volume.</li>
</ol>
<p>Crop Volume approach is fine too, but when you have very large sequences (100s of GBs) this approach is more memory efficient as you don’t need to load the whole volume at full resolution.</p>

---
