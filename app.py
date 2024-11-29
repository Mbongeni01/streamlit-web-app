import streamlit as st

# Title and Introduction
st.title("SA End to End: A Guide for Entrepreneurship in South Africa")
st.subheader("The Catalyst of Economic Growth")

st.write("""
SA End to End is a guide for entrepreneurship in South Africa, shining a light on the very institutions 
that entrepreneurs need to be competent with and to reach compliance throughout the lifespan of creating 
and maintaining a private company.
""")

# Sections
st.header("Unemployment and Entrepreneurship")
st.write("""
The citizens of South Africa are able to accomplish anything they put their minds to. However, 
the stark reality of the ever-growing unemployment rates calls for a new spirit of business. This guide 
provides steps for reducing unemployment by fostering entrepreneurship.
""")

st.header("Steps for Company Registration")
st.write("""
To register a business with the Companies and Intellectual Property Commission (CIPC), follow these steps:
""")
st.markdown("""
1. Choose a Business Structure.
2. Create an account on the [CIPC Website](https://www.cipc.co.za).
3. Reserve your business name.
4. Complete the registration application.
5. Submit required documents and pay fees.
6. Receive your registration confirmation.
""")

st.video("https://youtu.be/LHhyesyg75E?si=fs9AYn1ckN675sTk")  # CIPC tutorial

# Funding Institutions
st.header("Funding Institutions")
st.write("""
South Africa offers several funding opportunities for entrepreneurs:
""")
funding_data = {
    "Institution": ["SEDA", "SETA", "NYDA"],
    "Description": [
        "Supports growth and development of SMMEs.",
        "Implements the National Skills Development Strategy.",
        "Focuses on empowering young entrepreneurs."
    ],
    "Link": [
        "https://www.seda.org.za",
        "https://www.servicesseta.org.za",
        "https://www.nyda.gov.za"
    ]
}

for i, institution in enumerate(funding_data["Institution"]):
    st.subheader(institution)
    st.write(funding_data["Description"][i])
    st.write(f"[Learn More]({funding_data['Link'][i]})")

# Tax Compliance
st.header("SARS Compliance")
st.write("""
Steps to file taxes in South Africa:
1. Register for taxes with SARS.
2. Gather financial documentation.
3. Complete and submit returns via the [SARS eFiling System](https://www.sars.gov.za/businesses-and-employers/).
4. Pay taxes by the deadline.
5. Maintain records for at least five years.
""")
st.video("https://youtu.be/dr3mMlJ65is?si=T89rA30DqKUtpHIz")  # SARS tutorial

# Conclusion
st.header("Conclusion")
st.write("""
SA End to End serves as a vital roadmap for aspiring entrepreneurs in South Africa, emphasizing the crucial role of compliance, funding, and proper registration in establishing successful businesses.
""")
