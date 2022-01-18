# multibarplot
Simple function to plot multiple barplots in the same figure. Supports padding and custom color.

# Usage
Exposes the function `grouped_barplot`.

```python
import numpy as np
import matplotlib.pyplot as plt

from multibarplot import grouped_barplot 

x = np.arange(3)
desired_padding = 0.1
ys = np.array([[0.1, 0.2, 0.3], [0.5, 0.25, 0.4], [0.1, 0.2, 0.3]])
colors = ["red", "blue", "coral"]
labels = ["a", "b", "c"]

fig, ax = plt.subplots(1,1)
grouped_barplot(ax, x, ys, desired_padding, colors, labels=labels)
ax.set_xticks(x)
ax.set_xticklabels(["First bars", "Second bars", "Third bars"])
fig.legend()

plt.show()
```

![](example.png)
