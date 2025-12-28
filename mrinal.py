import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns

np.random.seed(1)
df = pd.DataFrame(np.random.randint(10,100,(30,6)),
    columns=["Performance","Sports","Transport","Disease","Sales","Health"])
df["Day"] = range(1,31)

print(df.describe())

plt.figure(figsize=(10,6))
for i,c in enumerate(df.columns[:-1],1):
    plt.subplot(2,3,i)
    sns.lineplot(x="Day", y=c, data=df); plt.title(c)

plt.tight_layout(); plt.show()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm"); plt.show()