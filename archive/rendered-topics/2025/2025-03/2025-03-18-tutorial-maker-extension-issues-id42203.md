# Tutorial maker extension issues

**Topic ID**: 42203
**Date**: 2025-03-18
**URL**: https://discourse.slicer.org/t/tutorial-maker-extension-issues/42203

---

## Post #1 by @muratmaga (2025-03-18 16:50 UTC)

<p>Tutorial maker seems like a very useful module and would like to give a try, but I can’t seem to get it to work on preview using the example on the source repo. My interface doesn’t look like the example. There is no <code>run and annotate</code>. When I try edit annotations, I get this error:</p>
<pre><code class="lang-auto">
------------------------------
Reloading module: TutorialMaker
------------------------------



Version Date: 2025/03/04-07:00PM
Traceback (most recent call last):
  File "/Users/amaga/Desktop/Slicer.app/Contents/Extensions-33550/TutorialMaker/lib/Slicer-5.9/qt-scripted-modules/TutorialMaker.py", line 265, in OpenAnnotator
    Annotator.open_json_file(os.path.dirname(slicer.util.modulePath("TutorialMaker")) + "/Outputs/Raw/Tutorial.json")
  File "/Users/amaga/Desktop/Slicer.app/Contents/Extensions-33550/TutorialMaker/lib/Slicer-5.9/qt-scripted-modules/Lib/TutorialGUI.py", line 805, in open_json_file
    with open(filepath, encoding='utf-8') as file:
FileNotFoundError: [Errno 2] No such file or directory: '/Users/amaga/Desktop/Slicer.app/Contents/Extensions-33550/TutorialMaker/lib/Slicer-5.9/qt-scripted-modules/Outputs/Raw/Tutorial.json'
[Qt] QImage::scaled: Image is a null image
[Qt] QImage::scaled: Image is a null image
[Qt] QImage::scaled: Image is a null image
[Qt] QImage::scaled: Image is a null image
</code></pre>
<p>I clicked on <code>create a new tutorial</code>, which is what I want to do really, and the python file is created in the resource folder, but I can’t seem to start annotating/capturing.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/6/46db0eb62caa4f3eabb8eec2f1215c4c30fd1b43.png" data-download-href="/uploads/short-url/a6OKAloPqKroyQ84spUbkB7efd1.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46db0eb62caa4f3eabb8eec2f1215c4c30fd1b43_2_303x500.png" alt="image" data-base62-sha1="a6OKAloPqKroyQ84spUbkB7efd1" width="303" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46db0eb62caa4f3eabb8eec2f1215c4c30fd1b43_2_303x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46db0eb62caa4f3eabb8eec2f1215c4c30fd1b43_2_454x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/6/46db0eb62caa4f3eabb8eec2f1215c4c30fd1b43_2_606x1000.png 2x" data-dominant-color="B7B9C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">774×1275 83 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2025-03-19 16:32 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a> any thoughts?</p>

---

## Post #3 by @DouSam (2025-03-20 17:06 UTC)

<p>Hi Murat,</p>
<p>Tutorial Maker is an experimental extension. For now, we haven’t implemented the process of recording the tutorial. So to use the extension you need to create a Python script that runs through the tutorial and takes the screenshots.</p>
<p>Use the <a href="https://github.com/SlicerLatinAmerica/TestSlicerTutorials/blob/main/Tutorials/FourMinuteTutorial/FourMinuteTutorial.py" rel="noopener nofollow ugc">4-minute tutorial script</a> as a sample.</p>
<p>Also, I saw that you are using the version 5.9. We recommend using the latest preview version since it is an experimental extension, the extension version available in 5.9 will have some problems that we already fixed after the version has been released to stable. Or you can download the extension from the <a href="https://github.com/SlicerLatinAmerica/SlicerTutorialMaker" rel="noopener nofollow ugc">GitHub repository</a> and try with the latest version.</p>
<p>If you have any problem during the use, open an issue or post here in the forum, tag me so I can help you!</p>

---
