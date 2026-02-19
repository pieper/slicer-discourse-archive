---
topic_id: 33378
title: "How Can I Redirect Std Cout To Python Interactor"
date: 2023-12-13
url: https://discourse.slicer.org/t/33378
---

# How can I redirect std::cout to Python Interactor?

**Topic ID**: 33378
**Date**: 2023-12-13
**URL**: https://discourse.slicer.org/t/how-can-i-redirect-std-cout-to-python-interactor/33378

---

## Post #1 by @nnzzll (2023-12-13 07:32 UTC)

<p>I’m developing a C++ extension and there are lots of output messages using “std::cout”.</p>
<p>However, I can only see these messages when slicer started from terminal and cannot see them in the python interactor.</p>
<p>How can I redirect those messages to python interactor?</p>

---

## Post #2 by @jcfr (2023-12-13 07:47 UTC)

<p>Did you also consider looking at the <code>Error Log</code> ?</p>
<p>See <a href="https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#application-menu">https://slicer.readthedocs.io/en/latest/user_guide/user_interface.html#application-menu</a></p>
<p>This should list all messages.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/d/edecb97957e019b4dc6d090f34e8d696904ee9eb.png" data-download-href="/uploads/short-url/xWMl6yuRNtipiv091vqa9JNqKKL.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edecb97957e019b4dc6d090f34e8d696904ee9eb_2_517x338.png" alt="image" data-base62-sha1="xWMl6yuRNtipiv091vqa9JNqKKL" width="517" height="338" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edecb97957e019b4dc6d090f34e8d696904ee9eb_2_517x338.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edecb97957e019b4dc6d090f34e8d696904ee9eb_2_775x507.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/d/edecb97957e019b4dc6d090f34e8d696904ee9eb_2_1034x676.png 2x" data-dominant-color="878995"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2571×1682 273 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #3 by @cpinter (2023-12-13 09:52 UTC)

<p>If you develop the extension then I assume you have control over the logging. In this case I’d suggest using VTK or Qt macros for logging (depending on whether your class is VTK or Qt based). I’m thinking about <code>vtk[Debug/Info/Warning/Error]Macro</code> and <code>qDebug/qWarning/qCritical</code>. These will appear in the Python console. Be mindful that you may need to lower the log level in Application Settings if you want to use <code>vtkInfoMacro</code> for example.</p>

---
