# Vertical section view of 3D model to save as STL

**Topic ID**: 9735
**Date**: 2020-01-08
**URL**: https://discourse.slicer.org/t/vertical-section-view-of-3d-model-to-save-as-stl/9735

---

## Post #1 by @Scott (2020-01-08 08:21 UTC)

<p>Hi All</p>
<p>I am new to 3DSlicer and I have been struggling to find a method on how to section view a part and save as stl.</p>
<p>My project:<br>
I have loaded a CT scan of the head, using DICOM files, and rendered a 3D image. I wish to vertically section the head down the middle so that I can see the cavities in the nasal cavity and save this as an STL to be 3D printed.</p>
<p>It seems like it should be a very simple task, however, since I am new I am struggling to find out how to do this.</p>
<p>Please could someone help or guide me through this?</p>
<p>Thank you in advance.<br>
Scott</p>

---

## Post #2 by @Juicy (2020-01-08 09:09 UTC)

<p>Start with some tutorials which are relevant to segmenting for 3d printing. The slicer tutorial page can be found <a href="https://www.slicer.org/wiki/Documentation/4.10/Training" rel="nofollow noopener">here</a></p>
<p>One video which you may find useful is <a href="https://www.youtube.com/watch?v=Uht6Fwtr9hE" rel="nofollow noopener">this one</a>. It is long so you may just want to watch the parts which are relevant.</p>
<p>Here are the general steps I would use:</p>
<ul>
<li>Go to the segment editor module and threshold out the bone using the threshold effect. A minimum value of around 200-300 HU should work well</li>
<li>Click the show 3D button at the top of the segment editor to show the segment in the 3D window.</li>
<li>Click the small pin at the top left of the 3D window and click othographic view projection (not sure exactly what it is called from memory).</li>
<li>In the same area click the ‘S’ label to look down on the top of the skull.</li>
<li>Now use the scissors effect in segment editor (use the box shape) click and drag the box to cut away half of the skull.</li>
<li>Go to the segmentations module and go to the export segments area. Click export and model from the selections. This will save the segment as a surface model.</li>
<li>When you save the file be sure to find the model and change the file type from vtk to STL.</li>
</ul>
<p>Hopefully that works. I dont have slicer open currently so this is from memory. You should be able to fill in the gaps by watching videos and tutorials. Also search google in general for videos on segmenting for 3d printing.</p>
<p>Good luck.</p>

---

## Post #3 by @lassoan (2020-01-08 14:07 UTC)

<aside class="quote no-group" data-username="Juicy" data-post="2" data-topic="9735">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/74df32/48.png" class="avatar"> Juicy:</div>
<blockquote>
<p>Go to the segmentations module and go to the export segments area. Click export and model from the selections. This will save the segment as a surface model.</p>
</blockquote>
</aside>
<p>Instead of export and save, you can use “Export to files…” option in the drop-down menu of “Segmentations…” button in Segment Editor. It creates printable STL files in one simple step.</p>

---

## Post #4 by @Juicy (2020-01-09 04:35 UTC)

<p>Thanks, good to know. That would save a few clicks.</p>

---

## Post #5 by @Scott (2020-01-09 06:19 UTC)

<p>Thank you so much.<br>
Its good to learn many ways of using the software.</p>
<p>After many a you tube video, I found one that showed me how to just crop the CT scan in half, and save the cropped section <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:"> haha</p>
<p>So basically:</p>
<ul>
<li>Load DICOM CT scan</li>
<li>Render Volume to see 3D model</li>
<li>Select Enable Crop and ROI to select the region you are interested in</li>
<li>Go to the Crop Module</li>
<li>Apply the crop and then you have Won <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=9" title=":slight_smile:" class="emoji" alt=":slight_smile:">
</li>
<li>Then just save the vtk as STL</li>
</ul>
<p>Thanks guys!<br>
I really appreciate the quick response.</p>
<p>Kind Regards<br>
Scott</p>

---

## Post #6 by @Juicy (2020-01-09 06:37 UTC)

<p>Nice one, yes cropping the volume is also another way to go about it. It can also be faster to segment a cropped volume as less computing power is needed.</p>

---

## Post #7 by @tsehrhardt (2020-01-10 18:45 UTC)

<p>Once you have your 3d model made, you can use the EasyClip module to make nice plane cuts to export. You can use the slice sliders to see where to make the cut. There is even an undo and flip, so you can easily make for example a midsagittal cut, save the left half, undo, flip, then save the right half.</p>

---
