# Scaling segmentation models in X-Y plane

**Topic ID**: 35417
**Date**: 2024-04-10
**URL**: https://discourse.slicer.org/t/scaling-segmentation-models-in-x-y-plane/35417

---

## Post #1 by @Von (2024-04-10 18:39 UTC)

<p>Operating system: Windows 11<br>
Slicer version: 4.10.2<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hello,</p>
<p>I have a huge array of screenshots that contains information that I cannot disclose. I manage to make a 3D model of the screenshot using threshold feature on the segmentation editor, but when I export the  model as an STL, the size is too big. The length of the model is correct, but the height and width are too big. Is there a way to scale the height and width (looking at it in a P and/or S plane) while making the length being the exact same?</p>

---

## Post #2 by @pieper (2024-04-10 22:25 UTC)

<p>You might want to use the ImageStacks module in SlicerMorph for that.  You’ll need to know the real pixel and slice spacing.  Another option would be to apply a transform to do the correction and then harden the model before exporting.</p>

---

## Post #3 by @Von (2024-04-11 17:36 UTC)

<p>Hi Steve,</p>
<p>I could not find the modules you were mentioning, but I had permission to disclose more information about what I am trying to do.</p>
<p>Essentially, I am using the software for Non Destructive Testing (NDT) purposes. We are trying to map out the cracks on a equipment by using a Ultrasound Testing (UT) machine, and we are able to extract those data by screenshotting on the scans. The number of screenshots represents the length of the crack in mm.</p>
<p>Next, we would import those screenshots into Slicer3D (typically around 300 to 800 screenshots), and then we would use the Threshold feature in the segment editor to detect the crack indications (typically in a red colour in the screenshot). We would then export the model as a STL file and import it into another CAD software and incorporate the crack indication model into the equipment.</p>
<p>The main problem is is that the model is out of scale. The length matches, but the width and height of the model is around 10 times bigger than the equipment. I tried scaling the 3D model when exporting it but it scales the model uniformly. The width and height matches but the length shrinks as a result.</p>
<p>Let me know if you need more details from me.</p>

---

## Post #4 by @pieper (2024-04-11 17:41 UTC)

<p>That makes sense, thanks for the context.</p>
<p>You need to install the SlicerMorph extension, and then you can use the ImageStacks module as described here: <a href="https://github.com/SlicerMorph/SlicerMorph/tree/master/Docs/ImageStacks" class="inline-onebox">SlicerMorph/Docs/ImageStacks at master · SlicerMorph/SlicerMorph · GitHub</a></p>
<p>In there you can describe the spacings in each dimension.  Let us know if that doesn’t work out.</p>

---
