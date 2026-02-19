---
topic_id: 33100
title: "Preserve Colors From Segment Editor Node And Export It As Ni"
date: 2023-11-28
url: https://discourse.slicer.org/t/33100
---

# Preserve colors from segment editor node and export it as Nifti LabelMap

**Topic ID**: 33100
**Date**: 2023-11-28
**URL**: https://discourse.slicer.org/t/preserve-colors-from-segment-editor-node-and-export-it-as-nifti-labelmap/33100

---

## Post #1 by @Vishal_P (2023-11-28 22:14 UTC)

<p>Slicer 5.2.2</p>
<p>Hello, i am currently using segment editor and selected Generic Color Table and made following sample segments.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/8/08c66f807055239c80892465f8dd05263b056e71.jpeg" data-download-href="/uploads/short-url/1fCXTddk0XdscfN9GJtdsJgcLpD.jpeg?dl=1" title="segment_editor" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08c66f807055239c80892465f8dd05263b056e71_2_690x214.jpeg" alt="segment_editor" data-base62-sha1="1fCXTddk0XdscfN9GJtdsJgcLpD" width="690" height="214" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08c66f807055239c80892465f8dd05263b056e71_2_690x214.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08c66f807055239c80892465f8dd05263b056e71_2_1035x321.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/8/08c66f807055239c80892465f8dd05263b056e71_2_1380x428.jpeg 2x" data-dominant-color="2D3032"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segment_editor</span><span class="informations">1903×592 120 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and then i move the segments to segmentation module and export it as a new label map, once the new label map is created and the segments are exported to the new LabelMap node, on the main screen i selected the new label map and it was preserving the segment colors.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/c/9c6b402267f0777ee70cd71fb7ca84f8e494714c.jpeg" data-download-href="/uploads/short-url/mjKgEq9QJY53PRgvXuOPHI98XlW.jpeg?dl=1" title="segmentations_1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c6b402267f0777ee70cd71fb7ca84f8e494714c_2_690x311.jpeg" alt="segmentations_1" data-base62-sha1="mjKgEq9QJY53PRgvXuOPHI98XlW" width="690" height="311" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c6b402267f0777ee70cd71fb7ca84f8e494714c_2_690x311.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c6b402267f0777ee70cd71fb7ca84f8e494714c_2_1035x466.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/c/9c6b402267f0777ee70cd71fb7ca84f8e494714c_2_1380x622.jpeg 2x" data-dominant-color="2C2E30"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentations_1</span><span class="informations">1900×858 192 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/86b11bb74b871c2e76bf09bf96c321ca9d5aba64.jpeg" data-download-href="/uploads/short-url/jdxqTkAiDHu9yOiIYvIZhZ7plOI.jpeg?dl=1" title="segmentations_2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86b11bb74b871c2e76bf09bf96c321ca9d5aba64_2_690x249.jpeg" alt="segmentations_2" data-base62-sha1="jdxqTkAiDHu9yOiIYvIZhZ7plOI" width="690" height="249" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86b11bb74b871c2e76bf09bf96c321ca9d5aba64_2_690x249.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86b11bb74b871c2e76bf09bf96c321ca9d5aba64_2_1035x373.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/86b11bb74b871c2e76bf09bf96c321ca9d5aba64_2_1380x498.jpeg 2x" data-dominant-color="393838"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentations_2</span><span class="informations">1897×685 140 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>But once i save the label map to my destination folder and reload it again with the scan, the colors are not preserved. (its changing to color code 1 and  color code 2)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d6ba7643d9df5ac812aac89a5d1beef93ff72eb.png" data-download-href="/uploads/short-url/kb3YbllQYgspZMNq4GVMlZGHStB.png?dl=1" title="Screenshot 2023-11-28 164512" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d6ba7643d9df5ac812aac89a5d1beef93ff72eb_2_678x500.png" alt="Screenshot 2023-11-28 164512" data-base62-sha1="kb3YbllQYgspZMNq4GVMlZGHStB" width="678" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d6ba7643d9df5ac812aac89a5d1beef93ff72eb_2_678x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d6ba7643d9df5ac812aac89a5d1beef93ff72eb.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d6ba7643d9df5ac812aac89a5d1beef93ff72eb.png 2x" data-dominant-color="444640"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-11-28 164512</span><span class="informations">881×649 152 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I want to preserve the colors that have been used at the segment editor in the saved Nifti label map. i need the output folder to have a Nifti LabelMap as i will be using python to read Nifti files and extract segmented regions based on the color codes in the LabelMap.</p>

---

## Post #2 by @muratmaga (2023-11-28 23:06 UTC)

<p>This came up recently in <a href="https://discourse.slicer.org/t/label-color-changed-after-saving/33070/7">this thread</a>. This is the important sentence from the documentation:</p>
<p><strong>The label value is index of the color table entry that has the same name as the segment name.</strong></p>
<p>Do you have entries called 31 and 307 in your custom color table?</p>

---

## Post #3 by @Vishal_P (2023-11-29 02:26 UTC)

<p>its not a custom table, i have selected the colors from “GenericColors” and the colors were named 31 and 307. so gave the segments same name.</p>

---

## Post #4 by @muratmaga (2023-11-29 04:24 UTC)

<p>The point is you do have to create a custom color table, if you want the indices to reflect your values.</p>
<p>Saved that genericColor table, somewhere on the disk, and edit with text editor to change the indices (the leftmost value in the rows) to match your indices. Save it. Load into your scene, and export your segmentation one more time to a labelmap by specifying the in the Segmentation module<br>
Here is an example one that exports my labels with indices 35, 42, 74, 500 and 502</p>
<pre><code class="lang-auto"># Color table file /Users/amaga/Documents/35_mic_23strain_mus_template_UCHAR-label.nii.gz-label_ColorTable.ctbl
# 6 values
35 Skull 128 174 128 255
42 Right_Mandible 241 214 145 255
74 Vertebra 177 122 101 255
400 Left_Mandible 111 184 210 255
502 Endocast 216 101 79 255
</code></pre>

---

## Post #5 by @Vishal_P (2023-11-30 20:48 UTC)

<p>there is already a color node called “GenericColors” which is available as one of the standard options in 3D slicer. i was just using this color table.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/178e57f0248cf07156b2e31c0c1498a477ed39eb.png" data-download-href="/uploads/short-url/3mnWZ6rvVhtMlOgmLGEgQKwmP6r.png?dl=1" title="color_node" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/178e57f0248cf07156b2e31c0c1498a477ed39eb_2_690x488.png" alt="color_node" data-base62-sha1="3mnWZ6rvVhtMlOgmLGEgQKwmP6r" width="690" height="488" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/178e57f0248cf07156b2e31c0c1498a477ed39eb_2_690x488.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/7/178e57f0248cf07156b2e31c0c1498a477ed39eb_2_1035x732.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/7/178e57f0248cf07156b2e31c0c1498a477ed39eb.png 2x" data-dominant-color="4F4B4B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">color_node</span><span class="informations">1327×940 101 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However, the error occurs when I export the segment regions created using ‘Segment Editor’ module as a label map using the ‘Segmentations’ module. when I load the saved label file again in a new scene The colors are not preserved, irrespective of any names given to a segment.</p>
<p>I will also give the custom color table solution a try.</p>

---

## Post #6 by @muratmaga (2023-11-30 21:09 UTC)

<aside class="quote no-group" data-username="Vishal_P" data-post="5" data-topic="33100">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vishal_p/48/6438_2.png" class="avatar"> Vishal_P:</div>
<blockquote>
<p>there is already a color node called “GenericColors” which is available as one of the standard options in 3D slicer. i was just using this color table.</p>
</blockquote>
</aside>
<p>You should create a custom table, if you want to use your own colors. As you can see number 1 is green, and two is yellow in GenericColors, and since you specified that it rightly exported the file with those colors and indices.</p>

---

## Post #7 by @muratmaga (2023-11-30 21:26 UTC)

<p><a class="mention" href="/u/vishal_p">@Vishal_P</a> here are some instructiosn with MRHead.<br>
Create three blank segments with names, Red, Blue and Green, and assign those colors to these segments. Then proceed with generating some segmentation like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c10009f544ace5177ce5a8752deebd7127741f38.jpeg" data-download-href="/uploads/short-url/rxmezRH47II0IoKTOy9kQZ4sp0k.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c10009f544ace5177ce5a8752deebd7127741f38_2_650x500.jpeg" alt="image" data-base62-sha1="rxmezRH47II0IoKTOy9kQZ4sp0k" width="650" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c10009f544ace5177ce5a8752deebd7127741f38_2_650x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/1/c10009f544ace5177ce5a8752deebd7127741f38_2_975x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c10009f544ace5177ce5a8752deebd7127741f38.jpeg 2x" data-dominant-color="A2A1A7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1183×910 249 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Go to the segmentations module, and export this as a labelmap (without specfying any color table). Notice that exported labelmap has correct colors. Then save this labelmap and reload this into Slicer, and you will see that colors are now green yellow and brown, because without knowing anything about your custom colors, slicer applied the Generic Color table.</p>
<p>During the export, Segmentations actually exported your custom color table as well. So go to the volumes module and change the assigned color table from the Lookup table and scroll down to find your table (which in my case is a called Segmentation-label_ColorTable). When you switch to this, you should see your original colors.</p>
<p>Now, if you also want to change the indices from 1, 2, 3 to some custom numeric index, you should save this color table to disk, open it and edit the index values and then reload, and re-export using this color table  (e.g., in the screenshot below, the indices in the labelmap is now 100, 200, 300, and colors are the original colors).</p>
<p>The point is, labelmap representation does know not anything about the colors it needs to be assigned. You need to specify that yourself.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a829b4cf2ad1cfa4fb3466bad63fdaa79de5648.jpeg" data-download-href="/uploads/short-url/cUGNkZc2sThzTayO4FYIhwfassM.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a829b4cf2ad1cfa4fb3466bad63fdaa79de5648_2_685x500.jpeg" alt="image" data-base62-sha1="cUGNkZc2sThzTayO4FYIhwfassM" width="685" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a829b4cf2ad1cfa4fb3466bad63fdaa79de5648_2_685x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5a829b4cf2ad1cfa4fb3466bad63fdaa79de5648_2_1027x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a829b4cf2ad1cfa4fb3466bad63fdaa79de5648.jpeg 2x" data-dominant-color="A9AAAD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1291×942 277 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @Vishal_P (2023-12-01 01:05 UTC)

<p>Thanks for the explanation. Now, I understand what is happening. Is there any way that, when reloading the label file in the ‘Add Data into the Scene’ screen and clicking on ‘Show Options,’ it automatically detects the intended color map (in your example, ‘Segmentation-label_ColorTable’)?"</p>
<p>and i also noticed if the segments are directly saved without exporting to label map, in “.seg.nrrd” the colors are preserved.</p>

---

## Post #9 by @muratmaga (2023-12-01 02:11 UTC)

<aside class="quote no-group" data-username="Vishal_P" data-post="8" data-topic="33100">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vishal_p/48/6438_2.png" class="avatar"> Vishal_P:</div>
<blockquote>
<p>if the segments are directly saved without exporting to label map, in “.seg.nrrd” the</p>
</blockquote>
</aside>
<p>You should always save your segmentation in the seg.nrrd format for archival purposes, particularly if you care for data fidelity. labelmap doesn’t have those features hence is only supported as a “Export” format.</p>
<aside class="quote no-group" data-username="Vishal_P" data-post="8" data-topic="33100">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vishal_p/48/6438_2.png" class="avatar"> Vishal_P:</div>
<blockquote>
<p>licking on ‘Show Options,’ it automatically detects the intended color map (in your example, ‘Segmentation-label_ColorTable’)?"</p>
</blockquote>
</aside>
<p>It will be probably be more convenient if you simply have your custom color map added to the Slicer defaults, and you can choose the correct color map from the volume lookup table. I imagine it is also possible to automate this through some customization script.</p>

---
