import streamlit as st
import altair as alt
import pandas as pd

phylum = pd.read_csv("data/phylum.csv")
phylum["Sample"] = phylum["Sample"].astype(str)
phylum = phylum.set_index("Sample")

genus = pd.read_csv("data/genus.csv")
genus["Sample"] = genus["Sample"].astype(str)
genus = genus.set_index("Sample")

muestra = st.multiselect(
    "Elija la muestra a visualizar", list(phylum.index)
)
print(muestra)


if not muestra:
    st.error("Por favor, elija una muestra para visualizar")
else:

    phylum_samples = phylum.loc[muestra]

    genus_samples = genus.loc[muestra]

    st.write("Taxonomia: Phylum")
    st.bar_chart(phylum_samples)

    st.write("Taxonomia: Genus")
    st.bar_chart(genus_samples)


#st.bar_chart(phylum)
