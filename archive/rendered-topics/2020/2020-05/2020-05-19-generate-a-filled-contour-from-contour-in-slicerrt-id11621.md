# Generate a filled contour from contour in SlicerRT

**Topic ID**: 11621
**Date**: 2020-05-19
**URL**: https://discourse.slicer.org/t/generate-a-filled-contour-from-contour-in-slicerrt/11621

---

## Post #1 by @loubna (2020-05-19 13:47 UTC)

<p>Hi;</p>
<p>I want construct a filled contour (vtkimagedata) from contour points in Slicer RT.</p>
<p>This is the code i have implemented :</p>
<p>vtkPoints* pointsSlice                    // the set of 3D points of the contour<br>
int nbpoints = pointsSlice-&gt;GetNumberOfPoints()-1;    // number of points</p>
<p>int dimSlice[3]; dimSlice[0]= dim[0]; dimSlice[1] =dim[1]; dimSlice[2]=1;  // set up vtkImagedata parameters</p>
<p>vtkSmartPointer imgSlice = vtkSmartPointer::New();<br>
int extent[6] = {0, dimSlice[0]-1, 0, dimSlice[1]-1, 0, 0};<br>
imgSlice-&gt;SetExtent(extent);<br>
imgSlice-&gt;SetOrigin(origin);<br>
imgSlice-&gt;SetDimensions(dimSlice);<br>
imgSlice-&gt;SetSpacing(1,1,1);<br>
imgSlice-&gt;AllocateScalars(VTK_UNSIGNED_CHAR,1);</p>
<p>for(int i=0; i&lt; nbpoints; i++)                                   // store 3D points in double array<br>
{<br>
double *p = pointsSlice-&gt;GetPoint(i);<br>
pts[i*3+0] = p[0];<br>
pts[i*3+1] = p[1];<br>
pts[i*3+2] = p[2];</p>
<p>}</p>
<p>double *boundSlice = pointsSlice-&gt;GetBounds();     // bounds of 3d Points<br>
double z_coord = vtkMath::Round(pts[2]);            //all 3d points of same contour have same z-coord</p>
<p>vtkPolygon::ComputeNormal(pointsSlice, normal);     //compute normal of the contour</p>
<p>for(int j=0; j&lt;dim[1];j++)<br>
for(int i=0; i&lt;dim[0]; i++)<br>
{<br>
double x[3] = {i+origin[0], j+origin[1], z_coord};<br>
in_poly = vtkPolygon::PointInPolygon(x, nbpoints,pts,boundSlice,normal);<br>
if(in_poly)                                              // point belong to the contour<br>
pixel =255;<br>
else<br>
pixel= 0<br>
}</p>
<p>However this method display filled square instead of filled circle (contour) as shown in figure.<br>
I think because I have used vtkPolygon:: PointInPolygon test?</p>
<p>How can I get a filled contour instead of filled square.</p>
<p>thank’s in advance for your help</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/665d3023bd322f0b756b8c05338b50c41e9f1338.png" alt="square" data-base62-sha1="eBym6cwx1cYRh5ple9srUGkj8hi" width="249" height="237"></p>

---

## Post #2 by @cpinter (2020-05-19 15:00 UTC)

<p>What you are trying to do is much harder than it looks, and we have been working for years to do it reliably. If you don’t believe it check out these publications:<br>
<a href="http://perk.cs.queensu.ca/contents/reconstruction-surfaces-planar-contours-through-contour-interpolation" class="onebox" target="_blank">http://perk.cs.queensu.ca/contents/reconstruction-surfaces-planar-contours-through-contour-interpolation</a><br>
<a href="https://qspace.library.queensu.ca/handle/1974/26422" class="onebox" target="_blank">https://qspace.library.queensu.ca/handle/1974/26422</a></p>
<p>So instead of reinventing everything I’d recommend using the infrastructure in place. Install the SlicerRT extension, import the structure set to the DICOM database, load it, convert the resulting segmentation node’s representation to binary labelmap, and extract the slice you want. There are tons of materials about the steps of this workflow in the documentation and the forum, so please start to look there if you have questions. Otherwise we’re happy to help.</p>

---

## Post #3 by @loubna (2020-05-19 16:04 UTC)

<p>Thank’s for response. However my goal is not to use things that already exist. I have imlemented an implcit method “Contour-BasedSurfaceReconstructionusing MPU ImplicitModels”  to convert planar contours to closed surface (it is not important if it is better or worse than the slicerRT method).</p>
<p>the only issue is to fill pixels that belong to the contour in order to construct binary volume by staking the 2D slices (filled contours). so I have used vtkPolygon::PointInPolygon(x, nbpoints,pts,boundSlice,normal).</p>
<p>Are there other solutions to keep the contour form?</p>

---

## Post #4 by @pieper (2020-05-19 20:23 UTC)

<aside class="quote no-group" data-username="loubna" data-post="3" data-topic="11621">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/l/cab0a1/48.png" class="avatar"> loubna:</div>
<blockquote>
<p>However my goal is not to use things that already exist.</p>
</blockquote>
</aside>
<p>Just out of curiosity, what do you mean here?  Are you trying to learn it from scratch for educational purposes?</p>

---
