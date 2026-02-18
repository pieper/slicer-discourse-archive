# Markups misalignment with the volume

**Topic ID**: 46137
**Date**: 2026-02-12
**URL**: https://discourse.slicer.org/t/markups-misalignment-with-the-volume/46137

---

## Post #1 by @SANTIAGO_PENDON_MING (2026-02-12 12:12 UTC)

<p>Hi to everyone. I’m using this  script to extract the pointCloud positions in IJK system:</p>
<pre><code class="lang-auto">def RAStoIJK(xyz, volumeNode, RAS = True):
    """
    Transforms a list of points or np array of shape (n,3) in RAS coordinates
    to IJK coordinates. 
    
    :xyz: list of lists (Ex: [[1,2,3], [4,5,6]]) or np array with the RAS coordinates
            of the points.
    :volumeNode: node of the reference images
    :RAS: True if coordinates are in RAS coordinate system (could be LPS)
    """
    
    transf = vtk.vtkMatrix4x4()
    volumeNode.GetRASToIJKMatrix(transf)

    transf = arrayFromVTKMatrix(transf)
    
    correccion = np.array([1, 1, 1]) if RAS else np.array([-1, -1, 1])
    
    puntos_malla = np.hstack((xyz*correccion, np.ones(len(xyz)).reshape(-1, 1))).T

    puntos_ijk = np.round(transf.dot(puntos_malla)).astype(int).T[:, :-1]
    
    return puntos_ijk # Coordenadas en la matriz (vóxeles)



volumeNode = getNode("resliced")

points = array('pointCloud_left')

points_ijk = RAStoIJK(points, volumeNode)

import numpy as np

np.save("points_ijk.npy", points_ijk)

volume = arrayFromVolume(volumeNode)

np.save("volume.npy", volume)

 
</code></pre>
<p>And in the scene I see:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bafd6a142f2325da197292bbaed16f03c0475c75.jpeg" data-download-href="/uploads/short-url/qGbKkzIOizWBD75dBmYbLdnJ82N.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/bafd6a142f2325da197292bbaed16f03c0475c75_2_613x500.jpeg" alt="image" data-base62-sha1="qGbKkzIOizWBD75dBmYbLdnJ82N" width="613" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/bafd6a142f2325da197292bbaed16f03c0475c75_2_613x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/bafd6a142f2325da197292bbaed16f03c0475c75_2_919x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bafd6a142f2325da197292bbaed16f03c0475c75.jpeg 2x" data-dominant-color="D6CEDF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1177×959 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>but when I use this data outside:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93a67a22fc2d08b9e9807c2fdc64c47230712262.jpeg" data-download-href="/uploads/short-url/l4aRy1uyZ0ReAYPDIL2XAYBTI0q.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93a67a22fc2d08b9e9807c2fdc64c47230712262_2_552x500.jpeg" alt="image" data-base62-sha1="l4aRy1uyZ0ReAYPDIL2XAYBTI0q" width="552" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/93a67a22fc2d08b9e9807c2fdc64c47230712262_2_552x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93a67a22fc2d08b9e9807c2fdc64c47230712262.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93a67a22fc2d08b9e9807c2fdc64c47230712262.jpeg 2x" data-dominant-color="D7D3D1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">749×678 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I used to extract data with this code several times and this is the first time that something like this happens. The scene can be found in: <a href="https://drive.google.com/file/d/1CiSP08h5oVePyaFyIzsggmpPjy1tQn-5/view?usp=drive_link" rel="noopener nofollow ugc">https://drive.google.com/file/d/1CiSP08h5oVePyaFyIzsggmpPjy1tQn-5/view?usp=drive_link</a></p>

---

## Post #2 by @lassoan (2026-02-14 04:47 UTC)

<p>If the volume’s IJK axes are not forming a right-handed coordinate system then Slicer reorders the voxel indices when the volume is loaded. I would recommend to always use physical coordinates in files, because applications can freely choose memory layout when they loading a volume, but physical position of objects will always be the same.</p>
<p>To confirm that this voxel reordering causes the problem for you: save the updated volume after loading it into Slicer and use that (instead of the original input volume).</p>

---
