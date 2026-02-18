# How to Get/Set the display area window size with python code?

**Topic ID**: 22275
**Date**: 2022-03-03
**URL**: https://discourse.slicer.org/t/how-to-get-set-the-display-area-window-size-with-python-code/22275

---

## Post #1 by @user4 (2022-03-03 06:38 UTC)

<p>Slicer 4.11<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d46346b1440629d0759c1c615c88aa5bce2a6d67.png" data-download-href="/uploads/short-url/uiRV9K1lMtnBlXSaa0NfLeQqetV.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d46346b1440629d0759c1c615c88aa5bce2a6d67_2_690x388.png" alt="image" data-base62-sha1="uiRV9K1lMtnBlXSaa0NfLeQqetV" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d46346b1440629d0759c1c615c88aa5bce2a6d67_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d46346b1440629d0759c1c615c88aa5bce2a6d67_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d46346b1440629d0759c1c615c88aa5bce2a6d67_2_1380x776.png 2x" data-dominant-color="DCDCED"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
By default,the window size is about 672x994 resolution which is marked in red.<br>
I can manually expand or shrink the window like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a0213b82acf8b074118aeb8040732d044cf475de.png" data-download-href="/uploads/short-url/mQzAV55uMOO69RrFSZAQ0IKCMsC.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0213b82acf8b074118aeb8040732d044cf475de_2_690x388.png" alt="image" data-base62-sha1="mQzAV55uMOO69RrFSZAQ0IKCMsC" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0213b82acf8b074118aeb8040732d044cf475de_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0213b82acf8b074118aeb8040732d044cf475de_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a0213b82acf8b074118aeb8040732d044cf475de_2_1380x776.png 2x" data-dominant-color="BEBEE0"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 119 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
I wonder if there is some way to get/set the window size?<br>
Thank you in advance for your advice and help!</p>

---

## Post #2 by @ebrahim (2022-03-03 14:00 UTC)

<p>I think you have to resize the module panel on the left:</p>
<pre data-code-wrap="py"><code class="lang-nohighlight">panelDockWidget = slicer.util.mainWindow().findChildren('QDockWidget','PanelDockWidget')[0]
slicer.util.mainWindow().resizeDocks([panelDockWidget],[1000], qt.Qt.Horizontal) # change 1000 to desired width
</code></pre>

---

## Post #3 by @user4 (2022-03-04 02:27 UTC)

<p>Thanks a lot ! Ebrahim<br>
It works! I noticed that you are actually changing the panel on the left in order to resize the display area so it changes the width.However do you think it possible to change the height? Maybe I need to change the Python Interactor window height in order to change the display area height?</p>

---

## Post #4 by @ebrahim (2022-03-04 13:39 UTC)

<blockquote>
<p>However do you think it possible to change the height? Maybe I need to change the Python Interactor window height in order to change the display area height?</p>
</blockquote>
<p>You can change the python interactor height in a similar way</p>
<pre data-code-wrap="py"><code class="lang-py">pyConsoleDockWidget = slicer.util.mainWindow().findChildren('QDockWidget','PythonConsoleDockWidget')[0]
slicer.util.mainWindow().resizeDocks([pyConsoleDockWidget],[100], qt.Qt.Vertical) # change 100 to desired height
</code></pre>
<p>The display area whose size you are trying to manipulate can be accessed as <code>slicer.util.mainWindow().centralWidget()</code>. Depending on what you’re trying to do exactly, you might want to play with its size policy and resize it. Or maybe insert some spacers around it.</p>

---

## Post #5 by @user4 (2022-03-05 18:16 UTC)

<p>Thanks Ebrahim,<br>
Actually,I just want to fix the display area window size.Maybe I accidentally dragged the window and made the size different.</p>
<aside class="quote no-group" data-username="ebrahim" data-post="4" data-topic="22275">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ebrahim/48/13403_2.png" class="avatar"> ebrahim:</div>
<blockquote>
<p>The display area whose size you are trying to manipulate can be accessed as</p>
</blockquote>
</aside>
<p>It seems that I can just <strong>directly</strong> get the QtWidget and play with its size?<br>
However I can not resize the window with the code below:</p>
<pre><code class="lang-auto">centralWidget = slicer.util.mainWindow().centralWidget()
slicer.util.mainWindow().resizeDocks([centralWidget],[100], qt.Qt.Horizontal)

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
In  [101]:
Line 2:     

ValueError: Called resizeDocks(QList&lt;QDockWidget*&gt; docks, QList&lt;qint32&gt; sizes, Qt::Orientation orientation) -&gt; void with wrong arguments: ([QWidget(0x1e4f319c700, name="CentralWidget") ], [100], 1)
---------------------------------------------------------------------------
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d199bdfb8b7f3efc2c2f5c5729b1500fde09977.png" data-download-href="/uploads/short-url/fz8Uu6innwhBjDxlClpVmPw05YX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/d/6d199bdfb8b7f3efc2c2f5c5729b1500fde09977.png" alt="image" data-base62-sha1="fz8Uu6innwhBjDxlClpVmPw05YX" width="690" height="104" data-dominant-color="FADADA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1317×199 6.84 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there something wrong with my code?<br>
Thank you for your continued attention.</p>

---

## Post #6 by @ebrahim (2022-03-07 13:56 UTC)

<aside class="quote no-group" data-username="user4" data-post="5" data-topic="22275">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/user4/48/13172_2.png" class="avatar"> user4:</div>
<blockquote>
<p>It seems that I can just <strong>directly</strong> get the QtWidget and play with its size?</p>
</blockquote>
</aside>
<p>It’s not that simple I think. The central widget size is determined according to its size policy, which you can check with <code>slicer.util.mainWindow().centralWidget().sizePolicy</code>. So it might be expanding to fill the space given to it within its layout, and in that case you’d have to control its size indirectly as I’ve described. You can also try change the size policy, or change the min/max sizes to get different effects. I’m not sure what effect you’re trying to get exactly.</p>
<aside class="quote no-group" data-username="user4" data-post="5" data-topic="22275">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/user4/48/13172_2.png" class="avatar"> user4:</div>
<blockquote>
<p>However I can not resize the window with the code below:</p>
</blockquote>
</aside>
<p><code>resizeDocks</code> was used in the case of resizing the python console and module panel dock widgets-- that’s because those are QDockWidgets, which are special. The central widget is not a QDockWidget so it is treated differently.</p>

---
