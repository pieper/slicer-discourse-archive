# Compute bounding sphere

**Topic ID**: 4361
**Date**: 2018-10-11
**URL**: https://discourse.slicer.org/t/compute-bounding-sphere/4361

---

## Post #1 by @ThomPote (2018-10-11 14:03 UTC)

<p>Hi everybody,</p>
<p>Can you help me to extract bounding sphere of my segment ?<br>
I did it with bounding box but not with bounding sphere.<br>
I use CT scan and segmentation</p>
<p><em>I’m new on Slicer it’s still difficult for me to understand all “3D-knowledges”</em></p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2018-10-11 18:15 UTC)

<p>I don’t think bounding spheres is implemented in any of the libraries that are bundled with Slicer. We use directed bounding box instead, because it can be computed very quickly.</p>
<p>Why do you need a bounding sphere?</p>

---

## Post #3 by @ThomPote (2018-10-12 07:02 UTC)

<p>I just found this in vtkSphere Class Reference</p>
<p>function static void <a href="https://www.vtk.org/doc/nightly/html/classvtkSphere.html#ad86cfd7f3ebd6f1d62ff06ad83aacdf5" rel="nofollow noopener">ComputeBoundingSphere</a> (<a href="https://www.vtk.org/doc/nightly/html/vtkVectorOperators_8h.html#a6a1bb6ed41f44b60e7bd83b0e9945aa7" rel="nofollow noopener">float</a> *pts, <a href="https://www.vtk.org/doc/nightly/html/vtkType_8h.html#a20bd6b6dedfe1bbb096c50354d52cc7e" rel="nofollow noopener">vtkIdType</a> numPts, <a href="https://www.vtk.org/doc/nightly/html/vtkVectorOperators_8h.html#a6a1bb6ed41f44b60e7bd83b0e9945aa7" rel="nofollow noopener">float</a> sphere[4], <a href="https://www.vtk.org/doc/nightly/html/vtkType_8h.html#a20bd6b6dedfe1bbb096c50354d52cc7e" rel="nofollow noopener">vtkIdType</a> hints[2])</p>
<p>But I was in troubles with arguments to use it, and slicer-app crashes …</p>
<p><strong>Do you know what is exactly the type of data required with argument 1 “Points” ?</strong></p>
<p>I still have my segment :</p>
<p>n = getNode(‘Segmentation’)<br>
s = n.GetSegmentation()<br>
ssid = s.GetSegmentIdBySegmentName(‘mysegment’)<br>
ss = s.GetSegment(ssid)<br>
pd = ss.GetRepresentation(‘Closed surface’)</p>
<p>In fact I have a volume which looks like a half-sphere and I want to have the sphere center.<br>
I can’t use the center of gravity here because the center of sphere and half-sphere is not same.</p>
<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #4 by @lassoan (2018-10-13 17:57 UTC)

<p>Thanks for the additional information. It is now clear that you need high-accuracy sphere fitting - this rules out most of the fast implementations (that only provide approximate results).</p>
<p>There are still many options how to approach this. Optimal method depends on what are the next steps and how much and what kind of interactions and manual processing do you plan to do.</p>
<p>Would you like to implement automatic sizing and positioning of hip implants? Do you plan to segment the femoral head or you would place points on the bone surface on a number of slices?</p>

---

## Post #6 by @ThomPote (2018-10-15 13:11 UTC)

<p>Hi,</p>
<p>Thanks it’s ok for me for the function now.</p>
<p>I just try to analyze segments by myself for the moment.</p>

---

## Post #7 by @ThomPote (2018-10-17 08:25 UTC)

<p>I’m still in troubles with argument 4 “hints” now</p>
<p>I can’t use None for arg4 when I call the function, it’s said hints are required in error message</p>
<p>In code source I can see that an else condition can execute script without “hints”</p>
<pre><code>void vtkSphereComputeBoundingSphere(T *pts, vtkIdType numPts, T sphere[4],
                                    vtkIdType hints[2])
{
  [...]
  }

  vtkIdType i;
  T *p, d1[3], d2[3];
  if ( hints )
  {
   [...]
  }
  else //no hints provided, compute an initial guess
{ [...]
</code></pre>
<p>Normally without hints the function has to find the points that span the greatest distance on the x-y-z axes and define a sphere centered between the two points.</p>
<p>Can you help me ?</p>

---

## Post #8 by @lassoan (2018-10-17 12:48 UTC)

<p>You can fit spheres using various calibration and registration methods that are already available in Slicer but it is not possible to recommend a good choice without knowing what specific input and constraints you have. So, it would be useful if you could tell us the big picture - what you would like to achieve - and we can help you to get you there. Also, most likely several people have done very similar things that you would like to do, so they can share their experience - what worked for them and what not.</p>
<p>For example, you can fit a generic sphere model using SlicerIGT extension. Create a sphere model using CreeateModel module then register it to another model’s points using SlicerIGT extension’s Model registration module, using Similarity method. The resulting transform gives you the sphere’s origin and relative scale to the input sphere model. This may or may not be the ideal method, depending on your end goal.</p>

---
