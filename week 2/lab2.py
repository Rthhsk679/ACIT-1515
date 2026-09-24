num_entries = float(input("Log entries per second: "))
entry_size = float(input("Average size of log entries in bytes: "))

KB = 1024
MB = 1048576
GB = 1073741824

unit = KB
time = 60 #time in seconds
kb_size = (num_entries * time * entry_size) / unit
print("Storage Estimates")
print(f"Per minute: {kb_size} KB")

unit = MB
time = 3600
kb_size = (num_entries * time * entry_size) / unit
print(f"Per hour: {kb_size} MB")

unit = GB
time = 86400
kb_size = (num_entries * time * entry_size) / unit
print(f"Per day: {kb_size} GB")