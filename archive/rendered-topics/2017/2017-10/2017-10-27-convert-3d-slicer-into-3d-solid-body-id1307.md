# Convert 3D slicer into 3D solid body

**Topic ID**: 1307
**Date**: 2017-10-27
**URL**: https://discourse.slicer.org/t/convert-3d-slicer-into-3d-solid-body/1307

---

## Post #1 by @111 (2017-10-27 15:20 UTC)

<p>Hi my friends<br>
i need  some help<br>
i want convert 3D stl into Solidwork solid body</p>

---

## Post #2 by @ihnorton (2017-10-27 15:22 UTC)

<p>You need to export to STL or similar supported format. There are many previous discussions, please use search to find them:</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59343d5f72f59119ba4d377fe8481bead7123082.png" alt="image" data-base62-sha1="cJ8pUL8VOzzgu31lvVVwY4vhcqu" width="473" height="412"></p>

---

## Post #3 by @111 (2017-10-27 15:32 UTC)

<p>i already have .stl<br>
i find method to convert CT scan into stl<br>
BUT<br>
i need method to convert CT scan image into 3D solid body not graphics, so i can use it in solidwork software to do mechanical analysis( simulation and other objectives)</p>
<p>please help<br>
thanks</p>

---

## Post #4 by @pieper (2017-10-27 15:48 UTC)

<p>I haven’t used it myself, but you could try the Cleaver extension and let us know how it goes:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Extensions/CleaverExtension" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Extensions/CleaverExtension</a></p>

---

## Post #5 by @lassoan (2017-10-27 15:56 UTC)

<p>FEA packages that can work with arbitrary geometries often have pre-processor component that can create volumetric mesh from surface mesh.</p>

---

## Post #6 by @111 (2017-10-27 17:29 UTC)

<p>in simple word i mean</p>
<p>i have CT image of camels skull i want import it as solid body in SOLIDWORK software<br>
is there any method in slicer do that?</p>
<p>i am waiting for you<br>
thanks</p>

---

## Post #7 by @lassoan (2017-10-29 12:03 UTC)

<p>You may try Cleaver (either the Slicer extension or the command-line tool - <a href="https://www.sci.utah.edu/cibc-software/cleaver.html">https://www.sci.utah.edu/cibc-software/cleaver.html</a>) or Solidworks built-in meshers (<a href="http://help.solidworks.com/2014/english/solidworks/cworks/c_background_on_meshing.htm">http://help.solidworks.com/2014/english/solidworks/cworks/c_background_on_meshing.htm</a>).</p>

---

## Post #8 by @lassoan (2017-10-30 19:00 UTC)

<p>I’ve added a new extension, <strong>Segment Mesher</strong> - it’ll be available in tomorrow’s nightly build. It can create volumetric meshes using either Cleaver2 or TetGen. See more information here: <a href="https://github.com/lassoan/SlicerSegmentMesher">https://github.com/lassoan/SlicerSegmentMesher</a></p>
<p>          <a href="https://raw.githubusercontent.com/lassoan/SlicerSegmentMesher/master/Screenshot01.jpg" target="_blank" rel="nofollow ugc noopener" class="onebox">
            <img src="https://raw.githubusercontent.com/lassoan/SlicerSegmentMesher/master/Screenshot01.jpg" width="690" height="426">
          </a>
</p>
<p>          <a href="https://raw.githubusercontent.com/lassoan/SlicerSegmentMesher/master/Screenshot02.gif" target="_blank" rel="nofollow ugc noopener" class="onebox">
            <img src="https://raw.githubusercontent.com/lassoan/SlicerSegmentMesher/master/Screenshot02.gif" width="644" height="500">
          </a>
</p>

---
