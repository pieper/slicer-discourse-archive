# Buttons need color

**Topic ID**: 27181
**Date**: 2023-01-10
**URL**: https://discourse.slicer.org/t/buttons-need-color/27181

---

## Post #1 by @Ulli_Wagner (2023-01-10 21:44 UTC)

<p>Hi,<br>
I am a new Slicer user. I would like to suggest that buttons appear in color. It is hard to recognize that the Apply button needs to be clicked because it has the same color as the field labels and dropdown lists. See screenshot below. I noticed the same with other buttons.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4edb09a23d557d69e327a4f49ff579424ed96a62.png" alt="image" data-base62-sha1="bfAwM9JWC4fw69AtPcFo4WkUa8a" width="506" height="328"></p>

---

## Post #2 by @fedorov (2023-01-11 03:47 UTC)

<p><a class="mention" href="/u/ulli_wagner">@Ulli_Wagner</a> thank you for providing your feedback.</p>
<p>I was helping Ulli navigate Slicer, and the other two situations where key buttons were missed was “Load” in DICOM Browser and “Restart” in Extension manager. I completely agree those are indeed very easy to miss.</p>

---

## Post #3 by @lassoan (2023-01-11 04:42 UTC)

<p>Thank you for the feedback. It is very useful to get specific information about what be users find unintuitive.</p>
<p>We definitely need to solve the issue of having some buttons that are ready to miss.</p>
<p>I’m not sure if the proposed solution of changing the color is ideal, because we use a standard color scheme and usually when we modify such defaults then it tends to result in unfamiliar look&amp;feel. Adding more colors would also go against current simple monochrome GUI design trends (the application may look odd and/or dated).</p>
<p>Maybe we could address the issues by changing the location or spacing of the widgets? For example, if we don’t show the textbox below the Apply button until the first run, increase the space around the button, and maybe if we make the button narrower then they button will be more noticeable. Also, maybe the “Apply” text of the button is not completely clear either?</p>

---

## Post #4 by @ebrahim (2023-01-11 05:10 UTC)

<p>Another alternative to color is to give a more prominent border or shading so it looks “pressable” and at-a-glance distinct from non-pressable UI elements.</p>
<p>(But with shading/borders also the wrong approach can easily lead to a tacky or dated look)</p>
<p>I’m thinking of something like the contrast seen here:<br>
                    <a href="https://doc.qt.io/qt-6/images/qtquickcontrols2-customize-buttons.png" target="_blank" rel="noopener nofollow ugc" class="onebox">
            <img src="https://doc.qt.io/qt-6/images/qtquickcontrols2-customize-buttons.png" width="360" height="120">
          </a>

<br>
(a figure from <a href="https://doc.qt.io/qt-6/qtquickcontrols2-customize.html#attached-properties" rel="noopener nofollow ugc">this page</a>)</p>

---

## Post #5 by @jamesobutler (2023-01-11 14:57 UTC)

<aside class="quote no-group" data-username="Ulli_Wagner" data-post="1" data-topic="27181">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ulli_wagner/48/17974_2.png" class="avatar"> Ulli_Wagner:</div>
<blockquote>
<p>It is hard to recognize that the Apply button needs to be clicked because it has the same color as the field labels and dropdown lists.</p>
</blockquote>
</aside>
<p>All the objects that can be pressed have the same look with Qt classic widget styling. The Collapsible buttons (Inputs/Outputs/Advanced), push buttons (Show 3D/Apply), comboboxes (Segmentation Task) and checkboxes which are all take input share their look.</p>
<p>I think what is being requested is more along the design lines of primary/secondary/tertiary styling of buttons as in material design (<a href="https://m3.material.io/components/buttons/overview#155c46f7-e332-4698-9d17-87a5701413fa" class="inline-onebox" rel="noopener nofollow ugc">Common buttons – Material Design 3</a>). Where material design is often seen in Qt QML usage planned with figma (<a href="https://www.qt.io/blog/qt-quick-control-templates-for-figma" class="inline-onebox" rel="noopener nofollow ugc">Creating Controls from Figma Design</a>). It is easier to identify that “Apply” is the primary action and more important than the button that expands the Advanced section or others.</p>

---

## Post #6 by @lassoan (2023-01-11 18:11 UTC)

<p><a class="mention" href="/u/jamesobutler">@jamesobutler</a> you raise some good points. Qt classic widget style can distinguish the default action (which button is clicked if you hit Enter in the “form”), see for example in “Add data” window:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d2afad2caa452c84ed920c7e3c2921931037755.png" data-download-href="/uploads/short-url/dicuhO2GBUavQoQwx1tsT2xlwwJ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/d/5d2afad2caa452c84ed920c7e3c2921931037755.png" alt="image" data-base62-sha1="dicuhO2GBUavQoQwx1tsT2xlwwJ" width="690" height="409" data-dominant-color="383838"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">816×484 12.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Maybe we should just make the <code>Apply</code> buttons the default button? It would highlight the button with a color accent and it could be also useful to be able to run the module by hitting the Enter key.</p>

---

## Post #7 by @jamesobutler (2023-01-11 18:45 UTC)

<p>Yes for certain situations defining the appropriate default action for a QDialog as you have shown is helpful. However the highlighting you show is based on the focus where the default action is the default focus. Clicking/tabbing elsewhere can change this highlighting focus. In the examples below the button primary color would remain even if the focus is elsewhere. There of course would be a slightly differently shade when it is focused/hovered/pressed/disabled.</p>
<p>Where in the situation of dialogs they would be stylized based on button role like:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/6/b6b99067b04d2f47da8c999666494cadb8a856ac.png" alt="image" data-base62-sha1="q4st4cjzE1hR7xp3kWMViYz7Bvu" width="437" height="231"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/3/13c34f5199b58dae5c526fa8e1abf15a8cf301d7.png" alt="image" data-base62-sha1="2OPwk1y7ws5lWmbicKgHVzAzCzZ" width="435" height="240"></p>
<p>The bigger topic is indicating levels of importance of buttons with different styling (such as different colors). There is <a href="https://github.com/UN-GCPDS/qt-material" class="inline-onebox" rel="noopener nofollow ugc">GitHub - UN-GCPDS/qt-material: Material inspired stylesheet for PySide2, PySide6, PyQt5 and PyQt6</a> which tries to apply this type of styling with Qt classic widget styling, but really requires more stylesheet specification for various buttons on an individual basis to mark them as “Primary” buttons or “Secondary” buttons. That repo provides an example usage that would be like <code>self.main.pushButton.setProperty('class', 'big_button')</code>. Currently we apply a QStylesheet that is applied to all buttons without defining individual customizations based on importance/button role.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/951a2ef3cc68342a070a0c94791ea1822bf09f8f.png" data-download-href="/uploads/short-url/lh1eVAJMLoSAVxFSgDZXr43zhyT.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/951a2ef3cc68342a070a0c94791ea1822bf09f8f.png" alt="image" data-base62-sha1="lh1eVAJMLoSAVxFSgDZXr43zhyT" width="690" height="241" data-dominant-color="EFF1F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">712×249 22.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #8 by @muratmaga (2023-01-11 19:16 UTC)

<aside class="quote no-group" data-username="jamesobutler" data-post="7" data-topic="27181">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jamesobutler/48/7511_2.png" class="avatar"> jamesobutler:</div>
<blockquote>
<p>However the highlighting you show is based on the focus where the default action is the default focus. Clicking/tabbing elsewhere can change this highlighting focus.</p>
</blockquote>
</aside>
<p>To further add to this point, we have modules that has multiple “apply” like button (one for each step of the process). so maintaining focus on all of them won’t be possible.</p>
<p>In general similarity of these buttons to the general UI elements (and hence not noticing that there needs to be interaction) has been a common complaint in our community too.</p>

---

## Post #9 by @sandigeeup (2023-01-13 11:39 UTC)

<p>Changing the apply button to upper case and bolder would work and tbh I found that after a few uses, it become intuitive to look for the apply button and if you’re using slicer alot much of the points above are resolved with familiarity.</p>

---

## Post #10 by @Lohi (2023-01-13 21:14 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="27181">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Adding more colors would also go against current simple monochrome GUI design trends</p>
</blockquote>
</aside>
<p>But, is ‘Trending’ always a good thing… Colour palettes do need to be sensitive to the 7% of males with red/green deficiency, and a couple of other issues, but there are good guidelines for that. If not suing colour, then there needs to be some geometric, or typographic, differentiator for required/desired action buttons.<br>
I guess that this forum is your ‘Focus Group’ ; we often found surprises when working with ‘trusted external reviewers’, people with no in-depth experience with applications. Big surprises  <img src="https://emoji.discourse-cdn.com/twitter/wink.png?v=12" title=":wink:" class="emoji" alt=":wink:" loading="lazy" width="20" height="20"><br>
(I worked at Tektronix, Agilent, Rohde &amp; Schwarz, and a big mobile phone company, where we did this type of work with new, or proposed, applications.)</p>
<p>All the best to you-all in 2023!</p>

---

## Post #11 by @Thibault_Pelletier (2023-01-16 08:29 UTC)

<p>Hi everyone,</p>
<p>If you want to try what Slicer would look like using Material color schemes, you may be interested in the qt-material python extension (<a href="https://github.com/UN-GCPDS/qt-material" class="inline-onebox" rel="noopener nofollow ugc">GitHub - UN-GCPDS/qt-material: Material inspired stylesheet for PySide2, PySide6, PyQt5 and PyQt6</a>).</p>
<p>It can be used directly in Slicer’s Python console :</p>
<pre><code class="lang-auto">slicer.util.pip_install("qt-material")
from qt_material import apply_stylesheet
apply_stylesheet(slicer.app, theme='light_blue.xml')
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/8/9807b450b5d47bb6f7d26ea27caf09c74c4026fa.png" data-download-href="/uploads/short-url/lGV55gIeQLSe17TkonCg98oQrii.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/9807b450b5d47bb6f7d26ea27caf09c74c4026fa_2_690x370.png" alt="image" data-base62-sha1="lGV55gIeQLSe17TkonCg98oQrii" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/9807b450b5d47bb6f7d26ea27caf09c74c4026fa_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/9807b450b5d47bb6f7d26ea27caf09c74c4026fa_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/8/9807b450b5d47bb6f7d26ea27caf09c74c4026fa_2_1380x740.png 2x" data-dominant-color="6F707A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1030 68.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #12 by @Sam_Horvath (2023-01-26 18:39 UTC)

<p>I am planning to look at how we can leverage / extend the qt-material package during the upcoming project week.</p>

---
