# Slicerfreesurfer in slicer5.0 not present

**Topic ID**: 24621
**Date**: 2022-08-03
**URL**: https://discourse.slicer.org/t/slicerfreesurfer-in-slicer5-0-not-present/24621

---

## Post #1 by @mosenco (2022-08-03 15:33 UTC)

<p>i have some file with extension <code>.pial</code> or <code>.white</code> made in freesurfer that works fine in slicer4.6.<br>
But when i try to load the data with add file i got an error <code>Could not find a suitable storage node for file</code>.</p>
<p>I tried to search up on the forum and found this one <a href="https://github.com/PerkLab/SlicerFreeSurfer/wiki/Using-FreeSurfer-Importer" rel="noopener nofollow ugc">https://github.com/PerkLab/SlicerFreeSurfer/wiki/Using-FreeSurfer-Importer</a> which i see that load <code>.pial</code> files like i wanted or the manual import one, that when i drag and drop, i have to choose in the description “FreeSurfer model”.</p>
<p>But i can only choose model or volume description and there is not freesurferimporter modules in slicer and from that github page for freesurfer importer i cannot load the modules</p>

---

## Post #2 by @Sunderlandkyl (2022-08-03 15:46 UTC)

<p>In 3D Slicer 5.0, you need to install the SlicerFreeSurfer extension from the extension manager.</p>
<p>Click on the extension manager icon:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/b/cbc3d018bcee3275468491f32d47c1235318191e.png" alt="image" data-base62-sha1="t4As7QZXLZukmpozzdCJAevt8xU" width="43" height="31"></p>
<ol>
<li>Click “Install Extensions”.</li>
<li>Search for “SlicerFreeSurfer”</li>
<li>Install</li>
<li>Restart 3D Slicer</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4b7980b6e8509260bb1d0c68cf36e3c399ed1d9.png" data-download-href="/uploads/short-url/pMHi9IjrKBxIC68LzZbJop0qi49.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4b7980b6e8509260bb1d0c68cf36e3c399ed1d9_2_551x499.png" alt="image" data-base62-sha1="pMHi9IjrKBxIC68LzZbJop0qi49" width="551" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/4/b4b7980b6e8509260bb1d0c68cf36e3c399ed1d9_2_551x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4b7980b6e8509260bb1d0c68cf36e3c399ed1d9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/4/b4b7980b6e8509260bb1d0c68cf36e3c399ed1d9.png 2x" data-dominant-color="EDEEF2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">820×744 89.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html" rel="noopener nofollow ugc">Extensions Manager — 3D Slicer documentation</a></p>

---
