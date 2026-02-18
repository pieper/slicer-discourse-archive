# What encoding format does mha file use?

**Topic ID**: 20933
**Date**: 2021-12-06
**URL**: https://discourse.slicer.org/t/what-encoding-format-does-mha-file-use/20933

---

## Post #1 by @Junshi_Peng (2021-12-06 17:07 UTC)

<p>I am trying to adjusting the header of .mha files, adding transform information into the .mha header by using a python script. But i’m facing a problem finding the correct encoding format to read and write the .mha file, and every time I got invalid output that can neither be uncompressed by VolumeReconstructor command line nor be rendered in 3D Slicer interface. Which encoding format does mha file use? and which one should I use to read and write the .mha file? Great Thank</p>

---

## Post #2 by @adamrankin (2021-12-06 17:08 UTC)

<p>Is this a sequence .mha file? Could you post the error(s) that you get?</p>

---

## Post #3 by @Junshi_Peng (2021-12-07 02:47 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bafbf5c06255dec7ab13f2512f7b1fea11ef4628.png" data-download-href="/uploads/short-url/qG8D8uP6uiXVmhjpDzANs2wRtJS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bafbf5c06255dec7ab13f2512f7b1fea11ef4628.png" alt="image" data-base62-sha1="qG8D8uP6uiXVmhjpDzANs2wRtJS" width="690" height="248" data-dominant-color="140B07"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1199×431 30.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Yes, I tried to adjust a .mha file of a png sequence, and after I inserted a header of transform, the .mha became unreadable.<br>
Here is the screen shot of the .mha file with inserted header, all following the sample data format.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed38059c515dfce101acf79e09d1f3da120fdf25.png" data-download-href="/uploads/short-url/xQxbArf4xxR28MUIre14GnAAosZ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/ed38059c515dfce101acf79e09d1f3da120fdf25.png" alt="image" data-base62-sha1="xQxbArf4xxR28MUIre14GnAAosZ" width="690" height="320" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1892×880 54.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @Junshi_Peng (2021-12-08 01:28 UTC)

<p>By the way, does EditSequenceFile.cxx in PlusCommon have the function of reading and editing png sequence? Thank you!</p>

---

## Post #5 by @adamrankin (2021-12-08 01:40 UTC)

<p>I don’t think it can do png sequence. The pixel data is stored as RGB, either compressed (zip) or uncompressed.</p>
<p>In the past I have first used ImageJ with the MetaImage plugins to load a sequence of images and then write it out into an mha (uncompressed). Then I’ve manually added the transform data into the header with notepad++</p>

---

## Post #7 by @Junshi_Peng (2021-12-08 02:14 UTC)

<p>So, can I understand it in this way, that in 3D Slicer, the encoding format of mha is metadata, and only metadata, which can only be edited or added lines by plugins related to itk? Is the notepad++ you’ve mentioned also have itk plugin? Thanks!</p>

---

## Post #8 by @adamrankin (2021-12-08 02:25 UTC)

<p>mha is metadata and image data. itk can read metadata, but does not recognize a number of tags related to sequences.</p>
<p>notepad++ is just a text editor, which you can use to edit the metadata part of the file.</p>

---

## Post #10 by @Junshi_Peng (2021-12-08 02:36 UTC)

<p>I’ve used the PSPad and windows txt editor before, as well as made a simple python script to edit a mha file’s header, but they all returned the error above. It seems not all text editors can do this job, due to the encoding format of mha file, I think.</p>

---

## Post #11 by @jamesobutler (2021-12-08 02:51 UTC)

<p>It is easier to put a MetaImage into .mhd+.raw files rather than the single .mha file. Then you can edit the metadata in the .mhd file without any issues related to encoding that could corrupt the .mha.</p>

---

## Post #12 by @Junshi_Peng (2021-12-08 03:32 UTC)

<p>Yeah this works good. Great thanks</p>

---
