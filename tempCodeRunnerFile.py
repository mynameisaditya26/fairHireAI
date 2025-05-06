# Bias Detection
# bias_check = data.groupby('Gender')['Hired'].value_counts(normalize=True).unstack()
# male_hired = bias_check.loc['M', 'Y']
# female_hired = bias_check.loc['F', 'Y']
# bias_gap = abs(male_hired - female_hired)

# st.write("Bias Detection:")
# st.write(f"Male Hired: {male_hired:.2%}")
# st.write(f"Female Hired: {female_hired:.2%}")
# st.write(f"Bias Gap: {bias_gap:.2%}")

# import matplotlib.pyplot as plt

# # Bar Chart
# st.write("Fairness Chart:")
# fig, ax = plt.subplots()
# ax.bar(['Male', 'Female'], [male_hired, female_hired], color=['blue', 'orange'])
# plt.ylabel("Hiring Rate")
# st.pyplot(fig)

# # Alert
# if bias_gap > 0.1:
#     st.error("Bias Detected!")
# else:
#     st.success("Model is Fair!")


# st.write("Candidate Insights:")
# candidate = st.selectbox("Select Candidate", data['Name'])
# selected_data = data[data['Name'] == candidate].iloc[0]
# st.write(f"Name: {candidate}")
# st.write(f"Score: {selected_data['Score']}")
# st.write(f"Hired: {selected_data['Hired']}")

# # Dummy explanation
# if selected_data['Hired'] == 'Y':
#     reason = "Score above threshold (80)."
# else:
#     reason = "Score below threshold (80). Missing key skills."
# st.write(f"Reason: {reason}")
# st.write("Governance Checklist:")
# st.write("✅ Data Anonymized")
# st.write("✅ GDPR Compliant")
# st.write("⚠️ Audit Pending")
# st.write("✅ No Sensitive Data Stored")
# governance_score = 90
# st.write(f"Governance Rating: {governance_score}%")
# st.progress(governance_score)

# col1, col2, col3 = st.columns(3)
# with col1:
#     st.write("Bias Detection:")
#     st.write(f"Male Hired: {male_hired:.2%}")
#     st.write(f"Female Hired: {female_hired:.2%}")
#     st.pyplot(fig)
# with col2:
#     st.write("Candidate Insights:")
#     st.write(f"Name: {candidate}")
#     st.write(f"Score: {selected_data['Score']}")
#     st.write(f"Reason: {reason}")
# with col3:
#     st.write("Governance Checklist:")
#     st.write("✅ Data Anonymized")
#     st.write(f"Rating: {governance_score}%")

  