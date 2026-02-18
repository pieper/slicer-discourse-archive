# Python command tooltips

**Topic ID**: 40279
**Date**: 2024-11-19
**URL**: https://discourse.slicer.org/t/python-command-tooltips/40279

---

## Post #1 by @Aidan (2024-11-19 22:12 UTC)

<p>The <a href="https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#how-to-find-a-python-function-for-any-slicer-features" rel="noopener nofollow ugc">current recommendation</a> for users wishing to learn how to Python script Slicer operations that they are already familiar with in the GUI is rather convoluted and time consuming. It involves searching the Slicer GitHub repository for strings from the relevant field in the GUI.</p>
<p>A vastly more user-friendly method (employed by Blender and other software) is to provide an optional feature that enables ‘tool tips’, where hovering the cursor over any interactive component of the GUI results in a tool tip window displaying the associated underlying Python variable.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba1a3d398dc6792a87895d26e0ab7695675f8a66.jpeg" data-download-href="/uploads/short-url/qyl1EpRvelBxxTtIYyPsTyfPul0.jpeg?dl=1" title="Screenshot 2024-11-19 at 10.55.27 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba1a3d398dc6792a87895d26e0ab7695675f8a66_2_690x386.jpeg" alt="Screenshot 2024-11-19 at 10.55.27 AM" data-base62-sha1="qyl1EpRvelBxxTtIYyPsTyfPul0" width="690" height="386" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba1a3d398dc6792a87895d26e0ab7695675f8a66_2_690x386.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba1a3d398dc6792a87895d26e0ab7695675f8a66_2_1035x579.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba1a3d398dc6792a87895d26e0ab7695675f8a66_2_1380x772.jpeg 2x" data-dominant-color="5A5959"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-11-19 at 10.55.27 AM</span><span class="informations">2316×1298 367 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Alternatively, having an option for all GUI interactions to be printed to the Python interpreter window in Slicer (like in FreeCAD, for example) may be even more convenient since it would allow the user to copy and paste Python commands into their scripts.</p>

---

## Post #2 by @pieper (2024-11-19 22:36 UTC)

<p>I think everyone agrees this would be great <img src="https://emoji.discourse-cdn.com/twitter/+1.png?v=12" title=":+1:" class="emoji" alt=":+1:" loading="lazy" width="20" height="20"></p>
<p>But it’s not clear how it would be implemented for Slicer.  Suggestions welcome.</p>

---
