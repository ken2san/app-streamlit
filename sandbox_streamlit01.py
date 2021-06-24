# streamlit run {File}
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from PIL import Image
from sklearn import datasets
import time

st.title('StreamLit Newbie Site')

@st.cache
def load_data():
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['target'] = iris.target_names[iris.target]
    return df

df = load_data()
targets = list(df.target.unique())
selected_targets = st.multiselect('select targets', targets, default=targets)
df = df[df.target.isin(selected_targets)]

st.dataframe(df.style.highlight_max(axis=0))
fig, ax = plt.subplots()

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(9, 6))
df.plot(ax=axes[0, 0], legend=False)
df.plot(ax=axes[0, 1], legend=False, kind='area')
df.plot(ax=axes[1, 1], legend=False,kind='scatter', x=df.columns[0], y=df.columns[1])
df.plot(ax=axes[1, 2], legend=False, kind='hist', alpha=0.5)


#df.hist()
st.pyplot(fig)

#latest_iteration=st.empty()

# bar = st.progress(0)
# for i in range(0,100):
#     latest_iteration.text(f'iteration {i+1}')
#     bar.progress(i+1)
#     time.sleep(0.1)

matrix = np.random.rand(100,2)/[50,50]+[35.68,139.70]
_df = pd.DataFrame(matrix,columns=['lat','lon'])
_df.head()
st.map(_df)



if st.checkbox('Show Image'):
    img = Image.open('image01.jpg')
    st.image(img,caption="Image",use_column_width=True)

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]
group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
    hist_data, group_labels, bin_size=[.1, .25, .5])

fig.update_layout(
    xaxis = dict(
        tickangle = 0,
        title_text = "Animal",
        title_font = {"size": 20},
        title_standoff = 25),
    yaxis = dict(
        title_text = "Populations",
        title_standoff = 25),
    title ='日本語のタイトル')
# Plot!
st.plotly_chart(fig)

with st.sidebar:
    st.button("Refresh")
