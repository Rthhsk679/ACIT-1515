num_entries = float(input("Log entries per second: "))
entry_size = float(input("Average size of log entries in bytes: "))

KB = 1024
MB = 1048576
GB = 1073741824

value = 0

unit = KB
time = 60 #time in seconds
def increaseMagnitude(value, magnitude):
    if magnitude == "GB":
        for i in range(3):
        value = value / 1024
        return value
    if magnitude == "MB":
        for i in range(2):
        value = value / 1024
        return value
    if magnitude == "KB":
        value = value / 1024
        return value

targetsize = input("input target magnitude (GB, MB, KB): ")

print(increaseMagnitude(entry_size, targetsize))
# kb_size = (num_entries * time * entry_size) / unit
# print("Storage Estimates")
# print(f"Per minute: {kb_size} KB")

# unit = MB
# time = 3600
# kb_size = (num_entries * time * entry_size) / unit
# print(f"Per hour: {kb_size} MB")

# unit = GB
# time = 86400
# kb_size = (num_entries * time * entry_size) / unit
# print(f"Per day: {kb_size} GB")

