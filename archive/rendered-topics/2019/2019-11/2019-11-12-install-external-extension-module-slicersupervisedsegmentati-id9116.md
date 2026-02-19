---
topic_id: 9116
title: "Install External Extension Module Slicersupervisedsegmentati"
date: 2019-11-12
url: https://discourse.slicer.org/t/9116
---

# Install external extension/module SlicerSupervisedSegmentation

**Topic ID**: 9116
**Date**: 2019-11-12
**URL**: https://discourse.slicer.org/t/install-external-extension-module-slicersupervisedsegmentation/9116

---

## Post #1 by @mikebind (2019-11-12 15:33 UTC)

<p>Hello, I would like to use the Slicer Supervised Segmentation extension (<a href="https://github.com/chalupaDaniel/SlicerSupervisedSegmentation" rel="nofollow noopener">https://github.com/chalupaDaniel/SlicerSupervisedSegmentation</a> ), but I do not understand how to access it from Slicer.  Does it need to be built from source with Slicer?  I was walked through the process of successfully building Slicer from source once during a training, but found that process non-intuitive and opaque, and I’m not sure I could accomplish it again on my own.  And even if I did accomplish that, I’m not sure at what point in the process or by what mechanism I would include the SlicerSupervisedSegmentation code.  I realize this code was not developed by the Slicer core, but I have not been able to find instructions with those files and I think my questions would apply to many other external extensions as well, so I am asking here if there is any guidance.  I did see instructions on the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers" rel="nofollow noopener">developer’s page</a> relating to creating and packaging extensions, but those all seem to be aimed at the original developer, rather than someone who just wants to use an extension developed by someone else.  Thanks for any help or guidance you can provide.</p>

---

## Post #2 by @Sam_Horvath (2019-11-12 18:12 UTC)

<p>External extensions need to built against a local build of Slicer.  See:  <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#How_to_build_an_extension_.3F" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#How_to_build_an_extension_.3F</a></p>
<p>So:</p>
<ol>
<li>Have a from source build of Slicer</li>
<li>Download the extension code</li>
<li>Configure the extension using CMake, providing the location of the Slicer build</li>
<li>Build the extension</li>
<li>Add the path to the built extension in the Slicer application settings: <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#How_to_manually_install_an_extension_package.3F" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Extensions#How_to_manually_install_an_extension_package.3F</a>
</li>
</ol>
<p>Extensions that are submitted to the ExtensionsIndex are also built with 3D Slicer and will be available through the Extension Manager.  Looking at the SlicerSupervisedSegmentation extension, it has been submitted, but has build errors and so is not currently available.</p>

---

## Post #3 by @mikebind (2019-11-12 23:16 UTC)

<p>Thanks, this is the information I needed.  I’ll have to decide whether to try to fumble my way through the process or not.</p>

---

## Post #4 by @morteza (2023-03-05 07:33 UTC)

<p>Hi Mike</p>
<p>I have a similar question to your question, but I still couldn’t get the right solution? Can you find a solution?<br>
Would be happy if you give me your experiences too</p>
<p>Yours sincerely</p>

---

## Post #5 by @mikebind (2023-03-06 01:17 UTC)

<p>Hello <a class="mention" href="/u/morteza">@morteza</a>, I did not end up trying to go through this whole process to try to get this extension.  I ended up looking into MONAI instead.  That system I did get working, but have not ended up using extensively.  The MONAI people have provided a lot of help in the Slicer forums, so there are several threads with lots of information if you are interested in going that route.  Good luck!</p>

---
