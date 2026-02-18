# CropVolumeSequence does not respect transforms

**Topic ID**: 8864
**Date**: 2019-10-22
**URL**: https://discourse.slicer.org/t/cropvolumesequence-does-not-respect-transforms/8864

---

## Post #1 by @mikebind (2019-10-22 18:35 UTC)

<p>Hello, I have used the CropVolumeSequence module in the past to successfully crop a volume sequence into a new sequence.  However, in my current use case, I have a transformed volume sequence and a transformed cropping ROI, and the output crop volume sequence is empty, I believe because the CropVolumeSequence code does not properly account for one or both of the transforms.  Interestingly, the CropVolume module does just fine for each individual frame of the sequence, and I was able to achieve the desired effect by simply stepping through the frames and pressing the Apply button in the CropVolume module (after first checking the Save Changes checkbox in the sequence browser for the cropped sequence).  I was surprised this worked because I thought the CropVolumeSequence module probably just used the logic of the CropVolume module, but it also means that this bug should be very easy to fix.</p>

---

## Post #2 by @lassoan (2019-10-22 21:05 UTC)

<p>CropVolumeSequence is just a simple scripted module that iterates through the sequence and uses Crop Volume module on each frame. It should work well with any transformation combination.</p>
<p>The actual cropping operation is just <a href="https://github.com/SlicerRt/Sequences/blob/master/CropVolumeSequence/CropVolumeSequence.py#L170-L241" rel="nofollow noopener">70 lines</a>. It would be great if you could have a look at it yourself, maybe <a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/DebuggingTools" rel="nofollow noopener">step through it using a Python debugger</a> to see why it is not working for you.</p>

---
