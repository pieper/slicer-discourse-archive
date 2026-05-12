---
topic_id: 46987
title: "3D Slicer Wont Open Due To Libssl On Ubuntu 24 04 Lts"
date: 2026-05-11
url: https://discourse.slicer.org/t/46987
---

# 3D Slicer won't open due to libssl on Ubuntu 24.04 LTS

**Topic ID**: 46987
**Date**: 2026-05-11
**URL**: https://discourse.slicer.org/t/3d-slicer-wont-open-due-to-libssl-on-ubuntu-24-04-lts/46987

---

## Post #1 by @dvijay (2026-05-11 15:52 UTC)

<p><strong>OS</strong>: Ubuntu 24.04.3 LTS</p>
<p><strong>Slicer</strong>: 5.10.0-linux-amd64</p>
<p>Installation method:</p>
<pre><code class="lang-auto">cd ~/Downloads
tar -xvf Slicer-5.10.0-linux-amd64.tar.gz
sudo mv ./Slicer-5.10.0-linux-amd64 /opt/Slicer-5.10.0-linux-amd64
sudo apt-get install libglu1-mesa libpulse-mainloop-glib0 libnss3 libasound2t64 qt5dxcb-plugin
</code></pre>
<p>Error while launching:</p>
<p><code>/opt/Slicer-5.10.0-linux-amd64/bin/SlicerApp-real: error while loading shared libraries: libssl.so.1.1: cannot open shared object file: No such file or directory</code></p>
<ul>
<li>How do I fix this? Some online search suggested that having system wide installation of lower libssl might cause stability issue with other things.</li>
<li>Shouldn’t this be already present in the /lib folder under Slicer and why doesn’t it work out of box?</li>
</ul>
<p>It did work for a while and sometime during one of the regular system updates from Ubuntu it stopped working.</p>

---

## Post #2 by @pieper (2026-05-11 16:16 UTC)

<p>Hmm, it “works for me” on a couple 24.04.3 machines.</p>
<p>Are you starting <code>SlicerApp-real</code> instead of <code>Slicer</code>? (<code>Slicer</code> is the launcher that sets the paths).</p>

---

## Post #3 by @dvijay (2026-05-11 16:19 UTC)

<p>I am running <code>Slicer</code> present in the directory root and not <code>SlicerApp-real</code> in its bin.</p>

---

## Post #4 by @muratmaga (2026-05-11 16:23 UTC)

<p>I would not suggest moving the application to /opt. Slicer does not work that way.</p>
<p>Install in your user space, without sudo and retry and report.</p>

---

## Post #5 by @dvijay (2026-05-11 16:35 UTC)

<p>Yes, that worked, thanks a lot! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---
