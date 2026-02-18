# SlicerOpenCV on Linux

**Topic ID**: 22560
**Date**: 2022-03-17
**URL**: https://discourse.slicer.org/t/sliceropencv-on-linux/22560

---

## Post #1 by @Karl-Philippe (2022-03-17 11:26 UTC)

<p>Hello,</p>
<p>Is the SlicerOpenCV extension available on Linux? I don’t see this extension in the extension manager of versions 4.11 and 4.13 on Linux while I see that SlicerOpenCV is available in the extension manager of Slicer 4.11 on Windows.</p>
<p>Thank you,</p>

---

## Post #2 by @jamesobutler (2022-03-17 11:41 UTC)

<p>SlicerOpenCV is currently <a href="https://slicer.cdash.org/viewBuildError.php?buildid=2629665" rel="noopener nofollow ugc">failing</a> to build on Linux primarily due to a lack of Linux developers to debug the issue.</p>
<p>Do you need the ITKVideoBridgeOpenCV component that it contains? If not, and you just need regular OpenCV to be accessible in python then you can try <code>slicer.util.pip_install("opencv-python")</code>. That will get official OpenCV whl files from PyPI where the latest version 4.5.5.64 has manylinux whl files available. <a href="https://pypi.org/project/opencv-python/#files" class="inline-onebox" rel="noopener nofollow ugc">opencv-python · PyPI</a></p>

---

## Post #3 by @Karl-Philippe (2022-03-17 12:38 UTC)

<p>Ok thank you, I am only planning to use OpenCV with python so this should work fine and I did not planned to use the ITKVideoBridgeOpenCV.</p>

---
