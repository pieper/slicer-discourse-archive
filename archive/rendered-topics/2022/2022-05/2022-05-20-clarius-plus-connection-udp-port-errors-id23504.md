# Clarius Plus Connection udp Port Errors

**Topic ID**: 23504
**Date**: 2022-05-20
**URL**: https://discourse.slicer.org/t/clarius-plus-connection-udp-port-errors/23504

---

## Post #1 by @ChristophG123 (2022-05-20 05:36 UTC)

<p>Operating system: Windows 10 64 bits<br>
Slicer version: 5.1.0 2022-05-04<br>
Expected behavior: Connecting Clarius to 3D Slicer using Cast API and Plus Server<br>
Actual behavior:<br>
Both the computer &amp; tablet are connected on the same network. The computer can ping the Clarius device, however when it tries to connect via Plus server, it gets this error:<br>
|ERROR|018.164000|SERVER&gt; error: connect failure: Exception ocurred (Error connecting to TCP socket: No connection could be made because the target machine actively refused it)| in E:\D\PTNPCb\PlusLib\src\PlusDataCollection\Clarius\vtkPlusClarius.cxx(572)<br>
|ERROR|018.165000|SERVER&gt; … Clarius device connected but could not get valid udp port| in E:\D\PTNPCb\PlusLib\src\PlusDataCollection\Clarius\vtkPlusClarius.cxx(535)</p>
<p>The IP and tcp port in the config file match the IP and casting port in the Clarius tablet application. I’m not sure what the utp port is and how to find/change it; this seems to be causing the error.</p>

---

## Post #2 by @lassoan (2022-05-21 17:41 UTC)

<p>We usually discuss hardware connection errors in issues in the Plus toolkit repository.</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://github.com/PlusToolkit/PlusLib/issues?q=is:issue%2Bis:open%2Bclarius">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/PlusToolkit/PlusLib/issues?q=is:issue%2Bis:open%2Bclarius" target="_blank" rel="noopener">GitHub</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:690/345;"><img src="https://opengraph.githubassets.com/ad0c3b0cda3b3d9c42a3fa16a4a10ba38ee745b7ce6a3c99ae399e542a301d9e/PlusToolkit/PlusLib" class="thumbnail" width="690" height="345"></div>

<h3><a href="https://github.com/PlusToolkit/PlusLib/issues?q=is:issue%2Bis:open%2Bclarius" target="_blank" rel="noopener">Issues · PlusToolkit/PlusLib</a></h3>

  <p>Software library for data acquisition, pre-processing, and calibration for navigated image-guided interventions. - Issues · PlusToolkit/PlusLib</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>If there is a similar open issue then you can comment there. If there is nothing similar then you can create a new issue.</p>
<p>For reference, copy here the link to the issue you have added/commented on.</p>

---
