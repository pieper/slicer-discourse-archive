# Unable to create a Docker container using a downloaded 3DSlicer version

**Topic ID**: 41384
**Date**: 2025-01-30
**URL**: https://discourse.slicer.org/t/unable-to-create-a-docker-container-using-a-downloaded-3dslicer-version/41384

---

## Post #1 by @jhlegarreta (2025-01-30 21:24 UTC)

<p>Hi,<br>
I have been trying to build a Docker image to run a given 3DSlicer version (5.2.2) on an HPC system. Once I have the base installation working, I will be willing to instal <code>SlicerDMRI</code>, <code>UKFTractography</code> and <code>SlicerWMA</code> extensions.</p>
<p>Although I have gone through the various related posts on the forum and even some repositories linked on those, I am unable to make the base installation work in the container.</p>
<p>My dockerfile is the following:</p>
<pre><code class="lang-auto">FROM ubuntu:22.04

LABEL version="1.0.0"
LABEL description="3DSlicer"

# Update + upgrade package management
RUN apt-get update &amp;&amp; apt-get -y upgrade

RUN apt-get install -y wget

# Install Slicer dependencies
RUN apt-get install -y \
    xvfb \
    libpulse0 \
    libnss3 \
    libsm6 \
    libglu1-mesa \
    libxrender1 \
    libxext6 \
    libgl1 \
    libegl1 \
    libglib2.0-0 \
    libpulse0 libpulse-mainloop-glib0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libfontconfig1 \
    libxcursor1 libxcb-cursor0 \
    libxi6 \
    libxtst6 \
    libxkbcommon0 \
    libasound2 \
    libxcb-xinerama0 \
    libpulse-dev libxkbcommon-x11-0 \
    libx11-6

RUN apt-get install --reinstall libxcb-xinerama0

RUN apt-get install -y libxcb-shape0
RUN apt-get install -y libxcb-icccm4-dev libxcb-image0-dev libxcb-keysyms1-dev libxcb-randr0 libxcb-render-util0 libxcb-xkb-dev libxkbcommon-x11-dev

RUN apt-get install -y '^libxcb.*-dev' libxcb-util-dev libxcb-xkb1 libxcb1 libxcb-glx0 libx11-xcb1 \
    libqt5gui5 libqt5core5a libqt5widgets5 qt5-qmake qtbase5-dev libqt5widgets5 libqt5network5 libqt5dbus5 qt5dxcb-plugin

RUN apt-get -y autoremove &amp;&amp; apt-get clean autoclean
RUN rm -rf /var/lib/apt/lists/*

RUN if [ ! -L /usr/lib/x86_64-linux-gnu/libxcb-util.so.1 ]; then \
        ln -s /usr/lib/x86_64-linux-gnu/libxcb-util.so /usr/lib/x86_64-linux-gnu/libxcb-util.so.1; \
    fi

ENV QT_QPA_PLATFORM=xcb
ENV QT_DEBUG_PLUGINS=1

ENV DISPLAY=:localhost:10.0

# Download and unpack Slicer (Slicer-5.2.2-linux-amd64)
ENV SLICER_URL="https://slicer-packages.kitware.com/api/v1/file/63f5bef28939577d9867b4da/download"
ENV SLICER_HOME=/opt/slicer

RUN wget -q ${SLICER_URL} -O /tmp/Slicer.tar.gz &amp;&amp; \
  mkdir -p ${SLICER_HOME} &amp;&amp; \
  tar -xzf /tmp/Slicer.tar.gz -C ${SLICER_HOME} --strip-components=1 &amp;&amp; \
  rm /tmp/Slicer.tar.gz

# Make Slicer available in the PATH
ENV PATH="${SLICER_HOME}:${PATH}"
</code></pre>
<p>The container is built successfully, but when I try to check that I can execute 3DSlicer, I get:</p>
<pre><code class="lang-auto">$ docker run 3dslicer Slicer --version
QFactoryLoader::QFactoryLoader() checking directory path "/opt/slicer/lib/QtPlugins/platforms" ...
QFactoryLoader::QFactoryLoader() looking at "/opt/slicer/lib/QtPlugins/platforms/libqxcb.so"
Found metadata in lib /opt/slicer/lib/QtPlugins/platforms/libqxcb.so, metadata=
{
    "IID": "org.qt-project.Qt.QPA.QPlatformIntegrationFactoryInterface.5.3",
    "MetaData": {
        "Keys": [
            "xcb"
        ]
    },
    "archreq": 0,
    "className": "QXcbIntegrationPlugin",
    "debug": false,
    "version": 331520
}


Got keys from plugin meta data ("xcb")
QFactoryLoader::QFactoryLoader() checking directory path "/opt/slicer/bin/platforms" ...
loaded library "/opt/slicer/lib/QtPlugins/platforms/libqxcb.so"
qt.qpa.xcb: could not connect to display 
qt.qpa.plugin: Could not load the Qt platform plugin "xcb" in "" even though it was found.
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.

Available platform plugins are: xcb.

error: [/opt/slicer/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>
<p>This error has been reported in other threads, but none of the solutions proposed seem to get past the error. In fact, all lines between <code>libx11-6</code> and <code>RUN apt-get install -y '^libxcb.*-dev'</code> that I have added after reading these threads have not modified the error message, so they could be removed from the above recipe.</p>
<p>What am I missing?</p>
<p>Thank you.</p>

---

## Post #2 by @jhlegarreta (2025-01-31 02:16 UTC)

<aside class="quote no-group" data-username="jhlegarreta" data-post="1" data-topic="41384">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p><code>ENV DISPLAY=:localhost:10.0</code></p>
</blockquote>
</aside>
<p>Also, not sure whether this will work nicely on an HCP system.</p>

---
