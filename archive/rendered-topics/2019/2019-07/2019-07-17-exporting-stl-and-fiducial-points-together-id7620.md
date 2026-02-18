# Exporting STL and Fiducial Points together

**Topic ID**: 7620
**Date**: 2019-07-17
**URL**: https://discourse.slicer.org/t/exporting-stl-and-fiducial-points-together/7620

---

## Post #1 by @Nicholas.jacobson (2019-07-17 04:32 UTC)

<p>Hi all,<br>
As a 3d print designer, I’m always exporting STL’s. Now, I’m looking to export fiducial points but having trouble. I’ve been placing fiducial points in the volume rendering and then copying their x,y,z coordinates into another program. When I do this the STL and point x,y,z are not coming in a the same location.</p>
<p>Can someone explain why these two coordinate systems are not the same or how I can transfer point coordinates accurately.</p>

---

## Post #2 by @pieper (2019-07-17 12:48 UTC)

<p>Hi Nick -</p>
<p>Probably it’s an LPS/RAS issue (see <a href="https://www.slicer.org/wiki/Coordinate_systems" class="inline-onebox">Coordinate systems - Slicer Wiki</a>)</p>
<p>When you export to STL you need to pick a coordinate system because there’s no standard.  In the .fcsv file the default is RAS (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Markups#File_Format" class="inline-onebox">Documentation/Nightly/Modules/Markups - Slicer Wiki</a>).</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/a/daa2f39af4d4e7f065b8d44229a7b8950cbdb70a.png" alt="image" data-base62-sha1="vc9d3Ze49j2kj1ZGzculSjMBnWG" width="289" height="209"></p>

---
