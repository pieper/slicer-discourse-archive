---
topic_id: 8058
title: "Slicer Build Fails On All Platforms"
date: 2019-08-16
url: https://discourse.slicer.org/t/8058
---

# Slicer build fails on all platforms

**Topic ID**: 8058
**Date**: 2019-08-16
**URL**: https://discourse.slicer.org/t/slicer-build-fails-on-all-platforms/8058

---

## Post #1 by @cpinter (2019-08-16 13:27 UTC)

<p>Hi all,</p>
<p>My clean Slicer builds failed, with undeterministic errors about CTK and/or ITK configuration.<br>
I checked and the dashboard shows failed build on all platforms<br>
<a href="http://slicer.cdash.org/index.php?project=SlicerPreview" class="onebox" target="_blank">http://slicer.cdash.org/index.php?project=SlicerPreview</a></p>
<p>Since I didn’t see any other possible cause, I reverted <a href="https://github.com/Slicer/Slicer/commit/aa6083015618f425653203df0eae90a4f9df7492">https://github.com/Slicer/Slicer/commit/aa6083015618f425653203df0eae90a4f9df7492</a><br>
and tried again. It has not failed yet but did not get too far either.</p>
<p>Please take a look at this.<br>
Thanks!</p>

---

## Post #2 by @jamesobutler (2019-08-16 13:43 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> I don’t think you ever pushed the new branch for <a href="https://github.com/Slicer/ITK" rel="nofollow noopener">Slicer/ITK</a> as part of this recent commit <a href="https://github.com/Slicer/Slicer/commit/aa6083015618f425653203df0eae90a4f9df7492" rel="nofollow noopener">https://github.com/Slicer/Slicer/commit/aa6083015618f425653203df0eae90a4f9df7492</a><br>
.</p>

---

## Post #3 by @Sam_Horvath (2019-08-16 14:12 UTC)

<p>Yep, the ITK on the Slicer fork branch that Slicer master wants to reference is missing.  Pushing that branch will fix.</p>

---

## Post #4 by @cpinter (2019-08-16 14:19 UTC)

<p>Thanks for checking!</p>
<p>So it seems no changes are needed in Slicer itself.</p>
<p>Interesting that my windows build errors were not definite… The mac and linux dashboards are much more informative.</p>

---

## Post #5 by @Sam_Horvath (2019-08-16 14:22 UTC)

<p>… They are all giving the exact same error when I look at CDash?</p>
<p>From the windows build: <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1671302" class="inline-onebox">CDash</a></p>
<blockquote>
<p>fatal: reference is not a tree: 35e6f546438557f22e66db25e066499637890214<br>
CMake Error at ITK-prefix/tmp/ITK-gitclone.cmake:40 (message):<br>
Failed to checkout tag: ‘35e6f546438557f22e66db25e066499637890214’</p>
</blockquote>

---

## Post #6 by @cpinter (2019-08-16 14:24 UTC)

<p>Right. My local build gave me generic “cmd” errors, sometimes when configuring ITK sometimes when CTK. Not sure why.</p>

---

## Post #7 by @Sam_Horvath (2019-08-16 14:28 UTC)

<p>So the non-specific cmd error are to be expected, since cmake/VS uses cmd.exe to execute system functions (git, file copies, etc.).  To figure out what actually happened, I usually search for <code>CMake Error</code> in the build output.</p>
<p>Visual Studio isn’t great with its reporting of these build target errors, and sometimes they get attached to the wrong project.</p>

---

## Post #8 by @Sam_Horvath (2019-08-16 14:30 UTC)

<p>Anyway, If we get that branch issues fixed in the next few hours, I will re-trigger the nightly builds.</p>

---

## Post #9 by @jcfr (2019-08-16 15:20 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="2" data-topic="8058">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>I don’t think you ever pushed the new branch for <a href="https://github.com/Slicer/ITK">Slicer/ITK</a></p>
</blockquote>
</aside>
<p>Ooops. Good catch. This should now be fixed.</p>

---

## Post #10 by @Sam_Horvath (2019-08-16 15:52 UTC)

<p>Great!</p>
<p>Should we retrigger the nightly?  My concern is that the extension builds will not finish before the next nightly is scheduled (esp. for windows).  If we skip the extensions, then the current nightly download wont have a working extension manager until next morning.  I am thinking we just skip for today, so that yesterday’s build will remain on the download page, unless it is critical to see build status today.</p>

---

## Post #11 by @cpinter (2019-08-16 17:58 UTC)

<p>I updated and started a build. I’m getting errors like</p>
<pre><code>c:\d\s4r\itk\modules\core\common\include\itkThreadSupport.h(59): error C2065: 'ITK_DEFAULT_MAX_THREADS': undeclared identifier [C:\d\S4R\Slicer-build
\Modules\Loadable\Markups\Logic\vtkSlicerMarkupsModuleLogicPythonD.vcxproj] [C:\d\S4R\Slicer.vcxproj]
c:\d\s4r\itk\modules\core\common\include\itkThreadSupport.h(59): error C2131: expression did not evaluate to a constant [C:\d\S4R\Slicer-build\Module
s\Loadable\Markups\Logic\vtkSlicerMarkupsModuleLogicPythonD.vcxproj] [C:\d\S4R\Slicer.vcxproj]
</code></pre>
<p>Something is still going on.</p>

---

## Post #12 by @Sam_Horvath (2019-08-16 18:10 UTC)

<p>Can you locate itkConfigure.h in your itk build, and check what it has (if anything) for ITK_DEFAULT_MAX_THREADS?  We may need to update the External_ITK file,</p>

---

## Post #13 by @cpinter (2019-08-16 18:14 UTC)

<p>Sorry I reverted again. I’d need to work but have been struggling with this all day so far.</p>

---

## Post #14 by @Sam_Horvath (2019-08-16 18:28 UTC)

<p>That’s fine, I am going to start a local build to look at this.</p>

---

## Post #15 by @jcfr (2019-08-16 20:30 UTC)

<p>I also just updated the version of SimleITK, it was failing to build on linux. See <a href="http://viewvc.slicer.org/viewvc.cgi/Slicer4?view=revision&amp;revision=28446" rel="nofollow noopener">r28446</a></p>

---

## Post #16 by @cpinter (2019-08-19 16:38 UTC)

<p>Just checked the result of my builds at work, and there is (hopefully) one last issue:</p>
<pre><code>  c:\d\s4r\brainstools\brainscommonlib\genericRegistrationHelper.h(506): error C2555: 'itk::MultiModal3DMutualRegistrationHelper&lt;TransformType,Optimi
zerType,FixedImageType,MovingImageType,FitCommonCodeMetricType&gt;::GetMTime': overriding virtual function return type differs and is not covariant from
 'itk::Object::GetMTime' [C:\d\S4R\Slicer-build\E\BRAINSTools\BRAINSCommonLib\BRAINSCommonLib.vcxproj] [C:\d\S4R\Slicer.vcxproj]
  c:\d\slicer\modules\cli\expertautomatedregistration\itkregistrationhelper\itkImageToImageRegistrationMethod.h(147): error C2555: 'itk::ImageToImage
RegistrationMethod&lt;TImage&gt;::GetMTime': overriding virtual function return type differs and is not covariant from 'itk::Object::GetMTime' [C:\d\S4R\Sl
icer-build\Modules\CLI\ExpertAutomatedRegistration\ExpertAutomatedRegistrationLib.vcxproj] [C:\d\S4R\Slicer.vcxproj]
  c:\d\slicer\modules\cli\resampledtivolume\itkDiffusionTensor3DResample.h(78): error C2555: 'itk::DiffusionTensor3DResample&lt;PixelType,PixelType&gt;::Ge
tMTime': overriding virtual function return type differs and is not covariant from 'itk::Object::GetMTime' [C:\d\S4R\Slicer-build\Modules\CLI\Resampl
eDTIVolume\ResampleDTIVolumeLib.vcxproj] [C:\d\S4R\Slicer.vcxproj]
  c:\d\slicer\modules\cli\resampledtivolume\itkTransformDeformationFieldFilter.h(58): error C2555: 'itk::TransformDeformationFieldFilter&lt;double,doubl
e,3&gt;::GetMTime': overriding virtual function return type differs and is not covariant from 'itk::Object::GetMTime' [C:\d\S4R\Slicer-build\Modules\CLI
\ResampleDTIVolume\ResampleDTIVolumeLib.vcxproj] [C:\d\S4R\Slicer.vcxproj]
  c:\d\slicer\modules\cli\resampledtivolume\itkDiffusionTensor3DResample.h(78): error C2555: 'itk::DiffusionTensor3DResample&lt;PixelType,PixelType&gt;::Ge
tMTime': overriding virtual function return type differs and is not covariant from 'itk::Object::GetMTime' [C:\d\S4R\Slicer-build\Modules\CLI\Resampl
eDTIVolume\ResampleDTIVolumeLib.vcxproj] [C:\d\S4R\Slicer.vcxproj]
  c:\d\slicer\modules\cli\resampledtivolume\itkTransformDeformationFieldFilter.h(58): error C2555: 'itk::TransformDeformationFieldFilter&lt;double,doubl
e,3&gt;::GetMTime': overriding virtual function return type differs and is not covariant from 'itk::Object::GetMTime' [C:\d\S4R\Slicer-build\Modules\CLI
\ResampleScalarVectorDWIVolume\ResampleScalarVectorDWIVolumeLib.vcxproj] [C:\d\S4R\Slicer.vcxproj]
</code></pre>
<p>The dashboard shows this too, and apparently only Windows is affected. Builds on the other two platforms are fine.</p>

---

## Post #17 by @lassoan (2019-08-19 16:39 UTC)

<p>I see this, too. I’m just testing if replacing <code>unsigned long</code> by <code>ModifiedTimeType</code> fixes the issue.</p>

---

## Post #18 by @lassoan (2019-08-19 16:54 UTC)

<p>I’ve pushed a <a href="https://github.com/Slicer/Slicer/commit/6ec0ceae9bc4beda25054bf601aed9c8254397aa">fix in Slicer</a>.</p>
<p>Unfortunately, there is a single use of the old <code>unsigned long</code> type in BRAINS, too (BRAINSTools\BRAINSCommonLib\genericRegistrationHelper.hxx and .h).<br>
<a class="mention" href="/u/jcfr">@jcfr</a> or <a class="mention" href="/u/sam_horvath">@Sam_Horvath</a> could you take care of this?</p>

---

## Post #19 by @Sam_Horvath (2019-08-19 17:05 UTC)

<p>Sure, I can get that.</p>

---

## Post #20 by @Sam_Horvath (2019-08-19 17:50 UTC)

<p>PR is up for BRAINSTools, <a class="mention" href="/u/hjmjohnson">@hjmjohnson</a></p>

---

## Post #21 by @cpinter (2019-08-19 18:01 UTC)

<p>Awesome! Thanks everyone for fixing these issues, a great help!</p>

---

## Post #22 by @Sam_Horvath (2019-08-20 14:58 UTC)

<p>BRAINS has been updated in Slicer to include this fix.  Thanks, <a class="mention" href="/u/hjmjohnson">@hjmjohnson</a> !</p>

---
