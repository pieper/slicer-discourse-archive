---
topic_id: 20798
title: "The Problem Of Itk Imagefilereader"
date: 2021-11-26
url: https://discourse.slicer.org/t/20798
---

# The problem of itk.ImageFileReader

**Topic ID**: 20798
**Date**: 2021-11-26
**URL**: https://discourse.slicer.org/t/the-problem-of-itk-imagefilereader/20798

---

## Post #1 by @476663616 (2021-11-26 10:23 UTC)

<p>Hello,</p>
<p>I have encountered some problems recently. I want to rebulid the volume image from a “.tre” file to show the refine image. I use itk to complete this work, and it works perfect in the conda env. However, when I run it in my Slicer extension, it shows:</p>
<pre><code class="lang-auto">TemplateImageType: &lt;class 'itk.itkImagePython.itkImageF3'&gt;
terminate called after throwing an instance of 'H5::DataSpaceIException'
error: [/mnt2/homes/xingyul/xinyul/Slicer/bin/SlicerApp-real] exit abnormally - Report the problem.
</code></pre>
<p>I tried to debug, found that this line of code caused the program to crash：</p>
<pre><code class="lang-auto">    TemplateImageType = itk.Image[itk.F, 3]
    print('TemplateImageType:',TemplateImageType)
    TemplateImageReaderType = itk.ImageFileReader[TemplateImageType]
</code></pre>
<p>I think the function ‘itk.ImageFileReader’ caused the conflict, how to fix it?</p>
<p>Thanks</p>

---

## Post #2 by @476663616 (2021-11-26 10:24 UTC)

<p>The entire code is as follows：</p>
<pre><code class="lang-auto">import itk
from itk import TubeTK as ttk
def treTomask(rootpath, ctpath):
    ctpath=''
    print('start treTomask')
    PixelType = itk.F
    Dimension = 3
    ImageType = itk.Image[PixelType, Dimension]
        
    # # Read tre file
    TubeFileReaderType = itk.SpatialObjectReader[Dimension]
        
    tubeFileReader = TubeFileReaderType.New()
    tubeFileReader.SetFileName(rootpath)
    tubeFileReader.Update()

    print('tubeFileReader complete')

    tubes = tubeFileReader.GetGroup()

    print('tubes = tubeFileReader.GetGroup()')

    # Read template image
    TemplateImageType = itk.Image[itk.F, 3]
    print('TemplateImageType:',TemplateImageType)
    TemplateImageReaderType = itk.ImageFileReader[TemplateImageType]
    print('TemplateImageReaderType')
    print(ctpath)
        
    templateImageReader = TemplateImageReaderType.New()
    templateImageReader.SetFileName(ctpath)
    templateImageReader.Update()
    print('templateImageReader')

    templateImage = templateImageReader.GetOutput()
    TubesToImageFilterType = ttk.ConvertTubesToImage[TemplateImageType]
    tubesToImageFilter = TubesToImageFilterType.New()
    tubesToImageFilter.SetUseRadius(True)
    tubesToImageFilter.SetTemplateImage(templateImageReader.GetOutput())
    tubesToImageFilter.SetInput(tubes)
    tubesToImageFilter.Update()
    outputImage = tubesToImageFilter.GetOutput()

    print('tubesToImageFilter  complete')

    TTKImageMathType = ttk.ImageMath[ImageType,ImageType]
    imMath = TTKImageMathType.New(Input = outputImage)
    img = imMath.GetOutput()
    # os.remove(rootpath)
    print('Tre convert is DONE')
    return img
</code></pre>

---

## Post #3 by @476663616 (2021-11-26 12:37 UTC)

<p>By the way, I try subprocess, like this:</p>
<pre><code class="lang-auto">subprocess.run('/mnt2/homes/xingyul/anaconda3/envs/labelsys/bin/python /mnt2/homes/xingyul/xinyul/Slicer/vessel_connect/infer_tools_tree/result/test.py', shell=True)
</code></pre>
<p>but it seems doesn’t work ：</p>
<pre><code class="lang-auto">Traceback (most recent call last):
  File "/mnt2/homes/xingyul/xinyul/Slicer/vessel_connect/infer_tools_tree/result/test.py", line 1, in &lt;module&gt;
    from TreToImg import treTomask
  File "/mnt2/homes/xingyul/xinyul/Slicer/vessel_connect/infer_tools_tree/result/TreToImg.py", line 1, in &lt;module&gt;
    import itk
  File "/mnt2/homes/xingyul/xinyul/Slicer/lib/Python/lib/python3.6/site-packages/itk/__init__.py", line 28, in &lt;module&gt;
    from itk.support.extras import *
  File "/mnt2/homes/xingyul/xinyul/Slicer/lib/Python/lib/python3.6/site-packages/itk/support/extras.py", line 23, in &lt;module&gt;
    import numpy as np
  File "/mnt2/homes/xingyul/xinyul/Slicer/lib/Python/lib/python3.6/site-packages/numpy/__init__.py", line 140, in &lt;module&gt;
    from . import core
  File "/mnt2/homes/xingyul/xinyul/Slicer/lib/Python/lib/python3.6/site-packages/numpy/core/__init__.py", line 22, in &lt;module&gt;
    from . import multiarray
  File "/mnt2/homes/xingyul/xinyul/Slicer/lib/Python/lib/python3.6/site-packages/numpy/core/multiarray.py", line 12, in &lt;module&gt;
</code></pre>

---

## Post #4 by @pieper (2021-11-26 14:02 UTC)

<p>This thread should help: <a href="https://discourse.slicer.org/t/slicer-crashes-when-creating-h5-file/19733/3" class="inline-onebox">Slicer crashes when creating h5 file - #3 by szymswiat</a></p>

---

## Post #5 by @476663616 (2021-11-27 12:42 UTC)

<p>Thanks for reply！I have successfully fixed it by subprocess, but I’d like to try your suggestion.</p>

---
