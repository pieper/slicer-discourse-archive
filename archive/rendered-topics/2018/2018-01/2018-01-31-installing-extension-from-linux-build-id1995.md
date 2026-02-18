# Installing extension from Linux build

**Topic ID**: 1995
**Date**: 2018-01-31
**URL**: https://discourse.slicer.org/t/installing-extension-from-linux-build/1995

---

## Post #1 by @dlevitas (2018-01-31 22:04 UTC)

<p>Hello,</p>
<p>I recently switched from Mac to Linux, so I downloaded the stable Linux release (4.8.1). I’m not as familiar with Linux, so I don’t know how to add extensions. With the Mac version I could load the GUI and do it that way, but I’m having trouble getting the SwissSkullStripping tool on the Linux build.</p>
<p>Thank you for the assistance.</p>
<p>Dan</p>

---

## Post #2 by @pieper (2018-02-01 00:05 UTC)

<p>The extension interface should be the same on mac/linux.  4.8.1 extensions look good to me…</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b809748f7950f31549571dd582e15b5e019f8463.jpeg" data-download-href="/uploads/short-url/qg46Yn7yMBYojUtO9N1t4BoTGgP.jpg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b809748f7950f31549571dd582e15b5e019f8463_2_690x424.jpg" alt="image" data-base62-sha1="qg46Yn7yMBYojUtO9N1t4BoTGgP" width="690" height="424" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b809748f7950f31549571dd582e15b5e019f8463_2_690x424.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b809748f7950f31549571dd582e15b5e019f8463_2_1035x636.jpg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b809748f7950f31549571dd582e15b5e019f8463_2_1380x848.jpg 2x" data-dominant-color="C5C7CD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1866×1148 624 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @dlevitas (2018-02-01 02:20 UTC)

<p>Oh, okay, I was now able to run the GUI and install the SwissSkullStripper extension. I added this to my path, but when I went to run SwissSkullStripper on the command line, I received the following error:</p>
<pre><code>SwissSkullStripper: error while loading shared libraries: libSwissSkullStripperLib.so: cannot open shared object file: No such file or directory
</code></pre>
<p>This is what I tried on the command line:</p>
<pre><code>SwissSkullStripper --atlasMRI atlas_with_skull.nii.gz --atlasMask atlas_no_skull_mask.nii.gz input_data.nii.gz output_brain_no_skull.nii.gz output_mask_no_skull.nii.gz
</code></pre>
<p>And this is where I’m calling it from:<br>
<code>export PATH="/.config/NA-MIC/Extensions-26813/SwissSkullStripper/lib/Slicer-4.8/cli-modules/:$PATH"</code></p>
<p>Is there some step I’m missing that’s causing the error?</p>

---

## Post #4 by @dlevitas (2018-02-01 03:00 UTC)

<p>Actually, never-mind. I changed my LD_LIBRARY_PATH variable, and that seemed to solve the issue.</p>

---

## Post #5 by @lassoan (2018-02-01 04:20 UTC)

<p>To run a CLI module outside Slicer, you need to use the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Launcher">launcher</a>, which sets up all necessary shared library paths. Something similar to this should work (you might need to specify full or relative path for the module executable):</p>
<pre><code>Slicer --launch SwissSkullStripper --atlasMRI atlas_with_skull.nii.gz --atlasMask atlas_no_skull_mask.nii.gz input_data.nii.gz output_brain_no_skull.nii.gz output_mask_no_skull.nii.gz</code></pre>

---

## Post #6 by @michalikthomas (2019-04-26 09:18 UTC)

<p>I am trying to install manually a packaged CLI c++ extension, as described here <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_manually_install_an_extension_package.3F" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#How_to_manually_install_an_extension_package.3F</a> , but I am getting the same error as <a class="mention" href="/u/dlevitas">@dlevitas</a>. The issue is “resolved” when I set LD_LIBRARY_PATH to the extension path. Why it behaves like this? Is there any other how to fully manually install a packaged extension without setting this environment variable?</p>

---

## Post #7 by @lassoan (2019-04-26 12:36 UTC)

<p>Do you have problems running CLI modules from the command-line or modules do not show up in Slicer?</p>

---

## Post #8 by @michalikthomas (2019-04-26 12:51 UTC)

<p>I am calling CLI module from another scripted module, but without setting that LD_LIBRARY_PATH the CLI module is not loaded (the command line, during Slicer app startup, displays the same error message as in <a class="mention" href="/u/dlevitas">@dlevitas</a> case - error while loading shared libraries )</p>

---

## Post #9 by @lassoan (2019-04-26 12:58 UTC)

<p>Could you please try with latest stable and nightly versions as well?</p>
<p>Have you downloaded the extension package from the Slicer appstore or you have built it yourself?</p>
<p>Does it work well with online installation (downloading and installing directly from the extension manager)?</p>

---

## Post #10 by @michalikthomas (2019-04-26 15:06 UTC)

<p>I have tried to run it with the latest stable and nightly versions but the result is still the same.<br>
FIX: The error message does not show up during Slicer startup but when the CLI module is called.</p>
<p>The error message is following:</p>
<pre><code>/path.../Slicer4101/TestExtension- packaged/7d48c57-linux-amd64-TestExtension-local0-0000-00-00/lib/Slicer-4.10/cli-modules/TestCLIModule: error while loading shared libraries: libTestCLIModuleLib.so: cannot open shared object file: No such file or directory
</code></pre>
<p>I am trying to install CLI module which I am implementing myself. It is built using <a href="https://github.com/Slicer/SlicerBuildEnvironment" rel="nofollow noopener">https://github.com/Slicer/SlicerBuildEnvironment</a> exactly <code>slicer/buildenv-qt5-centos7:slicer-4.10</code> with the following cmake parameters:</p>
<pre><code>sudo ~/bin/slicer-buildenv-qt5-centos7-slicer-4.10 cmake \
  -BSlicer-build -HSlicer \
  -GNinja \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DSlicer_USE_PYTHONQT_WITH_TCL:BOOL=OFF \
  -DSlicer_BUILD_CLI:BOOL=OFF \
  -DSlicer_USE_SimpleITK:BOOL=OFF \
  -DBUILD_TESTING:BOOL=OFF \
  -DQt5_DIR:PATH=./Qt5
</code></pre>
<p>(side note, offtopic: I was not sure about how to set Qt5 path properly inside docker container, so I used locally installed Qt5)</p>
<p>I tried to download and install randomly selected extension from extension manager (SwissSkullStripper) and everything works all fine, but I don’t know which type module it is so it maybe does not prove anything.</p>

---

## Post #11 by @lassoan (2019-04-26 15:30 UTC)

<aside class="quote no-group" data-username="michalikthomas" data-post="10" data-topic="1995">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/7cd45c/48.png" class="avatar"> michalikthomas:</div>
<blockquote>
<p>I tried to download and install randomly selected extension from extension manager (SwissSkullStripper) and everything works all fine,</p>
</blockquote>
</aside>
<p>Compare the zip file that you download from the appstore with the zip file that you generate. Are there any differences in the directory structure, file names, or content of non-binary files?</p>
<p>You can find examples of docker images that include some additional extensions: <a href="https://github.com/pieper/SlicerDockers" class="inline-onebox">GitHub - pieper/SlicerDockers: docker config files for slicer</a></p>
<p>If you want to build a custom Slicer package that comes with a few bundled extensions then it may be better to build a <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate">custom application</a>.</p>

---

## Post #12 by @michalikthomas (2019-04-26 16:46 UTC)

<p>I am not sure how to download an extension from the extension manager directly - to get the zip file. But checking the module import paths in the application settings it looks it is probably the same as the one I built and packaged.</p>
<p>SwissSkullStripper CLI module import path:</p>
<pre><code>~/.config/NA-MIC/Extensions-27931/SwissSkullStripper/lib/Slicer-4.10/cli-modules
</code></pre>
<p>My custom CLI module import path:</p>
<pre><code>.../lib/Slicer-4.10/cli-modules
</code></pre>
<p>And the content looks, in my eyes, very much the same:</p>
<pre><code>-rwxr-xr-x 1 usrname 1792320 dub 26 00:26 libTestCLIModuleLib.so
-rwxr-xr-x 1 usrname   12800 dub 26 00:26 TestCLIModule
-rw-r--r-- 1 usrname    2262 dub 26 00:15 TestCLIModule.xml
</code></pre>
<p>Note, the module seems to be registered - it is present in <code>slicer.modules.MODULE_NAME</code> and when calling the CLI module cmd output include lines “TestCLIModule standard error:” then the error message I posted earlier, and finally “TestCLIModule completed with errors” afterward.</p>
<p>Anyway, thanks for providing links to custom Slicer package creation. But, it this case, if there is any other working way I would prefer distributing the modules separately.</p>

---

## Post #13 by @lassoan (2019-04-26 17:27 UTC)

<aside class="quote no-group" data-username="michalikthomas" data-post="12" data-topic="1995">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/7cd45c/48.png" class="avatar"> michalikthomas:</div>
<blockquote>
<p>I am not sure how to download an extension from the extension manager directly - to get the zip file</p>
</blockquote>
</aside>
<p>Open this URL: <a href="http://slicer.kitware.com/midas3/slicerappstore?os=linux&amp;arch=amd64&amp;revision=27931" class="inline-onebox">@KitwareMedical/slicer-extensions-webapp</a> (replacing revision as needed) then click Download. It is very important to know if there are any differences, even very small differences (4.10 vs 4.11) may break things.</p>
<aside class="quote no-group" data-username="michalikthomas" data-post="12" data-topic="1995">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/7cd45c/48.png" class="avatar"> michalikthomas:</div>
<blockquote>
<p>if there is any other working way I would prefer distributing the modules separately.</p>
</blockquote>
</aside>
<p>I don’t think you can reliably distribute modules separately (to be used with Slicer executable that someone else creates) due to potential ABI incompatibility issues.</p>

---

## Post #14 by @michalikthomas (2019-04-26 17:49 UTC)

<p>Checking the extension structure for specific revision no and the folder structure and files still look similar.</p>
<p>SwissSkullStripper</p>
<pre><code>./27931-linux-amd64-SwissSkullStripper-git317d74d-2018-01-22
├── lib
│   └── Slicer-4.10
│       ├── cli-modules
│       │   ├── libSwissSkullStripperLib.so
│       │   ├── SwissSkullStripper
│       │   ├── SwissSkullStripperDefaultAtlas
│       │   │   ├── atlasImage.mha
│       │   │   └── atlasMask.mha
│       │   └── SwissSkullStripper.xml
│       └── qt-scripted-modules
│           ├── Resources
│           │   └── Icons
│           │       ├── AtlasImage.png
│           │       └── AtlasMask.png
│           ├── SwissSkullStripperSampleData.py
│           └── SwissSkullStripperSampleData.pyc
└── share
    └── Slicer-4.10
        └── SwissSkullStripper.s4ext
</code></pre>
<p>My custom CLI module</p>
<pre><code>./7d48c57-linux-amd64-TestExtension-local0-0000-00-00
├── lib
│   └── Slicer-4.10
│       └── cli-modules
│           ├── libTestCLIModuleLib.so
│           ├── TestCLIModule
│           └── TestCLIModule.xml
└── share
    └── Slicer-4.10
        └── TestExtension.s4ext
</code></pre>
<p>Speaking about possible ABI compatibility issues, I thought that it can be overcome using Docker predefined images - if they are the same as used for official builds.</p>

---
