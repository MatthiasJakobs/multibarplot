import numpy as np

def calculate_bar_width(nr_bars, desired_padding):
    space_after_padding = 1 - 2 * desired_padding
    width = space_after_padding / nr_bars

    return width

def calculate_x_positions(nr_bars, width):
    nr_one_side = nr_bars // 2
    odd_nr_bars = nr_bars % 2 == 1
    offsets = [i * width/2 for i in range(nr_one_side)]
    one_side = np.array([offsets[i-1] + i * width/2 + odd_nr_bars*width/2 for i in range(1, nr_one_side+1)])

    if odd_nr_bars:
        return np.concatenate([np.flip(-one_side), np.zeros((1)), one_side])
    else:
        return np.concatenate([np.flip(-one_side), one_side])

def grouped_barplot(ax, ys, x_positions=None, padding=0.1, colors=None, labels=None):
    nr_ticks, bars_per_tick = ys.shape
    if x_positions is None:
        x_positions = np.arange(nr_ticks)
    if colors is None:
        colors = [f"C{i}" for i in range(bars_per_tick)]

    used_labels = set()
    for x, y in zip(x_positions, ys):
        nr_bars = len(y)
        width = calculate_bar_width(nr_bars, padding)
        xs = calculate_x_positions(nr_bars, width) + x
        for i, (_x, _y) in enumerate(zip(xs,y)):
            if labels is not None and labels[i] not in used_labels:
                ax.bar(x=_x, height=_y, width=width, color=colors[i], label=labels[i])
                used_labels.add(labels[i])
            else:
                ax.bar(x=_x, height=_y, width=width, color=colors[i])

