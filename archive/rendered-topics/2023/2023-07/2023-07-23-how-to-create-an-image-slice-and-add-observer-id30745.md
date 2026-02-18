# How to create an image slice and add observer

**Topic ID**: 30745
**Date**: 2023-07-23
**URL**: https://discourse.slicer.org/t/how-to-create-an-image-slice-and-add-observer/30745

---

## Post #1 by @slicer365 (2023-07-23 10:35 UTC)

<p>This is a volume slice created by other module, and I can display different slices by dragging the position.<br>
This  is not a plane, but a volume node with only one sheet</p>
<p>so that I can transfer the sigle volume to other programs in real time through IGT.</p>
<p>I would like to ask if there are other ways or script  to create this kind of slice, and I  can specify the length and width of the slice</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/744d4a847e7ace550fc79b981ccbe06f7039065e.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/744d4a847e7ace550fc79b981ccbe06f7039065e.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/744d4a847e7ace550fc79b981ccbe06f7039065e.mp4</a>
    </video>
  </div><p></p>

---

## Post #2 by @ungi (2023-07-24 02:26 UTC)

<p>Hi, maybe this script helps: <a href="https://gist.github.com/ungi/80442ac03b5ea9ed6ae680a800837ece" class="inline-onebox" rel="noopener nofollow ugc">Volume reslice with tracking · GitHub</a><br>
You need to install the SlicerIGT extension for the Volume Reslice Driver module to use this script.<br>
It uses a transform node (SliceToRas). Every time that transform changes, it updates the 2D images that is resliced from the 3D volume.</p>

---

## Post #3 by @slicer365 (2023-07-24 10:56 UTC)

<p>Yes,this is what I want ,thank you very much,Mr Ungi ！</p>

---

## Post #4 by @derekcbr (2023-11-22 13:24 UTC)

<p>Hi ungi,<br>
Great script so far. Is it possible to control three slices red, green and yellow together in the meantime by using the same matrix?<br>
sliceToRasTransform = vtk.vtkTransform()<br>
sliceToRasTransform.SetMatrix(my_matrix)<br>
Thanks a lot!</p>

---

## Post #5 by @ungi (2023-11-22 13:33 UTC)

<p>If you duplicate the code under “Show and follow output image in red slice view” and replace the word “red” with “green”, then the green slice will do the same as the red. And you may repeat this with the yellow slice too. But I’m not sure I understand what you want to achieve. Why would you show the same slice three times? They are duplicates in the 2D views, and they overlap and hide each other in the 3D view.</p>

---

## Post #6 by @derekcbr (2023-11-22 13:40 UTC)

<p>Thank you for the quick answer. If I pass the same matrix to sliceToRasTransform for green, red and yellow slice.<br>
sliceToRasNode = slicer.mrmlScene.GetFirstNodeByName(“SliceToRas_%s” % strcolor)<br>
outputNode = slicer.mrmlScene.GetFirstNodeByName(“OutputVolume_%s” % strcolor)<br>
They will generate the same image? Or different image slice?<br>
Thanks a lot!</p>

---

## Post #7 by @ungi (2023-11-22 14:54 UTC)

<p>The same transform matrix will generate the same image. If you want the same image in all views, then you don’t need to change the code related to reslice, because you can reuse the same image in all the views. Just duplicate lines 87-93 and change “red” to “green”.</p>

---

## Post #8 by @derekcbr (2023-11-23 01:05 UTC)

<p>Hi Ungi,<br>
Thanks a lot for the help! Will try again.</p>

---

## Post #9 by @derekcbr (2023-11-25 00:19 UTC)

<p>Hi Tamas,<br>
I found that by using your script can achieve the same functions by SetSliceToRASByNTP. One question is that in your script it does not use SetSliceToRASByNTP to position the slice. Is there any difference between your script and uusing SetSliceToRASByNTP? Thanks  a lot!</p>

---

## Post #10 by @ungi (2023-11-25 00:42 UTC)

<p>It should be possible to achieve the same function using SetSliceToRASByNTP too. I just use Volume Reslice Driver for moving the slice, because that is more common in IGT applications. It has a user interface so we don’t always need to code.</p>

---

## Post #11 by @derekcbr (2023-11-25 00:54 UTC)

<p>Hi Tamas,<br>
Ok that is good to know. Also after running the script, one of the slice edge point is on the center of wireframe box. Is it possible to overlap the center with the  wireframe box? Thanks a lot!</p>

---

## Post #12 by @ungi (2023-11-25 00:58 UTC)

<p>Do you mean the yellow coordinate system model? I don’t see a wireframe box after running the script. If you mean the yellow model, then you can add a transform node in the transform hierarchy tree (Data module) between the model and the SliceToRAS transform to move the model relative to the slice.</p>

---

## Post #13 by @derekcbr (2023-11-25 01:10 UTC)

<p>Hi Tamas,<br>
Thank you for the clarification. That is what I want.</p>

---

## Post #14 by @derekcbr (2023-11-29 06:23 UTC)

<p>Hi Tamas,<br>
Another question is when I rotate the red, green and yellow slice, is it possible to rotate by the image slice’s center point? Now it seems that it is rotated by the points on the edges. Thanks.</p>

---

## Post #15 by @ungi (2023-11-29 13:54 UTC)

<p>Last time I checked, this was not directly possible. See comment near the beginning of the script. But of course you may create additional transforms in the scene and set up the transform hierarchy to achieve the same effect. Similar to how the yellow model can be translated to the center of the slice.</p>

---

## Post #16 by @derekcbr (2023-11-30 04:56 UTC)

<p>Thanks a lot for help!</p>

---
