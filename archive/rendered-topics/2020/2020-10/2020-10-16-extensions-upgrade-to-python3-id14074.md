# Extensions upgrade to Python3

**Topic ID**: 14074
**Date**: 2020-10-16
**URL**: https://discourse.slicer.org/t/extensions-upgrade-to-python3/14074

---

## Post #1 by @Frederic (2020-10-16 09:23 UTC)

<p>Hi all,</p>
<p>Our extension (<a href="https://github.com/FredericBr/SlicerGeodesic" rel="noopener nofollow ugc">GeodesicSlicer</a>) does not work in the last version of Slicer (4.11.20200903) because it needs to be ported for python3. I have to do that in a couple of days (or may I have to wait the Slicer5?).<br>
But even if I upgraded it for Python 3, is it possible to keep a version compatible with the previous version of Slicer (and thus Python2, if yes, how to do that)?</p>
<p>Thanks,</p>
<p>Frederic</p>

---

## Post #2 by @lassoan (2020-10-16 14:42 UTC)

<p>What seems to work best for most extensions is to create a separate branch for each Slicer major.minor release:</p>
<ul>
<li>create a <code>4.10</code> branch from your current master (if you want to make further fixes or improvements in this version, you can do that in this branch)</li>
<li>update your s4ext file for SLicer-4.10 to use this branch (in <a href="https://github.com/Slicer/ExtensionsIndex/blob/4.10/GeodesicSlicer.s4ext">https://github.com/Slicer/ExtensionsIndex/blob/4.10/GeodesicSlicer.s4ext</a>, change <code>master</code> to <code>4.10</code>)</li>
<li>make all the necessary changes <code>master</code> branch to make your extension work in the current Slicer version</li>
</ul>
<p>See for example how it is done for MarkupsToModels:</p>
<ul>
<li><a href="https://github.com/SlicerIGT/SlicerMarkupsToModel/branches">https://github.com/SlicerIGT/SlicerMarkupsToModel/branches</a></li>
<li><a href="https://github.com/Slicer/ExtensionsIndex/blob/4.10/MarkupsToModel.s4ext#L10">https://github.com/Slicer/ExtensionsIndex/blob/4.10/MarkupsToModel.s4ext#L10</a></li>
</ul>

---

## Post #3 by @jcfr (2020-10-16 14:46 UTC)

<p>Looking at the migration guide may also be helpful. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide#Python_2_to_Python_3">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MigrationGuide#Python_2_to_Python_3</a></p>

---

## Post #4 by @Frederic (2020-10-21 13:42 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> and <a class="mention" href="/u/jcfr">@jcfr</a> for your valuable comments.</p>
<p>The first step is done, Now I have to make the changes to work with Python 3.</p>
<p>Best.</p>

---

## Post #5 by @Frederic (2020-10-22 14:10 UTC)

<p>I allow myself another question, if you want I can create another post.</p>
<p>When I use your script <a class="mention" href="/u/lassoan">@lassoan</a> ( <a href="https://gist.github.com/lassoan/1673b25d8e7913cbc245b4f09ed853f9#file-extractskin-py" rel="noopener nofollow ugc"> <strong>ExtractSkin.py</strong> </a>, I obtain the wrong orientation (cf. pic where the yellow nose is normally in anterior) of my model.</p>
<p>Do you now why?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/a/aaaf44bd62bef623ab7aff2ac03de1461a4b8d0f.png" data-download-href="/uploads/short-url/olWGdUiel37L32QAUFegO0h3hKL.png?dl=1" title="Sans titre" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaaf44bd62bef623ab7aff2ac03de1461a4b8d0f_2_690x136.png" alt="Sans titre" data-base62-sha1="olWGdUiel37L32QAUFegO0h3hKL" width="690" height="136" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaaf44bd62bef623ab7aff2ac03de1461a4b8d0f_2_690x136.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaaf44bd62bef623ab7aff2ac03de1461a4b8d0f_2_1035x204.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/a/aaaf44bd62bef623ab7aff2ac03de1461a4b8d0f_2_1380x272.png 2x" data-dominant-color="474744"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sans titre</span><span class="informations">1879×373 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks.</p>

---

## Post #6 by @Frederic (2020-10-23 14:24 UTC)

<p>I got it. It was a <a href="https://discourse.slicer.org/t/ras-to-lps-origin-shift/7075">coordinate problem</a>.<br>
For the next one with the same issue, you just have to place this code (here in python) when you create you object.stl:</p>
<p><code>writer.SetHeader("Name of the output. SPACE=RAS")</code></p>
<p><a href="https://github.com/FredericBr/SlicerGeodesic" rel="noopener nofollow ugc">GeodesicSlicer</a> is now ready for Slicer 4.11!</p>

---

## Post #7 by @lassoan (2020-10-25 01:58 UTC)

<p>Thanks for the update. I’ve updated the example script to export the mesh in a simpler way, by calling:</p>
<pre><code class="lang-python">slicer.vtkSlicerSegmentationsModuleLogic.ExportSegmentsClosedSurfaceRepresentationToFiles(
  "c:/tmp", segmentationNode, None, "STL")
</code></pre>

---
