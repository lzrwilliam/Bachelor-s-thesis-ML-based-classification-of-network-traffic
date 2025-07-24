import pandas as pd
from sklearn.model_selection import train_test_split


data = pd.read_csv("all_data.csv")


y = data["Label"]


y = y.replace({
    "Heartbleed": "Rare Events",
    "Infiltration": "Rare Events",
    "Web Attack - Brute Force": "Web Attack",
    "Web Attack - XSS": "Web Attack",
    "Web Attack - Sql Injection": "Web Attack"
})


rf_features = [
    "Init_Win_bytes_backward", "Init_Win_bytes_forward", "min_seg_size_forward", "Fwd IAT Mean",
    "Average Packet Size", "Fwd Packet Length Max", "Flow IAT Mean", "Bwd Packets/s",
    "Flow IAT Std", "Subflow Fwd Bytes", "Bwd Packet Length Max", "Total Length of Fwd Packets",
    "Flow Duration", "Avg Fwd Segment Size", "Packet Length Mean", "Bwd Header Length",
    "Subflow Bwd Bytes", "Avg Bwd Segment Size", "Flow IAT Max", "Fwd IAT Total"
]

xgb_features = [
    "PSH Flag Count", "Idle Mean", "Total Length of Fwd Packets", "Bwd Packet Length Std",
    "Fwd Packet Length Min", "Total Fwd Packets", "Fwd URG Flags", "act_data_pkt_fwd",
    "Fwd Packet Length Std", "Flow Bytes/s", "Bwd Packets/s", "Total Length of Bwd Packets",
    "Bwd Packet Length Mean", "Average Packet Size", "FIN Flag Count", "Active Std",
    "Total Backward Packets", "Fwd PSH Flags", "Packet Length Mean", "Fwd Packet Length Max",
    "Max Packet Length", "Init_Win_bytes_forward", "Fwd Header Length", "Min Packet Length",
    "Init_Win_bytes_backward", "Bwd Header Length", "Idle Max", "Flow IAT Max",
    "Fwd Packet Length Mean", "min_seg_size_forward", "Bwd IAT Mean", "Packet Length Std",
    "Active Mean", "Packet Length Variance", "Fwd IAT Total", "Fwd IAT Min",
    "Fwd IAT Mean", "ACK Flag Count", "Bwd Packet Length Max", "Flow IAT Std"
]

dense_features = [
    "Flow ID", "Source IP", "Source Port", "Destination IP", "Destination Port", "Protocol",
    "Flow Duration", "Total Fwd Packets", "Total Backward Packets", "Total Length of Fwd Packets",
    "Total Length of Bwd Packets", "Fwd Packet Length Max", "Fwd Packet Length Min",
    "Fwd Packet Length Mean", "Fwd Packet Length Std", "Bwd Packet Length Max", "Bwd Packet Length Min",
    "Bwd Packet Length Mean", "Bwd Packet Length Std", "Flow Bytes/s", "Flow Packets/s",
    "Flow IAT Mean", "Flow IAT Std", "Flow IAT Max", "Flow IAT Min", "Fwd IAT Total",
    "Fwd IAT Mean", "Fwd IAT Std", "Fwd IAT Max", "Fwd IAT Min", "Bwd IAT Total",
    "Bwd IAT Mean", "Bwd IAT Std", "Bwd IAT Max", "Bwd IAT Min", "Fwd PSH Flags", "Bwd PSH Flags",
    "Fwd URG Flags", "Bwd URG Flags", "Fwd Header Length", "Bwd Header Length", "Fwd Packets/s",
    "Bwd Packets/s", "Min Packet Length", "Max Packet Length", "Packet Length Mean",
    "Packet Length Std", "Packet Length Variance", "FIN Flag Count", "SYN Flag Count",
    "RST Flag Count", "PSH Flag Count", "ACK Flag Count", "URG Flag Count", "CWE Flag Count",
    "ECE Flag Count", "Down/Up Ratio", "Average Packet Size", "Avg Fwd Segment Size",
    "Avg Bwd Segment Size", "Fwd Avg Bytes/Bulk", "Fwd Avg Packets/Bulk", "Fwd Avg Bulk Rate",
    "Bwd Avg Bytes/Bulk", "Bwd Avg Packets/Bulk", "Bwd Avg Bulk Rate", "Subflow Fwd Packets",
    "Subflow Fwd Bytes", "Subflow Bwd Packets", "Subflow Bwd Bytes", "Init_Win_bytes_forward",
    "Init_Win_bytes_backward", "act_data_pkt_fwd", "min_seg_size_forward", "Active Mean",
    "Active Std", "Active Max", "Active Min", "Idle Mean", "Idle Std", "Idle Max", "Idle Min"
]

# unim features fara duplicate
all_features = sorted(set(rf_features + xgb_features + dense_features))


missing = [feat for feat in all_features if feat not in data.columns]
if missing:
    print("⚠️ Următoarele coloane lipsesc din all_data.csv:", missing)
else:
    print("✅ Toate coloanele necesare sunt prezente.")

# Extragem subsetul de date pentru toate feature-urile si eticheta
X = data[all_features]
X['Label'] = y

# Split 70/30 
_, test_df = train_test_split(X, test_size=0.3, stratify=y, random_state=42)


test_df.to_csv("test_data.csv", index=False)
print("✅ Fișierul test_data.csv a fost generat cu succes.")
