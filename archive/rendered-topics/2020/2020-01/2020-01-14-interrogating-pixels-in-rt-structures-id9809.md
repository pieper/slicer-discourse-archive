# interrogating pixels in RT structures

**Topic ID**: 9809
**Date**: 2020-01-14
**URL**: https://discourse.slicer.org/t/interrogating-pixels-in-rt-structures/9809

---

## Post #1 by @mcjury (2020-01-14 15:50 UTC)

<p>Can anyone save me time? - I have spend considerable time but not found the answer to this:</p>
<p>I have a data set comprising a set of MRI images, and a set of RT (Radiotherapy) structures.<br>
Aim - I would like to obtain the pixel values from each of the structure volumes, and do simple processing of them - generate historgrams of the pixel values, etc.<br>
I don’t necessarily need to do the image processing of the pixels in Slicer - I would be happy even to be able to export the pixel values for each structure out of Slicer and process elsewhere if necessary.</p>
<p>So far, I can get my data into 3DSlicer, and I have installed SlicerRT.<br>
I can see the images, and the structures/volumes.</p>
<p>BUT, I do not know how to actually analyse the pixels in the structures, or export their values offline.<br>
This is really such a basic thing to do, I strongly suspect someone has already done it - I don’<span class="hashtag">#t</span> want to reinvent the wheel here.<br>
I’ve been told I need to do something with binary labelmap representations…but I have no idea what do do, and can’t quickly find help in documentation/tutorials so far…</p>
<p>If anyone can point me to exactly where there are understandable instructions for this kind of thing, or suggest a set of steps I can try - that would be awesome.</p>
<p>Thanks<br>
mark</p>

---

## Post #2 by @cpinter (2020-01-14 16:22 UTC)

<p>You got most of it done. You just need to use one more tool:</p>
<ul>
<li>Install the SegmentEditorExtraEffects extension</li>
<li>Make sure the RT structure set is selected as segmentation and the MRI as master volume</li>
<li>Use the Mask volume effect</li>
</ul>

---

## Post #3 by @mcjury (2020-01-15 14:12 UTC)

<p>Thanks Csaba!<br>
Good to know I’m almost there - I was beginning to think Slicer was more focussed on visualisation, than pixel analysis…<br>
OK - so I’ve installed that extension [ and btw, I get an error (That extension is dependent on another which cannot be found - MarkupsToModel - but hopefully that will not affect what I am trying to do?]<br>
In SegmentationEditor, I can set the volume as master, etc. and I see the mask tool.</p>
<p>I’ll read the module document on how to use the mask effect and explore this process…<br>
Fingers-crossed - but I may need to come back to you if I get stuck.<br>
Thanks again<br>
mark</p>

---

## Post #4 by @lassoan (2020-01-15 21:13 UTC)

<aside class="quote no-group" data-username="mcjury" data-post="3" data-topic="9809">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/df705f/48.png" class="avatar"> mcjury:</div>
<blockquote>
<p>That extension is dependent on another which cannot be found - MarkupsToModel</p>
</blockquote>
</aside>
<p>MarkupsToModel extension should be available on all platforms. Please try again. If it still cannot find it then let us know which Slicer version you use on what platform and I’ll lok into it.</p>

---

## Post #5 by @mcjury (2020-01-22 11:11 UTC)

<p>Csaba,<br>
OK - here is where I have gotten to with this:</p>
<blockquote>
<p>I load up my images and RT structures<br>
Set the images as master volume<br>
Select a segment<br>
Mask outside the segment to 0 intensity and store the masked segment;<br>
Make the masked_segment the active volume<br>
In volume module, I can see some information about the volume - including a displayed histogram of pixel intensities.<br>
–Two things I cannot see how to do:<br>
How do I save this histogram as something which allows me to have this data in a useful form, eg .csv file or similar? can the displayed histogram be formatted better, with axis labels and saved as an image file?<br>
Secondly - the histogram is great - but I’m surprised not to see the simple stuff - mean and median pixel values for the volume - where can I get these?</p>
</blockquote>
<p>Thanks!<br>
mark</p>

---

## Post #6 by @cpinter (2020-01-22 16:03 UTC)

<p>You can use the Segment Statistics module (even without doing the masking, just with the original volume and the segmentation) to see simple metrics.</p>
<p>I’m not sure you can show the histogram just using modules. I’d use the vtkImageAccumulate filter from python and fill a vtkTable and put it in a vtkMRMLTableNode to show the histogram nicely as a Plot.</p>

---
