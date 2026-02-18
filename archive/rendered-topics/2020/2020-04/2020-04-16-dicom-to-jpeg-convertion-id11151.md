# DICOM to JPEG Convertion

**Topic ID**: 11151
**Date**: 2020-04-16
**URL**: https://discourse.slicer.org/t/dicom-to-jpeg-convertion/11151

---

## Post #1 by @Fabricio_Barbosa (2020-04-16 13:46 UTC)

<p>Operating system: Windows 10 x64<br>
Slicer version: 4.10.2<br>
Expected behavior: all the file format changed when I choose one format<br>
Actual behavior: format changed at once for the selected file</p>
<p>Is it possible change at once the file format chosen in Save Scene and Unsaved Data?<br>
when I try to save scene and choose the file format (eg. .nrrd to .jpeg) I have to change all the files, one by one.</p>
<p>I need change all the extension file choosing the file format, at once. Because I have many files to convert (.nrrd to .jpeg).</p>

---

## Post #2 by @pieper (2020-04-16 14:09 UTC)

<p>These instructions should help:</p>
<p><a href="https://www.slicer.org/w/index.php/Documentation/Nightly/ScriptRepository#Change_default_file_type_for_nodes_.28that_have_never_been_saved_yet.29" class="onebox" target="_blank">https://www.slicer.org/w/index.php/Documentation/Nightly/ScriptRepository#Change_default_file_type_for_nodes_.28that_have_never_been_saved_yet.29</a></p>

---

## Post #3 by @lassoan (2020-04-16 14:49 UTC)

<aside class="quote no-group" data-username="Fabricio_Barbosa" data-post="1" data-topic="11151">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fabricio_barbosa/48/6556_2.png" class="avatar"> Fabricio_Barbosa:</div>
<blockquote>
<p>I try to save scene and choose the file format (eg. .nrrd to .jpeg) I have to change all the files, one by one.</p>
</blockquote>
</aside>
<p>In general, JPG cannot be used for medical image storage. Not just due to compression artifacts but because it is limited to 8 bits and does not preserve slice spacing and axis directions. If you want to use medical images for deep learning then you don’t have to degrade them by saving to JPEG but you can load nrrd images in Python and extract slices using simple numpy array indexing.</p>

---
