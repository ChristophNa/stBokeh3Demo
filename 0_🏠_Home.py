import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Streamlit Bokeh3 Events",
        page_icon="⛏️",
    )

    st.write("# Welcome to Streamlit Bokeh3 Events! 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        streamlit_bokeh3_events is a component for integrating [Bokeh3](https://docs.bokeh.org/en/latest/index.html) plots into [Streamlit](https://streamlit.io).  
        **👈 Select a demo from the sidebar** to see some examples
        ### Installation
        ```bash
        pip install streamlit_bokeh3_events
        ```
        ### Code
        - You can find the code for all examples [here](https://github.com/ChristophNa/stBokeh3Demo)
        - [original component](https://github.com/ash2shukla/streamlit_bokeh_events) from ash2shukla for bokeh 2
        - The here used [updated version](https://github.com/ChristophNa/streamlit-bokeh3-events) for bokeh 3
    """
    )


if __name__ == "__main__":
    run()