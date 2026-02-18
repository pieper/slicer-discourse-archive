# Access to List of Segmented Organs

**Topic ID**: 40080
**Date**: 2024-11-08
**URL**: https://discourse.slicer.org/t/access-to-list-of-segmented-organs/40080

---

## Post #1 by @Filippo_Parronchi (2024-11-08 11:57 UTC)

<p>Hello everyone.<br>
After applying the “totalSegmentator” module to my volume, I obtain a list of all segmented structures with their respective names, as shown in the figure. I would like to know how, through a Python script, I can access this list of structures by the name of the organ I am interested in (for example, “liver”), in order to get its corresponding index. This will be useful for then entering it as the “Label Value” in the “Mask Scalar Volume” module, allowing me to treat that object as an independent volume.<br>
Thanks a lot!!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/576e147618ee81fd5915d531ca6d5b7701cc15b9.png" data-download-href="/uploads/short-url/ctrnSgxtpEMrXYeblHwMmpfUXOx.png?dl=1" title="screen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/576e147618ee81fd5915d531ca6d5b7701cc15b9_2_690x360.png" alt="screen" data-base62-sha1="ctrnSgxtpEMrXYeblHwMmpfUXOx" width="690" height="360" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/576e147618ee81fd5915d531ca6d5b7701cc15b9_2_690x360.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/576e147618ee81fd5915d531ca6d5b7701cc15b9_2_1035x540.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/576e147618ee81fd5915d531ca6d5b7701cc15b9_2_1380x720.png 2x" data-dominant-color="BAB8B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screen</span><span class="informations">3840×2008 490 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-11-10 04:38 UTC)

<p>What would you like to achieve? Create a fake CT from a segmentation so that you can import the segmentation into some clinical software?</p>

---

## Post #3 by @Filippo_Parronchi (2024-11-10 22:26 UTC)

<p>I needed access to the list so I could use the index related to the name of the organ of interest to set it as an input parameter for the “Mask Scalar Volume” module, specifically as the value of the Label Map to use in creating a new node. However, I might be able to work around this and solve it differently.</p>
<p>The aspect I need the most at the moment is the one discussed in this other topic:</p>
<aside class="quote quote-modified" data-post="1" data-topic="40082">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/filippo_parronchi/48/77852_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/how-to-set-parameters-in-maskscalarvolume-module-via-console/40082">How to set parameters in "MaskScalarVolume" module via console</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Hello, I am trying to run the “MaskScalarVolume” CLI module via Python console. With the lines of code shown in the figure, I am able to open the module interface and execute it (apply). I would like to know how to modify the input parameters indicated by the red arrow through the Python console. 
 <a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/0/f00c931ab1e00a41ed25728e9ee64eb1ff660352.png" data-download-href="/uploads/short-url/yfzx6o3Q1vXxXzFYSgSUu27PM66.png?dl=1" title="Slicer" rel="noopener nofollow ugc">[Slicer]</a> 
Thank you
  </blockquote>
</aside>

<p>I would be very grateful for any help with this!<br>
Thanks a lot!</p>

---

## Post #4 by @lassoan (2024-11-11 01:40 UTC)

<p>Mask scalar volume is no longer relevant. Masking is now available in Segment Editor module (<code>Mask volume</code> effect).</p>

---
