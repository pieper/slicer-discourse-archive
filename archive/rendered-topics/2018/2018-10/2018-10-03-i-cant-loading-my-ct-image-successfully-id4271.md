# I can't loading my CT image successfully

**Topic ID**: 4271
**Date**: 2018-10-03
**URL**: https://discourse.slicer.org/t/i-cant-loading-my-ct-image-successfully/4271

---

## Post #1 by @SlicerRookie (2018-10-03 13:43 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 3D slicer 4.9 (nightly)<br>
Expected behavior: No problem!<br>
Actual behavior: The software gives me a error message when using MultiVolumeImporter plugin.</p>
<p>Hello!<br>
I’m a newbie for doing PET-CT researches and using this software to analysis.<br>
When I try to using DICOM module for importing dcm data. The software shows a error message of MultiVolumeImporter.<br>
Can you give me some suggestion to solve this problem?<br>
The pictures of screenshot and python log message as follow:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d0449afc817c02dfe287c52e09f788f6889c63b0.jpeg" data-download-href="/uploads/short-url/tIqiCgFHQ3PrDmxkHmufb7MLeY8.jpeg?dl=1" title="error01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0449afc817c02dfe287c52e09f788f6889c63b0_2_690x460.jpeg" alt="error01" data-base62-sha1="tIqiCgFHQ3PrDmxkHmufb7MLeY8" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0449afc817c02dfe287c52e09f788f6889c63b0_2_690x460.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0449afc817c02dfe287c52e09f788f6889c63b0_2_1035x690.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d0449afc817c02dfe287c52e09f788f6889c63b0_2_1380x920.jpeg 2x" data-dominant-color="EDF1F4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error01</span><span class="informations">3240×2160 407 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/1/c107900631ea11a7828f30f6bb60d5fea8dc2ee6.jpeg" data-download-href="/uploads/short-url/rxClZ0vOankSAxuFUuUAgwyQAfQ.jpeg?dl=1" title="error02" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c107900631ea11a7828f30f6bb60d5fea8dc2ee6_2_690x460.jpeg" alt="error02" data-base62-sha1="rxClZ0vOankSAxuFUuUAgwyQAfQ" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c107900631ea11a7828f30f6bb60d5fea8dc2ee6_2_690x460.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c107900631ea11a7828f30f6bb60d5fea8dc2ee6_2_1035x690.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/c/c107900631ea11a7828f30f6bb60d5fea8dc2ee6_2_1380x920.jpeg 2x" data-dominant-color="EEF3F5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">error02</span><span class="informations">3240×2160 398 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<pre><code>============Message from Python Interactor===================
Python 2.7.13 (default, Sep 27 2018, 23:06:33) [MSC v.1900 64 bit (AMD64)] on win32

&amp;gt;&amp;gt;&amp;gt;

Traceback (most recent call last):

File &amp;quot;C:\Program Files\Slicer 4.9.0-2018-09-27\lib\Slicer-4.9\qt-scripted-modules\DICOMLib\DICOMWidgets.py&amp;quot;, line 737, in getLoadablesFromFileLists

loadablesByPlugin[plugin] = plugin.examine(fileLists)

File &amp;quot;C:/Program Files/Slicer 4.9.0-2018-09-27/bin/../lib/Slicer-4.9/qt-scripted-modules/MultiVolumeImporterPlugin.py&amp;quot;, line 106, in examine

loadables += self.examineFiles(files)

File &amp;quot;C:/Program Files/Slicer 4.9.0-2018-09-27/bin/../lib/Slicer-4.9/qt-scripted-modules/MultiVolumeImporterPlugin.py&amp;quot;, line 493, in examineFiles

mvNodes = self.initMultiVolumes(subseriesLists[key])

File &amp;quot;C:/Program Files/Slicer 4.9.0-2018-09-27/bin/../lib/Slicer-4.9/qt-scripted-modules/MultiVolumeImporterPlugin.py&amp;quot;, line 787, in initMultiVolumes

tagValue = self.tm2ms(tagValueStr) # convert to ms

File &amp;quot;C:/Program Files/Slicer 4.9.0-2018-09-27/bin/../lib/Slicer-4.9/qt-scripted-modules/MultiVolumeImporterPlugin.py&amp;quot;, line 756, in tm2ms

sec = sec+ssfrac

UnboundLocalError: local variable 'sec' referenced before assignment

Warning: Plugin failed: MultiVolumeImporterPlugin

See python console for error message.

DICOM Plugin failed: local variable 'sec' referenced before assignment
</code></pre>

---

## Post #2 by @lassoan (2018-10-03 14:18 UTC)

<p>MultiVolumeImporterPlugin fails because in one of the DICOM files, time string format is invalid. If you are not trying to read a 4D CT then you don’t need MultiVolumeImporterPlugin, so you can ignore the error (you can disable the plugin if you don’t want to see the error message at all).</p>
<p>If you cannot load the CT then most likely it is not valid DICOM. See more details <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/DICOM#When_I_click_on_.22Load_selection_to_slicer.22_I_get_an_error_message_.22Could_not_load_..._as_a_scalar_volume.22">here</a>.</p>

---
