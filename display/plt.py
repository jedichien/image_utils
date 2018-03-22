"""
Display package
"""
import matplotlib.pyplot as plt

def simple_show_grid(images, rows, cols, cmap='rgb', figsize=(10, 10)):
    assert images.shape[-1] <= rows*cols
    fig, ax_list = plt.subplots(cols, rows, figsize=figsize)
    for idx, ax in enumerate(ax_list.ravel()):
        if idx < images.shape[-1]:
            ax.imshow(images[:,:,idx], cmap=cmap)
        else:
            ax.axis('off')
    plt.setp([ax.get_xticklabels() for ax in ax_list.ravel()], visible=False)
    plt.setp([ax.get_yticklabels() for ax in ax_list.ravel()], visible=False)
    plt.show()
