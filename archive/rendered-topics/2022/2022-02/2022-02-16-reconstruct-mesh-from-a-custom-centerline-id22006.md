# Reconstruct Mesh from a custom centerline

**Topic ID**: 22006
**Date**: 2022-02-16
**URL**: https://discourse.slicer.org/t/reconstruct-mesh-from-a-custom-centerline/22006

---

## Post #1 by @_11 (2022-02-16 20:52 UTC)

<p>Hi,</p>
<p>Thanks for the very valuable repository. I am wondering if it is possible to generate the tubular mesh based on a synthetically generated centerline with bifurcation?</p>
<p>So what I have is a graph/tree structure with nodes indicating each point along the centerlines with radius at each point, as well as edges indicating the connectivity of each point, but what I do not have is the Voronoi diagram.</p>
<p>Is it possible to reconstruct the surface/volume mesh from such centerlines using this tool?</p>
<p>Thanks a lot in advance!</p>

---

## Post #2 by @ramtingh (2022-02-16 22:36 UTC)

<p>You’d want <a href="http://www.vmtk.org/vmtkscripts/vmtkcenterlinemodeller.html" rel="noopener nofollow ugc">vmtkcenterlinemodeller</a> + a mesh extraction algorithm, e.g. vmtkmarchingcubes</p>

---

## Post #3 by @_11 (2022-02-17 09:47 UTC)

<p>Hi Ramtin,</p>
<p>Thank you so much for your reply. I am wondering if there is any example of using vmtkcenterlinemodeller, because I really cannot find one? Especially, what I have is a graph structure (V, E), where V could be a numpy array of |V| * 4 indicating xyz coordinates + radius at current location, and E could be a adjacant matrix in |V| * |V| where each value is 1 if the nodes are connected and 0 otherwise. How should I convert such a data structure to the Centerlines vtkPolyData and the radiusarray, which are the required input to vmtkcenterlinemodeller?</p>

---

## Post #4 by @ramtingh (2022-02-18 08:10 UTC)

<p>Assuming the graph is acyclic you shouldn’t have issues creating a centerline. The numpy interface (vmtknumpytocenterline) is probably easier to work with compared to directly using vtk objects. You’ll have to add the radius as a PointData array.</p>

---

## Post #5 by @_11 (2022-05-17 15:25 UTC)

<p>Hi Ramtin,</p>
<p>Thanks a lot for your reply and hope you are doing well! I know it’s been a while but I actually made it work by following the steps you provided! And the mesh it generated looks very good. But I am just confused about how to interpret the output from  <a href="http://www.vmtk.org/vmtkscripts/vmtkcenterlinemodeller.html" rel="noopener nofollow ugc">vmtkcenterlinemodeller </a> before running the marching cube, and what should be an appropriate <strong>level</strong> value for <a href="http://www.vmtk.org/vmtkscripts/vmtkmarchingcubes.html" rel="noopener nofollow ugc">vmtkmarchingcubes</a> in this case.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a9f2914f8358ce903700e7991c412b91d6ef4d1.png" data-download-href="/uploads/short-url/aE8kCmyYpkYOv7C74YTf8cstYxb.png?dl=1" title="Screenshot 2022-05-17 at 17.19.10" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a9f2914f8358ce903700e7991c412b91d6ef4d1_2_370x500.png" alt="Screenshot 2022-05-17 at 17.19.10" data-base62-sha1="aE8kCmyYpkYOv7C74YTf8cstYxb" width="370" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a9f2914f8358ce903700e7991c412b91d6ef4d1_2_370x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a9f2914f8358ce903700e7991c412b91d6ef4d1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a9f2914f8358ce903700e7991c412b91d6ef4d1.png 2x" data-dominant-color="393E75"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-05-17 at 17.19.10</span><span class="informations">490×662 242 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Intuitively I would think that  <a href="http://www.vmtk.org/vmtkscripts/vmtkcenterlinemodeller.html" rel="noopener nofollow ugc">vmtkcenterlinemodeller </a>  generates high intensity values inside the tubes around the centerline and low values outside. But I checked it does have high intensity values around the tube, but it has higher values near the corners.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a4f182d2bafbeb6c2838236af2256f997d862a8.png" data-download-href="/uploads/short-url/m14ZlErhrrnXQ73Op8j9Qrt29f2.png?dl=1" title="Screenshot 2022-05-17 at 17.19.00" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/a/9a4f182d2bafbeb6c2838236af2256f997d862a8.png" alt="Screenshot 2022-05-17 at 17.19.00" data-base62-sha1="m14ZlErhrrnXQ73Op8j9Qrt29f2" width="322" height="500" data-dominant-color="242422"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-05-17 at 17.19.00</span><span class="informations">376×583 23.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>More confusingly is that, when I apply <a href="http://www.vmtk.org/vmtkscripts/vmtkmarchingcubes.html" rel="noopener nofollow ugc">vmtkmarchingcubes</a> afterwards, if I use a high value for <strong>level</strong>, I am getting thicker tubes and thus merged sometime. If I use a low <strong>level</strong> value, it will be thinner and sometimes disconnected. This is a bit contrary to what I would think, because usually I would think <strong>I(x)&gt;level</strong> means inside, so that a small <strong>level</strong> means larger parts inside and thus thicker tube.</p>
<p>Can you maybe recommend a paper about the theories behind  <a href="http://www.vmtk.org/vmtkscripts/vmtkcenterlinemodeller.html" rel="noopener nofollow ugc">vmtkcenterlinemodeller </a> so that I can better understand it?</p>
<p>Thanks a lot in advance!</p>

---

## Post #6 by @ramtingh (2022-05-17 23:33 UTC)

<p>By default it is negative inside, 0 at the boundary of the vessel and positive outside. So corners will probably end up with the largest value since they’re farthest away.</p>
<p>Appropriate level for marching cubes should be just 0, if they are disconnected you might need to increase the sampling resolution used in vmtkcenterline modeller, the default of <code>-dimensions 64 64 64</code> might not be sufficient depending on how thin your vessels are</p>
<p>I don’t think there’s a paper discussing this, the tube function used is briefly discussed in " An image-based modeling framework for patient-specific computational hemodynamics". it looks like a distance transform so you can try looking that up.</p>

---

## Post #7 by @_11 (2022-05-19 08:04 UTC)

<p>Thanks a lot! This has been really helpful!</p>

---
