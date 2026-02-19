---
topic_id: 28037
title: "Fcal Lego Phantom Configuration File And 3D Model"
date: 2023-02-24
url: https://discourse.slicer.org/t/28037
---

# Fcal Lego phantom: configuration file and 3D model

**Topic ID**: 28037
**Date**: 2023-02-24
**URL**: https://discourse.slicer.org/t/fcal-lego-phantom-configuration-file-and-3d-model/28037

---

## Post #1 by @Qianqian_Cai (2023-02-24 18:32 UTC)

<p>Hi! I am following the instruction to perform freehand 3D ultrasound calibration using the Lego phantom. It is stated in the pdf tutorial that the 3D model and XML file of the lego phantom is provided.</p>
<p>Plus version: PlusApp-2.9.0.20230201-Clarius-Win64</p>
<ol>
<li>In the PLUS config folder, there is an STL file, fCal_L1.4. Is this the latest 3D model of the Lego phantom?</li>
<li>Where can I find the configuration file of the Lego phantom?</li>
</ol>
<p>Thank you for the help!</p>

---

## Post #2 by @Sunderlandkyl (2023-02-24 18:47 UTC)

<p>The Lego phantom config files are in this folder:</p><aside class="onebox githubfolder" data-onebox-src="https://github.com/PlusToolkit/PlusLibData/tree/master/ConfigFiles">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/PlusToolkit/PlusLibData/tree/master/ConfigFiles" target="_blank" rel="noopener nofollow ugc">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/PlusToolkit/PlusLibData/tree/master/ConfigFiles" target="_blank" rel="noopener nofollow ugc">PlusLibData/ConfigFiles at master · PlusToolkit/PlusLibData</a></h3>

  <p><a href="https://github.com/PlusToolkit/PlusLibData/tree/master/ConfigFiles" target="_blank" rel="noopener nofollow ugc">master/ConfigFiles</a></p>

  <p><span class="label1">Data file storage repository for Plus library. Contribute to PlusToolkit/PlusLibData development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>The Lego phantom STL are here: <a href="https://github.com/PlusToolkit/PlusLibData/tree/master/CADModels/LegoPhantom" class="inline-onebox" rel="noopener nofollow ugc">PlusLibData/CADModels/LegoPhantom at master · PlusToolkit/PlusLibData · GitHub</a></p>

---

## Post #3 by @Qianqian_Cai (2023-02-24 19:03 UTC)

<p>Thanks a lot! The Lego phantom has 3 different versions. My phantom is corresponding with the LegoPhantom.stl</p>
<p>However, in the ConfigFiles list, the Lego-related files all refer to LegoPhantom 2 and Lego Phantom 3. Could you advise on which one is closer to the first version LegoPhantom?</p>

---

## Post #4 by @Sunderlandkyl (2023-02-24 19:38 UTC)

<p>I’ve found the config file on our data server and added it to PlusLibData: <a href="https://github.com/PlusToolkit/PlusLibData/blob/master/ConfigFiles/PlusConfiguration_Sonix_Ascension_LegoPhantom.xml" class="inline-onebox" rel="noopener nofollow ugc">PlusLibData/PlusConfiguration_Sonix_Ascension_LegoPhantom.xml at master · PlusToolkit/PlusLibData · GitHub</a>.</p>

---
