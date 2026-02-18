# ShapePopulationViewer cannot open spharm output

**Topic ID**: 35954
**Date**: 2024-05-06
**URL**: https://discourse.slicer.org/t/shapepopulationviewer-cannot-open-spharm-output/35954

---

## Post #1 by @chz31 (2024-05-06 20:33 UTC)

<p>Hi,</p>
<p>I am trying spharm in Slicer Salt on Windows 11. I directly ran the extension in Slicer. I got two mice mandibles and I filled all the internal holes for the segmentations. I followed the <a href="https://bit.ly/3wSrpKC" rel="noopener nofollow ugc">tutorial</a> from Salt website. The raw VOLs, input VTK, and label maps as well as the output from using the label maps are in this <a href="https://drive.google.com/file/d/1WxUGHAnY5fj-xQpFl0GQSn38-qvE_ctq/view?usp=sharing" rel="noopener nofollow ugc">zip file</a>. The source volumes are 129S1_SVIMJ and 129 X1_XVJ from <a href="https://osf.io/xzj4t/" class="inline-onebox" rel="noopener nofollow ugc">OSF | High Resolution microCT scans of Inbred Mice</a>.</p>
<p>I could not open the output in ShapePopulationViewer. The full log is <a href="https://drive.google.com/file/d/15utNg3UTZ7CkFqardRgNDCwr8E_Qy7WG/view?usp=sharing" rel="noopener nofollow ugc">here</a>.The error message is:</p>
<pre><code class="lang-auto">ShapePopulationViewer standard error:
Qt: Untested Windows version 6.2 detected!
libpng warning: Interlace handling should be turned on when using png_read_image
</code></pre>
<p>I wonder if it is related to how I installed ShapePopulationViewer. I could not find it in the Extension Manager, so I downloaded <a href="https://www.nitrc.org/frs/?group_id=759" rel="noopener nofollow ugc">v1.3.2_windows</a> and added the .exe file to Slicer Modules. However, when I tried to load any file from the spharm output either in shapePopulationViewer in Slicer or the exe file, it just reported the above error and forced closing the app.</p>

---
