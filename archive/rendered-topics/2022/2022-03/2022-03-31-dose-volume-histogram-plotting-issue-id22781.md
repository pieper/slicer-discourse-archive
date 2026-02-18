# Dose Volume Histogram Plotting issue

**Topic ID**: 22781
**Date**: 2022-03-31
**URL**: https://discourse.slicer.org/t/dose-volume-histogram-plotting-issue/22781

---

## Post #1 by @Js165 (2022-03-31 16:43 UTC)

<p>Hi,<br>
I am trying to plot a dose-volume histogram (DVH) graph using SlicerRT. I have a segmentation file in NIFTI format and a dose file in DICOM format. I am uploading the segmentation file as “segmentation” and the dose file as “volume”. Dose Volume Histogram of Radiotherapy extension can detect segmentation file but can’t recognize dose file [image attached]. Could you please help me with what I am missing? Do I need to convert the segmentation file to label map or RTstruct format?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a45a67052596969655e7c97c1a341de4e8a5f297.png" data-download-href="/uploads/short-url/nrVZt8k3MysTYd5cyq4vkxTfIzl.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a45a67052596969655e7c97c1a341de4e8a5f297_2_690x366.png" alt="1" data-base62-sha1="nrVZt8k3MysTYd5cyq4vkxTfIzl" width="690" height="366" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a45a67052596969655e7c97c1a341de4e8a5f297_2_690x366.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/4/a45a67052596969655e7c97c1a341de4e8a5f297_2_1035x549.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/4/a45a67052596969655e7c97c1a341de4e8a5f297.png 2x" data-dominant-color="ABACA9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1296×689 76.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65ffaa5a1dc8abe1e555628bf2bae47b172af28f.png" data-download-href="/uploads/short-url/eyjZ5495CDmku7pzi98BaNc3d7x.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65ffaa5a1dc8abe1e555628bf2bae47b172af28f_2_689x376.png" alt="2" data-base62-sha1="eyjZ5495CDmku7pzi98BaNc3d7x" width="689" height="376" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65ffaa5a1dc8abe1e555628bf2bae47b172af28f_2_689x376.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/5/65ffaa5a1dc8abe1e555628bf2bae47b172af28f_2_1033x564.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65ffaa5a1dc8abe1e555628bf2bae47b172af28f.png 2x" data-dominant-color="B8B9B7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1299×709 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2022-03-31 16:52 UTC)

<p>You can either uncheck “Show dose volumes only” to show all volume nodes in the Dose volume selector, or you can right-click on the volume node in the subject hierarchy, and click “Convert to RT dose volume…”.</p>

---

## Post #3 by @Js165 (2022-03-31 16:54 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> Thanks a lot! Issue solved.</p>

---

## Post #4 by @Js165 (2022-03-31 17:16 UTC)

<p>The DVH graph I generated shows Fractional Volume vs Intensity [attached Image]. Is it possible to get  Fractional Volume vs Dose [Gy]? I’m not sure if there is any relation between Intensity and Dose [Gy].<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/6/c6369c63c26550893dde121659ad86b7f4caf27d.png" alt="3" data-base62-sha1="shtxDcAt8Z3HwHExf1UNkIysvIp" width="644" height="466"></p>

---

## Post #5 by @Sunderlandkyl (2022-03-31 17:54 UTC)

<p>Yeah, converting the volume using “Convert to RT dose volume…” will allow you to change the units to Gy. You may have to scale the values as well.</p>

---

## Post #6 by @Js165 (2022-03-31 18:08 UTC)

<p>Thanks a lot for your response! I am getting this error “The volume must be under a study in order to be converted to dose. Please drag&amp;drop the volume under a study. If there is no study, it can be created under a subject. Consult the help window for more details.” Attached Image for your reference.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41295954a8e167fa3dde42d761b451c28fc77027.png" data-download-href="/uploads/short-url/9irCLCy55jwbZXm2FvCKKXOhAAD.png?dl=1" title="4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41295954a8e167fa3dde42d761b451c28fc77027_2_690x424.png" alt="4" data-base62-sha1="9irCLCy55jwbZXm2FvCKKXOhAAD" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/1/41295954a8e167fa3dde42d761b451c28fc77027_2_690x424.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41295954a8e167fa3dde42d761b451c28fc77027.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/1/41295954a8e167fa3dde42d761b451c28fc77027.png 2x" data-dominant-color="B8BABB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">4</span><span class="informations">746×459 67.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #7 by @Sunderlandkyl (2022-03-31 18:19 UTC)

<p>To create a subject+study, just right-click in an empty area in the subject hierarchy, then click “Create new subject”, right-click on the subject and click “Create child study”. Then you can drag the dose volume onto the study.</p>

---

## Post #8 by @Js165 (2022-03-31 18:38 UTC)

<p>Thanks a lot! You solved my issues. I have two more questions. How can I change the color of each graph, and how can I limit the X and Y axis value?</p>

---

## Post #9 by @Js165 (2022-03-31 19:10 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a>  got one solution, i.e., “Export DVH to File”. Not sure if there is any other option available or not. Btw, thanks a lot!</p>

---

## Post #10 by @Sunderlandkyl (2022-03-31 20:24 UTC)

<p>You can change the properties of the graph from the “Charts” module. The  X and Y axis limits are in the Charts tab, and the color of each line is in the Series tab.</p>

---

## Post #11 by @Js165 (2022-03-31 23:07 UTC)

<p>Thanks, <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> ! Just in case anyone needs help in plot modification, follow this step. <strong>Go to “Informatics”, then select “Plots”. It contains two tabs “Charts” and “Series”.</strong> Now change whatever you want.</p>

---
