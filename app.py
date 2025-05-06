import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("hiring_data.csv")

# Bias Detection
bias_check = data.groupby('Gender')['Hired'].value_counts(normalize=True).unstack(fill_value=0)
male_hired = bias_check.loc['M', 'Y']
female_hired = bias_check.loc['F', 'Y']
bias_gap = abs(male_hired - female_hired)

# Streamlit UI - Bias Section
st.title("FairHire AI")
st.header("Bias Detection")
st.write(f"Male Hired: {male_hired:.2%}")
st.write(f"Female Hired: {female_hired:.2%}")
st.write(f"Bias Gap: {bias_gap:.2%}")
fig, ax = plt.subplots()
ax.bar(['Male', 'Female'], [male_hired, female_hired], color=['blue', 'orange'])
ax.set_title("Hiring Rate by Gender")
ax.set_ylabel("Hiring Rate (%)")
for i, v in enumerate([male_hired, female_hired]):
    ax.text(i, v + 0.02, f"{v:.0%}", ha="center")
st.pyplot(fig)
if bias_gap > 0.2:
    st.error("High Bias Detected! Action Required!")
elif bias_gap > 0.1:
    st.warning("Moderate Bias Detected! Monitor Closely!")
else:
    st.success("Bias within Acceptable Limits!")

# Transparency Dashboard
st.header("Transparency Dashboard")
candidate = st.selectbox("Select a Candidate", data['Name'])
selected_data = data[data['Name'] == candidate].iloc[0]
st.write(f"Name: {candidate}")
st.write(f"Gender: {selected_data['Gender']}")
st.write(f"Score: {selected_data['Score']}")
st.write(f"Hired: {selected_data['Hired']}")
if selected_data['Hired'] == 'Y':
    reason = f"Score ({selected_data['Score']}) above 80 threshold."
else:
    reason = f"Score ({selected_data['Score']}) below 80 threshold or missing skills (e.g., leadership)."
st.write(f"Reason for Decision: {reason}")
if st.button("Download Report"):
    report = f"Candidate: {candidate}\nGender: {selected_data['Gender']}\nScore: {selected_data['Score']}\nHired: {selected_data['Hired']}\nReason: {reason}"
    st.download_button("Click to Download", report, file_name=f"{candidate}_report.txt")

# Dynamic Governance Algorithm
st.header("Dynamic Governance Checklist")
bias_penalty = min(25, max(0, int(bias_gap * 100 - 5)))
data_anonymity = 0 if any(data['Name'].str.contains(r'[A-Za-z]')) else 1
audit_status = st.radio("Audit Status", ["Pending", "Completed"])
sensitive_data = st.radio("Sensitive Data Stored?", ["No", "Yes"])
max_score = 100
base_score = 50
bias_score = max(0, 25 - bias_penalty)
anonymity_score = 15 if data_anonymity == 1 else 0
audit_score = 20 if audit_status == "Completed" else 5
sensitive_score = 15 if sensitive_data == "No" else 0
governance_score = base_score + bias_score + anonymity_score + audit_score + sensitive_score
governance_score = max(0, min(100, governance_score))
st.write("**Governance Criteria:**")
st.write(f"✅ Data Anonymity: {'Achieved' if data_anonymity == 1 else 'Failed (Names detected)'}")
st.write(f"⚠️ Audit Status: {audit_status}")
st.write(f"✅ Sensitive Data: {'Not Stored' if sensitive_data == 'No' else 'Stored'}")
st.write(f"Bias Level Impact: {'High' if bias_gap > 0.2 else 'Moderate' if bias_gap > 0.1 else 'Low'}")
st.write(f"**Governance Score: {governance_score}%**")
st.progress(governance_score / 100)
if governance_score < 90:
    st.warning("Recommendations:")
    if bias_gap > 0.2:
        st.write("- Reduce bias by reweighting the hiring algorithm.")
    if audit_status == "Pending":
        st.write("- Schedule an audit to improve compliance.")
    if data_anonymity == 0:
        st.write("- Anonymize names (e.g., use IDs) to improve governance.")
    if sensitive_data == "Yes":
        st.write("- Remove sensitive data storage.")
    if governance_score < 70:
        st.write("- Conduct a full policy review.")

# AI-Powered Bias Prediction
st.header("AI-Powered Bias Prediction")
st.write("Predict hiring probability for a new candidate:")

# Prepare data for ML
X = data[['Score', 'Gender']].replace({'M': 0, 'F': 1})
y = data['Hired'].replace({'Y': 1, 'N': 0})
model = LogisticRegression()
model.fit(X, y)

# User Input
new_score = st.number_input("New Candidate Score", min_value=50, max_value=100, value=80)
new_gender = st.selectbox("New Candidate Gender", ['M', 'F'])
gender_encoded = 0 if new_gender == 'M' else 1

# Predict
if st.button("Predict"):
    prediction = model.predict_proba([[new_score, gender_encoded]])[0]
    hire_probability = prediction[1]  # Probability of being hired
    st.write(f"Predicted Hiring Probability: {hire_probability:.2%}")
    avg_male_prob = model.predict_proba([[new_score, 0]])[0][1]
    avg_female_prob = model.predict_proba([[new_score, 1]])[0][1]
    if gender_encoded == 1 and hire_probability < avg_male_prob - 0.1:
        st.warning(f"Bias Risk: Female hiring probability ({hire_probability:.2%}) is significantly lower than male ({avg_male_prob:.2%}).")

# Note
st.write("Note: Model trained on current data. Add diverse data for better accuracy.")