# Segmenting in Photoshop?

**Topic ID**: 9462
**Date**: 2019-12-10
**URL**: https://discourse.slicer.org/t/segmenting-in-photoshop/9462

---

## Post #1 by @NoobForSlicer (2019-12-10 14:13 UTC)

<p>I was wondering…<br>
Is there some way to segment stuff in photoshop with slightly different shades of grey or some other color, and then just import those painted images into slicer and make slicer differentiate each and every single one of them because they all have unique shades of grey and hue colors?</p>
<p>So what do you guys thing?</p>
<p>Let’s say, structure 1, color red, structure 2, color light red, structure 3 extremely light red structure 4 grey, structure 5 dark grey structure 6 extremely dark grey structure 7 blue structure 8 light blue bla bla bla and so on and on…</p>
<p>Basically, to paint stuff in photoshop using magic brush and import it to slicer?</p>
<p>In any case, structyre by structure could be imported painter all dark, but it would be a lot of manual work to be honest.</p>

---

## Post #2 by @lassoan (2019-12-10 14:28 UTC)

<p>Photoshop is great but it is not suitable for segmenting medical images. If you write more about your segmentation task then we can give you tips how to accomplish them.</p>

---

## Post #3 by @NoobForSlicer (2019-12-11 01:18 UTC)

<p>so I am not segmenting medical images…</p>
<p>I am segmenting scans of some plastic structures. Those structures were made through some industrial product and inside of them they have like shapes. Those shapes are just like organs in a body.</p>
<p>The plastic or silicone is transparent and you can see those colored artistic structures inside of it.</p>
<p>So to segment those structures, we took one sample and sliced it up.</p>
<p>took photos of slices and now we have slices in png and we have obviously color in those scans.</p>
<p>So segmenting with photoshop here is really easy to be honest… since photoshop can distinguish colors very well.</p>
<p>So using photoshop, I wonder how should we prepare the images so that when we import them to slicer, slicer can easily give us ability to diferentiate between different objects we segmented.</p>

---

## Post #4 by @Hamburgerfinger (2019-12-11 01:56 UTC)

<p>There are surely easier ways to do this, but if you really wanted to do it this way, you might just use shades of gray for the different structures, export from photoshop as *.png for example, then import the png(s) into slicer, then convert your image/image<br>
stack to a scalar volume with the ‘vector to scalar volume’ module, and then you’d be able to get each as segments using thresholding (and then convert to models or whatever else you want to do).</p>

---

## Post #5 by @lassoan (2019-12-11 02:32 UTC)

<p>For segmenting photographed slices, first you need to align the slices. For this, I would recommend to use ImageJ, which can import a stack of color images and automatically align them. You can then export the aligned stack as 3D metaimage, nrrd, or nifti image.</p>
<p>You can then load this 3D image into Slicer for segmentation and convert to scalar using “Vector to scalar volume” as <a class="mention" href="/u/hamburgerfinger">@Hamburgerfinger</a> described above. Most probably you can segment the entire volume in about 2 minutes using “Grow from seeds” effect in Segment editor.</p>

---

## Post #6 by @NoobForSlicer (2019-12-11 04:34 UTC)

<p>This is definitely insightful…</p>
<p>the images are already aligned since the sample was designed for us to segment it and one of the structures are 3 simple vertical lines…</p>
<p>we have aligned this line which looks like a circle in a crossection tbh… a small circle. By aligning these three,  in every scan, what was left inbetween was inevitably aligned as well.</p>
<p>It is amazing how much 3D slicer has applications in industrial designs and artistic works as well.</p>
<p>I definitely have worked with multiple clients, some university people, organic medical stuff and some of them just like this, completely different set of clients.</p>
<p>Amazing 3D slicer is really amazing…</p>

---
