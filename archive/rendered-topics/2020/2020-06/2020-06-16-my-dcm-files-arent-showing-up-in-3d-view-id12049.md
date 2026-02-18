# My DCM files aren't showing up in 3D View?

**Topic ID**: 12049
**Date**: 2020-06-16
**URL**: https://discourse.slicer.org/t/my-dcm-files-arent-showing-up-in-3d-view/12049

---

## Post #1 by @Wolf1471 (2020-06-16 02:22 UTC)

<p>So I’m following along with this tutorial provided on their documentation page:</p><div class="youtube-onebox lazy-video-container" data-video-id="Uht6Fwtr9hE" data-video-title="How to segment multiple vertebrae in spine CT for 3D printing" data-video-start-time="" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=Uht6Fwtr9hE" target="_blank" class="video-thumbnail" rel="noopener nofollow ugc">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/Uht6Fwtr9hE/maxresdefault.jpg" title="How to segment multiple vertebrae in spine CT for 3D printing" width="" height="">
  </a>
</div>

<p>To turn some .dcm files i was provided with into either .stl or .obj to import into Maya or 3ds Max. I followed up to 4 minutes in. The first thing I noticed is they’re button says “Create surface” and has done the video mine says “Show 3D” however when clicking it nothing appears in my 3D space. I’m not sure what I’m missing here I needed to do? This is my first time with the program and I need to convert some CT scans of Teeth into 3D models</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d7ff6a137310426e3a12bf6ee6172403134cd90.png" data-download-href="/uploads/short-url/kbLtZ8QBxrrzYPkqFm3yORd9vji.png?dl=1" title="slicererror" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d7ff6a137310426e3a12bf6ee6172403134cd90_2_690x475.png" alt="slicererror" data-base62-sha1="kbLtZ8QBxrrzYPkqFm3yORd9vji" width="690" height="475" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d7ff6a137310426e3a12bf6ee6172403134cd90_2_690x475.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/d/8d7ff6a137310426e3a12bf6ee6172403134cd90_2_1035x712.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/d/8d7ff6a137310426e3a12bf6ee6172403134cd90.png 2x" data-dominant-color="B0B1C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicererror</span><span class="informations">1264×871 49.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-06-16 02:38 UTC)

<p>Show 3D button (old name: Create surface) displays the segments that you created. If you haven’t added any segments or the segments are empty then nothing is expected to appear in 3D view.</p>
<p>You can complete any of the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#Segmentation">segmentation tutorials</a> to learn about how to use Segment Editor module.</p>

---
