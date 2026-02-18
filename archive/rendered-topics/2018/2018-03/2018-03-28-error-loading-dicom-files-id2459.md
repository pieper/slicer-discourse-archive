# Error loading Dicom Files

**Topic ID**: 2459
**Date**: 2018-03-28
**URL**: https://discourse.slicer.org/t/error-loading-dicom-files/2459

---

## Post #1 by @cedric_pereira (2018-03-28 16:03 UTC)

<p>Hello.</p>
<p>I’m trying to load some Dicom files but I have got this error: “Could not load: 2: MPRAGE_p2_1mm_iso as a Scalar Volume”</p>
<p>I have tried with the advanced option “DICOMScalarVolumePlugin” disabled, but I got the same.<br>
I’m using the last version of Nightly Build.</p>
<p>If you want to try my files: <a href="http://dropbox" rel="nofollow noopener">https://www.dropbox.com/sh/tn7i6v93hvddyf9/AAC0A-XK3h_snKJICt-KG7lma?dl=0</a></p>
<p>Can you help me?<br>
Thank you <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<pre><code>The report:
-----------------------------------------------------------------------
[DEBUG][Qt] 28.03.2018 16:42:57 [] (unknown:0) - Session start time .......: 2018-03-28 16:42:57
[DEBUG][Qt] 28.03.2018 16:42:57 [] (unknown:0) - Slicer version ...........: 4.9.0-2018-03-27 (revision 27110) win-amd64 - installed
[DEBUG][Qt] 28.03.2018 16:42:57 [] (unknown:0) - Operating system .........: Windows /  Professional /  (Build 9200) - 64-bit
[DEBUG][Qt] 28.03.2018 16:42:57 [] (unknown:0) - Memory ...................: 12176 MB physical, 14608 MB virtual
[DEBUG][Qt] 28.03.2018 16:42:57 [] (unknown:0) - CPU ......................: GenuineIntel , 8 cores, 8 logical processors
[DEBUG][Qt] 28.03.2018 16:42:57 [] (unknown:0) - Developer mode enabled ...: no
[DEBUG][Qt] 28.03.2018 16:42:57 [] (unknown:0) - Prefer executable CLI ....: yes
[DEBUG][Qt] 28.03.2018 16:42:57 [] (unknown:0) - Additional module paths ..: (none)
[DEBUG][Python] 28.03.2018 16:42:58 [Python] (C:\Program Files\Slicer 4.9.0-2018-03-27\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
[DEBUG][Python] 28.03.2018 16:42:58 [Python] (C:\Program Files\Slicer 4.9.0-2018-03-27\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(%s, cwd=%s, universal_newlines=%s, shell=%s)
[WARNING][Qt] 28.03.2018 16:42:58 [] (unknown:0) - libpng warning: iCCP: known incorrect sRGB profile
[DEBUG][Python] 28.03.2018 16:42:59 [Python] (C:\Program Files\Slicer 4.9.0-2018-03-27\lib\Slicer-4.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations
[DEBUG][Python] 28.03.2018 16:42:59 [Python] (C:\Program Files\Slicer 4.9.0-2018-03-27\lib\Slicer-4.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor
[DEBUG][Python] 28.03.2018 16:42:59 [Python] (C:\Program Files\Slicer 4.9.0-2018-03-27\lib\Slicer-4.9\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics
[DEBUG][Qt] 28.03.2018 16:42:59 [] (unknown:0) - Switch to module:  "Welcome"
[DEBUG][Qt] 28.03.2018 16:43:03 [] (unknown:0) - Switch to module:  "DICOM"
[DEBUG][Qt] 28.03.2018 16:43:16 [] (unknown:0) - New patient inserted: 10
[DEBUG][Qt] 28.03.2018 16:43:16 [] (unknown:0) - New patient inserted as :  10
[DEBUG][Qt] 28.03.2018 16:43:16 [] (unknown:0) - Need to insert new study:  "1.3.6.1.4.1.22619.2.1.201803191600345270209"
[DEBUG][Qt] 28.03.2018 16:43:16 [] (unknown:0) - Study Added
[DEBUG][Qt] 28.03.2018 16:43:16 [] (unknown:0) - Need to insert new series:  "1.3.12.2.1107.5.2.32.35377.2018031916065999260209821.0.0.0"
[DEBUG][Qt] 28.03.2018 16:43:16 [] (unknown:0) - Series Added
[DEBUG][Qt] 28.03.2018 16:43:18 [] (unknown:0) - "DICOM indexer has successfully processed 176 files [1.16s]"
[INFO][Python] 28.03.2018 16:43:18 [Python] (C:\Program Files\Slicer 4.9.0-2018-03-27\lib\Slicer-4.9\qt-scripted-modules\DICOMLib\DICOMWidgets.py:460) - Imported a DICOM directory, checking for extensions
[INFO][Stream] 28.03.2018 16:43:18 [] (unknown:0) - C:/Users/Cédric Pereira/Desktop/39490000/93827208C:/Users/Cédric Pereira/Desktop/39490000/93827224C:/Users/Cédric Pereira/Desktop/39490000/93827240C:/Users/Cédric Pereira/Desktop/39490000/93827256C:/Users/Cédric Pereira/Desktop/39490000/93827272C:/Users/Cédric Pereira/Desktop/39490000/93827288C:/Users/Cédric Pereira/Desktop/39490000/93827304C:/Users/Cédric Pereira/Desktop/39490000/93827320C:/Users/Cédric Pereira/Desktop/39490000/93827336C:/Users/Cédric Pereira/Desktop/39490000/93827352C:/Users/Cédric Pereira/Desktop/39490000/93827368C:/Users/Cédric Pereira/Desktop/39490000/93827384C:/Users/Cédric Pereira/Desktop/39490000/93827400C:/Users/Cédric Pereira/Desktop/39490000/93827416C:/Users/Cédric Pereira/Desktop/39490000/93827432C:/Users/Cédric Pereira/Desktop/39490000/93827448C:/Users/Cédric Pereira/Desktop/39490000/93842848C:/Users/Cédric Pereira/Desktop/39490000/93842864C:/Users/Cédric Pereira/Desktop/39490000/93842880C:/Users/Cédric Pereira/Desktop/39490000/93842896C:/Users/Cédric Pereira/Desktop/39490000/93842912C:/Users/Cédric Pereira/Desktop/39490000/93842928C:/Users/Cédric Pereira/Desktop/39490000/93842944C:/Users/Cédric Pereira/Desktop/39490000/93842960C:/Users/Cédric Pereira/Desktop/39490000/93842976C:/Users/Cédric Pereira/Desktop/39490000/93842992C:/Users/Cédric Pereira/Desktop/39490000/93843008C:/Users/Cédric Pereira/Desktop/39490000/93843024C:/Users/Cédric Pereira/Desktop/39490000/93843040C:/Users/Cédric Pereira/Desktop/39490000/93843056C:/Users/Cédric Pereira/Desktop/39490000/93843072C:/Users/Cédric Pereira/Desktop/39490000/93843088C:/Users/Cédric Pereira/Desktop/39490000/93843104C:/Users/Cédric Pereira/Desktop/39490000/93843120C:/Users/Cédric Pereira/Desktop/39490000/93843136C:/Users/Cédric Pereira/Desktop/39490000/93843152C:/Users/Cédric Pereira/Desktop/39490000/93843168C:/Users/Cédric Pereira/Desktop/39490000/93843184C:/Users/Cédric Pereira/Desktop/39490000/93843200C:/Users/Cédric Pereira/Desktop/39490000/93843216C:/Users/Cédric Pereira/Desktop/39490000/93843232C:/Users/Cédric Pereira/Desktop/39490000/93843248C:/Users/Cédric Pereira/Desktop/39490000/93843264C:/Users/Cédric Pereira/Desktop/39490000/93843280C:/Users/Cédric Pereira/Desktop/39490000/93843296C:/Users/Cédric Pereira/Desktop/39490000/93843312C:/Users/Cédric Pereira/Desktop/39490000/93843328C:/Users/Cédric Pereira/Desktop/39490000/93843344C:/Users/Cédric Pereira/Desktop/39490000/93843360C:/Users/Cédric Pereira/Desktop/39490000/93843376C:/Users/Cédric Pereira/Desktop/39490000/93843392C:/Users/Cédric Pereira/Desktop/39490000/93843408C:/Users/Cédric Pereira/Desktop/39490000/93843424C:/Users/Cédric Pereira/Desktop/39490000/93843440C:/Users/Cédric Pereira/Desktop/39490000/93843456C:/Users/Cédric Pereira/Desktop/39490000/93843472C:/Users/Cédric Pereira/Desktop/39490000/93843488C:/Users/Cédric Pereira/Desktop/39490000/93843504C:/Users/Cédric Pereira/Desktop/39490000/93843520C:/Users/Cédric Pereira/Desktop/39490000/93843536C:/Users/Cédric Pereira/Desktop/39490000/93843552C:/Users/Cédric Pereira/Desktop/39490000/93843568C:/Users/Cédric Pereira/Desktop/39490000/93843584C:/Users/Cédric Pereira/Desktop/39490000/93843600C:/Users/Cédric Pereira/Desktop/39490000/93843616C:/Users/Cédric Pereira/Desktop/39490000/93843632C:/Users/Cédric Pereira/Desktop/39490000/93843648C:/Users/Cédric Pereira/Desktop/39490000/93843664C:/Users/Cédric Pereira/Desktop/39490000/93843680C:/Users/Cédric Pereira/Desktop/39490000/93843696C:/Users/Cédric Pereira/Desktop/39490000/93843712C:/Users/Cédric Pereira/Desktop/39490000/93843728C:/Users/Cédric Pereira/Desktop/39490000/93843744C:/Users/Cédric Pereira/Desktop/39490000/93843760C:/Users/Cédric Pereira/Desktop/39490000/93843776C:/Users/Cédric Pereira/Desktop/39490000/93843792C:/Users/Cédric Pereira/Desktop/39490000/93843808C:/Users/Cédric Pereira/Desktop/39490000/93843824C:/Users/Cédric Pereira/Desktop/39490000/93843840C:/Users/Cédric Pereira/Desktop/39490000/93843856C:/Users/Cédric Pereira/Desktop/39490000/93843872C:/Users/Cédric Pereira/Desktop/39490000/93843888C:/Users/Cédric Pereira/Desktop/39490000/93843904C:/Users/Cédric Pereira/Desktop/39490000/93843920C:/Users/Cédric Pereira/Desktop/39490000/93843936C:/Users/Cédric Pereira/Desktop/39490000/93843952C:/Users/Cédric Pereira/Desktop/39490000/93843968C:/Users/Cédric Pereira/Desktop/39490000/93843984C:/Users/Cédric Pereira/Desktop/39490000/93844000C:/Users/Cédric Pereira/Desktop/39490000/93844016C:/Users/Cédric Pereira/Desktop/39490000/93844032C:/Users/Cédric Pereira/Desktop/39490000/93844048C:/Users/Cédric Pereira/Desktop/39490000/93844064C:/Users/Cédric Pereira/Desktop/39490000/93844080C:/Users/Cédric Pereira/Desktop/39490000/93844096C:/Users/Cédric Pereira/Desktop/39490000/93844112C:/Users/Cédric Pereira/Desktop/39490000/93844128C:/Users/Cédric Pereira/Desktop/39490000/93844144C:/Users/Cédric Pereira/Desktop/39490000/93844160C:/Users/Cédric Pereira/Desktop/39490000/93844176C:/Users/Cédric Pereira/Desktop/39490000/93844192C:/Users/Cédric Pereira/Desktop/39490000/93844208C:/Users/Cédric Pereira/Desktop/39490000/93844224C:/Users/Cédric Pereira/Desktop/39490000/93844240C:/Users/Cédric Pereira/Desktop/39490000/93844256C:/Users/Cédric Pereira/Desktop/39490000/93844272C:/Users/Cédric Pereira/Desktop/39490000/93844288C:/Users/Cédric Pereira/Desktop/39490000/93844304C:/Users/Cédric Pereira/Desktop/39490000/93844320C:/Users/Cédric Pereira/Desktop/39490000/93844336C:/Users/Cédric Pereira/Desktop/39490000/93844352C:/Users/Cédric Pereira/Desktop/39490000/93844368C:/Users/Cédric Pereira/Desktop/39490000/93844384C:/Users/Cédric Pereira/Desktop/39490000/93844400C:/Users/Cédric Pereira/Desktop/39490000/93844416C:/Users/Cédric Pereira/Desktop/39490000/93844432C:/Users/Cédric Pereira/Desktop/39490000/93844448C:/Users/Cédric Pereira/Desktop/39490000/93844464C:/Users/Cédric Pereira/Desktop/39490000/93844480C:/Users/Cédric Pereira/Desktop/39490000/93844496C:/Users/Cédric Pereira/Desktop/39490000/93844512C:/Users/Cédric Pereira/Desktop/39490000/93844528C:/Users/Cédric Pereira/Desktop/39490000/93844544C:/Users/Cédric Pereira/Desktop/39490000/93844560C:/Users/Cédric Pereira/Desktop/39490000/93844576C:/Users/Cédric Pereira/Desktop/39490000/93844592C:/Users/Cédric Pereira/Desktop/39490000/93844608C:/Users/Cédric Pereira/Desktop/39490000/93844624C:/Users/Cédric Pereira/Desktop/39490000/93844640C:/Users/Cédric Pereira/Desktop/39490000/93844656C:/Users/Cédric Pereira/Desktop/39490000/93844672C:/Users/Cédric Pereira/Desktop/39490000/93844688C:/Users/Cédric Pereira/Desktop/39490000/93844704C:/Users/Cédric Pereira/Desktop/39490000/93844720C:/Users/Cédric Pereira/Desktop/39490000/93844736C:/Users/Cédric Pereira/Desktop/39490000/93844752C:/Users/Cédric Pereira/Desktop/39490000/93844768C:/Users/Cédric Pereira/Desktop/39490000/93844784C:/Users/Cédric Pereira/Desktop/39490000/93844800C:/Users/Cédric Pereira/Desktop/39490000/93844816C:/Users/Cédric Pereira/Desktop/39490000/93844832C:/Users/Cédric Pereira/Desktop/39490000/93844848C:/Users/Cédric Pereira/Desktop/39490000/93844864C:/Users/Cédric Pereira/Desktop/39490000/93844880C:/Users/Cédric Pereira/Desktop/39490000/93844896C:/Users/Cédric Pereira/Desktop/39490000/93844912C:/Users/Cédric Pereira/Desktop/39490000/93844928C:/Users/Cédric Pereira/Desktop/39490000/93844944C:/Users/Cédric Pereira/Desktop/39490000/93844960C:/Users/Cédric Pereira/Desktop/39490000/93844976C:/Users/Cédric Pereira/Desktop/39490000/93844992C:/Users/Cédric Pereira/Desktop/39490000/93845008C:/Users/Cédric Pereira/Desktop/39490000/93845024C:/Users/Cédric Pereira/Desktop/39490000/93845040C:/Users/Cédric Pereira/Desktop/39490000/93845056C:/Users/Cédric Pereira/Desktop/39490000/93845072C:/Users/Cédric Pereira/Desktop/39490000/93845088C:/Users/Cédric Pereira/Desktop/39490000/93845104C:/Users/Cédric Pereira/Desktop/39490000/93845120C:/Users/Cédric Pereira/Desktop/39490000/93845136C:/Users/Cédric Pereira/Desktop/39490000/93845152C:/Users/Cédric Pereira/Desktop/39490000/93845168C:/Users/Cédric Pereira/Desktop/39490000/93845184C:/Users/Cédric Pereira/Desktop/39490000/93845200C:/Users/Cédric Pereira/Desktop/39490000/93845216C:/Users/Cédric Pereira/Desktop/39490000/93845232C:/Users/Cédric Pereira/Desktop/39490000/93845248C:/Users/Cédric Pereira/Desktop/39490000/93845264C:/Users/Cédric Pereira/Desktop/39490000/93845280C:/Users/Cédric Pereira/Desktop/39490000/93845296C:/Users/Cédric Pereira/Desktop/39490000/93845312C:/Users/Cédric Pereira/Desktop/39490000/93845328C:/Users/Cédric Pereira/Desktop/39490000/93845344C:/Users/Cédric Pereira/Desktop/39490000/93845360C:/Users/Cédric Pereira/Desktop/39490000/93845376C:/Users/Cédric Pereira/Desktop/39490000/93845392Imported a DICOM directory, checking for extensions
[DEBUG][Python] 28.03.2018 16:43:25 [Python] (C:/Program Files/Slicer 4.9.0-2018-03-27/lib/Slicer-4.9/qt-scripted-modules/MultiVolumeImporterPlugin.py:452) - MultiVolumeImportPlugin::examine
[DEBUG][Python] 28.03.2018 16:43:25 [Python] (C:/Program Files/Slicer 4.9.0-2018-03-27/lib/Slicer-4.9/qt-scripted-modules/MultiVolumeImporterPlugin.py:492) - DICOMMultiVolumePlugin found 0 multivolumes!
[DEBUG][Python] 28.03.2018 16:43:26 [Python] (C:/Program Files/Slicer 4.9.0-2018-03-27/lib/Slicer-4.9/qt-scripted-modules/MultiVolumeImporterPlugin.py:165) - MultiVolumeImportPlugin:examineMultiseries
[DEBUG][Python] 28.03.2018 16:43:26 [Python] (C:/Program Files/Slicer 4.9.0-2018-03-27/lib/Slicer-4.9/qt-scripted-modules/MultiVolumeImporterPlugin.py:170) - DICOMMultiVolumePlugin found 0 multivolumes!
[ERROR][Python] 28.03.2018 16:43:26 [Python] (C:\Program Files\Slicer 4.9.0-2018-03-27\lib\Slicer-4.9\qt-scripted-modules\DICOMLib\DICOMWidgets.py:862) - DICOM plugin failed to load '2: MPRAGE_p2_1mm_iso' as a 'Scalar Volume'.
Traceback (most recent call last):
  File "C:\Program Files\Slicer 4.9.0-2018-03-27\lib\Slicer-4.9\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 856, in proceedWithReferencedLoadablesSelection
    loadSuccess = plugin.load(loadable)
  File "C:/Program Files/Slicer 4.9.0-2018-03-27/lib/Slicer-4.9/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 411, in load
    volumeNode = self.loadFilesWithSeriesReader("GDCM", loadable.files, loadable.name)
  File "C:/Program Files/Slicer 4.9.0-2018-03-27/lib/Slicer-4.9/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 288, in loadFilesWithSeriesReader
    reader.SetArchetype(files[0]);
TypeError: SetArchetype argument 1: (unicode conversion error)
[WARNING][Python] 28.03.2018 16:43:26 [Python] (C:\Program Files\Slicer 4.9.0-2018-03-27\bin\Python\slicer\util.py:1015) - 
Could not load: 2: MPRAGE_p2_1mm_iso as a Scalar Volume
[CRITICAL][Stream] 28.03.2018 16:43:26 [] (unknown:0) - DICOM plugin failed to load '2: MPRAGE_p2_1mm_iso' as a 'Scalar Volume'.
[CRITICAL][Stream] 28.03.2018 16:43:26 [] (unknown:0) - Traceback (most recent call last):
[CRITICAL][Stream] 28.03.2018 16:43:26 [] (unknown:0) -   File "C:\Program Files\Slicer 4.9.0-2018-03-27\lib\Slicer-4.9\qt-scripted-modules\DICOMLib\DICOMWidgets.py", line 856, in proceedWithReferencedLoadablesSelection
[CRITICAL][Stream] 28.03.2018 16:43:26 [] (unknown:0) -     loadSuccess = plugin.load(loadable)
[CRITICAL][Stream] 28.03.2018 16:43:26 [] (unknown:0) -   File "C:/Program Files/Slicer 4.9.0-2018-03-27/lib/Slicer-4.9/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 411, in load
[CRITICAL][Stream] 28.03.2018 16:43:26 [] (unknown:0) -     volumeNode = self.loadFilesWithSeriesReader("GDCM", loadable.files, loadable.name)
[CRITICAL][Stream] 28.03.2018 16:43:26 [] (unknown:0) -   File "C:/Program Files/Slicer 4.9.0-2018-03-27/lib/Slicer-4.9/qt-scripted-modules/DICOMScalarVolumePlugin.py", line 288, in loadFilesWithSeriesReader
[CRITICAL][Stream] 28.03.2018 16:43:26 [] (unknown:0) -     reader.SetArchetype(files[0]);
[CRITICAL][Stream] 28.03.2018 16:43:26 [] (unknown:0) - TypeError: SetArchetype argument 1: (unicode conversion error)
[CRITICAL][Stream] 28.03.2018 16:43:26 [] (unknown:0) -
[CRITICAL][Stream] 28.03.2018 16:43:26 [] (unknown:0) -
[CRITICAL][Stream] 28.03.2018 16:43:26 [] (unknown:0) - Could not load: 2: MPRAGE_p2_1mm_iso as a Scalar Volume
-----------------------------------------------------------------------</code></pre>

---

## Post #2 by @pieper (2018-03-28 20:23 UTC)

<p>Hi -</p>
<p>It looks like the accent character in your pathname is causing a problem.  When I open the data from a directory with a plain ascii path it loads with no problem.  (the unicode conversion error message is the clue).</p>
<p>-Steve</p>
<aside class="quote no-group quote-modified" data-username="cedric_pereira" data-post="1" data-topic="2459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cedric_pereira/48/1410_2.png" class="avatar"> cedric_pereira:</div>
<blockquote>
<p>[CRITICAL][Stream] 28.03.2018 16:43:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -   File “C:/Program Files/Slicer 4.9.0-2018-03-27/lib/Slicer-4.9/qt-scripted-modules/DICOMScalarVolumePlugin.py”, line 288, in loadFilesWithSeriesReader<br>
[CRITICAL][Stream] 28.03.2018 16:43:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) -     reader.SetArchetype(files[0]);<br>
[CRITICAL][Stream] 28.03.2018 16:43:26 <span class="chcklst-box fa fa-square-o fa-fw"></span> (unknown:0) - TypeError: SetArchetype argument 1: (unicode conversion error)</p>
</blockquote>
</aside>

---
