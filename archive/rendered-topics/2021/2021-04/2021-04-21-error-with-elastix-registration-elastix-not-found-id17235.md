# Error with Elastix Registration: Elastix not found

**Topic ID**: 17235
**Date**: 2021-04-21
**URL**: https://discourse.slicer.org/t/error-with-elastix-registration-elastix-not-found/17235

---

## Post #1 by @marianaslicer (2021-04-21 18:18 UTC)

<p>Hi everyone,</p>
<p>I’m working on a Slicer custom application, which was built according to this tutorial: <a href="https://blog.kitware.com/slicercat-creating-custom-applications-based-on-3d-slicer/" rel="noopener nofollow ugc">SlicerCAT: Creating custom applications based on 3D Slicer - Kitware Blog</a></p>
<p>The application runs a custom module developed in Python language programming using the Extension Manager module available in 3D Slicer.</p>
<p>The module should perform image registration using the SlicerElastix toolbox through the following lines of code:</p>
<pre><code>    self.elastixLogic = Elastix.ElastixLogic()

    self.elastixLogic.registerVolumes(
        self.movingNode, self.referenceNode,
        outputVolumeNode=self.warpVolume,
        parameterFilenames=self.parametersFile,
        outputTransformNode=self.elastix)
</code></pre>
<p>But I’m getting an error message saying “Elastix Not Found”. Any idea how to solve it?</p>
<p>Thanks in advance.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c1b5acd4b7f7ee708cd4fde9d571c0fd5677aa4.png" data-download-href="/uploads/short-url/40DYx2j7jV1SfZH0gZtoRSq4yBC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c1b5acd4b7f7ee708cd4fde9d571c0fd5677aa4_2_690x237.png" alt="image" data-base62-sha1="40DYx2j7jV1SfZH0gZtoRSq4yBC" width="690" height="237" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c1b5acd4b7f7ee708cd4fde9d571c0fd5677aa4_2_690x237.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c1b5acd4b7f7ee708cd4fde9d571c0fd5677aa4.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c1b5acd4b7f7ee708cd4fde9d571c0fd5677aa4.png 2x" data-dominant-color="F9F0F1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">708×244 97.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @jamesobutler (2021-04-21 21:40 UTC)

<p>Did you use <a href="https://github.com/KitwareMedical/SlicerCustomAppTemplate" rel="noopener nofollow ugc">https://github.com/KitwareMedical/SlicerCustomAppTemplate</a> to generate your Slicer custom application? I believe when you use that it will use the current Slicer master git hash when setting up the custom application. It looks from the image you posted that you are using an older Slicer version (4.11). <a href="https://github.com/KitwareMedical/SlicerCAT" rel="noopener nofollow ugc">https://github.com/KitwareMedical/SlicerCAT</a> is an example of a Slicer custom app, but not necessarily the starting point or the source you should be editing to create your application.</p>
<p>As it relates to Elastix, did you specify to build your Slicer custom application with the <a href="https://github.com/lassoan/SlicerElastix" rel="noopener nofollow ugc">SlicerElastix</a> as a remote extension? Were there any build errors? I would suggest to use latest Slicer master git hash and SlicerElastix git hash as these should be currently compatible.</p>

---

## Post #3 by @jamesobutler (2021-04-22 22:10 UTC)

<p><a class="mention" href="/u/marianaslicer">@marianaslicer</a> Can you answer some of the above questions? Did your Slicer custom app build without errors? Did you solve the Elastix error you posted about earlier?</p>

---

## Post #4 by @marianaslicer (2021-04-22 22:36 UTC)

<p>Hi James,</p>
<p>Sorry for answering later.<br>
I used the link you mentioned to generate my Slicer application and I think I used the current Slicer master git, Slicer 4.11.20210226.<br>
Then, I added to the cmakefile.txt the SlicerElastix extension:</p>
<p>set(extension_name “SlicerElastix”)<br>
set(${extension_name}_SOURCE_DIR “${CMAKE_BINARY_DIR}/${extension_name}”)<br>
FetchContent_Populate(${extension_name}<br>
SOURCE_DIR     ${${extension_name}_SOURCE_DIR}<br>
GIT_REPOSITORY ${EP_GIT_PROTOCOL}://github.com/lassoan/SlicerElastix.git<br>
GIT_TAG        master<br>
GIT_PROGRESS   1<br>
QUIET<br>
)<br>
list(APPEND Slicer_EXTENSION_SOURCE_DIRS ${${extension_name}_SOURCE_DIR})</p>
<p>And there were no build errors. What I did to solve my problem (which is not the best approach) was to add manually the elastix.exe and transformix.exe files to the Slicer Elastix folder and specify it at the custom elastix toolbox location.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/6/2628ed4aebe5c84fefa4ba1e4a1042d7bcfe5b27.png" alt="image" data-base62-sha1="5rzPqfe1ohbf3nJAuQr4w5AqH6T" width="535" height="186"></p>

---
