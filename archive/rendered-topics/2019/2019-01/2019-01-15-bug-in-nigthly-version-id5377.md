# Bug in nigthly version

**Topic ID**: 5377
**Date**: 2019-01-15
**URL**: https://discourse.slicer.org/t/bug-in-nigthly-version/5377

---

## Post #1 by @Alex_Vergara (2019-01-15 16:45 UTC)

<p>Version 4.11.0<br>
Expected behaviour: when using the slicer.util.plot in a python interpreter with more than 2 plots in the same graphic it shows a legend, that legend was changeable by plt.GetNthPlotSeriesNode(i).SetName(name_i) and all elements changed their name respectively.<br>
Actual behaviour: only the last element change name and the rest take a default PlotSeries_i name regardless of the name I gave. This was not happening in 4.10.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5e437539d6b80478a5a61ba8210b808ad2dc4c5.png" data-download-href="/uploads/short-url/uwaEqeJwa0NmeN2ft8OcU2PpVE9.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5e437539d6b80478a5a61ba8210b808ad2dc4c5_2_690x357.png" alt="image" data-base62-sha1="uwaEqeJwa0NmeN2ft8OcU2PpVE9" width="690" height="357" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5e437539d6b80478a5a61ba8210b808ad2dc4c5_2_690x357.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5e437539d6b80478a5a61ba8210b808ad2dc4c5_2_1035x535.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5e437539d6b80478a5a61ba8210b808ad2dc4c5_2_1380x714.png 2x" data-dominant-color="7A7A74"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1891×979 235 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
