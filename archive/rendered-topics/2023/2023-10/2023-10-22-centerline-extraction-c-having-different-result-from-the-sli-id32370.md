---
topic_id: 32370
title: "Centerline Extraction C Having Different Result From The Sli"
date: 2023-10-22
url: https://discourse.slicer.org/t/32370
---

# Centerline extraction C++ having different result from the slicer

**Topic ID**: 32370
**Date**: 2023-10-22
**URL**: https://discourse.slicer.org/t/centerline-extraction-c-having-different-result-from-the-slicer/32370

---

## Post #1 by @liy0na (2023-10-22 07:43 UTC)

<p>Hello,</p>
<p>I have an <a href="https://www.dropbox.com/scl/fi/8gt64nbh0za9yy6gctdiy/surface_mesh.stl?rlkey=c51rxxzg81vctjuod4saaatit&amp;dl=0" rel="noopener nofollow ugc">STL file</a> containing a surface mesh.</p>
<p>When I use the slicer I can easily extract the centerlines from it.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84026e7831f4d1feb6f6339b3ab3a39d899d0620.png" data-download-href="/uploads/short-url/iPOeBGutriMsjxaJxGd57QW8l6U.png?dl=1" title="slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84026e7831f4d1feb6f6339b3ab3a39d899d0620_2_310x500.png" alt="slicer" data-base62-sha1="iPOeBGutriMsjxaJxGd57QW8l6U" width="310" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84026e7831f4d1feb6f6339b3ab3a39d899d0620_2_310x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/4/84026e7831f4d1feb6f6339b3ab3a39d899d0620_2_465x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/4/84026e7831f4d1feb6f6339b3ab3a39d899d0620.png 2x" data-dominant-color="9A99C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer</span><span class="informations">561×902 96.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>However when I use the following C++ code. I am only getting 3 output points.<br>
vtkSmartPointer reader = vtkSmartPointer::New();<br>
reader-&gt;SetFileName( “D:\Projects\cooling to test\conformal\surface_mesh.stl” );<br>
reader-&gt;Update();</p>
<p>vtkSmartPointer inletSeedIds = vtkSmartPointer::New();<br>
vtkSmartPointer outletSeedIds = vtkSmartPointer::New();</p>
<p>//Locate points<br>
vtkSmartPointer pointLocator = vtkSmartPointer::New();<br>
pointLocator-&gt;SetDataSet( reader-&gt;GetOutput() );<br>
pointLocator-&gt;BuildLocator();</p>
<p>double sourcePoint[3];<br>
sourcePoint[0] = -6.092;<br>
sourcePoint[1] = -6.036;<br>
sourcePoint[2] = 128.186;</p>
<p>double targetPoint[3];</p>
<p>targetPoint[0] = -15.177;<br>
targetPoint[1] = -6.048;<br>
targetPoint[2] = 128.183;</p>
<p>int sourceid = pointLocator-&gt;FindClosestPoint( sourcePoint );<br>
int targetid = pointLocator-&gt;FindClosestPoint( targetPoint );</p>
<p>inletSeedIds-&gt;InsertNextId( sourceid );<br>
outletSeedIds-&gt;InsertNextId( targetid );</p>
<p>//// Compute Centerlines<br>
vtkSmartPointer centerlineFilter = vtkSmartPointer::New();<br>
centerlineFilter-&gt;SetInputData( reader-&gt;GetOutput() );</p>
<p>centerlineFilter-&gt;SetSourceSeedIds( inletSeedIds );<br>
centerlineFilter-&gt;SetTargetSeedIds( outletSeedIds );<br>
centerlineFilter-&gt;SetRadiusArrayName( “MaximumInscribedSphereRadius” );<br>
centerlineFilter-&gt;SetCostFunction( “1/R” );<br>
centerlineFilter-&gt;SetFlipNormals( false );<br>
centerlineFilter-&gt;SetAppendEndPointsToCenterlines( 0 );<br>
centerlineFilter-&gt;SetSimplifyVoronoi( 0 );<br>
centerlineFilter-&gt;SetCenterlineResampling( 0 );<br>
centerlineFilter-&gt;SetResamplingStepLength( 1.0 );<br>
centerlineFilter-&gt;Update();</p>
<p>// access centerline points<br>
vtkSmartPointer centerlinesPolyData = vtkSmartPointer::New();<br>
centerlinesPolyData = centerlineFilter-&gt;GetOutput();</p>
<p>vtkSmartPointer points = centerlinesPolyData-&gt;GetPoints();<br>
sim::Dbl3Array centerline_points_array;</p>
<p>int numberOfCells = centerlinesPolyData-&gt;GetNumberOfCells();<br>
int numberOfPoints = centerlinesPolyData-&gt;GetNumberOfPoints();<br>
int numberOfLines = centerlinesPolyData-&gt;GetNumberOfLines();<br>
//int numberOfVerts = centerlinesPolyData-&gt;GetNumberOfVerts();<br>
//int numberOfStrips = centerlinesPolyData-&gt;GetNumberOfStrips();<br>
int numberOfPieces = centerlinesPolyData-&gt;GetNumberOfPieces();<br>
int numberOfPolys = centerlinesPolyData-&gt;GetNumberOfPolys();</p>
<p>I would appreciate it if you could let me know what I am doing wrong.</p>

---

## Post #2 by @Lulu (2024-08-09 04:10 UTC)

<p>Hi，<br>
I have the same problem as you.Apply the same code but generate a different centerline than the one generated in slicer.<br>
Have you solved the problem？I would appreciate it if you have any suggestions</p>

---

## Post #3 by @lassoan (2024-08-12 12:47 UTC)

<p>Slicer’s <code>Extract Centerline</code> module uses the VMTK C++ code via a thin Python wrapping layer so there is no difference due to using C++ or Python.</p>
<p>You get different results when you use the code above because you missed the required preprocessing steps - see the <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py">centerline extraction module source code</a>.</p>

---
