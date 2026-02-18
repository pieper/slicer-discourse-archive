# Retreive triangle from Flying edges mesh

**Topic ID**: 13773
**Date**: 2020-09-30
**URL**: https://discourse.slicer.org/t/retreive-triangle-from-flying-edges-mesh/13773

---

## Post #1 by @Nina (2020-09-30 12:54 UTC)

<p>Hi;</p>
<p>I have closed surface generated from segmentation using Flying edges. I want retreive triangle and points from each cell</p>
<p>here is my code:</p>
<p>for(int i = 0; i &lt; FEMesh-&gt;GetNumberOfCells(); i++)<br>
{<br>
vtkSmartPointer cell = FEMesh-&gt;GetCell(i);<br>
vtkSmartPointer triangle = vtkTriangle::SafeDownCast(cell);<br>
double p0[3];<br>
double p1[3];<br>
double p2[3];<br>
triangle-&gt;GetPoints()-&gt;GetPoint(0, p0);<br>
triangle-&gt;GetPoints()-&gt;GetPoint(1, p1);<br>
triangle-&gt;GetPoints()-&gt;GetPoint(2, p2);</p>
<pre><code>   triangle_points-&gt;InsertNextPoint(p0[0], p0[1], p0[2]);
   triangle_points-&gt;InsertNextPoint(p1[0], p1[1], p1[2]);
   triangle_points-&gt;InsertNextPoint(p2[0], p2[1], p2[2]);
   
   triangles-&gt;InsertNextCell(triangle);
</code></pre>
<p>}</p>
<p>in order to check if all triangle and points are well recovered, I stored points and triangles in vtkPolydata  (the mesh is deformed, I want keep the initial form how can I obtain this). see attached figure of deformed mesh</p>
<p>Polydata-&gt;SetPoints(triangle_points);<br>
Polydata-&gt;SetPolys(triangles);</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b38a2f90ee90c3b58abd39b0959eb4e77ebf8b8.png" data-download-href="/uploads/short-url/fiwqPnCONJgLTQUBoRPlL0yCgdy.png?dl=1" title="mesh" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b38a2f90ee90c3b58abd39b0959eb4e77ebf8b8_2_690x447.png" alt="mesh" data-base62-sha1="fiwqPnCONJgLTQUBoRPlL0yCgdy" width="690" height="447" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b38a2f90ee90c3b58abd39b0959eb4e77ebf8b8_2_690x447.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b38a2f90ee90c3b58abd39b0959eb4e77ebf8b8_2_1035x670.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b38a2f90ee90c3b58abd39b0959eb4e77ebf8b8.png 2x" data-dominant-color="646777"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mesh</span><span class="informations">1158×751 88.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thank’s in advance</p>

---

## Post #2 by @Nina (2020-09-30 14:37 UTC)

<p>I found my bug!</p>
<p>here is solution:</p>
<p>FEMesh-&gt;GetPolys()-&gt;InitTraversal();<br>
vtkSmartPointer idList = vtkSmartPointer::New();<br>
while( FEMesh-&gt;GetPolys()-&gt;GetNextCell(idList))<br>
{<br>
for(vtkIdType pointId = 0; pointId &lt; idList-&gt;GetNumberOfIds(); pointId++){<br>
FEMesh-&gt;GetPoint(idList-&gt;GetId(pointId), pt);<br>
triangle_points-&gt;InsertNextPoint(pt[0], pt[1], pt[2]);</p>
<pre><code>}
}

// Insert all cells (triangles)
 for (int i = 0 ; i &lt; triangle_points-&gt;GetNumberOfPoints() ; i += 3) {

     const vtkIdType cellPoints[] = {i, i + 1, i + 2};
     triangles-&gt;InsertNextCell(3, cellPoints);
 }



Polydata-&gt;SetPoints(triangle_points);
Polydata-&gt;SetPolys(triangles);
</code></pre>
<p>thank’s!</p>

---
