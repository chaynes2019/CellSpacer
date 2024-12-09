import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import math

iterations = 500
T = 100

fig3, ax3 = plt.subplots()

ax3.set_title("Environment over Time")
ax3.set_box_aspect(1)

ax3.set_xlim([-1, 1])
ax3.set_ylim([-1, 1])

ax3.plot(np.array([math.cos(2 * math.pi * 0.001 * k) for k in range(1000)]),
         np.array([math.sin(2 * math.pi * 0.001 * k) for k in range(1000)]),
         'k')

ax3.arrow(0, 0, 1, 0)
ax3.annotate("", xy=(1, 0), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->"))

ax3.arrow(0, 0, 1, 0)
ax3.annotate("", xy=(1, 0), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", color = "red"))

fig3.savefig("CircleTestPlot.png")

def animateEnvironment(t):
    ax3.clear()

    ax3.set_title("Environment over Time")
    ax3.set_box_aspect(1)

    ax3.set_xlim([-1, 1])
    ax3.set_ylim([-1, 1])

    ax3.plot(np.array([math.cos(2 * math.pi * 0.001 * k) for k in range(1000)]),
         np.array([math.sin(2 * math.pi * 0.001 * k) for k in range(1000)]),
         'k')

    ax3.arrow(0, 0, 1, 0)
    ax3.annotate("", xy=(1, 0), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->"))

    ax3.arrow(0, 0, math.cos(2 * math.pi * t / T),
              math.sin(2 * math.pi * t / T))
    ax3.annotate("", xy=(math.cos(2 * math.pi * t / T),
                        math.sin(2 * math.pi * t / T)), xytext=(0, 0),
             arrowprops=dict(arrowstyle="->", color = "red"))

environmentAnim = animation.FuncAnimation(fig3, func = animateEnvironment, frames = iterations, interval = 30)

environmentValuesAnimation = animation.PillowWriter(fps = 30)

environmentAnim.save("circleTestGif.gif")