# slicerMorph - ALPACA registration error in open3d

**Topic ID**: 22908
**Date**: 2022-04-11
**URL**: https://discourse.slicer.org/t/slicermorph-alpaca-registration-error-in-open3d/22908

---

## Post #1 by @MrMarkus (2022-04-11 14:22 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11.20210226 r29738 / 7a593c8</p>
<p><strong>Expected behavior:</strong><br>
I am trying to redo an example of the SlicerMORPH workshop (<a href="https://github.com/SlicerMorph/S_2020/blob/master/Lab_ALPACA/README.md" class="inline-onebox" rel="noopener nofollow ugc">S_2020/README.md at master · SlicerMorph/S_2020 · GitHub</a>). Data can be loaded in the ALPACA module, the “subsampling” step works too, and the points are visualized. Next the “rigid alignment” should work.</p>
<p><strong>Actual behavior:</strong><br>
But the “rigid alignment” does not work / start. Instead the following errors is shown:</p>
<p>Traceback (most recent call last):<br>
File “C:/Program Files/SlicerVersions/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/ALPACA.py”, line 513, in onAlignButton<br>
self.transformMatrix = logic.estimateTransform(self.sourcePoints, self.targetPoints, self.sourceFeatures, self.targetFeatures, self.voxelSize, self.skipScalingCheckBox.checked, self.parameterDictionary)<br>
File “C:/Program Files/SlicerVersions/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/ALPACA.py”, line 1048, in estimateTransform<br>
parameters[“distanceThreshold”], parameters[“maxRANSAC”], parameters[“maxRANSACValidation”], skipScaling)<br>
File “C:/Program Files/SlicerVersions/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/ALPACA.py”, line 1147, in execute_global_registration<br>
], registration.RANSACConvergenceCriteria(maxIter, maxValidation))<br>
TypeError: registration_ransac_based_on_feature_matching(): incompatible function arguments. The following argument types are supported:<br>
1. (source: open3d.open3d_pybind.geometry.PointCloud, target: open3d.open3d_pybind.geometry.PointCloud, source_feature: open3d::registration::Feature, target_feature: open3d::registration::Feature, max_correspondence_distance: float, estimation_method: open3d.open3d_pybind.registration.TransformationEstimation = registration::TransformationEstimationPointToPoint without scaling., ransac_n: int = 4, checkers: List[open3d.open3d_pybind.registration.CorrespondenceChecker] = [], criteria: open3d.open3d_pybind.registration.RANSACConvergenceCriteria = registration::RANSACConvergenceCriteria class with max_iteration=100000, and max_validation=100) → open3d.open3d_pybind.registration.RegistrationResult</p>
<p>As an information:</p>
<ul>
<li>
<p>List item Extension “Sandbox” is not installed since it can´t be found in the extension manager</p>
</li>
<li>
<p>List item the “Auto3dgm” module works fine.</p>
</li>
</ul>
<p>Any idea how to solve this issue?</p>
<p>THANKS!!!</p>
<p>Best,<br>
Markus</p>

---

## Post #2 by @muratmaga (2022-04-12 00:45 UTC)

<aside class="quote no-group" data-username="MrMarkus" data-post="1" data-topic="22908">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<p>TypeError: registration_ransac_based_on_feature_matching(): incompatible function arguments. The following argument types are supported:</p>
</blockquote>
</aside>
<p>This is due to a change in open3d (library we use for point cloud registration) versions. If you uninstall and reinstall SlicerMorph, this should be fixed (it should automatically update the open3d to the correct version).</p>
<p>Let us know if that doesn’t help.</p>

---

## Post #3 by @MrMarkus (2022-04-12 10:30 UTC)

<p>Hi,</p>
<p>I deinstalled:</p>
<ul>
<li>
<p>List item slicerMorph</p>
</li>
<li>
<p>List item 3dgm</p>
</li>
</ul>
<p>Now I try to perform the registration without the 3dgm model, which must fail since<br>
the module is not installed.</p>
<p>The error message is identical:</p>
<p>File “C:/Program Files/SlicerVersions/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/ALPACA.py”, line 513, in onAlignButton<br>
self.transformMatrix = logic.estimateTransform(self.sourcePoints, self.targetPoints, self.sourceFeatures, self.targetFeatures, self.voxelSize, self.skipScalingCheckBox.checked, self.parameterDictionary)<br>
File “C:/Program Files/SlicerVersions/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/ALPACA.py”, line 1048, in estimateTransform<br>
parameters[“distanceThreshold”], parameters[“maxRANSAC”], parameters[“maxRANSACValidation”], skipScaling)<br>
File “C:/Program Files/SlicerVersions/Slicer 4.11.20210226/NA-MIC/Extensions-29738/SlicerMorph/lib/Slicer-4.11/qt-scripted-modules/ALPACA.py”, line 1147, in execute_global_registration<br>
], registration.RANSACConvergenceCriteria(maxIter, maxValidation))<br>
TypeError: registration_ransac_based_on_feature_matching(): incompatible function arguments. The following argument types are supported:<br>
1. (source: open3d.open3d_pybind.geometry.PointCloud, target: open3d.open3d_pybind.geometry.PointCloud, source_feature: open3d::registration::Feature, target_feature: open3d::registration::Feature, max_correspondence_distance: float, estimation_method: open3d.open3d_pybind.registration.TransformationEstimation = registration::TransformationEstimationPointToPoint without scaling., ransac_n: int = 4, checkers: List[open3d.open3d_pybind.registration.CorrespondenceChecker] = [], criteria: open3d.open3d_pybind.registration.RANSACConvergenceCriteria = registration::RANSACConvergenceCriteria class with max_iteration=100000, and max_validation=100) → open3d.open3d_pybind.registration.RegistrationResult</p>
<p>For my understanding:</p>
<ul>
<li>List item <em>open3d</em>
</li>
<li>List item <em>auto3dgm</em>
</li>
</ul>
<p>are two different modules / functions?</p>
<p>Thanks.</p>
<p>Best,<br>
Markus</p>

---

## Post #4 by @muratmaga (2022-04-12 16:02 UTC)

<aside class="quote no-group" data-username="MrMarkus" data-post="3" data-topic="22908">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<p>I deinstalled:</p>
<ul>
<li>List item slicerMorph</li>
<li>List item 3dgm</li>
</ul>
<p>Now I try to perform the registration without the 3dgm model, which must fail since<br>
the module is not installed.</p>
</blockquote>
</aside>
<p>First off, Auto3Dgm has nothing to do with a ALPACA. They are separate modules and they do not work together or depend each other. They serve different functions as well.</p>
<p>There is currently an issue with the stable and open3d. If you want to use ALPACA, you have to options:</p>
<ol>
<li>
<p>Download a preinstalled stable from this link and use as is, without updating anything. (I.e., just uncompress the zip file and run Slicer) <a href="https://app.box.com/shared/static/xziombnoti3jbrc8hqp236v95ghcz2c2.zip">https://app.box.com/shared/static/xziombnoti3jbrc8hqp236v95ghcz2c2.zip</a></p>
</li>
<li>
<p>Use the latest preview version and install SlicerMorph.</p>
</li>
</ol>

---

## Post #5 by @MrMarkus (2022-04-13 09:36 UTC)

<p>Hi,</p>
<ul>
<li>
<p>List item preinstalled stable Slicer works; slicerMorph and ALPACA are running too; in the Extension there is also now the <strong>SandBox</strong> extension installed! Previously SandBox was not available in the ExtensionManager</p>
</li>
<li>
<p>List item slicerMorph is not available in the ExtensionManager of the the latest preview version of 3DSlicer</p>
</li>
</ul>
<p>For now I will work with the precompiled version of Slicer; as long as slicerMorph is not available for the latest preview version.</p>
<p>Best,<br>
Markus</p>

---

## Post #6 by @jamesobutler (2022-04-13 13:53 UTC)

<aside class="quote no-group" data-username="MrMarkus" data-post="5" data-topic="22908">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/71e660/48.png" class="avatar"> MrMarkus:</div>
<blockquote>
<p>List item slicerMorph is not available in the ExtensionManager of the the latest preview version of 3DSlicer</p>
</blockquote>
</aside>
<p>The extension had not yet completed its nightly build on the Windows platform. The build for it was started approximately 21 minutes after your post here at 9:57 UTC. SlicerMorph is one of the last extensions built for the night. Something SlicerMorph has knowledge about it and has created <a href="https://github.com/SlicerMorph/SlicerMorph/issues/195" class="inline-onebox" rel="noopener nofollow ugc">Remove SlicerMorph dependencies but provide a convenient mechanism to install those extensions · Issue #195 · SlicerMorph/SlicerMorph · GitHub</a>.</p>

---
