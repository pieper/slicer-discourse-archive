---
topic_id: 36913
title: "Slicer Closes Suddendly In Event Driven Program"
date: 2024-06-20
url: https://discourse.slicer.org/t/36913
---

# Slicer closes suddendly in event driven program

**Topic ID**: 36913
**Date**: 2024-06-20
**URL**: https://discourse.slicer.org/t/slicer-closes-suddendly-in-event-driven-program/36913

---

## Post #1 by @SANTIAGO_PENDON_MING (2024-06-20 09:47 UTC)

<p>Hi to everyone, the problem today is a bit weird.</p>
<p>Me and my team have developed a python script where we can create and delete buttons (these buttons allow the user make actions i.e. reslice volume automatically using Resample Scalar Volume or smooth and retouch centerlines generated).</p>
<p>The buttons are made using:</p>
<pre><code class="lang-auto">def create_button(function,text):
    slicer.util.mainWindow().setStatusBar(None)
    stDock = slicer.util.mainWindow().findChild(qt.QDockWidget,"SegmentTracerDockWidget")
    
    if stDock:
        # Crear el botón
        button = qt.QPushButton(text)
        # Conectar la señal clicked del botón a la función de retorno
        button.clicked.connect(function)
        # Establecer un ancho máximo para el botón
        # button.setMaximumWidth(100)  # Ajusta este valor según tus necesidades
        # Obtener el layout del contenido del dock
        layout = stDock.widget().layout()
        # Agregar el nuevo botón al layout
        layout.addWidget(button)
        slicer.app.processEvents()
        return button

</code></pre>
<p>and one example of use could be:</p>
<pre><code class="lang-auto">        self.button_continue_action = self.action_creator(self.cleanPointCloud, event_type = 'Continue')
        self.button_continue = utils.create_button(self.button_continue_action,'Continue')
</code></pre>
<p>To create buttons we also use _action call, where self.action_creator is:</p>
<pre><code class="lang-auto">    def action_creator(self, function, event_type, ):
        
        if event_type in ['Yes', 'No']:
            slicer.app.processEvents()
            def yes_no_button():
            
                if event_type == 'Yes':
                    self.choice = True 
                    
                elif event_type == 'No':
                    self.choice = False
                
                function()
                return None
            
            return yes_no_button
            
        elif event_type == 'Continue':
            slicer.app.processEvents()
            def continue_button():
                function()
            return continue_button
    
</code></pre>
<p>We use the action creator to track the user decisions and make decisions inside the code.</p>
<p>To give a completely example, this buttons are generated in one Qt Dock:</p>
<pre><code class="lang-auto">def createDockInterface():
    # Delete the statusBar to have cleaner view:
    slicer.util.mainWindow().setStatusBar(None)
    
    # Create and name the widget:
    dock_widget = qt.QDockWidget("ST Assistant v16")
    dock_widget.setObjectName('SegmentTracerDockWidget')
    
    
    # Add the Welcome text:
    label = qt.QLabel("Welcome to SegmentTracer. ")
    dock_layout = qt.QVBoxLayout()
    dock_layout.addWidget(label)
    dock_content = qt.QWidget()
    dock_content.setLayout(dock_layout)
    dock_widget.setWidget(dock_content)
    
    # Display the widget in bottom left corner:
    slicer.util.mainWindow().addDockWidget(qt.Qt.LeftDockWidgetArea, dock_widget)   
</code></pre>
<p>If everything is working fine in the patient, the user only has to click continue buttons, with any interactions or extra process. This buttons are deleted using:</p>
<pre><code class="lang-auto">self.button_continue.delete()
</code></pre>
<p>My question is the next one:</p>
<p>Sometimes the code runs well (I repeat, the user only has to do click in the button if the process is correct) and nothing strange happen, but in other cases Slicer starts ‘thinking’ for a few seconds (usually 3-4 seconds) and then suddenly closes. If I open the same patient, run the same code and make the same click again the code runs well again (or not).</p>
<p>I’m very concerned with this behavior, because I guess is not related with the functions the buttons call (functions works well always)</p>
<p>I’m not allowed to share the whole code but the scheme of use for buttons and their functions are the same over the whole code.</p>
<p>Also, we worked in reduce the number of cores slicer take to operate (we reduce the number from 12 (the maximum possible) to 9), just in case Slicer collapses the system and the Windows Administrator close it, but nothing happen. We move the affinity to the process to high, letting Slicer be more ‘important’ in the list of task the PC has to do, but nothing happen.</p>
<p>The memory and CPU usage was tracked during the code execution and the peaks of usage are clearly not related with suddenly closing events.</p>
<p>At this moment, the project is well underway and we don’t have any alternative to deal with this problem, so any help or suggestion could be very useful.</p>
<p>Thanks to the community once again. <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>

---

## Post #2 by @pieper (2024-06-20 12:56 UTC)

<p>It’s hard to debug from snippets of code, so making a complete stand-alone example that demonstrates the issue will always be best (that’s the magic of open source).  But if I had to guess from a quick read, I think you have some kind of recursion condition that is generating buttons in a loop or events triggering each other back and forth.</p>
<p>Even if you don’t share it, the process or stripping down your code to just the essentials and then incrementally adding back features can help you ensure you have the event processing and guid manipulation debugged.</p>

---
