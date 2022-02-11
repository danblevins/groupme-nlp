import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.set_context("talk")
sns.set_style("dark")
sns.despine()

def show_values(axs, orient="v", space=.01):
    def _single(ax):
        if orient == "v":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() / 2
                _y = p.get_y() + p.get_height() + (p.get_height()*0.01)
                value = '{:.1f}'.format(p.get_height())
                ax.text(_x, _y, value, ha="center") 
        elif orient == "h":
            for p in ax.patches:
                _x = p.get_x() + p.get_width() + float(space)
                _y = p.get_y() + p.get_height() - (p.get_height()*0.5)
                value = '{:.1f}'.format(p.get_width())
                ax.text(_x, _y, value, ha="left")

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _single(ax)
    else:
        _single(axs)

def bar_chart(x_axis: str, y_axis: str, title: str, name: str, data=None) -> True:
    plt.clf()
    plt.close()

    generic_bar_color = []
    bars = len(data)-3
    for i in range(bars):
        generic_bar_color.append("#444444")

    palette = ["#FFD700", "#C0C0C0", "#CD7F32"] + generic_bar_color

    sns.color_palette("muted")
    plot = sns.barplot(x=x_axis, y=y_axis, data=data, palette=palette, ci=None)
    plot.set(yticklabels=[])
    plt.title(title)
    plt.ylim(0, max(data[y_axis]*1.10))
    plt.ylabel("")
    plt.legend(frameon=False)
    show_values(plot)
    plt.savefig("image")

    return True

def line_chart(x_axis: str, y_axis: str, title: str, name: str, data=None) -> True:
    plt.clf()
    plt.close()

    sns.color_palette("muted")
    plot = sns.lineplot(x=x_axis, y=y_axis, data=data, color="#444444", ci=None)
    plt.xticks(np.arange(min(data[x_axis]), max(data[x_axis])+1))
    plt.title(title)
    plt.ylim(0, round(max(data[y_axis]*1.10),10))
    plt.ylabel("")
    plt.legend(frameon=False)
    plt.savefig("image")

    return True

def ngram_bar_chart(x_axis: str, y_axis: str, title: str, name: str, data=None) -> True:
    plt.clf()
    plt.close()

    palette = []
    bars = len(data)
    for i in range(bars):
        palette.append("#444444")

    sns.color_palette("muted")
    plot = sns.barplot(x=x_axis, y=y_axis, data=data, palette=palette, ci=None, orient='h')
    plt.title(title)
    plt.xlim(0, max(data[x_axis]*1.10))
    plt.xlabel("")
    plt.ylabel("")
    plt.legend(frameon=False)
    show_values(plot, orient='h')
    plt.tight_layout()
    plt.savefig("image")

    return True