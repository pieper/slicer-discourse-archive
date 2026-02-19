---
topic_id: 22289
title: "Import Dicomsegmentationplugin Does Not Work In Preview Rele"
date: 2022-03-03
url: https://discourse.slicer.org/t/22289
---

# Import DICOMSegmentationPlugin does not work in preview release

**Topic ID**: 22289
**Date**: 2022-03-03
**URL**: https://discourse.slicer.org/t/import-dicomsegmentationplugin-does-not-work-in-preview-release/22289

---

## Post #1 by @koeglfryderyk (2022-03-03 15:52 UTC)

<p>Slicer version 4.13.0, revision 30670, built 2022-03-03, MacOS</p>
<p><code>import DICOMSegmentationPlugin</code><br>
does not work, gives the following error:</p>
<blockquote>
<p>ModuleNotFoundError: No module named ‘DICOMSegmentationPlugin’</p>
</blockquote>

---

## Post #2 by @pieper (2022-03-03 22:04 UTC)

<p>Usually this means there was an error during module discovery and there should be info in the logs.  It’s probably a python syntax issue.</p>

---

## Post #3 by @koeglfryderyk (2022-03-03 23:09 UTC)

<p>That’s the entire log (there’s only the previously mentioned error there):<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/9/59b4f777d0690094a61fa3186b956adbf4d2ebc7.jpeg" data-download-href="/uploads/short-url/cNAdhig9m84rVGQwLrf5aJGzz1l.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59b4f777d0690094a61fa3186b956adbf4d2ebc7_2_690x228.jpeg" alt="image" data-base62-sha1="cNAdhig9m84rVGQwLrf5aJGzz1l" width="690" height="228" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59b4f777d0690094a61fa3186b956adbf4d2ebc7_2_690x228.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59b4f777d0690094a61fa3186b956adbf4d2ebc7_2_1035x342.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/59b4f777d0690094a61fa3186b956adbf4d2ebc7_2_1380x456.jpeg 2x" data-dominant-color="D9E1EC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2020×670 198 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @pieper (2022-03-03 23:37 UTC)

<p>The error probably happened during module discovery as startup, so higher up the log.</p>

---

## Post #5 by @koeglfryderyk (2022-03-03 23:45 UTC)

<p>That’s the entire log - I don’t see any errors higher up<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5add40fda452c4748a1ee88cfd491116038de348.jpeg" data-download-href="/uploads/short-url/cXP0pg6Sfkdj8hteredpvyIZ11K.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5add40fda452c4748a1ee88cfd491116038de348_2_690x271.jpeg" alt="image" data-base62-sha1="cXP0pg6Sfkdj8hteredpvyIZ11K" width="690" height="271" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5add40fda452c4748a1ee88cfd491116038de348_2_690x271.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5add40fda452c4748a1ee88cfd491116038de348_2_1035x406.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5add40fda452c4748a1ee88cfd491116038de348_2_1380x542.jpeg 2x" data-dominant-color="ECECEC"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×756 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @jamesobutler (2022-03-04 00:04 UTC)

<p>Are you trying to replicate this example?<br>
<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-segmentation-to-dicom-segmentation-object" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#export-a-segmentation-to-dicom-segmentation-object</a></p>
<p>According to this statement in Slicer core, the “DICOMSegmentationPlugin” comes from a Slicer extension. You would need to install Quantitative Reporting before being able to <code>import DICOMSegmentationPlugin</code>.</p><aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/7cef1fff130116376f81882470bd314c22199fdf/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L269-L270">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/7cef1fff130116376f81882470bd314c22199fdf/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L269-L270" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/7cef1fff130116376f81882470bd314c22199fdf/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L269-L270" target="_blank" rel="noopener nofollow ugc">Slicer/Slicer/blob/7cef1fff130116376f81882470bd314c22199fdf/Modules/Scripted/DICOMPlugins/DICOMScalarVolumePlugin.py#L269-L270</a></h4>



    <pre class="onebox"><code class="lang-py">
      <ol class="start lines" start="269" style="counter-reset: li-counter 268 ;">
          <li>if 'DICOMSegmentationPlugin' not in slicer.modules.dicomPlugins:</li>
          <li>  logging.warning('Please install Quantitative Reporting extension to enable loading of DICOM Segmentation objects')</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd7299bb8ec6e597ba09bbf44a229810355558c9.png" data-download-href="/uploads/short-url/Aa6kurJrwJN5N9lQOieGE0J14wN.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd7299bb8ec6e597ba09bbf44a229810355558c9_2_201x375.png" alt="image" data-base62-sha1="Aa6kurJrwJN5N9lQOieGE0J14wN" width="201" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/d/fd7299bb8ec6e597ba09bbf44a229810355558c9_2_201x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd7299bb8ec6e597ba09bbf44a229810355558c9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/d/fd7299bb8ec6e597ba09bbf44a229810355558c9.png 2x" data-dominant-color="EEE9E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">280×520 50.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><a class="mention" href="/u/pieper">@pieper</a> This probably brings up a point that the Script Repository needs to make mentions of any dependent extensions that are required for various examples.</p>

---

## Post #7 by @koeglfryderyk (2022-03-04 00:16 UTC)

<p>Yes, I am!</p>
<p>However, I’m not able to to install this extension.</p>
<p>I’m not sure if I’m doing something wrong, but when I search for it in the Extension Manager nothing is found (in the preview release 2022-03-02, macOS)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f57d0b6dae2729e68b9f42678d7c038b6f846d52.png" data-download-href="/uploads/short-url/z1GT0hBG6i7QeGkdyLXmjrkOMv0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f57d0b6dae2729e68b9f42678d7c038b6f846d52_2_345x174.png" alt="image" data-base62-sha1="z1GT0hBG6i7QeGkdyLXmjrkOMv0" width="345" height="174" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f57d0b6dae2729e68b9f42678d7c038b6f846d52_2_345x174.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f57d0b6dae2729e68b9f42678d7c038b6f846d52_2_517x261.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/5/f57d0b6dae2729e68b9f42678d7c038b6f846d52_2_690x348.png 2x" data-dominant-color="EDF1F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1494×754 57.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>(I can install the extension in the stable Slicer release (4.11.20210226)</p>
<p>Also, shouldn’t I then get the warning ‘Please install Quantitative Reporting extension to enable loading of DICOM Segmentation objects’?</p>

---

## Post #8 by @jamesobutler (2022-03-04 00:23 UTC)

<p>For the latest Slicer Preview, Quantitative Reporting extension is currently only building successfully on Windows which is why it is missing on macOS and Linux.</p>
<p><a href="https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2022-03-03&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=QuantitativeReporting" class="onebox" target="_blank" rel="noopener nofollow ugc">https://slicer.cdash.org/index.php?project=SlicerPreview&amp;date=2022-03-03&amp;filtercount=1&amp;showfilters=1&amp;field1=buildname&amp;compare1=63&amp;value1=QuantitativeReporting</a></p>
<p>That logged warning about the missing DICOMSegmentationPlugin is currently only designed to be logged when using the DICOM module UI and is not currently designed to be logged when attempting to do <code>import DICOMSegmentationPlugin</code> from code.</p>

---
