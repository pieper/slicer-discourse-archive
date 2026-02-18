# Release [windows] build of Slicer fails with error on sphinx-build

**Topic ID**: 30602
**Date**: 2023-07-14
**URL**: https://discourse.slicer.org/t/release-windows-build-of-slicer-fails-with-error-on-sphinx-build/30602

---

## Post #1 by @drdH (2023-07-14 13:16 UTC)

<p>Hello Team,<br>
Kindly wanted your help on the below build issue:</p>
<aside class="quote" data-post="6" data-topic="30544">
  <div class="title">
    <div class="quote-controls"></div>
    <img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/release-build-of-slicer-fails-with-error-on-sphinx-build/30544/6">Release build of Slicer fails with error on sphinx-build</a> <a class="badge-category__wrapper " href="/c/dev/5"><span data-category-id="5" data-drop-close="true" class="badge-category " title="The Development category is for discussion of Slicer application and extension programming, software testing, and related topics - similarly to the former slicer-devel mailing list."><span class="badge-category__name">Development</span></span></a>
  </div>
  <blockquote>
    Probably there is something else going wrong with the build.  Look higher up in the logs to see what is going on.  Maybe someone who routinely builds on Windows can offer suggestions.
  </blockquote>
</aside>

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/0/1014dad4dac0a1cc9ac673d41e9b17f91c38983f.png" data-download-href="/uploads/short-url/2igjSYhhHXOil8ACLacCuGY4k4n.png?dl=1" title="grafik" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1014dad4dac0a1cc9ac673d41e9b17f91c38983f_2_690x21.png" alt="grafik" data-base62-sha1="2igjSYhhHXOil8ACLacCuGY4k4n" width="690" height="21" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1014dad4dac0a1cc9ac673d41e9b17f91c38983f_2_690x21.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1014dad4dac0a1cc9ac673d41e9b17f91c38983f_2_1035x31.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/0/1014dad4dac0a1cc9ac673d41e9b17f91c38983f_2_1380x42.png 2x" data-dominant-color="3A3A3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">grafik</span><span class="informations">1840×58 81.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Regards,<br>
Darshan</p>

---

## Post #2 by @lassoan (2023-07-14 13:55 UTC)

<p>Sphinx build is just a warning. It is expected if you haven’t set up sphinx. You can ignore it.</p>
<p>To learn more about the build error, you need to look a the build log. The error list does not contain information about the root cause of the error (I usually search for the first occurrence of <code>: err</code>).</p>

---
