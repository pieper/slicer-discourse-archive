# Exporting Segmentation to OBJ and 3D Viewer

**Topic ID**: 22404
**Date**: 2022-03-09
**URL**: https://discourse.slicer.org/t/exporting-segmentation-to-obj-and-3d-viewer/22404

---

## Post #1 by @Eserval (2022-03-09 13:04 UTC)

<p>Hello everyone,</p>
<p>Hello everyone,</p>
<p>I’m having a problem exporting the slicers to OBJ file. I believe there is an error in the lighting and transparency settings during the creation of the OBJ file.<br>
When loading the file in the Online 3D Viewer, the 100% opaque parts appear transparent and the transparent ones appear opaque but with very bad lighting. Is there any way to configure these settings before exporting?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/8/d86457b340167f00d59f1d6f8711f3c4801b05c7.jpeg" data-download-href="/uploads/short-url/uSi7edelHi3xUSD3g0J3aSxtNYj.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d86457b340167f00d59f1d6f8711f3c4801b05c7_2_690x349.jpeg" alt="image" data-base62-sha1="uSi7edelHi3xUSD3g0J3aSxtNYj" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d86457b340167f00d59f1d6f8711f3c4801b05c7_2_690x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d86457b340167f00d59f1d6f8711f3c4801b05c7_2_1035x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d86457b340167f00d59f1d6f8711f3c4801b05c7_2_1380x698.jpeg 2x" data-dominant-color="B9B3B2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×972 65 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2022-03-09 14:58 UTC)

<p>I would recommend to use SlicerOpenAnatomy for web viewer export. See detailed instructions <a href="https://github.com/PerkLab/SlicerOpenAnatomy/">here</a>.</p>
<p>If you export in glTF format (supported by <a href="http://3dviewer.net">3dviewer.net</a> that you show in your screenshot above) then not just transparency is correct but all segment names and even the hierarchy. See some more information and example in this post:</p>
<aside class="quote quote-modified" data-post="15" data-topic="17734">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/open-source-human-anatomy-atlas/17734/15">Open source Human Anatomy Atlas</a> <a class="badge-category__wrapper " href="/c/community/openanatomy/25"><span data-category-id="25" style="--category-badge-color: #0088CC; --category-badge-text-color: #FFFFFF; --parent-category-badge-color: #F7941D;" data-parent-category-id="12" data-drop-close="true" class="badge-category --has-parent"><span class="badge-category__name">OpenAnatomy</span></span></a>
  </div>
  <blockquote>
    Exactly! 
I would also add that since we discussed this we spent some more time with gltf and available web viewers and improved the SlicerOpenAnatomy extension. As a result we now have a very good workflow for creating and share models: 

Create/edit segmentation using Segment Editor
Export segmentation to glTF format using SlicerOpenAnatomy extension. The glTF file stores segment names, hierarchy, and display properties. We use simple shading and no texture, but we could specify more interest…
  </blockquote>
</aside>

<p>Example segmentation exported from Slicer: <a href="https://3dviewer.net/#model=https://raw.githubusercontent.com/lassoan/Test/master/SPL-Abdominal-Atlas.gltf">https://3dviewer.net/#model=https://raw.githubusercontent.com/lassoan/Test/master/SPL-Abdominal-Atlas.gltf</a></p>
<p><a href="https://3dviewer.net/#model=https://raw.githubusercontent.com/lassoan/Test/master/SPL-Abdominal-Atlas.gltf"><img src="https://github.com/PerkLab/SlicerOpenAnatomy/raw/master/Screenshot02.png" alt="" role="presentation" width="" height=""></a></p>

---

## Post #3 by @Eserval (2022-03-10 05:02 UTC)

<p>Hello Andras,</p>
<p>Thanks so much for your fast answare.<br>
For some reason, exporting as gITF does not bring the opacity configurations and segment names.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/1/2149fffd1c8a919cf4bbc909ba048bdf9804c72f.jpeg" data-download-href="/uploads/short-url/4KuiDT2gkuk0wia7AadHIjyJP6n.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2149fffd1c8a919cf4bbc909ba048bdf9804c72f_2_690x334.jpeg" alt="image" data-base62-sha1="4KuiDT2gkuk0wia7AadHIjyJP6n" width="690" height="334" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2149fffd1c8a919cf4bbc909ba048bdf9804c72f_2_690x334.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2149fffd1c8a919cf4bbc909ba048bdf9804c72f_2_1035x501.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2149fffd1c8a919cf4bbc909ba048bdf9804c72f_2_1380x668.jpeg 2x" data-dominant-color="F3F3F2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1906×923 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fdd3c7bf0b1de4fa583b316f9b7082071f767a8.jpeg" data-download-href="/uploads/short-url/kwGh2hMukJhcGBxWp1scdA75Xfi.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fdd3c7bf0b1de4fa583b316f9b7082071f767a8_2_690x373.jpeg" alt="image" data-base62-sha1="kwGh2hMukJhcGBxWp1scdA75Xfi" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fdd3c7bf0b1de4fa583b316f9b7082071f767a8_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fdd3c7bf0b1de4fa583b316f9b7082071f767a8_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8fdd3c7bf0b1de4fa583b316f9b7082071f767a8_2_1380x746.jpeg 2x" data-dominant-color="B4B2C0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1916×1038 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2022-03-13 05:56 UTC)

<p>You need to use the latest Slicer Preview Release.</p>

---

## Post #5 by @Eserval (2022-03-13 22:48 UTC)

<p>Thanks a lot Andras!</p>

---
