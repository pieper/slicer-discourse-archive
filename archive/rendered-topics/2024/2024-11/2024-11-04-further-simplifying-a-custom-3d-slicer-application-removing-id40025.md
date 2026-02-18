#  Further Simplifying a Custom 3D Slicer Application: Removing Unneeded Modules and Adding Custom Modules

**Topic ID**: 40025
**Date**: 2024-11-04
**URL**: https://discourse.slicer.org/t/further-simplifying-a-custom-3d-slicer-application-removing-unneeded-modules-and-adding-custom-modules/40025

---

## Post #1 by @nih4t (2024-11-04 22:48 UTC)

<p>Hello,</p>
<p>I’ve successfully built a simplified version of 3D Slicer following this guide from Kitware (<a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/</a>).</p>
<p>Hello,</p>
<p>I’ve successfully built a simplified version of 3D Slicer following <a href="https://www.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">this guide from Kitware</a>.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23c8c926b12e0202c132d13dc68809689db6644e.png" data-download-href="/uploads/short-url/56yTmtxv5NVe7fCNj4WXBHZydwW.png?dl=1" title="Ekran görüntüsü 2024-11-04 143300" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23c8c926b12e0202c132d13dc68809689db6644e_2_690x349.png" alt="Ekran görüntüsü 2024-11-04 143300" data-base62-sha1="56yTmtxv5NVe7fCNj4WXBHZydwW" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23c8c926b12e0202c132d13dc68809689db6644e_2_690x349.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23c8c926b12e0202c132d13dc68809689db6644e_2_1035x523.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/2/3/23c8c926b12e0202c132d13dc68809689db6644e_2_1380x698.png 2x" data-dominant-color="88898D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Ekran görüntüsü 2024-11-04 143300</span><span class="informations">1599×810 51.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Now, I’d like to create an even more streamlined version. Specifically, I’m aiming for a version that only includes options to upload data and visualize volumes. I also need a button that allows me to add custom modules (developed in Python) to the application as needed, post-build.</p>
<p>I’ve already hidden some menus using <code>qCustomAppNameAppMainWindow.cxx</code> as follows</p>
<pre><code class="lang-auto">// Hide the menus
// this-&gt;menubar-&gt;setVisible(false);
// this-&gt;FileMenu-&gt;setVisible(false);
this-&gt;EditMenu-&gt;setVisible(false);
this-&gt;ViewMenu-&gt;setVisible(false);
this-&gt;LayoutMenu-&gt;setVisible(false);
this-&gt;HelpMenu-&gt;setVisible(false);
</code></pre>
<p>However, I think this approach isn’t giving me the minimalist setup I’m looking for. My goal is to completely remove all 3D Slicer default modules, keeping only the necessary structure to load data, view volumes, and easily add my own Python-based modules.</p>
<p>Could anyone advise on which folders and files I should modify to achieve this? Any guidance would be greatly appreciated!</p>

---
