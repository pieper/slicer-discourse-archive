# We aren't getting the filtering options to display while using parenchyma analysis package on a few chest CTs.

**Topic ID**: 33098
**Date**: 2023-11-28
**URL**: https://discourse.slicer.org/t/we-arent-getting-the-filtering-options-to-display-while-using-parenchyma-analysis-package-on-a-few-chest-cts/33098

---

## Post #1 by @punyasharoul (2023-11-28 20:48 UTC)

<p>Operating system: Windows &amp; MAC<br>
Slicer version: 4-10-2<br>
Expected behavior:</p>
<ol>
<li>
<p>Filtering on and off should display options.</p>
</li>
<li>
<p>output for attenuation areas should be generated as numbers<br>
Actual behavior:<br>
We are facing below 2 key issues below and hope we can connect again to troubleshoot.</p>
</li>
<li>
<p>We aren’t getting the filtering options to display. There is an error message that pops up that makes us think there might be an issue with the code for displaying these. Here is the error message:</p>
</li>
</ol>
<pre><code class="lang-auto">Traceback (most recent call last):
File "C:\Users\bryant.england\OneDrive - University of Nebraska Medical Center\Documents\SlicerCIP4-10-2\SlicerCIP4-10-2-Extensions\Chest_Imaging_Platform\lib\Slicer-4.10\qt-scripted-modules\CIP\ui\PreProcessingWidget.py", line 198, in hideFilterParams
self.showFilterOptions(False)
File "C:\Users\bryant.england\OneDrive - University of Nebraska Medical Center\Documents\SlicerCIP4-10-2\SlicerCIP4-10-2-Extensions\Chest_Imaging_Platform\lib\Slicer-4.10\qt-scripted-modules\CIP\ui\PreProcessingWidget.py", line 216, in showFilterOptions
self.filterOptionsFrame.setShown(show)
AttributeError: QFrame has no attribute named 'setShown'
Traceback (most recent call last):
File "C:\Users\bryant.england\OneDrive - University of Nebraska Medical Center\Documents\SlicerCIP4-10-2\SlicerCIP4-10-2-Extensions\Chest_Imaging_Platform\lib\Slicer-4.10\qt-scripted-modules\CIP\ui\PreProcessingWidget.py", line 195, in showFilterParams
self.showFilterOptions(True)
File "C:\Users\bryant.england\OneDrive - University of Nebraska Medical Center\Documents\SlicerCIP4-10-2\SlicerCIP4-10-2-Extensions\Chest_Imaging_Platform\lib\Slicer-4.10\qt-scripted-modules\CIP\ui\PreProcessingWidget.py", line 216, in showFilterOptions
self.filterOptionsFrame.setShown(show)
AttributeError: QFrame has no attribute named 'setShown'
</code></pre>
<ol start="2">
<li>If we try to create a lung label map despite the above error, it seems to create a map and segment the lungs. However, no output for attenuation areas is generated. Attached is a screenshot of the result:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/c/ec909bd04aefbec30a902a7301725e8d9daf6a74.jpeg" data-download-href="/uploads/short-url/xKKvlCd00zD7N3VcnfQh3mHrcNe.jpeg?dl=1" title="CIP_Issue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec909bd04aefbec30a902a7301725e8d9daf6a74_2_690x375.jpeg" alt="CIP_Issue" data-base62-sha1="xKKvlCd00zD7N3VcnfQh3mHrcNe" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec909bd04aefbec30a902a7301725e8d9daf6a74_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec909bd04aefbec30a902a7301725e8d9daf6a74_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/c/ec909bd04aefbec30a902a7301725e8d9daf6a74_2_1380x750.jpeg 2x" data-dominant-color="9998A9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">CIP_Issue</span><span class="informations">1911×1039 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>
<p>Several Debug, Error, Info, and Critical messages appear. The last of these which we wonder if it might be the most serious is the following:</p>
<pre><code class="lang-auto">Traceback (most recent call last):
File "C:/Users/bryant.england/OneDrive - University of Nebraska Medical Center/Documents/SlicerCIP4-10-2/bin/../SlicerCIP4-10-2-Extensions/Chest_Imaging_Platform/lib/Slicer-4.10/qt-scripted-modules/CIP_ParenchymaAnalysis.py", line 434, in onApply
if not self.inputVolumesAreValid():
File "C:/Users/bryant.england/OneDrive - University of Nebraska Medical Center/Documents/SlicerCIP4-10-2/bin/../SlicerCIP4-10-2-Extensions/Chest_Imaging_Platform/lib/Slicer-4.10/qt-scripted-modules/CIP_ParenchymaAnalysis.py", line 362, in inputVolumesAreValid
self.createLungLabelMap()
File "C:/Users/bryant.england/OneDrive - University of Nebraska Medical Center/Documents/SlicerCIP4-10-2/bin/../SlicerCIP4-10-2-Extensions/Chest_Imaging_Platform/lib/Slicer-4.10/qt-scripted-modules/CIP_ParenchymaAnalysis.py", line 408, in createLungLabelMap
input_array = vtk.util.numpy_support.vtk_to_numpy(label_image.GetPointData().GetScalars())
AttributeError: 'module' object has no attribute 'util'
</code></pre>

---

## Post #2 by @rbumm (2023-11-29 02:31 UTC)

<p>Please fully install the latest version of 3D Slicer and try again. Would be great if you could report back.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/90326825e300ab7840011ac1e5fa3b0fcc034276.jpeg" data-download-href="/uploads/short-url/kzCKCd3yqVU5t6geUc3gMXJI3hY.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90326825e300ab7840011ac1e5fa3b0fcc034276_2_690x341.jpeg" alt="image" data-base62-sha1="kzCKCd3yqVU5t6geUc3gMXJI3hY" width="690" height="341" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90326825e300ab7840011ac1e5fa3b0fcc034276_2_690x341.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90326825e300ab7840011ac1e5fa3b0fcc034276_2_1035x511.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/90326825e300ab7840011ac1e5fa3b0fcc034276_2_1380x682.jpeg 2x" data-dominant-color="A5A5AE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1397×691 163 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @punyasharoul (2023-11-29 16:44 UTC)

<p>Thank you, Rudolf, for your response !</p>
<p>We installed the version from:<br>
cip.bwh.harvard.edu</p>
<p>Is that the latest version you are suggesting?</p>
<p>Punyasha</p>

---

## Post #4 by @rbumm (2023-11-29 16:49 UTC)

<p>You should install the chest imaging platform from 3D Slicers installation manager.</p>

---
