---
topic_id: 32319
title: "Filereader And Filewriter For 2 Classes"
date: 2023-10-19
url: https://discourse.slicer.org/t/32319
---

# FileReader and FileWriter for 2 classes

**Topic ID**: 32319
**Date**: 2023-10-19
**URL**: https://discourse.slicer.org/t/filereader-and-filewriter-for-2-classes/32319

---

## Post #1 by @rphellan2210 (2023-10-19 02:47 UTC)

<p>Hello,</p>
<p>I have used the [ModuleName] FileReader and [ModuleName] FileWriter before to allow drag and drop of a file with a specific extension into my module. However, I cannot figure out how to add more than one file extension. Do you have any example of this?</p>
<p>The code below shows a simple FileReader, but because the name of the class matches the name of the module, I cannot add more than one extension.</p>
<pre><code class="lang-auto">class MyModuleFileReader:

    def __init__(self, parent):
        self.parent = parent

    def description(self):
        return 'Specific type'

    def fileType(self):
        return 'Specific'

    def extensions(self):
        return ['Specific (*.spc)']

    def canLoadFile(self, filePath):
        return filePath.endswith('.spc')

    def load(self, properties):
        try:
            pass
        except Exception as e:
            logging.error('Failed to load file: ' + str(e))
            import traceback
            traceback.print_exc()
            return False

        return True
</code></pre>

---

## Post #2 by @pieper (2023-10-19 14:44 UTC)

<p>You should be able to use a format like this:</p>
<aside class="onebox githubblob" data-onebox-src="https://github.com/Slicer/Slicer/blob/d47277045f3cbc6db69953c1f118739005350e5d/Modules/Loadable/Transforms/qSlicerTransformsReader.cxx#L85">
  <header class="source">

      <a href="https://github.com/Slicer/Slicer/blob/d47277045f3cbc6db69953c1f118739005350e5d/Modules/Loadable/Transforms/qSlicerTransformsReader.cxx#L85" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h4><a href="https://github.com/Slicer/Slicer/blob/d47277045f3cbc6db69953c1f118739005350e5d/Modules/Loadable/Transforms/qSlicerTransformsReader.cxx#L85" target="_blank" rel="noopener">Slicer/Slicer/blob/d47277045f3cbc6db69953c1f118739005350e5d/Modules/Loadable/Transforms/qSlicerTransformsReader.cxx#L85</a></h4>



    <pre class="onebox"><code class="lang-cxx">
      <ol class="start lines" start="75" style="counter-reset: li-counter 74 ;">
          <li></li>
          <li>//-----------------------------------------------------------------------------</li>
          <li>qSlicerIO::IOFileType qSlicerTransformsReader::fileType()const</li>
          <li>{</li>
          <li>  return QString("TransformFile");</li>
          <li>}</li>
          <li></li>
          <li>//-----------------------------------------------------------------------------</li>
          <li>QStringList qSlicerTransformsReader::extensions()const</li>
          <li>{</li>
          <li class="selected">  return QStringList() &lt;&lt; "Transform (*.h5 *.tfm *.mat *.nrrd *.nhdr *.mha *.mhd *.nii *.nii.gz *.txt *.hdf5 *.he5)";</li>
          <li>}</li>
          <li></li>
          <li>//-----------------------------------------------------------------------------</li>
          <li>bool qSlicerTransformsReader::load(const IOProperties&amp; properties)</li>
          <li>{</li>
          <li>  Q_D(qSlicerTransformsReader);</li>
          <li>  Q_ASSERT(properties.contains("fileName"));</li>
          <li>  QString fileName = properties["fileName"].toString();</li>
          <li></li>
          <li>  if (d-&gt;TransformLogic.GetPointer() == nullptr)</li>
      </ol>
    </code></pre>



  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #3 by @rphellan2210 (2023-10-19 21:26 UTC)

<p>Oh this allows me to add more than one extension for the same type of file. But, is it possible to also add more than one file type?</p>

---

## Post #4 by @pieper (2023-10-19 21:28 UTC)

<p>I believe it follows the conventions described here:</p>
<aside class="onebox allowlistedgeneric" data-onebox-src="https://doc.qt.io/qt-5/qfiledialog.html#details">
  <header class="source">
      <img src="https://d33sqmjvzgs8hq.cloudfront.net/wp-content/themes/oneqt/assets/images/favicon.ico.gzip" class="site-icon" width="32" height="32">

      <a href="https://doc.qt.io/qt-5/qfiledialog.html#details" target="_blank" rel="noopener">doc.qt.io</a>
  </header>

  <article class="onebox-body">
    

<h3><a href="https://doc.qt.io/qt-5/qfiledialog.html#details" target="_blank" rel="noopener">QFileDialog Class | Qt Widgets 6.6.0</a></h3>

  <p>The QFileDialog class provides a dialog that allow users to select files or directories.</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
