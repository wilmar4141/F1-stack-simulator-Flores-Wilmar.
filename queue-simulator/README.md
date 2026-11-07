# Flask Queue Simulator

A FIFO (First In, First Out) queue simulator built with Flask. Adapted from the Stack Simulator.

## Run

    pip install -r requirements.txt
    python app.py

Open http://127.0.0.1:5000

## Operations
- **Enqueue** adds a value to the rear.
- **Dequeue** removes the front value and shows it in Removed Items.
- **Peek** highlights the front value without removing it.
- **Clear** resets the queue and removed items.

## Files
- app.py: Flask routes
- queue_model.py: Queue class
- templates/: base.html, index.html, contact.html
- static/: css/style.css, js/ui.js
