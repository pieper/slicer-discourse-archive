# Importing a tiff sequence

**Topic ID**: 11864
**Date**: 2020-06-04
**URL**: https://discourse.slicer.org/t/importing-a-tiff-sequence/11864

---

## Post #1 by @Deepa (2020-06-04 17:09 UTC)

<p>Hi there</p>
<p>I’ve imported a tiff file that contains a stack of images from <a href="https://ndownloader.figshare.com/files/21660105?private_link=5091cb1b57c1e7cfa112" rel="nofollow noopener">here</a> using<br>
ImageStack &gt; Browse files in Slicer 4.11.</p>
<p>After hitting load, I couldn’t see the images as a stack/view slice by slice in RGY panel and I couldn’t<br>
view the volume too.<br>
Could someone kindly check this import?</p>
<p>Thanks a lot<br>
Deepa</p>

---

## Post #2 by @pieper (2020-06-04 17:31 UTC)

<p>Hi - That’s a multiframe tiff, so probably you can split it into a set individual files using an external tool and then use it with ImageStacks.</p>

---

## Post #3 by @muratmaga (2020-06-04 18:38 UTC)

<aside class="quote no-group" data-username="Deepa" data-post="1" data-topic="11864">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>I’ve imported a tiff file that contains a stack of images from <a href="https://ndownloader.figshare.com/files/21660105?private_link=5091cb1b57c1e7cfa112">here </a> using</p>
</blockquote>
</aside>
<p><code>ImageStacks</code> works best for non-tiff image sequences as those usually require additional steps to make them work as scalar volumes in slicer. I dragged and dropped your sample file in Slicer and in worked just fine. However, I don’t think the image spacing is correct, so might have to edit that manually.</p>

---

## Post #4 by @lassoan (2020-06-05 01:13 UTC)

<p>Yes, multiframe tiff loads fine in recent Slicer versions, but it is better to use a 3D volume file format (DICOM, nrrd, mha, …).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/d/9d14a19bf3b6457bef9bb880c1d4803ea9e2d107.jpeg" data-download-href="/uploads/short-url/mpBaeYBzzjLMbcWu6nNPWSCoDPN.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d14a19bf3b6457bef9bb880c1d4803ea9e2d107_2_690x417.jpeg" alt="image" data-base62-sha1="mpBaeYBzzjLMbcWu6nNPWSCoDPN" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d14a19bf3b6457bef9bb880c1d4803ea9e2d107_2_690x417.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d14a19bf3b6457bef9bb880c1d4803ea9e2d107_2_1035x625.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9d14a19bf3b6457bef9bb880c1d4803ea9e2d107_2_1380x834.jpeg 2x" data-dominant-color="807D80"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1366 624 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #5 by @Deepa (2020-06-05 02:44 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thank you. I  couldn’t obtain the volume similar to what you have obtained. Here’s what I get</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fb33e4eb0dc8957718ba6e6fae29b093b7e8ef9e.jpeg" data-download-href="/uploads/short-url/zQf1JjJhL6mj93db5gA1uDDqU46.jpeg?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fb33e4eb0dc8957718ba6e6fae29b093b7e8ef9e_2_690x378.jpeg" alt="Untitled" data-base62-sha1="zQf1JjJhL6mj93db5gA1uDDqU46" width="690" height="378" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fb33e4eb0dc8957718ba6e6fae29b093b7e8ef9e_2_690x378.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fb33e4eb0dc8957718ba6e6fae29b093b7e8ef9e_2_1035x567.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fb33e4eb0dc8957718ba6e6fae29b093b7e8ef9e_2_1380x756.jpeg 2x" data-dominant-color="5F5F5F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">1913×1049 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I dragged and dropped the multiframe tiff and selected volume in the Description. Next, I have retained the default spacing in Volume rendering.</p>
<p>Could you please suggest if I am missing any step here?</p>

---

## Post #6 by @lassoan (2020-06-05 02:45 UTC)

<p>Check out a few different presets and adjust the “Shift” slider.</p>

---

## Post #7 by @Deepa (2020-06-05 04:44 UTC)

<p>Thank you. The vessels are visible when “Shift” slider is adjusted. I’d like to know if there are alternate ways to do this. The problem here is while I adjust “Shift” I don’t know the right value at which slider should be stopped and some fraction vessel might be visble/not visible depending on the position at which the slider is stopped.</p>

---

## Post #8 by @rkikinis (2020-06-05 12:02 UTC)

<p>Hi,<br>
the shift slider shifts the transfer function for volume rendering. If you open the “advanced” section visible on your screen shot, you will see the actual transfer function which is being shifted. The control points in the transfer function come with numbers.</p>

---

## Post #9 by @lassoan (2020-06-05 16:41 UTC)

<aside class="quote no-group" data-username="Deepa" data-post="7" data-topic="11864">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>The problem here is while I adjust “Shift” I don’t know the right value at which slider should be stopped and some fraction vessel might be visble/not visible depending on the position at which the slider is stopped</p>
</blockquote>
</aside>
<p>There is no “correct” value, you need to make this decision based on your best judgement and you may even need to edit the transfer functions as <a class="mention" href="/u/rkikinis">@rkikinis</a> suggested above. Moreover, this is only visualization. Segmentation is even harder, as you need to make a binary decision about each voxel (and you cannot blur things as during volume rendering).</p>

---

## Post #10 by @Deepa (2020-07-02 17:37 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Thank you. I’d like to perform segmentation for centerline extraction.<br>
In the documentation available in the <a href="https://github.com/BenKingston/Islet_analysis_Vlahos" rel="noopener nofollow ugc">repository</a> associated with the above-mentioned input, it is described that ilastik has been used for image segmentation.</p>
<blockquote>
<p>The pixel classication tool was trained for at least 30 mins using all 37 default image filters with each of the pre-processed nuclei and blood vessel images. Once satisfactory performance was seen for the binary segmentation of each of the nuclei and blood vessel channels this segmentation was batch applied to other images aquired from the same tissue and animal. The output is a labelled, segmented images of the nuclei and blood vessel channels as multipage tiff files.</p>
</blockquote>
<p>I would like to know if it is possible to do the above in Slicer.</p>

---

## Post #11 by @lassoan (2020-07-02 19:52 UTC)

<p>I haven’t heard about Ilastik until now, but it seems to be a nice tool for segmenting cells in 2D microscopy images. If your task is 2D microscopy image segmentation then it may be a good idea to use it.</p>
<p>If you don’t segment cells or if you want to segment 3D images then probably Slicer’s Segment Editor is a better choice.</p>

---

## Post #12 by @Deepa (2020-07-06 05:44 UTC)

<p>Thank you very much for your response.</p>
<aside class="quote no-group" data-username="Deepa" data-post="10" data-topic="11864">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/deepa/48/5634_2.png" class="avatar"> Deepa:</div>
<blockquote>
<p>The pixel classication tool was trained for at least 30 mins using all 37 default image filters with each of the pre-processed nuclei and blood vessel images.</p>
</blockquote>
</aside>
<p>From what has been documented in the above-mentioned repository, blood vessel images were also subject to segmentation in Ilastik. I’m not sure if this has been done for retaining only the blood vessels during volume rendering of datasets like the following<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d82f122eb05a59dd882eba21065546bd577a128.jpeg" alt="image" data-base62-sha1="b3Hj2f4IImpyGPY5oimM7hU7oIU" width="345" height="208"> .<br>
I’m not sure how to do this in Slicer because I find some tissue mass (in addition to the blood vessel volume) in the Volume displayed in the snapshot.</p>
<p>The repository link that I shared above has used Ilastik to carry out segmentation on the volume seen in the snapshot.</p>

---
