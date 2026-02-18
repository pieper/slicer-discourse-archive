# Changing default mesh files from VTK to OBJ

**Topic ID**: 1600
**Date**: 2017-12-06
**URL**: https://discourse.slicer.org/t/changing-default-mesh-files-from-vtk-to-obj/1600

---

## Post #1 by @Peter_Simpson-Young (2017-12-06 01:34 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.6.2</p>
<p>Hey guys,</p>
<p>I’m using Slicer to create OBJ models of Freesurfer parcellations, which requires going through each individual region and changing the file type from VTK to OBJ (see image below). Changing all ~250 white matter &amp; grey matter region takes about 30 mins per participant.</p>
<p>Does anyone know a quicker way of doing this? Is it possible to change the default mesh file type from VTK to OBJ? Or to subsequently convert the files? Or can it be done in Freesurfer (by a complete novice like myself)?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/bab5305c871c6cf1701917a3657afd44468dca76.png" data-download-href="/uploads/short-url/qDH0j3m4Fk3N6EebkZ4h6BCXrBI.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/bab5305c871c6cf1701917a3657afd44468dca76_2_690x370.png" alt="image" data-base62-sha1="qDH0j3m4Fk3N6EebkZ4h6BCXrBI" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/bab5305c871c6cf1701917a3657afd44468dca76_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/bab5305c871c6cf1701917a3657afd44468dca76_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/1X/bab5305c871c6cf1701917a3657afd44468dca76_2_1380x740.png 2x" data-dominant-color="D0D0D5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3836×2060 612 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>For context, I’ve been using the OBJ files for renderings in [Keyshot] and for EEG data visualisation projects in Unity &amp; Unreal. (<a href="https://petersimpsonyoung.github.io/Alexei_VR/Alexei_VR.179.html" class="inline-onebox" rel="noopener nofollow ugc">KeyShotVR</a>)</p>
<p>Many thanks,</p>
<p>Peter</p>

---

## Post #2 by @ihnorton (2017-12-06 01:52 UTC)

<p>I have also wanted to batch-apply a change to all nodes of a specific type.</p>
<p>For a quick solution though, are you using Slicer just to do this conversion? If you are loading all the models from a directory and then immediately re-saving as OBJ, then we could provide a simple script do that in batch for all files in a directory.</p>

---

## Post #3 by @lassoan (2017-12-06 02:24 UTC)

<p>You can change default save file format as described here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_default_file_type_for_nodes_.28that_have_never_been_saved_yet.29">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_default_file_type_for_nodes_.28that_have_never_been_saved_yet.29</a></p>
<p>Just below that there is a script that changes file format for existing nodes.</p>

---

## Post #4 by @lassoan (2023-03-21 02:53 UTC)



---
