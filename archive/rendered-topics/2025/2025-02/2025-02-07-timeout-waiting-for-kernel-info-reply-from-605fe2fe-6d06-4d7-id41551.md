# Timeout waiting for kernel_info reply from 605fe2fe-6d06-4d71-a2e1-001bf

**Topic ID**: 41551
**Date**: 2025-02-07
**URL**: https://discourse.slicer.org/t/timeout-waiting-for-kernel-info-reply-from-605fe2fe-6d06-4d71-a2e1-001bf/41551

---

## Post #1 by @Saurabh_Mishra (2025-02-07 11:56 UTC)

<p>I am using one dockerfile to create one jupyterImage</p>
<pre><code class="lang-auto"># Base image with Jupyter Notebook
FROM jupyter/base-notebook

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC
ENV DISPLAY=:1

# Switch to root user for installations
USER root

# Install required dependencies
RUN apt-get update --fix-missing \
    &amp;&amp; apt-get install -y --no-install-recommends \
    bzip2 \
    xvfb \
    xauth \
    x11-utils \
    x11-xserver-utils \
    libgl1-mesa-glx \
    libglu1-mesa \
    libpulse0 \
    libnss3 \
    libxss1 \
    libasound2 \
    libdbus-glib-1-2 \
    libxcursor1 \
    libxcomposite1 \
    libxdamage1 \
    libxkbcommon0 \
    libxkbcommon-x11-0 \
    libqt5gui5 \
    libqt5core5a \
    libqt5widgets5 \
    libxcb-xinerama0 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-shape0 \
    libxcb-xfixes0 \
    libxrender1 \
    libpulse-mainloop-glib0 \
    libfontconfig1 \
    libglib2.0-0 \
    libx11-6 \
    libxtst6 \
    libxi6 \
    qt5-qmake \
    qtbase5-dev \
    qtbase5-dev-tools \
    qtchooser \
    libxcb-xinerama0 \
    libx11-xcb1 \
    &amp;&amp; rm -rf /var/lib/apt/lists/*

# Install Python packages (optional)
RUN pip install --no-cache-dir numpy scipy pandas matplotlib jupyterlab_launcher

# Copy the pre-downloaded Slicer package into the container
COPY Slicer.tar.gz /tmp/Slicer.tar.gz

# Extract and install Slicer
RUN tar -xzf /tmp/Slicer.tar.gz -C /opt/ \
    &amp;&amp; rm /tmp/Slicer.tar.gz \
    &amp;&amp; mv /opt/Slicer-* /opt/Slicer \
    &amp;&amp; chmod +x /opt/Slicer/Slicer

# Add Slicer to PATH
ENV PATH="/opt/Slicer:$PATH"

# Create JupyterLab Launcher Entry for Slicer
RUN mkdir -p /home/jovyan/.jupyter/custom \
    &amp;&amp; echo "{\"name\": \"Slicer\", \"display_name\": \"3D Slicer\", \"icon_path\": \"/opt/Slicer/icon.png\", \"command\": [\"/opt/Slicer/Slicer\"]}" &gt; /home/jovyan/.jupyter/custom/slicer-launcher.json

# Install Jupyter Kernel support for Slicer
RUN mkdir -p /usr/local/share/jupyter/kernels/slicer \
    &amp;&amp; echo "{ \
        \"argv\": [\"/opt/Slicer/Slicer\", \"--no-splash\", \"--python\", \"-m\", \"ipykernel_launcher\", \"-f\", \"{connection_file}\"], \
        \"display_name\": \"3D Slicer\", \
        \"language\": \"python\" \
    }" &gt; /usr/local/share/jupyter/kernels/slicer/kernel.json


# Set correct permissions for Jupyter config
RUN chown -R jovyan:users /home/jovyan/.jupyter /usr/local/share/jupyter/kernels
# Set XDG_RUNTIME_DIR for Slicer compatibility
ENV XDG_RUNTIME_DIR=/tmp/runtime-jovyan
RUN mkdir -p /tmp/runtime-jovyan &amp;&amp; chown -R 1000:100 /tmp/runtime-jovyan

# Ensure Slicer can write to its extensions directory
RUN mkdir -p /opt/Slicer/slicer.org/Extensions-33216 \
    &amp;&amp; chown -R 1000:100 /opt/Slicer

# Start Xvfb and JupyterLab
ENTRYPOINT ["sh", "-c", "Xvfb :1 -screen 0 1024x768x24 &amp; export DISPLAY=:1 &amp;&amp; start-notebook.sh"]

# Start JupyterLab when the container starts
CMD ["start-notebook.sh"]

</code></pre>
<p>Using this i have 2 files in my folder along with this One is Slicer.tar.gz which is latest version of Slicer that i downloaded and i have jupyter_notebook_config.py in which i have<br>
c.ServerApp.kernel_info_timeout = 60 # Increase timeout to 60 seconds</p>
<p>That’s it.</p>
<p>Everythins seems to be working The jupyterlab is working fine . I am seeing the SLicer on jupyterlab also.<br>
But when i run the commands inside my slicer notebook. I get</p>
<pre><code class="lang-auto"> Timeout waiting for kernel_info reply from 605fe2fe-6d06-4d71-a2e1-001bf734113c
[I 2025-02-06 09:40:47.668 ServerApp] Connecting to kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c.
[W 2025-02-06 09:40:47.688 ServerApp] Replacing stale connection: 605fe2fe-6d06-4d71-a2e1-001bf734113c:eba35d9b-b3c7-442e-a07c-42ec07f749fe
[W 2025-02-06 09:40:52.187 ServerApp] Nudge: attempt 10 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:40:57.207 ServerApp] Nudge: attempt 20 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:41:02.227 ServerApp] Nudge: attempt 30 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:41:07.248 ServerApp] Nudge: attempt 40 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:41:12.265 ServerApp] Nudge: attempt 50 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:41:17.281 ServerApp] Nudge: attempt 60 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:41:22.301 ServerApp] Nudge: attempt 70 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:41:27.322 ServerApp] Nudge: attempt 80 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:41:32.341 ServerApp] Nudge: attempt 90 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:41:37.362 ServerApp] Nudge: attempt 100 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:41:42.379 ServerApp] Nudge: attempt 110 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:41:47.393 ServerApp] Nudge: attempt 120 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[E 2025-02-06 09:41:47.667 ServerApp] Uncaught exception GET /api/kernels/605fe2fe-6d06-4d71-a2e1-001bf734113c/channels?session_id=09db911a-5d9d-4b9e-b742-5694602cd880 (172.17.0.1)
    HTTPServerRequest(protocol='http', host='127.0.0.1:8888', method='GET', uri='/api/kernels/605fe2fe-6d06-4d71-a2e1-001bf734113c/channels?session_id=09db911a-5d9d-4b9e-b742-5694602cd880', version='HTTP/1.1', remote_ip='172.17.0.1')
    Traceback (most recent call last):
      File "/opt/conda/lib/python3.11/site-packages/tornado/websocket.py", line 939, in _accept_connection
        await open_result
      File "/opt/conda/lib/python3.11/site-packages/jupyter_server/services/kernels/websocket.py", line 74, in open
        await self.connection.connect()
    TimeoutError: Timeout
[W 2025-02-06 09:41:47.685 ServerApp] Timeout waiting for kernel_info reply from 605fe2fe-6d06-4d71-a2e1-001bf734113c
[I 2025-02-06 09:41:47.686 ServerApp] Connecting to kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c.
[W 2025-02-06 09:41:47.706 ServerApp] Replacing stale connection: 605fe2fe-6d06-4d71-a2e1-001bf734113c:35b83666-d972-4d9a-bc6d-fcecf51ca449
[W 2025-02-06 09:41:52.203 ServerApp] Nudge: attempt 10 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:41:57.221 ServerApp] Nudge: attempt 20 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:42:02.239 ServerApp] Nudge: attempt 30 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:42:07.254 ServerApp] Nudge: attempt 40 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:42:12.274 ServerApp] Nudge: attempt 50 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:42:17.292 ServerApp] Nudge: attempt 60 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:42:22.312 ServerApp] Nudge: attempt 70 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:42:27.336 ServerApp] Nudge: attempt 80 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:42:32.356 ServerApp] Nudge: attempt 90 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:42:37.372 ServerApp] Nudge: attempt 100 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:42:42.390 ServerApp] Nudge: attempt 110 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:42:47.410 ServerApp] Nudge: attempt 120 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[E 2025-02-06 09:42:47.685 ServerApp] Uncaught exception GET /api/kernels/605fe2fe-6d06-4d71-a2e1-001bf734113c/channels?session_id=eba35d9b-b3c7-442e-a07c-42ec07f749fe (172.17.0.1)
    HTTPServerRequest(protocol='http', host='127.0.0.1:8888', method='GET', uri='/api/kernels/605fe2fe-6d06-4d71-a2e1-001bf734113c/channels?session_id=eba35d9b-b3c7-442e-a07c-42ec07f749fe', version='HTTP/1.1', remote_ip='172.17.0.1')
    Traceback (most recent call last):
      File "/opt/conda/lib/python3.11/site-packages/tornado/websocket.py", line 939, in _accept_connection
        await open_result
      File "/opt/conda/lib/python3.11/site-packages/jupyter_server/services/kernels/websocket.py", line 74, in open
        await self.connection.connect()
    TimeoutError: Timeout
[W 2025-02-06 09:42:47.702 ServerApp] Timeout waiting for kernel_info reply from 605fe2fe-6d06-4d71-a2e1-001bf734113c
[I 2025-02-06 09:42:47.703 ServerApp] Connecting to kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c.
[W 2025-02-06 09:42:52.224 ServerApp] Nudge: attempt 10 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:42:57.244 ServerApp] Nudge: attempt 20 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:43:02.262 ServerApp] Nudge: attempt 30 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:43:07.283 ServerApp] Nudge: attempt 40 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:43:12.304 ServerApp] Nudge: attempt 50 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:43:17.322 ServerApp] Nudge: attempt 60 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:43:22.349 ServerApp] Nudge: attempt 70 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:43:27.371 ServerApp] Nudge: attempt 80 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:43:32.393 ServerApp] Nudge: attempt 90 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:43:37.414 ServerApp] Nudge: attempt 100 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:43:42.435 ServerApp] Nudge: attempt 110 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[W 2025-02-06 09:43:47.452 ServerApp] Nudge: attempt 120 on kernel 605fe2fe-6d06-4d71-a2e1-001bf734113c
[E 2025-02-06 09:43:47.703 ServerApp] Uncaught exception GET /api/kernels/605fe2fe-6d06-4d71-a2e1-001bf734113c/channels?session_id=35b83666-d972-4d9a-bc6d-fcecf51ca449 (172.17.0.1)
    HTTPServerRequest(protocol='http', host='127.0.0.1:8888', method='GET', uri='/api/kernels/605fe2fe-6d06-4d71-a2e1-001bf734113c/channels?session_id=35b83666-d972-4d9a-bc6d-fcecf51ca449', version='HTTP/1.1', remote_ip='172.17.0.1')
    Traceback (most recent call last):
      File "/opt/conda/lib/python3.11/site-packages/tornado/websocket.py", line 939, in _accept_connection
        await open_result
      File "/opt/conda/lib/python3.11/site-packages/jupyter_server/services/kernels/websocket.py", line 74, in open
        await self.connection.connect()
    TimeoutError: Timeout
[W 2025-02-06 09:43:47.749 ServerApp] Timeout waiting for kernel_info reply from 605fe2fe-6d06-4d71-a2e1-001bf734113c
</code></pre>

---
