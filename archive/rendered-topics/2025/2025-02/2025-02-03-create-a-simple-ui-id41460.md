---
topic_id: 41460
title: "Create A Simple Ui"
date: 2025-02-03
url: https://discourse.slicer.org/t/41460
---

# Create a simple UI

**Topic ID**: 41460
**Date**: 2025-02-03
**URL**: https://discourse.slicer.org/t/create-a-simple-ui/41460

---

## Post #1 by @SANTIAGO_PENDON_MING (2025-02-03 13:49 UTC)

<p>Hi to everyone!</p>
<p>version: 5.6.2<br>
OS: windows11</p>
<p>I’m working in create a robust (but also simple) interface for  our python module named SegmentTracer. This code contains several classes and create/remove buttons begins to be hard.</p>
<p>Watching some Scripted Modules as could be Endoscopy I see that the most common  way to do that is using a classUI to manage all the functions related with the UI.  I am not familiarized with <code>ScriptedLoadableModuleWidget </code>  but I have made a complete Qt integration:</p>
<pre><code class="lang-auto">import slicer
import qt

class SegmentTracerUI:
    def __init__(self):
        
        
        self.dock_widget = slicer.util.mainWindow().findChild(qt.QDockWidget,"SegmentTracerDockWidget")
        
        if self.dock_widget:
            self.dock_layout = self.dock_widget.findChild(qt.QWidget).layout()
            self.label = self.dock_widget.findChild(qt.QLabel)

       
        else:
            self.main_window.setStatusBar(None)
            self.create_dock_widget()

    def create_dock_widget(self, title="ST Assistant"):
        """Crea el dock widget y lo agrega a la interfaz."""
        self.dock_widget = qt.QDockWidget(title)
        self.dock_widget.setObjectName("SegmentTracerDockWidget")
        
        # Contenedor y layout
        dock_content = qt.QWidget()
        self.dock_layout = qt.QVBoxLayout(dock_content)
        
        # Label de bienvenida
        self.label = qt.QLabel("Welcome to SegmentTracer.")
        self.label.setFont(qt.QFont("Times", 11))
        self.dock_layout.addWidget(self.label)
        
        self.dock_widget.setWidget(dock_content)
        self.main_window.addDockWidget(qt.Qt.LeftDockWidgetArea, self.dock_widget)
        
        

    def create_button(self, function, text):
        """Crea un botón y lo añade al dock."""
        button = qt.QPushButton(text)
        button.clicked.connect(function)
        self.dock_layout.addWidget(button)
        slicer.app.processEvents()
        return button

    def clear_buttons(self):
        """Elimina todos los botones del dock, preservando solo el QLabel."""
        for i in reversed(range(self.dock_layout.count())):
            widget = self.dock_layout.itemAt(i).widget()
            if widget and widget is not self.label:
                widget.setParent(None)
                widget.deleteLater()
        slicer.app.processEvents()

    def show_message(self, text):
        """Cambia el texto del QLabel dentro del dock."""
        self.label.setText(text)
        print(text)
        slicer.app.processEvents()
</code></pre>
<p>What I am wondering is:</p>
<p>1º Can I modify something to guarantee a better user experience? (i.e. not blocking the Slicer window)</p>
<p>2º Also, to link one function to a specific button I use:</p>
<pre><code class="lang-auto">self._continue_action = action_creator(myFunction, event_type = 'Continue', args = [myFunctionArg1,myFunctionArg2,...])
self.button_continue = ui.create_button(self.button_continue_action, 'Continue')
</code></pre>
<p>where the function action_creator is the following function:</p>
<pre><code class="lang-auto">    def action_creator(self, function, event_type, args = []):

        if event_type == 'Continue':
            slicer.app.processEvents()
            def action():
                if len(args) &gt; 0:
                    function(*args)
                else:
                    function()
                return None
            return action
</code></pre>
<p>Which looks a little bit difficult… Has anyone any idea to associate the button with the functions and their args?</p>
<p>Thanks a lot! <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @SANTIAGO_PENDON_MING (2025-02-04 13:49 UTC)

<p>Update: I use this class now to manage all the UI:</p>
<pre><code class="lang-auto">
class SegmentTracerUI:
    def __init__(self):
        slicer.util.mainWindow().setStatusBar(None)
 
        

    def createDockInterface(self, title="ST Assistant"):
        """Crea el dock widget y lo agrega a la interfaz."""
        self.dock_widget = qt.QDockWidget(title)
        self.dock_widget.setObjectName("SegmentTracerDockWidget")
        
        # Contenedor y layout
        dock_content = qt.QWidget()
        self.dock_layout = qt.QVBoxLayout(dock_content)
        
        # Label de bienvenida
        self.label = qt.QLabel("Welcome to SegmentTracer.")
        self.label.setFont(qt.QFont("Times", 11))
        self.dock_layout.addWidget(self.label)
        
        self.dock_widget.setWidget(dock_content)
        slicer.util.mainWindow().addDockWidget(qt.Qt.LeftDockWidgetArea, self.dock_widget)

    def create_button(self, function, text, type, args=[]):
        """Crea un botón y lo añade al dock con la opción de pasarle argumentos a la función."""
        button = qt.QPushButton(text)
        
        # Asignación de la función que actualiza el estado global
        button.clicked.connect(lambda: self.on_button_pressed(type, function, args))
        
        self.dock_layout.addWidget(button)
        slicer.app.processEvents()
        return button

    def on_button_pressed(self, button_type, function, args):
        """Maneja la lógica cuando un botón es presionado, actualiza el estado global y llama a la función."""
        self.choice = button_type
        print(self.choice)
        function(*args)
        
    def fastRemoveButtons(self): # Más rápida que la antigua removeButtons
        """Elimina todos los botones del dock, preservando solo el QLabel, de manera más eficiente."""
       
        widgets_to_remove = [self.dock_layout.itemAt(i).widget() for i in range(self.dock_layout.count())]
        
        for widget in widgets_to_remove:
            if widget and widget is not self.label:
                widget.delete()
    
       
        slicer.app.processEvents()
        

    def removeButtons(self):
        
        """Elimina todos los botones del dock, preservando solo el QLabel."""
        for i in reversed(range(self.dock_layout.count())):
            widget = self.dock_layout.itemAt(i).widget()
            if widget and widget is not self.label:
                widget.setParent(None)
                widget.deleteLater()
        slicer.app.processEvents()

    def showMessage(self, text):
        """Cambia el texto del QLabel dentro del dock."""
        self.label.setText(text)
        print(text)
        slicer.app.processEvents()
</code></pre>
<p>This works fine most of the times but, sometimes (creating/deleting buttons) it crashes and slicer app closes suddenly. The crash is not related with an specific part of the code, because it not always fail in the same place or even fail…</p>
<p>I have reading something about delete/deleteLater functions in qt and the related dangers when you try to delete a button in some specific thread, but I’m not sure if this can affect in this case.</p>
<p>Can anybody tell me how to remove/ create the buttons in a better way?</p>
<p>Thanks a lot.</p>

---

## Post #3 by @shai-ikko (2025-02-05 08:39 UTC)

<p>Hi,</p>
<p>It isn’t clear from the description above if the buttons are truly dynamic (come and go as the module is being used) or removing them is just part of your module cleanup.</p>
<p>Either way, my (non-expert) advice is to use the extension wizard, which is probably less simple (in the sense that it introduces more components and concepts) but easier.</p>

---

## Post #4 by @SANTIAGO_PENDON_MING (2025-02-05 08:56 UTC)

<aside class="quote no-group" data-username="shai-ikko" data-post="3" data-topic="41460">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/shai-ikko/48/15765_2.png" class="avatar"> shai-ikko:</div>
<blockquote>
<p>e description above if the buttons are truly dynamic (come and go as the module is being used) or removing them is just part of your module cleanup.</p>
</blockquote>
</aside>
<p>Hi <a class="mention" href="/u/shai-ikko">@shai-ikko</a> , the buttons are dynamic in the sense of I have other classes that calls the UI and this functions in the new class creates/deletes buttons during the process allowing the user take decisions. Usually a function in the main class execute some code (for example segment something in a volume) and then creates a button to ask if the segment is OK or it should be re-done.</p>
<p>When the user clicks the button, the interface has to remove all the buttons and continue the execution (for example, saving the segment or create other buttons…)</p>
<p>Example use:</p>
<pre><code class="lang-auto"> def startQuestioningReSegmentation(self):

   
        self.stUI.showMessage('What do you want to do now?')

        # Button generation: 
        self.button_left = self.stUI.create_button(self.startAddNewPointsToSegmentationByEvent, text = 'Add points at Left', type = True, args = []) # Botón para poner puntos en la rama izq., equivalente a la pregunta: Ponemos puntos en la izq.?-&gt; True
        self.button_right  = self.stUI.create_button(self.startAddNewPointsToSegmentationByEvent, text = 'Add points at Right', type = False, args = []) # Botón para poner puntos en la rama der., equivalente a la pregunta: Ponemos puntos en la izq.?-&gt; False
        



    def startAddNewPointsToSegmentationByEvent(self):

        self.stUI.showMessage('Select first point')
        # Delete Buttons:
        self.stUI.fastRemoveButtons()
        
        # Register Button:

        self.button_register = self.stUI.create_button(self.addNewPointsToSegmentationByEvent, text = 'Register Point', type = 'Continue', args = [])

</code></pre>
<p>In other things, where I can find some examples of extensions-wizard?</p>

---

## Post #5 by @shai-ikko (2025-02-05 13:28 UTC)

<p>The Extension Wizard is a tool that is included in Slicer:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c8d689805a92c6918710f88b36283e61bdfc504.png" data-download-href="/uploads/short-url/dcKTpym5xoYsiYFi34pE00x5YWw.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c8d689805a92c6918710f88b36283e61bdfc504_2_410x500.png" alt="image" data-base62-sha1="dcKTpym5xoYsiYFi34pE00x5YWw" width="410" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c8d689805a92c6918710f88b36283e61bdfc504_2_410x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/c/5c8d689805a92c6918710f88b36283e61bdfc504_2_615x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c8d689805a92c6918710f88b36283e61bdfc504.png 2x" data-dominant-color="D1D1DA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">637×776 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Re dynamics – unless your requirements are truly exceptional, the more common practice is to create all the buttons in advance, and disable or hide those which aren’t relevant, rather than create and destroy them on the go. If you do it that way, you will be more likely to find similar examples, and answers from people working in similar ways.</p>
<p>That said, of course you know your requirements and I don’t.</p>

---
