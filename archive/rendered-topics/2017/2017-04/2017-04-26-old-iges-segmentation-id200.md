# Old IGES segmentation

**Topic ID**: 200
**Date**: 2017-04-26
**URL**: https://discourse.slicer.org/t/old-iges-segmentation/200

---

## Post #1 by @daniel_elizondo (2017-04-26 20:30 UTC)

<p>Hello to everyone,</p>
<p>I’m actually working on a research project in which shoulder segmentations are needed. As I’m “exhuming” some old bone segmented files, the proprietary software being discontinued since a decade (Surfdriver), it is impossible for me to recover proper geometries. I have however the IGES files with the segmented bony structures as a collection of closed contours. So, my question is: can I use 3D slicer (or any extension) to open these IGES contours and regenerate the surfaces/volumes?</p>
<p>I appreciate any comment that could guide me through this.</p>
<p>Best regards,<br>
Daniel E.</p>

---

## Post #2 by @lassoan (2017-04-26 22:15 UTC)

<p>Convert the geometry from IGES to STL using FreeCAD or similar software. You can then load the STL files into Slicer.</p>

---

## Post #3 by @daniel_elizondo (2017-04-26 23:56 UTC)

<p>Hello Andras,</p>
<p>Thanks for the reply! However, I think I didn’t make myself clear in the past message. I cannot directly (although, this is the objective) convert from IGES to STL because these IGES files are a collection of contours, of the segmented geometry. I’m attaching an example of what I have.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d76c30dbf14aa3742ecca3dc05abb09d74e6a3b.png" data-download-href="/uploads/short-url/fCmupCLygXVf2nHioXvp8MrfyRB.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d76c30dbf14aa3742ecca3dc05abb09d74e6a3b.png" alt="image" data-base62-sha1="fCmupCLygXVf2nHioXvp8MrfyRB" width="515" height="500" data-dominant-color="587774"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">670×650 27.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I know I can segment again the original DICOM images in 3D slicer but, if I have already these segmentations in IGES (which I can easily transform to another format for sure), is there any chance to regenerate the surfaces based using the surface generating tools from 3D slicer? Here the main issue is how to “read and interpret” those contours.</p>
<p>Thanks again for your feedback.</p>

---

## Post #4 by @lassoan (2017-04-27 02:32 UTC)

<p>Of course, Slicer can help in this, too. In its <code>SlicerRT</code> extension there are sophisticated algorithms to reconstruct closed surfaces from parallel contours, such as your data set.</p>
<p>For example, this is a polydata consisting of parallel contours, shown in Paraview:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/23860e5c9f7c6cbe450956e41f89bfd98ecf0d38.png" data-download-href="/uploads/short-url/54fVmZJQudrKxrdCauAnXCsG2Gk.png?dl=1" title="image.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/23860e5c9f7c6cbe450956e41f89bfd98ecf0d38_2_690x444.png" width="690" height="444" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/23860e5c9f7c6cbe450956e41f89bfd98ecf0d38_2_690x444.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/23860e5c9f7c6cbe450956e41f89bfd98ecf0d38_2_1035x666.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/23860e5c9f7c6cbe450956e41f89bfd98ecf0d38_2_1380x888.png 2x" data-dominant-color="A0A2AE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">2982×1920 457 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>You need to save each segment as a .vtp (VTK XML polydata) file, adding field data into each file’s header that indicates that it has to be interpreted as parallel set of contours. The easiest to do it by using a text editor, copy-pasting this into the file header:</p>
<pre><code class="lang-auto">&lt;FieldData&gt;
  &lt;Array type="String" Name="Segmentation_MasterRepresentation" NumberOfTuples="1" format="binary"&gt;AQAAAACAAAAPAAAAFwAAAA==eJwLyEnMSyxSSM7PK8kvLWIAAC1zBYk=&lt;/Array&gt;
&lt;/FieldData&gt;
</code></pre>
<p>You can also specify segment name, color, etc. in the field data (optional). You can see/edit field data in ParaView using a Spreadsheet view.</p>
<p>Then, you have to create a .vtm file that lists all your .vtp files (using a text editor, it’s a simple text file).</p>
<p>If you drag-and-drop the vtm file into Slicer, then it loads it as segmentation, which you can show and export as closed surface, labelmap, etc. For example, the contour set above imported as segmentation looks like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/66c87e16a01b7a148429e7ba026f3b370f464fe7.png" data-download-href="/uploads/short-url/eFgfPcG5C9JUsjuTjHCQQCPH8b5.png?dl=1" title="image.png"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/66c87e16a01b7a148429e7ba026f3b370f464fe7_2_690x441.png" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/66c87e16a01b7a148429e7ba026f3b370f464fe7_2_690x441.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/66c87e16a01b7a148429e7ba026f3b370f464fe7_2_1035x661.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/66c87e16a01b7a148429e7ba026f3b370f464fe7_2_1380x882.png 2x" data-dominant-color="607B65"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image.png</span><span class="informations">3000×1920 780 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>An example set of vtp and vtm files is available here:</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://onedrive.live.com/redir?resid=872AF7415C00BFB9%21774720&amp;authkey=%21ANV0W9SGJnI9c-0">
  <header class="source">

      <a href="https://onedrive.live.com/redir?resid=872AF7415C00BFB9%21774720&amp;authkey=%21ANV0W9SGJnI9c-0" target="_blank" rel="noopener">onedrive.live.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:93/96;"><img src="https://p.sfx.ms/icons/v2/Large/Zip.png" class="thumbnail" width="93" height="96"></div>

<h3><a href="https://onedrive.live.com/redir?resid=872AF7415C00BFB9%21774720&amp;authkey=%21ANV0W9SGJnI9c-0" target="_blank" rel="noopener">ContourSetExample.zip</a></h3>

  <p>Compressed (zipped) Folder</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #5 by @daniel_elizondo (2017-04-27 21:18 UTC)

<p>Dear Andras,</p>
<p>Thank you so much! This is exactly what I was looking for. It will be only a matter of converting the IGES contours (defined as a collection of points and closed lines) to the VTP structure, I guess in ASCII format. I’ll be working on it, and hopefully I’ll be able to publish soon here an example of the resulting work.</p>
<p>I appreciate your time and your guide.</p>
<p>Best regards,</p>
<p>Daniel E.</p>

---
