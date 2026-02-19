---
topic_id: 31045
title: "Trouble Setting Up Optitrack Duo With Plus"
date: 2023-08-08
url: https://discourse.slicer.org/t/31045
---

# Trouble setting up OptiTrack duo with Plus

**Topic ID**: 31045
**Date**: 2023-08-08
**URL**: https://discourse.slicer.org/t/trouble-setting-up-optitrack-duo-with-plus/31045

---

## Post #1 by @deringur (2023-08-08 13:26 UTC)

<p>I am following the tutorial (<a href="https://andysbrainbook.readthedocs.io/en/latest/Slicer/Slicer_Short_Course/Slicer_04_OpeningPLUSConnection.html" class="inline-onebox" rel="noopener nofollow ugc">Slicer Tutorial #4: Opening the PLUS Connection — Andy's Brain Book 1.0 documentation</a>) and have successfully exported the configuration and profile .xml files. When I click “Launch server” on PLUS Server Launcher, it prints “Connection failed, please select another device set and try again.” and throws the following errors:</p>
<p>|ERROR|055.036000|SERVER&gt; Unable to find required ProjectFile attribute in Device element in device set configuration| in :\D\PSNPb\PlusLib\src\PlusDataCollection\OptiTrack\vtkPlusOptiTrack.cxx(142)</p>
<p>|ERROR|055.051000|SERVER&gt; Failed to read parameters of device: TrackerDevice (type: OptiTrack)| in :\D\PSNPb\PlusLib\src\PlusDataCollection\vtkPlusDataCollector.cxx(126)</p>
<p>|ERROR|055.051000|SERVER&gt; Datacollector failed to read configuration| in :\D\PSNPb\PlusLib\src\PlusDataCollection\vtkPlusDataCollector.cxx(248)</p>
<p>|ERROR|055.051000|SERVER&gt; Datacollector failed to read configuration| in :\D\PSNPb\PlusLib\src\PlusServer\Tools\PlusServer.cxx(87)</p>
<p>|ERROR|055.073000| Server stopped unexpectedly. Return code: 1| in E:\D\PSNPb\PlusApp\PlusServerLauncher\PlusServerLauncherMainWindow.cxx(864)</p>
<p>Link to my config file:</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1qM7r7HNRo7lEw8f_ccj3nt3adfZEFE2r/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1qM7r7HNRo7lEw8f_ccj3nt3adfZEFE2r/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1qM7r7HNRo7lEw8f_ccj3nt3adfZEFE2r/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1qM7r7HNRo7lEw8f_ccj3nt3adfZEFE2r/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">MyConfig.xml</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Link to my profile file:</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1KLK8iqRr2BuyAgSxrkAexCCP28G7rJJ0/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1KLK8iqRr2BuyAgSxrkAexCCP28G7rJJ0/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1KLK8iqRr2BuyAgSxrkAexCCP28G7rJJ0/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1KLK8iqRr2BuyAgSxrkAexCCP28G7rJJ0/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">MyProfile.xml</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>Thank you in advance for any tips for troubleshooting or solutions.</p>
<p><a class="mention" href="/u/lassoan">@lassoan</a></p>

---

## Post #2 by @Sunderlandkyl (2023-08-08 14:34 UTC)

<p>Where is your Profile.xml located relative to the config file directory?</p>

---

## Post #3 by @deringur (2023-08-08 18:40 UTC)

<p>Both the profile and config .xml files are located in the same folder.</p>

---

## Post #4 by @muratmaga (2023-08-08 21:01 UTC)

<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Would someone from your teams have sometime to help us setup the instrument via zoom session? This is very new to us, I think if we can pass the point of configuring we can make some progress, but our interns time is quite limited.</p>

---

## Post #5 by @lassoan (2023-08-08 23:09 UTC)

<p>Probably the configuration files need to be in the configuration folder. Follow the pattern used in the example configuration files. <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> is the expert in this - he may be able to give more specific advice.</p>

---

## Post #6 by @muratmaga (2023-08-09 04:41 UTC)

<p>Thanks.</p>
<p><a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> would you have time for a zoom session?</p>

---

## Post #7 by @Sunderlandkyl (2023-08-09 14:16 UTC)

<p>Sure, I can make time today before 12 or after 2, or tomorrow after 12.</p>

---

## Post #8 by @muratmaga (2023-08-09 14:20 UTC)

<p>I will send you a PM</p>

---

## Post #9 by @muratmaga (2023-08-09 23:23 UTC)

<p>Thanks to <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> we managed to get our camera working.</p>
<p>We now would like to replace the generic needle model with the actual optitrack probe/stylus model. Is there a repository of 3D models? For reference , this is what we have.<br>
<a href="https://www.optitrack.com/accessories/measurement-tools/" rel="noopener nofollow ugc">OptiTrack - Measurement Tools</a></p>

---
