
import pandas as pd
import random
import config

def generate_data():

    def func(x):
        return 2*x + random.random()

    xs= []
    ys = []    

    for i in range(100):
        x = random.normalvariate(0, 1)
        y = func(x)
        xs.append(x)
        ys.append(y)

    df = pd.DataFrame({"x": xs, "y": ys})
    df.to_csv(config.DATA_DIR / "data_01.csv", index=False)


generate_data()
