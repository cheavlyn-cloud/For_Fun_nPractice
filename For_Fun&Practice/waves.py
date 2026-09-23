import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider

# Apply the global dark theme style
plt.style.use('dark_background')

# 1. Set up the figure and axis layout
fig, ax = plt.subplots()
# Made more room at the bottom (0.35) to comfortably fit 4 sliders
plt.subplots_adjust(bottom=0.35)

fig.patch.set_facecolor('black')
ax.set_facecolor('black')

x = np.linspace(0, 4 * np.pi, 1000)

# Line 1 (Cyan) Initial Parameters
h1, sp1 = 1.0, 1.0
# Line 2 (Blue) Initial Parameters
h2, sp2 = 0.5, 2.0

# Plot both lines with distinct colors and labels for the legend
line1, = ax.plot(x, h1 * np.sin(x), color='cyan', label='Mode A: Cyan Wave')
line2, = ax.plot(x, h2 * np.cos(x), color='blue', label='Mode B: Blue Wave')

# Display the legend in the upper right corner
ax.legend(loc='upper right')

ax.set_xlim(0, 4 * np.pi)
ax.set_ylim(-2.5, 2.5)
ax.set_title("Dual Moving Waves Mode", color='white')

# 2. Position and create Sliders (Stacked vertically)
# Format: [left, bottom, width, height]
ax_h1  = plt.axes([0.15, 0.24, 0.65, 0.025], facecolor='#222222')
ax_sp1 = plt.axes([0.15, 0.19, 0.65, 0.025], facecolor='#222222')
ax_h2  = plt.axes([0.15, 0.10, 0.65, 0.025], facecolor='#222222')
ax_sp2 = plt.axes([0.15, 0.05, 0.65, 0.025], facecolor='#222222')

# Create the sliders
s_h1  = Slider(ax_h1,  'Cyan H',  0.1, 2.0, valinit=h1,  track_color='#444444')
s_sp1 = Slider(ax_sp1, 'Cyan Sp', 0.1, 3.0, valinit=sp1, track_color='#444444')
s_h2  = Slider(ax_h2,  'Blue H',   0.1, 2.0, valinit=h2,  track_color='#444444')
s_sp2 = Slider(ax_sp2, 'Blue Sp',  0.1, 3.0, valinit=sp2, track_color='#444444')

# Apply text styling and accent theme colors to matching handles
sliders = [s_h1, s_sp1, s_h2, s_sp2]
for s in sliders:
    s.label.set_color('white')
    s.valtext.set_color('white')

s_h1.poly.set_facecolor('cyan')
s_sp1.poly.set_facecolor('cyan')
s_h2.poly.set_facecolor('blue')
s_sp2.poly.set_facecolor('blue')

# 3. Define the animation update function
def update(frame):
    # Dynamically extract current data from all sliders
    cur_h1, cur_sp1 = s_h1.val, s_sp1.val
    cur_h2, cur_sp2 = s_h2.val, s_sp2.val
    
    # Calculate separate independent motion math tracking
    y1 = cur_h1 * np.sin(x - (frame * cur_sp1) / 10.0)
    y2 = cur_h2 * np.cos(x - (frame * cur_sp2) / 10.0) # Uses cosine for visual variety
    
    # Push data changes straight to both items
    line1.set_ydata(y1)
    line2.set_ydata(y2)
    
    return line1, line2

# 4. Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=20, blit=False)

plt.show()
