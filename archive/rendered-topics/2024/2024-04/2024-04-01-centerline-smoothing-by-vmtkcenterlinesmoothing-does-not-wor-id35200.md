# Centerline smoothing by vmtkCenterlineSmoothing does not work

**Topic ID**: 35200
**Date**: 2024-04-01
**URL**: https://discourse.slicer.org/t/centerline-smoothing-by-vmtkcenterlinesmoothing-does-not-work/35200

---

## Post #1 by @tomo-akiyama (2024-04-01 15:10 UTC)

<p>Hello, everyone,</p>
<p>I’m interested in smoothing the centerlines of the cerebral arteries.</p>
<p>Following the parameters recommended by “Kjeldsberg et al. BioMedical Engineering OnLine (2021) Automated landmarking of bends in vascular structures: a comparative study with application to the internal carotid artery (<a href="https://doi.org/10.1186/s12938-021-00957-6" class="inline-onebox" rel="noopener nofollow ugc">Automated landmarking of bends in vascular structures: a comparative study with application to the internal carotid artery | BioMedical Engineering OnLine | Full Text</a>)”, I set the smoothing factor to 1.2 and the iteration number to 100. I’ve written a script using Python 3.8.10 (Anaconda) and VMTK 1.5.0.</p>
<p>Comparing with the original centerlines, there’s hardly any change in their trajectories. Even when I tried a significantly larger number for the smoothing factor, there was no variation, and the individual coordinates remained unchanged as well. Do you have any suggestions for improvement?</p>
<p>For the vascular data, I’m using the freely available AneuriskWeb’s C0002 (<a href="http://ecm2.mathcs.emory.edu/aneuriskweb/repository#" rel="noopener nofollow ugc">http://ecm2.mathcs.emory.edu/aneuriskweb/repository#</a>).</p>
<p>Thank you.</p>
<pre data-code-wrap="python"><code class="lang-python">from vmtk import vmtkscripts

def vmtk_centerline_smoothing(centerlines, num_iteration=100, smooth_factor=1.2):
    # smooth centerlines with a moving average filter
    # args: centerlines: centerlines (vtkPolydata)
    #       num_iteration: number of iterations (str)
    #       smooth_factor: smooth factor (float)
    # returns: smoothed centerline (vtkPolyData)
 
    smoother = vmtkscripts.vmtkCenterlineSmoothing()
    smoother.Centerlines = centerlines
    smoother.SetNumberOfSmoothingIterations = num_iteration
    smoother.SetSmoothingFactor = smooth_factor
    smoother.Execute()
    smoothed_centerlines = smoother.Centerlines
    return smoothed_centerlines

CL # original centerlines
smoothed_centerlines1 = vmtk_centerline_smoothing(CL, num_iteration=100, smooth_factor=0.1)
smoothed_centerlines2 = vmtk_centerline_smoothing(CL, num_iteration=100, smooth_factor=1000)

# check the coordinate
print(CL.GetPoints().GetPoint(10))
print(smoothed_centerlines1.GetPoints().GetPoint(10))
print(smoothed_centerlines2.GetPoints().GetPoint(10))
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90c101f93f7612fd5e2bb681fda71c8377f1f9a2.png" data-download-href="/uploads/short-url/kEygUR0pFjKbftVC3a2lg3EpFpo.png?dl=1" title="output" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90c101f93f7612fd5e2bb681fda71c8377f1f9a2_2_666x500.png" alt="output" data-base62-sha1="kEygUR0pFjKbftVC3a2lg3EpFpo" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90c101f93f7612fd5e2bb681fda71c8377f1f9a2_2_666x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90c101f93f7612fd5e2bb681fda71c8377f1f9a2_2_999x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90c101f93f7612fd5e2bb681fda71c8377f1f9a2.png 2x" data-dominant-color="EBEEEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">output</span><span class="informations">1024×768 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(62.38236999511719, 4.450344562530518, 63.071693420410156)<br>
(62.37776184082031, 4.44761848449707, 63.0672607421875)<br>
(62.37776184082031, 4.44761848449707, 63.0672607421875)</p>

---

## Post #2 by @lassoan (2024-04-01 15:49 UTC)

<p>Everything seems to work very well. Since the centerline is already very much smoothed and the curve points are very close to each other, you wont see much if you just use 100 iterations and not too strong smoothing factor.</p>
<p>You can copy-paste this code snippet into 3D Slicer’s Python console to see the effect of smoothing:</p>
<pre data-code-wrap="python"><code class="lang-python">centerlineFilePath = 'path/to/C0002/morphology/centerlines.vtp'

reader = vtk.vtkXMLPolyDataReader()
reader.SetFileName(centerlineFilePath)
reader.Update()

try:
    import vtkvmtkComputationalGeometryPython as vtkvmtkComputationalGeometry
except ImportError:
    raise ImportError("Please install VMTK extension")
smoothing = vtkvmtkComputationalGeometry.vtkvmtkCenterlineSmoothing()
smoothing.SetInputConnection(reader.GetOutputPort())
smoothing.SetSmoothingFactor(0.1)
smoothing.SetNumberOfSmoothingIterations(100)
smoothing.Update()

modelNode = slicer.modules.models.logic().AddModel(smoothing.GetOutputPort())
modelNode.GetDisplayNode().SetLineWidth(2)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cba1ead1080553a56cf8623f14fa654fb6514f5.png" data-download-href="/uploads/short-url/8FdpiOp0ZVUtNe0C8t7CEa3U2UJ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cba1ead1080553a56cf8623f14fa654fb6514f5.png" alt="image" data-base62-sha1="8FdpiOp0ZVUtNe0C8t7CEa3U2UJ" width="690" height="348" data-dominant-color="9C9ED2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1506×760 14.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After this you can adjust the smoothing parameters and see the result immediately:</p>
<pre><code class="lang-auto">smoothing.SetNumberOfSmoothingIterations(1000)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93c5f6f82ad6a8b1ad0ae8c604f3135fd90e94ed.png" data-download-href="/uploads/short-url/l5gkbGJRqtWMuDOs9YeMdlTaKa9.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/93c5f6f82ad6a8b1ad0ae8c604f3135fd90e94ed.png" alt="image" data-base62-sha1="l5gkbGJRqtWMuDOs9YeMdlTaKa9" width="690" height="348" data-dominant-color="9C9ED2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1506×760 14.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<pre><code class="lang-auto">smoothing.SetSmoothingFactor(0.5)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1eaa0977c7c4b263e4b51d487ec9ee204ac4f67.png" data-download-href="/uploads/short-url/n6nyGtVSOYHuDMFNodYV3ym7iB1.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/1/a1eaa0977c7c4b263e4b51d487ec9ee204ac4f67.png" alt="image" data-base62-sha1="n6nyGtVSOYHuDMFNodYV3ym7iB1" width="690" height="348" data-dominant-color="9C9ED2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1506×760 14.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @tomo-akiyama (2024-04-03 04:58 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thank you for your reply.</p>
<p>I didn’t have a good understanding of this smoothing. Looking at your display, it seems to be smoothed properly, but when I write a script with the same in Python, it’s clearly not working well. I wonder what the cause might be?</p>
<blockquote>
<p>centerlineFilePath = “path/to/C0002/morphology/centerlines.vtp”</p>
</blockquote>
<blockquote>
<p>def load_vtp(file_path):<br>
reader = vtk.vtkXMLPolyDataReader()<br>
reader.SetFileName(file_path)<br>
reader.Update()<br>
vtkpolydata = reader.GetOutput()<br>
return vtkpolydata</p>
</blockquote>
<blockquote>
<p>def vmtk_centerline_smoothing(centerlines, num_iteration, smooth_factor):<br>
smoother = vmtkscripts.vmtkCenterlineSmoothing()<br>
smoother.Centerlines = centerlines<br>
smoother.SetNumberOfSmoothingIterations = num_iteration<br>
smoother.SetSmoothingFactor = smooth_factor<br>
smoother.Execute()<br>
smoothed_centerlines = smoother.Centerlines<br>
return smoothed_centerlines</p>
</blockquote>
<blockquote>
<p>CL = load_vtp(centerlineFilePath)</p>
</blockquote>
<blockquote>
<p>smoothed_centerlines1 = vmtk_centerline_smoothing(centerlines=CL, num_iteration=<strong>100</strong>, smooth_factor=<strong>0.1</strong>)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0ffa7e0545d621e44cd2a4f3e011aec11f86d3e5.png" data-download-href="/uploads/short-url/2hlQ28w2835WlvrwewnxKSogCRT.png?dl=1" title="スクリーンショット 2024-04-03 13.50.02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0ffa7e0545d621e44cd2a4f3e011aec11f86d3e5_2_669x500.png" alt="スクリーンショット 2024-04-03 13.50.02" data-base62-sha1="2hlQ28w2835WlvrwewnxKSogCRT" width="669" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/f/0ffa7e0545d621e44cd2a4f3e011aec11f86d3e5_2_669x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0ffa7e0545d621e44cd2a4f3e011aec11f86d3e5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/f/0ffa7e0545d621e44cd2a4f3e011aec11f86d3e5.png 2x" data-dominant-color="CFD6D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2024-04-03 13.50.02</span><span class="informations">884×660 253 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>
<blockquote>
<p>smoothed_centerlines2 = vmtk_centerline_smoothing(centerlines=CL, num_iteration=<strong>1000</strong>, smooth_factor=<strong>0.1)</strong><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78e031f0439a3a911571eba51f0a0553c81300ab.png" data-download-href="/uploads/short-url/hfjDc6tKgPwJp7AE4qMVCxYSL8f.png?dl=1" title="スクリーンショット 2024-04-03 13.54.22" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78e031f0439a3a911571eba51f0a0553c81300ab_2_625x500.png" alt="スクリーンショット 2024-04-03 13.54.22" data-base62-sha1="hfjDc6tKgPwJp7AE4qMVCxYSL8f" width="625" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/8/78e031f0439a3a911571eba51f0a0553c81300ab_2_625x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78e031f0439a3a911571eba51f0a0553c81300ab.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/78e031f0439a3a911571eba51f0a0553c81300ab.png 2x" data-dominant-color="CCD4D5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2024-04-03 13.54.22</span><span class="informations">810×648 250 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>
<blockquote>
<p>smoothed_centerlines3 = vmtk_centerline_smoothing(centerlines=CL, num_iteration=<strong>1000</strong>, smooth_factor=<strong>0.5</strong>)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/853309d0182f944631b86ba040e16f8471060801.png" data-download-href="/uploads/short-url/j0kQRK4aK3nwtg1uIpJvEaiaiYx.png?dl=1" title="スクリーンショット 2024-04-03 13.55.05" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/853309d0182f944631b86ba040e16f8471060801_2_665x500.png" alt="スクリーンショット 2024-04-03 13.55.05" data-base62-sha1="j0kQRK4aK3nwtg1uIpJvEaiaiYx" width="665" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/853309d0182f944631b86ba040e16f8471060801_2_665x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/853309d0182f944631b86ba040e16f8471060801.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/853309d0182f944631b86ba040e16f8471060801.png 2x" data-dominant-color="C5CDCE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2024-04-03 13.55.05</span><span class="informations">897×674 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</blockquote>
<p>Compared to the original centerlines, all of them are smoothed, but all smoothed centerlines seem to be the same even if the parameters are adjusted…</p>
<p>Incidentally, smoothing once does not change the smoothing situation even if the parameters are adjusted, but further smoothing of centerlines that have been smoothed (smoothing 2 times) seems to result in the intended smoothed centerlines.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/486bcaba2faf622500aafc54540f4b11a42e0eda.png" data-download-href="/uploads/short-url/akFjTLRcEooyUgNiBX20MYCXIh4.png?dl=1" title="f6d3ab3b-c7e9-42ec-b80a-36ef34e57c73" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/486bcaba2faf622500aafc54540f4b11a42e0eda_2_666x500.png" alt="f6d3ab3b-c7e9-42ec-b80a-36ef34e57c73" data-base62-sha1="akFjTLRcEooyUgNiBX20MYCXIh4" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/486bcaba2faf622500aafc54540f4b11a42e0eda_2_666x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/486bcaba2faf622500aafc54540f4b11a42e0eda_2_999x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/486bcaba2faf622500aafc54540f4b11a42e0eda.png 2x" data-dominant-color="F6F4F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">f6d3ab3b-c7e9-42ec-b80a-36ef34e57c73</span><span class="informations">1024×768 167 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>One more question, is this smoothing with Moving Average? Is it smoothing using a Laplacian filter? I don’t understand the definition of lambda.</p>
<p>I’m not sure from the VMTK document.</p>
<p>Thank you.</p>

---

## Post #5 by @lassoan (2024-04-04 01:27 UTC)

<aside class="quote no-group" data-username="tomo-akiyama" data-post="4" data-topic="35200">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tomo-akiyama/48/69831_2.png" class="avatar"> tomo-akiyama:</div>
<blockquote>
<p>I didn’t have a good understanding of this smoothing. Looking at your display, it seems to be smoothed properly, but when I write a script with the same in Python, it’s clearly not working well.</p>
</blockquote>
</aside>
<p>I would recommend to start in the Slicer Python console and confirm that everything works well. You can then change things step by step and see what change breaks it.</p>
<aside class="quote no-group quote-modified" data-username="tomo-akiyama" data-post="3" data-topic="35200">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tomo-akiyama/48/69831_2.png" class="avatar"> tomo-akiyama:</div>
<blockquote>
<p>One more question, is this smoothing with Moving Average? Is it smoothing using a Laplacian kernel?</p>
</blockquote>
</aside>
<p>The <a href="https://github.com/vmtk/vmtk/blob/master/vtkVmtk/ComputationalGeometry/vtkvmtkCenterlineSmoothing.h#L21">documentation</a> mentions <a href="https://graphics.stanford.edu/courses/cs468-12-spring/LectureSlides/06_smoothing.pdf">Laplacian smoothing</a> and <a href="https://github.com/vmtk/vmtk/blob/6211af00372d099454acaf5d90520ddfcdf6cf96/vtkVmtk/ComputationalGeometry/vtkvmtkCenterlineSmoothing.cxx#L101-L107">implementation</a> seems to be that, too.</p>

---

## Post #6 by @tomo-akiyama (2024-04-04 13:44 UTC)

<p>It worked perfectly with the method you described. I have since realized the mistake in my script. When using the VMTK’s vmtkCenterlineSmoothing class in Python, the ‘Set’ prefix is not required, and direct assignment to properties is necessary.</p>
<p>The correct script is:<br>
def vmtk_centerline_smoothing(centerlines, num_iteration, smooth_factor)：<br>
smoother = vmtkscripts.vmtkCenterlineSmoothing()<br>
smoother.Centerlines = centerlines<br>
smoother.NumberOfSmoothingIterations = num_iteration<br>
smoother.SmoothingFactor = smooth_factor<br>
smoother.Execute()<br>
smoothed_centerlines = smoother.centerlines<br>
return smoothed_centerlines</p>
<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> and everyone !</p>

---
