---
topic_id: 36414
title: "Is Slicer Able To Load Large Images 2 31 Voxels"
date: 2024-05-27
url: https://discourse.slicer.org/t/36414
---

# Is Slicer able to load large images (> 2^31 voxels)?

**Topic ID**: 36414
**Date**: 2024-05-27
**URL**: https://discourse.slicer.org/t/is-slicer-able-to-load-large-images-2-31-voxels/36414

---

## Post #1 by @dyollb (2024-05-27 09:48 UTC)

<p>I was trying to load an image (labelfield) with shape (566, 1081, 3597) in Slicer 5.6.2.</p>
<p>Note: <code>566 * 1081 * 3597 &gt; 2^31</code></p>
<p>When the segmentation is loaded, I get no error message and it is shown in the Data/Scene explorer, but it is not displayed (views stay black), and if I try to create surfaces or do something else Slicer crashes. Reducing the resolution fixes the issue.</p>
<p>Is this a known limitation of Slicer (is the code using 32-bit signed <code>int</code> for the indices or to compute the size (e.g. from a vtkImageData::GetDimensions(int dims[3]), or similar)?</p>
<p>I have lots of RAM, I doubt I am running out.</p>

---

## Post #2 by @muratmaga (2024-05-27 16:18 UTC)

<aside class="quote no-group" data-username="dyollb" data-post="1" data-topic="36414">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dyollb/48/16686_2.png" class="avatar"> dyollb:</div>
<blockquote>
<p>I was trying to load an image (labelfield) with shape (566, 1081, 3597) in Slicer 5.6.2.</p>
<p>Note: <code>566 * 1081 * 3597 &gt; 2^31</code></p>
</blockquote>
</aside>
<p>That’s not a very large image, it is barely 2GB if the data type is 8 bit unsigned, which would be typical datatype for labelmaps (unless of course there are more than 256 labels).</p>
<p>How are you loading this dataset to slicer, are you making sure the “label” option is checked when in the data load menu (make sure to expand the options). Or are you loading it as a segmentation. If that’s the case, it is normal nothing is displayed in slice views, since segmentation requires a “master volume” to display in Slice views. (You can drag it into 3D viewer to see it though).</p>

---

## Post #3 by @dyollb (2024-05-28 06:39 UTC)

<p>I am loading the labelfield as segmentation. I tried nrrd and nifty formats, and uint16 and uint8 data (there are only 21 labels). I first load a color table (ctbl file) to get my colors and names, and then import the segmentation and assign the color table using the advanced options.</p>
<p>I will try again. Are PDB files available for the installers (symbol files for debugging on Windows, i.e. you would need to build with RelWithDebInfo)?</p>

---

## Post #4 by @pieper (2024-05-28 07:38 UTC)

<aside class="quote no-group" data-username="dyollb" data-post="3" data-topic="36414">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dyollb/48/16686_2.png" class="avatar"> dyollb:</div>
<blockquote>
<p>Are PDB files available for the installers (symbol files for debugging on Windows, i.e. you would need to build with RelWithDebInfo)?</p>
</blockquote>
</aside>
<p>No, but you can build everything from source in Debug or RelWithDebInfo.  On a fast linux machine it may take an hour or so, probably longer on a windows desktop and overnight on a laptop.</p>

---
