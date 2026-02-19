---
topic_id: 34189
title: "Change Default Settings For Volume Rendering Module"
date: 2024-02-07
url: https://discourse.slicer.org/t/34189
---

# Change default settings for Volume Rendering module

**Topic ID**: 34189
**Date**: 2024-02-07
**URL**: https://discourse.slicer.org/t/change-default-settings-for-volume-rendering-module/34189

---

## Post #1 by @ruili (2024-02-07 16:19 UTC)

<p>Hi!</p>
<p>I have been using the volume rendering module to visualise 3D volumes with maximum intensity projection technique. Due to the properties of my images, I always have to change the settings in “Volume properties” so that most of the “points” for “Scalar Color Mapping” are set to 0. However, the problem is that by default there are many control points for this setting, and everytime I have to spend a while dragging many control points to 0. I have to process many images, so doing this repeatedly is quite tedious. I am wondering if it is possible for me to change the default setting for this part so that I don’t have to change this setting manually every time? Many thanks in advance!</p>
<p>Current default:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d952eda25c10471714ea2817de6916843fde743.png" data-download-href="/uploads/short-url/hUXj1TomBsc90z4DqRby0HZgpVx.png?dl=1" title="Screenshot 2024-02-01 at 12.26.35" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d952eda25c10471714ea2817de6916843fde743_2_475x500.png" alt="Screenshot 2024-02-01 at 12.26.35" data-base62-sha1="hUXj1TomBsc90z4DqRby0HZgpVx" width="475" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d952eda25c10471714ea2817de6916843fde743_2_475x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d952eda25c10471714ea2817de6916843fde743.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d952eda25c10471714ea2817de6916843fde743.png 2x" data-dominant-color="E9E9E9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-02-01 at 12.26.35</span><span class="informations">676×711 36.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>What I want:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fbb131d871a724f5bd2a2923c8fff14ddd1f5ae.png" data-download-href="/uploads/short-url/dESafv8v4wDee5gSb9XSZpSaWeO.png?dl=1" title="Screenshot 2024-02-07 at 16.15.47" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fbb131d871a724f5bd2a2923c8fff14ddd1f5ae_2_436x375.png" alt="Screenshot 2024-02-07 at 16.15.47" data-base62-sha1="dESafv8v4wDee5gSb9XSZpSaWeO" width="436" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fbb131d871a724f5bd2a2923c8fff14ddd1f5ae_2_436x375.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5fbb131d871a724f5bd2a2923c8fff14ddd1f5ae_2_654x562.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5fbb131d871a724f5bd2a2923c8fff14ddd1f5ae.png 2x" data-dominant-color="EAEBEB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-02-07 at 16.15.47</span><span class="informations">693×595 31.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @muratmaga (2024-02-07 16:26 UTC)

<p>In the order of from simplest to slightly to more work:</p>
<p>You can save and reload the volume property you customized.<br>
You can do bit of python scripting to have it automatically loaded into Slicer through slicerrc.py.<br>
You can even register as a default preset.</p>
<p>All of those are possibilities.</p>

---

## Post #3 by @ruili (2024-02-15 17:16 UTC)

<p>Thank you. Your discussion on the forum <a href="https://discourse.slicer.org/t/setting-the-volume-property-to-be-used-when-a-volume-is-rendered-automatically/16653">here</a> is also very helpful. I think for my purpose loading my volume property file (.vp) is sufficient, and I have managed to add the following code to my .slicerrc.py so that my .vp file is loaded automatically:</p>
<pre><code class="lang-auto">vp_file = '/path/to/myVolumeProperty.vp'
volRenLogic = slicer.modules.volumerendering.logic()
volRenLogic.AddVolumePropertyFromFile(vp_file)
</code></pre>
<p>However, I now still have to go to “Inputs” section in the volume rendering module to select this volume property every time. Do you know how I can set it as the default volume property in .slicerrc.py? I am really unfamiliar with writing python scripts for slicer and have found it very difficult to find the write function to use, so your help will be very much appreciated!</p>

---

## Post #4 by @muratmaga (2024-02-15 19:42 UTC)

<aside class="quote no-group" data-username="ruili" data-post="3" data-topic="34189">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/dec6dc/48.png" class="avatar"> ruili:</div>
<blockquote>
<p>Do you know how I can set it as the default volume property in .slicerrc.py?</p>
</blockquote>
</aside>
<p>I will defer this to <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a>. I know it is possible, but not sure.</p>
<p>We have MRML file where we define our custom presets. I imagine there is a some sort of weight that needs to be defined to make them the first choice (e.g., for 16 bit unsigned data).</p>

---

## Post #5 by @chir.set (2024-02-15 20:59 UTC)

<p>I don’t know what you mean by ‘default volume property’. Perhaps you mean ‘change the default values of a given factory preset’. It’s probably possible, experts may have a valuable reply as <a class="mention" href="/u/muratmaga">@muratmaga</a> said.</p>
<p>Nevertheless, I use this <em>ugly</em> hack in .slicerrc.py. It did not crash anything for years. You may add your custom presets in the combobox and select them like factory presets.</p>
<pre><code class="lang-auto">def loadCustomVolumeProperty(name):
    VolRenLogic = slicer.modules.volumerendering.logic()
    VolProp = VolRenLogic.GetPresetByName(name)
    if (VolProp is None):
        VolProp = VolRenLogic.AddVolumePropertyFromFile(/path/to/vp/file)
        vReader = vtk.vtkPNGReader()
        vReader.SetFileName(str(/path/to/png/file)
        vReader.Update()
        VolRenLogic.AddPreset(VolProp, vReader.GetOutput())
    
    # The loaded Volume Property is *sometimes* found as volume nodes, in Volume Rendering module only, not in Volumes module !
    alienNodes = slicer.mrmlScene.GetNodesByName(name)
    for node in alienNodes:
        # We are just removing the vtkMRMLVolumePropertyNode we just loaded, but it persists as a preset and is functional !!!
        # print(node.GetClassName())
        slicer.mrmlScene.RemoveNode(node)
        
loadCustomVolumeProperty(customVR1)
loadCustomVolumeProperty(customVR2)
</code></pre>

---

## Post #6 by @lassoan (2024-02-15 22:17 UTC)

<p>If you want to modify an existing volume rendering preset or reorder volume rendering presets then you can use the code snippet above to remove a preset and then prepend it to the preset list.</p>
<p>If you want to use special volume rendering presets used by default for some special volume types then you can create a subject hierarchy plugin that recognizes and takes ownership of the special volume types.</p>
<p>However, what you probably actually want is a custom <em>hanging protocol</em>, which goes beyond just some volume rendering presets and customizes the view layout, select which volumes are displayed in what views, with what opacity, colormap, etc. These can be all easily set using a Python script that you can activate by a keyboard shortcut (see complete example <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#activate-hanging-protocol-by-keyboard-shortcut">here</a>). If a keyboard shortcut is not convenient enough then you can observe <code>newFileLoaded</code> signal of the <code>ioManager</code> and detect if your custom hanging protocol is applicable to the loaded data and if yes then activate it automatically.</p>

---

## Post #7 by @ruili (2024-02-16 11:52 UTC)

<p>Sorry my question wasn’t very clear. What I meant was that when I load a volume into slicer and go to the Volume Rendering module, it will be visualised with a default ‘VolumeProperty’, as can be seen in the ‘Inputs’ section ‘Property’ box. After adding those few lines to my .slicerrc.py, I now automatically load my custom volume property ‘MIP_VolumeProperty’ to slicer and can see it in the options. However, to use my custom volume property, I still have to go to this section and select it every time. Thus, I was wondering if there is a way to let it automatically select my custom volume property to use when I do volume rendering. I am not registering my volume property as a preset at this moment.</p>
<p>Thanks to <a class="mention" href="/u/lassoan">@lassoan</a> for your input as well. However, I’m afraid that what you wrote about the “hierarchy plugin” and “hanging protocol” is a bit beyond my understanding. With my current clarification of my question, do you think those are what I need?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/6249054824e4db2dc9ead856cecaff061bdd505e.png" alt="Screenshot 2024-02-16 at 11.43.16" data-base62-sha1="e1teLcJonxChr6Tb7sTCiTDnkMm" width="426" height="250"></p>

---

## Post #8 by @lassoan (2024-02-16 15:14 UTC)

<p>Hanging protocol defines in a radiology workflow what images you show and where, in what orientation, with what settings.</p>
<p>Volume rendering preset is a just one of the details that you need to set up. So, instead of investing time into developing a custom subject hierarchy plugin (that is responsible for choosing the volume rendering preset), I would recommend to implement a short Python code snippet that sets the volume rendering preset and all other view options you want. You can run this script by a keyboard shortcut ir automatically when images are loaded.</p>

---
