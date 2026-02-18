# The SlicerDMRI extension is currently unavailable.

**Topic ID**: 12276
**Date**: 2020-06-29
**URL**: https://discourse.slicer.org/t/the-slicerdmri-extension-is-currently-unavailable/12276

---

## Post #1 by @KIM_TY (2020-06-29 16:19 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/e/2e6d5a04aa220007662bcc09a057139be9cd75cb.jpeg" alt="2" data-base62-sha1="6CIfoZ5qi2xkkOq5RGtsKDgwaoP" width="459" height="388"></p>

---

## Post #2 by @pieper (2020-06-29 18:08 UTC)

<p>Thanks for the report.  Yes, it looks like the build is broken on windows.</p>
<p><a href="http://slicer.cdash.org/viewBuildError.php?buildid=1951157" class="onebox" target="_blank">http://slicer.cdash.org/viewBuildError.php?buildid=1951157</a></p>
<p>Does anyone know how to fix that error?  My local SlicerDMRI build works on mac.</p>

---

## Post #3 by @Sam_Horvath (2020-06-29 18:32 UTC)

<p>We had similar errors on Slicer when we switched to the newer Visual Studio.  Discussion here:<br>
</p><aside class="onebox githubpullrequest">
  <header class="source">
      <a href="https://github.com/Slicer/DashboardScripts/pull/28" target="_blank" rel="nofollow noopener">github.com/Slicer/DashboardScripts</a>
  </header>
  <article class="onebox-body">
    <div class="github-row">
  <div class="github-icon-container" title="Pull Request">
    <svg width="60" height="60" class="github-icon" viewBox="0 0 12 16" aria-hidden="true"><path d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"></path></svg>
  </div>

  <div class="github-info-container">
    <h4>
      <a href="https://github.com/Slicer/DashboardScripts/pull/28" target="_blank" rel="nofollow noopener">overload: Update nightly builds to use Qt 5.15.0</a>
    </h4>

    <div class="branches">
      <code>Slicer:master</code> ← <code>jamesobutler:windows-qt-5.15.0</code>
    </div>

    <div class="github-info">
      <div class="date">
        opened <span class="discourse-local-date" data-format="ll" data-date="2020-05-27" data-time="12:50:33" data-timezone="UTC">12:50PM - 27 May 20 UTC</span>
      </div>

      <div class="user">
        <a href="https://github.com/jamesobutler" target="_blank" rel="nofollow noopener">
          <img alt="jamesobutler" src="https://avatars1.githubusercontent.com/u/15837524?v=4" class="onebox-avatar-inline" width="20" height="20">
          jamesobutler
        </a>
      </div>

      <div class="lines" title="2 commits changed 3 files with 12 additions and 12 deletions">
        <a href="https://github.com/Slicer/DashboardScripts/pull/28/files" target="_blank" rel="nofollow noopener">
          <span class="added">+12</span>
          <span class="removed">-12</span>
        </a>
      </div>
    </div>

  </div>
</div>

  </article>
  <div class="onebox-metadata">
    
    
  </div>
  <div style="clear: both"></div>
</aside>

<p>tl;dr is that I just disabled the tests.  I tried re-writing the test driver that they use (it is clearly out of date compared to tests that are working) but I couldn’t get anything to work.</p>

---

## Post #5 by @KIM_TY (2020-07-04 00:25 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e17b17361f26dd2af102d9ba2d8647c83430b39.jpeg" alt="1" data-base62-sha1="4id5msPqlwREOZ9oIqSrCB6sOLL" width="403" height="493"> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c8fa7949ab2f45b860ab3a344597c585dff6c3c.jpeg" data-download-href="/uploads/short-url/1N7vvDzN3AZMmu9lSDiUzASzjuA.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c8fa7949ab2f45b860ab3a344597c585dff6c3c_2_679x500.jpeg" alt="2" data-base62-sha1="1N7vvDzN3AZMmu9lSDiUzASzjuA" width="679" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c8fa7949ab2f45b860ab3a344597c585dff6c3c_2_679x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/0c8fa7949ab2f45b860ab3a344597c585dff6c3c_2_1018x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0c8fa7949ab2f45b860ab3a344597c585dff6c3c.jpeg 2x" data-dominant-color="E9EFF4"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1128×830 165 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>An error occurs whenever a new version is released.</p>
<p>The same error appears when installing a new visual studio.</p>

---

## Post #6 by @fpsiddiqui91 (2020-07-13 10:32 UTC)

<p>I am facing the same error. Could anyone find the solution yet?</p>

---

## Post #7 by @fpsiddiqui91 (2020-07-20 09:48 UTC)

<p>I have tried to rebuilt the slicer last week, I am still facing the same problem. The version and the platform is mentioned in the screenshot. Could you able to fix the problem? Thanks</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/956c04d4c917d7c526ae4d3c6f511c851cdcd0e7.png" alt="image" data-base62-sha1="ljQzuxQkfEIZ8ce2k0GdlsxT219" width="403" height="151"></p>

---

## Post #8 by @pieper (2020-07-22 18:13 UTC)

<p>We’re hopeful that <a href="https://github.com/SlicerDMRI/SlicerDMRI/commit/d2cd670f86e45b28a41ee5f3a61dd5bfd56d7916">this change</a> will fix the windows version of SlicerDMRI.  Please try tomorrow’s preview build and let us know.</p>

---

## Post #9 by @fpsiddiqui91 (2020-07-24 06:29 UTC)

<p>Thank you for your response <a class="mention" href="/u/pieper">@pieper</a> . I just rebuilt the slicer with the latest version. The problem still persists. Is the problem in my built?  Is there anyone who has this problem in windows?</p>
<p>Thank you</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/9/79a32bf0e7822d70878aba4dcaaae05cb68f9344.png" alt="image" data-base62-sha1="hm3mMU0vMwa7eQN7GpS9gr9GUBe" width="376" height="154"></p>

---

## Post #10 by @fpsiddiqui91 (2020-07-24 09:18 UTC)

<p>In my terminal window, I can see this error (picture attached). I think the clicer is not able to open the URL. I have downloaded the the Slicer DMRI pkg from the given address. Is there any way to install and add this package in my slicer built?</p>
<p>Looking forward to your response</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9edd5fd4bfb61c7f387efcfa10a33939ff4edb34.png" data-download-href="/uploads/short-url/mFnJqn4R590F1KDsGSzxBu4Ghco.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/e/9edd5fd4bfb61c7f387efcfa10a33939ff4edb34.png" alt="image" data-base62-sha1="mFnJqn4R590F1KDsGSzxBu4Ghco" width="690" height="138" data-dominant-color="181818"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">735×147 3.23 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #11 by @pieper (2020-07-24 12:46 UTC)

<p>The windows build of the dmri extension succeeded today, so you should be able to use it with the nightly preview download of Slicer.  It’s not expected that the download will work with your local build because the compilation environment is different.  You can checkout and build the dmri extension on your local machine if you want to try that.</p>

---

## Post #12 by @fpsiddiqui91 (2020-07-24 13:14 UTC)

<p>Thanks for your response <a class="mention" href="/u/pieper">@pieper</a>. I just tried, it worked. I am able to rub SlicerDMRI now.</p>
<p>However, UKF tractography is not working and I cannot find it in the extension manager. I think I have to build it on my local machine.<br>
Any remarks on this?</p>
<p>Thank you again.</p>

---

## Post #13 by @pieper (2020-07-24 13:29 UTC)

<p>Thanks for letting us know.  It looks like UKF has the <a href="http://slicer.cdash.org/viewBuildError.php?buildid=1971396">same kind of linker errors</a>.  Unfortunately on this it appears it’s not just the tests, but the program itself.  You could try to build UKF yourself, but you might run into the same issue.  I’ll try a build here too.</p>

---

## Post #14 by @fpsiddiqui91 (2020-07-24 13:49 UTC)

<p>Yeah, I tried, but I could not make it running. Can you please fix the problem.<br>
Do I have to build the slicer again to install UKF module once the problem is fixed?</p>
<p>Thank you</p>

---

## Post #15 by @fpsiddiqui91 (2020-07-24 16:03 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> , I am trying to build the UKF myself but I indeed came across some linking errors. I am attaching the build output log. I hope it will help</p>
<p>1&gt;------ Build started: Project: ZERO_CHECK, Configuration: Release x64 ------<br>
1&gt;Checking Build System<br>
2&gt;------ Build started: Project: UKF-Eigen, Configuration: Release x64 ------<br>
3&gt;------ Build started: Project: _GEN_GITVER, Configuration: Release x64 ------<br>
4&gt;------ Build started: Project: vtkSlicerInteractiveUKFModuleLogicHierarchy, Configuration: Release x64 ------<br>
5&gt;------ Build started: Project: CopyInteractiveUKFPythonScriptFiles, Configuration: Release x64 ------<br>
6&gt;------ Build started: Project: ConfigureAdditionalLauncherSettings, Configuration: Release x64 ------<br>
7&gt;------ Build started: Project: SlicerWithUKFTractographyConfigureLauncher, Configuration: Release x64 ------<br>
2&gt;Creating directories for ‘UKF-Eigen’<br>
3&gt;Generating UKF_GIT_HASH<br>
5&gt;Copying python Script: InteractiveUKF.py<br>
4&gt;For vtkSlicerInteractiveUKFModuleLogic - updating vtkSlicerInteractiveUKFModuleLogicHierarchy.txt<br>
6&gt;Configuring: AdditionalLauncherSettings.ini<br>
6&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/CMakeLists.txt<br>
5&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/InteractiveUKF/UI/CMakeLists.txt<br>
8&gt;------ Build started: Project: CompileInteractiveUKFPythonFiles, Configuration: Release x64 ------<br>
2&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/CMakeLists.txt<br>
3&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/ukf/CMakeLists.txt<br>
2&gt;Performing download step (git clone) for ‘UKF-Eigen’<br>
8&gt;Compiling python scripts: InteractiveUKF<br>
2&gt;-- Avoiding repeated git clone, stamp file is up to date: ‘C:/Users/20191382/Documents/Slicer_Extensions/UKF_build2/UKF-Eigen-prefix/src/UKF-Eigen-stamp/UKF-Eigen-gitclone-lastrun.txt’<br>
2&gt;Performing update step for ‘UKF-Eigen’<br>
2&gt;No patch step for ‘UKF-Eigen’<br>
7&gt;Configuring application launcher: SlicerWithUKFTractography<br>
2&gt;No configure step for ‘UKF-Eigen’<br>
8&gt;Compiling C:/Users/20191382/Documents/Slicer_Extensions/UKF_build2/lib/Slicer-4.11/qt-scripted-modules/InteractiveUKF.py …<br>
8&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/InteractiveUKF/UI/CMakeLists.txt<br>
2&gt;No build step for ‘UKF-Eigen’<br>
7&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/CMakeLists.txt<br>
2&gt;No install step for ‘UKF-Eigen’<br>
2&gt;Completed ‘UKF-Eigen’<br>
9&gt;------ Build started: Project: UKFBase, Configuration: Release x64 ------<br>
9&gt;Generating git_version.cc<br>
9&gt;Generating UKFTractographyCLP.h<br>
9&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/ukf/CMakeLists.txt<br>
9&gt;GenerateCLP --InputXML C:/Users/20191382/Documents/Git_Reps/ukftractography/UKFTractography/UKFTractography.xml --OutputCxx C:/Users/20191382/Documents/Slicer_Extensions/UKF_build2/ukf/UKFTractographyCLP.h<br>
9&gt;GenerateCLP: Found 6 parameters groups<br>
9&gt;GenerateCLP: Group “IO” has 5 parameters<br>
9&gt;GenerateCLP: Group “Tractography Options” has 11 parameters<br>
9&gt;GenerateCLP: Group “Tensor Model (default)” has 7 parameters<br>
9&gt;GenerateCLP: Group “NODDI Model” has 6 parameters<br>
9&gt;GenerateCLP: Group “Signal Parameters (Expert Only)” has 1 parameters<br>
9&gt;GenerateCLP: Group “Not Used: Debug/Develop Only” has 12 parameters<br>
9&gt;git_version.cc<br>
9&gt;BRAINSThreadControl.cxx<br>
4&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/InteractiveUKF/Logic/CMakeLists.txt<br>
9&gt;utilities.cc<br>
9&gt;C:\Users\20191382\Documents\Git_Reps\ukftractography\ukf\utilities.cc(866,9): warning C4244: ‘argument’: conversion from ‘ukfPrecisionType’ to ‘Eigen::EigenBase::Index’, possible loss of data<br>
9&gt;        with<br>
9&gt;        [<br>
9&gt;            Derived=Eigen::Matrix&lt;double,-1,1,0,-1,1&gt;<br>
9&gt;        ]<br>
9&gt;cli.cc<br>
9&gt;tractography.cc<br>
9&gt;unscented_kalman_filter.cc<br>
9&gt;seed.cc<br>
9&gt;ukffiber.cc<br>
9&gt;NrrdData.cc<br>
9&gt;vtk_writer.cc<br>
9&gt;dwi_normalize.cc<br>
9&gt;thread.cc<br>
9&gt;QuadProg++_Eigen.cc<br>
9&gt;filter_model.cc<br>
9&gt;filter_Full1T.cc<br>
9&gt;filter_Full1T_FW.cc<br>
9&gt;filter_Full2T.cc<br>
9&gt;filter_Full2T_FW.cc<br>
9&gt;filter_Full3T.cc<br>
9&gt;filter_NODDI1F.cc<br>
9&gt;Generating Code…<br>
9&gt;Compiling…<br>
9&gt;filter_NODDI2F.cc<br>
9&gt;filter_Simple1T.cc<br>
9&gt;filter_Simple1T_FW.cc<br>
9&gt;filter_Simple2T.cc<br>
9&gt;filter_Simple2T_FW.cc<br>
9&gt;filter_Simple3T.cc<br>
9&gt;Generating Code…<br>
9&gt;Auto build dll exports<br>
9&gt;jsoncpp.lib(jsoncpp.dll) : error LNK2005: “public: __cdecl Json::Reader::~Reader(void)” (??1Reader@Json@<span class="mention">@QEAA</span>@XZ) already defined in ParameterSerializerLib.lib(itkJsonCppArchiver.obj)<br>
9&gt;jsoncpp.lib(jsoncpp.dll) : error LNK2005: “public: __cdecl Json::StyledStreamWriter::~StyledStreamWriter(void)” (??1StyledStreamWriter@Json@<span class="mention">@QEAA</span>@XZ) already defined in ParameterSerializerLib.lib(itkJsonCppArchiver.obj)<br>
9&gt;   Creating library C:/Users/20191382/Documents/Slicer_Extensions/UKF_build2/lib/Release/UKFBase.lib and object C:/Users/20191382/Documents/Slicer_Extensions/UKF_build2/lib/Release/UKFBase.exp<br>
9&gt;C:\Users\20191382\Documents\Slicer_Extensions\UKF_build2\bin\Release\UKFBase.dll : fatal error LNK1169: one or more multiply defined symbols found<br>
9&gt;Done building project “UKFBase.vcxproj” – FAILED.<br>
10&gt;------ Build started: Project: UKFTractographyLib, Configuration: Release x64 ------<br>
11&gt;------ Build started: Project: vtkSlicerInteractiveUKFModuleLogic, Configuration: Release x64 ------<br>
12&gt;------ Build started: Project: ConvertVTKLib, Configuration: Release x64 ------<br>
11&gt;For vtkSlicerInteractiveUKFModuleLogic - updating vtkSlicerInteractiveUKFModuleLogicHierarchy.txt<br>
10&gt;Generating UKFTractographyCLP.h<br>
12&gt;Generating ConvertVTKCLP.h<br>
10&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/UKFTractography/CMakeLists.txt<br>
10&gt;GenerateCLP --InputXML C:/Users/20191382/Documents/Git_Reps/ukftractography/UKFTractography/UKFTractography.xml --OutputCxx C:/Users/20191382/Documents/Slicer_Extensions/UKF_build2/UKFTractography/UKFTractographyCLP.h<br>
10&gt;GenerateCLP: Found 6 parameters groups<br>
10&gt;GenerateCLP: Group “IO” has 5 parameters<br>
10&gt;GenerateCLP: Group “Tractography Options” has 11 parameters<br>
10&gt;GenerateCLP: Group “Tensor Model (default)” has 7 parameters<br>
10&gt;GenerateCLP: Group “NODDI Model” has 6 parameters<br>
10&gt;GenerateCLP: Group “Signal Parameters (Expert Only)” has 1 parameters<br>
10&gt;GenerateCLP: Group “Not Used: Debug/Develop Only” has 12 parameters<br>
12&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/UKFTractography/CMakeLists.txt<br>
12&gt;GenerateCLP --InputXML C:/Users/20191382/Documents/Git_Reps/ukftractography/UKFTractography/ConvertVTK.xml --OutputCxx C:/Users/20191382/Documents/Slicer_Extensions/UKF_build2/UKFTractography/ConvertVTKCLP.h<br>
12&gt;GenerateCLP: Found 1 parameters groups<br>
12&gt;GenerateCLP: Group “” has 4 parameters<br>
10&gt;UKFTractography.cxx<br>
12&gt;ConvertVTK.cxx<br>
12&gt;C:\D\S4R\JsonCpp\include\json\value.h(53,50): warning C4275: non dll-interface class ‘std::exception’ used as base for dll-interface class ‘Json::Exception’<br>
12&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\VC\Tools\MSVC\14.26.28801\include\vcruntime_exception.h(48): message : see declaration of ‘std::exception’<br>
12&gt;C:\D\S4R\JsonCpp\include\json\value.h(53): message : see declaration of ‘Json::Exception’<br>
12&gt;C:\D\S4R\JsonCpp\include\json\reader.h(249,63): warning C4275: non dll-interface class ‘Json::CharReader::Factory’ used as base for dll-interface class ‘Json::CharReaderBuilder’<br>
12&gt;C:\D\S4R\JsonCpp\include\json\reader.h(227): message : see declaration of ‘Json::CharReader::Factory’<br>
12&gt;C:\D\S4R\JsonCpp\include\json\reader.h(249): message : see declaration of ‘Json::CharReaderBuilder’<br>
11&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/InteractiveUKF/Logic/CMakeLists.txt<br>
11&gt;vtkSlicerInteractiveUKFLogic.cxx<br>
12&gt;ConvertVTKLib.vcxproj -&gt; C:\Users\20191382\Documents\Slicer_Extensions\UKF_build2\lib\Slicer-4.11\cli-modules\Release\ConvertVTKLib.lib<br>
12&gt;Done building project “ConvertVTKLib.vcxproj”.<br>
13&gt;------ Build started: Project: ConvertVTK, Configuration: Release x64 ------<br>
13&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/UKFTractography/CMakeLists.txt<br>
13&gt;SEMCommandLineLibraryWrapper.cxx<br>
13&gt;   Creating library C:/Users/20191382/Documents/Slicer_Extensions/UKF_build2/lib/Slicer-4.11/cli-modules/Release/ConvertVTK.lib and object C:/Users/20191382/Documents/Slicer_Extensions/UKF_build2/lib/Slicer-4.11/cli-modules/Release/ConvertVTK.exp<br>
13&gt;ConvertVTK.vcxproj -&gt; C:\Users\20191382\Documents\Slicer_Extensions\UKF_build2\lib\Slicer-4.11\cli-modules\Release\ConvertVTK.exe<br>
10&gt;UKFTractographyLib.vcxproj -&gt; C:\Users\20191382\Documents\Slicer_Extensions\UKF_build2\lib\Slicer-4.11\cli-modules\Release\UKFTractographyLib.lib<br>
14&gt;------ Build started: Project: UKFTractography, Configuration: Release x64 ------<br>
13&gt;Copying XML file ‘ConvertVTK.xml’ along side the executable<br>
14&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/UKFTractography/CMakeLists.txt<br>
14&gt;SEMCommandLineLibraryWrapper.cxx<br>
14&gt;UKFTractography.vcxproj -&gt; C:\Users\20191382\Documents\Slicer_Extensions\UKF_build2\lib\Slicer-4.11\cli-modules\Release\UKFTractography.exe<br>
14&gt;Copying XML file ‘UKFTractography.xml’ along side the executable<br>
15&gt;------ Build started: Project: UKFTractographyTest, Configuration: Release x64 ------<br>
15&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/UKFTractography/Testing/CMakeLists.txt<br>
15&gt;CompareFibers.cc<br>
11&gt;   Creating library C:/Users/20191382/Documents/Slicer_Extensions/UKF_build2/lib/Slicer-4.11/qt-loadable-modules/Release/vtkSlicerInteractiveUKFModuleLogic.lib and object C:/Users/20191382/Documents/Slicer_Extensions/UKF_build2/lib/Slicer-4.11/qt-loadable-modules/Release/vtkSlicerInteractiveUKFModuleLogic.exp<br>
11&gt;vtkSlicerInteractiveUKFModuleLogic.vcxproj -&gt; C:\Users\20191382\Documents\Slicer_Extensions\UKF_build2\lib\Slicer-4.11\qt-loadable-modules\Release\vtkSlicerInteractiveUKFModuleLogic.dll<br>
16&gt;------ Build started: Project: vtkSlicerInteractiveUKFModuleLogicPythonD, Configuration: Release x64 ------<br>
16&gt;Python Wrapping - generating vtkSlicerInteractiveUKFLogicPython.cxx<br>
15&gt;UKFTractographyTest.vcxproj -&gt; C:\Users\20191382\Documents\Slicer_Extensions\UKF_build2\bin\Release\UKFTractographyTest.exe<br>
16&gt;Python Wrapping - generating vtkSlicerInteractiveUKFModuleLogicPythonInit.cxx<br>
16&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/InteractiveUKF/Logic/CMakeLists.txt<br>
16&gt;vtkSlicerInteractiveUKFLogicPython.cxx<br>
16&gt;vtkSlicerInteractiveUKFModuleLogicPythonInitImpl.cxx<br>
16&gt;Generating Code…<br>
16&gt;   Creating library C:/Users/20191382/Documents/Slicer_Extensions/UKF_build2/lib/Slicer-4.11/qt-loadable-modules/Release/vtkSlicerInteractiveUKFModuleLogicPythonD.lib and object C:/Users/20191382/Documents/Slicer_Extensions/UKF_build2/lib/Slicer-4.11/qt-loadable-modules/Release/vtkSlicerInteractiveUKFModuleLogicPythonD.exp<br>
16&gt;vtkSlicerInteractiveUKFModuleLogicPythonD.vcxproj -&gt; C:\Users\20191382\Documents\Slicer_Extensions\UKF_build2\lib\Slicer-4.11\qt-loadable-modules\Release\vtkSlicerInteractiveUKFModuleLogicPythonD.dll<br>
17&gt;------ Build started: Project: vtkSlicerInteractiveUKFModuleLogicPython, Configuration: Release x64 ------<br>
17&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/InteractiveUKF/Logic/CMakeLists.txt<br>
17&gt;vtkSlicerInteractiveUKFModuleLogicPythonInit.cxx<br>
17&gt;   Creating library C:/Users/20191382/Documents/Slicer_Extensions/UKF_build2/lib/Slicer-4.11/qt-loadable-modules/Release/vtkSlicerInteractiveUKFModuleLogicPython.lib and object C:/Users/20191382/Documents/Slicer_Extensions/UKF_build2/lib/Slicer-4.11/qt-loadable-modules/Release/vtkSlicerInteractiveUKFModuleLogicPython.exp<br>
17&gt;vtkSlicerInteractiveUKFModuleLogicPython.vcxproj -&gt; C:\Users\20191382\Documents\Slicer_Extensions\UKF_build2\lib\Slicer-4.11\qt-loadable-modules\Release\vtkSlicerInteractiveUKFModuleLogicPython.pyd<br>
18&gt;------ Build started: Project: ALL_BUILD, Configuration: Release x64 ------<br>
18&gt;Building Custom Rule C:/Users/20191382/Documents/Git_Reps/ukftractography/CMakeLists.txt<br>
========== Build: 17 succeeded, 1 failed, 0 up-to-date, 0 skipped ==========</p>

---

## Post #16 by @pieper (2020-07-24 18:55 UTC)

<p>Interesting - your build fails with the same error as the dashboard, but my local ukftractography build succeeded without the error.</p>
<p>I’m using Visual Studio 2019 and needed to make a small change to the Boost build script but otherwise it’s the ukf master version.  I am building in debug though, and that might be the difference.</p>
<pre><code class="lang-auto">diff --git a/SuperBuild/External_Boost.cmake b/SuperBuild/External_Boost.cmake
index 4eda1a4..35c66b2 100644
--- a/SuperBuild/External_Boost.cmake
+++ b/SuperBuild/External_Boost.cmake
@@ -74,7 +74,7 @@ if(NOT ( DEFINED "USE_SYSTEM_${extProjName}" AND "${USE_SYSTEM_${extProjName}}"
          list(APPEND Boost_b2_Command toolset=msvc-14.0)
     elseif(MSVC_VERSION GREATER_EQUAL 1910 AND MSVC_VERSION LESS 1920)
          list(APPEND Boost_b2_Command toolset=msvc-14.1)
-    elseif(MSVC_VERSION GREATER_EQUAL 1920 AND MSVC_VERSION LESS 1922)
+    elseif(MSVC_VERSION GREATER_EQUAL 1920 AND MSVC_VERSION LESS 1927)^M
          list(APPEND Boost_b2_Command toolset=msvc-14.2)
     else()
          message(FATAL_ERROR "Unknown MSVC compiler version [${MSVC_VERSION}]")
@@ -143,4 +143,4 @@ mark_as_superbuild(
     ${extProjName}_DIR:PATH
   LABELS
     "FIND_PACKAGE"

</code></pre>
<pre><code class="lang-auto">1&gt;------ Build started: Project: ZERO_CHECK, Configuration: Debug x64 ------
1&gt;Checking Build System
2&gt;------ Build started: Project: UKF-Eigen, Configuration: Debug x64 ------
3&gt;------ Build started: Project: _GEN_GITVER, Configuration: Debug x64 ------
4&gt;------ Build started: Project: vtkSlicerInteractiveUKFModuleLogicHierarchy, Configuration: Debug x64 ------
5&gt;------ Build started: Project: CopyInteractiveUKFPythonScriptFiles, Configuration: Debug x64 ------
6&gt;------ Build started: Project: ConfigureAdditionalLauncherSettings, Configuration: Debug x64 ------
7&gt;------ Build started: Project: SlicerWithUKFTractographyConfigureLauncher, Configuration: Debug x64 ------
2&gt;Creating directories for 'UKF-Eigen'
3&gt;Generating UKF_GIT_HASH
2&gt;Building Custom Rule C:/pieper/ukftractography/CMakeLists.txt
2&gt;Performing download step (git clone) for 'UKF-Eigen'
4&gt;For vtkSlicerInteractiveUKFModuleLogic - updating vtkSlicerInteractiveUKFModuleLogicHierarchy.txt
3&gt;Building Custom Rule C:/pieper/ukftractography/ukf/CMakeLists.txt
5&gt;Copying python Script: InteractiveUKF.py
5&gt;Building Custom Rule C:/pieper/ukftractography/InteractiveUKF/UI/CMakeLists.txt
8&gt;------ Build started: Project: CompileInteractiveUKFPythonFiles, Configuration: Debug x64 ------
6&gt;Configuring: AdditionalLauncherSettings.ini
6&gt;Building Custom Rule C:/pieper/ukftractography/CMakeLists.txt
2&gt;Cloning into 'Eigen'...
7&gt;Configuring application launcher: SlicerWithUKFTractography
8&gt;Compiling python scripts: InteractiveUKF
7&gt;Building Custom Rule C:/pieper/ukftractography/CMakeLists.txt
8&gt;Compiling C:/pieper/ukftractography-build/lib/Slicer-4.11/qt-scripted-modules/InteractiveUKF.py ...
8&gt;Building Custom Rule C:/pieper/ukftractography/InteractiveUKF/UI/CMakeLists.txt
4&gt;Building Custom Rule C:/pieper/ukftractography/InteractiveUKF/Logic/CMakeLists.txt
2&gt;Note: checking out '3.3.7'.
2&gt;
2&gt;You are in 'detached HEAD' state. You can look around, make experimental
2&gt;changes and commit them, and you can discard any commits you make in this
2&gt;state without impacting any branches by performing another checkout.
2&gt;
2&gt;If you want to create a new branch to retain commits you create, you may
2&gt;do so (now or later) by using -b with the checkout command again. Example:
2&gt;
2&gt;  git checkout -b &lt;new-branch-name&gt;
2&gt;
2&gt;HEAD is now at cf794d3... bump to 3.3.7
2&gt;Performing update step for 'UKF-Eigen'
2&gt;No patch step for 'UKF-Eigen'
2&gt;No configure step for 'UKF-Eigen'
2&gt;No build step for 'UKF-Eigen'
2&gt;No install step for 'UKF-Eigen'
2&gt;Completed 'UKF-Eigen'
2&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(231,5): warning MSB8064: Custom build for item "C:\pieper\ukftractography-build\CMakeFiles\a5211e23d24912afe631421c4a932b9f\UKF-Eigen-configure.rule" succeeded, but specified dependency "c:\pieper\ukftractography-build\ukf-eigen-prefix\src\ukf-eigen-stamp\debug\ukf-eigen-update" does not exist. This may cause incremental build to work incorrectly.
2&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\MSBuild\Microsoft\VC\v160\Microsoft.CppCommon.targets(231,5): warning MSB8064: Custom build for item "C:\pieper\ukftractography-build\CMakeFiles\bed4b501aa27d504470e64d79786f98a\UKF-Eigen-complete.rule" succeeded, but specified dependency "c:\pieper\ukftractography-build\ukf-eigen-prefix\src\ukf-eigen-stamp\debug\ukf-eigen-update" does not exist. This may cause incremental build to work incorrectly.
2&gt;Done building project "UKF-Eigen.vcxproj".
9&gt;------ Build started: Project: UKFBase, Configuration: Debug x64 ------
9&gt;Generating git_version.cc
9&gt;Generating UKFTractographyCLP.h
9&gt;Building Custom Rule C:/pieper/ukftractography/ukf/CMakeLists.txt
9&gt;GenerateCLP --InputXML C:/pieper/ukftractography/UKFTractography/UKFTractography.xml --OutputCxx C:/pieper/ukftractography-build/ukf/UKFTractographyCLP.h
9&gt;GenerateCLP: Found 6 parameters groups
9&gt;GenerateCLP: Group "IO" has 5 parameters
9&gt;GenerateCLP: Group "Tractography Options" has 11 parameters
9&gt;GenerateCLP: Group "Tensor Model (default)" has 7 parameters
9&gt;GenerateCLP: Group "NODDI Model" has 6 parameters
9&gt;GenerateCLP: Group "Signal Parameters (Expert Only)" has 1 parameters
9&gt;GenerateCLP: Group "Not Used: Debug/Develop Only" has 12 parameters
9&gt;git_version.cc
9&gt;BRAINSThreadControl.cxx
9&gt;utilities.cc
9&gt;C:\pieper\ukftractography\ukf\utilities.cc(866,9): warning C4244: 'argument': conversion from 'ukfPrecisionType' to 'Eigen::EigenBase&lt;Derived&gt;::Index', possible loss of data
9&gt;        with
9&gt;        [
9&gt;            Derived=Eigen::Matrix&lt;double,-1,1,0,-1,1&gt;
9&gt;        ]
9&gt;cli.cc
9&gt;tractography.cc
9&gt;unscented_kalman_filter.cc
9&gt;seed.cc
9&gt;ukffiber.cc
9&gt;NrrdData.cc
9&gt;vtk_writer.cc
9&gt;dwi_normalize.cc
9&gt;thread.cc
9&gt;QuadProg++_Eigen.cc
9&gt;filter_model.cc
9&gt;filter_Full1T.cc
9&gt;filter_Full1T_FW.cc
9&gt;filter_Full2T.cc
9&gt;filter_Full2T_FW.cc
9&gt;filter_Full3T.cc
9&gt;filter_NODDI1F.cc
9&gt;Generating Code...
9&gt;Compiling...
9&gt;filter_NODDI2F.cc
9&gt;filter_Simple1T.cc
9&gt;filter_Simple1T_FW.cc
9&gt;filter_Simple2T.cc
9&gt;filter_Simple2T_FW.cc
9&gt;filter_Simple3T.cc
9&gt;Generating Code...
9&gt;Auto build dll exports
9&gt;   Creating library C:/pieper/ukftractography-build/lib/Debug/UKFBase.lib and object C:/pieper/ukftractography-build/lib/Debug/UKFBase.exp
9&gt;UKFBase.vcxproj -&gt; C:\pieper\ukftractography-build\bin\Debug\UKFBase.dll
9&gt;Done building project "UKFBase.vcxproj".
10&gt;------ Build started: Project: UKFTractographyLib, Configuration: Debug x64 ------
11&gt;------ Build started: Project: vtkSlicerInteractiveUKFModuleLogic, Configuration: Debug x64 ------
12&gt;------ Build started: Project: ConvertVTKLib, Configuration: Debug x64 ------
11&gt;For vtkSlicerInteractiveUKFModuleLogic - updating vtkSlicerInteractiveUKFModuleLogicHierarchy.txt
10&gt;Generating UKFTractographyCLP.h
12&gt;Generating ConvertVTKCLP.h
10&gt;Building Custom Rule C:/pieper/ukftractography/UKFTractography/CMakeLists.txt
10&gt;GenerateCLP --InputXML C:/pieper/ukftractography/UKFTractography/UKFTractography.xml --OutputCxx C:/pieper/ukftractography-build/UKFTractography/UKFTractographyCLP.h
12&gt;Building Custom Rule C:/pieper/ukftractography/UKFTractography/CMakeLists.txt
12&gt;GenerateCLP --InputXML C:/pieper/ukftractography/UKFTractography/ConvertVTK.xml --OutputCxx C:/pieper/ukftractography-build/UKFTractography/ConvertVTKCLP.h
12&gt;GenerateCLP: Found 1 parameters groups
12&gt;GenerateCLP: Group "" has 4 parameters
10&gt;GenerateCLP: Found 6 parameters groups
10&gt;GenerateCLP: Group "IO" has 5 parameters
10&gt;GenerateCLP: Group "Tractography Options" has 11 parameters
10&gt;GenerateCLP: Group "Tensor Model (default)" has 7 parameters
10&gt;GenerateCLP: Group "NODDI Model" has 6 parameters
10&gt;GenerateCLP: Group "Signal Parameters (Expert Only)" has 1 parameters
10&gt;GenerateCLP: Group "Not Used: Debug/Develop Only" has 12 parameters
12&gt;ConvertVTK.cxx
10&gt;UKFTractography.cxx
12&gt;C:\sq5\JsonCpp\include\json\value.h(53,50): warning C4275: non dll-interface class 'std::exception' used as base for dll-interface class 'Json::Exception'
12&gt;C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.26.28801\include\vcruntime_exception.h(48): message : see declaration of 'std::exception'
12&gt;C:\sq5\JsonCpp\include\json\value.h(53): message : see declaration of 'Json::Exception'
12&gt;C:\sq5\JsonCpp\include\json\reader.h(249,63): warning C4275: non dll-interface class 'Json::CharReader::Factory' used as base for dll-interface class 'Json::CharReaderBuilder'
12&gt;C:\sq5\JsonCpp\include\json\reader.h(227): message : see declaration of 'Json::CharReader::Factory'
12&gt;C:\sq5\JsonCpp\include\json\reader.h(249): message : see declaration of 'Json::CharReaderBuilder'
11&gt;Building Custom Rule C:/pieper/ukftractography/InteractiveUKF/Logic/CMakeLists.txt
11&gt;vtkSlicerInteractiveUKFLogic.cxx
12&gt;ConvertVTKLib.vcxproj -&gt; C:\pieper\ukftractography-build\lib\Slicer-4.11\cli-modules\Debug\ConvertVTKLib.lib
12&gt;Done building project "ConvertVTKLib.vcxproj".
13&gt;------ Build started: Project: ConvertVTK, Configuration: Debug x64 ------
13&gt;Building Custom Rule C:/pieper/ukftractography/UKFTractography/CMakeLists.txt
13&gt;SEMCommandLineLibraryWrapper.cxx
13&gt;   Creating library C:/pieper/ukftractography-build/lib/Slicer-4.11/cli-modules/Debug/ConvertVTK.lib and object C:/pieper/ukftractography-build/lib/Slicer-4.11/cli-modules/Debug/ConvertVTK.exp
13&gt;ConvertVTK.vcxproj -&gt; C:\pieper\ukftractography-build\lib\Slicer-4.11\cli-modules\Debug\ConvertVTK.exe
13&gt;Copying XML file 'ConvertVTK.xml' along side the executable
10&gt;UKFTractographyLib.vcxproj -&gt; C:\pieper\ukftractography-build\lib\Slicer-4.11\cli-modules\Debug\UKFTractographyLib.lib
14&gt;------ Build started: Project: UKFTractography, Configuration: Debug x64 ------
14&gt;Building Custom Rule C:/pieper/ukftractography/UKFTractography/CMakeLists.txt
14&gt;SEMCommandLineLibraryWrapper.cxx
14&gt;UKFTractography.vcxproj -&gt; C:\pieper\ukftractography-build\lib\Slicer-4.11\cli-modules\Debug\UKFTractography.exe
14&gt;Copying XML file 'UKFTractography.xml' along side the executable
15&gt;------ Build started: Project: UKFTractographyTest, Configuration: Debug x64 ------
15&gt;Building Custom Rule C:/pieper/ukftractography/UKFTractography/Testing/CMakeLists.txt
15&gt;CompareFibers.cc
11&gt;   Creating library C:/pieper/ukftractography-build/lib/Slicer-4.11/qt-loadable-modules/Debug/vtkSlicerInteractiveUKFModuleLogic.lib and object C:/pieper/ukftractography-build/lib/Slicer-4.11/qt-loadable-modules/Debug/vtkSlicerInteractiveUKFModuleLogic.exp
11&gt;vtkSlicerInteractiveUKFModuleLogic.vcxproj -&gt; C:\pieper\ukftractography-build\lib\Slicer-4.11\qt-loadable-modules\Debug\vtkSlicerInteractiveUKFModuleLogic.dll
16&gt;------ Build started: Project: vtkSlicerInteractiveUKFModuleLogicPythonD, Configuration: Debug x64 ------
16&gt;Python Wrapping - generating vtkSlicerInteractiveUKFLogicPython.cxx
15&gt;UKFTractographyTest.vcxproj -&gt; C:\pieper\ukftractography-build\bin\Debug\UKFTractographyTest.exe
16&gt;Python Wrapping - generating vtkSlicerInteractiveUKFModuleLogicPythonInit.cxx
16&gt;Building Custom Rule C:/pieper/ukftractography/InteractiveUKF/Logic/CMakeLists.txt
16&gt;vtkSlicerInteractiveUKFLogicPython.cxx
16&gt;vtkSlicerInteractiveUKFModuleLogicPythonInitImpl.cxx
16&gt;Generating Code...
16&gt;   Creating library C:/pieper/ukftractography-build/lib/Slicer-4.11/qt-loadable-modules/Debug/vtkSlicerInteractiveUKFModuleLogicPythonD.lib and object C:/pieper/ukftractography-build/lib/Slicer-4.11/qt-loadable-modules/Debug/vtkSlicerInteractiveUKFModuleLogicPythonD.exp
16&gt;vtkSlicerInteractiveUKFModuleLogicPythonD.vcxproj -&gt; C:\pieper\ukftractography-build\lib\Slicer-4.11\qt-loadable-modules\Debug\vtkSlicerInteractiveUKFModuleLogicPythonD.dll
17&gt;------ Build started: Project: vtkSlicerInteractiveUKFModuleLogicPython, Configuration: Debug x64 ------
17&gt;Building Custom Rule C:/pieper/ukftractography/InteractiveUKF/Logic/CMakeLists.txt
17&gt;vtkSlicerInteractiveUKFModuleLogicPythonInit.cxx
17&gt;   Creating library C:/pieper/ukftractography-build/lib/Slicer-4.11/qt-loadable-modules/Debug/vtkSlicerInteractiveUKFModuleLogicPython.lib and object C:/pieper/ukftractography-build/lib/Slicer-4.11/qt-loadable-modules/Debug/vtkSlicerInteractiveUKFModuleLogicPython.exp
17&gt;vtkSlicerInteractiveUKFModuleLogicPython.vcxproj -&gt; C:\pieper\ukftractography-build\lib\Slicer-4.11\qt-loadable-modules\Debug\vtkSlicerInteractiveUKFModuleLogicPython.pyd
18&gt;------ Build started: Project: ALL_BUILD, Configuration: Debug x64 ------
18&gt;Building Custom Rule C:/pieper/ukftractography/CMakeLists.txt
========== Build: 18 succeeded, 0 failed, 0 up-to-date, 0 skipped ==========
</code></pre>

---

## Post #17 by @fpsiddiqui91 (2020-07-24 20:21 UTC)

<p>Thank you fro your response <a class="mention" href="/u/pieper">@pieper</a>.</p>
<p>I am also using VS2019, but I am building in release mode. Could you find any solution for this?</p>

---

## Post #18 by @fpsiddiqui91 (2020-07-24 21:22 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>, just an update, After building UKF module, I can run SlicerwithUKFTractography application. In this app, Slicer can actually detect UKF module. However, I cannot load the UKF module in the main slicer app.</p>
<p>I tried importing my own loadable module and its showing the same behaviour. I can load my loadable module with SlicerwithLoadabaleModule app but I cannot load that module in the main slicer app.</p>
<p>Am I missing something?</p>

---

## Post #19 by @pieper (2020-07-24 22:16 UTC)

<p>So you were able to build UKF in release mode?  Did you change anything to fix the json link error?  Let us know and maybe we can fix the extension build too. (Or even better, maybe you make a pull request with a fix?)</p>
<p>Regarding your local build, I suggest setting up the module path manually.  I typically do this on the command line with the <code>--additional-module-paths</code> option from a script so that I can include all the local build paths conveniently for multiple extensions.  But you can also do it in the Modules pane of the Application Settings.</p>

---

## Post #20 by @fpsiddiqui91 (2020-07-24 22:40 UTC)

<p>No, I have not changed anything. I just checked SlicerwithUKFTRacktography and it worked. I can see the UI and widgets of the UKF module but its giving error on fiber generation.</p>
<p>About the local build. Yes I have tried to add module paths in the application setting of the main Slicer exe, but its not working. Its not detecting the UKF module. Maybe I am missing something?</p>
<p>I am following these steps to load the loadable module in Slicer:</p>
<p>" After successfully compiling the Slicer module, the Slicer module executables and libraries are located in your module build directory under lib  <code>build_dir/lib/Slicer-X.Y/module_type</code> . Adding this directory to the Additional module paths in the Application Settings GUI within slicer, will allow testing of your module without recompiling the super-build. Refer to <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/DirectoryStructure" rel="nofollow noopener">Directory Structure</a> description for more details."</p>

---

## Post #21 by @fpsiddiqui91 (2020-07-25 12:22 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a>,  I tried to load my own loadable modules, but its not loading in the main slicer app. Maybe I am missing some steps to load the loadable module. I am following the steps suggested above. Do I have to do anything else?</p>

---

## Post #22 by @pieper (2020-07-27 00:41 UTC)

<p><a class="mention" href="/u/fpsiddiqui91">@fpsiddiqui91</a> it looks llike you are doing the right thing, just add those paths pointing to your local build.</p>
<p><a href="https://github.com/pnlbwh/ukftractography/pull/130">I fixed a couple things</a> in the windows build of ukf, but it’s still not quite right I’m afraid.</p>

---

## Post #23 by @fpsiddiqui91 (2020-07-27 08:42 UTC)

<p>Yeah, It worked. I actually have to add  “build_dir/lib/Slicer-X.Y/module_type/Release” Folder.</p>
<p>Regarding UKF. I managed to load the module but unfortunately it’s giving an error of unknown exception.</p>
<pre><code>UKF Tractography command line:

C:/Users/20191382/Documents/Slicer_Extensions/UKF_build3/lib/Slicer-4.11/cli-modules/Release/UKFTractography.exe --dwiFile C:/Users/20191382/AppData/Local/Temp/Slicer/CABHC_vtkMRMLDiffusionWeightedVolumeNodeB.nhdr --seedsFile C:/Users/20191382/AppData/Local/Temp/Slicer/CABHC_vtkMRMLLabelMapVolumeNodeD.nhdr --labels 1 --maskFile C:/Users/20191382/AppData/Local/Temp/Slicer/CABHC_vtkMRMLLabelMapVolumeNodeC.nhdr --tracts C:/Users/20191382/AppData/Local/Temp/Slicer/CABHC_vtkMRMLFiberBundleNodeB.vtp --seedsPerVoxel 1 --seedingThreshold 0.18 --stoppingFA 0.15 --stoppingThreshold 0.1 --numThreads -1 --numTensor 2 --stepLength 0.3 --Qm 0 --recordLength 0.9 --maxHalfFiberLength 250 --recordFA --recordTensors --Ql 0 --Qw 0 --Qkappa 0.01 --Qvic 0.004 --Rs 0 --sigmaSignal 0 --maxBranchingAngle 0 --minBranchingAngle 0 --minGA 10000

UKF Tractography terminated with an unknown exception.</code></pre>

---

## Post #24 by @pieper (2020-07-27 14:33 UTC)

<p>Hmm, for this we may need to go back to the debug build.</p>

---

## Post #25 by @ljod (2020-07-28 13:27 UTC)

<p>Hi Steve and all. I sent an email to ask Yogesh to accept your pull request for UKF.</p>

---

## Post #26 by @pieper (2020-07-28 13:51 UTC)

<p>Thanks <a class="mention" href="/u/ljod">@ljod</a> - there’s still a link error for me on the windows release build.   I hope someone can suggest a fix.</p>

---

## Post #27 by @pieper (2020-07-29 19:59 UTC)

<p>So I believe this is the current state:</p>
<p>UKF is available for Windows today in the preview builds (not 4.10 and it probably won’t be fixable there).</p>
<p>There’s an issue with SlicerDMRI for 4.10 should be working tomorrow (we hope).  DMRI is available for windows and linux for today’s preview,. There was an issue with mac builds last night, but probably an the slightly older version from the download page will work.</p>

---
