---
topic_id: 8784
title: "Tests Failed On Circleci"
date: 2019-10-15
url: https://discourse.slicer.org/t/8784
---

# Tests failed on CircleCI

**Topic ID**: 8784
**Date**: 2019-10-15
**URL**: https://discourse.slicer.org/t/tests-failed-on-circleci/8784

---

## Post #1 by @smrolfe (2019-10-15 19:47 UTC)

<p>Hello,<br>
I’ve posted a pull request with some changes to the Markups module and I noticed that it failed a test on CircleCI. I looked at the details and it looks like the error is related to the DICOM module. Is this something I need to address? Would I would need to merge my pull request with a more recent version to pass this test?</p>
<p>Thanks,<br>
Sara</p>
<pre><code class="lang-auto">/usr/src/Slicer/Modules/Scripted/DICOMLib/Widgets/qSlicerDICOMExportDialog.cxx:579:93: error: no matching function for call to ‘ctkDICOMIndexer::addDirectory(ctkDICOMDatabase&amp;, QString, QString&amp;)’
         indexer-&gt;addDirectory(*dicomDatabase, outputFolder.absolutePath(), destinationFolderPath);
                                                                                                 ^
    In file included from /usr/src/Slicer/Modules/Scripted/DICOMLib/Widgets/qSlicerDICOMExportDialog.cxx:70:0:
    /usr/src/Slicer-build/CTK/Libs/DICOM/Core/ctkDICOMIndexer.h:71:20: note: candidate: void ctkDICOMIndexer::addDirectory(const QString&amp;, bool, bool)
       Q_INVOKABLE void addDirectory(const QString&amp; directoryName, bool copyFile = false, bool includeHidden = true);
                        ^
    /usr/src/Slicer-build/CTK/Libs/DICOM/Core/ctkDICOMIndexer.h:71:20: note:   no known conversion for argument 1 from ‘ctkDICOMDatabase’ to ‘const QString&amp;’
    /usr/src/Slicer-build/CTK/Libs/DICOM/Core/ctkDICOMIndexer.h:73:20: note: candidate: void ctkDICOMIndexer::addDirectory(ctkDICOMDatabase*, const QString&amp;, bool, bool)
       Q_INVOKABLE void addDirectory(ctkDICOMDatabase* db, const QString&amp; directoryName, bool copyFile = false, bool includeHidden = true);
                        ^
    /usr/src/Slicer-build/CTK/Libs/DICOM/Core/ctkDICOMIndexer.h:73:20: note:   no known conversion for argument 1 from ‘ctkDICOMDatabase’ to ‘ctkDICOMDatabase*’
    [4513/5132] Building CXX object Modules/Scripted/DICOMLib/Widgets/CMakeFiles/qSlicerDICOMLibModuleWidgets.dir/moc_qSlicerDICOMTagEditorWidget.cpp.o
    [4514/5132] Building CXX object Modules/Scripted/DICOMLib/Widgets/CMakeFiles/qSlicerDICOMLibModuleWidgets.dir/qSlicerDICOMTagEditorWidget.cxx.o
    ninja: build stopped: subcommand failed.
    Exited with code 1
</code></pre>

---

## Post #2 by @jcfr (2019-10-15 21:16 UTC)

<p>Since the docker image  used on CircleCI is re-generated once per day, the error associated with the update CTK dependency is to be expected.</p>

---

## Post #3 by @smrolfe (2019-10-15 21:26 UTC)

<p>Thanks <a class="mention" href="/u/jcfr">@jcfr</a> for the clarification.</p>

---

## Post #4 by @smrolfe (2019-10-16 16:44 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a>, it looks like I may not have permission to trigger a rebuild. Is there a way I can do this without submitting another pull request?</p>

---

## Post #5 by @jcfr (2019-10-16 17:13 UTC)

<blockquote>
<p>Is there a way I can do this without submitting another pull request?</p>
</blockquote>
<p>Assuming <code>smrolfe</code> is associated with your github fork, to re-trigger the build associated with <a href="https://github.com/Slicer/Slicer/pull/1230">PR#1230</a> you could do the following:</p>
<pre data-code-wrap="bash"><code class="lang-bash">git commit --amend --no-edit
git push smrolfe master --force
</code></pre>

---
