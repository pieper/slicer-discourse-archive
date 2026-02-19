---
topic_id: 15850
title: "Features Value Mean And Variance"
date: 2021-02-04
url: https://discourse.slicer.org/t/15850
---

# Features value (mean and variance)

**Topic ID**: 15850
**Date**: 2021-02-04
**URL**: https://discourse.slicer.org/t/features-value-mean-and-variance/15850

---

## Post #1 by @Aleja_Ichina (2021-02-04 21:51 UTC)

<p>Hi,</p>
<p>Sorry, I have a question, why mean value and variance value are big. For example, I’m working with DICOM abdomen images and I segmented these in 3D slicer and I converted to .nrrd but when I apply pyradiomics the mean value is 133. I don’t have idea what is the range and I whan to create an histrogram but I tried it and I failed. Help me please</p>

---

## Post #2 by @JoostJM (2021-03-09 12:25 UTC)

<p>A mean value without any context is meaningless. I cannot say without knowing what you would expect. Also, preprocessing can alter the interpretation of your values (e.g. by applying normalization).<br>
What settings did you use? What structures did you segment? What value would make sense to you for mean?</p>
<p>Range is available, it is one of the firstorder features.</p>

---

## Post #3 by @Aleja_Ichina (2021-03-10 22:52 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9ea66854407cf73d5f83b103fa17eb47daec6c68.jpeg" data-download-href="/uploads/short-url/mDtXWv3lKKd6bZczIbY0I18GsVq.jpeg?dl=1" title="2021-03-08-Scene.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ea66854407cf73d5f83b103fa17eb47daec6c68_2_517x349.jpeg" alt="2021-03-08-Scene.jpg" data-base62-sha1="mDtXWv3lKKd6bZczIbY0I18GsVq" width="517" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ea66854407cf73d5f83b103fa17eb47daec6c68_2_517x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ea66854407cf73d5f83b103fa17eb47daec6c68_2_775x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9ea66854407cf73d5f83b103fa17eb47daec6c68_2_1034x698.jpeg 2x" data-dominant-color="585650"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-03-08-Scene.jpg</span><span class="informations">1331×899 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/1/b121bbd417af9a776b60a014d23be9a45073f005.jpeg" data-download-href="/uploads/short-url/pgYMKUWqeLZG6HCfSVH9sYsdmCx.jpeg?dl=1" title="2021-03-04-Scene.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b121bbd417af9a776b60a014d23be9a45073f005_2_517x349.jpeg" alt="2021-03-04-Scene.jpg" data-base62-sha1="pgYMKUWqeLZG6HCfSVH9sYsdmCx" width="517" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b121bbd417af9a776b60a014d23be9a45073f005_2_517x349.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b121bbd417af9a776b60a014d23be9a45073f005_2_775x523.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b121bbd417af9a776b60a014d23be9a45073f005_2_1034x698.jpeg 2x" data-dominant-color="4B4943"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2021-03-04-Scene.jpg</span><span class="informations">1331×899 173 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hi Joost,</p>
<p>I segmented the liver. The range is available but what happens if I have a different range as the image shows? How can I interpret my data?<br>
I need radiomics features to develop a neural network according to the values of these features. For example, it is a fatty liver if its mean value has a range [-100,150] (this is just a guess.)<br>
I don’t have idea how to normalize my dataset. Could you help me, please? I extracted the mask and the image to apply pyradiomics in nrrd format</p>

---

## Post #4 by @JoostJM (2021-03-22 16:37 UTC)

<p>I’m having difficulty understanding your specific question. If I understand correctly, you want to differentiate between fatty and non-fatty liver? In any case, in radiomics studies you have some outcome label defined per case (e.g. yes/no to fatty liver). You the analyze if features or a combination of features is correlated to your outcome. That way you can make a model that can take the segmented image as input and output a prediction of your outcome for new cases.</p>
<p>In the PyRadiomics documentation at <a href="http://pyradiomics.readthedocs.io">pyradiomics.readthedocs.io</a> you can find how to enable normalization.</p>

---

## Post #5 by @Aleja_Ichina (2021-03-22 16:50 UTC)

<p>Thank you so much, I understand.<br>
I have another question: Why is it important to normalize the data?</p>

---

## Post #6 by @JoostJM (2021-04-12 08:27 UTC)

<p>Normalization strives to remove systematic differences between images that are due to differences in acquisition and therefore represent noise that can suppress any signal in your data.</p>
<p>For example, if 1 scanner stores it’s values with 10x than another scanner, your model will most likely reflect which scanner acquired the image, and not any true differences in texture, etc.<br>
For CT this is generally less of a problem and normalization may be switched off, as the values are linked to an absolute value (Hounsfield Units reflecting density/atomic number of the tissue at that specific voxel). However, MR uses a <em>relative</em> intensity, so the value in itself doesn’t really mean anything, just in relation to other values. Therefore there is no ‘standard’ value to compare against.</p>
<p>Normalization in PyRadiomics is fairly simple, and better methods probably exist, but are outside the scope of the PyRadiomics project. In short, PyRadiomics assumes that your input images reflect more or less the same area in your patients and should therefore have a comparable range of intensity values. This is then enforced to be so by subtracting the mean and dividing by the standard deviation (meaning the mean and standard deviation afterwards will be 0 and 1, respectively, though the latter can be scaled by <code>normalizationScale</code>).<br>
Any differnces between ROIs should be retained as often, the ROI represents just a very small area of the image and should not have a large influence on the overall mean and standard deviation.</p>

---

## Post #7 by @JoostJM (2021-04-12 08:33 UTC)

<p>Be aware that in your case, the ROI actually <em>does</em>  represent a rather large part of the image, and that normalization may also ‘normalize’ some of the differences between your cases (fatty/non-fatty liver). If you are analyzing cases from just 1 scanner, you may consider to not use normalization, as there are likely to be no systematic differences in acquistion within 1 scanner (if also the same acquisition protocol is used).</p>
<p>That said, if you analyze both with and without normalization and the normalized cases function just as good as the non-normalized ones, I’d advise to use normalization as they are more likely to be generalizable to cases acquired using different scanners/acquisition protocols.</p>

---
