# Call "Center Volume" button from python script

**Topic ID**: 1132
**Date**: 2017-09-27
**URL**: https://discourse.slicer.org/t/call-center-volume-button-from-python-script/1132

---

## Post #1 by @mangotee (2017-09-27 12:29 UTC)

<p>Hi all,</p>
<p>In the Volumes module, there is a “Center Volume” button. Unfortunately, I cannot find how to call this button from a python script… I know how to do this e.g. with an ITK workaround (using sitkUtils as sitku):</p>
<p>def centerVolume(volNodeName):<br>
img = sitku.PullFromSlicer(volNodeName)<br>
newCenter=-0.5*np.array(img.GetSize())*np.array(img.GetSpacing())<br>
img.SetOrigin(tuple(newCenter.tolist()))<br>
sitku.PushToSlicer(img,volNodeName,compositeView=0,overwrite=True)</p>
<p>However, this pushes an entirely new volume, and I lose the volumes location in the transformation chain and visualization settings (colormap, window/level/contrast etc.).<br>
The “Center Volume” button just centers the volume coordinates without changing its properties in the mrml scene.</p>
<p>Thanks and cheers,<br>
Ahmad</p>

---

## Post #2 by @lassoan (2017-09-27 12:46 UTC)

<p>Use <code>slicer.util.setSliceViewerLayers</code> method. Type <code>help(slicer.util.setSliceViewerLayers)</code> for documentation.</p>
<p>You can always have a look at the source code if you are interested in what a method does internally. In this case, it is <a href="https://github.com/Slicer/Slicer/blob/533559a7fe9f02253637c1dc3a9bb56a2b220b43/Base/Python/sitkUtils.py#L231">here</a>.</p>

---

## Post #3 by @mangotee (2017-09-27 13:04 UTC)

<p>Hi Andras,</p>
<p>thanks as always for your fast response!<br>
I think there is a misunderstanding… I am not interesting in centering<br>
the slice views on a certain volume.<br>
Instead, I would like to call the logic of the button “Center Volume” (in<br>
module “Volumes”, sub-panel “Volume Information”). It changes the “Image<br>
Origin” property of the volume.</p>
<p>Cheers,<br>
Ahmad</p>

---

## Post #4 by @lassoan (2017-09-27 21:15 UTC)

<p>Code that computes the origin that centers the volume is available <a href="https://github.com/Slicer/Slicer/blob/d1bc71e59abf1405a5f14fb8e7c3250915d83607/Libs/MRML/Widgets/qMRMLVolumeInfoWidget.cxx#L117-L143">here</a>.</p>
<p>However, <strong>volume centering should never be used</strong> for anything else than troubleshooting! Need for centering is typically a sign of an error in the data processing workflow.</p>
<p>Can you explain why you need to center the volume?</p>

---

## Post #5 by @mangotee (2017-09-28 11:30 UTC)

<p>Hi Andras,</p>
<p>I agree, usually centering volumes is dangerous, e.g. because it is difficult to undo (without code), and it is better to work with transformations and the transform hierarchy.<br>
However, there are scenarios where it is useful, I have not used this feature in years, but recently, there were two situations where I used hard-centering:</p>
<ol>
<li>I created a new volume (e.g. a small Gaussian blob, i.e. a voxelized fiducial) from scratch in numpy, converted it to an ITK object via sitk and pushed it to Slicer via sitku. There, I would have liked to center it programatically, such that I can quickly apply transformations to it and accurately position the center of the volume (instead of, say one of the corners). I couldn’t find a way to trigger that button programatically, so I coded the centering on the ITK volume before pushing (with the code I wrote in my previous post). In this case, it’s ok, because I am pushing a new volume to the scene and I don’t care about pre-existing transformations/visualizations etc…</li>
<li>I resampled small ROIs of the same anatomy in brain MRI from left and right hemisphere from which I wanted to create a group template. To do so, “Crop Volume” module resamples in-place (which is good), but to export the ROIs, I wanted to center all of them and L/R mirror all ROIs from left to right side in Slicer(!), so that the external template creation routine can run rightaway without initialization methods (the ROI center-point was carefully chosen for all crops). Before export, I wanted to check overlay quality of these crops, and the centering via sitku’s PullFromSlicer/sitk-center/PushToSlicer does the job, but the coloring and contrast of the ROI crops got lost, because a new volume is created. A bit inconvenient, but nothing dramatic.</li>
</ol>
<p>These are both very peculiar and rare things to do, and the “Center Volume” button is rarely useful, but in these two cases, it would have done the job nicely.<br>
Since it is not callable from code though, I will implement my own scripted method. Thanks for the link to the sample code!</p>
<p>Cheers,A</p>

---

## Post #6 by @lassoan (2017-09-28 23:46 UTC)

<aside class="quote no-group" data-username="mangotee" data-post="5" data-topic="1132">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/c57346/48.png" class="avatar"> mangotee:</div>
<blockquote>
<p>PullFromSlicer/sitk-center/PushToSlicer does the job, but the coloring and contrast of the ROI crops got lost,</p>
</blockquote>
</aside>
<p>Yes, the old sitkUtils push/pull methods were very limited and had several side effects (mess up visualization, create new nodes, etc). Use this new function instead, where you can specify an existing target node:</p>
<pre><code>PushVolumeToSlicer(sitkimage, targetNode=None, name=None, className='vtkMRMLScalarVolumeNode')
</code></pre>
<p>Also note that for centering the volume, you don’t need to export it to a SimpleITK image. Just adjust the origin of the volume node using its SetOrigin() method.</p>

---

## Post #7 by @mangotee (2017-09-29 09:38 UTC)

<p>Thanks, Andras! Didn’t know about these new functions?<br>
Where are they included? Can’t find it in sitkUtils… Do I have to download a new nightly version?</p>

---

## Post #8 by @lassoan (2017-09-29 13:01 UTC)

<p>Yes, it is in the nightly. As the stable build is almost a year old, I would recommend everybody to use the nightly build. We’ll release a new stable version based on the current nightly version in a couple of weeks.</p>

---

## Post #9 by @mangotee (2017-09-29 13:31 UTC)

<p>I do use the nightly, but it’s a couple of weeks old and you guys are just too fast! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"> So much new functionality on a constant basis, I should make a weekly habit of downloading the nightly. Thanks to you and the entire team for all the great work, Slicer has become a real workhorse in my research, since I learned how to script my workflows!</p>

---
