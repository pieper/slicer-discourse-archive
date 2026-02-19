---
topic_id: 23754
title: "Slicer 5 0 Summary Highlights And Changelog"
date: 2022-07-28
url: https://discourse.slicer.org/t/23754
---

# Slicer 5.0: Summary, Highlights and Changelog

**Topic ID**: 23754
**Date**: 2022-07-28
**URL**: https://discourse.slicer.org/t/slicer-5-0-summary-highlights-and-changelog/23754

---

## Post #1 by @jcfr (2022-07-28 14:12 UTC)

<h1><a name="p-79088-table-of-contents-1" class="anchor" href="#p-79088-table-of-contents-1" aria-label="Heading link"></a>Table of Contents</h1>
<ul>
<li><a href="#heading--summary">Summary</a></li>
<li><a href="#heading--highlights">Highlights</a></li>
<li><a href="https://discourse.slicer.org/t/slicer-5-0-summary-highlights-and-changelog/23754/2">Detailed Changelog</a></li>
</ul>
<h1 id="heading--summary">Summary</h1>
<p>The community of 3D Slicer developers is proud to announce that version 5.0 is<a href="http://download.slicer.org/"> now available for download</a>. This version introduces hundreds of feature enhancements and bug fixes for better performance and stability. It includes many new-and-improved core modules and more than 40 new-and-improved extensions.  Many of these features have been available for months to users of the Slicer Preview version, but now there is a release that developers and users can rely on for stability and maintenance.</p>
<p>3D Slicer 5.0 builds on the success of the version 4 with over one million downloads of the core program and 5.3 million downloads of extensions during the last decade.</p>
<p>The development of 3D Slicer—including its numerous modules, extensions, datasets, pull requests, patches, issues reports, suggestions—is made possible by users, developers, contributors and commercial partners around the world. 3D Slicer is based on a stack of open-source softwares and we are working constantly on <a href="https://discourse.slicer.org/t/slicer-5-0-summary-highlights-and-changelog/23754/2#heading--dependencies">updating</a> the underlying packages. This development is funded by various grants and agencies. For more details, please see the 3D Slicer <a href="https://slicer.readthedocs.io/en/latest/user_guide/about.html#acknowledgments">Acknowledgments</a> page.</p>
<p>One of the main distinguishing features of 3D Slicer is its easy extensibility enabled by good quality documentation, a thriving community, cross-platform support &amp; open source code. 3D Slicer supports a number of extension types which offer a different mix of simplicity and range of control of the software.<br>
A rigorous quality assurance system leveraging automated testing and user <a href="https://discourse.slicer.org">feedback</a> ensures the timely detection of issues caused by ongoing work in different components of the platform. See the <a href="https://slicer.readthedocs.io/en/5.0/developer_guide/contributing.html">contributing guidelines</a></p>
<p><a href="https://www.slicer.org/">slicer.org</a> is the portal to the application, training materials, and the development community.</p>
<p>The <a href="https://slicer.readthedocs.io/en/5.0/user_guide/getting_started.html#tutorials">Slicer Tutorials</a> page provides a series of tutorials and data sets for training in the use of Slicer.</p>
<p><em>Please note that Slicer continues to be a research package and is not intended for clinical use (clinical users must obtain the necessary ethics or regulatory approvals).</em></p>
<h1 id="heading--highlights">Highlights</h1>
<h2 id="heading--highlights--markups">Markups improvements</h2>
<ul>
<li>
<p>New built-in markups types<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a04a8acd505292b564841be4f1cd0a3b3dd9d5c.png" alt="unnamed (1)" data-base62-sha1="jGXS638vev8Oc8bLaKT6RGkoC9m" width="512" height="83"></p>
</li>
<li>
<p>Support for <a href="https://slicer.readthedocs.io/en/5.0/user_guide/modules/markups.html">computing markups measurements</a> (<code>length</code> for line and curve, <code>angle</code> for angle markups, <code>curvature mean</code> and <code>curvature max</code> for curve markups and <code>area</code> for plane and curve markups)<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e4c444ebba4681f210fdfb150778f200557e537.png" data-download-href="/uploads/short-url/4k1IX2egL9Fz3XMDTSmYPY19cB9.png?dl=1" title="unnamed"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/e/1e4c444ebba4681f210fdfb150778f200557e537.png" alt="unnamed" data-base62-sha1="4k1IX2egL9Fz3XMDTSmYPY19cB9" width="317" height="178"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">unnamed</span><span class="informations">512×313 64.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>New <strong>interaction handles</strong> for translating, rotating and scaling markups from 2D and 3D views.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d822ebba53acc114bbf26b2ef4aef47b54477a6.png" data-download-href="/uploads/short-url/b3FGa7IAqQDGznqs17W7eaVGSV0.png?dl=1" title="unnamed (2)"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4d822ebba53acc114bbf26b2ef4aef47b54477a6.png" alt="unnamed (2)" data-base62-sha1="b3FGa7IAqQDGznqs17W7eaVGSV0" width="317" height="178"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">unnamed (2)</span><span class="informations">423×238 13.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><strong>Pluggable markups infrastructure</strong>: The infrastructure has been generalized to enable developers add new markup types in extensions. For example, the <a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup/tree/master#surfacemarkup-extension-for-3d-slicer">SurfaceMarkups extension</a> adds editable NURBS surfaces for modelling thin objects.</p>
</li>
</ul>
<h2 id="heading--highlights--ai">Artificial Intelligence support</h2>
<h3 id="heading--highlights--monai-label">MONAILabel extension</h3>
<p>The <a href="https://github.com/Project-MONAI/MONAILabel/tree/main/plugins/slicer#readme">MONAILabel extension</a> builds on the very popular MONAI toolkit for building AI models for automatic segmentation of medical images. The extension allows users to segment images (using classic and AI-assisted Segment Editor effects) and uses these data sets to train an AI model. MONAILabel can be set up without a dedicated server, on any computer with a strong GPU.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f763b0eac2ea77146b0902aeaeb573ee81e9090d.jpeg" data-download-href="/uploads/short-url/zivwnWSkdK7JUM8fiyvr8Prq7gh.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f763b0eac2ea77146b0902aeaeb573ee81e9090d_2_517x282.jpeg" alt="image" data-base62-sha1="zivwnWSkdK7JUM8fiyvr8Prq7gh" width="517" height="282" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f763b0eac2ea77146b0902aeaeb573ee81e9090d_2_517x282.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f763b0eac2ea77146b0902aeaeb573ee81e9090d_2_775x423.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/7/f763b0eac2ea77146b0902aeaeb573ee81e9090d_2_1034x564.jpeg 2x" data-dominant-color="67666E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1965×1071 260 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is the most popular framework for users who want to train their own AI models for image segmentation.</p>
<p>3D Slicer and MONAI Label were highlighted by the CEO of NVIDIA during his <a href="https://www.youtube.com/watch?v=39ubNuxnrK8&amp;t=2955s">2022 GCT Keynote Address</a> as the suggested tools for working with DICOM data.</p>
<h3 id="heading--highlights--ai-nvidia-aiaa">NVIDIA AI-assisted annotation extension</h3>
<p>The new Slicer extension <a href="https://github.com/NVIDIA/ai-assisted-annotation-client/blob/master/slicer-plugin/README.md">Nvidia AI-assisted annotation (AIAA)</a> adds a new effect in the Segment Editor module.</p>
<p>Example result of automatic segmentation:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/778952fdecd6c918e10d422749b4038e955ef0e4.jpeg" data-download-href="/uploads/short-url/h3t29nlZRJYSGFlrppAHB56m884.jpeg?dl=1" title="snapshot"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/778952fdecd6c918e10d422749b4038e955ef0e4_2_517x320.jpeg" alt="snapshot" data-base62-sha1="h3t29nlZRJYSGFlrppAHB56m884" width="517" height="320" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/778952fdecd6c918e10d422749b4038e955ef0e4_2_517x320.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/778952fdecd6c918e10d422749b4038e955ef0e4_2_775x480.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/778952fdecd6c918e10d422749b4038e955ef0e4_2_1034x640.jpeg 2x" data-dominant-color="6A6F74"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">snapshot</span><span class="informations">1412×875 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>A community-supported AI segmentation server is provided for Slicer users to allow easy evaluation of the extension, without the need for users to have access to a computer with a strong GPU. The server hosts a number of trained models for segmentation of liver, lungs, brain tumor, etc. This extension is recommended quick evaluation and for users who find the already available pre-trained models suitable for their work. For creating new AI models, MONAILabel extension is recommended.</p>
<h3 id="heading--highlights--ai-custom">More AI tools deployed via 3D Slicer</h3>
<p>Several other AI-assisted extensions are added to the Extensions Manager, including:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://discourse.slicer.org/t/new-extension-hdbrainextraction-for-ai-based-skull-stripping/24420">HD Brain Extraction Tool</a></td>
<td>HD-BET skull stripping tool from DKFZ/Heidelberg</td>
</tr>
<tr>
<td><a href="https://discourse.slicer.org/t/submillimetric-covid-19-ct-dataset-and-automatic-lung-tissue-labeling-extension/16007">DensityLungSegmentation</a></td>
<td>AI-based lung segmentation</td>
</tr>
<tr>
<td><a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation">RVXLiverSegmentation</a></td>
<td>AI-based liver segmentation</td>
</tr>
<tr>
<td><a href="https://github.com/SlicerIGT/aigt">SlicerAIGT</a></td>
<td>Real-time ultrasound and optical image stream segmentation and volume reconstruction</td>
</tr>
<tr>
<td><a href="https://github.com/fepegar/SlicerPyTorch">SlicerPyTorch</a></td>
<td>Helper extension for installing Pytorch, used by extensions that require PyTorch</td>
</tr>
<tr>
<td><a href="https://torchio.readthedocs.io/interfaces/slicer.html">TorchIO</a></td>
<td>Graphical user interface for the TorchIO AI helper toolkit</td>
</tr>
</tbody>
</table>
</div><h2 id="heading--highlights--dicom">DICOM improvements</h2>
<ul>
<li>
<p><strong><a href="https://discourse.slicer.org/t/new-dicom-browser-is-ready/8819">Reworked DICOM browser</a></strong> including performance and UI improvements.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/a/3ae29c85410d86044c1c04dc6d4dd1d816530e64.png" data-download-href="/uploads/short-url/8oVcLOZ25tQt0tBUplXzAog5ebG.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3ae29c85410d86044c1c04dc6d4dd1d816530e64_2_517x240.png" alt="image" data-base62-sha1="8oVcLOZ25tQt0tBUplXzAog5ebG" width="517" height="240" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3ae29c85410d86044c1c04dc6d4dd1d816530e64_2_517x240.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3ae29c85410d86044c1c04dc6d4dd1d816530e64_2_775x360.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/a/3ae29c85410d86044c1c04dc6d4dd1d816530e64_2_1034x480.png 2x" data-dominant-color="E5E0E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2234×1041 275 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p>New <strong><a href="https://discourse.slicer.org/t/new-dicomweb-features-launch-slicer-from-web-browser-and-download-upload-data-sets-to-the-cloud-using-dicomweb/17811">DICOMweb features</a></strong> allowing to launch Slicer from web browser and download/upload data sets to the cloud using DICOMweb.</p>
</li>
</ul>
<h2 id="heading--highlights--dicom">Cloud/Web support</h2>
<ul>
<li><a href="https://slicer.readthedocs.io/en/5.0/user_guide/modules/webserver.html">WebServer</a> module is added with the following features:
<ul>
<li>allow Slicer features to be accessed via web requests using a <strong>REST API</strong></li>
<li>expose the Slicer DICOM database content via <strong>DICOMweb interface</strong></li>
<li>serve webpages to allow <strong>hosting simple web applications</strong> directly in Slicer</li>
</ul>
</li>
<li>Slicer can be <a href="https://discourse.slicer.org/t/new-dicomweb-features-launch-slicer-from-web-browser-and-download-upload-data-sets-to-the-cloud-using-dicomweb/17811"><strong>launched from a web browser</strong></a> to load a selected study, for example from <a href="https://www.bing.com/ck/a?!&amp;&amp;p=f9ab40f9943b9df8JmltdHM9MTY1ODUyOTE2MyZpZ3VpZD1kNDExOTIzMS03ZjlmLTQ5NWYtYmQ1Mi04ZGI3MmZiZmZlNTkmaW5zaWQ9NTEyOQ&amp;ptn=3&amp;hsh=3&amp;fclid=33b7352e-0a0e-11ed-8c0d-25a332862e01&amp;u=a1aHR0cHM6Ly9raGVvcHMub25saW5lLw&amp;ntb=1">Kheops</a></li>
<li>Multiple <strong>docker images</strong> are provided to run Slicer in docker containers, with <a href="https://github.com/SlicerMorph/SlicerMorphCloud">CPU rendering and with GPU accelerated rendering</a>; standalone or as a <a href="https://github.com/Slicer/SlicerDocker/tree/main/slicer-notebook">Jupyter kernel</a> (with JupyterHub compatible interface).</li>
<li>Slicer is compatible with AWS AppStreaming for cloud-hosted virtual workstation.  This was used for <a href="https://discourse.slicer.org/t/monailabel-3d-slicer-for-cloud-computing-workshop-jan-12-2022-2-4-est/21152">MONAI Label training workshops</a>.</li>
<li>SlicerVR can be used with <a href="https://vimeo.com/user26958043/review/678951613/08807e6148">NVIDIA CloudXR on cloud-hosted machines</a></li>
</ul>
<h2 id="heading--highlights--extensions-manager">Extensions Manager improvements</h2>
<p>We have implemented some long-awaited improvements in the Extensions Manager in Slicer-5.0.3. Most importantly extensions can be updated automatically and bookmarks can be used for convenient reinstallation of a list of extensions across different Slicer versions, computers, or users.</p>
<p>For the list of new features as well as usability, stability and performance improvements. See <a href="https://discourse.slicer.org/t/new-feature-automatic-update-of-extensions/24416">New feature: Automatic update of extensions</a></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9a8ea12cc91915200ca009e077a4de52a9e3772.jpeg" data-download-href="/uploads/short-url/v3vvwkMJ3qkBzehOG6Renc2vpnk.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9a8ea12cc91915200ca009e077a4de52a9e3772.jpeg" alt="image" data-base62-sha1="v3vvwkMJ3qkBzehOG6Renc2vpnk" width="480" height="360"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">480×360 41.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h2 id="heading--highlights--translation-workflow">Translation (internationalization) support</h2>
<p>Slicer was awarded a <a href="https://discourse.slicer.org/t/czi-essential-open-source-software-for-science-eoss-award-for-3d-slicer-internationalization/19500">CZI Essential Open Source Software grant for <strong>translation</strong> of the application and extensions</a> to French and develop infrastructure for allowing translation to any other languages. This is still a work in progress (expected to be complete in September 2023), but language selection and translation of a large part of the displayed text in the Slicer core application is already translatable.</p>
<ul>
<li>
<p><a href="https://github.com/Slicer/SlicerLanguagePacks#readme">LanguagePacks</a> extension is provided for creating, editing, and storing translations for Slicer core and extensions.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/0/e04b742db26b40276eac25131bf949d5a7bfb8d4.png" data-download-href="/uploads/short-url/w0cBYfO2pYBJzNL3c4YJB80IPI0.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e04b742db26b40276eac25131bf949d5a7bfb8d4_2_517x288.png" alt="image" data-base62-sha1="w0cBYfO2pYBJzNL3c4YJB80IPI0" width="517" height="288" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e04b742db26b40276eac25131bf949d5a7bfb8d4_2_517x288.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e04b742db26b40276eac25131bf949d5a7bfb8d4_2_775x432.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e04b742db26b40276eac25131bf949d5a7bfb8d4_2_1034x576.png 2x" data-dominant-color="7797BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1951×1090 258 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
</li>
<li>
<p><a href="https://discourse.slicer.org/t/czi-essential-open-source-software-for-science-eoss-award-for-3d-slicer-internationalization/19500/19#h-1-switch-to-weblate-1">Weblate online collaborative translation system</a> is used for for crowdsourcing translation work to the Slicer community.</p>
</li>
</ul>
<h2 id="heading--highlights--infrastructure">Infrastructure improvements</h2>
<ul>
<li>
<p><strong>Redesigned documentation website</strong> and improve documentation workflow</p>
<ul>
<li>Transitioned user and developer guides from mediawiki to readthedocs allowing to contribute, maintain and preview updates along side the Slicer source code.</li>
</ul>
<details>
<summary>
Click to compare Before and After</summary>
<div class="md-table">
<table>
<thead>
<tr>
<th>Before</th>
<th>After</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e3713c36f98213af615a1a88ad1e142d9045a5a7.jpeg" data-download-href="/uploads/short-url/ws2ZrRlbiezffUAlswhNRmhppwX.jpeg?dl=1" title=""><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3713c36f98213af615a1a88ad1e142d9045a5a7_2_690x383.jpeg" alt="" data-base62-sha1="ws2ZrRlbiezffUAlswhNRmhppwX" role="presentation" width="690" height="383" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3713c36f98213af615a1a88ad1e142d9045a5a7_2_690x383.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3713c36f98213af615a1a88ad1e142d9045a5a7_2_1035x574.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/3/e3713c36f98213af615a1a88ad1e142d9045a5a7_2_1380x766.jpeg 2x" data-dominant-color="F6F7F8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">1920×1066 156 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td></td>
</tr>
</tbody>
</table>
</div></details>
</li>
<li>
<p><strong>Revamped <a href="https://slicer.org">landing page</a></strong></p>
<ul>
<li>Improved search engine indexing and social networks integration by adding relevant metadata tags</li>
<li>Mobile “friendly” landing page</li>
<li>Improvements to the landing page can be proposed and previewed on GitHub at <a href="https://github.com/Slicer/slicer.org#readme">Slicer/slicer.org</a></li>
<li>The new website was collaboratively developed by the Slicer community<br>
between July 2020 and March 2021. See <a href="https://discourse.slicer.org/t/its-all-about-transitions-lets-talk-about-slicers-landing-page/113/44">here</a>.</li>
</ul>
<details>
<summary>
Click to compare Before and After</summary>
<div class="md-table">
<table>
<thead>
<tr>
<th>Before</th>
<th>After</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2a33c544eef2393baf88aeded966150563be11b.jpeg" data-download-href="/uploads/short-url/yCthh5NKIYv3PntJBWN2FBJKdAL.jpeg?dl=1" title=""><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2a33c544eef2393baf88aeded966150563be11b_2_453x500.jpeg" alt="" data-base62-sha1="yCthh5NKIYv3PntJBWN2FBJKdAL" role="presentation" width="453" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2a33c544eef2393baf88aeded966150563be11b_2_453x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2a33c544eef2393baf88aeded966150563be11b_2_679x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/2/f2a33c544eef2393baf88aeded966150563be11b_2_906x1000.jpeg 2x" data-dominant-color="D6D6D7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">1544×1702 250 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td></td>
</tr>
</tbody>
</table>
</div></details>
</li>
<li>
<p><strong>Redesigned Slicer logo</strong></p>
<ul>
<li>Assets are currently organized in this public <a href="https://drive.google.com/drive/u/0/folders/1dh7O6PNdh5EkePtwyjFREfjUdsaxrrai">Google folder</a>.</li>
<li>The discussions leading to the new design are available on discourse <a href="https://discourse.slicer.org/t/proposed-new-slicer-logo/11295">here</a>.</li>
<li>See issue <a href="https://github.com/Slicer/Slicer/issues/6161">#6161</a> for proposal to better organize Slicer logos material.</li>
</ul>
<details>
<summary>
Click to compare Before and After</summary>
<div class="md-table">
<table>
<thead>
<tr>
<th>Before</th>
<th>After</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5f3b367a8bd0cdd9a42812ca797892b6e1eac0c.png" data-download-href="/uploads/short-url/z5N6CBtHy6OyeRuuEFX7aJ0uUfq.png?dl=1" title=""><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5f3b367a8bd0cdd9a42812ca797892b6e1eac0c.png" alt="" data-base62-sha1="z5N6CBtHy6OyeRuuEFX7aJ0uUfq" role="presentation" width="201" height="204"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">201×204 16.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td></td>
</tr>
</tbody>
</table>
</div></details>
</li>
<li>
<p><strong>Improved</strong> frontend for searching and downloading extensions. See <a href="https://extensions.slicer.org">https://extensions.slicer.org</a></p>
<ul>
<li>Source code of the site available at <a href="https://github.com/KitwareMedical/slicer-extensions-webapp">KitwareMedical/slicer-extensions-webapp</a></li>
</ul>
<details>
<summary>
Click to compare Before and After</summary>
<div class="md-table">
<table>
<thead>
<tr>
<th>Before</th>
<th>After</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6de2042f77cf616431ca9cd6d8e95965d76051ea.png" data-download-href="/uploads/short-url/fG4hui8WKftLdF3AsvqAxpnRZgK.png?dl=1" title=""><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6de2042f77cf616431ca9cd6d8e95965d76051ea_2_459x499.png" alt="" data-base62-sha1="fG4hui8WKftLdF3AsvqAxpnRZgK" role="presentation" width="459" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6de2042f77cf616431ca9cd6d8e95965d76051ea_2_459x499.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/d/6de2042f77cf616431ca9cd6d8e95965d76051ea_2_688x748.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6de2042f77cf616431ca9cd6d8e95965d76051ea.png 2x" data-dominant-color="D3D9DD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">913×994 284 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td></td>
</tr>
</tbody>
</table>
</div></details>
</li>
<li>
<p>Updated <a href="https://download.slicer.org/">download.slicer.org</a>.</p>
<ul>
<li>Source code of the site available at <a href="https://github.com/Slicer/slicer_download">Slicer/slicer_download</a></li>
<li>Learn about the history <a href="https://github.com/Slicer/slicer_download#history">here</a>.</li>
</ul>
<details>
<summary>
Click to compare Before and After</summary>
<div class="md-table">
<table>
<thead>
<tr>
<th>Before</th>
<th>After</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a61b149973db268b5889b5171e37acb1bbadd2f.png" data-download-href="/uploads/short-url/aC0DyP6uIOJff9fUMdAHiXxGV3N.png?dl=1" title=""><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a61b149973db268b5889b5171e37acb1bbadd2f_2_437x500.png" alt="" data-base62-sha1="aC0DyP6uIOJff9fUMdAHiXxGV3N" role="presentation" width="437" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a61b149973db268b5889b5171e37acb1bbadd2f_2_437x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a61b149973db268b5889b5171e37acb1bbadd2f_2_655x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a61b149973db268b5889b5171e37acb1bbadd2f_2_874x1000.png 2x" data-dominant-color="F4F4F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">1468×1679 308 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></td>
<td></td>
</tr>
</tbody>
</table>
</div></details>
</li>
<li>
<p>Updated backend infrastructure for <strong>managing and organizing Slicer application and extension packages</strong>.</p>
<ul>
<li>The new infrastructure was designed built on Girder to scale and support management of packages associated with custom Slicer-based applications.</li>
<li>See <a href="https://slicer-packages.kitware.com/">https://slicer-packages.kitware.com/</a> and <a href="https://github.com/girder/slicer_package_manager">girder/slicer_package_manager</a></li>
</ul>
</li>
</ul>
<h2 id="heading--highlights--other">Other improvements</h2>
<ul>
<li>
<p>Integration with the Python ecosystem. See details in the <a href="#heading--scripting">Scripting</a> and <a href="#heading--dependencies">Dependencies</a> sections below</p>
</li>
<li>
<p>Library updates. See details in the <a href="#heading--dependencies">Dependencies</a> section below</p>
</li>
<li>
<p><strong>More than 40 new extensions</strong> have been added. See complete list in the <a href="#heading--extensions">Extensions</a> section below.</p>
</li>
<li>
<p>Although we have a common understanding about how to conduct operations in the Slicer community, consensus was reached and we now formally <a href="https://discourse.slicer.org/t/code-of-conduct-document/17663">adopted a code of conduct</a>.</p>
</li>
</ul>

---

## Post #2 by @Sam_Horvath (2022-07-28 14:12 UTC)

<h1 id="heading--changelog">Changelog</h1>
<ul>
<li>
<a href="#heading--core">Core</a>
<ul>
<li><a href="#heading--application">Application</a></li>
<li><a href="#heading--extension">Extension</a></li>
<li><a href="#heading--scripting">Scripting</a></li>
<li><a href="#heading--internationalizationlocalization">Internationalization/Localization </a></li>
<li><a href="#heading--installation">Installation</a></li>
<li><a href="#heading--io">IO</a></li>
<li><a href="#heading--rendering-and-display">Rendering and display</a></li>
<li><a href="#heading--registration">Registration</a></li>
</ul>
</li>
<li>
<a href="#heading--new-modules">New Modules</a>
<ul>
<li><a href="#heading--text">Text</a></li>
<li><a href="#heading--sequences">Sequences</a></li>
<li><a href="#heading--lights">Lights</a></li>
</ul>
</li>
<li>
<a href="#heading--improved-modules">Improved Modules</a>
<ul>
<li><a href="#heading--markups">Markups</a></li>
<li><a href="#heading--dicom">DICOM</a></li>
<li><a href="#heading--models">Models</a></li>
<li><a href="#heading--segmentations">Segmentations</a></li>
</ul>
</li>
<li>
<a href="#heading--infrastructure">Infrastructure</a>
<ul>
<li><a href="#heading--build-system">Build system</a></li>
<li><a href="#heading--platform-support">Platform support</a></li>
<li><a href="#heading--dependencies">Dependencies</a></li>
</ul>
</li>
<li>
<a href="#heading--extensions">Extensions</a>
<ul>
<li><a href="#heading--extensions-new">New</a></li>
<li><a href="#heading--extensions-updated">Updated</a></li>
<li><a href="#heading--extensions-removed">Removed</a></li>
</ul>
</li>
</ul>
<h2 id="heading--core">Core</h2>
<h3 id="heading--application">Application</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/new-module-finder-for-selecting-modules/12356">Revamped module finder!</a></li>
<li><a href="https://discourse.slicer.org/t/touchscreen-and-trackpad-interactions/7557">Improved touch screen and trackpad support</a></li>
</ul>
<h3 id="heading--extension">Extension</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/new-feature-automatic-update-of-extensions/24416">New feature: Automatic update of extensions</a></li>
</ul>
<h3 id="heading--scripting">Scripting</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/use-full-power-of-python-in-slicer/7162">Slicer now uses Python 3!</a></li>
<li>Slicer’s python is now binary-compatible with pypi packages</li>
<li>Users can install most packages using <code>slicer.util.pip_install</code>
</li>
</ul>
<h3 id="heading--installation">Installation</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/slicer-is-now-fully-portable/15410">Slicer installation is now fully portable</a></li>
<li><a href="https://discourse.slicer.org/t/slicer-can-be-installed-without-administrator-privileges-on-windows/7137">User-space install on Windows</a></li>
</ul>
<h3 id="heading--internationalizationlocalization">Internationalization/Localization</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/slicer-switches-to-utf-8-everywhere/10374">Improved support for utf-8 character strings</a></li>
</ul>
<h3 id="heading--io">IO</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/compressed-video-support-in-slicer/9194">Compressed video support</a></li>
<li><a href="https://discourse.slicer.org/t/new-export-functionality/20950">Export nodes from data module</a></li>
</ul>
<h3 id="heading--rendering-and-display">Rendering &amp; Display</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/new-feature-basic-support-for-physically-based-rendering-pbr/21725">New support for basic physically based rendering (PBR)</a></li>
<li><a href="https://discourse.slicer.org/t/interactive-slice-intersections/21677">Interactive Slice Intersections</a></li>
<li><a href="https://discourse.slicer.org/t/color-scalar-bar-reworked-and-upgraded-now-it-s-called-color-legend/21567">Updated Color Scalar Bar</a></li>
<li><a href="https://discourse.slicer.org/t/new-feature-configurable-volume-display-presets-in-right-click-menu-and-volumes-module/20640">Volume display presets</a></li>
<li><a href="https://discourse.slicer.org/t/color-rgb-volume-rendering/19732">Improved RGB volume rendering</a></li>
<li><a href="https://discourse.slicer.org/t/new-feature-maximize-view/19581">View maximization</a></li>
<li><a href="https://discourse.slicer.org/t/tilt-lock-in-3d-view/18801">3D view tilt lock</a></li>
<li><a href="https://discourse.slicer.org/t/new-feature-surface-rendering-with-ambient-shadows-for-improved-depth-perception/16903">Surface rendering with ambient shadows</a></li>
<li><a href="https://discourse.slicer.org/t/how-to-make-fiducial-points-placed-in-curved-planar-reformatted-image-appear-in-the-original-image/12189">Improved curved planar reformat</a></li>
<li><a href="https://discourse.slicer.org/t/new-lightbox-contact-image-mode-in-screen-capture-module/10840">New lightbox image mode in Screen Capture</a></li>
<li><a href="https://discourse.slicer.org/t/watermark-feature/8252">3D view watermark</a></li>
<li><a href="https://discourse.slicer.org/t/recent-improvements-in-window-level-management/7284">Improved window/level management</a></li>
</ul>
<h3 id="heading--registration">Registration</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/partial-surface-registration-tutorial/21118/4">Partial Surface Registration Videotutorial</a></li>
</ul>
<h2 id="heading--new-modules">New Modules</h2>
<h3 id="heading--text">Text</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/new-module-texts/9196">Texts module</a></li>
</ul>
<h3 id="heading--sequences">Sequences</h3>
<ul>
<li><a href="https://github.com/Slicer/Slicer/pull/4810">Sequences module moved into Slicer core</a></li>
</ul>
<h3 id="heading--lights">Lights</h3>
<ul>
<li>
<p><a href="https://discourse.slicer.org/t/new-module-to-customize-lighting-in-3d-view/8804">Lights module  to customize lighting in 3D view</a></p>
</li>
<li>
<p>Lights module enables <a href="https://discourse.slicer.org/t/new-feature-surface-rendering-with-ambient-shadows-for-improved-depth-perception/16903">Surface rendering with ambient shadows</a>:</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Without ambient-shadows</th>
<th>With ambient-shadows</th>
</tr>
</thead>
<tbody>
<tr>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/5/d5b1b2696b36c992db322a3947672475de011b74.jpeg" data-download-href="/uploads/short-url/uuqpJEIfx9mNKBePVXM4eLnIGJS.jpeg?dl=1" title=""><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5b1b2696b36c992db322a3947672475de011b74_2_446x500.jpeg" alt="" data-base62-sha1="uuqpJEIfx9mNKBePVXM4eLnIGJS" role="presentation" width="446" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5b1b2696b36c992db322a3947672475de011b74_2_446x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5b1b2696b36c992db322a3947672475de011b74_2_669x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/5/d5b1b2696b36c992db322a3947672475de011b74_2_892x1000.jpeg 2x" data-dominant-color="4B2420"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">937×1049 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></td>
<td><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/334f2aa455c2ddd26ad6a963ac8620fcdf37c28d.jpeg" data-download-href="/uploads/short-url/7jTXNS5tSDqM8w2Ej32TOiFcOsd.jpeg?dl=1" title=""><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/334f2aa455c2ddd26ad6a963ac8620fcdf37c28d_2_449x500.jpeg" alt="" data-base62-sha1="7jTXNS5tSDqM8w2Ej32TOiFcOsd" role="presentation" width="449" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/334f2aa455c2ddd26ad6a963ac8620fcdf37c28d_2_449x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/334f2aa455c2ddd26ad6a963ac8620fcdf37c28d_2_673x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/334f2aa455c2ddd26ad6a963ac8620fcdf37c28d_2_898x1000.jpeg 2x" data-dominant-color="371C19"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename"></span><span class="informations">944×1051 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></td>
</tr>
</tbody>
</table>
</div>
</li>
</ul>
<h2 id="heading--improved-modules">Improved Modules</h2>
<h3 id="heading--markups">Markups</h3>
<ul>
<li>New, better widget infrastructure</li>
<li>New line, curve, angle markups, and more</li>
<li><a href="https://discourse.slicer.org/t/changes-to-the-markups-module/19871">Markups UI improvements</a></li>
<li>
<a href="https://github.com/Slicer/Slicer/pull/5349">Markups pluggable infrastructure</a> - easily create new markups types in other modules</li>
</ul>
<h3 id="heading--dicom">DICOM</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/new-dicomweb-features-launch-slicer-from-web-browser-and-download-upload-data-sets-to-the-cloud-using-dicomweb/17811">New DICOMWeb features</a></li>
<li>
<a href="https://discourse.slicer.org/t/new-dicom-browser-is-ready/8819">Reworked DICOM browser</a>  to make it more responsive and display more relevant information. Additionally, the browser is now <a href="https://discourse.slicer.org/t/dicom-browser-layout/8148">embedded in the layout</a> rather than as a popup window.</li>
<li><a href="https://discourse.slicer.org/t/load-ge-invenia-abus-images-from-dicom/15067/11">New GE Invenia ABUS plugin</a></li>
</ul>
<h3 id="heading--models">Models</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/improvements-in-atlas-management-model-hierarchy-refactoring/8512">Revamp of Models module with improved model hierarchies</a></li>
<li><a href="https://discourse.slicer.org/t/new-experimental-feature-boolean-operations-union-intersection-difference-on-meshes/16048">Boolean mesh operations</a></li>
<li><a href="https://discourse.slicer.org/t/new-decimation-methods-added-quadric-and-fast-quadric/12729">New mesh decimation methods</a></li>
<li>
<a href="https://discourse.slicer.org/t/new-module-dynamic-modeler-parametric-surface-editing-for-biomedical-applications/11759">Dynamic Modeler - many new mesh operations</a>
<ul>
<li><a href="https://discourse.slicer.org/t/new-dynamic-modeler-tool-select-by-points/22165/1">Select by Points</a></li>
</ul>
</li>
<li><a href="https://discourse.slicer.org/t/model-files-are-now-saved-in-lps-coordinate-system/10446">Models are saved in LPS coordinate system by default</a></li>
</ul>
<h3 id="heading--segmentations">Segmentations</h3>
<ul>
<li><a href="https://discourse.slicer.org/t/new-segment-editor-layout-vertical-effect-toolbar/19649">New vertical toolbar layout</a></li>
<li><a href="https://discourse.slicer.org/t/new-apply-to-all-segments-checkbox-available-in-margin-hollow-smoothing-and-scissors-effect/18587">Apply operations to all segments support</a></li>
<li><a href="https://discourse.slicer.org/t/new-module-for-cross-section-area-measurement/11429">Compute cross section area of segments</a></li>
<li><a href="https://discourse.slicer.org/t/new-segment-statistics-oriented-bounding-box-diameter-and-more/10203">New statistics added</a></li>
<li><a href="https://discourse.slicer.org/t/new-feature-histogram-for-setting-threshold-range-in-segment-editor/9221">Histogram based thresholding</a></li>
<li><a href="https://discourse.slicer.org/t/new-feature-shared-labelmap-segmentations/8814">Shared label maps</a></li>
<li><a href="https://discourse.slicer.org/t/new-feature-search-and-filter-in-segments-table/7827">Search and filter segments in table</a></li>
<li>Introduction of new segment editor effects
<ul>
<li><a href="https://discourse.slicer.org/t/new-segment-editor-feature-added-split-volume/7324">Split volume</a></li>
<li><a href="https://discourse.slicer.org/t/new-segment-editor-effect-local-threshold/9233">Local threshold</a></li>
<li><a href="https://discourse.slicer.org/t/fill-or-extract-cavities-in-segmentations-using-the-new-wrap-solidify-effect/11248">Create solid segments</a></li>
<li><a href="https://discourse.slicer.org/t/new-text-engrave-emboss-effect-in-segment-editor/12013">Text engrave/emboss</a></li>
<li><a href="https://discourse.slicer.org/t/new-segment-editing-feature-smoothing-brush/14577">Smoothing brush</a></li>
</ul>
</li>
</ul>
<h2 id="heading--infrastructure">Infrastructure</h2>
<h3 id="heading--build-system">Build System</h3>
<ul>
<li>Embrace C++11 for coding style</li>
<li>Remove last remnants of TCL support. See details in <a href="#heading--dependencies">dependencies</a>
</li>
</ul>
<h3 id="heading--platform-support">Platform Support</h3>
<ul>
<li>Support for building on newer Mac OSX (10.15+) and newer Linux builds (Ubuntu 18.04+)</li>
</ul>
<h3 id="heading--dependencies">Dependencies</h3>
<ul>
<li>
<p>Python wheels integration</p>
<ul>
<li>
<p>Most recent python packages (at the time of the release) are installed using <a href="https://pypi.org/">PyPI (Python Package Index)</a> wheels. Relevant SHA256 hashes are specified for each supported platforms.</p>
</li>
<li>
<p>Re-organization of python external projects as <code>External_python-&lt;project&gt;.cmake</code> and   <code>External_python-&lt;project&gt;-requirements.cmake</code></p>
</li>
<li>
<p>Introduction of maintenance script <a href="https://github.com/Slicer/Slicer/blob/v5.0.3/Utilities/Scripts/python_package_updater.py">python_package_updater.py</a> to update external python project files with the latest package version along with corresponding download hashes.</p>
</li>
</ul>
</li>
<li>
<p>Updated dependencies</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Update</th>
<th>from</th>
<th>to</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>DCMTK</td>
<td>
<code>v3.6.3_20180621</code><br><sup><a href="https://github.com/commontk/DCMTK/commit/22f253424">commontk/DCMTK@22f253424</a></sup>
</td>
<td>
<code>DCMTK-3.6.6_20210115</code><br><sup><a href="https://github.com/commontk/DCMTK/commit/0f9bf4d9e">commontk/DCMTK@0f9bf4d9e</a></sup>
</td>
<td>See release announcements on the <a href="https://forum.dcmtk.org/viewforum.php?f=6&amp;sid=48ce51e66dc6c55e750f89f13d5eb6ba">DCMTK forum</a>.</td>
</tr>
<tr>
<td>curl</td>
<td><code>7.34</code></td>
<td><code>7.70</code></td>
<td></td>
</tr>
<tr>
<td>CTK</td>
<td><a href="https://github.com/commontk/CTK/commit/6cd82aab5f21db7c021e1eb502c9e5161e4a636d">6cd82aab5</a></td>
<td><a href="https://github.com/commontk/CTK/commit/ec816cbb77986f6ee28c41a495e82238dee0e2d3">ec816cbb7</a></td>
<td>See <a href="https://github.com/commontk/CTK/compare/6cd82aab5...ec816cbb7">list of commits</a>.</td>
</tr>
<tr>
<td>ITK</td>
<td>
<code>4.13.1</code><br><sub><a href="https://github.com/Slicer/ITK/commit/87f5d83f1">87f5d83f1</a></sub>
</td>
<td>
<code>5.3rc03</code><br><sub><a href="https://github.com/Slicer/ITK/commit/46a71c744">46a71c744</a></sub>
</td>
<td>See release notes for <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/Documentation/ReleaseNotes/4.13.md">4.13</a>, <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/Documentation/ReleaseNotes/5.0.md">5.0</a>, <a href="https://github.com/InsightSoftwareConsortium/ITK/blob/master/Documentation/ReleaseNotes/5.1.md">5.1</a>, <a href="https://github.com/InsightSoftwareConsortium/ITK/releases/tag/v5.1.1">5.1.1</a>, <a href="https://github.com/InsightSoftwareConsortium/ITK/releases/tag/v5.1.2">5.1.2</a>, <a href="https://github.com/InsightSoftwareConsortium/ITK/releases/tag/v5.2.0">5.2.0</a>, <a href="https://github.com/InsightSoftwareConsortium/ITK/releases/tag/v5.2.1">5.2.1</a>, <a href="https://github.com/InsightSoftwareConsortium/ITK/releases/tag/v5.3rc01">5.3rc01</a>, <a href="https://github.com/InsightSoftwareConsortium/ITK/releases/tag/v5.3rc02">5.3rc02</a> and <a href="https://github.com/InsightSoftwareConsortium/ITK/releases/tag/v5.3rc03">5.3rc03</a>.</td>
</tr>
<tr>
<td>LibArchive</td>
<td>
<code>3.3.3</code><br><sub><a href="https://github.com/Slicer/LibArchive/commit/0737ce70653716995508f4613338410b2eb7f6ec">Slicer/LibArchive@0737ce706</a></sub>
</td>
<td>
<code>3.6.1</code><br><sub><a href="https://github.com/libarchive/libarchive/commit/6c3301111">libarchive/libarchive@6c3301111</a></sub>
</td>
<td></td>
</tr>
<tr>
<td>OpenSSL</td>
<td>
<code>1.0.2n</code> (unix)<br><code>1.0.1h</code> (windows)</td>
<td><code>1.1.1g</code></td>
<td></td>
</tr>
<tr>
<td>qRestAPI</td>
<td><a href="https://github.com/commontk/qRestAPI/commit/ddc0cfcc220d0ccd02b4afdd699d1e780dac3fa3">ddc0cfcc2</a></td>
<td><a href="https://github.com/commontk/qRestAPI/commit/ea5e85a1ecfb05174ab604d66fa3186ae9a45eda">ea5e85a1e</a></td>
<td>Add support for Girder API. See <a href="https://github.com/commontk/qRestAPI/compare/ddc0cfcc2...ea5e85a1e">list of commits</a>
</td>
</tr>
<tr>
<td>SimpleITK</td>
<td>
<code>1.1.0</code><br><sup><a href="https://github.com/Slicer/SimpleITK/commit/e52c9ab047b514ef9584fef475e0ed416ad8fa4a">Slicer/SimpleITK@e52c9ab04</a></sup>
</td>
<td>
<code>2.2rc3</code><br><sup><a href="https://github.com/SimpleITK/SimpleITK/commit/ffd48e274">SimpleITK/SimpleITK@ffd48e274</a></sup>
</td>
<td>See release notes for <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v1.1.0">1.1.0</a>, <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v1.2.0">1.2.0</a>, <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v1.2.1">1.2.1</a>, <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v1.2.2">1.2.2</a>, <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v1.2.3">1.2.3</a>, <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v1.2.4">1.2.4</a>, <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v2.0.0">2.0.0</a>, <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v2.0.1">2.0.1</a>, <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v2.0.2">2.0.2</a>, <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v2.1.0">2.1.0</a>, <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v2.1.1">2.1.1</a>, <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v2.2rc1">2.2rc1</a>, <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v2.2rc2">2.2rc2</a> and <a href="https://github.com/SimpleITK/SimpleITK/releases/tag/v2.2rc3">2.2rc3</a>
</td>
</tr>
<tr>
<td>TBB</td>
<td><code>2018_20171205oss</code></td>
<td><code>2021.5.0</code></td>
<td>See <a href="https://github.com/Slicer/Slicer/pull/5105">PR-5105</a> <sup><code>2018_20171205oss</code> → <code>2019_20191006oss</code></sup>,  <a href="https://github.com/Slicer/Slicer/pull/6405">PR-6405</a> <sup><code>2019_20191006oss</code> → <code>2021.5.0</code></sup> and <a href="https://github.com/oneapi-src/oneTBB/tags">oneTBB releases notes</a>.</td>
</tr>
<tr>
<td>VTK</td>
<td>
<code>8.2.0</code> <br><sup><a href="https://github.com/Slicer/VTK/commit/31dc6a08b">Slicer/VTK@31dc6a08b</a></sup>
</td>
<td>
<code>9.1.20220125</code><br><sup><a href="https://github.com/Slicer/VTK/commit/bccd2b8f7">Slicer/VTK@bccd2b8f7</a></sup>
</td>
<td>See release notes for <a href="https://www.kitware.com/vtk-8-2-0/">8.2</a> , and for <a href="https://gitlab.kitware.com/vtk/vtk/-/tree/master/Documentation/release">9.0 and 9.1</a>.<br>Include backports of selected rendering improvements and OpenXR Holographic Remoting support <sup><a href="https://github.com/Slicer/Slicer/pull/6433">PR-6433</a></sup>.</td>
</tr>
</tbody>
</table>
</div>
</li>
<li>
<p>New dependencies</p>
<div class="md-table">
<table>
<thead>
<tr>
<th></th>
<th>version</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>LibFFI</td>
<td>
<code>v3.4.2</code><br><sup><a href="https://github.com/python-cmake-buildsystem/libffi/tree/libffi-cmake-buildsystem-v3.4.2-2021-06-28-f9ea416">python-cmake-buildsystem/libffi@libffi-cmake-buildsystem-v3.4.2-2021-06-28-f9ea416</a></sup>
</td>
<td>Introduced in <a href="https://github.com/Slicer/Slicer/pull/6026">PR-6026</a> to support building against Python 3.9.10. Our fork <a href="https://github.com/python-cmake-buildsystem/libffi">python-cmake-buildsystem/libffi</a> provides support for building using CMake.</td>
</tr>
<tr>
<td>LZMA</td>
<td><code>5.2.5</code></td>
<td>Introduced in <a href="https://github.com/Slicer/Slicer/pull/5194">PR-5194</a> to support use of <code>lzma</code> python module.</td>
</tr>
<tr>
<td>sqlite</td>
<td><code>3.30.1</code></td>
<td></td>
</tr>
</tbody>
</table>
</div>
</li>
<li>
<p>Updated build-time dependencies</p>
<div class="md-table">
<table>
<thead>
<tr>
<th>Update</th>
<th>from</th>
<th>to</th>
<th></th>
</tr>
</thead>
<tbody>
<tr>
<td>PCRE</td>
<td><code>8.38</code></td>
<td><code>8.44</code></td>
<td>Used to generate SimpleITK Python wrappers.</td>
</tr>
<tr>
<td>Swig</td>
<td><code>3.0.10</code></td>
<td><code>4.0.2</code></td>
<td>Used to generate SimpleITK Python wrappers.</td>
</tr>
</tbody>
</table>
</div>
</li>
<li>
<p>Removed dependencies</p>
<ul>
<li>Removed support for building TCL compatibility layers and associated <code>tk</code>, <code>tcl</code> and <code>incrTcl</code> external projects.</li>
<li>Removed <code>NUMPY</code> and <code>SciPy</code> external projects now installed as python wheels.</li>
</ul>
</li>
</ul>
<h2 id="heading--extensions">Extensions</h2>
<p><em>Listed below are extensions added, removed or updated since the <code>4.10.2</code> release.</em></p>
<p>The Slicer <a href="https://slicer.readthedocs.io/en/latest/user_guide/extensions_manager.html">extensions manager</a> enables Slicer users to install more than 150 extensions written and contributed by their peers from around the world.</p>
<h3 id="heading--extensions-new">New</h3>
<ul>
<li>Segmentation
<ul>
<li><a href="https://github.com/R-Vessel-X/SlicerRVXLiverSegmentation">RVXLiverSegmentation</a></li>
<li><a href="https://github.com/pzaffino/SlicerDensityLungSegmentation">DensityLungSegmentation</a></li>
<li><a href="https://github.com/jmhuie/Slicer-SegmentGeometry">SegmentGeometry</a></li>
<li><a href="https://github.com/rnadkarni2/SlicerBreast_DCEMRI_FTV">Breast DCE-MRI FTV</a></li>
<li><a href="https://github.com/SlicerMicro/Slicer-TITAN">TITAN</a></li>
<li><a href="https://github.com/RivettiLuciano/SlicerT1_ECVMapping">T1_ECVMapping</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/BrainVolumeRefinement">BrainVolumeRefinement</a></li>
</ul>
</li>
<li>Infrastructure / Utilities
<ul>
<li><a href="https://github.com/hina-shah/SlicerBatchAnonymize">SlicerBatchAnonymize</a></li>
<li><a href="https://www.kitware.com/introducing-slicerpipelines-a-coding-free-way-to-create-simple-modules-in-3d-slicer/">SlicerPipelines</a></li>
<li><a href="https://github.com/Slicer/SlicerLanguagePacks">LanguagePacks</a></li>
<li><a href="https://github.com/pieper/SlicerParallelProcessing">Parallel Processing</a></li>
<li><a href="https://githubcomets-vis-interactiveslicerprismrendering.readthedocs.io">SlicerPRISM</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/ImageCompare">ImageCompare</a></li>
<li><a href="https://github.com/PerkLab/SlicerOpenAnatomy">OpenAnatomy</a></li>
<li><a href="https://discourse.slicer.org/t/import-osirix-roi-as-segmentation/10719">Osirix ROI importer</a></li>
<li><a href="https://discourse.slicer.org/t/new-developer-feature-styletester/15509">StyleTester</a></li>
<li><a href="https://discourse.slicer.org/t/new-extension-slicerfreesurfer/12751">FreeSurfer support moved to extension</a></li>
<li><a href="https://discourse.slicer.org/t/new-extension-rawimageguess-for-loading-of-images-from-unrecognized-file-format/9219">RawImageGuess - loading data in unknown formats</a></li>
<li><a href="https://discourse.slicer.org/t/new-module-for-measuring-user-statistics/9220">New module for user statistics</a></li>
</ul>
</li>
<li>Markups
<ul>
<li><a href="https://github.com/koegl/SlicerMRUSLandmarking">MRUSLandmarking</a></li>
<li>
<a href="https://github.com/SlicerHeart/SlicerSurfaceMarkup/tree/master">SurfaceMarkup</a>
<ul>
<li><a href="https://discourse.slicer.org/t/extending-the-markups-module/14882/12">Discourse</a></li>
</ul>
</li>
<li><a href="https://discourse.slicer.org/t/new-module-extract-centerline-in-slicervmtk-extension/12117">Centerline extraction in SlicerVMTK</a></li>
</ul>
</li>
<li>IGT
<ul>
<li><a href="https://discourse.slicer.org/t/new-3d-slicer-extension-for-planning-and-surgical-guide-generation-for-mandibular-bone-reconstruction/17638">Mandibular reconstruction planning and custom surgical guides</a></li>
<li>
<a href="https://github.com/naterex23/SlicerAblationPlanner">SlicerAblationPlanne</a>r</li>
<li><a href="https://github.com/OrthodonticAnalysis/SlicerOrthodonticAnalysis">OrthodonticAnalysis</a></li>
<li><a href="https://github.com/lancelevine/SlicerBreastImplantAnalyzer#breastimplantanalyzer">BreastImplantAnalyzer</a></li>
<li><a href="https://toothandclaw.github.io">Auto3dgm</a></li>
<li><a href="https://cmf.slicer.org/">SlicerCMF</a></li>
<li><a href="https://www.slicer.org/wiki/Documentation/Nightly/Extensions/KidneyStoneCalculator">KidneyStoneCalculator</a></li>
<li><a href="https://discourse.slicer.org/t/new-module-baffle-planner-for-designing-surface-patches/16799">SlicerHeart - Baffle Planner</a></li>
<li><a href="https://discourse.slicer.org/t/new-lungctanalyzer-extension-for-lung-ct-segmentation-and-analysis-for-covid-19-assessment/15006">Lung CT Analyzer</a></li>
</ul>
</li>
<li>Machine learning
<ul>
<li><a href="https://github.com/fepegar/SlicerPyTorch">SlicerPyTorch</a></li>
<li><a href="https://github.com/SlicerIGT/aigt">SlicerAIGT</a></li>
<li><a href="https://torchio.readthedocs.io/interfaces/slicer.html">TorchIO</a></li>
<li><a href="https://discourse.slicer.org/t/ai-assisted-segmentation-extension/9536">NVIDIA Ai assisted segmentation</a></li>
</ul>
</li>
<li>Registration
<ul>
<li><a href="https://github.com/netstim/SlicerNetstim">SlicerNetstim</a></li>
<li><a href="https://github.com/netstim/SlicerANTs">SlicerANTS</a></li>
</ul>
</li>
<li>Hardware support
<ul>
<li><a href="https://github.com/KitwareMedical/SlicerLookingGlass">SlicerLookingGlass</a></li>
<li><a href="https://discourse.slicer.org/t/new-extension-arduinocontroller/12156">Arduino Controller</a></li>
</ul>
</li>
<li>Web/Cloud
<ul>
<li><a href="https://flywheel.io/2019/09/06/flywheel-connect-3d-slicer-extension/">FlywheelSlicerConnect</a></li>
</ul>
</li>
<li>Dosimetry
<ul>
<li><a href="https://gitlab.com/opendose/OpenDose3D">OpenDose</a></li>
</ul>
</li>
</ul>
<h3 id="heading--extensions-updated">Updated</h3>
<p><em>Referenced below are new features added to existing extensions. Note all the existing extensions have been maintained and updated to account for API and build environment changes.</em></p>
<ul>
<li>
<p>IGT</p>
<ul>
<li><a href="https://discourse.slicer.org/t/lung-ct-segmenter-with-local-threshold-airway-segmentation/22065">Updates to the Chest Imaging Platform</a></li>
<li><a href="https://discourse.slicer.org/t/real-time-3d-ultrasound-volume-reconstruction-using-slicerigt-extension/11197">SlicerIGT - adds real time 3D ultrasound reconstruction</a></li>
</ul>
</li>
<li>
<p>Web/Cloud</p>
<ul>
<li><a href="https://discourse.slicer.org/t/run-slicer-in-your-web-browser-as-a-jupyter-notebook-or-as-a-full-application/11569">SlicerJupyter improvements</a></li>
</ul>
</li>
</ul>
<h3 id="heading--extensions-updated">Removed</h3>
<p>List of archived extensions is documented at <a href="https://github.com/Slicer/ExtensionsIndex/blob/main/ARCHIVE/README.md">Slicer/ExtensionsIndex/ARCHIVE/README.md</a></p>

---
