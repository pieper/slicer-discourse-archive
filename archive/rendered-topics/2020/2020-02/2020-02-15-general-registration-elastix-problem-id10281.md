---
topic_id: 10281
title: "General Registration Elastix Problem"
date: 2020-02-15
url: https://discourse.slicer.org/t/10281
---

# General Registration(Elastix) problem!

**Topic ID**: 10281
**Date**: 2020-02-15
**URL**: https://discourse.slicer.org/t/general-registration-elastix-problem/10281

---

## Post #1 by @endlessric23 (2020-02-15 18:24 UTC)

<p>Dear Slicer user</p>
<p>I am using the General Registration(Elastix) tool,when I use the parameter (Preset)“2D x-ray - 3D CT(cerebral)”,there’s some error occured.</p>
<p>The detailed log is in the following line.Seems like the library “RayCastInterpolator” is not included in Slicer?</p>
<p>Anyone could help?Thanks in advance.</p>
<hr>
<p>Volume registration is started in working directory: C:/Users/endlessric23/AppData/Local/Temp/Slicer/Elastix/20200215_004706_305</p>
<p>Register volumes…</p>
<p>elastix is started at Sat Feb 15 00:47:06 2020.</p>
<p>which elastix: C:\Users\endlessric23\AppData\Roaming\NA-MIC\Extensions-28770\SlicerElastix\lib\Slicer-4.11\elastix.exe</p>
<p>elastix runs at: DESKTOP-I4B32KJ</p>
<p>Windows Professional (x64), (Build 9200)</p>
<p>with 16191 MB memory, and 4 cores @ 2295 MHz.</p>
<hr>
<p>Running elastix with parameter file 0: “C:\Users\endlessric23\AppData\Roaming\NA-MIC\Extensions-28770\SlicerElastix\lib\Slicer-4.11\qt-scripted-modules\Resources\RegistrationParameters\par0013Powel_NGC_singleImage.txt”.</p>
<p>Current time: Sat Feb 15 00:47:06 2020.</p>
<p>Reading the elastix parameters from file …</p>
<p>Installing all components.</p>
<p>InstallingComponents was successful.</p>
<p>Error:</p>
<p>RayCastInterpolator(index 3) - This component is not installed!</p>
<p>ERROR: error occurred while creating Interpolator 0.</p>
<p>itk::ExceptionObject (000000177172F1A0)</p>
<p>Location: “unknown”</p>
<p>File: D:\D\P\S-0-E-b\SlicerElastix-build\elastix\Core\Kernel\elxElastixMain.cxx</p>
<p>Line: 822</p>
<p>Description: itk::ERROR: ElastixMain(0000021068BF4AA0): The following component could not be created: RayCastInterpolator</p>
<p>Error:</p>
<p>NormalizedGradientCorrelation(index 3) - This component is not installed!</p>
<p>ERROR: error occurred while creating Metric 0.</p>
<p>itk::ExceptionObject (000000177172F1A0)</p>
<p>Location: “unknown”</p>
<p>File: D:\D\P\S-0-E-b\SlicerElastix-build\elastix\Core\Kernel\elxElastixMain.cxx</p>
<p>Line: 822</p>
<p>Description: itk::ERROR: ElastixMain(0000021068BF4AA0): The following component could not be created: NormalizedGradientCorrelation</p>
<p>Error:</p>
<p>FinalRayCastInterpolator(index 3) - This component is not installed!</p>
<p>ERROR: error occurred while creating ResampleInterpolator 0.</p>
<p>itk::ExceptionObject (000000177172F1A0)</p>
<p>Location: “unknown”</p>
<p>File: D:\D\P\S-0-E-b\SlicerElastix-build\elastix\Core\Kernel\elxElastixMain.cxx</p>
<p>Line: 822</p>
<p>Description: itk::ERROR: ElastixMain(0000021068BF4AA0): The following component could not be created: FinalRayCastInterpolator</p>
<p>ERROR:</p>
<p>One or more components could not be created.</p>
<p>Errors occurred!</p>
<p>vtkDebugLeaks has found no leaks.</p>
<p>Error: Command ‘elastix’ returned non-zero exit status 1.</p>

---

## Post #2 by @lassoan (2020-02-15 18:28 UTC)

<p>We bundle an Elastix instance with the SlicerElastix extension that is built with default build options. If you find that FinalRayCastInterpolator is not included then please contact the Elastix team and ask why this is not enabled when building Elastix with default options. Depending on the answer, we may decide to enable this option.</p>
<p>In the meantime, you can use a custom Elastix package (that has all the optional components that you need) by setting path to Elastix in “Advanced” section.</p>

---

## Post #3 by @endlessric23 (2020-02-16 05:47 UTC)

<p>I have find out the solution.<br>
The Elastix extension I install from the Slicer is not the complete version. After I download the new version from the Elastix official website and overwrite the “elastix.exe” and “transformix.exe” to the relative path ,the problem have been solved.<br>
Maybe it’s better to add the new Elastix version to the next release.Thanks!</p>

---

## Post #4 by @timeanddoctor (2020-02-16 13:32 UTC)

<aside class="quote no-group" data-username="endlessric23" data-post="1" data-topic="10281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/endlessric23/48/6037_2.png" class="avatar"> endlessric23:</div>
<blockquote>
<p>2D x-ray - 3D CT</p>
</blockquote>
</aside>
<p>Hi, Eric, This means that the Elastrix can register the ‘2D X ray’ with  3d CT? interesting. Could you give me some information about that? Thanks.</p>

---

## Post #5 by @lassoan (2020-02-16 13:40 UTC)

<aside class="quote no-group" data-username="endlessric23" data-post="3" data-topic="10281">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/endlessric23/48/6037_2.png" class="avatar"> endlessric23:</div>
<blockquote>
<p>The Elastix extension I install from the Slicer is not the complete version.</p>
</blockquote>
</aside>
<p>We build Slicer’s Elastix from latest version of the source code, default build options. If there are features that are disabled by default then they are not included. Please ask the Elastix team what build options they are using for building their downloadable binaries and then we can switch to using the same options.</p>

---

## Post #6 by @endlessric23 (2020-02-23 15:42 UTC)

<p>Sorry for replying late.<br>
This is the 2D-3D registration in elastix, and it can use inside 3Dslicer by some modification.<br>
<a href="http://elastix.bigr.nl/wiki/index.php/Par0013" class="onebox" target="_blank" rel="nofollow noopener">http://elastix.bigr.nl/wiki/index.php/Par0013</a></p>

---
