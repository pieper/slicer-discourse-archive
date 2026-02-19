---
topic_id: 21933
title: "Problems To Build 3Dslicer In Ubuntu 20 04"
date: 2022-02-12
url: https://discourse.slicer.org/t/21933
---

# Problems to build 3DSlicer in Ubuntu 20.04

**Topic ID**: 21933
**Date**: 2022-02-12
**URL**: https://discourse.slicer.org/t/problems-to-build-3dslicer-in-ubuntu-20-04/21933

---

## Post #1 by @shahrokh (2022-02-12 12:04 UTC)

<p>Hello</p>
<p>Dear Developers and Users<br>
I want to build Slicer on Ubuntu 20.04 as mentioned in “<a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html" rel="noopener nofollow ugc">GNU/Linux systems — 3D Slicer documentation</a>”.</p>
<p>My system</p>
<pre><code class="lang-auto">sn@sn:~$ uname --all
Linux sn 5.13.0-28-generic #31~20.04.1-Ubuntu SMP Wed Jan 19 14:08:10 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
sn@sn:~$
</code></pre>
<p>Firstly I installed Ubuntu 20.04 and then other packages as mentioned below:</p>
<pre><code class="lang-auto">sn@sn:~$ sudo apt update
...
sn@sn:~$ sudo apt install git
…
sn@sn:~$ sudo apt install subversion
…
sn@sn:~$ sudo apt install build-essential
…
sn@sn:~$ sudo apt install cmake
…
</code></pre>
<p>I installed Qt as mentioned in “<a href="https://www.qt.io/download-qt-installer" rel="noopener nofollow ugc">Download Qt: Get Qt Online Installer</a>”, I execute the following commands:</p>
<pre><code class="lang-auto">sn@sn:~$ mkdir QtInstaller
sn@sn:~$ cp ~/Downloads/qt-unified-linux-x64-4.2.0-online.run ./QtInstaller/
sn@sn:~/QtInstaller$ chmod a+x qt-unified-linux-x64-4.2.0-online.run
sn@sn:~/QtInstaller$ ./qt-unified-linux-x64-4.2.0-online.run
…
</code></pre>
<p>I click next and select default options.</p>
<pre><code class="lang-auto">sn@sn:~/QtInstaller$ ll -h /home/sn/Qt
total 30M
drwxr-xr-x 6 sn sn 4.0K Feb 9 17:22 ./
drwxr-xr-x 21 sn sn 4.0K Feb 9 16:46 ../
-rw-r--r-- 1 sn sn 4.7K Feb 9 17:22 components.xml
drwxrwxr-x 2 sn sn 4.0K Feb 9 17:21 dist/
-rw-r--r-- 1 sn sn 46K Feb 9 17:22 InstallationLog.txt
-rw-r--r-- 1 sn sn 48 Feb 9 17:22 installer.dat
drwxr-xr-x 8 sn sn 4.0K Feb 9 17:22 installerResources/
drwxr-xr-x 2 sn sn 4.0K Feb 9 17:22 Licenses/
-rwxr-xr-x 1 sn sn 30M Feb 9 17:22 MaintenanceTool*
-rw-r--r-- 1 sn sn 510K Feb 9 17:22 MaintenanceTool.dat
-rw-r--r-- 1 sn sn 7.0K Feb 9 17:22 MaintenanceTool.ini
-rw-r--r-- 1 sn sn 362 Feb 9 17:22 network.xml
drwxrwxr-x 6 sn sn 4.0K Feb 9 17:22 Tools/
sn@sn:~/QtInstaller$
</code></pre>
<p>I found an easier way. I found instructions on installing libraries on the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/linux.html" rel="noopener nofollow ugc">building Slicer</a>:</p>
<p><code>sn@sn:~$ sudo apt update &amp;&amp; sudo apt install git subversion build-essential cmake cmake-curses-gui cmake-qt-gui \  qt5-default qtmultimedia5-dev qttools5-dev libqt5xmlpatterns5-dev libqt5svg5-dev qtwebengine5-dev qtscript5-dev \  qtbase5-private-dev libqt5x11extras5-dev libxt-dev</code></p>
<p>After doing it (the installation of the development tools and the support libraries), I enter the following commands:</p>
<pre><code class="lang-auto">sn@sn:~$ git clone https://github.com/Slicer/Slicer.git
...
sn@sn:~$ cd Slicer
sn@sn:~/Slicer$ ./Utilities/SetupForDevelopment.sh
Checking basic user information...
Please enter your full name, such as 'John Doe': Shahrokh Nasseri
Setting name to 'Shahrokh Nasseri'
Please enter your email address, such as 'john@email.com': naserish@mums.ac.ir
Setting email address to 'naserish@mums.ac.ir'
Your commits will have the following author:
Shahrokh Nasseri &lt;naserish@mums.ac.ir&gt;
Is the author name and email address above correct? [Y/n] Y
Setting up git hooks...
Initialized empty Git repository in /home/sn/Slicer/.git/hooks/.git/
Pulling the hooks...
Done.
Suggesting git tips...

You may want to enable color output from Git commands with
git config --global color.ui auto
A dynamic, informative Git shell prompt can be obtained by sourcing the git
bash-completion script in your ~/.bashrc. Set the PS1 environmental variable as
suggested in the comments at the top of the bash-completion script. You may
need to install the bash-completion package from your distribution to obtain the
script.
A merge tool can be configured with
git config merge.tool &lt;toolname&gt;
For more information, see
git help mergetool
Done.

sn@sn:~/Slicer$ git config --global color.ui auto
sn@sn:~/Slicer$ cd ..
sn@sn:~$ mkdir Slicer-SuperBuild-Debug
sn@sn:~$ cd Slicer-SuperBuild-Debug
sn@sn:~/Slicer-SuperBuild-Debug$ cmake ../Slicer
...
-- SuperBuild - Slicer[OK]
-- Configuring done
-- Generating done
-- Build files have been written to: /home/sn/Slicer-SuperBuild-Debug
sn@sn:~/Slicer-SuperBuild-Debug$ cmake -DCMAKE_BUILD_TYPE:STRING=Release ../Slicer
...
-- SuperBuild - python-extension-manager-ssl-requirements[OK]
-- SuperBuild - JsonCpp[OK]
-- SuperBuild - Slicer[OK]
-- Configuring done
-- Generating done
-- Build files have been written to: /home/sn/Slicer-SuperBuild-Debug
sn@sn:~/Slicer-SuperBuild-Debug$ make -j2
...
[ 99%] Linking CXX shared library ../../../../lib/libITKReview-5.2.so
[ 99%] Built target ITKReview
[ 99%] Built target ITKReview-all
[ 99%] Built target ITKSuperPixel-all
[100%] Linking CXX shared library ../../../../lib/libITKTestKernel-5.2.so
[100%] Built target ITKTestKernel
[100%] Linking CXX executable ../../../../bin/itkTestDriver
/usr/bin/ld: ../../../../lib/libITKTestKernel-5.2.so.1: undefined reference to `itk::FreeSurferBinaryMeshIOFactory::FreeSurferBinaryMeshIOFactory()'
/usr/bin/ld: ../../../../lib/libITKTestKernel-5.2.so.1: undefined reference to `itk::FreeSurferAsciiMeshIOFactory::FreeSurferAsciiMeshIOFactory()'
/usr/bin/ld: ../../../../lib/libITKTestKernel-5.2.so.1: undefined reference to `itk::BYUMeshIOFactory::BYUMeshIOFactory()'
collect2: error: ld returned 1 exit status
make[5]: *** [Modules/Core/TestKernel/src/CMakeFiles/itkTestDriver.dir/build.make:115: bin/itkTestDriver] Error 1

make[4]: *** [CMakeFiles/Makefile2:14326: Modules/Core/TestKernel/src/CMakeFiles/itkTestDriver.dir/all] Error 2
make[3]: *** [Makefile:152: all] Error 2
make[2]: *** [CMakeFiles/ITK.dir/build.make:116: ITK-prefix/src/ITK-stamp/ITK-build] Error 2
make[1]: *** [CMakeFiles/Makefile2:1404: CMakeFiles/ITK.dir/all] Error 2
make: *** [Makefile:95: all] Error 2

sn@sn:~/Slicer-SuperBuild-Debug$
</code></pre>
<p>As seen above, I get error during Built target ITKTestKernel.<br>
Please guide me to solve it.<br>
Best regards.</p>
<p>Shahrokh</p>

---

## Post #2 by @chir.set (2022-02-12 16:15 UTC)

<p>It seems the ITK <em>test</em> binaries are looking for FreeSurfer in vain.</p>
<p>You may disable testing in the configure step :</p>
<p><code>cmake -DBUILD_TESTING:BOOL=OFF -DCMAKE_BUILD_TYPE:STRING=Release ../Slicer</code></p>
<p>Hint : if you use <em>ccmake</em> instead of <em>cmake</em>, you’ll have finer control over available options.</p>

---

## Post #3 by @shahrokh (2022-02-14 05:15 UTC)

<p>Thank you for your guidance.</p>
<p>With your command, I get again the same error. Then I built directly ITK (cd /home/sn/Slicer-SuperBuild-Debug/ITK-build &amp;&amp; make clean &amp;&amp; cmake …/ITK &amp;&amp; make) and repeated the build steps in 3DSlicer. I did not get error message during building ITK.</p>
<p>Of course, your guidance seems to be logical and correct. My problem was solved at this step.</p>
<p>Thanks again for your guidance.</p>

---
