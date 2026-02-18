# Distance between two segments

**Topic ID**: 4910
**Date**: 2018-11-29
**URL**: https://discourse.slicer.org/t/distance-between-two-segments/4910

---

## Post #1 by @torquil (2018-11-29 14:25 UTC)

<p>Hi!</p>
<p>How do I get Slicer to calculate the distance between two segments in 3d space? By fiddling with the ruler endpoints I cannot be sure that I’m acually measuring the minimum distance between the segments, and it is also quite inconvenient. Does Slicer have some way to automatically determining the minimum distance between two segments?</p>
<p>Best regards,<br>
Torquil Sørensen</p>

---

## Post #2 by @cpinter (2018-11-29 14:54 UTC)

<p>I believe the minimum Hausdorff distance is exactly the distance you’re trying to get. Use Segment Comparison module in the SlicerRT extension to calculate that.</p>

---

## Post #3 by @torquil (2018-11-29 18:54 UTC)

<p>Thanks, but I don’t think that is what I’m after. I just tried it and it returns something called “Maximum” “Average” and “95%” distances. All the values are far larger than the value I expect to get in the case I’m working on right now.</p>
<p>According to Wikipedia, Hausdorff distance is “the greatest of all the distances from a point in one set to the closest point in the other set”, which is not what I’m after.</p>
<p>What I want is the smallest possible distance that can be obtained by choosing one point in each segment. I.e. what I think is the most common definition of the distance between two subsets in a metric space.</p>

---

## Post #4 by @lassoan (2018-11-29 20:26 UTC)

<p>We compute statistics for the distances between all points of both surfaces. We typically report mean, 95th percentile, and maximum, because the segments usually overlap and so minimum distance is always 0.</p>
<p>Are your segments intersecting or they are at a distance from each other?</p>

---

## Post #5 by @cpinter (2018-11-29 20:53 UTC)

<aside class="quote no-group" data-username="torquil" data-post="3" data-topic="4910">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e79b87/48.png" class="avatar"> torquil:</div>
<blockquote>
<p>What I want is the smallest possible distance</p>
</blockquote>
</aside>
<p>Yes this is why I wrote that you’ll need the minimum Hausdorff, which will be the distance between the two closest points. As <a class="mention" href="/u/lassoan">@lassoan</a> says it’s usually 0 because usually we compare two segments representing the same objects (so they overlap). So this is why it’s not shown in Segment Statistics UI (I thought for some reason that it was). I’m not aware of any method for getting this number on the UI, but this is some python code that will get it for you:</p>
<pre><code>import vtkSlicerSegmentComparisonModuleLogicPython
s=getNode('vtkMRMLSegmentationNode1') # Whatever your input is
p1=s.GetClosedSurfaceRepresentation('Segment_1') # Again, depends on your input. If it's not a segmentation then you'll need to access the model nodes
p2=s.GetClosedSurfaceRepresentation('Segment_2')
pdf=vtkSlicerSegmentComparisonModuleLogicPython.vtkPolyDataDistanceHistogramFilter()
pdf.SetInputReferencePolyData(p1)
pdf.SetInputComparePolyData(p2)
pdf.Update()
pdf.GetNthPercentileHausdorffDistance(0)
</code></pre>

---

## Post #6 by @torquil (2018-11-29 21:39 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> My segments are nonintersecting, and I think that will be the case every time I need to do distance measurements in Slicer.</p>
<p><a class="mention" href="/u/cpinter">@cpinter</a> Thanks! At first I didn’t catch your point about the minimum distance since it wasn’t in the graphical interface. Your code works perfectly, so I can use that.</p>
<p>It would be very nice to get this distance measure into the Segment Comparison graphical interface.</p>

---

## Post #7 by @cpinter (2018-11-29 21:52 UTC)

<p>I’m glad you managed to make use of the code! I know it’s not the most convenient way, but if you don’t need it in a workflow that you repeat many times, then it should do the trick for you. Let us know otherwise.</p>

---

## Post #8 by @torquil (2018-11-30 09:37 UTC)

<p>Yes, thanks. I will be measuring quite a lot of such distances. I’m working on a study where we are measuring the minimal distance between a drilled volume in bone and the surrounding anatomical structures. Would it be a lot of work for you to include this distance among the other ones in the Segment Comparison module? It would be very convenient to be able to just select the segment name in the GUI and have it do the calculation.</p>
<p>I would love to propose a patch for this myself, but the only part of Slicer I have tried to work on is the Screen Capture module which seems easier because everything seems to be written in Python there, and this doesn’t seem to be the case with this module. I guess it is in the source for the libvtkSlicerSegmentComparisonModule*.so-files in this case?</p>

---

## Post #9 by @cpinter (2018-11-30 14:49 UTC)

<p>Yes it’s that module, see source <a href="https://github.com/SlicerRt/SlicerRT/tree/master/SegmentComparison" rel="nofollow noopener">here</a>. I’m wondering if we should include it there or not. Currently we use Plastimatch’ Hausdorff implementation and not the filter that I used in the python snippet above. If we just add a new option to specify percentile for Hausdorff (that’s what I’d do), then we need to calculate it twice, once in Plastimatch and once in the VTK filter. If this overhead is fine then the change will be quite easy to make. We could also replace the Plastimatch one with the VTK one completely, but then it has to be validated again.</p>

---

## Post #10 by @gcsharp (2018-12-03 14:39 UTC)

<p>I never considered this before, but it seems useful.  It would be easy to modify to compute this without running the filter twice.</p>
<p>What would be the preferred implementation?  Min distance from boundary to boundary or set to set?  (Or both?)</p>

---

## Post #11 by @cpinter (2018-12-03 16:24 UTC)

<p>Thanks, Greg!<br>
Can you see a scenario where the min distance between set to set won’t be the same as the boundary to boundary? The boundary is always the outside shell of the set right?</p>

---

## Post #12 by @cpinter (2018-12-03 17:29 UTC)

<p>Actually I found a ticket about adding surface-based Hausdorff comparison: <a href="https://github.com/SlicerRt/SlicerRT/issues/67" rel="nofollow noopener">https://github.com/SlicerRt/SlicerRT/issues/67</a><br>
Since the two Hausdorff algorithms are quite different in what data type they work on (Plastimatch: labelmap, custom VTK filter: poly data), it could make sense to add it as a third option somehow in the module. It would be then very easy to add a custom percentile option.</p>

---

## Post #13 by @gcsharp (2018-12-03 19:46 UTC)

<p>Yes, vertex-based HD would be a nice addition.</p>
<p>Custom percent could be added to labelmap too.  There is already a function for this:</p>
<pre><code>/*! \brief Set the fraction of voxels to include when computing 
  the percent hausdorff distance.  The input value should be 
  a number between 0 and 1.  The default value is 0.95. */
void set_hausdorff_distance_fraction (
    float hausdorff_distance_fraction);
</code></pre>
<p>I did add some code for minimum as well.  (But not yet tested.)</p>
<pre><code>/*! \brief Return the minimum Hausdorff distance */
float get_min_min_hausdorff ();
/*! \brief Return the minimum boundary Hausdorff distance */
float get_min_min_boundary_hausdorff ();
</code></pre>
<p>The boundary value differs from the set value when one segment is completely contained within the other, where the set distance is zero but the boundary distance is non-zero.</p>

---

## Post #14 by @cpinter (2018-12-05 15:14 UTC)

<p>In this case the best would probably be to add the custom percentage option, and decide to use between the two logic classes run-time based on the master representation.</p>

---

## Post #15 by @ahopf (2020-11-11 01:35 UTC)

<p>Hi, I’m new to coding and wondering if someone can help me with the above-mentioned Python code to calculate minimum Hausdorff distance between two segmentations. I have installed the SlicerRT extension and have access to the “Segment Comparison” module.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aeb1661ebacd15028e6da0dfc7e03e79663ae6df.png" alt="image" data-base62-sha1="oVp9CPkuohOJO4qxUiuMgdczZEP" width="505" height="105"></p>
<p>If I am working with the above pictured scene, should the code be input as:</p>
<pre><code class="lang-auto">import vtkSlicerSegmentComparisonModuleLogicPython
s=getNode('Left Excised Volume') 
p1=s.GetClosedSurfaceRepresentation('Left Excised Volume') 
p2=s.GetClosedSurfaceRepresentation('Left Structures')
pdf=vtkSlicerSegmentComparisonModuleLogicPython.vtkPolyDataDistanceHistogramFilter()
pdf.SetInputReferencePolyData(p1)
pdf.SetInputComparePolyData(p2)
pdf.Update()
pdf.GetNthPercentileHausdorffDistance(0)
</code></pre>
<p>Using this, Slicer crashes after “pdf.SetInputReferencePolyData(p1).”</p>

---
