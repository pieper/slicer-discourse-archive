# Using the pyigtl Library to send data across a docker compose network

**Topic ID**: 45859
**Date**: 2026-01-22
**URL**: https://discourse.slicer.org/t/using-the-pyigtl-library-to-send-data-across-a-docker-compose-network/45859

---

## Post #1 by @Oskey999 (2026-01-22 07:19 UTC)

<p>Hello,<br>
I am trying to run SlicerTMS as two containers in a docker-compose but I am having issues using the pyigtl python library to send the data between the two containers.<br>
I have got a container to send the data from a container to my local machine but that does not work for sending data between containers.</p>
<p>Likely it is just a modification to the the SlicerTMS code that I missed.<br>
I will also add a link to the repo for the project and a brief explanation.</p><aside class="onebox githubrepo" data-onebox-src="https://github.com/Oskey999/demo-pyigtlcompose">
  <header class="source">

      <a href="https://github.com/Oskey999/demo-pyigtlcompose" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <div class="github-row" data-github-private-repo="false">
  <img width="690" height="344" src="https://opengraph.githubassets.com/bc17448ca62ba17a4b7745e6cd28ecba/Oskey999/demo-pyigtlcompose" class="thumbnail">

  <h3><a href="https://github.com/Oskey999/demo-pyigtlcompose" target="_blank" rel="noopener nofollow ugc">GitHub - Oskey999/demo-pyigtlcompose: demo for trying to use py igtl between containers</a></h3>

    <p><span class="github-repo-description">demo for trying to use py igtl between containers</span></p>
</div>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>
<p>
Simplistically, the docker compose creates two containers slicergui which hosts 3D Slicer 5.8.1 accessible using novnc through the web browser and installs the necessary extensions (OpenIGTLinkIF does need to be re-installed manually), and tmsserver which has the python server where SlicerTMS’s ai predictions occur.</p>
<p>I have been able to trigger the tmsserver to register a connection from within the slicergui container,  but never with the pyigtl library needed to send the correct data</p>

---

## Post #2 by @pieper (2026-01-25 11:11 UTC)

<p>I haven’t tried to use SlicerTMS with docker, but I can’t think of anything fundamental that would be different.  I guess you should doublecheck the port mappings and maybe try to make some simple pyigtl experiments to confirm that simpler things work.</p>

---

## Post #3 by @Oskey999 (2026-01-26 08:05 UTC)

<p>Hi, thanks for the reply.<br>
Just building simpler tests at the moment. I noticed whilst running a test script that the slicergui was not using the locally modified version of SlicerTMS for whatever reason. This may not be the only issue but it is likely part of it.</p>

---

## Post #4 by @pieper (2026-01-26 10:17 UTC)

<p>Yes, that sounds like a docker issue.  You should be able to configure things to use the TMS module from a shared volume so you can update it outside of docker without needing to rebuild the image.</p>

---

## Post #5 by @Oskey999 (2026-01-30 03:18 UTC)

<p>Hi,<br>
Thanks for your input, it looks like the root of the issue was my installs.py file for installing extensions was improperly installing the requisite extensions.<br>
I could find them under installed extensions but the nodes and widgets were not accessible. I am attempting a new version which is building from source based on the rosmed ISMR2024 tutorial container rosmed/docker-ubuntu-22.04-ros2-slicerros2-lw:ismr2024</p>

---

## Post #6 by @Oskey999 (2026-02-05 12:02 UTC)

<p>Hi, Thanks for all the help.</p>
<p>It looks like it was a mish-mash of my python script failing to import all of the extensions (but still appearing as installed in the extension manager),  not having slicer built from source so manually building extensions didn’t work and environment variables set at the docker compose level not making it through to the python code.</p>

---
