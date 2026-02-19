---
topic_id: 32032
title: "Install Extension Module In Built Slicer"
date: 2023-10-04
url: https://discourse.slicer.org/t/32032
---

# Install extension module in built Slicer

**Topic ID**: 32032
**Date**: 2023-10-04
**URL**: https://discourse.slicer.org/t/install-extension-module-in-built-slicer/32032

---

## Post #1 by @park (2023-10-04 12:23 UTC)

<p>Hi all<br>
I’m having trouble installing an extension module in the built Slicer. Here is my situation:</p>
<ul>
<li>
<p>Slicer build was successful.</p>
</li>
<li>
<p>I separately built the source code of the extension module from a Git repository, following the Developer guide for extesion, and it was successful.</p>
</li>
<li>
<p>My current directory structure is as follows:</p>
</li>
</ul>
<pre><code class="lang-auto">C:\D\S                             %slicer source
C:\D\SD                            %slicer build
C:\D\SlicerIGSIO                   %extesion source
C:\D\SlicerIGSIO-D                 %extesion build
C:\D\SlicerIGSIO-D\lib\Slicer-5.5
C:\D\SlicerIGT
C:\D\SlicerIGT-D
C:\D\SlicerOpenIGTLink
C:\D\SlicerOpenIGTLink-D
</code></pre>
<p><strong>In this situation, how can I make Slicer recognize modules like SlicerIGSIO-D,  SlicerIGT-D and ETC ?</strong></p>
<p>*(following option A) I try to find ‘SlicerWithMyExtension’ following the Developer guide for extesion but I can’t</p>
<p>*(following option B) Moreover, I try to add the path to ‘Application setting’ but I could not find ‘qt-scripted-modules’ in ‘C:\D\SlicerIGSIO-D\lib\Slicer-5.5’ instruted in  Developer guide</p>
<p>Should the extension module be included in the Slicer build process, or can it be separately built and then included?</p>

---

## Post #2 by @pieper (2023-10-04 13:49 UTC)

<p>The shell script below is and example of what I use when working with an extension that includes multiple  c++ and python shared and loadable modules.  This is for mac, but something similar should work on windows.</p>
<pre><code class="lang-auto">SLICER_BUILD=/opt/sr/Slicer-build
LIB_PATH=$(pwd)/inner-build/lib/Slicer-5.3

${SLICER_BUILD}/Slicer $* \
  --additional-module-paths \
    ${LIB_PATH}/cli-modules ${LIB_PATH}/qt-loadable-modules ${LIB_PATH}/qt-scripted-modules
</code></pre>

---

## Post #3 by @Sunderlandkyl (2023-10-04 14:53 UTC)

<p>When I am debugging multiple extensions with third-party libraries, I combine the AdditionalLauncherSettings.ini files from each of the extensions into a single one, and launch Slicer/VisualStudio with that file (<code>--launcher-additional-settings GeneratedAdditionalSettings.ini</code>).</p>
<p>I created a python script to combine the files (copied <a href="https://gist.github.com/Sunderlandkyl/f6b5fbf365a4cbf0935e4a89f4f38130" rel="noopener nofollow ugc">here</a>), but you can copy and paste to merge the ini together manually.</p>

---

## Post #4 by @park (2023-10-04 15:33 UTC)

<p>Thank you for kind reply!</p>
<p>Then, is it correct that I need to make the following steps every time I edit the code in the extension module?</p>
<ol>
<li>Edit somthing in extension</li>
<li>build extension</li>
<li>make ini from python</li>
<li>build slicer</li>
</ol>
<p>Am I right ?</p>
<p>If it is right, could I ask about your development environment? (e.g., cmake, vscode or visual studio)</p>
<p>I try to use vscode because it it easy to make settings.json for cmake and running python</p>

---

## Post #5 by @Sunderlandkyl (2023-10-04 15:41 UTC)

<p>You shouldn’t need to rebuild Slicer if you’re only editing the extension.</p>
<p>The ini also probably won’t need to be changed unless you</p>
<ul>
<li>a) Add a new extension that you want to use.<br>
or</li>
<li>b) Modify the inclusion of ThirdParty libraries of an extension in CMake.</li>
</ul>
<p>I use CMake and Visual Studio for compiling Slicer on Windows (see <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/windows.html" class="inline-onebox" rel="noopener nofollow ugc">Windows — 3D Slicer documentation</a>).</p>

---

## Post #6 by @park (2023-10-05 02:04 UTC)

<p>I am sorry for such a basic question.</p>
<p>I made .ini file follow your python code it is amazing !!</p>
<p>Then, I try to do command like this</p>
<pre><code class="lang-auto">C:\D\SD\Slicer-build&gt;Slicer.exe --VisualStudio --launcher-additional-settings C:\D\SD\GeneratedSuperAdditionalLauncherSettings.ini
</code></pre>
<p>Is this right ?<br>
After the visual studio come up I try to build slicer then, turn on it again<br>
but I cannot find any changes …</p>

---

## Post #7 by @park (2023-10-05 07:52 UTC)

<p>Hi Kyle Sunderland<br>
I tried this also</p>
<pre><code class="lang-auto">C:\D\SD\Slicer-build&gt;slicer --launcher-additional-settings C:\D\S\GeneratedSuperAdditionalLauncherSettings.ini
</code></pre>
<p>There is no error but nothing was changed , I cannot find extension modules in my slicer.</p>
<p>This is my .ini file. Is there something wrong ?</p>
<pre><code class="lang-auto">[General]
additionalpathvariables = PYTHONPATH

[LibraryPaths]
1\path = C:/D/SlicerIGSIO-D/inner-build/lib/Slicer-5.5/cli-modules/Debug
2\path = C:/D/SlicerIGSIO-D/inner-build/lib/Slicer-5.5/qt-loadable-modules/Debug
3\path = C:/D/SlicerIGSIO-D/lib/Slicer-5.5/Debug
4\path = C:/D/SlicerOpenIGTLink-D/inner-build/lib/Slicer-5.5/cli-modules/Debug
5\path = C:/D/SlicerOpenIGTLink-D/inner-build/lib/Slicer-5.5/qt-loadable-modules/Debug
6\path = C:/D/SlicerOpenIGTLink-D/lib/Slicer-5.5/Debug
7\path = C:/D/SlicerOpenIGTLink-D/OpenIGTLink-buildC:/D/SlicerOpenIGTLink-D/OpenIGTLink-build/bin/DebugC:/D/SlicerOpenIGTLink-D/binC:/D/SlicerOpenIGTLink-D/bin/Debug
8\path = C:/D/SlicerOpenIGTLink-D/OpenIGTLinkIO-buildC:/D/SlicerOpenIGTLink-D/OpenIGTLinkIO-build/bin/DebugC:/D/SlicerOpenIGTLink-D/binC:/D/SlicerOpenIGTLink-D/bin/Debug
size = 8

[Paths]
1\path = C:/D/SlicerIGSIO-D/inner-build/lib/Slicer-5.5/cli-modules/Debug
2\path = C:/D/SlicerIGSIO-D/inner-build/bin/Debug
3\path = C:/D/SlicerIGSIO-D/bin/Debug
4\path = C:/D/SlicerIGSIO-D/VP9/
5\path = C:/D/SlicerOpenIGTLink-D/inner-build/lib/Slicer-5.5/cli-modules/Debug
6\path = C:/D/SlicerOpenIGTLink-D/inner-build/bin/Debug
7\path = C:/D/SlicerOpenIGTLink-D/bin/Debug
size = 7

[EnvironmentVariables]

[PYTHONPATH]
1\path = C:/D/SlicerIGSIO-D/inner-build/lib/Slicer-5.5/qt-scripted-modules
2\path = C:/D/SlicerIGSIO-D/inner-build/lib/Slicer-5.5/qt-loadable-modules/Debug
3\path = C:/D/SlicerIGSIO-D/inner-build/lib/Slicer-5.5/qt-loadable-modules/Python
4\path = C:/D/SlicerIGSIO-D/lib/Slicer-5.5/Debug
5\path = C:/D/SlicerOpenIGTLink-D/inner-build/lib/Slicer-5.5/qt-scripted-modules
6\path = C:/D/SlicerOpenIGTLink-D/inner-build/lib/Slicer-5.5/qt-loadable-modules/Debug
7\path = C:/D/SlicerOpenIGTLink-D/inner-build/lib/Slicer-5.5/qt-loadable-modules/Python
8\path = C:/D/SlicerOpenIGTLink-D/lib/Slicer-5.5/Debug
size = 8

</code></pre>

---

## Post #8 by @Sunderlandkyl (2023-10-05 14:00 UTC)

<p>You also still need to include <code>--additional-module-paths</code> when launching Slicer, pointing to the qt-loadable-modules/Debug, qt-scripted-modules and cli-modules/Debug for each of the extensions.</p>

---

## Post #9 by @park (2023-10-05 16:11 UTC)

<p>You mean… in commend line?</p>
<p>I really appreciate if you provide to me the example of your commend line and .ini<br>
Then I can follow you</p>

---

## Post #10 by @Sunderlandkyl (2023-10-05 16:21 UTC)

<p>Yes, in command line, something like:</p>
<pre><code class="lang-auto">"C:/d/s/S4W/Slicer-build/Slicer.exe" --launcher-additional-settings "C:d/s/GeneratedSuperAdditionalLauncherSettings.ini --additional-module-paths "C:\d\s\SIGSIOW\inner-build\lib\Slicer-5.5\qt-loadable-modules\RelWithDebInfo" "C:\d\s\SOIGTLW\inner-build\lib\Slicer-5.5\qt-loadable-modules\RelWithDebInfo" "C:\d\s\SOIGTLW\inner-build\lib\Slicer-5.5\qt-scripted-modules" "C:\d\s\SIGTW\lib\Slicer-5.5\qt-loadable-modules\RelWithDebInfo" "C:\d\s\SIGTW\lib\Slicer-5.5\qt-scripted-modules"
</code></pre>

---

## Post #11 by @park (2023-10-07 02:53 UTC)

<p>Thank you Kyle !</p>
<p>I sovled the problem!</p>
<p>Then I made a python code the to run Slicer with .ini setting<br>
automatically consider additional path setting</p>
<pre><code class="lang-auto">import subprocess
import configparser

paths = []
config = configparser.ConfigParser()
config.read('C:/D3/S/GeneratedSuperAdditionalLauncherSettings.ini')

# Check if the 'Paths' section exists in the INI file
if 'Paths' in config:
    paths_section = config['PYTHONPATH']

    # Get all the keys in the 'Paths' section
    path_keys = paths_section.keys()

    # Iterate through the keys and print the corresponding values
    for key in path_keys:
        if key != 'size':  # Exclude the 'size' key
            path_value = paths_section[key]
            paths.append(path_value)

command = [
    "C:/D3/SR/Slicer-build/Slicer.exe",
    
    "--launcher-additional-settings",
    "C:/D3/S/GeneratedSuperAdditionalLauncherSettings.ini",
    
    "--additional-module-paths",
]+paths

subprocess.run(command)
</code></pre>

---
