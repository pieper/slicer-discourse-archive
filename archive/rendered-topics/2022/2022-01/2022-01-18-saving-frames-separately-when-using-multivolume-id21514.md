# Saving frames separately when using MultiVolume

**Topic ID**: 21514
**Date**: 2022-01-18
**URL**: https://discourse.slicer.org/t/saving-frames-separately-when-using-multivolume/21514

---

## Post #1 by @Mark_Brahier (2022-01-18 15:02 UTC)

<p>Hello, is there a way to easily download frames separately when using MultiVolume? I am using retrospectively gated CTs with about 20 frames (one at each 5% of the cardiac cycle). I would like to download as 20 separate files, each representing some % of the cardiac cycle… is there a way to do this?</p>

---

## Post #2 by @mikebind (2022-01-19 01:33 UTC)

<p>One workaround I have used is to load the multivolume as a Sequence (I’m not sure if that’s what you’ve done or not), then clone each frame of the sequence to save separately.  The process for this is:</p>
<ol>
<li>Right-click on the multivolume/sequence node in the “Data” module and click “Clone”. A copy of this volume will appear below.  Then right click on that new cloned volume and click “Export to file…” and save in your desired format</li>
<li>Advance to the next frame using the sequence browser’s “next frame” button and then repeat Step 1.</li>
</ol>
<p>At the end of this process you would have the 20 separate volumes in your scene (21 if you count the original sequence).  If you don’t see the Sequence Browser, you can show it in the toolbar by checking the following box:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/134029793114b18ee33df8f10fa7ca2e5d3e761d.png" alt="image" data-base62-sha1="2KixnC6yVpgSi2qBSO7gDHyqC3r" width="635" height="421"></p>

---

## Post #3 by @lassoan (2022-01-19 02:41 UTC)

<p>It could be nicer to avoid splitting up a 4D volume sequence into separate 3D volume files, because you would lose some context and metadata, such as order and timestamp of each volume. You may find that you don’t need to split up the volume sequence into separate files:</p>
<ul>
<li>You can easily <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#access-voxels-of-a-4d-volume-as-numpy-array">access the voxels of each volume as a numpy array</a> in Slicer’s Python environment.</li>
<li>You can iterate through the sequence, the volumes one by one - as it is done in <a href="https://github.com/moselhy/SlicerSequenceRegistration/blob/master/SequenceRegistration/SequenceRegistration.py">Sequence Registration</a> and <a href="https://github.com/Slicer/Slicer/blob/60042b1ef63ef262289a6d1ea0eaa6399d5cbcde/Modules/Scripted/CropVolumeSequence/CropVolumeSequence.py#L226-L235">Crop Volume Sequence modules</a>.</li>
<li>If you need to process the volume sequence outside Slicer’s Python environment, then you can save the volume sequence as a 4D nrrd file and load it in any Python environment using <a href="https://pypi.org/project/pynrrd/">pynrrd</a>.</li>
</ul>

---
