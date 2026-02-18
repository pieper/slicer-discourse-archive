# Export segmentation as bin file

**Topic ID**: 10970
**Date**: 2020-04-02
**URL**: https://discourse.slicer.org/t/export-segmentation-as-bin-file/10970

---

## Post #1 by @kopachini (2020-04-02 12:34 UTC)

<p>Hello everyone, I hope that you are doing fine in these hard times?</p>
<p>I have a question regarding segmentation export.<br>
Is there any way to export segmentation or even whole study DICOM data without segmentation (CT or MR) as bin (binary) file that could be later on imported in Monte Carlo N Particle Transport Code (MCNP)?</p>
<p>Stay safe and receive my best regards,<br>
Vjekoslav.</p>

---

## Post #2 by @lassoan (2020-04-04 21:10 UTC)

<p>I believe we have a complete set of import/export tools for EGSnrc Monte Carlo engine. I’ve found <a href="https://github.com/SlicerRt/SlicerRT/tree/master/DosxyzNrc3dDoseFileReader">Dosxyz NRC 3D dose file reader in SlicerRT extension</a> but did not find others. <a class="mention" href="/u/cpinter">@cpinter</a> can you give more information on this?</p>
<p>Regardless of this, you can always export the segmentation to a labelmap volume then access voxels as numpy array (<code>slicer.util.arrayFromVolume</code>) and write it to any custom file format using a few lines of Python code.</p>

---

## Post #3 by @kopachini (2020-04-14 07:22 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a>,<br>
Thank you for your reply. I have installed SlicerRT but can’t find the mentioned Dosxyz extension or manuals for the rest of the applications in Radiotherapy section.</p>
<p>Since I am no expert at python and coding, is there another approach to the problem (regarding to second part of your answer)?</p>

---

## Post #4 by @cpinter (2020-04-14 15:33 UTC)

<p>In SlicerRT we indeed support a complete DOSXYZnrc workflow. For example, <a href="https://github.com/SlicerRt/SlicerRT/blob/master/ExternalBeamPlanning/Widgets/Python/OrthovoltageDoseEngine.py#L233">this</a> is the call from python to the ctcreate utility that saves the CT data in a format that DOSXYZ can read. You don’t need to be an expert to understand this code, as a matter of fact, I don’t consider myself a python expert either, although I wrote much of this.</p>
<p>Probably the MCNP toolkit you use has different file formats. If you have the specification, then you should be able to figure out how to read/write the formats it uses. This is how we did it for DOSXYZnrc, although it has <a href="https://nrc-cnrc.github.io/EGSnrc/doc/pirs794-dosxyznrc.pdf">really good documentation</a>.</p>

---

## Post #5 by @kopachini (2020-04-15 05:00 UTC)

<p>Thank you for your reply <a class="mention" href="/u/cpinter">@cpinter</a>. Actually, I don’t know any of coding and since I am in medical filed, this whole thing is really new to me :). I’ll have to find someone who could help me with that.<br>
As I have already made the whole model (stl file), combining two persons DICOM data, and is it possible to run this script on that model? I presume that I have to import it back in Slicer and run it from there?</p>
<p>Regarding specifications for binary file, my collegue imports it in software manually or copy/paste <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20">  (but for whole body it would be too much I think). I have example data that I open in note (it is classical bin data as I’ve been said, as seen in pic). I hope that I could get same thing when import my model in Slicer.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91722a4ed101260e568d10791421e1dc31553648.jpeg" data-download-href="/uploads/short-url/kKFPx0vQQybQmEJfgjTvHMzTbmg.jpeg?dl=1" title="Untitled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91722a4ed101260e568d10791421e1dc31553648_2_467x500.jpeg" alt="Untitled" data-base62-sha1="kKFPx0vQQybQmEJfgjTvHMzTbmg" width="467" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/91722a4ed101260e568d10791421e1dc31553648_2_467x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91722a4ed101260e568d10791421e1dc31553648.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/1/91722a4ed101260e568d10791421e1dc31553648.jpeg 2x" data-dominant-color="ECECEB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled</span><span class="informations">626×670 206 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Best regards, Vjekoslav.</p>

---

## Post #6 by @cpinter (2020-04-15 08:36 UTC)

<p>Reading in this file in Slicer would not be hard it seems. There are many examples for such a reader, like the one <a class="mention" href="/u/lassoan">@lassoan</a> referred to. If you check out the differences between the two file formats and modify the code according to the few differences, then it should be really easy to have a working reader in Slicer.<br>
If either you or a colleague of yours takes on this challenge, we will be happy to help you. Or if you have funding, you can find paid services around here to do such things.</p>
<aside class="quote no-group" data-username="kopachini" data-post="5" data-topic="10970">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/kopachini/48/65543_2.png" class="avatar"> kopachini:</div>
<blockquote>
<p>As I have already made the whole model (stl file), combining two persons DICOM data, and is it possible to run this script on that model? I presume that I have to import it back in Slicer and run it from there?</p>
</blockquote>
</aside>
<p>There are many things I don’t understand in your question. I am not familiar with the MCNP toolkit, its capabilities, or your workflow. If you describe your steps (and the input/output of each step) in detail, then we could give some pointers.</p>

---

## Post #7 by @kopachini (2020-04-15 15:28 UTC)

<p>I segmented neck, thorax, abdomen and pelvis from one person, but didn’t have whole head… Then, I segmented head (brain, skull, eyes) of another person. In 3d modeling software i combined these two and made one whole model of head, neck, thorax, abdomen and pelvis. Is it possible to import that whole body model (stl file) to 3D slicer and then try to export it as binary file that would be then imported in Monte Carlo simulation?</p>

---

## Post #8 by @cpinter (2020-04-16 08:21 UTC)

<p>I suggest against this heterogeneic approach. STL files do not explicitly contain information about the coordinate system, so depending on the method of saving the file in your chosen application, they may appear on top of each other. In either case (appear correctly vs need to manually align) you can convert the STL models easily into 3D volumes (i.e. labelmaps) in the Segmentations module (you can find lots of information about this in the documentation and this forum).</p>
<p>Once you have the labelmap you will need the exporter above so that you have the desired binary file format.</p>

---

## Post #9 by @kopachini (2020-04-16 13:00 UTC)

<p>That is what I thought, import it as labelmap, that shouldn’t be a problem.<br>
The exporter that you mention, is it DOSXYZ? This next steps are confusing to me and that is the main problem <img src="https://emoji.discourse-cdn.com/twitter/confused.png?v=9" title=":confused:" class="emoji" alt=":confused:"></p>

---

## Post #10 by @cpinter (2020-04-16 13:28 UTC)

<p>The exporter I mean is for the MCNP toolkit you use and it does not exist yet, it needs to be created. The DOSXYZ exporter can be a good starting point and serve as a sample. It is a programming task to create this exporter, and it is not hard at all, just read the existing code, and change what is different. Here on this forum we do not offer free programming services, but can help you go along the way.</p>

---

## Post #11 by @kopachini (2020-05-18 16:36 UTC)

<p>Hello guys, it’s me, again <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"><br>
I need help, again.<br>
So, I manage to import stl files of different organs in 3d slicer and when I try to save all of them as segmentation (.nrrd file) message pops up saying “Exception trown in event: Bad allocation”</p>
<p>Few days ago I manage to do same but only with few organ stl files and it worked just fine…<br>
What could be the problem?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/2/72c1e5b9e49cb07e446c461b5ae11a6290005eec.jpeg" data-download-href="/uploads/short-url/gnbQZWTCo2QaBX7cLRshwEhqbJq.jpeg?dl=1" title="error" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72c1e5b9e49cb07e446c461b5ae11a6290005eec_2_690x388.jpeg" alt="error" data-base62-sha1="gnbQZWTCo2QaBX7cLRshwEhqbJq" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72c1e5b9e49cb07e446c461b5ae11a6290005eec_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72c1e5b9e49cb07e446c461b5ae11a6290005eec_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/72c1e5b9e49cb07e446c461b5ae11a6290005eec_2_1380x776.jpeg 2x" data-dominant-color="7A8681"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error</span><span class="informations">1920×1080 302 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Operating system: Windows 10 Home, 64 bit<br>
Intel core i7-7700 2.8GHz<br>
16GB RAM<br>
I am using 4.10.2 version od 3D slicer.</p>

---

## Post #12 by @pieper (2020-05-18 17:08 UTC)

<p>“Bad allocation” means you’ve run out of memory.  Makes sense that it works for small data but not past a certain size.  You should be able to either add real or virtual memory to your computer.</p>
<p>Also you could try the newer Slicer versions, but that may not help in this case.</p>

---

## Post #13 by @kopachini (2020-05-19 11:39 UTC)

<p>As I thought so… Thank you.</p>

---

## Post #14 by @lassoan (2020-06-08 20:53 UTC)

<p>3 posts were split to a new topic: <a href="/t/viewers-do-not-appear-in-openstack/11934">Viewers do not appear in OpenStack</a></p>

---

## Post #17 by @kopachini (2020-06-08 19:55 UTC)

<p>hmmm, when I import all desired organs in slicer 11 and want to save as nrrd file (segmentation) it succeeds, but when I want to perform same process with slicer 10, it says not enough memory (as earlier)… why is that happening when everything is the same regarding computing power?</p>

---

## Post #18 by @lassoan (2020-06-08 21:02 UTC)

<p>Slicer-4.11 is hugely improved compared to Slicer-4.10, including optimized memory management for segmentations. In some cases (when you have hundreds of non-overlapping segments in a segmentation) then memory usage and computation times may be decreased by a factor of 10-100x in Slicer-4.11.</p>

---

## Post #19 by @kopachini (2020-06-09 04:45 UTC)

<p>Thank you for your reply.<br>
I just need to figure out why I can export 11 organ segmentation flawlessly into the third application, but when I have 24 organ segmentation in the same app it appears only as part of the body (part of the abdomen) and magnified.<br>
Not sure, but could it be due to memory again? We should get access to more memory usage in that other computer and will know if that is a cause. <img src="https://emoji.discourse-cdn.com/twitter/crossed_fingers.png?v=9" title=":crossed_fingers:" class="emoji" alt=":crossed_fingers:"> <img src="https://emoji.discourse-cdn.com/twitter/crossed_fingers.png?v=9" title=":crossed_fingers:" class="emoji" alt=":crossed_fingers:"></p>

---

## Post #20 by @lassoan (2020-06-09 05:06 UTC)

<p>It may be because you run out of memory, or it may be due to one of those hundreds of small issues that have been fixed since Slicer-4.10.</p>

---
