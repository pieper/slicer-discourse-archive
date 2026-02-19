---
topic_id: 8383
title: "How To Tell Slicer To Save By Default In Whatever Folder It"
date: 2019-09-11
url: https://discourse.slicer.org/t/8383
---

# How to tell Slicer to save by default in whatever folder it is called from

**Topic ID**: 8383
**Date**: 2019-09-11
**URL**: https://discourse.slicer.org/t/how-to-tell-slicer-to-save-by-default-in-whatever-folder-it-is-called-from/8383

---

## Post #1 by @muratmaga (2019-09-11 15:36 UTC)

<p>I use Slicer on Linux a lot, and I usually invoke it from the terminal window and typically from the folder where the dataset I am going to work on is present. I would like to have the default save behavior to be in the same folder (so something like “./”, or $PWD) but I can’t seem to type a field in the ‘default save scene folder’ under settings. Is there a place to set this in .slicerrc.py or some other initialization script?</p>

---

## Post #2 by @lassoan (2019-09-11 15:46 UTC)

<p>Default scene location is a directory selector button. You can click on it to change the default scene location. It is also can be read/written from Python as <code>slicer.app.defaultScenePath</code>.</p>

---

## Post #3 by @pieper (2019-09-11 19:54 UTC)

<p>In case it wasn’t clear, Andras is referring to this button in the Application Settings.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4898f61a16d58a3e96bd186d22d605b3aed5f26f.png" data-download-href="/uploads/short-url/ame5X6PqHkPhTS6Qlw3zspzXJx5.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/4898f61a16d58a3e96bd186d22d605b3aed5f26f_2_690x94.png" alt="image" data-base62-sha1="ame5X6PqHkPhTS6Qlw3zspzXJx5" width="690" height="94" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/4898f61a16d58a3e96bd186d22d605b3aed5f26f_2_690x94.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/4898f61a16d58a3e96bd186d22d605b3aed5f26f_2_1035x141.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/4898f61a16d58a3e96bd186d22d605b3aed5f26f_2_1380x188.png 2x" data-dominant-color="E2E5E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1962×270 92.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2019-09-11 20:47 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Yes, that’s the setting that I was talking about. neither in Windows nor Linux it accepts relative path. It is not an editable field for me to put something like “./”. It reverts to the full path of that where working directory I am, and hard codes. So next time I start in a different working directory, it will be wrong again. Anyways, I think python solution might be more relevant. Get the $PWD from the os, and set it as the default scene location.</p>

---

## Post #5 by @lassoan (2019-09-12 01:30 UTC)

<p>Default scene save path would be something like your “documents” folder. It should not be overwritten each time you run a script from some random working directory.</p>
<p>Instead, if you want to change the default save location in a scripting session then modify the root directory of the scene. For example, you can set it to the current working directory by calling <code>slicer.mrmlScene.SetRootDirectory(os.getcwd())</code>.</p>

---

## Post #6 by @muratmaga (2019-09-12 04:21 UTC)

<p>I think it depends on what you want to do. I personally do not have any use for a ‘documents’ folder as a default save location. I would prefer if the behavior is to make the default save path to the location of current (or last loaded) dataset. In my experience the setting ‘default scene path’ to Documents (or like) doesn’t just effect the scenes, but any new volume or data that gets created in the scene by default get the same path.  Again everybody has different use cases, and I understand it is hard to find a solution that’s going to fit everyone. I think python manipulation is going to work for me.</p>

---

## Post #7 by @lassoan (2019-09-12 18:30 UTC)

<p>Current Slicer behavior follows common convention used by applications such as MS Office (new files are always saved to “documents” folder by default; existing files are saved to their current location).</p>
<p>It is  impossible to meet expectations of all users with a single behavior, that’s why all the customization options are made available.</p>

---
