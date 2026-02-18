# Slicer 3D MPR-able DICOM Modalities

**Topic ID**: 17260
**Date**: 2021-04-22
**URL**: https://discourse.slicer.org/t/slicer-3d-mpr-able-dicom-modalities/17260

---

## Post #1 by @spycolyf (2021-04-22 22:57 UTC)

<p>What is the minimum number of multi-frame series frames or single-frame series images reasonable for performing Slicer 3D Multi-Planar Reconstruction?</p>
<p>Which modalities will Slicer MPR process other than CT, MR, PT, or NM?</p>
<p>I’m launching Slicer MPR from another app, specifying the DICOM series folder in the Python command. How do I filter the types of DICOM series sent to Slicer? Will modality and number of frames be enough?</p>
<pre><code>	if (Number of frames &gt; 3) &amp;&amp; (modality =  CT, MR, PT, or NM)
	{
		then enable the Slicer MPR extension menu item selection in the image right mouse menu.;
	}
</code></pre>
<p>Is this correct?</p>

---

## Post #2 by @pieper (2021-04-23 21:17 UTC)

<p>Slicer treats even a single frame as a volume, so there’s not specific cutoff but looking at fewer than 3 probably doesn’t make sense.</p>
<p>Slicer can also handle other volumetric modalities, like US or OCT.  But for all modalities it’s more complex than just is it CT or not, since they CT may be a cine acquired without moving the table, so the frames are like frames of a movie and not slices of a volume.  Slicer tries to sort these things out when loading and usually that works for a lot of scans, but sometimes manual intervention is required.</p>

---

## Post #3 by @jcfr (2021-04-23 21:25 UTC)

<p>May also be worth reviewing support for specific modalities provided by extensions: <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/DICOM/DICOMExtensions.json">Modules/Scripted/DICOM/DICOMExtensions.json</a></p>

---

## Post #4 by @spycolyf (2021-05-07 17:27 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>OK, I still a little confused. Are you saying that I should put no filters on types of images the users are allow to process with MPR? I don’t want MPR to crash or malfunction. Remember, I’ve got 30K plus users and I don’t want a lot of confusion and generation of support tickets. I would imaging if it’s not slice-based, don’t allow MPR viewing. But, how can I tell?</p>
<p>Thanks</p>

---

## Post #5 by @lassoan (2021-05-07 18:09 UTC)

<aside class="quote no-group" data-username="spycolyf" data-post="4" data-topic="17260">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/f17d59/48.png" class="avatar"> spycolyf:</div>
<blockquote>
<p>I would imaging if it’s not slice-based, don’t allow MPR viewing. But, how can I tell?</p>
</blockquote>
</aside>
<p>In short, you cannot tell. I would consider this one of the big failures of DICOM. It is not really the fault of the standard but you can blame the imaging vendors, who failed to adopt enhanced DICOM information objects.</p>
<p>The best you can do is to guess when it comes to interpreting series in a DICOM study. A 2D, 2D+t, 3D, 3D+t series are stored exactly the same way and you need to inspect dozens of DICOM fields (many of those are private fields) to decide what is the most likely interpretation. Most of the times there is a quite clear winner among potential interpretations, but not always. For example, if your slices are acquired at a few different time points and number of slices at each time point are not the same then how would you know if you should group all slices into one 3D volume or it makes more sense to present it as a 3D+t time series? If a slice is missing how would you know if that slice was not acquired (to reduce patient dose) or just lost somewhere along network transfer? If a single slice is missing it might be more likely that the slice was lost and you can replace it by interpolating the two neighbor slices. However, if 10 are missing then it could just as well mean that the image was acquired with varying spacing between slices, or that the series is severely corrupted and should be discarded.</p>
<p>You can make better guesses if you develop an application for a specific purpose. For example, if you develop a structural heart intervention planning software then you may decide to interpret all input images as 4D cardiac CTs and ignore/reject anything else, and you can implement specific hacks for each known mistake made by imaging system or software vendors. But there is no definitive solution for general-purpose viewers, other than making guesses and allow users to choose an alternative interpretation if the default does not look good.</p>
<p>In Slicer, we run through each DICOM study through a set of plugins, each of those plugins tries to fit a number of different interpretation rules and returns all the possible interpretations with an associated confidence value. By default, we load the interpretation with the highest confidence value, but the user can enable advanced option and load the data using another interpretation. You could duplicate this logic in the QREADS application, but this logic is quite complex and constantly evolving (as imaging vendors come up with new software versions, imaging protocols, etc. and users are discovering issues in them).</p>

---
