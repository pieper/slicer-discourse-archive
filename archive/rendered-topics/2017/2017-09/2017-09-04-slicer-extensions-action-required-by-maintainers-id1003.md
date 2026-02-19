---
topic_id: 1003
title: "Slicer Extensions Action Required By Maintainers"
date: 2017-09-04
url: https://discourse.slicer.org/t/1003
---

# Slicer extensions: Action required by maintainers

**Topic ID**: 1003
**Date**: 2017-09-04
**URL**: https://discourse.slicer.org/t/slicer-extensions-action-required-by-maintainers/1003

---

## Post #1 by @jcfr (2017-09-04 21:33 UTC)

<p>During the past few days, while testing the recent updates associated with Slicer build system, I ended updating some extensions.</p>
<h3>List of extension that will be fixed shortly</h3>
<ul>
<li>
<p>Eigen3</p>
<ul>
<li>missing packageupload: We will probably extend the extension description file to include support for <code>skip_packageupload 1</code>
</li>
</ul>
</li>
</ul>
<h3>List of extension fixed: Waiting integration and review of proposed Pull Requests by maintainers</h3>
<p>Yes, for these extensions … the work has been done.</p>
<p>Please, consider <strong>reviewing and integrating these PRs during this week</strong>. We would like to have as much extensions as possible available for an upcoming release. (to be announced)</p>
<p>If you would prefer not to maintain your extension, let us know and we will remove it from the extension build system.</p>
<ul>
<li>
<p>CBC_3D_I2MConversion - See <a href="https://github.com/fdrakopo/CBC3D_I2M_Conversion_SlicerExtension/pull/1" rel="nofollow noopener">fdrakopo/CBC3D_I2M_Conversion_SlicerExtension#1</a></p>
<ul>
<li>Fix build error caused by use of ITK ivar.</li>
<li>Fix sign-compare warnings</li>
<li>Fix undefined itkFactoryRegistration link error</li>
</ul>
</li>
<li>
<p>MarginCalculator</p>
<ul>
<li>Repository converted to Git: <a href="https://github.com/jcfr/MarginCalculator" rel="nofollow noopener">https://github.com/jcfr/MarginCalculator</a>
</li>
<li>Patches available at <a href="https://github.com/jcfr/MarginCalculator/compare/add-vtk7-and-qt5-support" rel="nofollow noopener">https://github.com/jcfr/MarginCalculator/compare/add-vtk7-and-qt5-support</a>
</li>
</ul>
</li>
<li>
<p>PBNRR_SlicerExtension</p>
<ul>
<li>Fix undefined itkFactoryRegistration link error. See <a href="https://github.com/fdrakopo/PBNRR_SlicerExtension/pull/1" rel="nofollow noopener">fdrakopo/PBNRR_SlicerExtension#1</a>
</li>
</ul>
</li>
<li>
<p>RSSExtension - See <a href="https://github.com/gaoyi/RSSExtension/pull/9" rel="nofollow noopener">gaoyi/RSSExtension#9</a></p>
<ul>
<li>Transition to VTK6 API</li>
<li>Update to use <code>vtkMRMLLabelMapVolumeNode</code>
</li>
<li>Add support for Qt5</li>
</ul>
</li>
</ul>
<h3>List of extensions failing to configure or build: Action required by maintainer</h3>
<ul>
<li>
<p>DTI-Reg:</p>
<ul>
<li>TODO: Fix problem with boost (extension is attempting to build boost internally)</li>
</ul>
</li>
<li>
<p>FacetedVisualizer</p>
<ul>
<li>Fix error <code>fatal error C1083: Cannot open include file: 'vtk_sqlite3.h'</code>
</li>
</ul>
</li>
<li>
<p>FiberViewerLight</p>
<ul>
<li>The extension still requires work to compile using Qt5 and VTK8</li>
</ul>
</li>
<li>
<p>MABMIS</p>
<ul>
<li>Fix build error updating code to use <code>itkInverseDisplacementFieldImageFilter</code> instead of <code>itkInverseDeformationFieldImageFilter</code>. This filter <code>itkInverseDeformationFieldImageFilter</code> is deprecated and available only when building ITK with <code>ITKV3_COMPATIBILITY</code> set to 1 and this<br>
is <strong>NOT</strong> the case anymore in Slicer.</li>
</ul>
</li>
<li>
<p>SegmentationAidedRegistration (see <a href="https://github.com/gaoyi/SegmentationAidedRegistration/issues/7" rel="nofollow noopener">gaoyi/SegmentationAidedRegistration#7</a>)</p>
<ul>
<li>see below <code>LASegmenter</code>
</li>
</ul>
</li>
<li>
<p>ErodeDilateLabel (see <a href="https://github.com/tokjun/ErodeDilateLabel/issues/2" rel="nofollow noopener">tokjun/ErodeDilateLabel#2</a>)</p>
<ul>
<li>see below <code>LASegmenter</code>
</li>
</ul>
</li>
</ul>
<h3>List of extensions expected to fail to configure or build: No actions required</h3>
<ul>
<li>
<a href="https://github.com/NIRALUser/DTIFiberTractStatistics" rel="nofollow noopener">DTIAtlasFiberAnalyzer</a>
<ul>
<li>Failure expected - look like the build system was updated to require Qt5</li>
</ul>
</li>
</ul>
<h3>List of extension fixed and updated</h3>
<ul>
<li>
<p>SlicerOpenCV</p>
<ul>
<li>numpy issue should be addressed by <s><a href="https://github.com/Slicer/Slicer/pull/786" rel="nofollow noopener">https://github.com/Slicer/Slicer/pull/786</a></s>  <strong>Merged</strong>
</li>
</ul>
</li>
<li>
<p>ModelClip <s><a href="https://github.com/j-lin/ModelClip/pull/3" rel="nofollow noopener">PR j-lin/ModelClip#3</a></s>  <strong>Merged</strong>. Repository transfer to <a href="https://github.com/Ting-Jia/ModelClip" rel="nofollow noopener">https://github.com/Ting-Jia/ModelClip</a></p>
<ul>
<li>Fix build error adding support for VTK &gt;= 6 and Qt5</li>
</ul>
</li>
<li>
<p>LightWeightRobotIGT <s><a href="https://github.com/SNRLab/LightWeightRobotIGT/pull/4" rel="nofollow noopener">PR SNRLab/LightWeightRobotIGT#1</a></s> <strong>Merged</strong></p>
<ul>
<li>Fix configure and build, add support for Qt5</li>
</ul>
</li>
<li>
<p>boost: <s><a href="https://github.com/Slicer/ExtensionsIndex/pull/1457" rel="nofollow noopener">PR Slicer/ExtensionsIndex#1457</a></s> - <strong>Merged</strong></p>
<ul>
<li>Remove unused and failing extension</li>
</ul>
</li>
<li>
<p>CarreraSlice <s><a href="https://github.com/ikolesov/CarreraSlice/pull/9" rel="nofollow noopener">PR ikolesov/CarreraSlice#9</a></s> - <strong>Merged</strong></p>
<ul>
<li>Simplify build system and update extension to support VTK8</li>
</ul>
</li>
<li>
<p>DCMQI</p>
<ul>
<li>Fix warnings <s><a href="https://github.com/QIICR/dcmqi/pull/299" rel="nofollow noopener">QIICR/dcmqi#299</a></s> - <strong>Merged</strong>
</li>
<li>cmake: Fix forcebuild step <s><a href="https://github.com/QIICR/dcmqi/pull/300" rel="nofollow noopener">QIICR/dcmqi#300</a></s> - <strong>Merged</strong>
</li>
<li>Fix setting of cxx standard <s><a href="https://github.com/QIICR/dcmqi/pull/298" rel="nofollow noopener">QIICR/dcmqi#298</a></s> - <strong>Merged</strong>
</li>
</ul>
</li>
<li>
<p>DTIPrep <s><a href="https://github.com/NIRALUser/DTIPrep/pull/45" rel="nofollow noopener">PR NIRALUser/DTIPrep#45</a></s> - <strong>Merged</strong></p>
<ul>
<li>Remove dependency on ITKv3Compatibility</li>
<li>Build against BRAINSTools, ITKv4 and SlicerExecutionModel provided by Slicer</li>
<li>Updated Slicer to allow extension reusing BRAINSCommonLib. See <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26331" rel="nofollow noopener">r26331</a>
</li>
</ul>
</li>
<li>
<p>Eigen: <s><a href="https://github.com/Slicer/ExtensionsIndex/pull/1455" rel="nofollow noopener">PR Slicer/ExtensionsIndex#1455</a></s> - <strong>Merged</strong></p>
<ul>
<li>Rename <em>build time</em> extension Eigen to Eigen3, and update to the latest version to add modern CMake support. Target <code>Eigen3::Eigen</code> should now be used to build against Eigen.</li>
</ul>
</li>
<li>
<p>exStone <s><a href="https://github.com/qimo601/exStone/pull/1" rel="nofollow noopener">PR qimo601/exStone#1</a></s> - <strong>Merged</strong></p>
<ul>
<li>Fix configure and build, add support for Qt5</li>
</ul>
</li>
<li>
<p>FiberViewerLight - <s>See <a href="https://github.com/NIRALUser/FiberViewerLight/pull/1" rel="nofollow noopener">NIRALUser/FiberViewerLight#1</a></s> - <strong>Merged</strong></p>
<ul>
<li>Fix build error using dedicated macro for building CLI: <a href="https://github.com/Slicer/SlicerExecutionModel/blob/master/CMake/SEMMacroBuildCLI.cmake" rel="nofollow noopener">SEMMacroBuildCLI</a>
</li>
<li>Fix build warnings</li>
</ul>
</li>
<li>
<p>ImageMaker: <s><a href="https://github.com/Slicer/ExtensionsIndex/pull/1459" rel="nofollow noopener">PR Slicer/ExtensionsIndex#1459</a></s> - <strong>Merged</strong></p>
<ul>
<li>Fix undefined itkFactoryRegistration link error</li>
</ul>
</li>
<li>
<p>LASegmenter <s><a href="https://github.com/ljzhu/LASegmenter/pull/5" rel="nofollow noopener">PR ljzhu/LASegmenter#5</a></s> - <strong>Merged</strong></p>
<ul>
<li>Simplify build system.</li>
<li><s>issue <a href="https://github.com/ljzhu/LASegmenter/issues/4" rel="nofollow noopener">ljzhu/LASegmenter#4</a> still need to be fixed by maintainer</s></li>
<li>Fix build error updating code to use <code>itkDisplacementFieldJacobianDeterminantFilter</code> instead of <code>itkMultiplyByConstantImageFilter</code>. The filter <code>itkMultiplyByConstantImageFilter</code> is deprecated and available only when building ITK with <code>ITKV3_COMPATIBILITY</code> set to 1 and this is <strong>NOT</strong> the case anymore in Slicer.</li>
</ul>
</li>
<li>
<p>LongitudinalPETCT <s><a href="https://github.com/QIICR/LongitudinalPETCT/pull/10" rel="nofollow noopener">PR QIICR/LongitudinalPETCT#10</a></s> - <strong>Merged</strong></p>
<ul>
<li>Fix build error</li>
<li>Add support for Qt5</li>
</ul>
</li>
<li>
<p>PortPlacement: <s><a href="https://github.com/giogadi/PortPlacement/pull/3" rel="nofollow noopener">PR giogadi/PortPlacement#3: Fix and improve build system</a>, <a href="https://github.com/Slicer/ExtensionsIndex/pull/1460" rel="nofollow noopener">PR Slicer/ExtensionsIndex#1460</a> and <a href="https://github.com/Slicer/ExtensionsIndex/pull/1461" rel="nofollow noopener">PR Slicer/ExtensionsIndex#1461</a></s> - <strong>Merged</strong></p>
<ul>
<li>Switch to a Superbuild structure to download and build NLopt</li>
<li>Update to use the latest version of Eigen</li>
<li>Add support for Qt5</li>
</ul>
</li>
<li>
<p>SlicerCIP (Chest_Imaging_Platform) - See <s><a href="https://github.com/acil-bwh/SlicerCIP/pull/21" rel="nofollow noopener">acil-bwh/SlicerCIP#21</a></s> - <strong>Merged</strong></p>
<ul>
<li>Fix build errors and warnings</li>
<li>Fix memory leaks</li>
<li>Update Slicer to call cleanup function when script module are unloaded. See <a href="https://github.com/Slicer/Slicer/pull/785" rel="nofollow noopener">Slicer/Slicer#785</a>
</li>
<li>Remove usage of factory methods like <code>vtkMRMLScene::GetNodesByClass</code> and use <code>slicer.util.getNodesByClass</code>. While wrapping of these methods can be improved with VTK8 thanks to wrapper hint like <code>VTK_NEWINSTANCE</code>, let’s avoid using them in Slicer. See <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Tutorials/MemoryManagement#Python_scripts_and_scripted_modules" rel="nofollow noopener">Slicer wiki /MemoryManagement#Python_scripts_and_scripted_modules</a> and <a href="http://www.vtk.org/Wiki/VTK/Wrapping_hints#Hinting_with_attributes" rel="nofollow noopener">VTK wiki /Wrapping_hints#Hinting_with_attributes</a> for more details.</li>
<li>Add support for Qt5</li>
</ul>
</li>
<li>
<p>SkullStripper: <s><a href="https://github.com/Slicer/SkullStripper/pull/9" rel="nofollow noopener">PR Slicer/SkullStripper#9</a>, <a href="https://github.com/Slicer/ExtensionsIndex/pull/1453" rel="nofollow noopener">PR Slicer/ExtensionsIndex#1453</a></s> - <strong>Merged</strong></p>
<ul>
<li>Fix undefined itkFactoryRegistration link error</li>
</ul>
</li>
<li>
<p>XNATSlicer: <s><a href="https://github.com/Slicer/ExtensionsIndex/pull/1456" rel="nofollow noopener">PR Slicer/ExtensionsIndex#1456</a></s> - <strong>Merged</strong></p>
<ul>
<li>Update extensionsIndex to fix “reference is not a tree” error.</li>
</ul>
</li>
<li>
<p>Extensions having <code>@rpath</code>-like packaging error are <strong>fixed</strong> by Slicer <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=26305" rel="nofollow noopener">r26305</a>:</p>
<ul>
<li>ABC</li>
<li>CarreraSlice</li>
<li>ChangeTracker</li>
<li>Cleaver</li>
<li>CMFreg</li>
<li>DCMQI - ~See also <a href="https://github.com/QIICR/dcmqi/pull/295" rel="nofollow noopener">PR QIICR/dcmqi#295</a>~ - <em>PR integrated</em>
</li>
<li>DSCMRIAnalysis</li>
<li>DTIProcess</li>
<li>IASEM</li>
<li>IntensitySegmenter</li>
<li>LAScarSegmenter</li>
<li>MarkupsToModel</li>
<li>PET-IndiC</li>
<li>PETDICOMExtension</li>
<li>PkModeling</li>
<li>ScatteredTransform</li>
<li>Sequences</li>
<li>ShapeVariationAnalyzer</li>
<li>SkullStripper</li>
<li>SlicerProstate</li>
<li>SlicerRT</li>
<li>SliceTracker</li>
<li>SobolevSegmenter</li>
<li>SPHARM-PDM - See also <a href="https://github.com/NIRALUser/SPHARM-PDM/pull/22" rel="nofollow noopener">PR NIRALUser/SPHARM-PDM#22</a>
</li>
<li>T1Mapping</li>
<li>UKFTractography</li>
</ul>
</li>
</ul>
<h3>Extension candidates for adoption</h3>
<ul>
<li>
<p>GraphCutSegmentExtension - See <a href="https://github.com/DaphneCD/GraphCutSegmentExtension/pull/1" rel="nofollow noopener">DaphneCD/GraphCutSegmentExtension#1</a> - <strong>Candidate for Adoption</strong>. See <a href="https://discourse.slicer.org/t/adopting-graphcutsegmentextension-extension/7248" class="inline-onebox">Adopting GraphCutSegmentExtension extension?</a></p>
<ul>
<li>Fix compilation errors and CMake warnings</li>
<li>Add support for Qt5</li>
</ul>
</li>
<li>
<p>VirtualFractureReconstruction <a href="https://github.com/kfritscher/VirtualFractureReconstructionSlicerExtension/pull/3" rel="nofollow noopener">PR kfritscher/VirtualFractureReconstructionSlicerExtension#3</a> - <strong>Candidate for Adoption</strong>. See <a href="https://discourse.slicer.org/t/adopting-virtualfracturereconstruction-extension/7237" class="inline-onebox">Adopting VirtualFractureReconstruction extension?</a></p>
<ul>
<li>Fix warnings, add support for Qt5</li>
</ul>
</li>
</ul>
<h3>List of extension removed from the extension index:</h3>
<ul>
<li>FinslerTractography:
<ul>
<li>
<s>TODO: Update to build against VTK7 / VTK8</s> - <strong>Removed</strong> from the extension index in <a href="https://github.com/Slicer/ExtensionsIndex/pull/1479" rel="nofollow noopener">PR Slicer/ExtensionsIndex#1479</a>
</li>
</ul>
</li>
</ul>

---

## Post #2 by @fedorov (2017-09-27 20:55 UTC)

<p>I confirm the SlicerOpenCV error is gone - thank you!</p>

---
