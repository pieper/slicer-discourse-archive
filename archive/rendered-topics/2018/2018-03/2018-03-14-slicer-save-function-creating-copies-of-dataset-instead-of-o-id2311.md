# Slicer save function creating copies of dataset instead of overwrite

**Topic ID**: 2311
**Date**: 2018-03-14
**URL**: https://discourse.slicer.org/t/slicer-save-function-creating-copies-of-dataset-instead-of-overwrite/2311

---

## Post #1 by @drusmanbashir (2018-03-14 11:39 UTC)

<p>Hi,<br>
I am not sure if this is how it is supposed to work. But when i load the data folder i saved previously, slicer creates copies of all files and assigns them a suffix like ‘_1’ . If I were to save the data again after updating a few segmentations for example, everything gets saved along with suffixed duplicates, hence doubling storage and creating confusion, unless i manually unselect the suffixed duplicates.</p>
<p>Screenshot showing contents of folder loaded into slicer, there are no duplicates originally:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/304aefa3c0ab7307e832eb27af15c65034ff7d6e.jpeg" data-download-href="/uploads/short-url/6Tdt2Bo97SfTMNAE4LewqGZ8HJc.JPG?dl=1" title="loaded_folder" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/304aefa3c0ab7307e832eb27af15c65034ff7d6e_2_690x421.JPG" alt="loaded_folder" data-base62-sha1="6Tdt2Bo97SfTMNAE4LewqGZ8HJc" width="690" height="421" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/304aefa3c0ab7307e832eb27af15c65034ff7d6e_2_690x421.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/304aefa3c0ab7307e832eb27af15c65034ff7d6e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/0/304aefa3c0ab7307e832eb27af15c65034ff7d6e.jpeg 2x" data-dominant-color="EDECEB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">loaded_folder</span><span class="informations">925×565 99 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>After loading the folder above, slicer creates copies of everything and suffixes them (so that if I were to save everything again, there will be duplicates):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df4284cfb0af4bce9ea6f81e5abb70f4b70eee55.jpeg" data-download-href="/uploads/short-url/vR2Zumnh6MdmVqW8sqCk4G1jw6F.JPG?dl=1" title="slicer_copying" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df4284cfb0af4bce9ea6f81e5abb70f4b70eee55_2_645x500.JPG" alt="slicer_copying" data-base62-sha1="vR2Zumnh6MdmVqW8sqCk4G1jw6F" width="645" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/df4284cfb0af4bce9ea6f81e5abb70f4b70eee55_2_645x500.JPG, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df4284cfb0af4bce9ea6f81e5abb70f4b70eee55.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/f/df4284cfb0af4bce9ea6f81e5abb70f4b70eee55.jpeg 2x" data-dominant-color="EAEDEF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_copying</span><span class="informations">662×513 64.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Usman</p>

---

## Post #2 by @ihnorton (2018-03-14 12:50 UTC)

<p>One way this could happen is if you use <code>Add Data</code> to load a MRML into Slicer twice (e.g. running Slicer instance where the MRML file was already open). Then the _1 suffix is added in Slicer for each node, and when you go to save then Slicer saves two copies. If this is the problem, then make sure to use <code>File-&gt;Close Scene</code> before loading a MRML file.</p>

---
