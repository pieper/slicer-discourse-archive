# Installation issues: macOS Mojave 10.14.6

**Topic ID**: 7950
**Date**: 2019-08-08
**URL**: https://discourse.slicer.org/t/installation-issues-macos-mojave-10-14-6/7950

---

## Post #1 by @unnmdnwb3 (2019-08-08 21:42 UTC)

<p>Hello everyone,</p>
<p>I’ve tried to locally install and compile Slicer to use its modules for an extension, on which I will be working on.<br>
However, I’m struggling with some issues and would appreciate some help.</p>
<p>My <strong>setup</strong> is the following:</p>
<ul>
<li>macOS: <em>Mojave 10.14.6</em>
</li>
<li>Xcode: <em>10.3</em>
</li>
<li>cmake: <em>3.15.1</em>
</li>
<li>qt: <em>5.13.0</em>
</li>
<li>wget: <em>1.20.3</em>
</li>
<li>gcc: <em>clang 1001.0.46.4</em>
</li>
</ul>
<p>I followed the <strong>instructions</strong> on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Build_Instructions#Mac_OSX_10.14_.28Mojave.29" rel="nofollow noopener">nightly build</a>:</p>
<pre><code class="lang-auto">% checkout
cd $HOME/PycharmProjects
git clone git://github.com/Slicer/Slicer.git
cd Slicer
./Utilities/SetupForDevelopment.sh

% build
mkdir Slicer-SuperBuild
cd Slicer-SuperBuild
cmake -DQt5_DIR:PATH=/usr/local/opt/qt/bin -DSlicer_USE_PYTHONQT_WITH_OPENSSL:BOOL=ON ../Slicer

% compile
SDKROOT=/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.14.sdk make -j4
</code></pre>
<p>During <strong>compilation</strong>, the following <strong>fatal error</strong> occurs and stops the process:</p>
<pre><code class="lang-auto">[ 38%] No install step for 'DCMTK'
[ 38%] Completed 'DCMTK'
[ 38%] Built target DCMTK
make: *** [all] Error 2
</code></pre>
<p>Thank you in advance for any help or suggestions!</p>

---

## Post #2 by @pieper (2019-08-09 00:03 UTC)

<p>When you use the <code>-j</code> option of make you won’t typically see the error message so run make without <code>-j</code> to see where it actually errors out.</p>
<p>Also, for a recent mac build I ended up using this cmake line:</p>
<pre><code class="lang-auto">cmake \
  -DCMAKE_BUILD_TYPE:STRING=Debug \
  -DQt5_VERSION:STRING=5.12 \
  -DQt5_DIR:FILEPATH=/usr/local/opt/qt5/lib/cmake/Qt5 \
  -DQt5Core_DIR:FILEPATH=/usr/local/opt/qt5/lib/cmake/Qt5Core \
  -DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=10.14 \
  -DSlicer_USE_SimpleITK:BOOL=OFF \
  -DSlicer_USE_QtTesting:BOOL=OFF \
  ~/slicer4/latest/Slicer
</code></pre>

---

## Post #3 by @unnmdnwb3 (2019-08-09 11:32 UTC)

<p>Hi <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Thank you so much for your input, after long hours of trial and error, I finally managed to build Slicer with the solution you proposed!</p>

---
