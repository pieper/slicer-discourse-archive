---
topic_id: 44957
title: "Getting Ffmpeg Crash On Linux"
date: 2025-11-03
url: https://discourse.slicer.org/t/44957
---

# Getting ffmpeg crash on Linux

**Topic ID**: 44957
**Date**: 2025-11-03
**URL**: https://discourse.slicer.org/t/getting-ffmpeg-crash-on-linux/44957

---

## Post #1 by @muratmaga (2025-11-03 23:02 UTC)

<p>On ubuntu 22.04, ScreenCapture is crashing with the latest preview with this error. I presume this is an ABI issue?</p>
<pre><code class="lang-auto">/usr/bin/ffmpeg -nostdin -y -r 60 -start_number 0 -i /tmp/Slicer-NCcZBZ/Slicer-%04d.png -codec mpeg4 -qscale 5 /home/exouser/Animation.mp4 ffmpeg error output: /usr/bin/ffmpeg: symbol lookup error: /lib/x86_64-linux-gnu/libssh-gcrypt.so.4: undefined symbol: GSS_C_NT_USER_NAME, version gssapi_krb5_2_MIT
</code></pre>
<p>FFmpeg is install via apt and there doesn’t seem like a newer version.</p>

---

## Post #2 by @muratmaga (2025-11-04 00:05 UTC)

<p>Static release from <a href="https://github.com/eugeneware/ffmpeg-static/releases" rel="noopener nofollow ugc">https://github.com/eugeneware/ffmpeg-static/releases</a> (ffmpeg-linux-x64) works without a problem. hopefully others can see this thread and avoid installing the apt package.</p>

---

## Post #3 by @pieper (2025-11-04 13:08 UTC)

<p><a class="mention" href="/u/jcfr">@jcfr</a> is this due to the same issues we had with git and kerberos?</p>

---

## Post #4 by @chir.set (2025-11-04 17:08 UTC)

<p>On Arch stock <code>ffmpeg</code> works as expected with <code>5.9.0-2025-11-03 r34025 / cbf73a6</code> and <code>ScreenCapture</code>. Just a ping.</p>

---
