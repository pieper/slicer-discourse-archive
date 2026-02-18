# VMTK centerline merge does not work

**Topic ID**: 36634
**Date**: 2024-06-07
**URL**: https://discourse.slicer.org/t/vmtk-centerline-merge-does-not-work/36634

---

## Post #1 by @tomo-akiyama (2024-06-07 04:20 UTC)

<p>Hello, everyone</p>
<p>I am encountering an issue while merging centerlines using VMTK, and I would appreciate some assistance.</p>
<p>I used the “Extract Centerlines” module in 3D Slicer to extract centerlines from a cerebral vascular mesh and saved it as a VTP file. Next, I loaded the centerlines VTP file in VS Code with Python 3.10 and performed branch splitting using vmtk_branch_splitting. Then, I smoothed the centerlines using vmtk_centerline_smoothing.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b641ba111de8058068aec1b4be33950e8206ee7d.png" data-download-href="/uploads/short-url/q0jIyEqHDOQ5zlgiWLXR43j771b.png?dl=1" title="9994b8dc-cf25-46ee-a55a-2b3cce0b880b" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b641ba111de8058068aec1b4be33950e8206ee7d_2_690x230.png" alt="9994b8dc-cf25-46ee-a55a-2b3cce0b880b" data-base62-sha1="q0jIyEqHDOQ5zlgiWLXR43j771b" width="690" height="230" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b641ba111de8058068aec1b4be33950e8206ee7d_2_690x230.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b641ba111de8058068aec1b4be33950e8206ee7d_2_1035x345.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/6/b641ba111de8058068aec1b4be33950e8206ee7d_2_1380x460.png 2x" data-dominant-color="A5B4B6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">9994b8dc-cf25-46ee-a55a-2b3cce0b880b</span><span class="informations">1500×500 378 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Finally, I merged the centerlines from the same vessel using vmtk_centerlinemerge. After merging the centerlines (magenta centerlines) and displaying them using PyVista alongside the pre-merged (smoothed, green centerlines), it is clear that the merged centerlines (magenta) deviate significantly from the original path of the centerlines (green).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7836eba5e84ad7db3f2462352ffa79fabd7449f.jpeg" data-download-href="/uploads/short-url/zjBwK17VLdrhQlWuvDp1sCB34iX.jpeg?dl=1" title="32119983-cc2c-423b-a412-22bcdc73e457" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7836eba5e84ad7db3f2462352ffa79fabd7449f_2_690x287.jpeg" alt="32119983-cc2c-423b-a412-22bcdc73e457" data-base62-sha1="zjBwK17VLdrhQlWuvDp1sCB34iX" width="690" height="287" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7836eba5e84ad7db3f2462352ffa79fabd7449f_2_690x287.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f7836eba5e84ad7db3f2462352ffa79fabd7449f_2_1035x430.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7836eba5e84ad7db3f2462352ffa79fabd7449f.jpeg 2x" data-dominant-color="A9B4B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">32119983-cc2c-423b-a412-22bcdc73e457</span><span class="informations">1200×500 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The step length during merging was adjusted, but the result did not change. Could you help me identify the cause and suggest improvements?</p>
<p>Here is the code I used:</p>
<pre><code class="lang-auto">from vmtk import vmtkscripts
import vtk
def load_vtp(file_name):
    reader = vtk.vtkXMLPolyDataReader()
    reader.SetFileName(file_name)
    reader.Update()
    polydata = reader.GetOutput()
    return polydata

def vmtk_branch_splitting(centerlines):
    branch_splitting = vmtkscripts.vmtkBranchExtractor()
    branch_splitting.Centerlines = centerlines
    branch_splitting.Execute()
    splitted_centerlines = branch_splitting.Centerlines 
    return splitted_centerlines

def vmtk_centerline_smoothing(centerlines, num_iteration=100, smooth_factor=1.2):
    smoother = vmtkscripts.vmtkCenterlineSmoothing()
    smoother.Centerlines = centerlines
    smoother.NumberOfSmoothingIterations = num_iteration 
    smoother.SmoothingFactor = smooth_factor 
    smoother.Execute()
    smoothed_centerlines = smoother.Centerlines
    return smoothed_centerlines

def vmtk_centerlinemerge(centerlines, step_length=0.1):  
    centerlinemerge = vmtkscripts.vmtkCenterlineMerge()
    centerlinemerge.Centerlines = centerlines
    centerlinemerge.Length = step_length     
    centerlinemerge.Execute()
    merged_centerlines = centerlinemerge.Centerlines
    return merged_centerlines 


centerlines = load_vtp("Centerline model.vtp")
radius_array = centerlines.GetPointData().GetArray("Radius")
radius_array.SetName("MaximumInscribedSphereRadius")

splitted_centerlines = vmtk_branch_splitting(centerlines) 
smoothed_centerlines = vmtk_centerline_smoothing(splitted_centerlines)
merged_splitted_centerlines = vmtk_centerlinemerge(smoothed_centerlines)

</code></pre>
<p>Thank you</p>

---

## Post #2 by @tomo-akiyama (2024-06-10 07:55 UTC)

<p>After testing by extracting centerlines from only a part of the cerebral vessels, smoothing, and then merging, it worked without any issues.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3ca1fe223b539f99d508272e44bedd7fcb8306b5.jpeg" data-download-href="/uploads/short-url/8EnIokxyZMJ902dzlpsX8rgUzZ3.jpeg?dl=1" title="スクリーンショット 2024-06-10 16.28.22" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3ca1fe223b539f99d508272e44bedd7fcb8306b5_2_408x375.jpeg" alt="スクリーンショット 2024-06-10 16.28.22" data-base62-sha1="8EnIokxyZMJ902dzlpsX8rgUzZ3" width="408" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3ca1fe223b539f99d508272e44bedd7fcb8306b5_2_408x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3ca1fe223b539f99d508272e44bedd7fcb8306b5_2_612x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3ca1fe223b539f99d508272e44bedd7fcb8306b5_2_816x750.jpeg 2x" data-dominant-color="A8A8B1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2024-06-10 16.28.22</span><span class="informations">1730×1590 179 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fb5141102b21192b83ff6c2100c4fec0e178987.png" data-download-href="/uploads/short-url/kvieGJAYTfxvMV6odDVTnQLHqnR.png?dl=1" title="スクリーンショット 2024-06-10 16.35.45" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fb5141102b21192b83ff6c2100c4fec0e178987_2_517x342.png" alt="スクリーンショット 2024-06-10 16.35.45" data-base62-sha1="kvieGJAYTfxvMV6odDVTnQLHqnR" width="517" height="342" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fb5141102b21192b83ff6c2100c4fec0e178987_2_517x342.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/f/8fb5141102b21192b83ff6c2100c4fec0e178987_2_775x513.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/f/8fb5141102b21192b83ff6c2100c4fec0e178987.png 2x" data-dominant-color="D3DADB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2024-06-10 16.35.45</span><span class="informations">914×606 376 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Next, I thought it might be a problem with the number of inlets, so I used two inlets and specified endpoints partially instead of all of them, and this also worked well.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/5/350c79ced1082e09cd0a5a172c49ca59965b4fe7.jpeg" data-download-href="/uploads/short-url/7zi2bs9foksmLqhfi4TUIr8sNoj.jpeg?dl=1" title="スクリーンショット 2024-06-10 16.42.06" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/350c79ced1082e09cd0a5a172c49ca59965b4fe7_2_502x375.jpeg" alt="スクリーンショット 2024-06-10 16.42.06" data-base62-sha1="7zi2bs9foksmLqhfi4TUIr8sNoj" width="502" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/350c79ced1082e09cd0a5a172c49ca59965b4fe7_2_502x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/350c79ced1082e09cd0a5a172c49ca59965b4fe7_2_753x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/5/350c79ced1082e09cd0a5a172c49ca59965b4fe7_2_1004x750.jpeg 2x" data-dominant-color="A4A5BF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2024-06-10 16.42.06</span><span class="informations">1920×1431 172 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a759c203f6d2caa076916f6d9d907fe98b8872cc.png" data-download-href="/uploads/short-url/nSs2EZgClNIyl0JX8eb4lYTUtJ2.png?dl=1" title="screenshot" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a759c203f6d2caa076916f6d9d907fe98b8872cc_2_517x340.png" alt="screenshot" data-base62-sha1="nSs2EZgClNIyl0JX8eb4lYTUtJ2" width="517" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a759c203f6d2caa076916f6d9d907fe98b8872cc_2_517x340.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a759c203f6d2caa076916f6d9d907fe98b8872cc_2_775x510.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a759c203f6d2caa076916f6d9d907fe98b8872cc.png 2x" data-dominant-color="E2E7E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot</span><span class="informations">910×600 233 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It seems that increasing the number of endpoints causes an error at some point.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/3150a4b7c1534fdffed019df6233a0e1279d61dd.jpeg" data-download-href="/uploads/short-url/72gaM5LWP8J4cDgtPVeQuV4dw0B.jpeg?dl=1" title="スクリーンショット 2024-06-10 16.58.17" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3150a4b7c1534fdffed019df6233a0e1279d61dd_2_314x250.jpeg" alt="スクリーンショット 2024-06-10 16.58.17" data-base62-sha1="72gaM5LWP8J4cDgtPVeQuV4dw0B" width="314" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3150a4b7c1534fdffed019df6233a0e1279d61dd_2_314x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3150a4b7c1534fdffed019df6233a0e1279d61dd_2_471x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/1/3150a4b7c1534fdffed019df6233a0e1279d61dd_2_628x500.jpeg 2x" data-dominant-color="A4A4C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">スクリーンショット 2024-06-10 16.58.17</span><span class="informations">1920×1527 164 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e188aa37bbd46512c613da6914545aacfe2c6947.png" data-download-href="/uploads/short-url/wbaevN0o9PaFViBV5ZTq7hciwcf.png?dl=1" title="screenshot１" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e188aa37bbd46512c613da6914545aacfe2c6947_2_517x340.png" alt="screenshot１" data-base62-sha1="wbaevN0o9PaFViBV5ZTq7hciwcf" width="517" height="340" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e188aa37bbd46512c613da6914545aacfe2c6947_2_517x340.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e188aa37bbd46512c613da6914545aacfe2c6947_2_775x510.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e188aa37bbd46512c613da6914545aacfe2c6947.png 2x" data-dominant-color="ECEEEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">screenshot１</span><span class="informations">910×600 169 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Does anyone have a solution for this?</p>

---

## Post #3 by @Tracy (2025-02-27 20:35 UTC)

<p>Hi tomo-san,</p>
<p>I would like to use vmtkscripts as well, but face the error</p>
<hr>
<p>ModuleNotFoundError                       Traceback (most recent call last)<br>
Cell In[1], line 2<br>
1 import slicer<br>
----&gt; 2 from vmtk import vmtkscripts<br>
3 import vtk</p>
<p>ModuleNotFoundError: No module named ‘vmtk’</p>
<p>Can you tell me how to install vmtk within the slicer?<br>
Thank you so much.</p>
<p>Best,<br>
Tracy</p>

---
