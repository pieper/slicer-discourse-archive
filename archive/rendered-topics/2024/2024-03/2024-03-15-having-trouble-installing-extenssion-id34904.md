# Having trouble Installing extenssion 

**Topic ID**: 34904
**Date**: 2024-03-15
**URL**: https://discourse.slicer.org/t/having-trouble-installing-extenssion/34904

---

## Post #1 by @Ajith_perera (2024-03-15 06:26 UTC)

<p>Operating system:Linux, X86_64, RHEL8<br>
Slicer version:GitHub(overnight)<br>
Expected behavior:<br>
Actual behavior:<br>
Hello: I am trying to install 3Dslicer and extensions with apptainer using the following definitions.<br>
export DEBIAN_FRONTEND=noninteractive<br>
apt update -y<br>
apt install -y python3-pip build-essential cmake wget git <br>
cmake-curses-gui cmake-qt-gui <br>
qtmultimedia5-dev qttools5-dev libqt5xmlpatterns5-dev libqt5svg5-dev <br>
qtwebengine5-dev qtscript5-dev <br>
qtbase5-private-dev libqt5x11extras5-dev libxt-dev libssl-dev<br>
git clone <a href="https://github.com/Slicer/Slicer" class="inline-onebox" rel="noopener nofollow ugc">GitHub - Slicer/Slicer: Multi-platform, free open source software for visualization and image computing.</a><br>
cd Slicer<br>
./Utilities/SetupForDevelopment.sh<br>
cd …<br>
mkdir Build<br>
cd ./Build<br>
cmake …/Slicer<br>
make  -j 16<br>
<strong>Installation is successful (I can run slicer using GUI)</strong>. Unfortunately, I do not know how to add Slicer extensions to apptainer type builds. Are there any docs. that I can review. I specifically want to slicerradiomics extension.<br>
Thank you, regards, Ajith</p>

---

## Post #2 by @jose-d (2024-03-18 08:16 UTC)

<p>TL/DR: at this moment, I’m now aware about any implicit way how to let users install extensions into <em>system-provided</em> Slicer.</p>
<p>longer answer:</p>
<p>Hi,  (I see nobody answered yet your question, so giving my 5c)</p>
<p>first, I’m more Apptainer guy rather than Slicer expert - we’re investigating how to use Slicer properly at our site too.</p>
<p>Did you try to build SlicerRadiomics in <code>%post</code> section of apptainer definition file, to have extension <em>baked in</em> apptainer image?</p>
<p>Cleaner way could be to install base slicer, and then, create apptainer image derived from base Slicer image with installed extension(s)…</p>
<p>The reason behind is (it was <a href="https://discourse.slicer.org/t/installing-extension-in-users-folder-in-linux/34805/23">explained</a> here at this forum recently) that Slicer mixes application itself and user-installed extensions in its “root” directory…</p>

---

## Post #3 by @muratmaga (2024-03-18 15:39 UTC)

<aside class="quote no-group" data-username="Ajith_perera" data-post="1" data-topic="34904">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ajith_perera/60/66917_2.png" class="avatar"> Ajith_perera:</div>
<blockquote>
<p>Unfortunately, I do not know how to add Slicer extensions to apptainer type builds. Are there any docs. that I can review.</p>
</blockquote>
</aside>
<p>If you have custom slicer build, you need to also build the extension. Please see this section of the developer’s guide: <a href="https://slicer.readthedocs.io/en/latest/developer_guide/build_instructions/overview.html#extensions-for-developer-builds-of-slicer">Overview — 3D Slicer documentation</a></p>

---

## Post #4 by @Ajith_perera (2024-03-18 20:25 UTC)

<p>Hi,  Thank you.  After a few trials and errors, I could add an extension more like you suggested. In the post section used<br>
git clone <a href="https://github.com/radiomics/SlicerRadiomics.git" class="inline-onebox" rel="noopener nofollow ugc">GitHub - AIM-Harvard/SlicerRadiomics: A Slicer extension to provide a GUI around pyradiomics</a><br>
mkdir SlicerRadiomics-build<br>
cd SlicerRadiomics-build<br>
cmake -DSlicer_DIR:PATH=/Build/Slicer-build …/SlicerRadiomics<br>
container image has /SlicerRadiomics-build/inner-build. Then I followed the instructions at <a href="https://github.com/AIM-Harvard/SlicerRadiomics?tab=readme-ov-file" class="inline-onebox" rel="noopener nofollow ugc">GitHub - AIM-Harvard/SlicerRadiomics: A Slicer extension to provide a GUI around pyradiomics</a>, Loading <code>SlicerRadiomics</code> from a build tree (first option). This seems to recognize Radiomics. I am not 100% this is the best way to go if I need to install additional packages. I would like to try “Cleaner way could be to install base slicer, and then, create apptainer image derived from base Slicer image with installed extension(s)…”. My first attempt at this fails. I tried a source level installation of slicer but failed because of Qt issues.</p>
<p>Once again thank you for your comments.</p>

---
