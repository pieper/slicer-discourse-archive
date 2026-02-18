# Adding Widgets to Layout

**Topic ID**: 2074
**Date**: 2018-02-12
**URL**: https://discourse.slicer.org/t/adding-widgets-to-layout/2074

---

## Post #1 by @asheu (2018-02-12 19:38 UTC)

<p>Hi there,</p>
<p>I am a fairly new to the game in terms of Slicer module development so would like some help. Right now, I am trying to add a LR slider widget onto the main window. Ideally, I would want this slider to interact with the reformat widget (i.e. allow me to move the individual slice at different angles). Are there any steps that I can go about into implementing this?</p>
<p>Thanks a lot!</p>

---

## Post #2 by @pieper (2018-02-12 20:29 UTC)

<p>Usually we would suggest putting functionality like that into a custom scripted module with it’s own interface panel as described here:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Training#Developing_and_contributing_extensions_for_3D_Slicer" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Training#Developing_and_contributing_extensions_for_3D_Slicer</a></p>
<p>If you really need your widget in the main layout it’s of course possible to child widgets to any of the layouts but it would be more likely to break in the future.</p>

---

## Post #3 by @lassoan (2018-02-12 22:20 UTC)

<p>Here is a module that does this, except that it rotates slice using a slider instead of translating it. It is a scripted module so it should be easy to modify it do what you need:</p>
<aside class="onebox githubfolder" data-onebox-src="https://github.com/SlicerHeart/SlicerHeart/tree/master/ValveView">
  <header class="source">
      <img src="https://github.githubassets.com/favicons/favicon.svg" class="site-icon" width="32" height="32">

      <a href="https://github.com/SlicerHeart/SlicerHeart/tree/master/ValveView" target="_blank" rel="noopener">github.com</a>
  </header>

  <article class="onebox-body">
    <h3><a href="https://github.com/SlicerHeart/SlicerHeart/tree/master/ValveView" target="_blank" rel="noopener">SlicerHeart/ValveView at master · SlicerHeart/SlicerHeart</a></h3>

  <p><a href="https://github.com/SlicerHeart/SlicerHeart/tree/master/ValveView" target="_blank" rel="noopener">master/ValveView</a></p>

  <p><span class="label1">3D Slicer extension for cardiac analysis. Contribute to SlicerHeart/SlicerHeart development by creating an account on GitHub.</span></p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---
