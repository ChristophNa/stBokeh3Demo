import streamlit as st
from bokeh.models import ColumnDataSource, CustomJS
from bokeh.plotting import figure
import pandas as pd
import numpy as np
from streamlit_bokeh3_events import streamlit_bokeh3_events

@st.cache_data
def data():
    df = pd.DataFrame({"x": np.random.rand(500), "y": np.random.rand(500), "size": np.random.rand(500) * 10})
    return df

df = data()
source = ColumnDataSource(df)

st.subheader("Select Points From Map")

plot = figure( tools="lasso_select,reset", width=500, height=500)
plot.circle(x="x", y="y", size="size", source=source, alpha=0.6)

source.selected.js_on_change(
    "indices",
    CustomJS(
        args=dict(source=source),
        code="""
        document.dispatchEvent(
            new CustomEvent("TestSelectEvent", {detail: {indices: cb_obj.indices}})
        )
    """,
    ),
)

event_result = streamlit_bokeh3_events(
    events="TestSelectEvent",
    bokeh_plot=plot,
    key="foo1",
    debounce_time=100,
    refresh_on_update=False
)

# some event was thrown
if event_result is not None:
    # TestSelectEvent was thrown
    if "TestSelectEvent" in event_result:
        st.subheader("Selected Points' Pandas Stat summary")
        indices = event_result["TestSelectEvent"].get("indices", [])
        st.table(df.iloc[indices].describe())

st.subheader("Raw Event Data")
st.write(event_result)
