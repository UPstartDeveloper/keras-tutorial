import matplotlib as plt
import numpy as np


def visualize_classes(class_names):
    """This function visualizes the classes in an image classification
       dataset. It depends on the libraries Matplotlib and Numpy.

       Parameters:
       class_names(list): a list of strings for the different class names

       Returns: None

    """
    fig = plt.figure(figsize=(8, 3))
    for i in range(num_classes):
        ax = fig.add_subplot(2, 5, 1 + i, xticks=[], yticks=[])
        idx = np.where(y_train[:] == i)[0]
        features_idx = x_train[idx, ::]
        img_num = np.random.randint(features_idx.shape[0])
        im = np.transpose(features_idx[img_num, ::], (1, 2, 0))
        ax.set_title(class_names[i])
        plt.imshow(im)
    plt.show()
