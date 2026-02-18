# Stable version of SlicerVR

**Topic ID**: 22336
**Date**: 2022-03-06
**URL**: https://discourse.slicer.org/t/stable-version-of-slicervr/22336

---

## Post #1 by @Leung_Aaron (2022-03-06 20:30 UTC)

<p>Hello<br>
Since I have a project needed to use SlicerVR, so I would like to build SlicerVR project in cmake.</p>
<p>I have tried many version of SlicerVR in github, most of them fail to build the project in vtkRenderingOpenVR and inner.</p>
<pre><code class="lang-auto">Severity	Code	Description	Project	File	Line	Suppression State
Error	MSB8066	Custom build for 'F:\D\S4R\SlicerVR\CMakeFiles\4de357d2a3659b3b5a81c69b6fc0b157\vtkRenderingOpenVR-mkdir.rule;F:\D\S4R\SlicerVR_04\CMakeFiles\4de357d2a3659b3b5a81c69b6fc0b157\vtkRenderingOpenVR-download.rule;F:\D\S4R\SlicerVR\CMakeFiles\4de357d2a3659b3b5a81c69b6fc0b157\vtkRenderingOpenVR-update.rule;F:\D\S4R\SlicerVR\CMakeFiles\4de357d2a3659b3b5a81c69b6fc0b157\vtkRenderingOpenVR-patch.rule;F:\D\S4R\SlicerVR\CMakeFiles\4de357d2a3659b3b5a81c69b6fc0b157\vtkRenderingOpenVR-configure.rule;F:\D\S4R\SlicerVR\CMakeFiles\4de357d2a3659b3b5a81c69b6fc0b157\vtkRenderingOpenVR-build.rule;F:\D\S4R\SlicerVR\CMakeFiles\4de357d2a3659b3b5a81c69b6fc0b157\vtkRenderingOpenVR-install.rule;F:\D\S4R\SlicerVR\CMakeFiles\1b423e06f6b430fa8b90efcad27df7cc\vtkRenderingOpenVR-complete.rule;F:\D\S4R\SlicerVR\CMakeFiles\efffa24efbec743773d9f93a8c20833e\vtkRenderingOpenVR.rule;F:\D\S4\SlicerVirtualReality-034d838e0eab2b3c70b4eae0e849d35073440653\CMakeLists.txt' exited with code 1.	vtkRenderingOpenVR	C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets	241	
Error	MSB8066	Custom build for 'F:\D\S4R\SlicerVR\CMakeFiles\9993858f00e15720affc7d195311cd9e\inner-mkdir.rule;F:\D\S4R\SlicerVR\CMakeFiles\9993858f00e15720affc7d195311cd9e\inner-download.rule;F:\D\S4R\SlicerVR\CMakeFiles\9993858f00e15720affc7d195311cd9e\inner-update.rule;F:\D\S4R\SlicerVR\CMakeFiles\9993858f00e15720affc7d195311cd9e\inner-patch.rule;F:\D\S4R\SlicerVR\CMakeFiles\9993858f00e15720affc7d195311cd9e\inner-configure.rule;F:\D\S4R\SlicerVR\CMakeFiles\9993858f00e15720affc7d195311cd9e\inner-build.rule;F:\D\S4R\SlicerVR\CMakeFiles\9993858f00e15720affc7d195311cd9e\inner-forceconfigure.rule;F:\D\S4R\SlicerVR\CMakeFiles\9993858f00e15720affc7d195311cd9e\inner-install.rule;F:\D\S4R\SlicerVR\CMakeFiles\1b423e06f6b430fa8b90efcad27df7cc\inner-complete.rule;F:\D\S4R\SlicerVR\CMakeFiles\efffa24efbec743773d9f93a8c20833e\inner.rule;F:\D\S4\SlicerVirtualReality-034d838e0eab2b3c70b4eae0e849d35073440653\CMakeLists.txt' exited with code 1.	inner	C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets	241	

</code></pre>
<p>I would like to ask that which version can be build successfully?</p>
<p>Thank you</p>

---
