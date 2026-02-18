# Build SlicerCAT on Ubuntu 22.04.3 LTS

**Topic ID**: 33019
**Date**: 2023-11-25
**URL**: https://discourse.slicer.org/t/build-slicercat-on-ubuntu-22-04-3-lts/33019

---

## Post #1 by @mau_igna_06 (2023-11-25 12:25 UTC)

<p>Hi,</p>
<p>I wanted to share I could successfully build the app with the following code:</p>
<pre><code class="lang-auto">cat /etc/os-release | grep PRETTY_NAME
# prints 'PRETTY_NAME="Ubuntu 22.04.3 LTS"'

sudo apt update &amp;&amp; sudo apt install git subversion build-essential cmake cmake-curses-gui cmake-qt-gui libxt-dev libssl-dev


curl -LO http://download.qt.io/official_releases/online_installers/qt-unified-linux-x64-online.run
chmod +x qt-unified-linux-x64-online.run

sudo su
export QT_ACCOUNT_LOGIN=&lt;set your qt.io account email here&gt; &amp;&amp; \
export QT_ACCOUNT_PASSWORD=&lt;set your password here&gt; &amp;&amp; \
sudo ./qt-unified-linux-x64-online.run \
  install \
    qt.qt5.5152.gcc_64 \
    qt.qt5.5152.qtwebengine \
    qt.qt5.5152.qtwebengine.gcc_64 \
  --root /opt/qt \
  --email $QT_ACCOUNT_LOGIN \
  --pw $QT_ACCOUNT_PASSWORD
# the Qt install succeeded
exit


sudo apt install mesa-common-dev libglu1-mesa-dev


cd /home/$USER/WholeApp/
mkdir SCATRelease
cd SCATRelease
cmake -DCMAKE_BUILD_TYPE:STRING=Release -DQt5_DIR=/opt/qt/5.15.2/gcc_64/lib/cmake/Qt5 -Dslicersources_SOURCE_DIR=/home/$USER/WholeApp/Slicer ../SCATCode
# make -j&lt;N&gt;
make -j32
</code></pre>
<p>Best wishes,<br>
Mauro</p>

---
