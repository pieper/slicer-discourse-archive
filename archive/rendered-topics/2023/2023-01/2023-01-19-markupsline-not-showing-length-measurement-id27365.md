# MarkupsLine not showing length measurement?

**Topic ID**: 27365
**Date**: 2023-01-19
**URL**: https://discourse.slicer.org/t/markupsline-not-showing-length-measurement/27365

---

## Post #1 by @mikebind (2023-01-19 19:13 UTC)

<p>In previous versions of Slicer, the length measurement was shown on the 3D view, but for some reason it doesn’t seem to be working for me now.  I have a MarkupsLine node with two control points, but the length measurement is not being calculated<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e7ff09236a0edbd959fd6749894618ebd222a9a.png" data-download-href="/uploads/short-url/bcrlQg371cpbkaAdiadjyrSvkWS.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7ff09236a0edbd959fd6749894618ebd222a9a_2_532x500.png" alt="image" data-base62-sha1="bcrlQg371cpbkaAdiadjyrSvkWS" width="532" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4e7ff09236a0edbd959fd6749894618ebd222a9a_2_532x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e7ff09236a0edbd959fd6749894618ebd222a9a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4e7ff09236a0edbd959fd6749894618ebd222a9a.png 2x" data-dominant-color="F9F9FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">579×544 31.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Any suggestions? Or is there a different way I need to trigger this?  Obviously it’s trivial to do the calculation myself, but previously this “just worked” in Slicer, so this seems like a bug.</p>
<p>I’m using Slicer 5.2.1. I just verified that opening a new Slicer instance and a single volume and adding a single MarkupsLine still shows this behavior (meaning it’s probably not caused by something weird I did in my current Slicer session).  I also copied and pasted this section from <a href="https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Modules/Loadable/Markups/Testing/Python/MarkupsMeasurementsTest.py">https://github.com/Slicer/Slicer/blob/a5f75351073ef62fd6198d9480d86c0009d70f9b/Modules/Loadable/Markups/Testing/Python/MarkupsMeasurementsTest.py</a></p>
<blockquote>
<p>markupsNode = slicer.mrmlScene.AddNewNodeByClass(‘vtkMRMLMarkupsLineNode’)<br>
length = 34.12<br>
direction = np.array([0.3, -0.4, 0.8])<br>
pos1 = np.array([20, -12.4, 3.8])<br>
pos2 = pos1 + direction / np.linalg.norm(direction) * length<br>
markupsNode.AddControlPoint(vtk.vtkVector3d(pos1))<br>
markupsNode.AddControlPoint(vtk.vtkVector3d(pos2))</p>
<p>measurement = markupsNode.GetMeasurement(“length”)<br>
if abs(measurement.GetValue() - length) &gt; 1e-4:<br>
raise Exception("Unexpected length value: " + str(measurement.GetValue()))</p>
</blockquote>
<p>This gives the error “Unexpected length value: 0.0”, so I think that means that this test should not have passed, and also it is not just my code or behavior which is leading to this.</p>

---

## Post #2 by @jamesobutler (2023-01-19 19:59 UTC)

<aside class="quote no-group" data-username="mikebind" data-post="1" data-topic="27365">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> mikebind:</div>
<blockquote>
<p>I just verified that opening a new Slicer instance and a single volume and adding a single MarkupsLine still shows this behavior (meaning it’s probably not caused by something weird I did in my current Slicer session).</p>
</blockquote>
</aside>
<p>I have tried to replicate on my Windows machine, but I am observing that Slicer 5.2.1 is working appropriately by showing the line measurement. I also do not have any extensions installed. If you uninstall any extensions and re-install Slicer 5.2.1 fresh, do you have the same issues?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c8136240b98444871a96116bd9ccdca839cf5e7e.jpeg" data-download-href="/uploads/short-url/sxX1t3ZVlSXf7C78X18XPFR8AYS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8136240b98444871a96116bd9ccdca839cf5e7e_2_690x373.jpeg" alt="image" data-base62-sha1="sxX1t3ZVlSXf7C78X18XPFR8AYS" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8136240b98444871a96116bd9ccdca839cf5e7e_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8136240b98444871a96116bd9ccdca839cf5e7e_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c8136240b98444871a96116bd9ccdca839cf5e7e_2_1380x746.jpeg 2x" data-dominant-color="7A7A83"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 266 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have also tried programmatically, but I’m still seeing correct behavior</p>
<pre data-code-wrap="python"><code class="lang-python">import SampleData
SampleData.SampleDataLogic().downloadMRHead()

markupsNode = slicer.mrmlScene.AddNewNodeByClass('vtkMRMLMarkupsLineNode')
markupsNode.AddControlPoint(0,0,0)
markupsNode.AddControlPoint(10,10,10)
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43b3f0143984ac690121f04a4aa5d97a5adc0d2e.png" data-download-href="/uploads/short-url/9EVvl86bjXQxqUa6g5MpGYQbeHA.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43b3f0143984ac690121f04a4aa5d97a5adc0d2e_2_690x373.png" alt="image" data-base62-sha1="9EVvl86bjXQxqUa6g5MpGYQbeHA" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43b3f0143984ac690121f04a4aa5d97a5adc0d2e_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43b3f0143984ac690121f04a4aa5d97a5adc0d2e_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/3/43b3f0143984ac690121f04a4aa5d97a5adc0d2e_2_1380x746.png 2x" data-dominant-color="999A9F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1040 268 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @mikebind (2023-01-20 17:48 UTC)

<p>Thanks for checking.  I will try without extensions when I get a chance.</p>

---
