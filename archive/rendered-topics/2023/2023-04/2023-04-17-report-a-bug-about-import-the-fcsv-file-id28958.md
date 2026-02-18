# Report a bug about import the fcsv file

**Topic ID**: 28958
**Date**: 2023-04-17
**URL**: https://discourse.slicer.org/t/report-a-bug-about-import-the-fcsv-file/28958

---

## Post #1 by @Chuan (2023-04-17 11:46 UTC)

<p>Hi,</p>
<p>I would like to report a bug when I load the fcsv files.<br>
I export landmarks as fcsv files, but when I want to load them in a new slicer windows. I found the value was changed to the opposite value automatically.<br>
For example, these are first two landmarks in the fcsv file.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/562f51eb86b30b6ac52d10a6c68d457d0d3db9d1.png" data-download-href="/uploads/short-url/ciqrAVHQ2jFSvo10hwut3AYHnSV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/562f51eb86b30b6ac52d10a6c68d457d0d3db9d1.png" alt="image" data-base62-sha1="ciqrAVHQ2jFSvo10hwut3AYHnSV" width="690" height="90" data-dominant-color="303030"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">731×96 5.79 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
You can see the x value are 2.989 and 3.341.<br>
But when I loaded in slicer, the value was changed to the reverse value -2.989 and -3.341<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77f08bc93a6de15e9246380b7ccfddb3dc078fed.png" alt="image" data-base62-sha1="h72byT8OT0LTab2pxI9P1LWDbD7" width="592" height="109"></p>
<p>Does anyone meet the similar bug before? Until now I have not solved this problem.</p>
<p>Best regards,<br>
Chuan</p>

---

## Post #2 by @jamesobutler (2023-04-17 12:04 UTC)

<p>Your file is saved in the LPS coordinate system. As shown in Slicer, it is RAS coordinates. Have a read about the coordinate systems:</p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank" rel="noopener nofollow ugc">https://www.slicer.org/wiki/Coordinate_systems</a></p>

---
