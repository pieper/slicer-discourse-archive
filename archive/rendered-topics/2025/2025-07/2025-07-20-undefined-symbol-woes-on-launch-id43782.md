---
topic_id: 43782
title: "Undefined Symbol Woes On Launch"
date: 2025-07-20
url: https://discourse.slicer.org/t/43782
---

# undefined symbol woes on launch

**Topic ID**: 43782
**Date**: 2025-07-20
**URL**: https://discourse.slicer.org/t/undefined-symbol-woes-on-launch/43782

---

## Post #1 by @Daniel_Drucker (2025-07-20 12:55 UTC)

<p>I’m trying to run ./Slicer (in 5.8.1) on RHEL8.9.<br>
I get:</p>
<pre><code class="lang-auto">$ ./Slicer
/home/ddrucker/Slicer-5.8.1/bin/SlicerApp-real: symbol lookup error: /lib64/libk5crypto.so.3: undefined symbol: EVP_KDF_ctrl, version OPENSSL_1_1_1b
</code></pre>
<p>I’ve tried dozens of permutations of setting <code>LD_LIBRARY_PATH</code> to various things to no avail.</p>
<p>I can’t change/upgrade/downgrade system libraries on the machine.</p>
<p>Is there a way to run the GUI (with extensions) inside a Singularity container? Or is there a <code>LD_LIBRARY_PATH</code> setting I’ve missed?</p>

---

## Post #2 by @Daniel_Drucker (2025-07-20 16:57 UTC)

<p>Solved!<br>
Moving the shipped libraries out of the way fixed it:</p>
<pre><code class="lang-auto">mv lib/Slicer-5.8/libcrypto.so.1.1 lib/Slicer-5.8/libcrypto.so.1.1.bak
mv lib/Slicer-5.8/libssl.so.1.1    lib/Slicer-5.8/libssl.so.1.1.bak
</code></pre>

---
