---
topic_id: 5310
title: "Could Not Load 1 3D Cbct Stitched Volume As A Scalar Volume"
date: 2019-01-08
url: https://discourse.slicer.org/t/5310
---

# Could not load: 1: 3D CBCT Stitched Volume as a Scalar Volume

**Topic ID**: 5310
**Date**: 2019-01-08
**URL**: https://discourse.slicer.org/t/could-not-load-1-3d-cbct-stitched-volume-as-a-scalar-volume/5310

---

## Post #1 by @gbenat (2019-01-08 14:23 UTC)

<p>Hello everyone,</p>
<p>It’s my first time using Slicer (latest version not nightly) and when I want to load the dicom files everytime I have this message “Could not load: 1: 3D CBCT Stitched Volume as a Scalar Volume”.</p>
<p>I’ve looked <a href="https://discourse.slicer.org/t/hi-i-have-problems-solving-the-couldnt-not-load-scalar-volume-problem/2840">here</a> but I don’t know how to use this patch and I’m not sure it’s going to resolve the problem.</p>
<p>here the log file :</p>
<pre><code class="lang-auto">[spoiler] [DEBUG][Qt] 08.01.2019 14:40:00 [] (unknown:0) - Session start time .......: 2019-01-08 14:40:00

[DEBUG][Qt] 08.01.2019 14:40:00 [] (unknown:0) - Slicer version ...........: 4.10.0 (revision 27501) win-amd64 - installed release

[DEBUG][Qt] 08.01.2019 14:40:00 [] (unknown:0) - Operating system .........: Windows / Professional / (Build 9200) - 64-bit

[DEBUG][Qt] 08.01.2019 14:40:00 [] (unknown:0) - Memory ...................: 8133 MB physical, 15694 MB virtual

[DEBUG][Qt] 08.01.2019 14:40:00 [] (unknown:0) - CPU ......................: GenuineIntel , 8 cores, 8 logical processors

[DEBUG][Qt] 08.01.2019 14:40:00 [] (unknown:0) - VTK configuration ........: OpenGL2 rendering, TBB threading

[DEBUG][Qt] 08.01.2019 14:40:00 [] (unknown:0) - Developer mode enabled ...: no

[DEBUG][Qt] 08.01.2019 14:40:00 [] (unknown:0) - Prefer executable CLI ....: yes

[DEBUG][Qt] 08.01.2019 14:40:00 [] (unknown:0) - Additional module paths ..: C:/Users/Gauthier/Downloads/SlicerDicomPatcher-master

[DEBUG][Python] 08.01.2019 14:40:01 [Python] (C:\Program Files\Slicer 4.10.0\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(['git', 'version'], cwd=C:\Program Files\Slicer 4.10.0, universal_newlines=False, shell=None)

[DEBUG][Python] 08.01.2019 14:40:02 [Python] (C:\Program Files\Slicer 4.10.0\lib\Python\Lib\site-packages\git\cmd.py:719) - Popen(['git', 'version'], cwd=C:\Program Files\Slicer 4.10.0, universal_newlines=False, shell=None)

[DEBUG][Python] 08.01.2019 14:40:02 [Python] (C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: Annotations

[DEBUG][Python] 08.01.2019 14:40:03 [Python] (C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentEditor

[DEBUG][Python] 08.01.2019 14:40:03 [Python] (C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\SubjectHierarchyPlugins\AbstractScriptedSubjectHierarchyPlugin.py:36) - Scripted subject hierarchy plugin registered: SegmentStatistics

[DEBUG][Qt] 08.01.2019 14:40:03 [] (unknown:0) - Switch to module: &amp;quot;Welcome&amp;quot;

[INFO][Stream] 08.01.2019 14:40:03 [] (unknown:0) - Loading Slicer RC file [C:/Users/Gauthier/.slicerrc.py]

[DEBUG][Qt] 08.01.2019 14:40:06 [] (unknown:0) - Switch to module: &amp;quot;DICOM&amp;quot;

[DEBUG][Python] 08.01.2019 14:40:10 [Python] (C:/Program Files/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:455) - MultiVolumeImportPlugin::examine

[DEBUG][Python] 08.01.2019 14:40:12 [Python] (C:/Program Files/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:495) - DICOMMultiVolumePlugin found 0 multivolumes!

[DEBUG][Python] 08.01.2019 14:40:12 [Python] (C:/Program Files/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:165) - MultiVolumeImportPlugin:examineMultiseries

[DEBUG][Python] 08.01.2019 14:40:12 [Python] (C:/Program Files/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/MultiVolumeImporterPlugin.py:170) - DICOMMultiVolumePlugin found 0 multivolumes!

[ERROR][Python] 08.01.2019 14:40:12 [Python] (C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py:873) - DICOM plugin failed to load '1: 3D CBCT Stitched Volume' as a 'Scalar Volume'.

Traceback (most recent call last):

File &amp;quot;C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py&amp;quot;, line 867, in proceedWithReferencedLoadablesSelection

loadSuccess = plugin.load(loadable)

File &amp;quot;C:/Program Files/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py&amp;quot;, line 411, in load

volumeNode = self.loadFilesWithSeriesReader(&amp;quot;GDCM&amp;quot;, loadable.files, loadable.name)

File &amp;quot;C:/Program Files/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py&amp;quot;, line 288, in loadFilesWithSeriesReader

reader.SetArchetype(files[0]);

TypeError: SetArchetype argument 1: (unicode conversion error)

[WARNING][Python] 08.01.2019 14:40:12 [Python] (C:\Program Files\Slicer 4.10.0\bin\Python\slicer\util.py:1066) -

Could not load: 1: 3D CBCT Stitched Volume as a Scalar Volume

[CRITICAL][Stream] 08.01.2019 14:40:12 [] (unknown:0) - DICOM plugin failed to load '1: 3D CBCT Stitched Volume' as a 'Scalar Volume'.

[CRITICAL][Stream] 08.01.2019 14:40:12 [] (unknown:0) - Traceback (most recent call last):

[CRITICAL][Stream] 08.01.2019 14:40:12 [] (unknown:0) - File &amp;quot;C:\Program Files\Slicer 4.10.0\lib\Slicer-4.10\qt-scripted-modules\DICOMLib\DICOMWidgets.py&amp;quot;, line 867, in proceedWithReferencedLoadablesSelection

[CRITICAL][Stream] 08.01.2019 14:40:12 [] (unknown:0) - loadSuccess = plugin.load(loadable)

[CRITICAL][Stream] 08.01.2019 14:40:12 [] (unknown:0) - File &amp;quot;C:/Program Files/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py&amp;quot;, line 411, in load

[CRITICAL][Stream] 08.01.2019 14:40:12 [] (unknown:0) - volumeNode = self.loadFilesWithSeriesReader(&amp;quot;GDCM&amp;quot;, loadable.files, loadable.name)

[CRITICAL][Stream] 08.01.2019 14:40:12 [] (unknown:0) - File &amp;quot;C:/Program Files/Slicer 4.10.0/bin/../lib/Slicer-4.10/qt-scripted-modules/DICOMScalarVolumePlugin.py&amp;quot;, line 288, in loadFilesWithSeriesReader

[CRITICAL][Stream] 08.01.2019 14:40:12 [] (unknown:0) - reader.SetArchetype(files[0]);

[CRITICAL][Stream] 08.01.2019 14:40:12 [] (unknown:0) - TypeError: SetArchetype argument 1: (unicode conversion error)

[CRITICAL][Stream] 08.01.2019 14:40:12 [] (unknown:0) -

[CRITICAL][Stream] 08.01.2019 14:40:12 [] (unknown:0) -

[CRITICAL][Stream] 08.01.2019 14:40:12 [] (unknown:0) - Could not load: 1: 3D CBCT Stitched Volume as a Scalar Volume[/spoiler]
</code></pre>
<p>Thanks</p>

---

## Post #2 by @pieper (2019-01-08 18:05 UTC)

<pre><code class="lang-auto">TypeError: SetArchetype argument 1: (unicode conversion error)

</code></pre>
<p>Probably means this issue noted in <a href="https://www.slicer.org/wiki/Documentation/4.10/FAQ/DICOM">the FAQ</a> is the problem:</p>
<blockquote>
<ul>
<li>Try moving the data and the database directory to a path that includes only US English characters (ASCII) to avoid possible parsing errors. No special, international characters are allowed.</li>
</ul>
</blockquote>

---

## Post #3 by @gbenat (2019-01-08 19:25 UTC)

<p>It’s working thanks a lot Pieper !</p>

---
