#%%
import git
import matplotlib.pyplot as plt
import numpy as np


repo = git.Repo(search_parent_directories=True)
short_hash = repo.head.object.hexsha[:10]

dummy_data = np.random.rand(10, 10)

figure = plt.figure(figsize=(6, 4))
plt.imshow(dummy_data)
plt.title(f"Commit: {short_hash}")
plt.show()
