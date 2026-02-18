# AWS EC2 (GPU) Instance setup

**Topic ID**: 40453
**Date**: 2024-11-30
**URL**: https://discourse.slicer.org/t/aws-ec2-gpu-instance-setup/40453

---

## Post #1 by @Muhammad_Hilal (2024-11-30 05:31 UTC)

<p>I have setup the slicer in AWS EC2 (GPU) Instance G5.8xlarge.<br>
I need guidelines, what should I do after completing the setup if I need UI?</p>
<p>final result<br>
./Slicer</p>
<p>Slicer: cannot connect to X server :0</p>
<p><strong>ubuntu@ip-172-31-114-1</strong>:<strong>~/Slicer-SuperBuild-Debug/Slicer-build</strong>$ export DISPLAY=:99</p>
<p><strong>ubuntu@ip-172-31-114-1</strong>:<strong>~/Slicer-SuperBuild-Debug/Slicer-build</strong>$ ./Slicer</p>
<p>qt.network.ssl: QSslSocket: cannot resolve SSL_get1_peer_certificate</p>
<p>qt.network.ssl: QSslSocket: cannot resolve EVP_PKEY_get_base_id</p>
<p>qt.network.ssl: QSslSocket: cannot resolve SSL_CTX_load_verify_dir</p>
<p>Switch to module: “Welcome”</p>

---

## Post #2 by @pieper (2024-11-30 14:02 UTC)

<p>It looks like you have some kind of X server running on display 99.  You need to connect to it via somthing like x11vnc/noVNC.</p>
<p>Something like what’s described here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://learn.canceridc.dev/cookbook/virtual-machines/idc-desktop">
  <header class="source">
      <img src="https://1031677300-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/spaces%2F-MCTG4fXybYgGMalZnmf%2Favatar-1612215897315.png?generation=1612215897690711&amp;alt=media" class="site-icon" width="256" height="256">

      <a href="https://learn.canceridc.dev/cookbook/virtual-machines/idc-desktop" target="_blank" rel="noopener">learn.canceridc.dev</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/362;"><img src="https://learn.canceridc.dev/~gitbook/ogimage/-MklWhZ0r2T5tzFKE7Xi" class="thumbnail" width="690" height="362"></div>

<h3><a href="https://learn.canceridc.dev/cookbook/virtual-machines/idc-desktop" target="_blank" rel="noopener">3D Slicer desktop VM | IDC User Guide</a></h3>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
