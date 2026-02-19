---
topic_id: 21896
title: "Unable To Launch Slicer Qt On Arch Linux"
date: 2022-02-10
url: https://discourse.slicer.org/t/21896
---

# Unable to launch Slicer QT on Arch Linux

**Topic ID**: 21896
**Date**: 2022-02-10
**URL**: https://discourse.slicer.org/t/unable-to-launch-slicer-qt-on-arch-linux/21896

---

## Post #1 by @tsims (2022-02-10 17:51 UTC)

<p>Hello, I recently updated to the newest pre-release of slicer, 4.13-2022-02-09 r30598, but for some reason, I am no longer able to access QT designer, when launching it I get the errors below:</p>
<pre><code class="lang-auto">Designer: The class attribute for the class qSlicerDiffusionTensorVolumeDisplayWidgetPlugin does not match the class name qSlicerDiffusionTensorVolumeDisplayWidget.
QMetaProperty::read: Unable to handle unregistered datatype 'ctkDICOMTableManager*' for property 'ctkDICOMQueryRetrieveWidget::dicomTableManager'
QMetaProperty::read: Unable to handle unregistered datatype 'QTableView*' for property 'ctkDICOMTableView::tblDicomDatabaseView'
</code></pre>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/home/tsims/Slicer/bin/../lib/Python/lib/python3.9/subprocess.py", line 73, in &lt;module&gt;
    import msvcrt
ModuleNotFoundError: No module named 'msvcrt'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "/home/tsims/Slicer/bin/../lib/Python/lib/python3.9/pydoc.py", line 66, in &lt;module&gt;
    import platform
  File "/home/tsims/Slicer/bin/../lib/Python/lib/python3.9/platform.py", line 119, in &lt;module&gt;
    import subprocess
  File "/home/tsims/Slicer/bin/../lib/Python/lib/python3.9/subprocess.py", line 78, in &lt;module&gt;
    import _posixsubprocess
ImportError: /home/tsims/Slicer/bin/../lib/Python/lib/python3.9/lib-dynload/_posixsubprocess.so: undefined symbol: PyTuple_Type
QMetaProperty::read: Unable to handle unregistered datatype 'QFrame::Shape' for property 'ctkCollapsibleButton::contentsFrameShape'
QMetaProperty::read: Unable to handle unregistered datatype 'QFrame::Shadow' for property 'ctkCollapsibleButton::contentsFrameShadow'
QMetaProperty::read: Unable to handle unregistered datatype 'QFileDialog::AcceptMode' for property 'ctkDirectoryButton::acceptMode'
QMetaProperty::read: Unable to handle unregistered datatype 'QSlider::TickPosition' for property 'ctkDoubleRangeSlider::tickPosition'
QMetaProperty::read: Unable to handle unregistered datatype 'QSlider::TickPosition' for property 'ctkDoubleSlider::tickPosition'
QMetaProperty::read: Unable to handle unregistered datatype 'QEasingCurve::Type' for property 'ctkBasePopupWidget::easingCurve'
QMetaProperty::read: Unable to handle unregistered datatype 'QSettings*' for property 'ctkSettingsPanel::settings'
QMetaProperty::read: Unable to handle unregistered datatype 'QSettings*' for property 'ctkSettingsDialog::settings'
QMetaProperty::read: Unable to handle unregistered datatype 'ctkSettingsPanel*' for property 'ctkSettingsDialog::currentPanel'
QMetaProperty::read: Unable to handle unregistered datatype 'QSlider::TickPosition' for property 'ctkSliderWidget::tickPosition'
This function is deprecated. Use currentNodeID() instead
qMRMLNodeComboBox::baseName failed: no node types have been set yet
QMetaProperty::read: Unable to handle unregistered datatype 'QComboBox::SizeAdjustPolicy' for property 'qMRMLNodeComboBox::sizeAdjustPolicy'
QMetaProperty::read: Unable to handle unregistered datatype 'QFrame::Shape' for property 'ctkCollapsibleButton::contentsFrameShape'
QMetaProperty::read: Unable to handle unregistered datatype 'QFrame::Shadow' for property 'ctkCollapsibleButton::contentsFrameShadow'
This function is deprecated. Use currentNodeID() instead
qMRMLNodeFactory::baseName failed: class name vtkMRMLColorTableNode not found
QMetaProperty::read: Unable to handle unregistered datatype 'QComboBox::SizeAdjustPolicy' for property 'qMRMLNodeComboBox::sizeAdjustPolicy'
This function is deprecated. Use currentNodeID() instead
QMetaProperty::read: Unable to handle unregistered datatype 'QComboBox::SizeAdjustPolicy' for property 'qMRMLNodeComboBox::sizeAdjustPolicy'
QObject::connect: No such slot qMRMLDisplayNodeWidget::set3DVisible(bool)
QObject::connect:  (sender name:   'ThreeDVisibilityCheckBox')
QObject::connect:  (receiver name: 'qMRMLDisplayNodeWidget')
QMetaProperty::read: Unable to handle unregistered datatype 'QSlider::TickPosition' for property 'ctkSliderWidget::tickPosition'
This function is deprecated. Use currentNodeID() instead
qMRMLNodeComboBox::baseName failed: no node types have been set yet
QMetaProperty::read: Unable to handle unregistered datatype 'QComboBox::SizeAdjustPolicy' for property 'qMRMLNodeComboBox::sizeAdjustPolicy'
QString qMRMLPlotViewControllerWidget::viewLabel() const  failed: must set view node first
QMetaProperty::read: Unable to handle unregistered datatype 'vtkMRMLScene*' for property 'qMRMLRangeWidget::mrmlScene'
QMetaProperty::read: Unable to handle unregistered datatype 'vtkMRMLDisplayNode::ScalarRangeFlagType' for property 'qMRMLScalarsDisplayWidget::scalarRangeMode'
qMRMLSliceControllerWidget::setSliceViewName failed: MRMLSliceNode is invalid
QString qMRMLSliceControllerWidget::sliceViewLabel() const  failed: must set view node first
qMRMLSliceControllerWidget::setSliceViewName failed: MRMLSliceNode is invalid
QString qMRMLSliceControllerWidget::sliceViewLabel() const  failed: must set view node first
QMetaProperty::read: Unable to handle unregistered datatype 'QSlider::TickPosition' for property 'ctkSliderWidget::tickPosition'
qMRMLTableView:: bool qMRMLTableView::transposed() const  failed: invalid node
qMRMLTableView:: bool qMRMLTableView::firstRowLocked() const  failed: invalid node
qMRMLTableView:: bool qMRMLTableView::firstColumnLocked() const  failed: invalid node
virtual void qSlicerMarkupsPlaceWidget::setup() : Markups module is not found, some markup manipulation features will not be available
bool qSlicerMarkupsPlaceWidget::placeModePersistency() const  failed: interactionNode is invalid
qSlicerMarkupsPlaceWidget::deleteAllMarkupsOptionVisible method is deprecated, please use deleteAllControlPointsOptionVisible instead
virtual void qSlicerSimpleMarkupsWidget::setup() : Markups module is not found, some markup manipulation features will not be available
virtual void qSlicerMarkupsPlaceWidget::setup() : Markups module is not found, some markup manipulation features will not be available
virtual void qSlicerSimpleMarkupsWidget::setup() : Markups module is not found, some markup manipulation features will not be available
virtual void qSlicerMarkupsPlaceWidget::setup() : Markups module is not found, some markup manipulation features will not be available
</code></pre>
<pre><code class="lang-auto">error: [/home/tsims/Slicer/bin/./designer-real] exit abnormally - Report the problem.
</code></pre>
<p>This happens regardless of whether I launch QT Designer through the slicer interface, or using the command line <code>Slicer --designer</code></p>
<p>I’m confused as to what’s going on here, Is there a dependency I’m missing on my system?<br>
Thanks!</p>

---

## Post #2 by @jamesobutler (2022-02-10 18:58 UTC)

<p>This may have been fixed just recently in <a href="https://github.com/Slicer/Slicer/commit/9766f4f1f8fd85ed4d33e8f7ea39235b0334502d" rel="noopener nofollow ugc">9766f4f</a> which was solving a Designer crash at startup. This commit is currently the latest commit on the Slicer <code>master</code> branch but since it was merged after the nightly factory Slicer Preview build was started the fix is not available in Today’s preview. It will be available in tomorrow’s Slicer Preview build, or if you build Slicer from source you can use the latest <code>master</code> .</p>
<p>Re <a href="https://github.com/Slicer/Slicer/issues/6174" rel="noopener nofollow ugc">https://github.com/Slicer/Slicer/issues/6174</a></p>

---

## Post #3 by @tsims (2022-02-10 20:10 UTC)

<p>Awesome! Thank you so much for bringing this to my attention. I haven’t been able to build slicer from source myself, but I can definitely wait for tomorrows preview build, Thank you!</p>

---

## Post #4 by @tsims (2022-02-11 14:29 UTC)

<p>Sorry to drudge this back up, but after updating to the latest slicer nightly release(4.13.0-2022-02-10) I am still having this issue…</p>
<p>Is there anything else I can try to get QT running again, or should I just try to build from source?</p>

---

## Post #5 by @chir.set (2022-02-11 15:27 UTC)

<aside class="quote no-group" data-username="tsims" data-post="4" data-topic="21896">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsims/48/11853_2.png" class="avatar"> tsims:</div>
<blockquote>
<p>4.13.0-2022-02-10</p>
</blockquote>
</aside>
<p>Same observation with 4.13.0-2022-02-10 on Arch.</p>
<p>You may try :</p>
<p>./Slicer --launch designer-qt4</p>
<p>This works on my box. designer-qt5 fails too, like designer-real from factory Slicer.</p>

---

## Post #6 by @tsims (2022-02-11 15:35 UTC)

<p>Thank you for the advice! Unfortunately, I don’t seem to have designer-qt4, running that command gets me: <code>error: Application does NOT exists [designer-qt4]</code></p>
<p>I’m working on building Slicer from source now to see if that helps at all.</p>

---

## Post #7 by @lassoan (2022-02-11 15:53 UTC)

<aside class="quote no-group" data-username="tsims" data-post="4" data-topic="21896" data-full="true">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/tsims/48/11853_2.png" class="avatar"> tsims:</div>
<blockquote>
<p>Sorry to drudge this back up, but after updating to the latest slicer nightly release(4.13.0-2022-02-10) I am still having this issue…</p>
<p>Is there anything else I can try to get QT running again, or should I just try to build from source?</p>
</blockquote>
</aside>
<p>The fix was incomplete. A full fix was committed today, which will be available in the Slicer Preview Release tomorrow. If you need Qt designer to work urgently then you can <a href="https://www.slicer.org/wiki/Documentation/Nightly/FAQ/General#Where_can_I_download_Slicer.3F">download a release from 1-2 weeks ago</a>, for example from a week ago: <a href="http://download.slicer.org/?offset=-7">http://download.slicer.org/?offset=-7</a></p>

---
