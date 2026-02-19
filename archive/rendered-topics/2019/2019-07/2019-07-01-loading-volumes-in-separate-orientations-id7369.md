---
topic_id: 7369
title: "Loading Volumes In Separate Orientations"
date: 2019-07-01
url: https://discourse.slicer.org/t/7369
---

# Loading Volumes in separate orientations

**Topic ID**: 7369
**Date**: 2019-07-01
**URL**: https://discourse.slicer.org/t/loading-volumes-in-separate-orientations/7369

---

## Post #1 by @ArisD (2019-07-01 11:58 UTC)

<p>Hi everyone,</p>
<p>New user here - all the examples I’ve found in the documentation show loading a volume and following that, all three orientations are shown separately.</p>
<p>The files I need to study are DICOM files and, moreover, they have been exported in three separate folders, each one having its own orientation.</p>
<p>I have not been able to load them and put them together. It loads them successively and I only end up with one of the three orientations instead of all of them at the same time.</p>
<p>Our files cannot be exported in any other manner in DICOM format I’m afraid (we use an older version of VGStudio Max for that).</p>
<p>Any suggestions most welcome.</p>
<p>Many thanks in advance.</p>

---

## Post #2 by @pieper (2019-07-01 12:37 UTC)

<p>Hi  - it sounds like you have a similar issue to the one described in these posts:</p>
<p><a href="https://discourse.slicer.org/t/3d-model-from-dicoms">https://discourse.slicer.org/t/3d-model-from-dicoms</a></p>
<p><a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing">https://discourse.slicer.org/t/combining-volumes-what-am-i-missing</a></p>

---

## Post #3 by @ArisD (2019-07-09 08:35 UTC)

<p>Hi,</p>
<p>None of these were helpful I’m afraid.</p>
<p>What I have is three folders, each having over 1200 images that are stacked in a certain orientation.</p>
<p>I need to load these sets of images separately for each orientation and then have slicer combine them into a 3D model.</p>
<p>I haven’t found any specific instructions on how to do that.</p>
<p>I am trying to drag and drop them onto specific views to no avail.</p>
<p>Each attempt takes about 30mins for the images to load and its becoming frustrating.</p>
<p>Please advise.</p>

---

## Post #4 by @pieper (2019-07-09 13:53 UTC)

<p>Hi -</p>
<p>Are you using the DICOM module or the Add Data button?  Are you selecting all the files or just one?  If it takes 30 minutes it maybe you need to try <a href="https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/LoadingData" rel="nofollow noopener">selecting one file and unchecking the Single File option</a></p>
<p>If that doesn’t work maybe you can get better help if you describe a little more about the data and what you are trying to accomplish?  It doesn’t sound like a standard medical imaging pipeline so maybe Slicer isn’t set up for it.</p>
<p>Where did the data come from (what type of scanner? what scan parameters?)</p>
<p>What did you do in VGStudio Max?</p>
<p>What do you mean by combine the images?  What’s different about them and how to you expect the resulting model to be different?</p>

---

## Post #5 by @ArisD (2019-07-10 05:08 UTC)

<p>Hi!</p>
<p>I am:</p>
<ol>
<li>using the add DICOM data button</li>
<li>selecting all the files at once</li>
<li>I can’t select one file at a time as there are about 1200 files on each orientation</li>
<li>the data came from a custom scanner - don’t have the parameters with me but each slice is about 0.002mm from the next</li>
<li>Someone exported these orientations into DICOM files using VGStudio Max (not me so I don’t know what they did)</li>
<li>By combining the images I expect a 3D model - at the time there is none forming. Each time I load a batch of files from a specific orientation they are loaded in the same axial orientation. For example I load the top orientation files (takes several minutes- like I said over 1200 images per orientation), and when I load the e.g. left orientation files afterwards, they are loaded in the top orientation again, replacing the previous files, instead of allowing me somehow to load the next files as a novel orientation and combine all three orientations into a 3D model that I can rotate zoom in out etc.</li>
<li>The scanned object is an archaeological artefact.</li>
</ol>
<p>Thanks in advance!</p>

---

## Post #6 by @lassoan (2019-07-10 11:52 UTC)

<p>If your main problem is that you can load 3 anisotropic volumes (much smaller in-slice pixel size than distance between slices) then <a class="mention" href="/u/pieper">@pieper</a>’s first response refers to the most relevant answers we can give now. In short, there is no tools available to combine multiple anisotropic volumes to somehow create an isotropic volume. If that was easily possible then algorithms would be readily available but they are not. There have been reports of attempts of such reconstructions in the literature (including some recent ones using machine learning) that you may try to reimplement.</p>
<p>Fortunately, you don’t need to combine multiple volumes to create 3D models. You can load one of the volumes (which have the highest resolution in the most relevant image plane direction) and create 3D models from that.</p>
<p>If loading time is an issue then import and load each volume and save as uncompressed nrrd file. DICOM series containing few-thousand slices take several minutes to import and about a minute to load. Loading the same series from uncompressed nrrd usually takes about 5-15 seconds.</p>

---

## Post #7 by @ArisD (2019-07-10 13:16 UTC)

<p>Thank you for the reply.</p>
<p>VGStudioMax allows us to export the files under the following formats:</p>
<p>Raw volume<br>
Image stack<br>
Analyze volume<br>
DICOM image series<br>
HDF volume<br>
Export multiple volumes<br>
Polygon</p>
<p>would any of the above export options work with 3d slicer?</p>
<p>Thanks!</p>

---

## Post #8 by @pieper (2019-07-11 19:14 UTC)

<p>DICOM should be working, but you could also test Analyze.</p>

---
