---
topic_id: 47220
title: "Micro CT larvae with soft tissue"
date: 2026-06-03
url: https://discourse.slicer.org/t/47220
last_bumped: 2026-06-03T23:27:49.167Z
---

# Micro CT larvae with soft tissue

**Topic ID**: 47220
**Date**: 2026-06-03
**URL**: https://discourse.slicer.org/t/micro-ct-larvae-with-soft-tissue/47220

---

## Post #1 by @Rin_2529 (2026-06-03 12:35 UTC)

<p>Hi everyone,</p>
<p>I am working with micro-CT scans of mosquito larvae (~3.97 µm voxel size) and I am trying to generate rendered anatomical visualizations similar to the figures in this paper:</p>
<p><a href="https://www.nature.com/articles/s41598-023-35411-1" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.nature.com/articles/s41598-023-35411-1</a></p>
<p>I hope to create reconstruction of the whole exterior of the body and the interor organs. I currently have reconstructed BMP slice stacks and have imported them into 3D Slicer, and I am importing them with the help of Imagestack. However, I am struggling with the reconstruction/rendering workflow and understanding the best pipeline for reconstructions.</p>
<p>I was wondering what is the recommended workflow in Slicer/SlicerMorph for  micro-CT datasets like insect larvae which is mainly soft tissue( i have used iodine staining to before microCT scanning)? I have aldready masked only the tissues and got rid of the background! I was wondering what I should try using primarily like Volume Rendering, Segment Editor, Surface meshes, Slice rendering or a combination? I am worried that it might be too hard to manually segment all the tissue types because of how small the images are.</p>
<p>This is an image of how my sections on 3D slicer</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/f/1f1c90ee17f4c5020792d575a0ac948df7a226d5.jpeg" data-download-href="/uploads/short-url/4re0giU4o2IqKbjMoIHeTu1N5hr.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f1c90ee17f4c5020792d575a0ac948df7a226d5_2_690x446.jpeg" alt="image" data-base62-sha1="4re0giU4o2IqKbjMoIHeTu1N5hr" width="690" height="446" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f1c90ee17f4c5020792d575a0ac948df7a226d5_2_690x446.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f1c90ee17f4c5020792d575a0ac948df7a226d5_2_1035x669.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/f/1f1c90ee17f4c5020792d575a0ac948df7a226d5_2_1380x892.jpeg 2x" data-dominant-color="AEAEB2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1243 229 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>and this is how my volume rendering looks, ( i have played with the transfer function and i amnot able to improve it)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bffa197566679732346853e060e15b3e45e30117.jpeg" data-download-href="/uploads/short-url/roj20JZY0v7nMKqoJt5tI3FDfGT.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bffa197566679732346853e060e15b3e45e30117_2_690x445.jpeg" alt="image" data-base62-sha1="roj20JZY0v7nMKqoJt5tI3FDfGT" width="690" height="445" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bffa197566679732346853e060e15b3e45e30117_2_690x445.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bffa197566679732346853e060e15b3e45e30117_2_1035x667.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/f/bffa197566679732346853e060e15b3e45e30117_2_1380x890.jpeg 2x" data-dominant-color="B9BAD4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1241 247 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I would really appreciate guidance!</p>
<p>Thank you!</p>

---

## Post #2 by @pieper (2026-06-03 13:06 UTC)

<p>One place to start is to see if you can get the images in the highest resolution possible from the scanner.  BMP files are typically 8-bit grayscale, which is typically less than the scanner would produce natively.  So definitely check that before you do anything else.  And as a general rule, the better the scan the better the visualizations, so be sure you have optimized your acquisition.</p>
<p>Beyond that, you can do all the things you mentioned in Slicer, and probably more.  There are lots of tutorials, and probably the SlicerMorph ones are closest to your needs.</p>
<p>If you want to share you images people might be able to give more specific guidance.</p>

---

## Post #3 by @Rin_2529 (2026-06-03 16:13 UTC)

<p>Thank you for the replty, we played with the resolution, and this was the highest we were able to get. Addionally I am either only using the last 500 sections and importing it with full resolution or all the sections with Half resolution as I am trying to figure out a wokflowpipeline, especially because my computer is also not able to handle the whole dataset on slicer! Also I was wondering what would you reccomend changing to the transfer function to see iodine stained tissue more clearly. Since there is only a subtle contrast between the different types of tissue, what direction should i try focusing on!</p>
<p>Thank you!</p>

---

## Post #4 by @lassoan (2026-06-03 20:39 UTC)

<p>I would also recommend to use segmentation to assign different colors to different anatomical regions, using Colorize Volume module (provided by Sandbox extension).</p>
<aside class="quote quote-modified" data-post="3" data-topic="32254">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/jaimigray/48/67886_2.png" class="avatar">
    <div class="quote-title__text-content">
      <a href="https://discourse.slicer.org/t/new-colorize-volume-module/32254/3">New Colorize Volume module</a> <a class="badge-category__wrapper " href="/c/community/success-stories/29"><span data-category-id="29" style="--category-badge-color: #92278F; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #F7941D;" data-parent-category-id="12" data-drop-close="true" class="badge-category --style-square --has-parent" title="This is the place where you can share how Slicer helped your work. Describe your project and how Slicer was useful in achieving your goal. Include reference to any publication(s) and if possible also add a few nice images or links to videos."><span class="badge-category__name">Success stories</span></span></a>
    </div>
  </div>
  <blockquote>
    To continue this thread, I would like to show you more rattlesnake images, this time I used to Colorize volume module to render the skull inside the transparent skin 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d650ff08eb9fc46d32be5aa8848c2358339798f.jpeg" data-download-href="/uploads/short-url/kaPQACpUtzzgxqCdmMPV1jigIfZ.jpeg?dl=1" title="72544-skull-with-skin" rel="noopener nofollow ugc">[72544-skull-with-skin]</a> 
Then I tried without the skull segment, using the whole volume to render the skull instead. This gave me control over the skull colormap. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/9/992a55ed9daacfe0c7672a7756b738718d647978.jpeg" data-download-href="/uploads/short-url/lQXKUM6cMtAPLxaclcRLuqW6cFG.jpeg?dl=1" title="72544-skull-with-skin-volren" rel="noopener nofollow ugc">[72544-skull-with-skin-volren]</a> 
Then a density colormap for fun! 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/7/87746e5d62bfd825491c6ffb108542083ce6e15c.jpeg" data-download-href="/uploads/short-url/jkhUtXeNwqNyjq60bPl6mQphUmw.jpeg?dl=1" title="72544-skull-with-skin-colmap-redyellow" rel="noopener nofollow ugc">[72544-skull-with-skin-colmap-redyellow]</a>
  </blockquote>
</aside>


---

## Post #5 by @muratmaga (2026-06-03 23:27 UTC)

<aside class="quote no-group" data-username="Rin_2529" data-post="1" data-topic="47220">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/rin_2529/48/79440_2.png" class="avatar"> Rin_2529:</div>
<blockquote>
<p>rendered anatomical visualizations similar to the figures in this paper:</p>
</blockquote>
</aside>
<p>These figures are actually very simple to reproduce, but there is a trick to it. Make sure the slice views are turned on in the 3D view, and the slice being shown and the crop positions are identical.  here is an example. I specifically set the volume rendering color a little different so that it is clear what the 2D slice view is adding. Default cropped internal rendering:</p>
<ol>
<li>Default 3D cropped rendering:</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abaca123da6c9d6b4ba46404e9755d4e05c757b4.jpeg" data-download-href="/uploads/short-url/ouHvgHtUwSzALHEqhiOmheVeUxS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abaca123da6c9d6b4ba46404e9755d4e05c757b4_2_580x500.jpeg" alt="image" data-base62-sha1="ouHvgHtUwSzALHEqhiOmheVeUxS" width="580" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abaca123da6c9d6b4ba46404e9755d4e05c757b4_2_580x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abaca123da6c9d6b4ba46404e9755d4e05c757b4_2_870x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abaca123da6c9d6b4ba46404e9755d4e05c757b4_2_1160x1000.jpeg 2x" data-dominant-color="38363B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1483×1278 182 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<ol start="2">
<li>When you turn on the slice visibility</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3feba7f64bdca7e8acb68cde82dfbc4138bc444.jpeg" data-download-href="/uploads/short-url/rXQRk0UX4WFvSoYsLNdnu0phTKY.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3feba7f64bdca7e8acb68cde82dfbc4138bc444_2_584x499.jpeg" alt="image" data-base62-sha1="rXQRk0UX4WFvSoYsLNdnu0phTKY" width="584" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3feba7f64bdca7e8acb68cde82dfbc4138bc444_2_584x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3feba7f64bdca7e8acb68cde82dfbc4138bc444_2_876x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c3feba7f64bdca7e8acb68cde82dfbc4138bc444_2_1168x998.jpeg 2x" data-dominant-color="36363C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1482×1267 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
