---
topic_id: 25912
title: "Failed To Load Hdr File"
date: 2022-10-26
url: https://discourse.slicer.org/t/25912
---

# Failed to load .hdr file

**Topic ID**: 25912
**Date**: 2022-10-26
**URL**: https://discourse.slicer.org/t/failed-to-load-hdr-file/25912

---

## Post #1 by @Sherry (2022-10-26 11:56 UTC)

<p>Hello everyone, I have a question, I can’t upload data to the 3D slicer, although I’ve searched a lot, but I still don’t understand why it doesn’t work. I am attaching my error and would be very happy if someone could help me.</p>
<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cd4fc511bfd6d012c2d85d63014eba52991492c.png" data-download-href="/uploads/short-url/473GHwLClz5Ays7CYeSiKTDgppG.png?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cd4fc511bfd6d012c2d85d63014eba52991492c_2_690x370.png" alt="error" data-base62-sha1="473GHwLClz5Ays7CYeSiKTDgppG" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cd4fc511bfd6d012c2d85d63014eba52991492c_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cd4fc511bfd6d012c2d85d63014eba52991492c_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cd4fc511bfd6d012c2d85d63014eba52991492c_2_1380x740.png 2x" data-dominant-color="797881"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">1920×1031 80.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-10-26 12:06 UTC)

<p>Please check the application log (menu: Help / Report a bug) to see if you find any more hints about what goes wrong.</p>
<p>The <code>.hdr</code> extension typically refers to legacy Analyze/Nifti file format, but the extension may also be used for proprietary file formats. Where does this .hdr file comes from? Do you know what file format is used?</p>

---

## Post #3 by @Sherry (2022-10-26 14:03 UTC)

<p>Thanks a lot for your quick reply. To be honest I did not get the report bug properly.<br>
I downloaded a dataset and this hdr files are CT images that i wanted to load in 3D slicer.<br>
The file format is zip and when you open the zip file there are image, hdr and cls files.</p>

---

## Post #4 by @Sherry (2022-10-26 14:30 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/a/caaa4b903b2c931db90526648a7350748a8d8870.png" data-download-href="/uploads/short-url/sURiTsa27s38G4ybJyQV13AoHVm.png?dl=1" title="report debug" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/caaa4b903b2c931db90526648a7350748a8d8870_2_690x427.png" alt="report debug" data-base62-sha1="sURiTsa27s38G4ybJyQV13AoHVm" width="690" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/caaa4b903b2c931db90526648a7350748a8d8870_2_690x427.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/caaa4b903b2c931db90526648a7350748a8d8870_2_1035x640.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/a/caaa4b903b2c931db90526648a7350748a8d8870_2_1380x854.png 2x" data-dominant-color="EAECEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">report debug</span><span class="informations">1580×980 94.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I attach the report debug.</p>

---

## Post #5 by @Sherry (2022-10-26 14:40 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/3066b16f87a5a8d9019abbae15061569e4c0841c.png" data-download-href="/uploads/short-url/6UaW7WCuQ0kRjz6n1fLKZyJAMji.png?dl=1" title="bug" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3066b16f87a5a8d9019abbae15061569e4c0841c_2_690x362.png" alt="bug" data-base62-sha1="6UaW7WCuQ0kRjz6n1fLKZyJAMji" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3066b16f87a5a8d9019abbae15061569e4c0841c_2_690x362.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3066b16f87a5a8d9019abbae15061569e4c0841c_2_1035x543.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/0/3066b16f87a5a8d9019abbae15061569e4c0841c_2_1380x724.png 2x" data-dominant-color="E8EAEC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">bug</span><span class="informations">1891×993 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @pieper (2022-10-26 14:43 UTC)

<p>I’ve never heard of .cls files, so probably this is a custom format you will need to research in order to figure out what’s in the file and then maybe we can help you load it.</p>

---

## Post #7 by @lassoan (2022-10-26 14:48 UTC)

<p>Where do these images come from? Have you acquired yourself? Using what equipment? If you received it from somewhere, could you ask it in any standard file format, not the equipment-specific custom format?</p>

---

## Post #8 by @Sherry (2022-10-26 14:51 UTC)

<p>LaTeX software installations typically include some CLS files that can be used as document templates.<br>
Cls included text and hdr files included CT images.</p>

---

## Post #9 by @Sherry (2022-10-26 14:53 UTC)

<p><a href="https://figshare.com/collections/A_preclinical_micro-computed_tomography_database_including_3D_whole_body_organ_segmentations/4224377" rel="noopener nofollow ugc">A preclinical micro-computed tomography database including 3D whole body organ segmentations (figshare.com)</a></p>

---

## Post #10 by @pieper (2022-10-26 14:56 UTC)

<p>Okay, then yes, the .hdr/.img pairs are probably analyze files and they should load in Slicer if you put them in the same folder and load the .hdr file, but the error log indicates some failure.  Maybe they are so old ITK no longer recognizes them.</p>

---

## Post #11 by @Sherry (2022-10-26 14:58 UTC)

<p>My Professor sent me the link and he can open the files in 3d Slicer but i can not. That’s why i am here for asking help, although i searched a lot but i could not find the solution.</p>

---

## Post #12 by @pieper (2022-10-26 14:59 UTC)

<p>Can you report what versions of Slicer you and your professor are using?</p>

---

## Post #13 by @Sherry (2022-10-26 15:00 UTC)

<p>But it works for my professor, for me not. Do you have any suggestion?</p>

---

## Post #14 by @Sherry (2022-10-26 15:00 UTC)

<p>For me 5.0.3, i have to ask him</p>

---

## Post #15 by @Sherry (2022-10-26 15:14 UTC)

<aside class="quote no-group" data-username="pieper" data-post="12" data-topic="25912" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Can you report what versions of Slicer you and your professor are using?</p>
</blockquote>
</aside>
<p>My professor has also 5.0.3</p>

---

## Post #16 by @pieper (2022-10-26 16:08 UTC)

<p>Can you easily share one example (.hdr/img pair) that works for your professor and not for you?  (e.g. put it on dropbox or google drive and share the link)</p>
<p>Also please report what OS you are both using.</p>

---

## Post #17 by @Sherry (2022-10-26 17:26 UTC)

<p>Okay I will update you soon.</p>

---

## Post #18 by @lassoan (2022-10-26 18:03 UTC)

<p>I’ve checked the data set and it indeed contains Analyze images. They are loaded into Slicer without problems.</p>
<p>Make sure to have the entire image (.hdr and .img files) available in the folder and open the .hdr file.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/82bf12240ac29704e15572c2b05ac2d93871fdfe.png" data-download-href="/uploads/short-url/iEDrbX2DP2sv2vJbdo52LxXMp3g.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82bf12240ac29704e15572c2b05ac2d93871fdfe_2_690x208.png" alt="image" data-base62-sha1="iEDrbX2DP2sv2vJbdo52LxXMp3g" width="690" height="208" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82bf12240ac29704e15572c2b05ac2d93871fdfe_2_690x208.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82bf12240ac29704e15572c2b05ac2d93871fdfe_2_1035x312.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/2/82bf12240ac29704e15572c2b05ac2d93871fdfe_2_1380x416.png 2x" data-dominant-color="3F3F3F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1575×476 22 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When you load the segmentation (Organ*.hdr file) then choose <code>Segmentation</code> in the <code>Description</code> column to indicate that it is a segmented structure (it will make it appear nicely overlaid on the image).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/3/0356ad63b26cfcdc5dc7364ffe8c480e1667466a.jpeg" data-download-href="/uploads/short-url/tx8xdVswJ1ytHX3NvGaiN1rwym.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/0356ad63b26cfcdc5dc7364ffe8c480e1667466a_2_690x407.jpeg" alt="image" data-base62-sha1="tx8xdVswJ1ytHX3NvGaiN1rwym" width="690" height="407" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/0356ad63b26cfcdc5dc7364ffe8c480e1667466a_2_690x407.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/0356ad63b26cfcdc5dc7364ffe8c480e1667466a_2_1035x610.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/3/0356ad63b26cfcdc5dc7364ffe8c480e1667466a_2_1380x814.jpeg 2x" data-dominant-color="444643"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1133 162 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The .cls files describe label names and colors. You can manually edit the file in any text editor to bring it into Slicer’s <a href="https://slicer.readthedocs.io/en/latest/developer_guide/modules/colors.html#discrete-scale-color-lookup-table">.ctbl format</a>. If you save that .ctbl file and load it into Slicer then after that when loading the segmentation file you can choose that .ctbl file in the Options column, which will make the segmentation loaded with correct segment names and colors.</p>

---

## Post #19 by @Sherry (2022-10-28 11:00 UTC)

<p>Thank you very much for your time and help.<br>
Now it works properly. Thanks a lot for your complete explanation.</p>

---
